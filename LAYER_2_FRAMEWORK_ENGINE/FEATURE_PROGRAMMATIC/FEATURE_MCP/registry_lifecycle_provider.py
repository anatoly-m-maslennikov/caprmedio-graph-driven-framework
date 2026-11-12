# CA-R-1105@30
# CA-M-167@26
# CA-O-10004@3

"""Private MCP adapter for the Project Atom Lifecycle backend."""
from __future__ import annotations

import asyncio
from copy import deepcopy
from dataclasses import replace
from functools import partial
from pathlib import Path
from weakref import WeakKeyDictionary

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
    'atom_lifecycle_create_draft': {'newAtom', 'sourceCurrent', 'changes'},
    'atom_lifecycle_archive': {'target', 'targets'},
    'atom_lifecycle_change_status': {'target', 'targetStatus'},
    'atom_lifecycle_direct_update': {'target', 'changes'},
    'atom_lifecycle_promote_draft': {'target', 'targetStatus', 'targets'},
    'atom_lifecycle_update': {'sourceCurrent', 'changes'},
}
_EDITABLE = frozenset({'atom_lifecycle_create_draft', 'atom_lifecycle_direct_update', 'atom_lifecycle_update'})
_SESSION = object()
_PENDING = WeakKeyDictionary()


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


def _parameters(name, retained, arguments):
    retained = deepcopy(retained)
    if name == 'atom_lifecycle_create_draft':
        old, new = retained.get('sourceCurrent'), arguments.get('sourceCurrent')
        if isinstance(old, dict) and isinstance(new, dict) and 'ref_id' in new and new['ref_id'] != old.get('ref_id'):
            retained.pop('sourceCurrent')
        elif isinstance(old, str) and isinstance(new, dict) and 'ref_id' not in new:
            retained['sourceCurrent'] = {'ref_id': old}
    if (name == 'atom_lifecycle_create_draft' and 'newAtom' in retained
            and ('sourceCurrent' in retained or 'changes' in retained)):
        selected = {'newAtom', 'sourceCurrent'} & arguments.keys()
        if selected == {'newAtom'}:
            retained.pop('sourceCurrent', None)
            retained.pop('changes', None)
        elif selected == {'sourceCurrent'}:
            retained.pop('newAtom', None)
    params = _merge(retained, {key: value for key, value in arguments.items() if key not in _FIELDS})
    logical = {key: value for key, value in arguments.items() if key in _FIELDS}
    if logical:
        group = ('newAtom' if name == 'atom_lifecycle_create_draft'
                 and ('newAtom' in params or 'sourceCurrent' not in params) else 'changes')
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


def _cancel_pending(arguments, state):
    cancel = arguments.pop('cancel', False)
    if not isinstance(cancel, bool) or (cancel and arguments):
        return {'status': 'failed', 'errors': [{'code': 'invalid_input', 'field': 'cancel',
                 'message': 'Use cancel=true without other fields.'}]}
    if not cancel:
        return None
    if state['pending'] is None:
        return {'status': 'failed', 'errors': [{'code': 'no_pending_input', 'field': 'cancel',
                 'message': 'No input is pending for this tool.'}]}
    state.update(pending=None, source=None, declaration_digest=None)
    return {'status': 'cancelled'}


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
        return {'status': 'completed', **workflow}
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
        # SDK ServerSession is request-scoped; its Connection is transport-scoped.
        connection = getattr(session, '_connection', None)
        if not isinstance(connection, Connection):
            raise ValueError('Lifecycle requires an MCP connection')
        return {**arguments, _SESSION: connection}

    async def call(self, name, arguments):
        if name not in _INPUTS:
            raise ValueError('Unknown lifecycle Tool')
        arguments = dict(arguments)
        connection = arguments.pop(_SESSION)
        projects = _PENDING.setdefault(connection, {})
        tools = projects.setdefault(self.project, {})
        state = tools.setdefault(name, {'lock': asyncio.Lock(), 'pending': None, 'source': None})
        async with state['lock']:
            cancelled = _cancel_pending(arguments, state)
            if cancelled is not None:
                return cancelled
            try:
                with span('refresh_project', tool=name, selection=self.selection):
                    selection = await anyio.to_thread.run_sync(self._select_project)
            except (OSError, RuntimeError, ValueError):
                state.update(pending=None, source=None, declaration_digest=None)
                return {'status': 'failed', 'effects': [], 'warnings': [],
                        'errors': [{'code': 'source_selection_failed',
                                    'message': 'Current Project declarations are unavailable or invalid.'}]}
            if state['pending'] is not None and state['declaration_digest'] != selection.declaration_digest:
                state.update(pending=None, source=None, declaration_digest=None)
                return {'status': 'failed', 'effects': [], 'warnings': [],
                        'errors': [{'code': 'source_changed',
                                    'message': 'Project declarations changed while input was pending.'}]}
            batch = name in {'atom_lifecycle_archive', 'atom_lifecycle_promote_draft'} and 'targets' in arguments
            if batch:
                state.update(pending=None, source=None, declaration_digest=None)
            params, source = _take_pending(name, state, arguments)
            value = await self._run(selection, name, params, source)
            if batch:
                return _result(value, batch=True)
            if value.get('outcome') != 'needs_input' or value.get('effects'):
                return _result(value)
            return _input_correction(name, value, params, source, state, selection.declaration_digest)

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
        result['cancel'] = {'type': 'boolean', 'description': 'Cancel this tool’s pending input without executing it.'}
        if name == 'atom_lifecycle_create_draft':
            result['sourceCurrent'] = {'description': 'An Atom ID string or {"ref_id": "CA-R-123", '
                                       '"version": 2}, with optional positive integer version. '
                                       'Without a version, select Current. An exact version can select '
                                       'Current, Archived or Draft.'}
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
                      'additionalProperties': False},
    ) for name, fields in _INPUTS.items())

