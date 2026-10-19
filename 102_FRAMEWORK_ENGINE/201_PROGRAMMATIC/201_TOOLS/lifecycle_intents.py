"""Shared no-mutation lifecycle-intent support for CA-R-1041 and CA-R-1042."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import sys
from collections.abc import Callable, Mapping
from dataclasses import replace
from pathlib import Path
from typing import Any

import yaml

from authoritative_status_models import StatusModelError, resolve_status_model
from artifact_metadata import current_timestamp, project_identity
from atom_operations import (
    Atom,
    _atomic_write,
    ToolError as AtomToolError,
    archive_atom_revision,
    atom_id_has_preserved_history_evidence,
    atom_identity_lock,
    atom_digest,
    atom_from_path,
    atom_version,
    canonical_json,
    carrier_directory_snapshot,
    carrier_directory_snapshot_matches,
    control_root,
    create_atom_revision,
    demote_atom_to_draft,
    frontmatter_scalar,
    migrate_atom_identity_revision,
    move_atom_revision,
    prepare_create_atom_revision,
    preserve_atom_revision,
    project_identity_prefix,
    promote_draft_atom,
    publish_status_atom_revision,
    status_bundle_snapshot,
    require_current_atom,
    remove_frontmatter_scalar,
    render,
    replace_frontmatter_scalar,
    resolve_repository,
    resolve_selector,
    safe_path,
    scan_atoms,
    split_frontmatter,
    write_atom_revision,
)
from project_selection import ProjectSelectionError, active_selection


ATOM_ID = re.compile(r"^CA-[A-Z]+-[0-9]{3,}$")
INACTIVE_LIFECYCLE_SEGMENTS = frozenset({"archive", "drafts", "done", "solved", "resolved", "canceled", "cancelled"})


class IntentError(RuntimeError):
    """Return one deterministic lifecycle-intent diagnostic."""

    def __init__(self, code: str, message: str) -> None:
        self.code = code
        super().__init__(message)


class LifecycleError(IntentError):
    """A route-local lifecycle diagnostic for the shared selected-run caller."""

    def __init__(self, code: str, message: str) -> None:
        super().__init__(code, f"{code}: {message}")


def load_payload(source: str) -> dict[str, Any]:
    """Read one JSON request for CA-M-128 or CA-M-129."""
    try:
        raw = sys.stdin.read() if source == "-" else Path(source).read_text(encoding="utf-8")
        payload = json.loads(raw)
    except OSError as error:
        raise IntentError("input-unreadable", "--input must name a readable JSON object") from error
    except json.JSONDecodeError as error:
        raise IntentError("input-json-invalid", "--input must contain one JSON object") from error
    if not isinstance(payload, dict):
        raise IntentError("input-json-invalid", "--input must contain one JSON object")
    return payload


def active_atoms(root: Path) -> dict[str, list[Atom]]:
    """Index active Atom IDs without rejecting unrelated duplicate identities."""
    try:
        atoms = scan_atoms(root)
    except AtomToolError as error:
        raise IntentError(error.code, str(error)) from error
    result: dict[str, list[Atom]] = {}
    for atom in atoms:
        if atom.atom_id is None or any(part.casefold() in INACTIVE_LIFECYCLE_SEGMENTS for part in atom.path.parts):
            continue
        result.setdefault(atom.atom_id, []).append(atom)
    return result


def required_atom_id(payload: Mapping[str, Any], field: str) -> str:
    """Read one canonical Atom ID supplied by the operator."""
    value = payload.get(field)
    if not isinstance(value, str) or not ATOM_ID.fullmatch(value):
        raise IntentError("atom-id-invalid", f"{field} must be an exact Atom ID such as CA-R-1041")
    return value


def required_context(payload: Mapping[str, Any]) -> dict[str, Any]:
    """Preserve explicit action context without giving it graph meaning."""
    value = payload.get("action_context")
    if not isinstance(value, Mapping):
        raise IntentError("action-context-required", "action_context must be a JSON object")
    return dict(value)


def optional_active_ids(payload: Mapping[str, Any], field: str, atoms: Mapping[str, list[Atom]]) -> list[str]:
    """Resolve supplied Atom IDs without inferring omitted participants."""
    value = payload.get(field, [])
    if not isinstance(value, list) or any(not isinstance(item, str) for item in value):
        raise IntentError("atom-id-list-invalid", f"{field} must be an array of exact Atom IDs")
    if len(value) != len(set(value)):
        raise IntentError("atom-id-list-duplicate", f"{field} must not repeat one Atom ID")
    for item in value:
        if not ATOM_ID.fullmatch(item):
            raise IntentError("active-atom-required", f"{field} contains no active Atom: {item}")
        active_atom(item, atoms)
    return list(value)


def active_atom(atom_id: str, atoms: Mapping[str, list[Atom]]) -> Atom:
    """Return one requested active carrier and reject only its duplicate identity."""
    matches = atoms.get(atom_id, [])
    if not matches:
        raise IntentError("active-atom-required", f"no active Atom has ID {atom_id}")
    if len(matches) != 1:
        raise IntentError("active-atom-id-ambiguous", f"more than one active Atom has ID {atom_id}")
    return matches[0]


def carrier(atom: Atom) -> dict[str, str]:
    """Project the minimal carrier locator needed for a later handoff."""
    assert atom.atom_id is not None
    return {"atom_id": atom.atom_id, "path": atom.relative, "lifecycle": atom.lifecycle}


def deferred_handoff(tool_id: str, operation: str, atom_ids: Mapping[str, Any], action_context: Mapping[str, Any]) -> dict[str, Any]:
    """Describe the explicit non-executable pipeline handoff boundary."""
    return {
        "contract_version": 1,
        "producer": tool_id,
        "operation": operation,
        "atom_ids": dict(atom_ids),
        "action_context": dict(action_context),
        "relation_inference": "not_performed",
        "status": "deferred",
        "reason": "COMMIT_CONTEXT has no admitted lifecycle-intent input contract",
    }


def envelope(tool_id: str, *, ok: bool, mode: str, result: Mapping[str, Any] | None = None, error: BaseException | None = None) -> dict[str, Any]:
    """Produce the common machine-readable Tool envelope."""
    value: dict[str, Any] = {"schema_version": 1, "tool": {"capability_id": tool_id, "kind": "doer"}, "ok": ok, "mode": mode, "diagnostics": []}
    if error is not None:
        value["diagnostics"] = [{"code": getattr(error, "code", "operation-failed"), "message": str(error)}]
    if result is not None:
        value["result"] = dict(result)
    return value


def run_cli(tool_id: str, input_schema: Mapping[str, Any], build_intent: Callable[[Path, Mapping[str, Any]], dict[str, Any]]) -> int:
    """Run one lifecycle Doer as describe, dry-run, or blocked apply."""
    parser = argparse.ArgumentParser(prog=tool_id.lower().replace("_", "-"))
    parser.add_argument("--repository", default=".", help="CAPRMEDIO repository root")
    commands = parser.add_subparsers(dest="command", required=True)
    commands.add_parser("describe", help="print capability and input contract")
    run = commands.add_parser("run", help="validate and describe one lifecycle intent")
    run.add_argument("--input", required=True, metavar="JSON_FILE_OR_DASH")
    run.add_argument("--apply", action="store_true", help="currently blocked before all mutation")
    args = parser.parse_args()
    if args.command == "describe":
        print(json.dumps(envelope(tool_id, ok=True, mode="describe", result={"input_schema": dict(input_schema), "mutation_default": "dry-run", "apply_status": "blocked"}), sort_keys=True, separators=(",", ":")))
        return 0
    try:
        result = build_intent(resolve_repository(args.repository), load_payload(args.input))
        if args.apply:
            error = IntentError("apply-blocked", "lifecycle-intent serialization is not admitted by the commit pipeline")
            print(json.dumps(envelope(tool_id, ok=False, mode="apply-blocked", result=result, error=error), sort_keys=True, separators=(",", ":")))
            return 2
        print(json.dumps(envelope(tool_id, ok=True, mode="dry-run", result=result), sort_keys=True, separators=(",", ":")))
        return 0
    except (IntentError, AtomToolError, OSError) as error:
        print(json.dumps(envelope(tool_id, ok=False, mode="apply-blocked" if args.apply else "dry-run", error=error), sort_keys=True, separators=(",", ":")))
        return 2


# CA-D-531 action API -------------------------------------------------------
#
# These are deliberately route-local effects.  The shared selected-run support
# owns the outer request, receipt, authorization seal, Run/Event identities,
# recording state, and retry.  A caller reaches an actual mutation only after
# it has admitted the outer request and passes execute=True, authorized=True.

_DESCRIPTOR_FIELDS = frozenset({"atom_id", "path", "filename", "version", "digest", "lifecycle", "status", "updated_at", "content_role", "type"})
_CARRIER_FIELDS = frozenset({"path", "frontmatter", "content"})
_UPDATE_CLASSES = frozenset({"carrier_only", "equivalent_refinement", "semantic_revision"})
_ATOM_REFERENCE = re.compile(r"\bCA-[A-Z]+-[0-9]+\b")


def _mapping(value: object, name: str) -> dict[str, Any]:
    if not isinstance(value, Mapping):
        raise LifecycleError("mapping-required", f"{name} must be one object")
    return dict(value)


def _exact_fields(value: Mapping[str, Any], fields: frozenset[str], name: str) -> None:
    missing = sorted(fields - value.keys())
    unknown = sorted(value.keys() - fields)
    if missing or unknown:
        detail = ", ".join(([f"missing {item}" for item in missing] + [f"unknown {item}" for item in unknown]))
        raise LifecycleError("carrier-fields-invalid", f"{name} must carry exactly its complete fields ({detail})")


def _translate(error: AtomToolError) -> LifecycleError:
    return LifecycleError(error.code, error.message)


def carrier_descriptor(root: Path, selector: str | Atom) -> dict[str, Any]:
    """Return the complete, serializable current Carrier seal for one Atom."""

    root = root.resolve()
    try:
        atom = selector if isinstance(selector, Atom) else resolve_selector(root, selector)
        return {
            "atom_id": atom.atom_id,
            "path": atom.relative,
            "filename": atom.filename,
            "version": atom_version(atom),
            "digest": atom_digest(atom),
            "lifecycle": atom.lifecycle,
            "status": frontmatter_scalar(atom.frontmatter, "status"),
            "updated_at": frontmatter_scalar(atom.frontmatter, "updated_at"),
            "content_role": frontmatter_scalar(atom.frontmatter, "content_role"),
            "type": frontmatter_scalar(atom.frontmatter, "type"),
        }
    except AtomToolError as error:
        raise _translate(error) from error


def _resolve_descriptor(root: Path, value: object, *, name: str, active: bool = True) -> Atom:
    if not isinstance(value, Mapping) and name in {"target", "predecessor"}:
        raise LifecycleError("one-target-required", f"{name} must name exactly one complete carrier set")
    descriptor = _mapping(value, name)
    _exact_fields(descriptor, _DESCRIPTOR_FIELDS, name)
    if not isinstance(descriptor["path"], str):
        raise LifecycleError("carrier-path-invalid", f"{name}.path must be a repository-relative string")
    try:
        atom = atom_from_path(root, safe_path(root, descriptor["path"], must_exist=True))
        require_current_atom(root, atom)
        observed = carrier_descriptor(root, atom)
    except AtomToolError as error:
        raise _translate(error) from error
    for field in _DESCRIPTOR_FIELDS:
        if descriptor[field] != observed[field]:
            raise LifecycleError("stale-carrier", f"{name} {field} no longer matches the observed carrier")
    if active and atom.lifecycle != "active":
        raise LifecycleError("active-carrier-required", f"{name} must resolve one active carrier")
    return atom


def _resolve_legacy_descriptor(root: Path, value: object, proof_value: object, *, mapped_identity: str | None = None) -> Atom:
    """Read one explicitly sealed historical carrier, never a lookup fallback.

    Only Update accepts this migration input.  The assigned filename identity
    must already exist in the exact committed bytes supplied by the caller;
    this cannot assign an identity to a draft or repair a colliding identity.
    An explicit mapping may encode an assigned pre-current-format identity;
    it never renumbers an already canonical assigned identity.
    """
    descriptor = _mapping(value, "target")
    _exact_fields(descriptor, _DESCRIPTOR_FIELDS, "target")
    proof = _mapping(proof_value, "legacy_identity_proof")
    _exact_fields(proof, frozenset({"atom_id", "commit", "path", "digest"}), "legacy_identity_proof")
    if (not isinstance(proof["commit"], str) or not re.fullmatch(r"[0-9a-f]{40}", proof["commit"])
            or not isinstance(proof["digest"], str) or not re.fullmatch(r"[0-9a-f]{64}", proof["digest"])
            or proof["path"] != descriptor["path"] or proof["atom_id"] != descriptor["atom_id"]):
        raise LifecycleError("legacy-proof-invalid", "historical proof must bind the exact target identity, path and bytes")
    try:
        path = safe_path(root, descriptor["path"], must_exist=True)
        raw = path.read_bytes()
        frontmatter, content = split_frontmatter(raw.decode("utf-8"))
        old_id = str(proof["atom_id"])
        declared_id = frontmatter_scalar(frontmatter, "atom_id")
        try:
            atom_from_path(root, path)
        except AtomToolError as error:
            missing_header = error.code == "atom-frontmatter-id-required" and declared_id is None
            explicit_legacy_header = (
                mapped_identity is not None
                and error.code == "atom-frontmatter-invalid"
                and declared_id == old_id
            )
            if not (missing_header or explicit_legacy_header):
                raise
        else:
            raise LifecycleError("legacy-proof-inapplicable", "target already carries an explicit identity")
        relative = path.relative_to(control_root(root))
        if any(part.casefold() in INACTIVE_LIFECYCLE_SEGMENTS | {"archived", "resolved"} for part in relative.parts):
            raise LifecycleError("legacy-proof-inapplicable", "migration requires a current carrier, not a draft or history")
        matches = re.findall(r"(?:^|-)(CA-[CAPRMEDO]-[0-9]+)(?=-|$)", path.stem)
        if mapped_identity is None:
            identity_matches = matches == [old_id]
        else:
            identity_matches = (not matches and not ATOM_ID.fullmatch(old_id)
                                and re.fullmatch(r"[A-Z][A-Z0-9]*(?:-[A-Z0-9]+)+-[0-9]+", old_id) is not None
                                and path.stem.partition("--")[0].startswith(old_id + "-"))
        if not identity_matches or hashlib.sha256(raw).hexdigest() != proof["digest"]:
            raise LifecycleError("legacy-proof-invalid", "historical assigned identity or present bytes differ")
        committed = subprocess.run(
            ["git", "-c", f"safe.directory={root}", "-C", str(root), "show", f"{proof['commit']}:{proof['path']}"],
            capture_output=True, check=False,
        )
        ancestor = subprocess.run(
            ["git", "-c", f"safe.directory={root}", "-C", str(root), "merge-base", "--is-ancestor", proof["commit"], "HEAD"],
            capture_output=True, check=False,
        )
        if committed.returncode != 0 or ancestor.returncode not in {0, 1}:
            raise LifecycleError("legacy-history-unavailable", "cannot read the explicitly scoped repository history")
        if ancestor.returncode != 0 or committed.stdout != raw:
            raise LifecycleError("legacy-proof-invalid", "exact assigned carrier is not backed by the current Git history")
        if explicit_legacy_header:
            from current_atom_locator import CurrentAtomLocator

            CurrentAtomLocator(root).assert_unique_current_claim(old_id, path)
        role = next(part for part in reversed(relative.parts[:-1]) if re.fullmatch(r"0[1-9]_[a-z0-9_]+", part))
        roles = {"C": "01_concern", "A": "02_analysis", "P": "03_plan", "R": "04_requirement",
                 "M": "05_method", "E": "06_evaluation", "D": "07_delivery", "O": "09_operations"}
        identity_letter = (mapped_identity or old_id).split("-")[1]
        if role != roles.get(identity_letter):
            raise LifecycleError("legacy-proof-invalid", "assigned identity differs from the carrier Content Role")
        old_status = frontmatter_scalar(frontmatter, "status")
        if old_status is not None and old_status.casefold() != "active":
            raise LifecycleError("legacy-proof-inapplicable", "migration cannot activate a draft or inactive Atom")
        role_values = {"C": "Concern", "A": "Analysis", "P": "Plan", "R": "Requirement", "M": "Method",
                       "E": "Evaluation", "D": "Delivery", "O": "Operations"}
        old_role = frontmatter_scalar(frontmatter, "content_role")
        if old_role is not None and old_role != role_values[identity_letter]:
            raise LifecycleError("legacy-proof-invalid", "migration cannot replace an explicitly different Content Role")
        atom = Atom(path, path.relative_to(root).as_posix(), path.name, str(proof["atom_id"]),
                    "active", role, frontmatter, content)
        observed = carrier_descriptor(root, atom)
        if any(descriptor[field] != observed[field] for field in _DESCRIPTOR_FIELDS):
            raise LifecycleError("stale-carrier", "legacy target no longer matches its complete sealed descriptor")
        for candidate in (() if explicit_legacy_header else control_root(root).rglob(f"*{atom.atom_id}*.md")):
            if candidate == path or any(part.casefold() in INACTIVE_LIFECYCLE_SEGMENTS | {"archived", "resolved"}
                                        for part in candidate.relative_to(control_root(root)).parts):
                continue
            try:
                other = atom_from_path(root, candidate)
            except AtomToolError as error:
                same_legacy_identity = (candidate.stem.partition("--")[0].startswith(old_id + "-")
                                        if mapped_identity is not None else
                                        re.findall(r"(?:^|-)(CA-[CAPRMEDO]-[0-9]+)(?=-|$)", candidate.stem) == [atom.atom_id])
                if error.code == "atom-frontmatter-id-required" and same_legacy_identity:
                    raise LifecycleError("active-atom-id-ambiguous", "legacy identity has another unnormalized owner") from error
            else:
                if other.atom_id == atom.atom_id:
                    raise LifecycleError("active-atom-id-ambiguous", "legacy identity already has another current owner")
        return atom
    except AtomToolError as error:
        raise _translate(error) from error


def _legacy_summary(content: str) -> str:
    headings = re.findall(r"(?m)^# (.+?)\s*$", content)
    if len(headings) != 1:
        raise LifecycleError("legacy-summary-ambiguous", "legacy migration requires one exact first-H1 Summary")
    if headings[0] == "Summary":
        return _summary(content)
    return headings[0]


def _summary(content: str) -> str:
    match = re.search(r"(?m)^# Summary\s*$\n(?P<tail>.*?)(?=^#|\Z)", content, re.DOTALL)
    if match is None:
        raise LifecycleError("summary-missing", "the complete carrier content must contain # Summary")
    for line in match.group("tail").splitlines():
        value = line.strip()
        if value:
            return value
    raise LifecycleError("summary-missing", "# Summary must carry a non-empty value")


def _goal_target(frontmatter: str) -> str | None:
    match = re.search(r'(?m)^  governs:\s*["\']?([A-Z][A-Z0-9_]*)/Goal["\']?\s*$', frontmatter)
    return match.group(1) if match else None


def _goal_filename_target(filename: str) -> str | None:
    matches = re.findall(r"(?:^|-)DEFINES_GOAL_FOR-([A-Z][A-Z0-9_]*)(?:--|$)", filename)
    return matches[0] if len(matches) == 1 else None


def _recovery_claim(content: str, *, legacy: bool) -> str | None:
    kind, claim = _claim_comparison_value(content)
    if kind == "claim-section":
        return claim.strip("\n") or None
    headings = re.findall(r"(?m)^# (.+?)\s*$", content)
    if legacy and len(headings) == 1 and not re.search(r"(?m)^## ", content):
        return re.sub(r"(?s)^# .+?\n", "", content).strip("\n") or None
    return None


def _recovery_metadata(root: Path, target: Atom, proposed: Mapping[str, str]) -> bool:
    try:
        before = yaml.safe_load(target.frontmatter) or {}
        after = yaml.safe_load(proposed["frontmatter"]) or {}
        rows = active_selection(root).structure["scope_units"]
        owners = {row["scope_unit_name"]: root / row["authority_path"] for row in rows}
        owner = max((name for name, path in owners.items() if target.path.is_relative_to(path)),
                    key=lambda name: len(owners[name].parts))
    except (AtomToolError, ProjectSelectionError, KeyError, TypeError, ValueError, yaml.YAMLError):
        return False
    if not isinstance(before, dict) or not isinstance(after, dict):
        return False
    canonical = {"atom_id", "content_role", "current_scope_unit", "claim_target_scope_unit", "local_tier",
                 "global_tier", "author", "status", "version", "updated_at", "subjects", "relations", "type"}
    retired = {"cce_version", "cce_form", "llm_session_ids"}
    if any((key not in retired and after.get(key) != value)
           or (key in retired and key in after and after[key] != value) for key, value in before.items()):
        return False
    if any(key not in before and key not in canonical for key in after):
        return False
    if before.get("status") is None and after.get("status") != "Active":
        return False
    if any(key not in before and after.get(key) not in ({}, []) for key in ("subjects", "relations")):
        return False
    target_scope = after.get("claim_target_scope_unit")
    return (isinstance(target_scope, str) and target_scope in owners
            and after.get("current_scope_unit") == owner)


def _legacy_recovery_body(proposed: Mapping[str, str], claim: str, target_scope: str) -> bool:
    expected = f"# Summary\n\n{_summary(proposed['content'])}\n\n## Scope\n\n{target_scope}.\n\n## Claim\n\n{claim}\n\n## Details\n"
    return proposed["content"].rstrip("\n") == expected.rstrip("\n")


def _goal_type_recovery(root: Path, target: Atom, proposed: Mapping[str, str], *, legacy: bool) -> bool:
    target_scope = frontmatter_scalar(proposed["frontmatter"], "claim_target_scope_unit")
    carried_scope = frontmatter_scalar(target.frontmatter, "claim_target_scope_unit")
    governed_scope = _goal_target(target.frontmatter)
    filename_scope = _goal_filename_target(target.filename)
    target_claim = _recovery_claim(target.content, legacy=legacy)
    proposed_claim = _recovery_claim(proposed["content"], legacy=False)
    return (frontmatter_scalar(target.frontmatter, "type") is None
            and frontmatter_scalar(proposed["frontmatter"], "type") == "Goal"
            and target.atom_id is not None and target.atom_id.startswith("CA-R-") and target.role_directory == "04_requirement"
            and frontmatter_scalar(proposed["frontmatter"], "content_role") == "Requirement"
            and target.lifecycle == "active" and frontmatter_scalar(target.frontmatter, "status") in {None, "Active"}
            and isinstance(target_scope, str)
            and filename_scope == target_scope
            and {value for value in (carried_scope, governed_scope) if value is not None} == {target_scope}
            and target_claim is not None and target_claim == proposed_claim and _recovery_metadata(root, target, proposed)
            and (target.content == proposed["content"] if not legacy else _legacy_recovery_body(proposed, target_claim, target_scope)))


def _require_recovery_carrier(root: Path, target: Atom, proposed: Mapping[str, str], *, required: bool) -> None:
    if not required:
        return
    try:
        prepare_create_atom_revision(root, target.relative, proposed["frontmatter"], proposed["content"], creating=False)
    except AtomToolError as error:
        raise _translate(error) from error


def _refresh_frontmatter(root: Path, frontmatter: str, *, version: int | None = None) -> str:
    result = frontmatter
    if version is not None:
        result = replace_frontmatter_scalar(result, "version", str(version))
    stamp = current_timestamp(root)
    return replace_frontmatter_scalar(result, "updated_at", f'"{stamp}"')


def _raw_carrier_body(raw: bytes) -> bytes:
    """Return the exact bytes after a Markdown carrier's closing YAML fence."""

    closing = re.search(br"\r?\n---\r?\n", raw[4:])
    if closing is None:
        raise LifecycleError("carrier-frontmatter-invalid", "Markdown carrier frontmatter is not closed")
    return raw[4 + closing.end():]


def _typed_relation_snapshot(frontmatter: str) -> str:
    try:
        metadata = yaml.safe_load(frontmatter) or {}
    except yaml.YAMLError as error:
        raise LifecycleError("carrier-frontmatter-invalid", "Atom frontmatter is not valid YAML") from error
    if not isinstance(metadata, dict):
        raise LifecycleError("carrier-frontmatter-invalid", "Atom frontmatter must be a mapping")
    return canonical_json(metadata.get("relations", {}))


def _move_link_evidence(outward: str) -> dict[str, Any]:
    return {"outward": {"before": outward, "after": outward, "changed": False},
            "inward": {"retargeted": False, "changed": False}}


def _effect(state: str, *, carrier: Mapping[str, Any], reason: str | None = None) -> dict[str, Any]:
    result: dict[str, Any] = {"carrier": dict(carrier), "state": state}
    if reason is not None:
        result["reason"] = reason
    return result


def _execute_allowed(*, execute: bool, authorized: bool) -> bool:
    if execute and not authorized:
        raise LifecycleError("authorization-required", "the caller has not admitted an authorized mutation")
    return execute


def _complete_carrier(value: object) -> dict[str, str]:
    carrier = _mapping(value, "carrier")
    _exact_fields(carrier, _CARRIER_FIELDS, "carrier")
    if any(not isinstance(carrier[field], str) for field in _CARRIER_FIELDS):
        raise LifecycleError("carrier-properties-invalid", "carrier path, frontmatter, and content must be strings")
    if not carrier["path"] or not carrier["frontmatter"]:
        raise LifecycleError("carrier-properties-invalid", "carrier path and frontmatter must be non-empty")
    return {field: carrier[field] for field in _CARRIER_FIELDS}


def _proposal(value: object) -> dict[str, str]:
    proposed = _mapping(value, "proposed")
    _exact_fields(proposed, frozenset({"frontmatter", "content"}), "proposed")
    if not all(isinstance(proposed[field], str) for field in ("frontmatter", "content")):
        raise LifecycleError("carrier-properties-invalid", "proposed frontmatter and content must be strings")
    return {"frontmatter": proposed["frontmatter"], "content": proposed["content"]}


def _is_lossless_carrier_normalization(target: Atom, proposed: Mapping[str, str]) -> bool:
    """Prove the only local carrier-only normalization safe without O067 evidence.

    A caller's class is not evidence that a changed Markdown body preserves the
    governed Claim or properties.  The Engine can independently establish one
    deliberately narrow case: surplus terminal line feeds.  They are outside
    the parsed frontmatter, Summary, Claim, and properties and have no rendered
    Markdown meaning.  Broader whitespace rewrites are intentionally excluded:
    for example, trailing spaces can be a Markdown hard line break.
    """

    return (
        proposed["frontmatter"] == target.frontmatter
        and proposed["content"].rstrip("\n") == target.content.rstrip("\n")
    )


def _is_lossless_identity_encoding(target: Atom, proposed: Mapping[str, str], mapping: Mapping[str, str]) -> bool:
    """Allow only the proven old-to-canonical identity field recoding."""

    atom_id_line = re.compile(r"(?m)^atom_id:\s*.*?(?:\n|$)")
    target_without_id, target_count = atom_id_line.subn("", target.frontmatter, count=1)
    proposed_without_id, proposed_count = atom_id_line.subn("", proposed["frontmatter"], count=1)
    return (
        target_count == proposed_count == 1
        and frontmatter_scalar(target.frontmatter, "atom_id") == mapping["legacy_atom_id"]
        and frontmatter_scalar(proposed["frontmatter"], "atom_id") == mapping["atom_id"]
        and target_without_id == proposed_without_id
        and proposed["content"] == target.content
    )


def _comparison_digest(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def _claim_comparison_value(content: str) -> tuple[str, str]:
    """Return the governed Claim, or the whole carrier when no Claim heading exists.

    A whole-carrier fingerprint remains a stronger equality proof for the
    mechanical-normalization path; it does not infer that a substantive
    unstructured body change is semantically safe.
    """

    match = re.search(r"(?ms)^## Claim\s*$\n(?P<claim>.*?)(?=^## |\Z)", content)
    if match is not None:
        return "claim-section", match.group("claim").rstrip("\n")
    return "whole-carrier", content.rstrip("\n")


def _mechanical_update_evidence(target: Atom, prior: Mapping[str, Any], proposed: Mapping[str, str], *,
                                admitted_change_class: str, exact_carrier: bool,
                                identity_mapping: Mapping[str, str] | None = None) -> dict[str, Any]:
    """Retain O067's actual target/proposal comparison for a proven safe class."""

    proposed_summary = _summary(proposed["content"])
    claim_kind, target_claim = _claim_comparison_value(target.content)
    proposed_claim_kind, proposed_claim = _claim_comparison_value(proposed["content"])
    result = {
        "admitted_change_class": admitted_change_class,
        "comparison": {
            "target": {"atom_id": target.atom_id, "path": target.relative, "digest": prior["digest"]},
            "proposal": {
                "frontmatter_digest": _comparison_digest(proposed["frontmatter"]),
                "content_digest": _comparison_digest(proposed["content"]),
            },
            "summary": {"target": _comparison_digest(_summary(target.content)),
                        "proposed": _comparison_digest(proposed_summary), "equal": True},
            "properties": {"target": _comparison_digest(target.frontmatter),
                           "proposed": _comparison_digest(proposed["frontmatter"]), "equal": True},
            "claim": {"target": _comparison_digest(target_claim), "proposed": _comparison_digest(proposed_claim),
                      "kind": claim_kind if claim_kind == proposed_claim_kind else "mismatch", "equal": True},
            "carrier_normalization": "exact-carrier" if exact_carrier else "terminal-newline-only",
        },
    }
    if identity_mapping is not None:
        result["comparison"]["properties"]["equal"] = False
        result["comparison"]["metadata_equal_except_identity"] = True
        result["comparison"]["carrier_normalization"] = "identity-encoding-only"
        result["comparison"]["identity_mapping"] = dict(identity_mapping)
    return result


def update_assessment_seal(parameters: Mapping[str, Any], evidence: Mapping[str, Any] | None = None) -> dict[str, Any]:
    """Bind O145's admitted class and actual comparison to one exact Update input."""

    request = _mapping(parameters, "parameters")
    required = ({"target", "subject_patches", "subject_intent_sha256"}
                if "subject_patches" in request else {"target", "proposed", "change_class"})
    if not required.issubset(request):
        raise LifecycleError("update-parameters-invalid", "assessment requires one complete Update request")
    seal: dict[str, Any] = {"request_digest": hashlib.sha256(canonical_json(request).encode("utf-8")).hexdigest()}
    if evidence is None:
        return seal
    comparison = _mapping(evidence, "assessment_evidence")
    _exact_fields(comparison, frozenset({"admitted_change_class", "comparison"}), "assessment_evidence")
    if comparison["admitted_change_class"] not in {*_UPDATE_CLASSES, "no-op"} or not isinstance(comparison["comparison"], Mapping):
        raise LifecycleError("assessment-invalid", "Update assessment does not contain one locally admitted class")
    seal.update(comparison)
    return seal


def _validate_update_assessment(parameters: Mapping[str, Any], assessment: Mapping[str, Any],
                                expected_evidence: Mapping[str, Any]) -> None:
    """Refuse an O145 result not sealed to this target, proposal, and class evidence."""

    if not isinstance(assessment.get("request_digest"), str):
        raise LifecycleError("assessment-invalid", "Update assessment seal is incomplete")
    expected = update_assessment_seal(parameters, expected_evidence)
    if dict(assessment) != expected:
        raise LifecycleError("reassessment-required", "Update target, proposal, class, or comparison evidence differs from completed O145 assessment")


def _pinned_project_file(root: Path, value: object, name: str, *, atom_id: str | None = None) -> tuple[Path, dict[str, str]]:
    """Read one exact project-relative evidence pin without following a caller path."""

    pin = _mapping(value, name)
    _exact_fields(pin, frozenset({"path", "digest"}), name)
    relative, digest = pin["path"], pin["digest"]
    if (not isinstance(relative, str) or not isinstance(digest, str)
            or re.fullmatch(r"[0-9a-f]{64}", digest) is None):
        raise LifecycleError("assessment-evidence-invalid", f"{name} must have canonical path and SHA-256 digest")
    candidate = Path(relative)
    if candidate.is_absolute() or not candidate.parts or ".." in candidate.parts or candidate.as_posix() != relative:
        raise LifecycleError("assessment-evidence-invalid", f"{name} path is unsafe")
    path = (root / candidate).resolve()
    try:
        path.relative_to(root)
        raw = path.read_bytes()
    except (OSError, ValueError) as error:
        raise LifecycleError("assessment-evidence-invalid", f"{name} is unavailable") from error
    if hashlib.sha256(raw).hexdigest() != digest:
        raise LifecycleError("assessment-evidence-invalid", f"{name} is stale")
    if atom_id is not None:
        try:
            frontmatter, _ = split_frontmatter(raw.decode("utf-8"))
        except (UnicodeDecodeError, AtomToolError) as error:
            raise LifecycleError("assessment-evidence-invalid", f"{name} is not an Atom carrier") from error
        if frontmatter_scalar(frontmatter, "atom_id") != atom_id:
            raise LifecycleError("assessment-evidence-invalid", f"{name} has wrong authority identity")
    return path, {"path": relative, "digest": digest}


def _assessment_object(raw: str) -> dict[str, Any]:
    """Reject ambiguous JSON in both individual reports and review packages."""
    def no_duplicates(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
        output: dict[str, Any] = {}
        for key, value in pairs:
            if key in output:
                raise LifecycleError("assessment-evidence-invalid", "Update assessment evidence has duplicate JSON keys")
            output[key] = value
        return output

    try:
        evidence = json.loads(raw, object_pairs_hook=no_duplicates)
    except (json.JSONDecodeError, LifecycleError) as error:
        if isinstance(error, LifecycleError):
            raise
        raise LifecycleError("assessment-evidence-invalid", "Update assessment evidence JSON is invalid") from error
    if not isinstance(evidence, dict):
        raise LifecycleError("assessment-evidence-invalid", "Update assessment evidence must be an object")
    return evidence


def _assessment_json(content: str) -> dict[str, Any]:
    """Read the one canonical external evidence block without interpreting prose."""

    results = re.search(r"(?ms)^## Results\s*$\n(?P<body>.*?)(?=^## |\Z)", content)
    if results is None:
        raise LifecycleError("assessment-evidence-invalid", "Analysis Report lacks Results")
    headings = list(re.finditer(r"(?m)^### Update assessment evidence\s*$", results.group("body")))
    if len(headings) != 1:
        raise LifecycleError("assessment-evidence-invalid", "Analysis Report must have one Update assessment evidence section")
    body = results.group("body")[headings[0].end():]
    body = re.split(r"(?m)^### |^## ", body, maxsplit=1)[0]
    fenced = re.fullmatch(r"\s*```json\n(?P<json>.*?)\n```\s*", body, re.DOTALL)
    if fenced is None:
        raise LifecycleError("assessment-evidence-invalid", "Update assessment evidence must be one JSON block")
    return _assessment_object(fenced.group("json"))


_ASSESSMENT_FIELDS = frozenset({
    "target", "proposal", "authorityPins", "admittedChangeClass", "primaryClaimIdentityPreserved",
    "declaredDelta", "lineageEvidencePins",
})


def _package_assessment(path: Path, atom_id: str) -> dict[str, Any]:
    try:
        package = _assessment_object(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError) as error:
        raise LifecycleError("assessment-evidence-invalid", "Review package is unreadable") from error
    _exact_fields(package, frozenset({"assessments"}), "Review package")
    records = package["assessments"]
    if not isinstance(records, list) or not records:
        raise LifecycleError("assessment-evidence-invalid", "Review package assessments must be a nonempty list")
    matches = []
    for record in records:
        record = _mapping(record, "Review package assessment")
        _exact_fields(record, _ASSESSMENT_FIELDS, "Review package assessment")
        target = _mapping(record["target"], "Review package target")
        _exact_fields(target, frozenset({"atom_id", "path", "digest"}), "Review package target")
        _exact_fields(_mapping(record["proposal"], "Review package proposal"),
                      frozenset({"frontmatter_digest", "content_digest"}), "Review package proposal")
        authority = _mapping(record["authorityPins"], "Review package authority pins")
        _exact_fields(authority, frozenset({"r1432", "r1464"}), "Review package authority pins")
        lineage = record["lineageEvidencePins"]
        if not isinstance(lineage, list) or not lineage:
            raise LifecycleError("assessment-evidence-invalid", "Review package lineage review is incomplete")
        for pin in [*authority.values(), *lineage]:
            _exact_fields(_mapping(pin, "Review package evidence pin"),
                          frozenset({"path", "digest"}), "Review package evidence pin")
        if target["atom_id"] == atom_id:
            matches.append(record)
    if len(matches) != 1:
        raise LifecycleError("assessment-evidence-invalid", "Review package must contain exactly one assessment for the target")
    return dict(matches[0])


def _recovery_authority_pins(root: Path, lineage: list[object]) -> dict[str, dict[str, str]]:
    required = {"CA-R-1766", "CA-D-531"}
    found: dict[str, dict[str, str]] = {}
    for index, item in enumerate(lineage):
        path, pin = _pinned_project_file(root, item, f"lineageEvidencePins[{index}]")
        try:
            atom = atom_from_path(root, path)
            require_current_atom(root, atom)
        except AtomToolError:
            continue
        relative = path.relative_to(control_root(root)).as_posix()
        source = ((atom.atom_id == "CA-R-1766" and "/METHODOLOGY_SOURCES/" in f"/{relative}"
                   and "/04_requirement/" in f"/{relative}")
                  or (atom.atom_id == "CA-D-531" and "/201_FEATURE_TOOLS/WORKFLOW_OPERATIONS/ATOM_LIFECYCLE/07_delivery/" in f"/{relative}"))
        if source and frontmatter_scalar(atom.frontmatter, "status") == "Active":
            found[atom.atom_id] = pin
    if set(found) != required:
        raise LifecycleError("assessment-evidence-invalid", "Goal Type recovery lacks current R1766 and D531 lineage")
    return found


def _admit_assessment_class(admitted: object, *, carrier_recovery: bool) -> None:
    allowed = {"equivalent_refinement", "semantic_revision", "replacement"}
    if carrier_recovery and admitted == "carrier_only":
        return
    if admitted not in allowed:
        raise LifecycleError("assessment-evidence-invalid", "assessment change class is not substantive")
    if carrier_recovery:
        raise LifecycleError("assessment-evidence-invalid", "Goal Type recovery must be carrier_only")


def _semantic_assessment_evidence(root: Path, target: Atom, prior: Mapping[str, Any],
                                  proposed: Mapping[str, str], reference: object, *,
                                  carrier_recovery: bool = False) -> dict[str, Any]:
    """Verify bound assessment evidence; a report/package never authorizes edits."""

    report_path, report_pin = _pinned_project_file(root, reference, "semantic_assessment_report")
    report_identity = dict(report_pin)
    if report_path.suffix == ".json":
        evidence = _package_assessment(report_path, target.atom_id)
    else:
        try:
            report = atom_from_path(root, report_path)
            if (frontmatter_scalar(report.frontmatter, "content_role") != "Analysis"
                    or frontmatter_scalar(report.frontmatter, "type") != "Analysis Report"
                    or frontmatter_scalar(report.frontmatter, "status") != "Done"):
                raise LifecycleError("assessment-evidence-invalid", "assessment report is not a Done Analysis Report")
            resolve_status_model(root, report, "Done")
        except (AtomToolError, StatusModelError) as error:
            raise LifecycleError("assessment-evidence-invalid", "assessment report lacks current Analysis authority") from error
        evidence = _assessment_json(report.content)
        report_identity["atom_id"] = report.atom_id
    _exact_fields(evidence, _ASSESSMENT_FIELDS, "Update assessment evidence")
    target_pin = _mapping(evidence["target"], "Update assessment target")
    _exact_fields(target_pin, frozenset({"atom_id", "path", "digest"}), "Update assessment target")
    if target_pin != {"atom_id": target.atom_id, "path": target.relative, "digest": prior["digest"]}:
        raise LifecycleError("assessment-evidence-invalid", "assessment target differs from current Update target")
    proposal_pin = _mapping(evidence["proposal"], "Update assessment proposal")
    _exact_fields(proposal_pin, frozenset({"frontmatter_digest", "content_digest"}), "Update assessment proposal")
    if proposal_pin != {"frontmatter_digest": _comparison_digest(proposed["frontmatter"]),
                        "content_digest": _comparison_digest(proposed["content"])}:
        raise LifecycleError("assessment-evidence-invalid", "assessment proposal differs from current Update proposal")
    authority = _mapping(evidence["authorityPins"], "Update assessment authorityPins")
    _exact_fields(authority, frozenset({"r1432", "r1464"}), "Update assessment authorityPins")
    _, r1432 = _pinned_project_file(root, authority["r1432"], "CA-R-1432 authority", atom_id="CA-R-1432")
    _, r1464 = _pinned_project_file(root, authority["r1464"], "CA-R-1464 authority", atom_id="CA-R-1464")
    admitted = evidence["admittedChangeClass"]
    _admit_assessment_class(admitted, carrier_recovery=carrier_recovery)
    if evidence["primaryClaimIdentityPreserved"] is not True:
        raise LifecycleError("assessment-evidence-invalid", "assessment does not establish primary Claim identity")
    if not isinstance(evidence["declaredDelta"], str) or not evidence["declaredDelta"].strip():
        raise LifecycleError("assessment-evidence-invalid", "assessment declared delta is absent")
    if not isinstance(evidence["lineageEvidencePins"], list) or not evidence["lineageEvidencePins"]:
        raise LifecycleError("assessment-evidence-invalid", "assessment lineage review is incomplete")
    lineage = [_pinned_project_file(root, item, f"lineageEvidencePins[{index}]")[1]
               for index, item in enumerate(evidence["lineageEvidencePins"])]
    result = {
        "admitted_change_class": admitted,
        "comparison": {
            "target": target_pin,
            "proposal": proposal_pin,
            "report": report_identity,
            "authority_pins": {"r1432": r1432, "r1464": r1464},
            "primary_claim_identity_preserved": True,
            "declared_delta": evidence["declaredDelta"],
            "lineage_evidence_pins": lineage,
        },
    }
    if carrier_recovery:
        result["comparison"]["type_recovery"] = _recovery_authority_pins(root, evidence["lineageEvidencePins"])
    return result


def _proposed_successors(root: Path, value: object, predecessor: Atom) -> list[dict[str, str]]:
    """Validate future successor carriers without requiring present carriers."""

    if not isinstance(value, list) or not value:
        raise LifecycleError("successor-set-required", "Replace requires one or more complete successor carrier sets")
    successors: list[dict[str, str]] = []
    atom_ids: list[str | None] = []
    paths: list[str] = []
    for index, item in enumerate(value):
        successor = _complete_carrier(item)
        try:
            destination, _, atom_id = prepare_create_atom_revision(
                root, successor["path"], successor["frontmatter"], successor["content"]
            )
        except AtomToolError as error:
            raise _translate(error) from error
        if atom_id == predecessor.atom_id:
            raise LifecycleError("replacement-self-reference", "predecessor cannot be one of its successors")
        successors.append(successor)
        atom_ids.append(atom_id)
        paths.append(destination.relative_to(root).as_posix())
    if len(atom_ids) != len(set(atom_ids)) or len(paths) != len(set(paths)):
        raise LifecycleError("successor-set-duplicate", "complete successor set must not repeat an Atom or destination")
    return successors


def _status_destination(root: Path, atom: Atom, status: str, *, filename: str | None = None,
                         version: int | None = None) -> str:
    """Resolve the current role-local status carrier location without inference."""

    control = control_root(root)
    try:
        relative = atom.path.relative_to(control)
        index = next(index for index, part in enumerate(relative.parts[:-1]) if re.fullmatch(r"0[1-9]_[a-z0-9_]+", part))
    except (ValueError, StopIteration) as error:
        raise LifecycleError("status-location-missing", "target has no content-role status location") from error
    role = control.joinpath(*relative.parts[:index + 1])
    stem = re.sub(r"@[0-9]+$", "", Path(filename or atom.filename).stem)
    next_version = atom_version(atom) + 1 if version is None else version
    name = f"{stem}@{next_version}.md" if status == "Archived" else f"{stem}.md"
    if frontmatter_scalar(atom.frontmatter, "content_role") in {"Plan", "Operations"}:
        local = atom.path.parent
        if local.name in {"001_backlog", "done", "canceled", "archived", "draft"}:
            local = local.parent
        folders = {"Active": None, "Backlog": "001_backlog", "Done": "done", "Canceled": "canceled", "Archived": "archived"}
        if status in folders:
            target = local / folders[status] / name if folders[status] else local / name
            return target.relative_to(root).as_posix()
    if status.casefold() == "active":
        target = role / name
    else:
        folder = status.casefold()
        if re.fullmatch(r"[a-z0-9][a-z0-9_-]*", folder) is None:
            raise LifecycleError("status-location-invalid", "admitted status cannot name a safe carrier subfolder")
        target = role / folder / name
    return target.relative_to(root).as_posix()


def _status_model(value: object, atom: Atom, requested_status: str) -> dict[str, Any]:
    model = _mapping(value, "status_model")
    required = frozenset({"model_ref", "model_revision", "content_role", "statuses"})
    missing = sorted(required - model.keys())
    if missing:
        raise LifecycleError("status-model-incomplete", f"status_model is missing {', '.join(missing)}")
    if not isinstance(model["model_ref"], str) or not model["model_ref"]:
        raise LifecycleError("status-model-invalid", "status_model.model_ref must be non-empty")
    if not isinstance(model["model_revision"], (str, int)):
        raise LifecycleError("status-model-invalid", "status_model.model_revision must be a scalar")
    if not isinstance(model["content_role"], str) or not model["content_role"]:
        raise LifecycleError("status-model-invalid", "status_model.content_role must be non-empty")
    model_type = model.get("type")
    if model_type is not None and (not isinstance(model_type, str) or not model_type):
        raise LifecycleError("status-model-invalid", "status_model.type must be an optional non-empty string")
    if frontmatter_scalar(atom.frontmatter, "content_role") != model["content_role"]:
        raise LifecycleError("status-model-unqualified", "status_model does not qualify the target Content Role")
    if model_type is not None and frontmatter_scalar(atom.frontmatter, "type") != model_type:
        raise LifecycleError("status-model-unqualified", "status_model type does not qualify the target")
    statuses = model["statuses"]
    if not isinstance(statuses, list) or not statuses or any(not isinstance(item, str) or not item for item in statuses):
        raise LifecycleError("status-model-invalid", "status_model.statuses must be a non-empty string list")
    if len(statuses) != len(set(statuses)) or requested_status not in statuses:
        raise LifecycleError("status-unadmitted", "requested status is not admitted by the qualified status model")
    current = frontmatter_scalar(atom.frontmatter, "status")
    if current is None or current not in statuses:
        raise LifecycleError("status-current-unadmitted", "target current status is not admitted by the qualified status model")
    archive_status = model.get("archive_status")
    if archive_status is not None and (not isinstance(archive_status, str) or archive_status not in statuses):
        raise LifecycleError("status-model-invalid", "status_model.archive_status must be one admitted status")
    return {
        "model_ref": model["model_ref"],
        "model_revision": str(model["model_revision"]),
        "content_role": model["content_role"],
        "type": model_type,
        "statuses": list(statuses),
        "archive_status": archive_status,
    }


def preflight_atom_lifecycle(root: Path, operation: str, parameters: Mapping[str, Any]) -> dict[str, Any]:
    """Purely observe one model-governed status operation before any effect."""
    root = root.resolve()
    request = _mapping(parameters, "parameters")
    if operation != "change_status":
        raise LifecycleError("operation-unadmitted", "preflight supports change_status only")
    allowed = frozenset({"target", "status"})
    if set(request) - allowed or not {"target", "status"}.issubset(request):
        raise LifecycleError("carrier-fields-invalid", "parameters must carry target and status only")
    requested = request["status"]
    if not isinstance(requested, str) or not requested:
        raise LifecycleError("status-invalid", "status must be a non-empty source-admitted value")
    target = _resolve_descriptor(root, request["target"], name="target", active=False)
    prior = carrier_descriptor(root, target)
    role = frontmatter_scalar(target.frontmatter, "content_role")
    atom_type = frontmatter_scalar(target.frontmatter, "type")
    if role is None:
        raise LifecycleError("status-model-unqualified", "target lacks a carried Content Role")
    try:
        model = resolve_status_model(root, {"content_role": role, "type": atom_type}, requested)
    except StatusModelError as error:
        raise LifecycleError(error.code, str(error)) from error
    current = frontmatter_scalar(target.frontmatter, "status")
    if current is None or current not in model["statuses"]:
        raise LifecycleError("status-current-unadmitted", "target current status is not admitted by the current source model")
    archive = requested == "Archived"
    return {"operation": operation, "target": target, "prior": prior, "requested_status": requested,
            "current_status": current, "status_model": model, "archive": archive}


def _draft_promotion_identity(root: Path, target: Atom) -> str:
    """Allocate a fresh unused identity for every ID-free Draft."""
    role = frontmatter_scalar(target.frontmatter, "content_role")
    if not role:
        raise LifecycleError("status-model-unqualified", "Draft lacks Content Role")
    prefix, letter = project_identity_prefix(root), role[0].upper()
    used = []
    for path in control_root(root).rglob("*.md"):
        if path.is_symlink():
            continue
        match = re.search(rf"(?:^|-){prefix}-{letter}-(\d+)(?=-|@|\.)", path.name)
        if match:
            used.append(int(match.group(1)))
        try:
            frontmatter, _content = split_frontmatter(path.read_text(encoding="utf-8"))
            match = re.fullmatch(rf"{prefix}-{letter}-(\d+)", frontmatter_scalar(frontmatter, "atom_id") or "")
            if match:
                used.append(int(match.group(1)))
        except (AtomToolError, UnicodeError, OSError):
            # A historical filename still reserves its number when its carrier
            # cannot establish any other Atom property.
            continue
    number = max(used, default=0) + 1
    while atom_id_has_preserved_history_evidence(root, f"{prefix}-{letter}-{number:03d}"):
        number += 1
    return f"{prefix}-{letter}-{number:03d}"


def _broken_references(root: Path, atom: Atom) -> list[dict[str, Any]]:
    """Report active relation endpoints; never change or retarget them."""

    assert atom.atom_id is not None
    result: list[dict[str, Any]] = []
    for reference in sorted(set(_ATOM_REFERENCE.findall(atom.frontmatter)) - {atom.atom_id}):
        result.append({
            "direction": "outgoing",
            "relation_owner": atom.atom_id,
            "referenced_atom_id": reference,
            "reason": "target-status-becomes-inactive",
            "active_referrer": True,
        })
    try:
        atoms = scan_atoms(root, lifecycle="active")
    except AtomToolError as error:
        raise _translate(error) from error
    for candidate in atoms:
        if candidate.atom_id is None or candidate.atom_id == atom.atom_id:
            continue
        if atom.atom_id in _ATOM_REFERENCE.findall(candidate.frontmatter):
            result.append({
                "direction": "inbound",
                "relation_owner": candidate.atom_id,
                "referenced_atom_id": atom.atom_id,
                "reason": "target-status-becomes-inactive",
                "active_referrer": True,
            })
    return result


def create_atom_action(root: Path, parameters: Mapping[str, Any], *, execute: bool = False, authorized: bool = False) -> dict[str, Any]:
    """Apply or preview one complete Create carrier, without any outer Run policy."""

    root = root.resolve()
    request = _mapping(parameters, "parameters")
    _exact_fields(request, frozenset({"carrier"}), "parameters")
    carrier = _complete_carrier(request["carrier"])
    try:
        destination, _, _ = prepare_create_atom_revision(
            root, carrier["path"], carrier["frontmatter"], carrier["content"]
        )
        if destination.exists():
            # A pathname alone does not prove that this is a replay of the
            # sealed Create request.  The route does not carry authenticated
            # prior-success evidence, so an occupied destination must remain a
            # conflict rather than being terminalized as a harmless no-op.
            raise LifecycleError(
                "destination-collision",
                "Create destination is already occupied; no authenticated replay proof is available",
            )
    except AtomToolError as error:
        raise _translate(error) from error
    if not _execute_allowed(execute=execute, authorized=authorized):
        return {"operation": "create", "outcome": "preview", "requested": carrier,
                "effects": [_effect("unchanged", carrier=carrier, reason="preview")]}
    try:
        created = create_atom_revision(root, carrier["path"], carrier["frontmatter"], carrier["content"])
    except AtomToolError as error:
        raise _translate(error) from error
    observed = carrier_descriptor(root, created)
    return {"operation": "create", "outcome": "applied", "requested": carrier, "observed": observed,
            "effects": [_effect("changed", carrier=observed)], "history": {"prior": None}}


def update_atom_action(root: Path, parameters: Mapping[str, Any], *, execute: bool = False, authorized: bool = False,
                       assessment: Mapping[str, Any] | None = None, session: object | None = None,
                       action_run_id: str | None = None, prior: Mapping[str, Any] | None = None) -> dict[str, Any]:
    """Apply one assessed identity-preserving Update or return a terminal handoff."""

    root = root.resolve()
    request = _mapping(parameters, "parameters")
    if "subject_patches" in request:
        from atom_subject_apply import subject_update_action
        return subject_update_action(
            root, request, execute=execute, authorized=authorized, assessment=assessment,
            session=session, action_run_id=action_run_id, prior=prior,
        )
    allowed = frozenset({"target", "proposed", "change_class", "successors", "legacy_identity_proof", "legacy_identity_mapping",
                         "semantic_assessment_report"})
    unknown = sorted(request.keys() - allowed)
    if unknown or not {"target", "proposed", "change_class"}.issubset(request):
        raise LifecycleError("update-parameters-invalid", "update requires target, complete proposed carrier, and change_class only")
    legacy = "legacy_identity_proof" in request
    mapping = None
    if "legacy_identity_mapping" in request:
        if not legacy:
            raise LifecycleError("identity-mapping-invalid", "explicit legacy mapping requires an exact historical proof")
        mapping = _mapping(request["legacy_identity_mapping"], "legacy_identity_mapping")
        _exact_fields(mapping, frozenset({"legacy_atom_id", "atom_id", "destination"}), "legacy_identity_mapping")
        if (not isinstance(mapping["atom_id"], str) or re.fullmatch(r"CA-[CAPRMEDO]-[0-9]{3,}", mapping["atom_id"]) is None
                or mapping["legacy_atom_id"] != _mapping(request["target"], "target").get("atom_id")
                or not isinstance(mapping["destination"], str)):
            raise LifecycleError("identity-mapping-invalid", "mapping must bind one exact legacy identity to a canonical identity and destination")
    target = (_resolve_legacy_descriptor(root, request["target"], request["legacy_identity_proof"],
                                        mapped_identity=mapping["atom_id"] if mapping else None)
              if legacy else _resolve_descriptor(root, request["target"], name="target", active=False))
    prior = carrier_descriptor(root, target)
    proposed = _proposal(request["proposed"])
    change_class = request["change_class"]
    if change_class not in _UPDATE_CLASSES:
        raise LifecycleError("change-class-unadmitted", "update change_class is not identity-preserving")
    expected_identity = mapping["atom_id"] if mapping else target.atom_id
    proposed_identity = frontmatter_scalar(proposed["frontmatter"], "atom_id")
    requested_draft = (frontmatter_scalar(proposed["frontmatter"], "status") or "").casefold() == "draft"
    if proposed_identity != expected_identity and not (
            not legacy and requested_draft and target.atom_id is not None and proposed_identity is None):
        raise LifecycleError("atom-identity-changed", "same-identity update must retain the current atom_id")
    if legacy:
        expected_role = {"C": "Concern", "A": "Analysis", "P": "Plan", "R": "Requirement", "M": "Method",
                         "E": "Evaluation", "D": "Delivery", "O": "Operations"}[expected_identity.split("-")[1]]
        if frontmatter_scalar(proposed["frontmatter"], "content_role") != expected_role:
            raise LifecycleError("atom-identity-changed", "legacy migration must retain the assigned Content Role")
    type_recovery = _goal_type_recovery(root, target, proposed, legacy=legacy)
    if frontmatter_scalar(proposed["frontmatter"], "type") != frontmatter_scalar(target.frontmatter, "type") and not type_recovery:
        raise LifecycleError("atom-type-changed", "same-identity Update must retain the current Type")
    _require_recovery_carrier(root, target, proposed, required=type_recovery)
    old_status = frontmatter_scalar(target.frontmatter, "status")
    new_status = frontmatter_scalar(proposed["frontmatter"], "status")
    status_change = new_status != old_status and not (legacy and old_status is None and new_status == "Active")
    status_preflight = None
    if status_change:
        status_preflight = preflight_atom_lifecycle(root, "change_status", {"target": prior, "status": new_status})
    if not legacy and frontmatter_scalar(proposed["frontmatter"], "content_role") != frontmatter_scalar(target.frontmatter, "content_role"):
        raise LifecycleError("atom-role-changed", "same-identity Update must retain the current Content Role")
    prior_summary = _legacy_summary(target.content) if legacy else _summary(target.content)
    if _summary(proposed["content"]) != prior_summary:
        if mapping:
            raise LifecycleError("legacy-summary-changed", "identity encoding migration must preserve the exact Summary")
        proposed_successors = _proposed_successors(root, request.get("successors"), target)
        return {
            "operation": "update",
            "outcome": "replace_handoff",
            "predecessor": prior,
            "replace_handoff": {"predecessor": prior, "successors": proposed_successors},
            "effects": [_effect("unchanged", carrier=prior, reason="summary-change-requires-separate-replace")],
            "history": {"prior": prior, "preserved": True},
        }
    if mapping:
        try:
            destination, _, destination_id = prepare_create_atom_revision(root, mapping["destination"], proposed["frontmatter"])
        except AtomToolError as error:
            raise _translate(error) from error
        if destination.parent != target.path.parent or destination_id != expected_identity:
            raise LifecycleError("identity-mapping-invalid", "canonical destination must preserve the source scope and Content Role")
        if destination.exists():
            raise LifecycleError("destination-collision", "canonical destination already exists")
        if any(atom.atom_id == expected_identity for atom in scan_atoms(root)):
            raise LifecycleError("atom-id-collision", "canonical identity was already used")
        for candidate in control_root(root).rglob("*.md"):
            if re.search(rf"(?:^|-){re.escape(expected_identity)}(?=-|@|\.)", candidate.name):
                raise LifecycleError("atom-id-collision", "canonical identity was already used by a historical or unnormalized carrier")
    if proposed["frontmatter"] == target.frontmatter and proposed["content"] == target.content and not mapping:
        admitted_evidence = _mechanical_update_evidence(
            target, prior, proposed, admitted_change_class="no-op", exact_carrier=True,
        )
        if assessment is not None:
            _validate_update_assessment(request, assessment, admitted_evidence)
        assessment_evidence = {"assessment": dict(assessment)} if assessment is not None else {}
        return {"operation": "update", "outcome": "no-op", "observed": prior,
                "assessment_evidence": admitted_evidence,
                "effects": [_effect("unchanged", carrier=prior, reason="equivalent-carrier")], "history": {"prior": prior, "preserved": True},
                **assessment_evidence}
    comparison_proposal = proposed
    comparison_target = target
    if status_change:
        comparison_proposal = {**proposed, "frontmatter": replace_frontmatter_scalar(proposed["frontmatter"], "status", old_status)}
        if requested_draft and proposed_identity is None and target.atom_id is not None:
            comparison_target = replace(target, frontmatter=remove_frontmatter_scalar(target.frontmatter, "atom_id"))
    mapped_encoding = (bool(mapping) and change_class == "carrier_only"
                       and _is_lossless_identity_encoding(target, proposed, mapping))
    mechanical = ((not legacy and change_class == "carrier_only"
                   and _is_lossless_carrier_normalization(comparison_target, comparison_proposal))
                  or mapped_encoding)
    admitted_evidence: dict[str, Any] | None = None
    if mechanical:
        admitted_evidence = _mechanical_update_evidence(
            target, prior, proposed, admitted_change_class="carrier_only", exact_carrier=False,
            identity_mapping=mapping if mapped_encoding else None,
        )
    elif not legacy or "semantic_assessment_report" in request or type_recovery:
        report = request.get("semantic_assessment_report")
        try:
            admitted_evidence = _semantic_assessment_evidence(
                root, target, prior, proposed, report, carrier_recovery=type_recovery,
            )
        except LifecycleError as error:
            assessment_evidence = {"assessment": dict(assessment)} if assessment is not None else {}
            return {
                "operation": "update", "outcome": "unresolved", "observed": prior,
                "classification": {
                    "requested": change_class, "reason": "semantic-assessment-unverified",
                    "required": "current bound assessment evidence with declared delta and completed lineage-impact review",
                    "diagnostic": error.code,
                },
                "effects": [_effect("unchanged", carrier=prior, reason="semantic-assessment-unverified")],
                "history": {"prior": prior, "preserved": True}, **assessment_evidence,
            }
        admitted = admitted_evidence["admitted_change_class"]
        if admitted == "replacement":
            proposed_successors = _proposed_successors(root, request.get("successors"), target)
            return {
                "operation": "update", "outcome": "replace_handoff", "predecessor": prior,
                "replace_handoff": {"predecessor": prior, "successors": proposed_successors},
                "effects": [_effect("unchanged", carrier=prior, reason="assessment-requires-replace")],
                "history": {"prior": prior, "preserved": True}, "assessment_evidence": admitted_evidence,
            }
        if admitted != change_class:
            return {
                "operation": "update", "outcome": "unresolved", "observed": prior,
                "classification": {"requested": change_class, "admitted": admitted,
                                   "reason": "semantic-assessment-class-mismatch"},
                "effects": [_effect("unchanged", carrier=prior, reason="semantic-assessment-class-mismatch")],
                "history": {"prior": prior, "preserved": True},
            }
    if assessment is not None:
        if admitted_evidence is None:
            raise LifecycleError("assessment-invalid", "legacy Update cannot consume a current O145 mechanical assessment")
        _validate_update_assessment(request, assessment, admitted_evidence)
    assessment_evidence = {"assessment": dict(assessment)} if assessment is not None else {}
    if not _execute_allowed(execute=execute, authorized=authorized):
        return {"operation": "update", "outcome": "preview", "observed": prior,
                "assessment_evidence": admitted_evidence,
                "effects": [_effect("unchanged", carrier=prior, reason="preview")], "history": {"prior": prior},
                **assessment_evidence}
    if status_preflight is not None or target.lifecycle == "archived":
        if status_preflight is None:
            status_preflight = preflight_atom_lifecycle(root, "change_status", {"target": prior, "status": new_status})
        refreshed = preflight_atom_lifecycle(root, "change_status", {"target": prior, "status": new_status})
        if refreshed["status_model"] != status_preflight["status_model"]:
            raise LifecycleError("status-model-stale", "authoritative status-model source changed after assessment")
        frontmatter = _refresh_frontmatter(root, proposed["frontmatter"], version=atom_version(target) + 1)
        observed_atom, predecessor = _publish_status_change(root, target, new_status, frontmatter, proposed["content"])
        observed = carrier_descriptor(root, observed_atom)
        history = {"prior": prior, "revision_class": change_class}
        if predecessor is not None:
            history["prior_revision"] = carrier_descriptor(root, predecessor)
        return {"operation": "update", "outcome": "applied", "observed": observed,
                "effects": [_effect("changed", carrier=observed)], "history": history,
                "status_model": status_preflight["status_model"], **assessment_evidence}
    identified_current = (not mapping and target.atom_id is not None
                          and target.lifecycle != "draft")
    next_version = atom_version(target) + 1
    prior_revision: Atom | None = None
    prior_revision_owner: tuple[int, int] | None = None
    prior_revision_carrier: dict[str, Any] | None = None
    before_bytes = target.path.read_bytes() if not mapping else None
    before_mode = target.path.stat().st_mode & 0o777 if not mapping else None
    if before_bytes is not None and hashlib.sha256(before_bytes).hexdigest() != prior["digest"]:
        raise LifecycleError("carrier-stale", "same-ID Update current bytes changed before publication")
    try:
        frontmatter = _refresh_frontmatter(root, proposed["frontmatter"], version=next_version)
        if target.atom_id is not None and (identified_current or change_class == "semantic_revision" or legacy):
            prior_revision = preserve_atom_revision(
                root, target, allow_nonactive=identified_current, allow_legacy_identity=bool(mapping)
            )
            if not mapping:
                owned = prior_revision.path.lstat()
                prior_revision_owner = (owned.st_dev, owned.st_ino)
        if mapping:
            observed_atom = migrate_atom_identity_revision(root, target, mapping["destination"], frontmatter, proposed["content"])
        else:
            write_atom_revision(target, frontmatter, proposed["content"])
            observed_atom = atom_from_path(root, target.path)
            observed = carrier_descriptor(root, observed_atom)
            if prior_revision is not None:
                prior_revision_carrier = carrier_descriptor(root, prior_revision)
    except BaseException as error:
        if not mapping:
            # History remains recoverable until the exact same-ID before-state
            # has been restored and independently reread. Never reconstruct
            # the old carrier from parsed fields: retain its original bytes.
            recovery_phase = "restore-current"
            try:
                assert before_bytes is not None and before_mode is not None
                if target.path.is_symlink():
                    raise OSError("current carrier became a symlink")
                try:
                    restore_current = not target.path.is_file() or target.path.read_bytes() != before_bytes
                except OSError:
                    restore_current = True
                if restore_current:
                    _atomic_write(target.path, before_bytes)
                if target.path.stat().st_mode & 0o777 != before_mode:
                    target.path.chmod(before_mode)
                if target.path.read_bytes() != before_bytes or target.path.stat().st_mode & 0o777 != before_mode:
                    raise OSError("current before-state could not be verified")
                if prior_revision is not None:
                    recovery_phase = "verify-history-ownership"
                    owned = prior_revision.path.lstat()
                    if (prior_revision.path.is_symlink() or not prior_revision.path.is_file()
                            or (owned.st_dev, owned.st_ino) != prior_revision_owner
                            or prior_revision.path.read_bytes() != before_bytes):
                        raise OSError("new prior-revision carrier ownership could not be verified")
                    recovery_phase = "remove-new-history"
                    prior_revision.path.unlink()
            except BaseException as recovery_error:
                # A raised error loses recovery refs at the selected adapter's
                # generic catch boundary. Retain the exact private native
                # failure packet instead, without inventing a current seal.
                current_ref = {"path": target.relative, "verification": "unknown"}
                retained_history: dict[str, Any] | None = None
                effects = [_effect("unknown", carrier=current_ref, reason="update-rollback-uncertain")]
                history = {"prior": prior}
                if prior_revision is not None:
                    creation_known = prior_revision_owner is not None
                    retained_history = {
                        "path": prior_revision.relative,
                        "expected_before_digest": prior["digest"],
                        "creation": "attempt-created" if creation_known else "unverified",
                        "ownership_verification": ("verified" if recovery_phase == "remove-new-history"
                                                   else "unverified" if recovery_phase == "verify-history-ownership"
                                                   else "not-rechecked"),
                    }
                    history["prior_revision"] = retained_history
                    known_effect = creation_known and recovery_phase != "verify-history-ownership"
                    effects.append(_effect("changed" if known_effect else "unknown", carrier=retained_history,
                                           reason="retained-new-prior-revision" if known_effect
                                           else "retained-prior-ownership-unverified"))
                failure = {
                    "code": "update-rollback-uncertain",
                    "original": {"type": type(error).__name__, "code": getattr(error, "code", None)},
                    "recovery": {"type": type(recovery_error).__name__, "code": getattr(recovery_error, "code", None),
                                 "phase": recovery_phase},
                }
                return {"operation": "update", "outcome": "partial", "failure": failure,
                        "effects": effects, "history": history,
                        "recovery": {"before": prior, "current": current_ref, "prior_revision": retained_history,
                                     "automatic_retry": False},
                        "unknown_remainder": [{"phase": recovery_phase, "code": "update-rollback-uncertain",
                                               "current_ref": target.relative,
                                               "history_ref": prior_revision.relative if prior_revision is not None else None}]}
        elif prior_revision is not None:
            prior_revision.path.unlink(missing_ok=True)
        if isinstance(error, AtomToolError):
            raise _translate(error) from error
        raise
    if mapping:
        observed = carrier_descriptor(root, observed_atom)
        if prior_revision is not None:
            prior_revision_carrier = carrier_descriptor(root, prior_revision)
    history: dict[str, Any] = {"prior": prior, "revision_class": change_class}
    if prior_revision is not None:
        history["prior_revision"] = prior_revision_carrier
    if mapping:
        history["identity_mapping"] = dict(mapping)
    effects = [_effect("changed", carrier=observed)]
    if mapping and prior_revision is not None:
        effects.extend([_effect("changed", carrier=prior_revision_carrier),
                        {"state": "changed", "carrier": prior, "operation": "relocated_to_canonical_encoding"}])
    return {"operation": "update", "outcome": "applied", "observed": observed,
            "effects": effects,
            "history": history,
            **assessment_evidence}


def _validate_move_filename_scope(root: Path, destination: Path, atom_id: str | None,
                                  owner: str) -> None:
    """Require the destination filename's current-scope token to match its owner."""

    if atom_id is None:
        raise LifecycleError("atom-identity-changed", "moved carrier must retain the current atom_id")
    head = destination.name.split("--", 1)[0]
    tokens = head.split("-")
    identity = atom_id.split("-")
    try:
        index = next(i for i in range(len(tokens) - len(identity) + 1)
                     if tokens[i:i + len(identity)] == identity)
    except StopIteration as error:
        raise LifecycleError("filename-scope-mismatch", "destination filename does not carry the current atom_id") from error
    suffix = tokens[index + len(identity):]
    try:
        project_name = project_identity(root)["project"]["name"]
    except (OSError, ValueError, KeyError, TypeError) as error:
        raise LifecycleError("project-identity-invalid", "project identity is unavailable for filename validation") from error
    if owner == project_name:
        if suffix and suffix[0] == owner:
            raise LifecycleError("filename-scope-mismatch", "Project-owned filename must omit its current Scope Unit token")
    elif not suffix or suffix[0] != owner:
        raise LifecycleError("filename-scope-mismatch", "destination filename must begin with its owning Scope Unit token")


def move_atom_action(root: Path, parameters: Mapping[str, Any], *, execute: bool = False,
                     authorized: bool = False) -> dict[str, Any]:
    """Apply one identity-preserving Atom rehome with a sealed placement."""

    root = root.resolve()
    request = _mapping(parameters, "parameters")
    _exact_fields(request, frozenset({"target", "placement"}), "parameters")
    placement = _mapping(request["placement"], "placement")
    _exact_fields(placement, frozenset({"destination_path", "owning_scope_unit", "claim_target_scope_unit"}),
                  "placement")
    if any(not isinstance(placement[field], str) or not placement[field].strip()
           for field in placement):
        raise LifecycleError("placement-invalid", "placement fields must be non-empty strings")
    destination_value = Path(placement["destination_path"])
    if destination_value.is_absolute() or ".." in destination_value.parts:
        raise LifecycleError("placement-invalid", "destination_path must be project-relative")
    target = _resolve_descriptor(root, request["target"], name="target", active=False)
    prior = carrier_descriptor(root, target)
    destination_path = placement["destination_path"]
    current_owner = frontmatter_scalar(target.frontmatter, "current_scope_unit")
    current_claim_target = frontmatter_scalar(target.frontmatter, "claim_target_scope_unit")
    if current_owner is None or current_claim_target is None:
        raise LifecycleError("placement-invalid", "current Atom must carry both Scope Unit fields")
    outward_links = _typed_relation_snapshot(target.frontmatter)

    proposed_frontmatter = replace_frontmatter_scalar(
        replace_frontmatter_scalar(target.frontmatter, "current_scope_unit", placement["owning_scope_unit"]),
        "claim_target_scope_unit", placement["claim_target_scope_unit"],
    )
    # prepare_create_atom_revision performs the complete destination, filename,
    # owner/path, status, relation, and collision preflight without mutation.
    try:
        destination, normalized, destination_id = prepare_create_atom_revision(
            root, destination_path, proposed_frontmatter, target.content, creating=False,
        )
    except AtomToolError as error:
        raise _translate(error) from error
    if destination_id != target.atom_id:
        raise LifecycleError("atom-identity-changed", "moved carrier must retain the current atom_id")
    if destination != target.path and destination.exists():
        raise LifecycleError("destination-collision", "Atom destination already exists")
    same_placement = (
        destination == target.path
        and placement["owning_scope_unit"] == current_owner
        and placement["claim_target_scope_unit"] == current_claim_target
    )
    if not same_placement:
        _validate_move_filename_scope(root, destination, target.atom_id, placement["owning_scope_unit"])
    if frontmatter_scalar(normalized, "content_role") != frontmatter_scalar(target.frontmatter, "content_role"):
        raise LifecycleError("atom-role-changed", "move must retain the current Content Role")
    if frontmatter_scalar(normalized, "type") != frontmatter_scalar(target.frontmatter, "type"):
        raise LifecycleError("atom-type-changed", "move must retain the current Type")
    try:
        bundle = status_bundle_snapshot(root, target)
    except AtomToolError as error:
        raise _translate(error) from error
    destination_bundle = destination.with_suffix("")
    if destination != target.path and (destination_bundle.exists() or destination_bundle.is_symlink()):
        raise LifecycleError("destination-collision", "matching destination directory already exists")
    if same_placement:
        return {"operation": "move", "outcome": "no-op", "observed": prior,
                "placement": {"before": {"path": prior["path"], "owner": current_owner,
                                            "claim_target_scope_unit": current_claim_target},
                               "after": {"path": prior["path"], "owner": current_owner,
                                          "claim_target_scope_unit": current_claim_target}},
                "typed_links": _move_link_evidence(outward_links),
                "effects": [_effect("unchanged", carrier=prior, reason="placement-already-current")],
                "history": {"prior": prior, "preserved": True}}
    if not _execute_allowed(execute=execute, authorized=authorized):
        return {"operation": "move", "outcome": "preview", "observed": prior,
                "placement": {"before": {"path": prior["path"], "owner": current_owner,
                                            "claim_target_scope_unit": current_claim_target},
                               "after": {"path": destination.relative_to(root).as_posix(),
                                          "owner": placement["owning_scope_unit"],
                                          "claim_target_scope_unit": placement["claim_target_scope_unit"]}},
                "typed_links": _move_link_evidence(outward_links),
                "effects": [_effect("unchanged", carrier=prior, reason="preview")],
                "history": {"prior": prior}}

    before_bytes = target.path.read_bytes()
    before_mode = target.path.stat().st_mode & 0o777
    if hashlib.sha256(before_bytes).hexdigest() != prior["digest"]:
        raise LifecycleError("carrier-stale", "move source bytes changed before publication")
    raw_body = _raw_carrier_body(before_bytes)
    try:
        body_for_publication = raw_body.decode("utf-8")
    except UnicodeDecodeError as error:
        raise LifecycleError("carrier-encoding-invalid", "move source body is not valid UTF-8") from error
    prior_revision: Atom | None = None
    prior_revision_owner: tuple[int, int] | None = None
    observed_atom: Atom | None = None
    attempted_destination_bytes: bytes | None = None
    try:
        revised_frontmatter = _refresh_frontmatter(root, normalized, version=atom_version(target) + 1)
        attempted_destination_bytes = render(revised_frontmatter, body_for_publication)
        prior_revision = preserve_atom_revision(root, target, allow_nonactive=True)
        owned = prior_revision.path.lstat()
        prior_revision_owner = (owned.st_dev, owned.st_ino)
        observed_atom = move_atom_revision(
            root, target, destination.relative_to(root).as_posix(), revised_frontmatter, body_for_publication,
            expected_bundle=bundle,
        )
        observed = carrier_descriptor(root, observed_atom)
        moved_bundle = status_bundle_snapshot(root, observed_atom)
        if (observed["path"] != destination.relative_to(root).as_posix()
                or observed["filename"] != destination.name
                or observed["atom_id"] != prior["atom_id"] or observed["version"] != prior["version"] + 1
                or observed["status"] != prior["status"] or observed["content_role"] != prior["content_role"]
                or observed["type"] != prior["type"] or observed_atom.content != target.content
                or _typed_relation_snapshot(observed_atom.frontmatter) != outward_links
                or frontmatter_scalar(observed_atom.frontmatter, "current_scope_unit") != placement["owning_scope_unit"]
                or frontmatter_scalar(observed_atom.frontmatter, "claim_target_scope_unit") != placement["claim_target_scope_unit"]
                or (destination != target.path and target.path.exists())
                or destination.read_bytes() != attempted_destination_bytes
                or _raw_carrier_body(destination.read_bytes()) != raw_body
                or prior_revision.path.read_bytes() != before_bytes
                or not carrier_directory_snapshot_matches(
                    {key: value for key, value in bundle.items() if key != "markdown"},
                    {key: value for key, value in moved_bundle.items() if key != "markdown"},
                    renamed=True,
                )):
            raise LifecycleError("move-verification-failed", "moved carrier failed independent readback")
    except BaseException as error:
        recovery_phase = "restore-current"
        try:
            source_directory = target.path.with_suffix("")
            destination_directory = destination.with_suffix("")
            if "directory" in bundle:
                expected_directory = bundle["directory"][1][:2]
                if destination_directory == source_directory:
                    recovery_phase = "verify-source-directory"
                    if (destination_directory.is_symlink() or not destination_directory.is_dir()
                            or (destination_directory.stat().st_dev, destination_directory.stat().st_ino)
                            != expected_directory):
                        raise OSError("source directory ownership could not be verified")
                    source_bundle = carrier_directory_snapshot(root, source_directory)
                    if not carrier_directory_snapshot_matches(
                            {key: value for key, value in bundle.items() if key != "markdown"}, source_bundle):
                        raise OSError("source directory contents changed during recovery")
                elif destination_directory.exists() or destination_directory.is_symlink():
                    recovery_phase = "verify-directory-ownership"
                    if (destination_directory.is_symlink() or not destination_directory.is_dir()
                            or source_directory.exists() or source_directory.is_symlink()
                            or (destination_directory.stat().st_dev, destination_directory.stat().st_ino)
                            != expected_directory):
                        raise OSError("moved directory ownership could not be verified")
                    moved_bundle = carrier_directory_snapshot(root, destination_directory)
                    if not carrier_directory_snapshot_matches(
                            {key: value for key, value in bundle.items() if key != "markdown"},
                            moved_bundle, renamed=True):
                        raise OSError("moved directory contents changed during recovery")
                    recovery_phase = "restore-directory"
                    destination_directory.rename(source_directory)
                elif (not source_directory.is_dir() or source_directory.is_symlink()
                      or (source_directory.stat().st_dev, source_directory.stat().st_ino) != expected_directory):
                    raise OSError("source directory ownership could not be verified")
                else:
                    source_bundle = carrier_directory_snapshot(root, source_directory)
                    if not carrier_directory_snapshot_matches(
                            {key: value for key, value in bundle.items() if key != "markdown"}, source_bundle):
                        raise OSError("source directory contents changed during recovery")
            if destination != target.path and destination.exists():
                if destination.is_symlink() or not destination.is_file():
                    raise OSError("destination ownership could not be verified")
                if attempted_destination_bytes is None or destination.read_bytes() != attempted_destination_bytes:
                    raise OSError("destination ownership could not be verified")
                recovery_phase = "remove-new-destination"
                destination.unlink()
            if target.path.is_symlink():
                raise OSError("current carrier became a symlink")
            if target.path.exists() and (not target.path.is_file() or target.path.read_bytes() != before_bytes):
                raise OSError("current source ownership could not be verified")
            if not target.path.exists():
                _atomic_write(target.path, before_bytes)
            if target.path.stat().st_mode & 0o777 != before_mode:
                target.path.chmod(before_mode)
            if target.path.read_bytes() != before_bytes or target.path.stat().st_mode & 0o777 != before_mode:
                raise OSError("current before-state could not be verified")
            if prior_revision is not None:
                recovery_phase = "verify-history-ownership"
                owned = prior_revision.path.lstat()
                if (prior_revision.path.is_symlink() or not prior_revision.path.is_file()
                        or (owned.st_dev, owned.st_ino) != prior_revision_owner
                        or prior_revision.path.read_bytes() != before_bytes):
                    raise OSError("new prior-revision carrier ownership could not be verified")
                recovery_phase = "remove-new-history"
                prior_revision.path.unlink()
        except BaseException as recovery_error:
            current_ref = {"path": target.relative, "verification": "unknown"}
            destination_ref = None
            if destination != target.path:
                destination_ref = {
                    "path": destination.relative_to(root).as_posix(),
                    "verification": "unknown" if destination.exists() else "absent",
                }
            bundle_ref = None
            if "directory" in bundle:
                bundle_ref = {
                    "source": {"path": source_directory.relative_to(root).as_posix(),
                               "verification": "unknown" if source_directory.exists() else "absent"},
                    "destination": {"path": destination_directory.relative_to(root).as_posix(),
                                    "verification": "unknown" if destination_directory.exists() else "absent"},
                }
            retained_history = ({"path": prior_revision.relative, "creation": "attempt-created",
                                 "ownership_verification": "unverified"}
                                if prior_revision is not None else None)
            effects = [_effect("unknown", carrier=current_ref, reason="move-rollback-uncertain")]
            if destination_ref is not None and destination_ref["verification"] == "unknown":
                effects.append(_effect("unknown", carrier=destination_ref,
                                       reason="retained-destination-ownership-unverified"))
            history = {"prior": prior}
            if retained_history is not None:
                history["prior_revision"] = retained_history
                effects.append(_effect("unknown", carrier=retained_history,
                                       reason="retained-prior-ownership-unverified"))
            if bundle_ref is not None:
                for endpoint in (bundle_ref["source"], bundle_ref["destination"]):
                    if endpoint["verification"] == "unknown":
                        effects.append(_effect("unknown", carrier=endpoint,
                                               reason="retained-bundle-ownership-unverified"))
            return {"operation": "move", "outcome": "partial",
                    "failure": {"code": "move-rollback-uncertain",
                                "original": {"type": type(error).__name__, "code": getattr(error, "code", None)},
                                "recovery": {"type": type(recovery_error).__name__,
                                              "code": getattr(recovery_error, "code", None),
                                              "phase": recovery_phase}},
                    "effects": effects, "history": history,
                    "recovery": {"before": prior, "current": current_ref,
                                 "destination": destination_ref, "prior_revision": retained_history,
                                 "bundle": bundle_ref,
                                 "automatic_retry": False}}
        if isinstance(error, AtomToolError):
            raise _translate(error) from error
        raise
    observed = carrier_descriptor(root, observed_atom)
    prior_revision_carrier = carrier_descriptor(root, prior_revision) if prior_revision is not None else None
    history: dict[str, Any] = {"prior": prior, "prior_revision": prior_revision_carrier}
    effects = [_effect("changed", carrier=observed)]
    if "directory" in bundle and destination_bundle != target.path.with_suffix(""):
        effects.append(_effect("changed", carrier={"path": destination_bundle.relative_to(root).as_posix()}))
    if prior_revision_carrier is not None:
        effects.append(_effect("changed", carrier=prior_revision_carrier))
    return {"operation": "move", "outcome": "applied", "observed": observed,
            "placement": {"before": {"path": prior["path"], "owner": current_owner,
                                        "claim_target_scope_unit": current_claim_target},
                           "after": {"path": observed["path"], "owner": placement["owning_scope_unit"],
                                      "claim_target_scope_unit": placement["claim_target_scope_unit"]}},
            "typed_links": _move_link_evidence(outward_links),
            "effects": effects,
            "history": history}


def change_status_atom_action(root: Path, parameters: Mapping[str, Any], *, execute: bool = False, authorized: bool = False) -> dict[str, Any]:
    """Apply one source-model-derived status change; callers cannot supply a model."""

    root = root.resolve()
    preflight = preflight_atom_lifecycle(root, "change_status", parameters)
    target, prior = preflight["target"], preflight["prior"]
    requested, current_status = preflight["requested_status"], preflight["current_status"]
    model, archive = preflight["status_model"], preflight["archive"]
    if requested == current_status:
        return {"operation": "change_status", "outcome": "no-op", "prior_status": current_status,
                "observed": prior, "status_model": model,
                "effects": [_effect("unchanged", carrier=prior, reason="status-already-current")], "broken_references": []}
    bundle = status_bundle_snapshot(root, target)
    diagnostics = _broken_references(root, target) if archive and target.atom_id is not None else []
    if not _execute_allowed(execute=execute, authorized=authorized):
        return {"operation": "change_status", "outcome": "preview", "prior_status": current_status, "observed": prior,
                "status_model": model,
                "effects": [_effect("unchanged", carrier=prior, reason="preview")], "broken_references": diagnostics}
    refreshed = preflight_atom_lifecycle(root, "change_status", parameters)
    if refreshed["status_model"] != model:
        raise LifecycleError("status-model-stale", "authoritative status-model source changed after preflight")
    frontmatter = replace_frontmatter_scalar(target.frontmatter, "status", requested)
    frontmatter = _refresh_frontmatter(root, frontmatter, version=atom_version(target) + 1)
    observed_atom, prior_revision = _publish_status_change(root, target, requested, frontmatter, target.content,
                                                         expected_bundle=bundle)
    observed = carrier_descriptor(root, observed_atom)
    result: dict[str, Any] = {
        "operation": "change_status",
        "outcome": "applied",
        "prior_status": current_status,
        "observed": observed,
        "status_model": model,
        "effects": [_effect("changed", carrier=observed)],
        "broken_references": diagnostics,
    }
    if archive:
        result["repair_handoff"] = {"operation": "repair_relations", "broken_references": diagnostics,
                                    "automatic_repair": False}
    if prior_revision is not None:
        result["history"] = {"prior": prior, "prior_revision": carrier_descriptor(root, prior_revision)}
    return result


def _publish_status_change(root: Path, target: Atom, requested: str, frontmatter: str, content: str, *,
                           expected_bundle: Mapping | None = None) -> tuple[Atom, Atom | None]:
    """One native status publication owner for both Change Status and Update."""
    prior_revision = None
    try:
        if requested.casefold() == "draft":
            observed = demote_atom_to_draft(root, target, frontmatter, content, expected_bundle=expected_bundle)
            # The shared publisher retained the exact identified predecessor.
            local = target.path.parent
            if local.name in {"001_backlog", "done", "canceled", "archived", "resolved", "draft"}:
                local = local.parent
            stem = re.sub(r"@[0-9]+$", "", target.path.stem)
            prior_revision = atom_from_path(root, local / "archive" / f"{stem}@{atom_version(target)}.md")
        elif target.atom_id is None:
            with atom_identity_lock(root):
                identity = _draft_promotion_identity(root, target)
                match = re.fullmatch(r"([A-Za-z0-9]+-[A-Z]+)--(.+)", target.filename)
                if match is None:
                    raise LifecycleError("draft-promotion-invalid", "Draft filename has no admitted role prefix")
                separator = "-" if "--" in match.group(2) else "--"
                filename = f"{identity}{separator}{match.group(2)}"
                destination = _status_destination(root, target, requested, filename=filename,
                                                  version=int(frontmatter_scalar(frontmatter, "version")))
                observed = promote_draft_atom(root, target, identity, frontmatter, content, relative_path=destination,
                                               expected_bundle=expected_bundle)
        else:
            observed, history_path = publish_status_atom_revision(
                root, target, _status_destination(root, target, requested), frontmatter, content,
                expected_bundle=status_bundle_snapshot(root, target) if expected_bundle is None else expected_bundle)
            prior_revision = atom_from_path(root, history_path) if history_path is not None else None
        return observed, prior_revision
    except AtomToolError as error:
        raise _translate(error) from error


def replace_atom_action(root: Path, parameters: Mapping[str, Any], *, execute: bool = False, authorized: bool = False) -> dict[str, Any]:
    """Publish supplied successors before archiving one predecessor."""

    root = root.resolve()
    request = _mapping(parameters, "parameters")
    _exact_fields(request, frozenset({"predecessor", "successors", "status_model"}), "parameters")
    predecessor = _resolve_descriptor(root, request["predecessor"], name="predecessor")
    prior = carrier_descriptor(root, predecessor)
    successors = _proposed_successors(root, request["successors"], predecessor)
    try:
        existing_ids = {atom.atom_id for atom in scan_atoms(root) if atom.atom_id is not None}
        for successor in successors:
            destination, _, atom_id = prepare_create_atom_revision(
                root, successor["path"], successor["frontmatter"], successor["content"]
            )
            if destination.exists():
                raise AtomToolError("destination-collision", f"Atom destination already exists: {destination.relative_to(root)}")
            if atom_id is not None and atom_id in existing_ids:
                raise AtomToolError("atom-id-collision", f"Atom ID already exists: {atom_id}")
    except AtomToolError as error:
        raise _translate(error) from error
    supplied_model = _mapping(request["status_model"], "status_model")
    try:
        model = resolve_status_model(root, predecessor, "Archived")
    except StatusModelError as error:
        raise LifecycleError("archive-status-unavailable", "qualified current status model has no Archived value") from error
    if supplied_model != model:
        raise LifecycleError("model-forged", "Replace status model differs from authoritative current sources")
    archive_status = "Archived"
    if not _execute_allowed(execute=execute, authorized=authorized):
        return {"operation": "replace", "outcome": "preview", "predecessor": prior, "successors": successors,
                "effects": [_effect("unchanged", carrier=prior, reason="preview")], "history": {"predecessor": prior}}
    try:
        predecessor_bundle = status_bundle_snapshot(root, predecessor)
        if hashlib.sha256(predecessor_bundle["markdown"][0]).hexdigest() != prior["digest"]:
            raise AtomToolError("stale-carrier", "replacement predecessor changed before publication")
    except AtomToolError as error:
        raise _translate(error) from error
    published: list[dict[str, Any]] = []
    try:
        for successor in successors:
            created = create_atom_revision(root, successor["path"], successor["frontmatter"], successor["content"])
            published.append(carrier_descriptor(root, created))
        frontmatter = replace_frontmatter_scalar(predecessor.frontmatter, "status", archive_status)
        frontmatter = _refresh_frontmatter(root, frontmatter, version=atom_version(predecessor) + 1)
        archived = archive_atom_revision(root, predecessor, frontmatter, predecessor.content,
                                        expected_bundle=predecessor_bundle)
    except AtomToolError as error:
        if not published:
            raise _translate(error) from error
        phase = "archive_predecessor" if len(published) == len(successors) else "publish_successor"
        effects = [_effect("changed", carrier=carrier) for carrier in published]
        effects.append({"state": "unknown", "phase": phase, "reason": error.code})
        return {
            "operation": "replace",
            "outcome": "partial",
            "predecessor": prior,
            "successors": published,
            "effects": effects,
            "unknown_remainder": [{"phase": phase, "code": error.code, "message": error.message}],
            "history": {"predecessor": prior, "successors": published},
        }
    observed = carrier_descriptor(root, archived)
    history_path = archived.path.with_name(
        re.sub(r"@[0-9]+$", "", predecessor.path.stem) + f"@{atom_version(predecessor)}.md")
    prior_revision = {**prior, "path": history_path.relative_to(root).as_posix(),
                      "filename": history_path.name, "lifecycle": "archived"}
    return {"operation": "replace", "outcome": "applied", "predecessor": observed, "successors": published,
            "effects": [_effect("changed", carrier=carrier) for carrier in [*published, observed, prior_revision]],
            "history": {"predecessor": prior, "prior_revision": prior_revision, "successors": published}}
