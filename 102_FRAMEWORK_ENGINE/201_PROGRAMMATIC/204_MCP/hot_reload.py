"""Explicit process generations; no watcher, workflow dispatch or automatic replay."""
import asyncio
import fcntl
import hashlib
import json
import os
from pathlib import Path
import re
import selectors
import shlex
import stat
import subprocess
import sys
import threading
import time
from contextlib import nullcontext
from typing import Literal

from jsonschema import Draft202012Validator
from mcp import Client, StdioServerParameters, types
from mcp.server.lowlevel import Server, NotificationOptions
from mcp.server.stdio import stdio_server
from pydantic import BaseModel, ConfigDict

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / '201_TOOLS'))
from project_selection import ProjectSelection, bind_selection, resolve_project, rebind_selection


def startup_selection(root, control_root=None, instance_id=None, host_root=None):
    selection = resolve_project(root, control_root)
    if host_root is not None and instance_id is None:
        raise ValueError('Host Project binding requires an explicit instance identity')
    return rebind_selection(selection, instance_id, host_root=host_root) if instance_id is not None else selection


class ReloadRequest(BaseModel):
    model_config = ConfigDict(extra='forbid', strict=True)
    operation: Literal['reload']
    request_id: str | None = None


CONTROL = types.Tool(name='reload_mcp_implementation',
    description='Explicitly reload MCP implementation; state-changing, no Workflow dispatch.',
    annotations=types.ToolAnnotations(read_only_hint=False, destructive_hint=False,
                                      idempotent_hint=True, open_world_hint=False),
    input_schema={'type': 'object', 'properties': {'request': ReloadRequest.model_json_schema()},
                  'required': ['request'], 'additionalProperties': False})

STATUS = types.Tool(name='get_mcp_reload_status',
    description='Read current MCP generations and in-flight counts; no reload or writes.',
    annotations=types.ToolAnnotations(read_only_hint=True, destructive_hint=False,
                                      idempotent_hint=True, open_world_hint=False),
    input_schema={'type': 'object', 'properties': {'request': {
        'type': 'object', 'properties': {}, 'additionalProperties': False}},
        'required': ['request'], 'additionalProperties': False})


def digest(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True).encode()).hexdigest()


def result(value, error=False):
    return types.CallToolResult(content=[types.TextContent(type='text', text=json.dumps(value))],
                                structured_content=value, is_error=error)


GENERATION_READY_TIMEOUT_SECONDS = 20
# Read-only catalog scans have their own sixty-second bound and watch calls may
# wait thirty seconds.  The child's startup budget must not truncate either.
IMPLEMENTATION_CALL_TIMEOUT_SECONDS = 90
_STARTUP_TELEMETRY_ENV = 'CAPRMEDIO_STARTUP_TELEMETRY'
_STARTUP_PHASES = frozenset({
    'initial_fingerprint', 'reload_fingerprint', 'fingerprint_verify',
    'child_handshake', 'list_tools', 'generation_ready', 'schema_validation',
})
_SINGLETON_LOCK_PARTS = ('.caprmedio_install', 'runtime_locks', 'mcp_hot_reload')
_INSTANCE_ID = re.compile(r'[0-9a-f]{64}\Z')
_PROCESS_QUERY_MAX_BYTES = 64 * 1024
_PROCESS_QUERY_MAX_SECONDS = 2.0
_GATEWAY_ENTRYPOINTS = frozenset(('server.py', 'http_server.py'))


def _startup_telemetry_enabled():
    """Keep bounded startup timing diagnostics opt-in and transport-safe."""
    return os.environ.get(_STARTUP_TELEMETRY_ENV) == '1'


def _startup_timing(enabled, phase, started, outcome='completed'):
    """Emit fixed phase timing only; never put diagnostic data on MCP stdout."""
    if enabled and phase in _STARTUP_PHASES:
        elapsed_ms = max(0, round((time.monotonic() - started) * 1000))
        print(f'caprmedio_mcp_startup phase={phase} outcome={outcome} elapsed_ms={elapsed_ms}',
              file=sys.stderr, flush=True)


def _singleton_lock_path(root, instance_id):
    """Create only the fixed local lock namespace, never infer process state."""
    if not isinstance(instance_id, str) or _INSTANCE_ID.fullmatch(instance_id) is None:
        raise RuntimeError('MCP gateway Project instance is unavailable')
    try:
        current = Path(root).resolve(strict=True)
        if not current.is_dir() or current.is_symlink():
            raise ValueError()
        for part in _SINGLETON_LOCK_PARTS:
            current = current / part
            status = os.lstat(current) if os.path.lexists(current) else None
            if status is None:
                current.mkdir(mode=0o700)
                status = os.lstat(current)
            if stat.S_ISLNK(status.st_mode) or not stat.S_ISDIR(status.st_mode):
                raise ValueError()
        return current / f'{instance_id}.lock'
    except (OSError, RuntimeError, TypeError, ValueError) as error:
        raise RuntimeError('MCP gateway singleton fence is unavailable') from error


def _open_singleton_lock(root, instance_id):
    """Acquire the lifetime fence shared by every gateway publisher process."""
    path = _singleton_lock_path(root, instance_id)
    descriptor = None
    try:
        descriptor = os.open(path, os.O_RDWR | os.O_CREAT | getattr(os, 'O_NOFOLLOW', 0), 0o600)
        if not stat.S_ISREG(os.fstat(descriptor).st_mode):
            raise RuntimeError('MCP gateway singleton fence is unsafe')
        try:
            fcntl.flock(descriptor, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError as error:
            raise RuntimeError('MCP gateway singleton fence is busy') from error
        return descriptor
    except BaseException:
        if descriptor is not None:
            os.close(descriptor)
        raise


def _close_singleton_lock(descriptor):
    if descriptor is None:
        return
    try:
        fcntl.flock(descriptor, fcntl.LOCK_UN)
    finally:
        os.close(descriptor)


def _project_root_arguments(tokens):
    values = []
    for index, token in enumerate(tokens):
        if token == '--project-root':
            values.append(tokens[index + 1] if index + 1 < len(tokens) else None)
        elif token.startswith('--project-root='):
            values.append(token.removeprefix('--project-root='))
    return tuple(values)


def _gateway_command_targets_project(command, root_text):
    """Keep ambiguous legacy entrypoints as candidates rather than discard them."""
    try:
        tokens = shlex.split(command)
    except ValueError:
        return any(marker in command for marker in (*_GATEWAY_ENTRYPOINTS, 'hot_reload'))
    entrypoint = any(Path(token).name in _GATEWAY_ENTRYPOINTS for token in tokens)
    # macOS `ps` can flatten a real ``python -c`` argument so its source is no
    # longer one shell token.  Inspect the bounded raw command too; a match is
    # only allowed to make coverage more conservative (unknown), never absent.
    embedded_gateway = 'from hot_reload import Gateway' in command
    if not entrypoint and not embedded_gateway:
        return False
    values = _project_root_arguments(tokens)
    if len(values) != 1:
        # argparse accepts repeated options with last-value semantics.  A
        # legacy process table cannot prove that its rendered argv preserved
        # that meaning, so retain every repeated/missing form as ambiguous.
        return True
    value = values[0]
    if not isinstance(value, str) or not value:
        # A malformed/relative command may still be a legacy gateway whose
        # process CWD is unavailable from this bounded platform-neutral scan.
        return True
    try:
        candidate = Path(value)
        if not candidate.is_absolute():
            return True
        return str(candidate.resolve(strict=False)) == root_text
    except (OSError, RuntimeError, TypeError, ValueError):
        return True


def _gateway_pids_from_process_output(output, root_text):
    try:
        pids = []
        for line in output.decode('utf-8').splitlines():
            match = re.match(r'^\s*([0-9]+)\s+(.*)$', line)
            if match is None:
                return None
            pid, command = int(match.group(1)), match.group(2)
            if _gateway_command_targets_project(command, root_text):
                pids.append(pid)
        return tuple(pids)
    except (UnicodeError, ValueError):
        return None


def _legacy_gateway_pids(root, deadline):
    """Return supported pre-lease gateway PIDs, or ``None`` if not queryable.

    The singleton lease was introduced after legacy gateways already existed.
    It cannot prove their absence.  This is therefore a bounded, read-only OS
    query for the three supported gateway entrypoint command shapes.  It does
    not attempt to identify, signal, or stop arbitrary Python processes.
    """
    remaining = min(_PROCESS_QUERY_MAX_SECONDS, deadline - time.monotonic())
    if remaining <= 0:
        return None
    process = None
    selector = selectors.DefaultSelector()
    output = bytearray()
    try:
        root_text = str(Path(root).resolve(strict=True))
        process = subprocess.Popen(
            ['ps', '-axo', 'pid=,command='], stdin=subprocess.DEVNULL,
            stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, shell=False,
        )
        if process.stdout is None:
            return None
        selector.register(process.stdout, selectors.EVENT_READ)
        query_deadline = time.monotonic() + remaining
        while selector.get_map():
            wait = query_deadline - time.monotonic()
            if wait <= 0:
                return None
            for key, _ in selector.select(wait):
                chunk = os.read(key.fileobj.fileno(), min(4096, _PROCESS_QUERY_MAX_BYTES + 1 - len(output)))
                if not chunk:
                    selector.unregister(key.fileobj)
                    continue
                output.extend(chunk)
                if len(output) > _PROCESS_QUERY_MAX_BYTES:
                    return None
        wait = query_deadline - time.monotonic()
        if wait <= 0 or process.wait(timeout=wait) != 0:
            return None
    except (OSError, subprocess.SubprocessError, ValueError):
        return None
    finally:
        selector.close()
        if process is not None:
            if process.stdout is not None:
                process.stdout.close()
            if process.poll() is None:
                try:
                    process.kill()
                    process.wait(timeout=1)
                except (OSError, subprocess.SubprocessError):
                    pass
    return _gateway_pids_from_process_output(bytes(output), root_text)


class Generation:
    def __init__(self, params, fingerprint):
        self.params, self.fingerprint = params, fingerprint
        self.client, self.tools, self.in_flight = None, [], 0
        self.retired_at = None
        self.stop = asyncio.Event()
        self.ready = asyncio.get_running_loop().create_future()
        self.startup_telemetry = _startup_telemetry_enabled()
        self.task = asyncio.create_task(self.run())

    async def run(self):
        phase = 'child_handshake'
        started = time.monotonic()
        try:
            # This is a known local implementation subprocess.  Its cold
            # import can exceed the client's fixed ten-second auto-discover
            # probe, whereas the gateway already owns a bounded readiness
            # deadline.  Negotiate the stable legacy handshake directly.
            async with Client(self.params, cache=None, mode='legacy',
                              read_timeout_seconds=GENERATION_READY_TIMEOUT_SECONDS) as client:
                _startup_timing(self.startup_telemetry, phase, started)
                self.client = client
                phase, started = 'list_tools', time.monotonic()
                page = await client.list_tools()
                self.tools = list(page.tools)
                while page.next_cursor:
                    page = await client.list_tools(cursor=page.next_cursor)
                    self.tools.extend(page.tools)
                _startup_timing(self.startup_telemetry, phase, started)
                self.ready.set_result(None)
                await self.stop.wait()
        except BaseException as error:
            if not self.ready.done():
                _startup_timing(self.startup_telemetry, phase, started, 'failed')
                self.ready.set_exception(error)

    async def close(self):
        self.stop.set()
        try:
            await asyncio.wait_for(asyncio.shield(self.task), 5)
        except (TimeoutError, asyncio.CancelledError):
            self.task.cancel()
            await asyncio.gather(self.task, return_exceptions=True)
            if asyncio.current_task().cancelling():
                raise


class Gateway:
    def __init__(self, root, implementation=None, *, selection=None):
        self.root = Path(root).resolve(strict=True)
        self.selection = selection
        if selection is not None and (not isinstance(selection, ProjectSelection) or selection.root != self.root):
            raise ValueError('Gateway selection belongs to another Project')
        self.implementation = Path(implementation or Path(__file__).with_name('implementation_server.py'))
        self.active, self.generations = None, []
        self.reload_lock, self.receipts = asyncio.Lock(), {}
        self.generation_fence = threading.Lock()
        self._singleton_descriptor = None
        self._initialized = False
        self.storage = selection.reload_state if selection is not None else self.root / '.caprmedio_install/mcp_hot_reload'

    @property
    def _singleton_instance_id(self):
        # Unbound compatibility launches remain Project-local.  An admitted
        # selection always supplies the cross-process installation identity.
        return self.selection.instance_id if self.selection is not None else digest(str(self.root))

    def _acquire_singleton_fence(self):
        if self._singleton_descriptor is not None:
            return False
        self._singleton_descriptor = _open_singleton_lock(self.root, self._singleton_instance_id)
        return True

    def _release_singleton_fence(self):
        descriptor, self._singleton_descriptor = self._singleton_descriptor, None
        _close_singleton_lock(descriptor)

    def _fingerprint_with_timing(self, phase):
        started = time.monotonic()
        try:
            value = self.fingerprint()
        except BaseException:
            _startup_timing(_startup_telemetry_enabled(), phase, started, 'failed')
            raise
        _startup_timing(_startup_telemetry_enabled(), phase, started)
        return value

    def fingerprint(self):
        files = [self.implementation]
        if self.implementation.name == 'implementation_server.py':
            files = [p for p in self.implementation.parent.parent.rglob('*.py')
                     if p.name not in ('server.py', 'hot_reload.py')
                     and not any(part in ('tests', '__pycache__', '.venv', 'venv') for part in p.parts)]
        return digest([(str(p), hashlib.sha256(p.read_bytes()).hexdigest()) for p in sorted(files)])

    async def _prepare(self, fingerprint):
        environment = self.child_environment()
        arguments = [str(self.implementation), '--project-root', str(self.root)]
        if self.selection is not None:
            arguments += ['--control-root', self.selection.control_relative.as_posix(),
                          '--instance-id', self.selection.instance_id]
            if self.selection.host_root is not None:
                arguments += ['--host-project-root', str(self.selection.host_root)]
        generation = Generation(StdioServerParameters(command=sys.executable,
            args=['-B', '-X', f'pycache_prefix={self.storage / "bytecode" / fingerprint}',
                  *arguments],
            env=environment), fingerprint)
        phase = 'generation_ready'
        started = time.monotonic()
        try:
            await asyncio.wait_for(asyncio.shield(generation.ready),
                                   GENERATION_READY_TIMEOUT_SECONDS)
            _startup_timing(_startup_telemetry_enabled(), phase, started)
            phase, started = 'schema_validation', time.monotonic()
            names = [t.name for t in generation.tools]
            if len(set(names)) != len(names) or {CONTROL.name, STATUS.name}.intersection(names):
                raise ValueError('Duplicate or reserved Tool name')
            for tool in generation.tools:
                if not re.fullmatch(r'[A-Za-z0-9_.-]{1,128}', tool.name):
                    raise ValueError('Invalid Tool name')
                Draft202012Validator.check_schema(tool.input_schema)
                if tool.output_schema is not None:
                    Draft202012Validator.check_schema(tool.output_schema)
            _startup_timing(_startup_telemetry_enabled(), phase, started)
            phase, started = 'fingerprint_verify', time.monotonic()
            if self._fingerprint_with_timing('fingerprint_verify') != fingerprint:
                raise ValueError('Implementation changed during preparation')
        except BaseException:
            if phase != 'fingerprint_verify':
                _startup_timing(_startup_telemetry_enabled(), phase, started, 'failed')
            await generation.close()
            raise
        generation.registry = digest([t.model_dump(mode='json', by_alias=True) for t in generation.tools])
        self.generations.append(generation)
        return generation

    async def prepare(self, fingerprint):
        """Public generation start seam guarded by the shared writer fence."""
        if not self.generation_fence.acquire(blocking=False):
            raise RuntimeError('MCP generation writer fence is busy')
        acquired = False
        try:
            acquired = self._acquire_singleton_fence()
            return await self._prepare(fingerprint)
        except BaseException:
            if acquired and not self._initialized:
                self._release_singleton_fence()
            raise
        finally:
            self.generation_fence.release()

    @staticmethod
    def child_environment():
        """Pass only runtime essentials; transport credentials never reach tools."""
        allowed = {'PATH', 'TMPDIR', 'TEMP', 'TMP', 'LANG', 'TZ', 'CAPRMEDIO_RUNTIME_NAMESPACE'}
        return {key: value for key, value in os.environ.items()
                if key in allowed or key.startswith('LC_')}

    def status(self):
        return {'active_generation': self.active.fingerprint if self.active else None,
                'client_refresh_status': 'unconfirmed',
                'generations': [{'generation': g.fingerprint, 'in_flight': g.in_flight,
                                 'serving': g is self.active,
                                 'process_available': not g.task.done(),
                                 'drain_limit_reached': g.retired_at is not None
                                 and g.in_flight > 0 and time.monotonic() - g.retired_at >= 60}
                                for g in self.generations]}

    def persist(self, request_id, value):
        current = self.storage
        while current != self.root:
            if current.is_symlink():
                raise ValueError('Symlink checkpoint directory')
            current = current.parent
        self.storage.mkdir(parents=True, exist_ok=True)
        path = self.storage / f'{request_id}.json'
        temporary = self.storage / f'{request_id}.pending'
        with temporary.open('x') as stream:
            json.dump(value, stream)
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(temporary, path)

    async def publish(self, old, fingerprint, context, value):
        candidate = await self._prepare(fingerprint)
        self.active = candidate
        old.retired_at = time.monotonic()
        changed = old.registry != candidate.registry
        value.update(outcome='reloaded', active_generation=fingerprint,
                     implementation_fingerprint=fingerprint,
                     registry_fingerprint=candidate.registry, registry_changed=changed)
        if changed:
            capabilities = self.server.get_capabilities(
                NotificationOptions(tools_changed=True), protocol_version=context.session.protocol_version)
            if capabilities.tools and capabilities.tools.list_changed:
                try:
                    await context.session.send_tool_list_changed()
                    value['notification_status'] = 'sent'
                except Exception:
                    value['notification_status'] = 'failed'
        if old.in_flight == 0:
            try:
                await old.close()
            except Exception:
                value['diagnostics'].append('Retired generation cleanup failed')

    async def reload(self, request, context):
        if not request.request_id or not re.fullmatch(r'[A-Za-z0-9_-]{1,128}', request.request_id):
            raise ValueError('reload requires a safe request_id')
        async with self.reload_lock:
            # This is also the physical fence held by retained-migration
            # observation.  Never block the event loop on a threading lock:
            # a fenced observer can yield while it owns the lock.
            if request.request_id in self.receipts:
                return self.receipts[request.request_id]
            if not self.generation_fence.acquire(blocking=False):
                old = self.active
                return {
                    'request_id': request.request_id,
                    'previous_generation': old.fingerprint if old is not None else None,
                    'active_generation': old.fingerprint if old is not None else None,
                    'implementation_fingerprint': old.fingerprint if old is not None else None,
                    'registry_fingerprint': old.registry if old is not None else None,
                    'registry_changed': False,
                    'notification_status': 'unsupported',
                    'client_refresh_status': 'unconfirmed',
                    'diagnostics': ['Generation writer fence is busy'],
                    'outcome': 'failed',
                }
            try:
                old = self.active
                if old is None or self._singleton_descriptor is None:
                    raise RuntimeError('MCP gateway is not initialized')
                value = {'request_id': request.request_id, 'previous_generation': old.fingerprint,
                         'active_generation': old.fingerprint, 'implementation_fingerprint': old.fingerprint,
                         'registry_fingerprint': old.registry, 'registry_changed': False,
                         'notification_status': 'unsupported', 'client_refresh_status': 'unconfirmed',
                         'diagnostics': [], 'outcome': 'unchanged'}
                try:
                    fingerprint = self._fingerprint_with_timing('reload_fingerprint')
                    if fingerprint != old.fingerprint:
                        await self.publish(old, fingerprint, context, value)
                except Exception as error:
                    value.update(outcome='failed', diagnostics=[f'{type(error).__name__}: candidate rejected'])
                self.receipts[request.request_id] = value
                try:
                    self.persist(request.request_id, value)
                except (OSError, ValueError):
                    value['diagnostics'].append('Receipt persistence failed')
                return value
            finally:
                self.generation_fence.release()

    async def control(self, context, arguments):
        try:
            if set(arguments) != {'request'}:
                raise ValueError('Expected only request')
            request = ReloadRequest.model_validate(arguments['request'])
            value = await self.reload(request, context)
            return result(value, value.get('outcome') in ('failed', 'rejected'))
        except ValueError as error:
            return result({'outcome': 'rejected', 'diagnostics': [str(error)]}, True)

    async def call(self, context, params):
        with bind_selection(self.selection) if self.selection is not None else nullcontext():
            return await self._call(context, params)

    async def _call(self, context, params):
        if params.name == STATUS.name:
            if params.arguments != {'request': {}}:
                return result({'outcome': 'rejected', 'diagnostics': ['Expected an empty request']}, True)
            return result(self.status())
        if params.name == CONTROL.name:
            return await self.control(context, params.arguments or {})
        generation = self.active
        generation.in_flight += 1
        try:
            if params.name not in {t.name for t in generation.tools}:
                return result({'outcome': 'rejected', 'diagnostics': ['Unknown Tool']}, True)
            return await generation.client.call_tool(params.name, params.arguments,
                read_timeout_seconds=IMPLEMENTATION_CALL_TIMEOUT_SECONDS)
        except Exception:
            return result({'outcome': 'uncertain', 'generation': generation.fingerprint,
                           'diagnostics': ['Implementation call failed; no automatic replay']}, True)
        finally:
            generation.in_flight -= 1
            if generation is not self.active and generation.in_flight == 0:
                await generation.close()

    async def serve(self):
        await self.initialize()
        try:
            async with stdio_server() as streams:
                await self.build_server().run(*streams, self.server.create_initialization_options(
                    notification_options=NotificationOptions(tools_changed=True)))
        finally:
            await self.close()

    async def initialize(self):
        if not self.generation_fence.acquire(blocking=False):
            raise RuntimeError('MCP generation writer fence is busy')
        acquired = False
        try:
            acquired = self._acquire_singleton_fence()
            if self.active is None:
                self.active = await self._prepare(self._fingerprint_with_timing('initial_fingerprint'))
            self._initialized = True
        except BaseException:
            if acquired and not self._initialized:
                self._release_singleton_fence()
            raise
        finally:
            self.generation_fence.release()

    async def close(self):
        # Closing while a retained-migration observation holds the exact
        # writer fence would invalidate its snapshot.  Refuse rather than
        # block this event loop behind a potentially yielding observer.
        if not self.generation_fence.acquire(blocking=False):
            return
        try:
            closing = [asyncio.create_task(generation.close()) for generation in self.generations]
            if not closing:
                return
            done, pending = await asyncio.wait(closing, timeout=6)
            for task in pending:
                task.cancel()
            await asyncio.gather(*done, *pending, return_exceptions=True)
        finally:
            try:
                self._release_singleton_fence()
            finally:
                self.generation_fence.release()

    def build_server(self):

        async def list_tools(context, params):
            return types.ListToolsResult(tools=[CONTROL, STATUS, *self.active.tools])

        server = Server('CAPRMEDIO', version='0.2.0', on_list_tools=list_tools,
                        on_call_tool=self.call)
        self.server = server
        return server


def collect_legacy_processes(admission, deadline, *, fenced=False):
    """Report zero only while the real cross-process publisher lock is held.

    This intentionally has no registry, receipt, PID, or readiness-file
    fallback.  Every publisher acquires the same Project/instance singleton
    before creating its first generation and retains it through ``close``.
    A collector that holds that lease then performs a bounded read-only
    process-table scan for pre-lease gateways.  It never signals, stops, or
    otherwise controls a process.
    """
    if not fenced or time.monotonic() >= deadline:
        return {'outcome': 'unavailable', 'records': []}
    pids = _legacy_gateway_pids(getattr(admission, 'project_root', None), deadline)
    if pids is None:
        return {'outcome': 'unavailable', 'records': []}
    if pids:
        # The legacy command line binds only the Project root.  It cannot
        # attest the sealed predecessor context or shutdown state, so this
        # raw live evidence must become ``unknown`` in the generic collector.
        return {'outcome': 'complete', 'records': [{'pid': pid} for pid in pids]}
    return {'outcome': 'complete', 'records': []}


class _LegacyProcessFence:
    """Hold the exact cross-process singleton that writers retain for life."""

    def __init__(self, admission, deadline):
        root = getattr(admission, 'project_root', None)
        instance = getattr(admission, 'project_instance_id', None)
        if time.monotonic() >= deadline:
            raise RuntimeError('MCP gateway singleton fence is unavailable')
        self.descriptor = _open_singleton_lock(root, instance)
        self.admission, self.closed = admission, False

    def snapshot(self, deadline):
        if self.closed or time.monotonic() >= deadline:
            return {'outcome': 'unavailable', 'records': []}
        return collect_legacy_processes(self.admission, deadline, fenced=True)

    def close(self):
        if not self.closed:
            self.closed = True
            _close_singleton_lock(self.descriptor)


def open_legacy_process_fence(admission, deadline):
    """Acquire the actual gateway singleton; no receipt fallback exists."""
    return _LegacyProcessFence(admission, deadline)
