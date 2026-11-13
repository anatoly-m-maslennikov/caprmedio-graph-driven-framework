# CA-R-1105@32
# CA-R-3016@2
# CA-R-3080@2
# CA-M-167@27
# CA-O-10004@3

"""Private MCP adapter for the Project Atom Lifecycle backend."""
from __future__ import annotations

import asyncio
import threading
from copy import deepcopy
from dataclasses import replace
from functools import partial
from pathlib import Path
from weakref import WeakKeyDictionary
from uuid import uuid4

from runtime_request_context import current_request_context

import anyio
from mcp import types
from mcp.server.session import ServerSession
from mcp.server.connection import Connection

from ATOM_LIFECYCLE import backend, source as lifecycle_source, status_model
from ATOM_LIFECYCLE.timing import span
from project_selection import bind_selection, rebind_selection, resolve_project
from scope_unit_declarations import ScopeUnitDeclarations


_FIELDS = {'role', 'form', 'scope_unit', 'container', 'summary', 'body', 'label', 'tier',
           'topics', 'relations', 'priority', 'work_sequence_number',
           'ai_agent_confidence_threshold'}
_INPUTS = {
    'atom_lifecycle_create_draft': {'newAtom', 'sourceCurrent', 'copyFrom', 'changes'},
    'atom_lifecycle_archive': {'target', 'targets'},
    'atom_lifecycle_change_status': {'target', 'targetStatus'},
    'atom_lifecycle_direct_update': {'target', 'changes'},
    'atom_lifecycle_promote_draft': {'target', 'targetStatus', 'targets'},
    'atom_lifecycle_update': {'sourceCurrent', 'changes'},
}
_EDITABLE = frozenset({'atom_lifecycle_create_draft', 'atom_lifecycle_direct_update', 'atom_lifecycle_update'})
_SESSION = object()
_CONNECTION_IDS = WeakKeyDictionary()
_PROJECT_RUNS = {}
_PROJECT_RUNS_LOCK = threading.RLock()
_RUN_TOOLS = {'lifecycle_run_list', 'lifecycle_run_continue', 'lifecycle_run_cancel'}


def live_runs_snapshot(project, session_id=None):
    with _PROJECT_RUNS_LOCK:
        return [{'run_id': ident, 'session_id': run['session_id'],
                 'tool': run['name'], 'status': run['status']}
                for ident, run in _PROJECT_RUNS.get(project, {}).items()
                if session_id is None or run['session_id'] == session_id]


def _remove_run(runs, run_id):
    with _PROJECT_RUNS_LOCK:
        del runs[run_id]


def _merge(original, correction):
    result = deepcopy(original)
    for key, value in correction.items():
        if isinstance(value, dict) and isinstance(result.get(key), dict):
            result[key] = _merge(result[key], value)
        else:
            result[key] = deepcopy(value)
    return result


def _correctable(name, requested):
    editable = name in _EDITABLE
    aliases = {'changes.body': 'body', 'container.scope_unit': 'scope_unit', 'container.atom': 'container',
               'topics.main_subject': 'topics', 'topics.dependencies': 'topics'} if editable else {}
    if 'targetStatus' in _INPUTS[name]:
        aliases['status'] = 'targetStatus'
    fields = _INPUTS[name] | (_FIELDS if editable else set())
    return {
        aliases.get(field, field): detail
        for field, detail in requested.items()
        if aliases.get(field, field) in fields
    }


def _draft_source_corrections(retained, arguments):
    for field in ('sourceCurrent', 'copyFrom'):
        old, new = retained.get(field), arguments.get(field)
        if field == 'copyFrom':
            old_ref = old.get('ref_id') if isinstance(old, dict) else old
            new_ref = new.get('ref_id') if isinstance(new, dict) else new
            if (isinstance(old_ref, str) and isinstance(new_ref, str)
                    and old_ref.split('@', 1)[0] != new_ref.split('@', 1)[0]):
                retained.pop('changes', None)
        if isinstance(old, dict) and isinstance(new, dict) and 'ref_id' in new and new['ref_id'] != old.get('ref_id'):
            retained.pop(field)
        elif isinstance(old, str) and isinstance(new, dict) and 'ref_id' not in new:
            retained[field] = {'ref_id': old}
    sources = {'newAtom', 'sourceCurrent', 'copyFrom'}
    selected = sources & arguments.keys()
    if len(selected) == 1:
        field = next(iter(selected))
        changed_source_kind = bool((sources - {field}) & retained.keys())
        for other in sources - {field}:
            retained.pop(other, None)
        if field == 'newAtom' or changed_source_kind:
            retained.pop('changes', None)


def _parameters(name, retained, arguments):
    retained = deepcopy(retained)
    if name == 'atom_lifecycle_create_draft':
        _draft_source_corrections(retained, arguments)
    params = _merge(retained, {key: value for key, value in arguments.items() if key not in _FIELDS})
    logical = {key: value for key, value in arguments.items() if key in _FIELDS}
    if logical:
        group = ('newAtom' if name == 'atom_lifecycle_create_draft'
                 and ('newAtom' in params or not {'sourceCurrent', 'copyFrom'} & params.keys()) else 'changes')
        existing = params.get(group)
        params[group] = _merge(existing if isinstance(existing, dict) else {}, logical)
    return params


def _take_pending(name, state, arguments):
    pending, state['pending'] = state['pending'] or {}, None
    source, state['source'] = state['source'], None
    params = _parameters(name, pending, arguments)
    if source is not None and params.get('sourceCurrent') != pending.get('sourceCurrent'):
        # A new source selection must not inherit another Atom's changes or pin.
        return _parameters(name, {}, arguments), None
    return params, source


def _input_correction(name, value, params, source, state, declaration_digest):
    requested = value.get('requested_input', {})
    correctable = _correctable(name, requested)
    errors = [{'code': 'invalid_input', 'field': field, 'message': detail.get('error')}
              for field, detail in requested.items()]
    if not correctable:
        return {'status': 'failed', 'errors': errors}
    state.update(pending=params, source=value.get('pending_source') or source,
                 declaration_digest=declaration_digest)
    return {'status': 'needs_input', 'requested_input': correctable, 'errors': errors}


def _result(value, *, batch=False):
    if batch:
        response = {'status': 'completed' if value.get('outcome') == 'completed' and not value.get('errors') else 'failed'}
        if 'target_results' in value:
            response['results'] = value['target_results']
        for key in ('remaining_targets', 'effects', 'errors', 'warnings'):
            if key in value:
                response[key] = value[key]
        if response['status'] == 'failed' and not response.get('errors'):
            response['errors'] = [
                {'code': 'invalid_input', 'field': field, 'message': detail.get('error')}
                for field, detail in value.get('requested_input', {}).items()
            ] or [{'code': 'backend_failure', 'message': 'Lifecycle operation failed.'}]
        return response
    workflow = {}
    if 'workflow_binding' in value:
        fields = ('workflow_binding', 'workflow_run_id', 'action_results', 'artifact', 'effects', 'warnings',
                  'failed_action', 'unrun_actions')
        workflow = {key: value[key] for key in fields if key in value}
    if value.get('outcome') == 'completed' and not value.get('errors'):
        if len(workflow.get('action_results', ())) > 1:
            return {'status': 'completed', **workflow}
        return {'status': 'completed'}
    errors = value.get('errors') or [
        {'code': 'invalid_input', 'field': field, 'message': detail.get('error')}
        for field, detail in value.get('requested_input', {}).items()
    ] or [{'code': 'backend_failure', 'message': 'Lifecycle operation failed.'}]
    status = 'blocked' if value.get('outcome') == 'blocked' else 'failed'
    failure = {'status': status, 'effects': value.get('effects', []),
               'errors': errors, 'warnings': value.get('warnings', []), **workflow}
    if 'remaining_targets' in value:
        failure['remaining_targets'] = value['remaining_targets']
    return failure


def _refresh_selection(selection, reader=None):
    if reader is not None:
        declarations = reader.lifecycle_declarations()
        if not isinstance(declarations, ScopeUnitDeclarations):
            raise ValueError('Project declarations are unavailable or invalid in Workbench')
        if declarations.digest == selection.declaration_digest:
            return selection
        if (not declarations.paths or any(not path.is_absolute() or not path.is_relative_to(selection.control_root)
                                          for path in declarations.paths)
                or declarations.root.name != selection.settings['project']['name']):
            raise ValueError('Project declarations are unavailable or invalid in Workbench')
        provenance = {path: dict(pin) for path, pin in selection.provenance.items()
                      if path not in selection.declaration_source_pins}
        provenance.update({path: dict(pin) for path, pin in declarations.source_pins.items()})
        return replace(selection, structure=declarations.as_structure(), declaration_paths=declarations.paths,
                       declaration_source_pins=declarations.source_pins,
                       declaration_digest=declarations.digest, provenance=provenance)
    selection._revalidate_boundary()
    current = resolve_project(selection.root, selection.control_relative)
    return rebind_selection(current, selection.instance_id, host_root=selection.host_root)


class LifecycleProvider:
    def __init__(self, gateway, model):
        self.selection = gateway.selection
        if self.selection is None:
            raise ValueError('Lifecycle requires an exact Project selection')
        self.model = model
        self.project = (self.selection.root, self.selection.instance_id)
        self.workbench = getattr(gateway, 'workbench', None)

    def _select_project(self):
        if self.workbench is None:
            return _refresh_selection(self.selection)
        with self.workbench.lifecycle_reader() as reader:
            self.selection = _refresh_selection(self.selection, reader)
            return self.selection

    def _execute(self, execute, selection, name, params):
        if self.workbench is None:
            return execute(selection, self.model, name, params)
        with (self.workbench.lifecycle_reader() as reader,
              reader.lifecycle_read_scope(), lifecycle_source.bind_query_reader(reader),
              bind_selection(selection)):
            return execute(selection, self.model, name, params)

    def prepare_arguments(self, name, arguments, context):
        session = getattr(context, 'session', None)
        if not isinstance(session, ServerSession):
            raise ValueError('Lifecycle requires an MCP ServerSession')
        connection = getattr(session, '_connection', None)
        if not isinstance(connection, Connection):
            raise ValueError('Lifecycle requires an MCP connection')
        request = current_request_context()
        session_id = request.session_id if request else None
        if session_id is None:
            session_id = _CONNECTION_IDS.setdefault(connection, uuid4().hex)
        return {**arguments, _SESSION: (session_id, request is None or request.session_id is None)}

    async def call(self, name, arguments):
        if name not in _INPUTS and name not in _RUN_TOOLS:
            raise ValueError('Unknown lifecycle Tool')
        arguments = dict(arguments)
        session_id, legacy = arguments.pop(_SESSION)
        runs = _PROJECT_RUNS.setdefault(self.project, {})
        if name == 'lifecycle_run_list':
            project_wide = arguments.get('project_wide', False)
            if set(arguments) - {'project_wide'} or not isinstance(project_wide, bool):
                return self._invalid('project_wide', 'Expected a boolean.')
            return {'runs': live_runs_snapshot(self.project, None if project_wide else session_id)}
        if legacy and name in _INPUTS:
            waiting = [ident for ident, item in runs.items() if item['session_id'] == session_id
                       and item['name'] == name and item['status'] == 'needs_input']
            cancel = arguments.pop('cancel', False)
            if not isinstance(cancel, bool) or (cancel and arguments):
                return self._invalid('cancel', 'Use cancel=true without other fields.')
            if cancel:
                if len(waiting) != 1:
                    return {'status': 'failed', 'errors': [{'code': 'no_pending_input', 'field': 'cancel',
                            'message': 'No unique input is pending for this tool.'}]}
                _remove_run(runs, waiting[0])
                return {'status': 'cancelled'}
            if len(waiting) == 1:
                if 'targets' in arguments and name in {'atom_lifecycle_archive', 'atom_lifecycle_promote_draft'}:
                    _remove_run(runs, waiting[0])
                else:
                    arguments = {'run_id': waiting[0], 'inputs': arguments}
                    name = 'lifecycle_run_continue'
        continuing = name in {'lifecycle_run_continue', 'lifecycle_run_cancel'}
        if continuing:
            run_id = arguments.pop('run_id', None)
            run = runs.get(run_id) if isinstance(run_id, str) else None
            if run is None or run['status'] != 'needs_input':
                return self._invalid('run_id', 'Unknown, terminal, or unavailable Run.')
            if name == 'lifecycle_run_cancel':
                if arguments:
                    return self._invalid(next(iter(arguments)), 'Unexpected field.')
                _remove_run(runs, run_id)
                return {'status': 'cancelled'}
            corrections = arguments.pop('inputs', {})
            if arguments or not isinstance(corrections, dict):
                return self._invalid('inputs', 'Expected an object of correction fields.')
            name = run['name']
            arguments = corrections
        else:
            run_id = uuid4().hex
            run = {'name': name, 'session_id': session_id, 'status': 'running',
                   'pending': None, 'source': None, 'declaration_digest': None, 'targets': set()}
            with _PROJECT_RUNS_LOCK:
                runs[run_id] = run
        unknown = set(arguments) - _INPUTS[name] - (_FIELDS if name in _EDITABLE else set())
        valid_arguments = {k: v for k, v in arguments.items() if k not in unknown}
        previous = {key: run[key] for key in ('pending', 'source', 'targets')}
        params, source = _take_pending(name, run, valid_arguments)
        targets = self._targets(name, params)
        if any(targets & other['targets'] for ident, other in runs.items() if ident != run_id):
            if continuing:
                run.update(previous)
            else:
                _remove_run(runs, run_id)
            return {'status': 'blocked', 'effects': [], 'warnings': [],
                    'errors': [{'code': 'live_run_conflict', 'message': 'A live Run already targets this Atom.'}]}
        run['targets'] = targets
        if unknown:
            with _PROJECT_RUNS_LOCK:
                run.update(status='needs_input', pending=params, source=source)
            return {'status': 'needs_input', 'run_id': run_id,
                    'requested_input': {}, 'errors': [{'code': 'invalid_input', 'field': k,
                    'message': 'Unknown field.'} for k in sorted(unknown)]}
        with _PROJECT_RUNS_LOCK:
            run['status'] = 'running'
        try:
            with span('refresh_project', tool=name, selection=self.selection):
                selection = await anyio.to_thread.run_sync(self._select_project)
        except (OSError, RuntimeError, ValueError):
            _remove_run(runs, run_id)
            return {'status': 'failed', 'effects': [], 'warnings': [],
                    'errors': [{'code': 'source_selection_failed',
                                'message': 'Current Project declarations are unavailable or invalid.'}]}
        except BaseException:
            _remove_run(runs, run_id)
            raise
        if run['declaration_digest'] is not None and run['declaration_digest'] != selection.declaration_digest:
            _remove_run(runs, run_id)
            return {'status': 'failed', 'effects': [], 'warnings': [],
                    'errors': [{'code': 'source_changed',
                                'message': 'Project declarations changed while input was pending.'}]}
        batch = name in {'atom_lifecycle_archive', 'atom_lifecycle_promote_draft'} and 'targets' in params
        try:
            value = await self._run(selection, name, params, source)
        except BaseException:
            _remove_run(runs, run_id)
            raise
        if batch or value.get('outcome') != 'needs_input' or value.get('effects'):
            _remove_run(runs, run_id)
            return _result(value, batch=batch)
        result = _input_correction(name, value, params, source, run, selection.declaration_digest)
        if result['status'] == 'needs_input':
            with _PROJECT_RUNS_LOCK:
                run['status'] = 'needs_input'
            result['run_id'] = run_id
        else:
            _remove_run(runs, run_id)
        return result

    @staticmethod
    def _invalid(field, message):
        return {'status': 'failed', 'errors': [{'code': 'invalid_input', 'field': field, 'message': message}]}

    @staticmethod
    def _targets(name, params):
        selector = 'sourceCurrent' if name in {'atom_lifecycle_update', 'atom_lifecycle_create_draft'} else 'target'
        selectors = [params.get(selector)]
        if isinstance(params.get('targets'), list):
            selectors.extend(item.get('target') for item in params['targets'] if isinstance(item, dict))
        refs = [item.get('ref_id') if isinstance(item, dict) else item for item in selectors]
        return {ref.split('@', 1)[0] for ref in refs if isinstance(ref, str) and ref}

    async def _run(self, selection, name, params, source):
        execute = backend.execute if source is None else partial(backend.execute, pending_source=source)
        # An Action owns its lifetime once dispatched; cancellation cannot interrupt effects.
        with anyio.CancelScope(shield=True):
            return await anyio.to_thread.run_sync(self._execute, execute, selection, name, params)

    async def close(self):
        return None


def create_provider(_root, gateway):
    from ATOM_LIFECYCLE.candidate_schema import load_candidate_schema

    if getattr(gateway, 'workbench', None) is None:
        raise ValueError('Lifecycle requires the Project Workbench query backend')
    model = status_model.load_status_model(Path(status_model.__file__).with_suffix('.json'))
    path = Path(status_model.__file__).with_name('candidate_schema.json')
    return LifecycleProvider(gateway, replace(model, candidate_schema=load_candidate_schema(path)))


def tool_descriptors():
    def properties(name, fields):
        result = {key: {} for key in sorted(fields | (_FIELDS if name in _EDITABLE else set()))}
        result['cancel'] = {'type': 'boolean', 'description': 'For legacy clients, cancel the unique pending request.'}
        if name == 'atom_lifecycle_create_draft':
            result['sourceCurrent'] = {'description': 'An Atom ID string or {"ref_id": "CA-R-123", '
                                       '"version": 2}, with optional positive integer version. '
                                       'Without a version, select Current. An exact version can select '
                                       'Current, Archived or Draft.'}
            result['copyFrom'] = {'description': 'Copy the selected Atom as an independent Draft with a new '
                                  'Atom ID and Version 1. Select Current by ID, or give an exact Version '
                                  'or Draft reference. Use changes for fields to update.'}
        if 'targets' in fields:
            item_properties = {'target': {'type': 'object'}}
            if name == 'atom_lifecycle_promote_draft':
                item_properties['targetStatus'] = {'type': 'string'}
            result['targets'] = {'type': 'array', 'minItems': 1, 'items': {
                'type': 'object', 'properties': item_properties,
                'required': list(item_properties), 'additionalProperties': False}}
        return result

    return tuple(types.Tool(
        name=name, description=('Execute a Project Atom Lifecycle operation. Single inputs can be corrected; batches stop on failure.'
                                if 'targets' in fields else
                                'Execute a Project Atom Lifecycle operation. Missing or invalid fields are returned for correction.'),
        input_schema={'type': 'object', 'properties': properties(name, fields),
                      'additionalProperties': True},
    ) for name, fields in _INPUTS.items()) + (
        types.Tool(name='lifecycle_run_list', description='List live Runs in this session or Project.',
                   input_schema={'type': 'object', 'properties': {'project_wide': {'type': 'boolean'}}, 'additionalProperties': False}),
        types.Tool(name='lifecycle_run_continue', description='Continue a waiting Run by exact ID.',
                   input_schema={'type': 'object', 'properties': {'run_id': {'type': 'string'}, 'inputs': {'type': 'object'}}, 'required': ['run_id', 'inputs'], 'additionalProperties': False}),
        types.Tool(name='lifecycle_run_cancel', description='Cancel a waiting Run by exact ID.',
                   input_schema={'type': 'object', 'properties': {'run_id': {'type': 'string'}}, 'required': ['run_id'], 'additionalProperties': False}),
    )

