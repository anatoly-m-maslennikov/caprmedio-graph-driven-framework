"""One trusted-host confirmation behind the unchanged selected authorization.

Issuance is an INTERNAL host API, called only after actual human review and
exclusive-window confirmation. MCP JSON, hashes and Operator membership cannot
invoke it or prove that confirmation. No runtime provider is configured here.
"""

from __future__ import annotations

import copy
from contextlib import contextmanager
from contextvars import ContextVar
from dataclasses import dataclass
from functools import wraps
import hashlib
import json
from pathlib import Path
import weakref

import atom_operations as operations
from connector_bindings import ConnectorBindingError, FileSource, capture_source
from engine_publication_lock import EnginePublicationLockError, engine_publication_lock
from operator_registry import parse_operators_registry
from workflow_run_support import _canonical_digest, _validate_common


class SubjectPublicationAuthorizationError(ValueError):
    code = "subject-publication-window-unconfirmed"


@dataclass(frozen=True)
class _ConfirmationRecord:
    root: Path
    request_digest: str
    authorization_digest: str
    intent_digest: str
    originals: tuple
    authorities: tuple[FileSource, ...]
    target: FileSource
    target_fingerprint: tuple
    predecessor: FileSource
    operator_name: str
    llm_session: tuple


class SubjectPublicationConfirmation:
    """Nonserializable exact confirmation, issued and retained by this host."""

    __slots__ = ("_record", "__weakref__")

    def __init__(self, *_args, **_kwargs):
        raise TypeError("Subject confirmation is issued only by the trusted host")

    def __setattr__(self, _key, _value):
        raise AttributeError("Subject confirmation is immutable")

    def __reduce__(self):
        raise TypeError("Subject confirmation is not serializable")


_ISSUED: dict = {}
_BOUND: ContextVar = ContextVar("subject_publication_confirmation", default=None)
_ACTIVE: ContextVar = ContextVar("subject_publication_window", default=None)


def _reject(message):
    raise SubjectPublicationAuthorizationError(message)


def _snapshot(record):
    def pin(source):
        return source.root.as_posix(), source.relative_path.as_posix(), source.sha256
    return (record.root.as_posix(), record.request_digest, record.authorization_digest,
            record.intent_digest, record.originals, tuple(pin(source) for source in record.authorities),
            pin(record.target), record.target_fingerprint, pin(record.predecessor),
            record.operator_name, record.llm_session)


def _record(confirmation):
    if type(confirmation) is not SubjectPublicationConfirmation:
        _reject("An actual trusted-host Subject confirmation is required")
    issued = _ISSUED.get(id(confirmation))
    if (issued is None or issued[0]() is not confirmation or confirmation._record is not issued[1]
            or _snapshot(confirmation._record) != issued[3]):
        _reject("Subject confirmation was not issued by this trusted host")
    if issued[2]:
        _reject("Subject publication confirmation has already been consumed")
    return issued[1]


def _originals(root):
    from VALIDATE_ATOMS.validate_atoms_workers.read_io import ReadContext
    from VALIDATE_ATOMS.validate_atoms_workers.settings import CEILINGS
    control = operations.control_root(root)
    reader = ReadContext(roots=[str(root)], limits=dict(CEILINGS))
    return tuple(path.relative_to(root).as_posix() for path in reader.inventory(control)
        if operations._role_directory(path, control) is not None
        and "_projection" not in path.relative_to(control).parts
        and operations._lifecycle(path, control) not in {"draft", "archived"})


def _frontier(root, prepared, execution):
    from VALIDATE_ATOMS.validate_atoms_workers.proposed_carrier import source_context_from_project
    control = operations.control_root(root)
    originals = _originals(root)
    paths = set(originals)
    context = source_context_from_project(root)
    paths.update(Path(item["path"]).relative_to(root).as_posix()
                 for item in context.authority.bindings)
    paths.update((control / name).relative_to(root).as_posix() for name in
                 ("caprmedio_project_settings.toml", "project_structure.toml", "operators_registry.toml"))
    paths.add(execution["definition_manifest"]["manifest_ref"])
    paths.update(item["definition"]["path"] for item in execution["requested_runs"])
    paths.update(pin["path"] for pin in prepared["subject_intent"]["subject_profile_evidence"]["grammar_pins"])
    report_pin = execution["parameters"]["semantic_assessment_report"]
    report_source = capture_source(root, report_pin["path"])
    report_raw = report_source.read_bytes()
    _, body = operations.split_frontmatter(report_raw.decode("utf-8"))
    from lifecycle_intents import _assessment_json
    report = _assessment_json(body)
    paths.add(report_pin["path"])
    paths.update(pin["path"] for pin in (*report["authorityPins"].values(), *report["lineageEvidencePins"]))
    target = prepared["subject_intent"]["target"]["path"]
    return originals, tuple(capture_source(root, path) for path in sorted(paths - {target}))


def authorize_subject_publication(root, execution, *, operator_name, llm_session, staged_manifest):
    """Record an actual human confirmation at the existing trusted-host boundary.

    Calling this internal issuer is the host's confirmation act, not evidence
    extracted from untrusted input. Do not expose it through a serializable route.
    """
    from atom_subject_apply import _parameters, _prepare
    from atom_subject_patch import preview_subject_patches

    root = Path(root).resolve(strict=True)
    execution = copy.deepcopy(_validate_common(execution))
    if execution["mode"] != "execute" or execution["operation_route"] != "update_atom":
        _reject("Confirmation applies only to the exact selected Subject update")
    if (not isinstance(llm_session, dict) or llm_session.keys() != {"app", "uuid"}
            or not all(isinstance(value, str) and value for value in llm_session.values())
            or llm_session["uuid"] != execution["request_id"]):
        _reject("Trusted host session differs from the selected request")
    registry = capture_source(root, operations.control_root(root).relative_to(root) / "operators_registry.toml")
    operators = [item for item in parse_operators_registry(registry.read_bytes()) if item.name == operator_name]
    if len(operators) != 1:
        _reject("Confirming Operator is not uniquely registered")
    request = _parameters(execution["parameters"])
    prepared = _prepare(root, request)
    intent = prepared["subject_intent"]
    if intent["noop"]:
        _reject("An unchanged no-op needs no publication window")
    if not isinstance(staged_manifest, dict) or staged_manifest.keys() != {"path", "digest"}:
        _reject("Reviewed staging requires its exact existing manifest pin")
    staged = FileSource(root, Path(staged_manifest["path"]), staged_manifest["digest"])
    manifest = json.loads(staged.read_bytes())
    if manifest.keys() != {"schema_version", "preview_sha256", "atoms"} or manifest["schema_version"] != 1 or len(manifest["atoms"]) != 1:
        _reject("Reviewed staging must bind exactly one Subject intent")
    atom = manifest["atoms"][0]
    if (atom["subject_intent_sha256"] != request["subject_intent_sha256"]
            or atom["source"] != {"path": intent["target"]["path"], "atom_id": intent["target"]["atom_id"],
                                  "version": intent["target"]["version"], "sha256": intent["target"]["digest"]}):
        _reject("Reviewed staging differs from the exact source-bound intent")
    candidate = FileSource(root, Path(atom["candidate"]["path"]), atom["candidate"]["sha256"])
    candidate_raw = candidate.read_bytes()
    frontmatter, _ = operations.split_frontmatter(candidate_raw.decode("utf-8"))
    illustrative_at = operations.frontmatter_scalar(frontmatter, "updated_at")
    expected = preview_subject_patches(root, [{"selector": request["target"]["path"],
        "expected": {"atom_id": request["target"]["atom_id"], "version": request["target"]["version"],
                     "sha256": request["target"]["digest"]}, "subject_patches": request["subject_patches"]}],
        timestamp=illustrative_at, subject_profile=request.get("subject_profile", "legacy"))
    if candidate_raw != expected["atoms"][0]["proposed_carrier"].encode("utf-8") or manifest["preview_sha256"] != expected["preview_sha256"]:
        _reject("Reviewed candidate differs from the independently reopened preview")
    originals, authorities = _frontier(root, prepared, execution)
    archive = capture_source(root, intent["predecessorArchive"]["path"])
    if archive.sha256 is not None:
        _reject("Pre-existing history cannot be included as attempt-owned absence")
    target_raw, target_fingerprint = operations.read_raw_atom_revision(root, root / intent["target"]["path"])
    if hashlib.sha256(target_raw).hexdigest() != intent["target"]["digest"]:
        _reject("Reviewed current Carrier changed during confirmation")
    record = _ConfirmationRecord(root, _canonical_digest(execution), _canonical_digest(execution["operator_authorization"]),
              request["subject_intent_sha256"], originals, (*authorities, registry, staged, candidate),
              FileSource(root, Path(intent["target"]["path"]), intent["target"]["digest"]), target_fingerprint, archive,
              operator_name, tuple(sorted(llm_session.items())))
    confirmation = object.__new__(SubjectPublicationConfirmation)
    object.__setattr__(confirmation, "_record", record)
    identity = id(confirmation)
    _ISSUED[identity] = (weakref.ref(confirmation, lambda _: _ISSUED.pop(identity, None)), record, False,
                         _snapshot(record))
    return confirmation


@contextmanager
def bind_subject_publication_confirmation(confirmation):
    _record(confirmation)
    token = _BOUND.set(confirmation)
    try:
        yield
    finally:
        _BOUND.reset(token)


def require_subject_publication_window(root, request, intent):
    record = _record(_BOUND.get())
    active = _ACTIVE.get()
    if (active is None or active[0] != record.root or active[0] != Path(root).resolve()
            or active[1] != _canonical_digest(request) or active[2] != intent
            or record.intent_digest != request["subject_intent_sha256"]):
        _reject("The exact trusted publication window is not active")


def revalidate_subject_publication_authority(root, request, intent):
    """Observe unchanged governing/review evidence after the actual readback."""
    require_subject_publication_window(root, request, intent)
    record = _record(_BOUND.get())
    if _originals(record.root) != record.originals:
        _reject("The confirmed original-identity frontier changed")
    for source in record.authorities:
        source.revalidate()


def with_subject_publication_window(action):
    """Hold shared ownership through the complete action and caught restoration."""
    @wraps(action)
    def admitted(root, parameters, **kwargs):
        if kwargs.get("execute") is not True:
            return action(root, parameters, **kwargs)
        from atom_subject_apply import _parameters, _prepare
        request = _parameters(parameters)
        prepared = _prepare(Path(root).resolve(), request)
        if prepared["subject_intent"]["noop"]:
            return action(root, parameters, **kwargs)
        confirmation = _BOUND.get()
        if confirmation is None:
            return action(root, parameters, **kwargs)
        result = None
        try:
            record = _record(confirmation)
            session = kwargs.get("session")
            if (record.root != Path(root).resolve() or session is None
                    or record.request_digest != _canonical_digest(session.request)
                    or record.authorization_digest != _canonical_digest(session.request["operator_authorization"])
                    or record.intent_digest != request["subject_intent_sha256"]):
                _reject("Confirmation differs from this exact admitted Session/intent")
            with engine_publication_lock(root):
                fresh = _prepare(Path(root).resolve(), request)
                originals, _ = _frontier(record.root, fresh, session.request)
                if originals != record.originals:
                    _reject("The confirmed original-identity frontier changed")
                for source in (*record.authorities, record.target, record.predecessor):
                    source.revalidate()
                _, target_fingerprint = operations.read_raw_atom_revision(root, root / record.target.relative_path)
                if target_fingerprint != record.target_fingerprint:
                    _reject("Reviewed current Carrier identity or mode changed")
                token = _ACTIVE.set((record.root, _canonical_digest(request), fresh["subject_intent"]))
                try:
                    result = action(root, parameters, **kwargs)
                finally:
                    _ACTIVE.reset(token)
                    issued = _ISSUED[id(confirmation)]
                    _ISSUED[id(confirmation)] = (issued[0], record, True, issued[3])
            return result
        except (SubjectPublicationAuthorizationError, ConnectorBindingError) as error:
            from lifecycle_intents import LifecycleError
            raise LifecycleError("subject-publication-window-unconfirmed", str(error)) from error
        except EnginePublicationLockError as error:
            if result is not None and result.get("outcome") in {"applied", "partial"}:
                intent = prepared["subject_intent"]
                return {**result, "outcome": "partial", "failure": {"code": error.code},
                    "effects": [{**effect, "state": "unknown"} for effect in result.get("effects", [])],
                    "recovery": {"automatic_retry": False, "inspection_required": True},
                    "unknown_remainder": [intent["target"]["path"], intent["predecessorArchive"]["path"]]}
            from lifecycle_intents import LifecycleError
            raise LifecycleError(error.code, str(error)) from error
    return admitted
