"""Private receiving-adapter bindings; this module admits no new Tool or route.

The receiver supplies its existing selected service, schema validator and private
logical-to-carrier mapping. Public requests cannot provide any of those objects.
Schema/source-view selection and result verification remain adapter-owned.
"""

from __future__ import annotations

import copy
import hashlib
import os
import stat
from collections.abc import Callable, Collection, Mapping
from dataclasses import dataclass
from pathlib import Path

from connector_contract import ERROR_CODES, validate_request
from VALIDATE_ATOMS.validate_atoms_workers.read_io import open_regular, protected
from workflow_run_support import (
    RunTracker, SelectedRunError, _canonical_digest, _common_bytes, _proposal, _validate_common,
)


class ConnectorBindingError(ValueError):
    """A pre-effect refusal in the common connector error vocabulary."""

    def __init__(self, code: str, message: str, field: str | None = None):
        if code not in ERROR_CODES:
            raise ValueError("Unknown connector error code.")
        self.code, self.message, self.field = code, message, field
        super().__init__(message)

    def record(self) -> dict:
        return {"code": self.code, "message": self.message, "field": self.field}


def _private_path(root: Path, relative_path: str | Path) -> Path:
    relative = Path(relative_path)
    if relative.is_absolute() or relative == Path(".") or ".." in relative.parts:
        raise ConnectorBindingError("input_invalid", "Invalid private source binding.", "context")
    path = root / relative
    if protected(path) or path.resolve() != path:
        raise ConnectorBindingError("permission_denied", "Private source binding is unsafe.", "context")
    return path


def _read_source(path: Path) -> bytes | None:
    try:
        with os.fdopen(open_regular(path), "rb") as stream:
            before = os.fstat(stream.fileno())
            if not stat.S_ISREG(before.st_mode):
                raise ConnectorBindingError("backend_failure", "Source is not a regular file.", "context")
            raw = stream.read()
            after = os.fstat(stream.fileno())
            fields = ("st_dev", "st_ino", "st_size", "st_mtime_ns", "st_ctime_ns")
            if any(getattr(before, key) != getattr(after, key) for key in fields):
                raise ConnectorBindingError("stale_state", "Source changed during observation.", "expected_state")
            return raw
    except FileNotFoundError:
        return None
    except OSError as error:
        raise ConnectorBindingError("backend_failure", "Source cannot be observed.", "context") from error


@dataclass(frozen=True)
class FileSource:
    """An exact private file/absence pin, never a public physical selector."""

    root: Path
    relative_path: Path
    sha256: str | None

    def _observe(self) -> bytes | None:
        raw = _read_source(_private_path(self.root, self.relative_path))
        digest = hashlib.sha256(raw).hexdigest() if raw is not None else None
        if digest != self.sha256:
            raise ConnectorBindingError("stale_state", "Bound source is no longer current.", "expected_state")
        return raw

    def read_bytes(self) -> bytes:
        raw = self._observe()
        if raw is None:
            raise ConnectorBindingError("target_not_found", "Bound source is absent.", "target")
        return raw

    def revalidate(self) -> None:
        self._observe()


def capture_source(root: str | Path, relative_path: str | Path) -> FileSource:
    """Observe a receiver-resolved source; unpinned reads need no caller digest."""
    project_root = Path(root).resolve(strict=True)
    path = _private_path(project_root, relative_path)
    raw = _read_source(path)
    return FileSource(project_root, path.relative_to(project_root),
                      hashlib.sha256(raw).hexdigest() if raw is not None else None)


class SelectedOperationAdmission:
    """Reuse an existing D527 service's exact admission, without effect flags.

    The receiver supplies the RunTracker, its execute request and the one
    mapping that extracts the inner request and context reference from that
    admitted request. Missing mapping fails closed; no public placement is chosen.
    """

    def __init__(
        self, tracker: RunTracker, outer_request: Mapping, *,
        map_request: Callable[[dict], tuple[dict, object]] | None = None,
    ):
        if not isinstance(tracker, RunTracker):
            raise TypeError("Existing selected RunTracker is required.")
        self._tracker = tracker
        self._outer_request = copy.deepcopy(dict(outer_request))
        self._map_request = map_request

    def check(self, request: dict) -> None:
        try:
            outer = _validate_common(self._outer_request)
            fingerprint = _common_bytes(outer)
            recorded = self._tracker._requests.get(outer["request_id"])
            if recorded is not None and recorded != fingerprint:
                raise SelectedRunError("request-id-conflict", "request_id was already used with different canonical request bytes")
            self._tracker._requests.setdefault(outer["request_id"], fingerprint)
            if outer["mode"] != "execute":
                raise ConnectorBindingError("permission_denied", "Preview has no execution permission.", "authorization")
            if self._map_request is None:
                raise ConnectorBindingError("input_invalid", "Receiving request/context mapping is unavailable.", "context")
            mapped = self._map_request(copy.deepcopy(outer))
            if not isinstance(mapped, tuple) or len(mapped) != 2 or not isinstance(mapped[0], dict):
                raise ConnectorBindingError("input_invalid", "Receiving request/context mapping is invalid.", "context")
            inner, context_reference = mapped
            if _canonical_digest(request) != _canonical_digest(inner):
                raise ConnectorBindingError("permission_denied", "Logical request differs from admitted parameters.", "context")
            if _canonical_digest(request["context"]) != _canonical_digest(context_reference):
                raise ConnectorBindingError("input_invalid", "Context reference is unresolved.", "context")
            observation = self._tracker._observe(outer)
            if not observation["selected"] or not observation["current"]:
                raise ConnectorBindingError("stale_state", "Selected source binding is not current.", "context")
            proposal = _proposal(outer, observation)
            self._tracker._validate_execute(outer, proposal, _canonical_digest(proposal))
            if request["authorization"] != outer["operator_authorization"]["authorization_ref"]:
                raise ConnectorBindingError("permission_denied", "Permission reference is not bound.", "authorization")
        except SelectedRunError as error:
            code = "stale_state" if error.code in {"stale-preview", "stale-authorization"} else "permission_denied"
            raise ConnectorBindingError(code, str(error), "authorization") from error
        except (KeyError, TypeError, ValueError, OSError) as error:
            if isinstance(error, ConnectorBindingError):
                raise
            raise ConnectorBindingError("backend_failure", "Receiving binding could not be resolved.", "context") from error


class ConnectorBindings:
    """Receiver-owned schema, authority pins and private storage resolution."""

    def __init__(
        self, admission: SelectedOperationAdmission, *, supported_operations: Collection[str],
        supported_kinds: Collection[str], validate_payload: Callable[[dict], None],
        resolve_sources: Callable[[dict], Collection[FileSource]], authority_sources: Collection[FileSource],
    ):
        if not isinstance(admission, SelectedOperationAdmission):
            raise TypeError("Existing selected admission binding is required.")
        self._admission = admission
        self._operations, self._kinds = frozenset(supported_operations), frozenset(supported_kinds)
        self._validate_payload, self._resolve_sources = validate_payload, resolve_sources
        self._authority_sources = tuple(authority_sources)
        if not self._authority_sources or any(not isinstance(source, FileSource) or source.sha256 is None
                                              for source in self._authority_sources):
            raise ValueError("Existing schema/source authority pins are required.")

    def _check(self, request: dict) -> None:
        errors = validate_request(request, supported_operations=self._operations, supported_kinds=self._kinds)
        if errors:
            error = errors[0]
            raise ConnectorBindingError(error["code"], error["message"], error["field"])
        for source in self._authority_sources:
            source.revalidate()
        self._admission.check(request)
        if self._validate_payload(copy.deepcopy(request)) is not None:
            raise ConnectorBindingError("schema_invalid", "Payload validator must raise on refusal, not return an approval flag.", "context")

    def bind(self, request: dict) -> BoundRequest:
        errors = validate_request(request, supported_operations=self._operations, supported_kinds=self._kinds)
        if errors:
            error = errors[0]
            raise ConnectorBindingError(error["code"], error["message"], error["field"])
        request = copy.deepcopy(request)
        self._check(request)
        sources = tuple(self._resolve_sources(copy.deepcopy(request)))
        if any(not isinstance(source, FileSource) for source in sources):
            raise ConnectorBindingError("backend_failure", "Private resolution returned an invalid source binding.", "context")
        if len({(source.root, source.relative_path) for source in sources}) != len(sources):
            raise ConnectorBindingError("target_ambiguous", "Private resolution contains duplicate sources.", "target")
        for source in sources:
            source.revalidate()
        return BoundRequest(request, sources, self)


@dataclass(frozen=True)
class BoundRequest:
    request: dict
    sources: tuple[FileSource, ...]
    _bindings: ConnectorBindings

    def revalidate_before_effect(self) -> None:
        current = self._bindings.bind(self.request)
        if current.sources != self.sources:
            raise ConnectorBindingError("stale_state", "Private source resolution changed after binding.", "context")
