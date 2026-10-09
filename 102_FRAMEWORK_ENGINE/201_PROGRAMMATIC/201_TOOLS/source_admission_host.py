"""Host-only assembly of D602 source-admission invocation evidence.

This module is deliberately a narrow seam, not an authorization system or an
O199 route/CLI implementation.  A future trusted host may supply
``command_binder`` after it has verified an explicit Operator command.  The
current generic selected-workflow CLI does not provide that binding and must
not use this helper as though it did.
"""

from __future__ import annotations

import hashlib
import os
import re
import stat
import tomllib
from collections.abc import Callable, Mapping
from pathlib import Path, PurePosixPath
from typing import Any

from source_catalog_admission import AdmissionInvocationRequest, TrustedSourceAdmissionInvocation
from workflow_run_support import RecordedActionStartProvenance, RunExecutionSession, SelectedRunError


O199_ACTION_ID = "CA-O-199"
_SHA256 = re.compile(r"[0-9a-f]{64}")


class SourceAdmissionHostError(RuntimeError):
    """Stable refusal from the host-only source-admission assembly seam."""

    def __init__(self, code: str, message: str) -> None:
        self.code = code
        super().__init__(f"{code}: {message}")


# The host owns this callback.  It receives the re-opened facts, including the
# exact snapshot request, and returns only the registered Operator identity and
# its canonical command reference.  No caller-provided authorization mapping is
# admitted at this boundary.
SourceAdmissionCommandBinder = Callable[
    [AdmissionInvocationRequest, RecordedActionStartProvenance], tuple[str, str]
]


def _refuse(code: str, message: str) -> None:
    raise SourceAdmissionHostError(code, message)


def _root(value: str | Path) -> Path:
    try:
        supplied = Path(value)
        resolved = supplied.resolve(strict=True)
    except (OSError, TypeError, ValueError) as error:
        raise SourceAdmissionHostError("source-admission-host-root-invalid", "Project root is unavailable") from error
    if supplied.is_symlink() or resolved.is_symlink() or not resolved.is_dir():
        _refuse("source-admission-host-root-invalid", "Project root must be a regular directory")
    return resolved


def _safe_relative(value: object, *, field: str) -> PurePosixPath:
    if not isinstance(value, str) or not value or "\\" in value:
        _refuse("source-admission-host-context-invalid", f"{field} must be a non-empty normalized relative path")
    relative = PurePosixPath(value)
    if relative.is_absolute() or relative == PurePosixPath(".") or any(part in {"", ".", ".."} for part in relative.parts):
        _refuse("source-admission-host-context-invalid", f"{field} is unsafe")
    if any(part.startswith(".env") or part.endswith(".env") for part in relative.parts):
        _refuse("source-admission-host-context-invalid", f"{field} names protected state")
    return relative


def _regular_bytes(root: Path, relative: PurePosixPath, *, code: str, label: str) -> bytes:
    cursor = root
    try:
        for index, part in enumerate(relative.parts):
            cursor = cursor / part
            metadata = os.lstat(cursor)
            expected = stat.S_ISREG if index == len(relative.parts) - 1 else stat.S_ISDIR
            if stat.S_ISLNK(metadata.st_mode) or not expected(metadata.st_mode):
                _refuse(code, f"{label} is aliased or has an invalid carrier type")
        return cursor.read_bytes()
    except SourceAdmissionHostError:
        raise
    except OSError as error:
        raise SourceAdmissionHostError(code, f"{label} is unavailable") from error


def _definition(context: Mapping[str, Any]) -> tuple[PurePosixPath, str, tuple[str, int, str, str]]:
    if context.get("action_definition_id") != O199_ACTION_ID:
        _refuse("source-admission-host-action-invalid", "selected Action is not CA-O-199")
    definition = context.get("action_definition")
    if (not isinstance(definition, Mapping) or definition.get("atom_id") != O199_ACTION_ID
            or definition.get("kind") != "action"):
        _refuse("source-admission-host-action-invalid", "selected Action definition is not CA-O-199")
    version = definition.get("version")
    digest = definition.get("sha256")
    if type(version) is not int or version < 1 or not isinstance(digest, str) or _SHA256.fullmatch(digest) is None:
        _refuse("source-admission-host-action-invalid", "selected CA-O-199 definition binding is invalid")
    relative = _safe_relative(definition.get("path"), field="action_definition.path")
    return relative, digest, (O199_ACTION_ID, version, relative.as_posix(), digest)


def _current_action_source(root: Path, relative: PurePosixPath, expected_sha256: str) -> bytes:
    payload = _regular_bytes(
        root, relative,
        code="source-admission-host-source-stale",
        label="selected CA-O-199 source",
    )
    if hashlib.sha256(payload).hexdigest() != expected_sha256:
        _refuse("source-admission-host-source-stale", "selected CA-O-199 source differs from its binding")
    return payload


def _registered_operator(root: Path, registry_ref: PurePosixPath, author: str) -> bytes:
    payload = _regular_bytes(
        root, registry_ref,
        code="source-admission-host-operator-invalid",
        label="registered Operator evidence",
    )
    try:
        document = tomllib.loads(payload.decode("utf-8"))
    except (UnicodeDecodeError, tomllib.TOMLDecodeError) as error:
        raise SourceAdmissionHostError(
            "source-admission-host-operator-invalid", "registered Operator evidence is invalid",
        ) from error
    operators = document.get("operators") if isinstance(document, Mapping) else None
    matching = [
        row for row in operators if isinstance(row, Mapping) and row.get("name") == author
    ] if isinstance(operators, list) else []
    if len(matching) != 1:
        _refuse(
            "source-admission-host-operator-invalid",
            "reopened Journal author is not one uniquely registered Operator",
        )
    return payload


def _provenance(session: RunExecutionSession, action_run_id: str) -> RecordedActionStartProvenance:
    try:
        observed = session.read_recorded_action_start(action_run_id)
    except SelectedRunError as error:
        raise SourceAdmissionHostError(
            "source-admission-host-start-invalid", "recorded CA-O-199 Action start cannot be reopened",
        ) from error
    if observed.action_run_id != action_run_id:
        _refuse("source-admission-host-start-invalid", "reopened Action start has a different actual Run")
    return observed


def _actual_action_binding(
    session: RunExecutionSession,
    *,
    root: Path,
    requested_action_run_id: str,
    action_run_id: str,
    expected: tuple[str, int, str, str],
    code: str,
) -> tuple[str, int, str, str]:
    """Match the frozen selected binding against the Session's actual Run."""

    tracker_root = getattr(getattr(session, "tracker", None), "root", None)
    try:
        same_root = isinstance(tracker_root, (str, Path)) and _root(tracker_root) == root
    except SourceAdmissionHostError:
        same_root = False
    actual = session.actual.get(requested_action_run_id)
    definition = actual.get("definition") if isinstance(actual, Mapping) else None
    if (
        not same_root
        or not isinstance(actual, Mapping)
        or actual.get("run_id") != action_run_id
        or actual.get("kind") != "action"
        or not isinstance(definition, Mapping)
    ):
        _refuse(code, "selected Action context is not the actual CA-O-199 Run")
    observed = (
        definition.get("atom_id"), definition.get("version"),
        definition.get("path"), definition.get("digest"),
    )
    if observed != expected:
        _refuse(code, "actual Action definition differs from the captured CA-O-199 binding")
    return expected


def _binder_result(value: object, *, author: str) -> tuple[str, str]:
    if type(value) is not tuple or len(value) != 2:
        _refuse("source-admission-host-command-invalid", "trusted command binder must return Operator and command_ref")
    operator, command_ref = value
    if (
        not isinstance(operator, str)
        or not operator
        or any(character in operator for character in "\x00\r\n")
        or not isinstance(command_ref, str)
        or not command_ref
        or len(command_ref) > 512
        or any(character in command_ref for character in "\x00\r\n")
    ):
        _refuse("source-admission-host-command-invalid", "trusted command binder returned invalid command evidence")
    if operator != author:
        _refuse("source-admission-host-command-invalid", "trusted command Operator differs from reopened Journal author")
    return operator, command_ref


def make_source_admission_invocation_admitter(
    project_root: str | Path,
    *,
    selected_context: Mapping[str, Any],
    operators_registry_ref: str,
    command_binder: SourceAdmissionCommandBinder,
) -> Callable[[AdmissionInvocationRequest], TrustedSourceAdmissionInvocation]:
    """Return the D602 callback for one exact, already-started CA-O-199 Action.

    The factory accepts a context created by selected execution, not enqueue
    request JSON.  It captures only the actual Session/Run and source binding;
    ``parameters``, ``assigned_action_id``, and generic authorization fields
    are intentionally ignored.  The host must provide its selected
    Project-context ``operators_registry_ref`` and ``command_binder``.
    """

    root = _root(project_root)
    if not isinstance(selected_context, Mapping) or selected_context.get("sealed_outer_admission") is not True:
        _refuse("source-admission-host-context-invalid", "an exact selected Action context is required")
    context_root = selected_context.get("project_root")
    if not isinstance(context_root, (str, Path)) or _root(context_root) != root:
        _refuse("source-admission-host-context-invalid", "selected Action context belongs to another Project")
    session = selected_context.get("session")
    action_run_id = selected_context.get("action_run_id")
    requested_action_run_id = selected_context.get("requested_action_run_id")
    if (not isinstance(session, RunExecutionSession) or not isinstance(action_run_id, str) or not action_run_id
            or not isinstance(requested_action_run_id, str) or not requested_action_run_id):
        _refuse("source-admission-host-context-invalid", "selected Action context lacks its actual Session and Run")
    if not callable(command_binder):
        _refuse("source-admission-host-command-required", "source admission requires a trusted host command binder")
    registry_ref = _safe_relative(operators_registry_ref, field="operators_registry_ref")
    source_relative, source_sha256, expected_actual_binding = _definition(selected_context)
    _actual_action_binding(
        session,
        root=root,
        requested_action_run_id=requested_action_run_id,
        action_run_id=action_run_id,
        expected=expected_actual_binding,
        code="source-admission-host-context-invalid",
    )

    def admit(request: AdmissionInvocationRequest) -> TrustedSourceAdmissionInvocation:
        if not isinstance(request, AdmissionInvocationRequest) or _SHA256.fullmatch(request.snapshot_sha256) is None:
            _refuse("source-admission-host-request-invalid", "source admission requires the exact typed snapshot request")
        before_start = _provenance(session, action_run_id)
        before_actual = _actual_action_binding(
            session,
            root=root,
            requested_action_run_id=requested_action_run_id,
            action_run_id=action_run_id,
            expected=expected_actual_binding,
            code="source-admission-host-context-invalid",
        )
        before_registry = _registered_operator(root, registry_ref, before_start.author)
        before_source = _current_action_source(root, source_relative, source_sha256)
        try:
            bound = command_binder(request, before_start)
        except SourceAdmissionHostError:
            raise
        except Exception as error:
            raise SourceAdmissionHostError(
                "source-admission-host-command-rejected", "trusted host command binder rejected the Action invocation",
            ) from error
        operator, command_ref = _binder_result(bound, author=before_start.author)
        after_actual = _actual_action_binding(
            session,
            root=root,
            requested_action_run_id=requested_action_run_id,
            action_run_id=action_run_id,
            expected=expected_actual_binding,
            code="source-admission-host-context-stale",
        )
        after_start = _provenance(session, action_run_id)
        after_registry = _registered_operator(root, registry_ref, after_start.author)
        after_source = _current_action_source(root, source_relative, source_sha256)
        if after_start != before_start:
            _refuse("source-admission-host-start-stale", "recorded Action start changed while binding the command")
        if after_actual != before_actual:
            _refuse("source-admission-host-context-stale", "actual CA-O-199 Run changed while binding the command")
        if after_registry != before_registry:
            _refuse("source-admission-host-operator-stale", "registered Operator evidence changed while binding the command")
        if after_source != before_source:
            _refuse("source-admission-host-source-stale", "selected CA-O-199 source changed while binding the command")
        return TrustedSourceAdmissionInvocation(
            snapshot_sha256=request.snapshot_sha256,
            operator=operator,
            command_ref=command_ref,
            action_run_id=before_start.action_run_id,
        )

    return admit


__all__ = [
    "O199_ACTION_ID",
    "SourceAdmissionCommandBinder",
    "SourceAdmissionHostError",
    "make_source_admission_invocation_admitter",
]
