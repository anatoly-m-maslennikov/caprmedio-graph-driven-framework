"""DBOS is the durable scheduler; existing Run evidence remains the observed history."""
from collections.abc import Mapping
from concurrent.futures import CancelledError as FutureCancelledError
import json
from pathlib import Path
import signal
import sys
import threading

from contracts import Enqueue, EnqueueSelected, Status
from agent import CodexAgent
from engine import Coordinator, Interrupted, execute_phase, runtime_fingerprint
from runtime_config import control_directory, docker_runtime, implementation_mock_runtime
from runtime_failure_diagnostics import report_failure
from remote_agent import RemoteAgent
from selected_execution import SelectedExecution, canonical_json
from selected_native_providers import SelectedNativeProviders

APPLICATION = 'caprmedio-orchestrator'
QUEUE = 'base-revise'
WORKFLOW = 'rmed-atoms-base-revise-independent'
APP_VERSION = 'base-revise-v5-selected-v1-docker-project-mount'
SELECTED_WORKFLOW = 'selected-workflow-execution'
CONTAINER_LIFECYCLE_SCHEMA = 'container-lifecycle/v1'
CONTAINER_IDENTITY_KIND = 'technical_coordinator'


def _scheduler_identity():
    return {'application': APPLICATION, 'queue': QUEUE, 'app_version': APP_VERSION,
            'selected_workflow': SELECTED_WORKFLOW}


def database(root):
    engine = Coordinator(root, None)
    path = engine.store.path(f'{control_directory()}/dbos.sqlite')
    path.parent.mkdir(parents=True, exist_ok=True)
    return path, f'sqlite:///{path}'


def client(root):
    from dbos import DBOSClient
    path, url = database(root)
    if not path.is_file():
        raise RuntimeError('Start the explicit worker once to initialize its DBOS database')
    return DBOSClient(system_database_url=url, application_name=_scheduler_identity()['application'],
                      retry_connection_errors=False)


def enqueue(root, request):
    request = Enqueue.model_validate(request)
    engine = Coordinator(root, None)
    # Admission is protected against simultaneous clients claiming one ID.
    with engine.store._lock(request.run_id):
        engine.freeze(request)
        transport = client(root)
        try:
            transport.enqueue({'queue_name': QUEUE, 'workflow_name': WORKFLOW,
                               'workflow_id': request.run_id, 'app_version': APP_VERSION}, request.run_id)
        finally:
            transport.destroy()
    return status(root, Status(run_id=request.run_id))


def enqueue_selected(root, request):
    """Freeze a source-bound request before its explicit DBOS queue admission."""
    request = EnqueueSelected.model_validate(request)
    selected = SelectedExecution(root)
    scheduler = _scheduler_identity()
    _verify_container_lifecycle_seal(root, request.execution)
    # The selected coordinator cannot reinterpret Base Revise request.json state.
    frozen = selected.freeze(request.model_dump())
    transport = client(root)
    try:
        transport.enqueue({'queue_name': scheduler['queue'], 'workflow_name': scheduler['selected_workflow'],
                           'workflow_id': request.run_id, 'app_version': scheduler['app_version']}, request.run_id)
    finally:
        transport.destroy()
    response = status(root, Status(run_id=request.run_id))
    if _container_lifecycle_marker(frozen) is not None:
        response.pop('workflow_run_id', None)
        response.pop('workflow_id', None)
        response.update({'coordinator_id': request.run_id,
                         'identity_kind': CONTAINER_IDENTITY_KIND,
                         'selected_route': frozen['graph']['route'], 'disposition': 'queued'})
    else:
        response.update({'workflow_id': frozen['graph']['workflow']['atom_id'],
                         'selected_route': frozen['graph']['route'], 'disposition': 'queued'})
    return response


def _container_lifecycle_marker(frozen):
    """Return the sealed container marker, or ``None`` for ordinary requests."""
    if not isinstance(frozen, Mapping):
        return None
    request = frozen.get('request')
    execution = request.get('execution') if isinstance(request, Mapping) else None
    receipt = execution.get('proposal_receipt') if isinstance(execution, Mapping) else None
    freshness = receipt.get('source_freshness') if isinstance(receipt, Mapping) else None
    observed = freshness.get('observed') if isinstance(freshness, Mapping) else None
    if not isinstance(observed, Mapping) or 'container_lifecycle' not in observed:
        return None
    marker = observed['container_lifecycle']
    return marker if isinstance(marker, Mapping) else {}


def _container_member_rows(value):
    if not isinstance(value, list) or not value:
        raise ValueError('container aggregate members are invalid')
    rows = []
    requested_ids = []
    actual_ids = []
    for item in value:
        if not isinstance(item, Mapping):
            raise ValueError('container aggregate members must carry Run identities')
        requested_id = item.get('requested_run_id')
        if not isinstance(requested_id, str) or not requested_id:
            raise ValueError('container aggregate member requested Run identity is invalid')
        if 'actual_run_id' not in item:
            raise ValueError('container aggregate member actual Run identity is missing')
        actual_id = item.get('actual_run_id')
        if actual_id is not None and (not isinstance(actual_id, str) or not actual_id):
            raise ValueError('container aggregate member actual Run identity is invalid')
        outcome = item.get('outcome')
        if not isinstance(outcome, str) or not outcome:
            raise ValueError('container aggregate member outcome is invalid')
        effect_refs = item.get('effect_refs')
        if not isinstance(effect_refs, list) or any(
                not isinstance(reference, str) or not reference for reference in effect_refs):
            raise ValueError('container aggregate member effect references are invalid')
        requested_ids.append(requested_id)
        if actual_id is not None:
            actual_ids.append(actual_id)
        rows.append(dict(item))
    if len(set(requested_ids)) != len(requested_ids):
        raise ValueError('container aggregate members contain duplicate requested Run identities')
    if len(set(actual_ids)) != len(actual_ids):
        raise ValueError('container aggregate members contain duplicate actual Run identities')
    return rows, requested_ids, actual_ids


def _container_ids(value, field):
    if not isinstance(value, list):
        raise ValueError(f'container aggregate {field} is invalid')
    identifiers = []
    for identifier in value:
        if not isinstance(identifier, str) or not identifier:
            raise ValueError(f'container aggregate {field} has an invalid Run identity')
        identifiers.append(identifier)
    if len(set(identifiers)) != len(identifiers):
        raise ValueError(f'container aggregate {field} contains duplicate Run identities')
    return identifiers


def _container_failed_member(value):
    if value is None:
        return None
    if not isinstance(value, Mapping):
        raise ValueError('container aggregate failed member must be a mapping or null')
    requested_id = value.get('requested_run_id')
    if not isinstance(requested_id, str) or not requested_id:
        raise ValueError('container aggregate failed member requested Run identity is invalid')
    actual_id = value.get('actual_run_id')
    if actual_id is not None and (not isinstance(actual_id, str) or not actual_id):
        raise ValueError('container aggregate failed member actual Run identity is invalid')
    return dict(value)


def _container_outcome_groups(result, requested_ids, actual_ids):
    completed = _container_ids(result.get('completed'), 'completed')
    failed = _container_failed_member(result.get('failed'))
    untouched = _container_ids(result.get('untouched'), 'untouched')
    requested_set = set(requested_ids)
    actual_set = set(actual_ids)
    if any(identifier not in actual_set for identifier in completed):
        raise ValueError('container aggregate completed IDs must be actual Run identities')
    if any(identifier not in requested_set for identifier in untouched):
        raise ValueError('container aggregate untouched IDs must be requested Run identities')
    failed_requested = failed.get('requested_run_id') if failed is not None else None
    if failed_requested is not None and failed_requested not in requested_set:
        raise ValueError('container aggregate failed member is not a requested member')
    completed_set = set(completed)
    completed_requested = {
        row['requested_run_id'] for row in result['members']
        if row.get('actual_run_id') in completed_set
    }
    groups = (completed_requested, {failed_requested} if failed_requested is not None else set(), set(untouched))
    if any(set(left) & set(right) for index, left in enumerate(groups) for right in groups[index + 1:]):
        raise ValueError('container aggregate member outcome groups overlap')
    if set().union(*groups) != requested_set:
        raise ValueError('container aggregate member outcome groups are incomplete')
    if failed is not None and failed.get('actual_run_id') is not None:
        failed_row = next(row for row in result['members'] if row['requested_run_id'] == failed_requested)
        if failed_row.get('actual_run_id') != failed['actual_run_id']:
            raise ValueError('container aggregate failed member actual Run identity differs from its member')
    for row in result['members']:
        requested_id = row['requested_run_id']
        if requested_id in completed_requested and row.get('outcome') not in {'completed', 'no_op'}:
            raise ValueError('container aggregate completed member outcome is invalid')
        if requested_id in untouched and row.get('actual_run_id') is not None:
            raise ValueError('container aggregate untouched member has an actual Run identity')
    return completed, failed, untouched


def _validate_container_aggregate(result, marker, run_id):
    if not isinstance(result, Mapping):
        raise ValueError('container lifecycle aggregate is not a mapping')
    if result.get('schema') != CONTAINER_LIFECYCLE_SCHEMA:
        raise ValueError('container lifecycle aggregate schema is invalid')
    if 'terminal_runs' in result or 'rootworkflow_run_id' in result:
        raise ValueError('container lifecycle aggregate carries a root Workflow terminal')
    if result.get('coordinator_id') != run_id:
        raise ValueError('container lifecycle coordinator does not match the requested Run')
    marker_coordinator = marker.get('coordinator_id')
    if marker_coordinator is not None and marker_coordinator != run_id:
        raise ValueError('container lifecycle seal coordinator does not match the requested Run')
    if result.get('original_requested_root_run_started') is not False:
        raise ValueError('container lifecycle aggregate incorrectly started the requested root Run')
    parent_requested_id = result.get('parent_requested_run_id')
    if not isinstance(parent_requested_id, str) or not parent_requested_id or parent_requested_id == run_id:
        raise ValueError('container lifecycle parent requested Run identity is invalid')
    members, requested_ids, actual_ids = _container_member_rows(result.get('members'))
    if requested_ids[-1] != parent_requested_id or run_id in requested_ids:
        raise ValueError('container lifecycle member identities do not bind the requested parent')
    if run_id in actual_ids:
        raise ValueError('container lifecycle member actual Run identity claims the technical coordinator')
    parent_run_id = result.get('parent_run_id')
    if parent_run_id is not None and (not isinstance(parent_run_id, str) or not parent_run_id or parent_run_id == run_id):
        raise ValueError('container lifecycle actual parent Run identity is invalid')
    completed, failed, untouched = _container_outcome_groups(
        {'members': members, 'completed': result.get('completed'), 'failed': result.get('failed'),
         'untouched': result.get('untouched')}, requested_ids, actual_ids,
    )
    parent_member = members[-1]
    if parent_run_id != parent_member.get('actual_run_id'):
        raise ValueError('container lifecycle actual parent Run identity is not bound to its member')
    effect_refs = result.get('effect_refs')
    if not isinstance(effect_refs, list) or any(not isinstance(item, str) or not item for item in effect_refs):
        raise ValueError('container lifecycle effect references are invalid')
    outcome = result.get('outcome')
    disposition = result.get('disposition')
    if not isinstance(outcome, str) or not outcome or not isinstance(disposition, str) or not disposition:
        raise ValueError('container lifecycle aggregate outcome is incomplete')
    return {
        'coordinator_id': run_id,
        'parent_requested_run_id': parent_requested_id,
        'parent_run_id': parent_run_id,
        'members': members,
        'completed': completed,
        'failed': failed,
        'untouched': untouched,
        'effect_refs': list(effect_refs),
        'outcome': outcome,
        'disposition': disposition,
    }


def _container_public_outcome(result, marker, run_id):
    try:
        aggregate = _validate_container_aggregate(result, marker, run_id)
    except ValueError as error:
        return 'interrupted_pending', 'recording_pending', str(error), None
    if aggregate['disposition'] != 'terminal' and aggregate['outcome'] in {'completed', 'no_op'}:
        return 'interrupted_pending', 'recording_pending', None, aggregate
    return aggregate['outcome'], aggregate['disposition'], None, aggregate


def _verify_container_lifecycle_seal(root, execution):
    """Require the exact root preview seal before direct queue admission."""
    marker = _container_lifecycle_marker({'request': {'execution': execution}})
    if marker is None:
        return
    if execution.get('operation_route') != 'change_atom_status':
        raise RuntimeError('container lifecycle seal is only valid for change_atom_status')
    from container_lifecycle_admission import seal_contained_status_changes
    from selected_execution import preflight_selected_lifecycle

    admission = preflight_selected_lifecycle(root, 'change_atom_status', execution.get('parameters'))
    if admission is None:
        raise RuntimeError('container lifecycle parent admission is missing')
    current = seal_contained_status_changes(root, execution.get('parameters'), admission)
    if not isinstance(current, Mapping) or canonical_json(dict(current)) != canonical_json(dict(marker)):
        raise RuntimeError('container lifecycle preview seal is stale or invalid')


def _selected_public_outcome(frozen, result, run_id):
    """Read the workflow outcome from canonical selected-Run terminal evidence.

    DBOS ``SUCCESS`` proves only that its scheduler wrapper returned.  It is
    never authority for a selected Workflow result, and neither is a nested
    Action terminal.  Older direct result envelopes predate ``terminal_runs``;
    retain their existing public shape unchanged.
    """
    marker = _container_lifecycle_marker(frozen)
    if marker is not None:
        outcome, disposition, reason, _aggregate = _container_public_outcome(result, marker, run_id)
        return outcome, disposition, reason
    if not isinstance(result, dict):
        return None, None, "selected result is not a mapping"
    if "terminal_runs" not in result:
        return result.get("outcome"), result.get("disposition"), None
    terminal_runs = result.get("terminal_runs")
    request = frozen.get("request") if isinstance(frozen, dict) else None
    execution = request.get("execution") if isinstance(request, dict) else None
    requested_runs = execution.get("requested_runs") if isinstance(execution, dict) else None
    workflow_bindings = [
        row for row in requested_runs if isinstance(row, dict)
        and row.get("requested_run_id") == run_id and row.get("kind") == "workflow"
    ] if isinstance(requested_runs, list) else []
    if not isinstance(terminal_runs, list) or len(workflow_bindings) != 1:
        return "failed", result.get("disposition"), "canonical Workflow terminal evidence is missing or ambiguous"
    candidates = [
        row for row in terminal_runs if isinstance(row, dict) and row.get("run_id") == run_id
        and ("kind" not in row or row.get("kind") == "workflow")
    ]
    if len(candidates) != 1 or candidates[0].get("disposition") not in {"terminal", "interrupted"}:
        return "failed", result.get("disposition"), "canonical Workflow terminal evidence is missing or ambiguous"
    outcome = candidates[0].get("outcome")
    if not isinstance(outcome, str) or not outcome:
        return "failed", result.get("disposition"), "canonical Workflow terminal evidence is incomplete"
    disposition = candidates[0]["disposition"]
    if disposition == "interrupted" and outcome != "interrupted_pending":
        return "failed", result.get("disposition"), "canonical Workflow interrupted evidence has an invalid outcome"
    return outcome, disposition, None


def status(root, request):
    request = Status.model_validate(request)
    transport = client(root)
    try:
        handle = transport.retrieve_workflow(request.run_id)
        queue_status = handle.get_status()
        response = {'workflow_run_id': request.run_id, 'scheduler_status': queue_status.status,
                    'backend': 'dbos', 'workflow_id': 'CA-O-104'}
        if queue_status.status == 'SUCCESS':
            response['result'] = handle.get_result()
    finally:
        transport.destroy()
    selected = SelectedExecution(root)
    selected_directory = selected.run_directory(request.run_id)
    selected_request = selected_directory / 'selected_request.json'
    if selected_request.is_file():
        frozen = selected._read(selected_request)
        marker = _container_lifecycle_marker(frozen)
        container = marker is not None
        if container:
            response.pop('workflow_run_id', None)
            response.pop('workflow_id', None)
            response.pop('result', None)
            response.update({'coordinator_id': request.run_id,
                             'identity_kind': CONTAINER_IDENTITY_KIND,
                             'selected_route': frozen['graph']['route']})
        else:
            response.update({'workflow_id': frozen['graph']['workflow']['atom_id'],
                             'selected_route': frozen['graph']['route']})
        batch_progress = selected_directory / 'subject_batch_progress.json'
        if batch_progress.is_file():
            from subject_batch import subject_batch_progress_summary
            response['subject_batch'] = subject_batch_progress_summary(selected._read(batch_progress),
                result_ref=batch_progress.relative_to(selected.root).as_posix())
            response.pop('result', None)
        accepted = selected_directory / 'accepted.json'
        uncertain = selected_directory / 'dispatch_uncertain.json'
        if accepted.is_file():
            if container:
                try:
                    accepted_value = selected._read(accepted)
                    result = accepted_value.get('result') if isinstance(accepted_value, Mapping) else None
                except (OSError, TypeError, ValueError):
                    result = None
            else:
                result = selected._read(accepted)['result']
            reconciliation_reason = None
            if (not container and frozen['graph'].get('route') in {'build_entities_graph', 'build_terms_graph'}
                    and isinstance(result, dict)
                    and result.get('disposition') in {'recording_pending', 'started'}):
                try:
                    if canonical_json(selected.load(request.run_id)) != canonical_json(frozen):
                        raise RuntimeError('graph status differs from its saved frozen request')
                    result = selected.reconcile_graph_recording(frozen, persist=False)
                except (ValueError, RuntimeError, OSError):
                    # Observation cannot authorize repair, construction replay,
                    # or admission bypass.  Retain the original pending state.
                    reconciliation_reason = 'graph-recording-reconciliation-unavailable: saved evidence or current admission gate is unresolved'
            outcome, disposition, terminal_reason = _selected_public_outcome(frozen, result, request.run_id)
            response.update({'selected_result': result, 'outcome': outcome,
                             'disposition': disposition})
            if container:
                _outcome, _disposition, _reason, aggregate = _container_public_outcome(
                    result, marker, request.run_id,
                )
                if aggregate is not None:
                    response.update({key: aggregate[key] for key in (
                        'parent_requested_run_id', 'parent_run_id', 'members', 'completed',
                        'failed', 'untouched', 'effect_refs')})
            if batch_progress.is_file():
                response['selected_result'] = {'outcome': outcome, 'disposition': disposition,
                                              'result_ref': accepted.relative_to(selected.root).as_posix()}
            if reconciliation_reason is not None:
                response['reason'] = reconciliation_reason
            elif terminal_reason is not None:
                response['reason'] = terminal_reason
        elif uncertain.is_file():
            response.update({'outcome': 'interrupted_pending', 'disposition': 'recording_pending',
                             'reason': selected._read(uncertain).get('reason')})
        else:
            if container and queue_status.status not in ('ENQUEUED', 'PENDING'):
                response.update({'outcome': 'interrupted_pending', 'disposition': 'recording_pending',
                                 'reason': 'container lifecycle aggregate is not recorded'})
            else:
                response.setdefault('outcome', 'queued')
        return response
    engine = Coordinator(root, None)
    try:
        state = engine.store.load(request.run_id)
        response.update({key: state.get(key) for key in ('outcome', 'progress', 'report_path',
                        'recording_blockers', 'reason', 'coverage_gates')})
        response['operator_question'] = next((row['operator_question'] for row in
            state.get('coverage_gates', {}).values() if row.get('operator_question')), None)
    except FileNotFoundError:
        blocked = engine.run_directory(request.run_id) / 'blocked.json'
        if blocked.is_file():
            response.update(outcome='interrupted', reason=json.loads(blocked.read_text())['reason'])
        else:
            response['outcome'] = 'queued' if queue_status.status in ('ENQUEUED', 'PENDING') else 'failed'
    if queue_status.status in ('ERROR', 'CANCELLED'):
        response['recorded_outcome'] = response.get('outcome')
        response['outcome'] = 'failed' if queue_status.status == 'ERROR' else 'interrupted'
    return response


def register_execution(DBOS, engine, *, selected_providers=None):
    """Register one admitted recipe with durable phase checkpoints."""
    selected_providers = selected_providers or SelectedNativeProviders(engine.root)
    @DBOS.step(name='base-revise-gather')
    def gather(run_id):
        return engine.gather(run_id)

    @DBOS.step(name='base-revise-check')
    def check(run_id, ordinal):
        return engine.check(run_id, ordinal)

    @DBOS.step(name='base-revise-fix')
    def fix(run_id, ordinal):
        return engine.fix(run_id, ordinal)

    @DBOS.step(name='base-revise-finish')
    def finish(run_id, outcome, reason):
        return engine.finish(run_id, outcome, reason)

    @DBOS.step(name='base-revise-coverage')
    def coverage(run_id, phase, failure_reason=None):
        return engine.coverage_gate(run_id, phase, failure_reason)

    @DBOS.step(name='selected-workflow-dispatch')
    def selected_dispatch(run_id):
        return selected_providers.dispatch(run_id)

    @DBOS.workflow(name=WORKFLOW)
    def execute(run_id):
        return execute_plan(engine, run_id, gather, check, fix, finish, coverage)

    @DBOS.workflow(name=SELECTED_WORKFLOW)
    def execute_selected(run_id):
        return selected_dispatch(run_id)



def execute_plan(engine, run_id, gather, check, fix, finish, coverage):
    finishing = False
    try:
        gathered = gather(run_id)
        if gathered['outcome'] != 'running':
            return gathered
        request, _ = engine.request(run_id)
        coverage(run_id, 'gather')
        execute_phase(run_id, 'check', len(request.selection), check, coverage)
        execute_phase(run_id, 'fix', len(request.selection), fix, coverage)
        finishing = True
        return finish(run_id, 'completed', None)
    except FutureCancelledError:
        raise
    except Exception as error:
        failure, _secondary = report_failure(
            engine.root,
            error,
            component='WORKFLOW_ORCHESTRATOR',
            operation='execute_plan',
            correlation_id=run_id,
        )
        reason = str(error) if isinstance(error, Interrupted) else failure.message
        interrupted = {'workflow_run_id': run_id, 'outcome': 'interrupted', 'reason': reason}
        if finishing:
            return interrupted
        try:
            return finish(run_id, 'interrupted', reason)
        except FileNotFoundError:
            try:
                engine.save(engine.run_directory(run_id) / 'blocked.json', {'reason': reason})
            except Exception:
                pass
            return interrupted
        except Exception:
            return interrupted


def worker(root, *, agent=None, ready_file=None, implementation_agent=None,
           _process_boundary=False):
    """Explicitly started foreground process; no implicit daemon or hook installation."""
    diagnostic_root = None
    dbos = None
    dbos_initialized = False
    previous = {}
    try:
        from dbos import DBOS

        diagnostic_root = Path(root).resolve(strict=True)
        if implementation_agent is None and implementation_mock_runtime():
            from implementation_mock_agent import ImplementationMockAgent
            implementation_agent = ImplementationMockAgent(diagnostic_root)
        _, url = database(diagnostic_root)
        default_agent = RemoteAgent() if docker_runtime() else CodexAgent()
        engine = Coordinator(diagnostic_root, agent or default_agent)
        stop = threading.Event()
        scheduler = _scheduler_identity()
        DBOS(config={'name': scheduler['application'], 'system_database_url': url,
                     'run_admin_server': False, 'enable_otlp': False,
                     'application_version': scheduler['app_version'],
                     'max_executor_threads': 2})
        dbos = DBOS
        dbos_initialized = True
        register_execution(dbos, engine, selected_providers=SelectedNativeProviders(
            diagnostic_root, implementation_agent=implementation_agent))

        previous = {number: signal.getsignal(number) for number in (signal.SIGINT, signal.SIGTERM)}
        for number in previous:
            signal.signal(number, lambda *_: stop.set())
        dbos.launch()
        dbos.register_queue(scheduler['queue'], global_concurrency=1, worker_concurrency=1,
                            polling_interval_sec=0.2)
        if ready_file:
            identity = {'state': 'ready',
                'pid': __import__('os').getpid(),
                'application_version': scheduler['app_version'],
                'runtime_fingerprint': runtime_fingerprint(diagnostic_root)}
            engine.save(Path(ready_file), identity)
        stop.wait()
    except FutureCancelledError:
        raise
    except Exception as error:
        if _process_boundary:
            raise
        failure, secondary = report_failure(
            diagnostic_root,
            error,
            component='WORKFLOW_ORCHESTRATOR',
            operation='worker.startup',
        )
        message = f'{failure.code}: {failure.message}'
        if secondary:
            message += '; technical diagnostic unavailable'
        print(message, file=sys.stderr, flush=True)
        return 1
    finally:
        try:
            if dbos_initialized:
                dbos.destroy()
        finally:
            for number, handler in previous.items():
                signal.signal(number, handler)
