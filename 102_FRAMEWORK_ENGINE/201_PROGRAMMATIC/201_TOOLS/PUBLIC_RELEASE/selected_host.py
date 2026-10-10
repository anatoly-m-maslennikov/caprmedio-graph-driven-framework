"""Private public-release host for one physically frozen, admitted Session.

No Run, handler registration, caller gate callback or alternate Project is
created here. All effects remain attached to the existing selected Action.
"""
from __future__ import annotations

import hashlib
import json
import os
from pathlib import Path
import stat
import sys
import tempfile
from collections.abc import Mapping

from native_bindings import NativeCommandEvidence, NativePublicReleaseBindings, _history_line
from public_release import GateResult, PublicReleaseError, SourceProof, ToolCallEvidence, _parameters, _pr, _safe_ref, _source
from workflow_run_support import RunExecutionSession, _proposal, _validate_common
import work_journal


PROGRAMMATIC = Path(__file__).resolve().parents[2]
for dependency in (PROGRAMMATIC / "204_MCP", PROGRAMMATIC / "203_APPS/WORKFLOW_ORCHESTRATOR",
                   PROGRAMMATIC / "201_TOOLS/RELEASE_VERSION"):
    if str(dependency) not in sys.path:
        sys.path.insert(0, str(dependency))

from selected_execution import SelectedExecution
from selected_routes import load_selected_manifest


class SelectedPublicHostError(PublicReleaseError):
    """A physical selected public host prerequisite cannot be reopened."""


def _bytes(value: object) -> bytes:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"), allow_nan=False).encode("utf-8")


def _refuse(message: str) -> None:
    raise SelectedPublicHostError("selected-public-host-invalid", message)


def _action_id(operation: str) -> str:
    if operation == "discover_matching_pr":
        return "CA-O-190"
    if operation == "prepare_public_materials":
        return "CA-O-192"
    if operation in {"before_history_finalization", "after_history_finalization", "finalize_history_link"}:
        return "CA-O-198"
    prefix, separator, phase = operation.partition(":")
    if separator and phase in {"initial", "history_link_final"}:
        if prefix in {"full_gate", "run_full_gate"}:
            return "CA-O-194" if phase == "initial" else "CA-O-198"
        if prefix in {"commit_and_push", "upsert_main_pr"}:
            return "CA-O-196" if phase == "initial" else "CA-O-198"
    _refuse("operation is not part of the sealed public Workflow")


def _regular(root: Path, reference: str) -> tuple[bytes, os.stat_result]:
    _safe_ref(reference, "host carrier")
    current = root
    for index, part in enumerate(Path(reference).parts):
        current /= part
        observed = current.lstat()
        if stat.S_ISLNK(observed.st_mode) or (index < len(Path(reference).parts) - 1 and not stat.S_ISDIR(observed.st_mode)):
            _refuse("host carrier has an aliased ancestor")
    descriptor = os.open(current, os.O_RDONLY | getattr(os, "O_NOFOLLOW", 0))
    with os.fdopen(descriptor, "rb") as handle:
        before = os.fstat(handle.fileno())
        if not stat.S_ISREG(before.st_mode) or before.st_nlink != 1 or before.st_size > 1024 * 1024:
            _refuse("host carrier is not one bounded regular file")
        payload = handle.read(1024 * 1024 + 1)
        after = os.fstat(handle.fileno())
    if (before.st_dev, before.st_ino, before.st_size, before.st_mtime_ns) != (
        after.st_dev, after.st_ino, after.st_size, after.st_mtime_ns,
    ) or len(payload) != before.st_size:
        _refuse("host carrier changed while reopening")
    return payload, before


def _directory(root: Path, relative: Path) -> Path:
    _safe_ref(relative.as_posix(), "evidence directory")
    current = root
    for part in relative.parts:
        current /= part
        try:
            current.mkdir(mode=0o700)
        except FileExistsError:
            pass
        observed = current.lstat()
        if stat.S_ISLNK(observed.st_mode) or not stat.S_ISDIR(observed.st_mode):
            _refuse("evidence directory is aliased")
    return current


def _history_payload(original: bytes, summary: str, history_line: str) -> bytes:
    """Replace only one exact summary bullet, preserving all other bytes."""
    lines = original.decode("utf-8").splitlines(keepends=True)
    matching = [index for index, line in enumerate(lines) if line.rstrip("\r\n") == "- " + summary]
    if len(matching) != 1:
        _refuse("history has no unique exact unlinked summary bullet")
    index = matching[0]
    ending = "\r\n" if lines[index].endswith("\r\n") else "\n" if lines[index].endswith("\n") else ""
    lines[index] = history_line + ending
    return "".join(lines).encode("utf-8")


def _sync_directory(path: Path) -> None:
    descriptor = os.open(path, os.O_RDONLY | getattr(os, "O_DIRECTORY", 0) | getattr(os, "O_NOFOLLOW", 0))
    try:
        os.fsync(descriptor)
    finally:
        os.close(descriptor)


class _SelectedPublicHost:
    def __init__(self, root: Path, frozen: Mapping[str, object], session: RunExecutionSession):
        if type(session) is not RunExecutionSession:
            _refuse("host needs the actual shared RunExecutionSession")
        self.root = Path(root).resolve(strict=True)
        if self.root != Path(session.tracker.root).resolve(strict=True):
            _refuse("host and Session name different Projects")
        self.session = session
        self.frozen = json.loads(_bytes(frozen))
        self.request_bytes = _bytes(session.request)
        self.store = SelectedExecution(self.root)
        self.current()

    def current(self) -> Mapping[str, object]:
        request = self.frozen["request"]
        if self.store.load(request["run_id"]) != self.frozen:
            _refuse("frozen public request differs from its physical carrier")
        if _bytes(self.session.request) != self.request_bytes or _validate_common(request["execution"]) != self.session.request:
            _refuse("Session request differs from the frozen execution")
        graph = self.store._revalidate(self.frozen)
        manifest = load_selected_manifest(self.root)
        if graph["route"] != "public.release" or len(manifest.get("public_release_source_admissions", [])) != 1:
            _refuse("current canonical manifest has no D613 public admission")
        if manifest["canonical_manifest_sha256"] != self.session.request["definition_manifest"]["manifest_digest"]:
            _refuse("current manifest differs from the original admission")
        self.store._validate_requested_runs(self.session.request, graph, request["run_id"])
        observation = self.session.tracker._observe(self.session.request)
        if not observation["selected"] or not observation["current"]:
            _refuse("selected authorization is no longer current")
        proposal = _proposal(self.session.request, observation)
        self.session.tracker._validate_execute(self.session.request, proposal, work_journal.canonical_json_digest(proposal))
        return graph

    def action(self, operation: str):
        self.current()
        expected = _action_id(operation)
        active = [(key, run) for key, run in self.session.actual.items()
                  if run["kind"] == "action" and key not in self.session.terminal and key not in self.session.interrupted]
        if len(active) != 1 or active[0][1]["definition"]["atom_id"] != expected:
            _refuse("operation has no unique active admitted public Action")
        run = active[0][1]
        provenance = self.session.read_recorded_action_start(run["run_id"])
        if provenance.action_run_id != run["run_id"] or not provenance.parent_lineage:
            _refuse("canonical Action start differs from the selected public lineage")
        return run, provenance

    def native_n(self):
        from release_promotion import bind_selected_native_n_from_checkpoint
        binding = bind_selected_native_n_from_checkpoint(self.root)
        if binding is None:
            _refuse("public release needs a physically selected native generation")
        return binding

    def candidate(self, parameters: Mapping[str, object], phase: str) -> str:
        self.action(phase)
        if _parameters(parameters) != _parameters(self.session.request["parameters"]):
            _refuse("public parameters differ from the sealed request")
        binding = self.native_n()
        retained = binding.full_gate_packet.retained_candidate
        candidate = retained.candidate_snapshot_manifest_sha256
        if (candidate != parameters["source"]["candidate_snapshot_manifest_sha256"]
                or binding.selected.framework_version != parameters["release"]["selected_version"].removeprefix("v")):
            _refuse("current native N differs from the selected same-Version local candidate")
        version_bytes, _ = _regular(self.root, "version.toml")
        if hashlib.sha256(version_bytes).hexdigest() != retained.version_toml_sha256:
            _refuse("root version.toml differs from the physically selected local candidate")
        return candidate

    def admit(self, operation: str, parameters: Mapping[str, object], source: SourceProof | None) -> None:
        self.action(operation)
        if _parameters(parameters) != _parameters(self.session.request["parameters"]):
            _refuse("effect parameters differ from the sealed request")
        if source is None:
            _refuse("an effect needs its physically reopened SourceProof")
        if source is not None:
            selected = parameters["source"]
            for field in ("readme_ref", "pr_body_ref", "version_history_ref", "version_history_summary"):
                if getattr(source, field) != selected[field]:
                    _refuse("effect source substitutes a sealed public material binding")
            if any(getattr(source, field) not in self.session.request["target_frontier"]
                   for field in ("readme_ref", "pr_body_ref", "version_history_ref")):
                _refuse("effect source is outside the sealed public frontier")
            _source(source, "selected effect source", project_root=self.root, release=parameters["release"])
            if source.candidate_snapshot_manifest_sha256 != self.candidate(parameters, operation):
                _refuse("effect source differs from the physical native candidate")

    def record(self, evidence: NativeCommandEvidence) -> ToolCallEvidence:
        if type(evidence) is not NativeCommandEvidence or type(evidence.effect) is not bool:
            _refuse("recorder needs concrete sanitized native command evidence")
        run, provenance = self.action(evidence.operation)
        def check(value):
            if isinstance(value, Mapping):
                for key, item in value.items():
                    if not isinstance(key, str) or key.lower() in {"secret", "password", "token", "credentials", "api_key", "contents"}:
                        _refuse("command observation contains a prohibited field")
                    check(item)
            elif isinstance(value, (list, tuple)):
                for item in value:
                    check(item)
            elif isinstance(value, str) and any(character in value for character in "\x00\r\n"):
                _refuse("command observation contains unbounded text")
        check(evidence.observations)
        for command in evidence.commands:
            if not isinstance(command, tuple) or not command or command[0] not in {"git", "gh"}:
                _refuse("native evidence has an undesignated command")
            for argument in command:
                if not isinstance(argument, str) or any(character in argument for character in "\x00\r\n") or argument.startswith(("--password", "--token", "--credential")):
                    _refuse("native command contains a prohibited argument")
        document = {"schema_version": 1, "request_id": self.session.request["request_id"],
                    "action_run_id": run["run_id"], "parent_step_run_id": run["parent_run_id"],
                    "action_start_event_id": provenance.event_id, "operation": evidence.operation,
                    "commands": evidence.commands, "observations": evidence.observations, "effect": evidence.effect}
        payload = _bytes(document)
        if len(payload) > 1024 * 1024:
            _refuse("command observation exceeds its bound")
        relative = work_journal.configured_runtime_root(self.root) / "state/public_release" / hashlib.sha256(run["run_id"].encode()).hexdigest()
        directory = _directory(self.root, relative)
        path = directory / (hashlib.sha256(payload).hexdigest() + ".json")
        try:
            descriptor = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_EXCL | getattr(os, "O_NOFOLLOW", 0), 0o600)
        except FileExistsError:
            existing, status = _regular(self.root, path.relative_to(self.root).as_posix())
            if existing != payload or stat.S_IMODE(status.st_mode) != 0o600:
                _refuse("immutable native evidence differs from its retained carrier")
        else:
            with os.fdopen(descriptor, "wb") as handle:
                os.fchmod(handle.fileno(), 0o600)
                handle.write(payload)
                handle.flush()
                os.fsync(handle.fileno())
            _sync_directory(directory)
        reference = path.relative_to(self.root).as_posix()
        reopened, _ = _regular(self.root, reference)
        if reopened != payload:
            _refuse("native command evidence did not reopen exactly")
        return ToolCallEvidence(reference, reference, (reference,) if evidence.effect else (), (reference,))

    def history(self, parameters, source, pull_request, history_line):
        self.admit("finalize_history_link", parameters, source)
        _pr(pull_request, "actual history PR", release=parameters["release"])
        if history_line != _history_line(source.version_history_summary, pull_request):
            _refuse("history line differs from the actual selected PR")
        original, status = _regular(self.root, source.version_history_ref)
        if hashlib.sha256(original).hexdigest() != source.version_history_sha256:
            _refuse("history source changed before the admitted mutation")
        replacement = _history_payload(original, source.version_history_summary, history_line)
        target = self.root / source.version_history_ref
        descriptor, temporary = tempfile.mkstemp(prefix=".public-history-", dir=target.parent)
        with os.fdopen(descriptor, "wb") as handle:
            os.fchmod(handle.fileno(), stat.S_IMODE(status.st_mode))
            handle.write(replacement)
            handle.flush()
            os.fsync(handle.fileno())
        self.admit("finalize_history_link", parameters, source)
        current, current_status = _regular(self.root, source.version_history_ref)
        if current != original or (current_status.st_dev, current_status.st_ino) != (status.st_dev, status.st_ino):
            _refuse("history carrier changed before atomic publication")
        os.replace(temporary, target)
        _sync_directory(target.parent)
        if _regular(self.root, source.version_history_ref)[0] != replacement:
            _refuse("actual history replacement did not reopen exactly")
        return self.candidate(parameters, "after_history_finalization")

    def gate(self, parameters, source, phase):
        self.admit("run_full_gate:" + phase, parameters, source)
        try:
            from release_public_gate import reopen_public_fresh_gate_inputs
            from release_public_producer import run_public_native_full_gate
            from public_release import FreshPublicNativeFullGateBinding
        except ImportError as error:
            raise SelectedPublicHostError("selected-public-producer-unavailable", "fresh selected public gate producer is unavailable") from error
        inputs = reopen_public_fresh_gate_inputs(self.root, self.session, self.native_n().full_gate_packet, source)
        result = run_public_native_full_gate(inputs)
        call = self.record(NativeCommandEvidence("run_full_gate:" + phase, (),
                           {"producer_result_ref": result.producer_result_ref,
                            "producer_result_sha256": result.producer_result_sha256,
                            "bridge_ref": result.bridge_ref, "bridge_sha256": result.bridge_sha256}, False))
        reports = (*call.report_refs, result.producer_result_ref)
        if result.bridge_ref is not None:
            reports = (*reports, result.bridge_ref)
        return GateResult(ToolCallEvidence(call.input_ref, call.result_ref, (), reports),
                          FreshPublicNativeFullGateBinding(result))


def create_selected_public_bindings(project_root: Path, frozen: Mapping[str, object], session: RunExecutionSession) -> NativePublicReleaseBindings:
    """Construct only program-owned callbacks for the existing admitted Session."""
    host = _SelectedPublicHost(project_root, frozen, session)
    return NativePublicReleaseBindings(host.root, effect_admitter=host.admit,
        candidate_observer=host.candidate, evidence_recorder=host.record,
        history_link_finalizer=host.history, full_gate_runner=host.gate)


__all__ = ["SelectedPublicHostError", "create_selected_public_bindings"]
