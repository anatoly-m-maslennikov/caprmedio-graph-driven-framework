# CA-R-1105@26
# CA-M-167@22
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
from mcp.shared.exceptions import NoBackChannelError

from ATOM_LIFECYCLE import backend, status_model


_FIELDS = {'role', 'form', 'scope_unit', 'container', 'summary', 'body', 'label', 'tier',
           'topics', 'relations', 'priority', 'work_sequence_number',
           'ai_agent_confidence_threshold'}
_INPUTS = {
    'atom_lifecycle_create_draft': {'newAtom', 'sourceCurrent', 'changes'},
    'atom_lifecycle_archive': {'target'},
    'atom_lifecycle_change_status': {'target', 'targetStatus'},
    'atom_lifecycle_direct_update': {'target', 'changes'},
    'atom_lifecycle_promote_draft': {'target', 'targetStatus'},
    'atom_lifecycle_update': {'sourceCurrent', 'changes'},
}
_EDITABLE = frozenset({'atom_lifecycle_create_draft', 'atom_lifecycle_direct_update', 'atom_lifecycle_update'})
_SESSION = object()
_FORM_TYPES = {
    **dict.fromkeys(('role', 'form', 'scope_unit', 'summary', 'body', 'label', 'priority', 'targetStatus'), 'string'),
    **dict.fromkeys(('tier', 'work_sequence_number', 'ai_agent_confidence_threshold'), 'integer'),
}
_FORM_VALUES = {'string': str, 'integer': int}
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


def _correction_schema(session, requested, correctable):
    caps = getattr(session, 'client_capabilities', None)
    elicitation = caps.elicitation if caps else None
    if (elicitation is None or (elicitation.form is None and elicitation.url is not None)
            or set(correctable) - _FORM_TYPES.keys() or len(correctable) != len(requested)):
        return None
    properties = {}
    for field, detail in correctable.items():
        form_type = _FORM_TYPES[field]
        prop = {'type': form_type, 'description': detail.get('error', '')}
        allowed = detail.get('allowed_values')
        if form_type == 'string' and allowed and all(isinstance(item, str) for item in allowed):
            prop['enum'] = allowed
        properties[field] = prop
    return {'type': 'object', 'properties': properties, 'required': list(properties)}


async def _request_correction(session, request_id, requested, correctable):
    schema = _correction_schema(session, requested, correctable)
    if schema is None:
        return None
    try:
        return await session.elicit_form(
            'Correct the requested fields to continue the lifecycle operation.',
            schema, related_request_id=request_id,
        )
    except NoBackChannelError:
        return None


def _valid_correction(correction, fields):
    return (isinstance(correction, dict) and correction.keys() == fields.keys()
            and all(type(value) is _FORM_VALUES[_FORM_TYPES[key]] for key, value in correction.items()))


def _promotion_requested(requested):
    result = {('targetStatus' if field == 'status' else field): detail
              for field, detail in requested.items() if field in {'target', 'targetStatus', 'status'}}
    other = [f"{field}: {detail.get('error', '')}" for field, detail in requested.items()
             if field not in {'target', 'targetStatus', 'status'}]
    if other:
        existing = result.get('target', {}).get('error', '')
        result['target'] = {'error': '; '.join(filter(None, [existing, *other])),
                            'format': 'Resolve the reported issue, then resume with the bound Draft selector'}
    return result


async def _promotion_correction(value, session, request_id):
    promotion = {'token': value['pending_promotion'], 'effects': value.get('effects', []),
                 'warnings': value.get('warnings', [])}
    requested = _promotion_requested(value.get('requested_input', {}))
    answer = (await _request_correction(session, request_id, requested, requested)
              if requested and set(requested) <= {'targetStatus'} else None)
    if answer is None:
        return promotion, None, {'status': 'needs_input', 'requested_input': requested,
                                 'effects': promotion['effects'], 'warnings': promotion['warnings']}
    if answer.action != 'accept':
        return promotion, None, {'status': 'cancelled', 'effects': promotion['effects'],
                                 'warnings': promotion['warnings']}
    if not _valid_correction(answer.content, requested):
        return promotion, None, {'status': 'failed', 'effects': promotion['effects'],
                                 'warnings': promotion['warnings'], 'errors': [{'code': 'invalid_input',
                                 'message': 'Correction does not match the requested fields and types.'}]}
    return promotion, answer.content, None


async def _input_correction(name, value, params, source, session, request_id, state):
    requested = value.get('requested_input', {})
    correctable = _correctable(name, requested)
    if not correctable:
        return None, None, {'status': 'failed', 'errors': [
            {'code': 'invalid_input', 'field': field, 'message': detail.get('error')}
            for field, detail in requested.items()
        ]}
    source = value.get('pending_source') or source
    answer = await _request_correction(session, request_id, requested, correctable)
    if answer is None:
        state['pending'], state['source'] = params, source
        return None, None, {'status': 'needs_input', 'requested_input': correctable}
    if answer.action != 'accept':
        return None, None, {'status': 'cancelled'}
    if not _valid_correction(answer.content, correctable):
        return None, None, {'status': 'failed', 'errors': [{'code': 'invalid_input',
                            'message': 'Correction does not match the requested fields and types.'}]}
    return _parameters(name, params, answer.content), source, None


def _execution(source, promotion):
    if promotion:
        return partial(backend.execute, pending_promotion=promotion['token'])
    return backend.execute if source is None else partial(backend.execute, pending_source=source)


def _result(value):
    if value.get('outcome') == 'completed' and not value.get('errors'):
        return {'status': 'completed'}
    failure = {'status': 'failed', 'effects': value.get('effects', []),
               'errors': value.get('errors', []), 'warnings': value.get('warnings', [])}
    if 'remaining_targets' in value:
        failure['remaining_targets'] = value['remaining_targets']
    return failure


class LifecycleProvider:
    def __init__(self, gateway, model):
        self.selection = gateway.selection
        if self.selection is None:
            raise ValueError('Lifecycle requires an exact Project selection')
        self.model = model
        self.project = (self.selection.root, self.selection.instance_id)

    def prepare_arguments(self, name, arguments, context):
        session = getattr(context, 'session', None)
        if not isinstance(session, ServerSession):
            raise ValueError('Lifecycle requires an MCP ServerSession')
        # SDK ServerSession is request-scoped; its Connection is transport-scoped.
        connection = getattr(session, '_connection', None)
        if not isinstance(connection, Connection):
            raise ValueError('Lifecycle requires an MCP connection')
        return {**arguments, _SESSION: (connection, session, getattr(context, 'request_id', None))}

    async def call(self, name, arguments):
        if name not in _INPUTS:
            raise ValueError('Unknown lifecycle Tool')
        arguments = dict(arguments)
        connection, session, request_id = arguments.pop(_SESSION)
        projects = _PENDING.setdefault(connection, {})
        tools = projects.setdefault(self.project, {})
        state = tools.setdefault(name, {'lock': asyncio.Lock(), 'pending': None, 'source': None, 'promotion': None})
        async with state['lock']:
            promotion, state['promotion'] = state.get('promotion'), None
            if promotion:
                params, source = arguments, None
            else:
                params, source = _take_pending(name, state, arguments)
            while True:
                execute = _execution(source, promotion)
                # The Action owns its lifetime once dispatched; cancellation cannot interrupt effects.
                with anyio.CancelScope(shield=True):
                    value = await anyio.to_thread.run_sync(execute, self.selection, self.model, name, params)
                outcome = value.get('outcome')
                token = value.get('pending_promotion')
                if promotion and outcome == 'needs_input' and token is None:
                    return {'status': 'failed', 'effects': promotion['effects'], 'warnings': promotion['warnings'],
                            'errors': [{'code': 'invalid_state', 'message': 'Promotion continuation is unavailable.'}]}
                if outcome != 'needs_input' or (value.get('effects') and token is None):
                    break
                if token is not None:
                    promotion, params, response = await _promotion_correction(value, session, request_id)
                    if response is not None:
                        if response['status'] == 'needs_input':
                            state['promotion'] = promotion
                        return response
                else:
                    params, source, response = await _input_correction(
                        name, value, params, source, session, request_id, state)
                    if response is not None:
                        return response
            return _result(value)

    async def close(self):
        return None


def create_provider(_root, gateway):
    from ATOM_LIFECYCLE.candidate_schema import load_candidate_schema

    model = status_model.load_status_model(Path(status_model.__file__).with_suffix('.json'))
    path = Path(status_model.__file__).with_name('candidate_schema.json')
    return LifecycleProvider(gateway, replace(model, candidate_schema=load_candidate_schema(path)))


def tool_descriptors():
    return tuple(types.Tool(
        name=name, description='Execute a Project Atom Lifecycle operation. Missing or invalid fields are returned for correction.',
        input_schema={'type': 'object', 'properties': {key: {} for key in sorted(fields | (_FIELDS if name in _EDITABLE else set()) | ({'target', 'targetStatus'} if name == 'atom_lifecycle_update' else set()))},
                      'additionalProperties': False},
    ) for name, fields in _INPUTS.items())

