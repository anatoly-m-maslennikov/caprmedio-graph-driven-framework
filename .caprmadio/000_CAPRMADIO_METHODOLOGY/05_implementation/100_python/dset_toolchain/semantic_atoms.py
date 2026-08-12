"""Provide DSET semantic atoms behavior."""

from __future__ import annotations

import hashlib
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from .diagnostics import Diagnostic
from .frontmatter import FrontmatterError
from .frontmatter import metadata as frontmatter_metadata
from .identity import has_logical_part, iter_control_files
from .layout import discover_layout
from .legacy_authority import validate_legacy_authority_ledger
from .lineage import ArtifactRelation, parse_authored_relations
from .semantic_types import (
    SEMANTIC_ID_KINDS,
    SEMANTIC_SUBTYPES,
    normalize_semantic_classification,
    semantic_id_kind,
    semantic_id_matches_classification,
    semantic_naming_axis,
)
from .settings import load_project_settings
from .structured_data import StructuredDataError, dump, load

# ID_PATTERN validates id pattern; this module owns the accepted syntax.
ID_PATTERN = re.compile(r"^[A-Z][A-Z0-9]*(?:-[A-Z0-9]+)+$")
# SESSION_PATTERN validates session pattern; this module owns the accepted syntax.
SESSION_PATTERN = re.compile(r"^[a-z][a-z0-9_-]*:[A-Za-z0-9._:-]+$")


@dataclass(frozen=True)
class SemanticAtom:
    """Represent semantic atom behavior and state."""

    semantic_id: str
    carrier_id: str
    path: str
    semantic_type: str
    subtype: str | None
    emission_status: str
    priority: str
    llm_session_ids: tuple[str, ...]
    relations: tuple[ArtifactRelation, ...]
    sha256: str

    @property
    def child_of(self) -> tuple[str, ...]:
        """Expose sealed legacy lineage to compatibility callers."""
        return tuple(
            relation.target
            for relation in self.relations
            if relation.type == "child_of" and relation.target is not None
        )


def collect_semantic_atoms(
    root: Path,
) -> tuple[dict[str, SemanticAtom], list[Diagnostic]]:
    """Collect semantic atoms using the declared repository contract."""
    root = root.resolve()
    atoms: dict[str, SemanticAtom] = {}
    diagnostics: list[Diagnostic] = []
    settings, _ = load_project_settings(root)
    allowed_priorities = {*settings.priority_scale, "unknown"}
    layout = discover_layout(root)
    paths = (
        iter_control_files(root, "*.md")
        if layout.separated
        else sorted(root.rglob("*.md"))
    )
    for path in paths:
        relative = path.relative_to(root)
        if _ignored(relative) or has_logical_part(relative, {"templates"}):
            continue
        metadata = _frontmatter(path)
        if metadata is None or metadata.get("artifact_type") != "atomic_record":
            continue
        atom, issues = _parse_atom(root, path, metadata, allowed_priorities)
        diagnostics.extend(issues)
        if atom is None:
            continue
        previous = atoms.get(atom.semantic_id)
        if previous is not None:
            diagnostics.append(
                Diagnostic(
                    "CAPRMADIO-E159",
                    path,
                    f"duplicate semantic atom ID: {atom.semantic_id}",
                )
            )
            continue
        atoms[atom.semantic_id] = atom
    return atoms, diagnostics


def validate_semantic_atoms(root: Path) -> list[Diagnostic]:
    """Validate semantic atoms using the declared repository contract."""
    atoms, diagnostics = collect_semantic_atoms(root)
    layout = discover_layout(root)
    if not (layout.recursive or layout.separated):
        diagnostics.extend(_validate_ledger(root, atoms))
        diagnostics.extend(validate_legacy_authority_ledger(root))
    return sorted(set(diagnostics))


def seal_atom(root: Path, path: Path) -> Path:
    """Seal atom using the declared repository contract."""
    root = root.resolve()
    path = path.resolve()
    try:
        path.relative_to(root)
    except ValueError as error:
        raise ValueError("atom carrier must be inside the repository") from error
    metadata = _frontmatter(path)
    settings, issues = load_project_settings(root)
    if issues:
        raise ValueError("project settings must pass before sealing an atom")
    if metadata is None:
        raise ValueError("atom carrier requires TOML or YAML frontmatter")
    if "child_of" in metadata:
        raise ValueError(
            "new atoms must use relations; child_of is sealed compatibility input only"
        )
    atom, diagnostics = _parse_atom(
        root, path, metadata, {*settings.priority_scale, "unknown"}
    )
    if diagnostics or atom is None:
        message = diagnostics[0].message if diagnostics else "invalid atom"
        raise ValueError(message)
    expected_kind = semantic_naming_axis(
        atom.semantic_type,
        atom.subtype,
        include_subtype=settings.artifact_subtype_in_names,
    )
    if expected_kind != semantic_id_kind(atom.semantic_id):
        mode = "subtype" if settings.artifact_subtype_in_names else "type"
        raise ValueError(
            f"new atom must use the configured {mode} naming kind: {expected_kind}"
        )
    from .artifact_emission import assess_artifact_candidate

    candidate = {
        "authority": metadata.get("authority"),
        "claim": metadata.get("claim"),
        "type": metadata.get("type"),
        "subtype": metadata.get("subtype"),
        "scope": metadata.get("scope"),
        "llm_session_ids": metadata.get("llm_session_ids"),
        "material_links": _material_relation_links(metadata, path),
        "priority": metadata.get("priority"),
        "acceptance": metadata.get("status"),
        "promotion": metadata.get("promotion"),
    }
    for field in (
        "boundary",
        "lineage",
        "conflict_state",
        "verification_obligation",
        "unknowns",
    ):
        if field in metadata:
            candidate[field] = metadata[field]
    assessment = assess_artifact_candidate(root, candidate)
    if assessment["emission_allowed"] is not True:
        first = assessment["diagnostics"][0]
        raise ValueError(f"artifact emission is blocked: {first['message']}")
    layout = discover_layout(root)
    if layout.recursive or layout.separated:
        return path
    ledger_path = _ledger_path(root)
    data = _load_or_empty(ledger_path, "records")
    records = data["records"]
    assert isinstance(records, list)
    if any(
        isinstance(item, dict) and item.get("semantic_id") == atom.semantic_id
        for item in records
    ):
        raise FileExistsError(f"atom is already sealed: {atom.semantic_id}")
    records.append(_ledger_record(atom))
    records.sort(key=lambda item: str(item.get("semantic_id", "")))
    _atomic_dump(ledger_path, data)
    return ledger_path


def effective_priority(root: Path, atom: SemanticAtom) -> tuple[str, str]:
    """Handle priority using the declared repository contract."""
    if atom.priority == "unknown":
        return "unknown", f"atom:{atom.semantic_id}"
    return atom.priority, f"atom:{atom.semantic_id}"


def build_semantic_atom_index(root: Path) -> list[dict[str, Any]]:
    """Build current atom, priority, relation, and archive lookup."""
    atoms, diagnostics = collect_semantic_atoms(root)
    if diagnostics:
        raise ValueError(diagnostics[0].message)
    replaced_by: dict[str, list[str]] = {}
    for candidate in atoms.values():
        for relation in candidate.relations:
            if relation.type == "replacement_of" and relation.target is not None:
                replaced_by.setdefault(relation.target, []).append(
                    candidate.semantic_id
                )
    rows: list[dict[str, Any]] = []
    for atom in atoms.values():
        priority, priority_source = effective_priority(root, atom)
        archived = "archive" in Path(atom.path).parts
        rows.append(
            {
                "id": atom.semantic_id,
                "carrier_id": atom.carrier_id,
                "carrier": Path(atom.path).name,
                "sha256": atom.sha256,
                "type": atom.semantic_type,
                "subtype": atom.subtype or "none",
                "emission_status": atom.emission_status,
                "current_status": "archived" if archived else atom.emission_status,
                "priority": priority,
                "priority_source": priority_source,
                "relations": [relation.as_dict() for relation in atom.relations],
                "replaced_by": sorted(replaced_by.get(atom.semantic_id, [])),
                "archived": archived,
            }
        )
    return sorted(rows, key=lambda item: str(item["id"]))


def archive_atom(root: Path, semantic_id: str) -> Path:
    """Move an inactive atom byte-for-byte into its Type-local archive."""
    root = root.resolve()
    atoms, diagnostics = collect_semantic_atoms(root)
    if diagnostics:
        raise ValueError(diagnostics[0].message)
    atom = atoms.get(semantic_id)
    if atom is None:
        raise ValueError(f"unknown semantic atom: {semantic_id}")
    source = root / atom.path
    if "archive" in source.relative_to(root).parts:
        raise ValueError(f"semantic atom is already archived: {semantic_id}")
    active_dependants = [
        candidate.semantic_id
        for candidate in atoms.values()
        if any(
            relation.target == semantic_id
            and relation.type in {"child_of", "override_of"}
            for relation in candidate.relations
        )
        and "archive" not in Path(candidate.path).parts
    ]
    if active_dependants:
        raise ValueError(
            "semantic atom has active child reliance: "
            + ", ".join(sorted(active_dependants))
        )
    destination = source.parent / "archive" / source.name
    if destination.exists():
        raise FileExistsError(f"archive destination already exists: {source.name}")
    destination.parent.mkdir(parents=True, exist_ok=True)
    source.replace(destination)
    layout = discover_layout(root)
    if not (layout.recursive or layout.separated):
        ledger_path = _ledger_path(root)
        data = _load_or_empty(ledger_path, "records")
        records = data["records"]
        assert isinstance(records, list)
        for record in records:
            if isinstance(record, dict) and record.get("semantic_id") == semantic_id:
                record["path"] = destination.relative_to(root).as_posix()
                break
        else:
            destination.replace(source)
            raise ValueError(f"semantic atom is not sealed: {semantic_id}")
        _atomic_dump(ledger_path, data)
    return destination


def _parse_atom(
    root: Path,
    path: Path,
    data: dict[str, Any],
    allowed_priorities: set[str],
) -> tuple[SemanticAtom | None, list[Diagnostic]]:
    """Parse atom using the declared repository contract."""
    diagnostics: list[Diagnostic] = []
    raw_semantic_type = data.get("type")
    raw_subtype = data.get("subtype")
    subtype = None if raw_subtype is None or raw_subtype == "none" else raw_subtype
    semantic_type = raw_semantic_type
    if isinstance(raw_semantic_type, str):
        semantic_type, subtype = normalize_semantic_classification(
            raw_semantic_type,
            str(subtype) if subtype is not None else None,
        )
    semantic_id = data.get("semantic_id")
    carrier_id = data.get("artifact_id")
    status = data.get("status")
    priority = data.get("priority")
    sessions = data.get("llm_session_ids")
    if semantic_type not in SEMANTIC_SUBTYPES:
        diagnostics.append(_atom_diag(path, "atom requires one of the four Types"))
    elif subtype is not None and subtype not in SEMANTIC_SUBTYPES[semantic_type]:
        diagnostics.append(_atom_diag(path, "atom has an invalid direct subtype"))
    elif semantic_type == "qa" and subtype not in {
        "test_case",
        "evaluation_case",
    }:
        diagnostics.append(
            _atom_diag(path, "QA atom requires test_case or evaluation_case")
        )
    if not isinstance(semantic_id, str) or not ID_PATTERN.fullmatch(semantic_id):
        diagnostics.append(_atom_diag(path, "atom requires a canonical semantic_id"))
    elif semantic_type in SEMANTIC_SUBTYPES:
        expected = SEMANTIC_ID_KINDS.get((semantic_type, subtype))
        if expected is None or not semantic_id_matches_classification(
            semantic_id, semantic_type, subtype
        ):
            diagnostics.append(
                _atom_diag(path, f"semantic_id must use the {expected} kind")
            )
    if not isinstance(carrier_id, str) or not ID_PATTERN.fullmatch(carrier_id):
        diagnostics.append(_atom_diag(path, "atom requires a canonical artifact_id"))
    if status not in {"proposed", "accepted"}:
        diagnostics.append(
            _atom_diag(path, "emission status must be proposed or accepted")
        )
    if priority not in allowed_priorities:
        diagnostics.append(_atom_diag(path, "atom priority is not in project scale"))
    if not _valid_sessions(sessions):
        diagnostics.append(
            _atom_diag(path, "atom requires unique host-prefixed llm_session_ids")
        )
    relations = parse_authored_relations(path, data, diagnostics)
    if diagnostics:
        return None, diagnostics
    assert isinstance(semantic_id, str)
    assert isinstance(carrier_id, str)
    assert isinstance(semantic_type, str)
    assert isinstance(status, str)
    assert isinstance(priority, str)
    assert isinstance(sessions, list)
    return (
        SemanticAtom(
            semantic_id=semantic_id,
            carrier_id=carrier_id,
            path=path.relative_to(root).as_posix(),
            semantic_type=semantic_type,
            subtype=str(subtype) if subtype is not None else None,
            emission_status=status,
            priority=priority,
            llm_session_ids=tuple(str(item) for item in sessions),
            relations=relations,
            sha256=_digest(path),
        ),
        diagnostics,
    )


def _material_relation_links(data: dict[str, Any], path: Path) -> list[str]:
    """Handle relation links using the declared repository contract."""
    diagnostics: list[Diagnostic] = []
    relations = parse_authored_relations(path, data, diagnostics)
    if diagnostics:
        raise ValueError(diagnostics[0].message)
    links: list[str] = []
    for relation in relations:
        if relation.target is not None:
            links.append(relation.target)
        elif relation.range is not None:
            links.append(relation.range.through)
    return links


def _validate_ledger(root: Path, atoms: dict[str, SemanticAtom]) -> list[Diagnostic]:
    """Validate ledger using the declared repository contract."""
    path = _ledger_path(root)
    if not path.is_file():
        if atoms:
            return [Diagnostic("CAPRMADIO-E161", path, "semantic atom ledger is missing")]
        return []
    try:
        data = load(path)
    except (OSError, UnicodeError, StructuredDataError) as error:
        return [Diagnostic("CAPRMADIO-E161", path, f"invalid atom ledger: {error}")]
    records = data.get("records") if isinstance(data, dict) else None
    if not isinstance(data, dict) or str(data.get("schema_version")) != "1.0":
        return [Diagnostic("CAPRMADIO-E161", path, "atom ledger schema_version must be 1.0")]
    if not isinstance(records, list):
        return [Diagnostic("CAPRMADIO-E161", path, "atom ledger records must be a list")]
    diagnostics: list[Diagnostic] = []
    indexed: dict[str, dict[str, Any]] = {}
    for record in records:
        if not isinstance(record, dict) or not isinstance(
            record.get("semantic_id"), str
        ):
            diagnostics.append(Diagnostic("CAPRMADIO-E161", path, "invalid ledger record"))
            continue
        identifier = str(record["semantic_id"])
        if identifier in indexed:
            diagnostics.append(
                Diagnostic("CAPRMADIO-E161", path, f"duplicate ledger atom: {identifier}")
            )
        indexed[identifier] = record
    for identifier, atom in atoms.items():
        record = indexed.get(identifier)
        if record is None:
            diagnostics.append(
                Diagnostic("CAPRMADIO-E161", root / atom.path, "emitted atom is not sealed")
            )
            continue
        expected = _ledger_record(atom)
        comparisons = {
            "carrier_id": "carrier_id",
            "type": "type",
            "subtype": "subtype",
            "current_path" if "current_path" in record else "path": "path",
            "current_sha256" if "current_sha256" in record else "sha256": "sha256",
        }
        for recorded_field, expected_field in comparisons.items():
            if record.get(recorded_field) != expected.get(expected_field):
                diagnostics.append(
                    Diagnostic(
                        "CAPRMADIO-E161",
                        root / atom.path,
                        f"sealed atom {recorded_field} changed: {identifier}",
                    )
                )
    for identifier in sorted(set(indexed) - set(atoms)):
        record_path = indexed[identifier].get(
            "current_path", indexed[identifier].get("path")
        )
        if not isinstance(record_path, str) or not (root / record_path).is_file():
            diagnostics.append(
                Diagnostic("CAPRMADIO-E161", path, f"sealed atom is missing: {identifier}")
            )
    return diagnostics


def _ledger_record(atom: SemanticAtom) -> dict[str, Any]:
    """Handle record using the declared repository contract."""
    return {
        "semantic_id": atom.semantic_id,
        "carrier_id": atom.carrier_id,
        "path": atom.path,
        "sha256": atom.sha256,
        "type": atom.semantic_type,
        "subtype": atom.subtype if atom.subtype is not None else "none",
    }


def _load_or_empty(path: Path, field: str) -> dict[str, Any]:
    """Load or empty using the declared repository contract."""
    if not path.is_file():
        return {"schema_version": "1.0", field: []}
    data = load(path)
    if not isinstance(data, dict) or str(data.get("schema_version")) != "1.0":
        raise ValueError(f"invalid registry: {path}")
    values = data.get(field)
    if not isinstance(values, list):
        raise ValueError(f"registry field must be a list: {field}")
    return data


def _atomic_dump(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(dump(data, path), encoding="utf-8")
    temporary.replace(path)


def _frontmatter(path: Path) -> dict[str, Any] | None:
    try:
        data = frontmatter_metadata(path)
    except (OSError, UnicodeError, FrontmatterError):
        return None
    return data if isinstance(data, dict) else None


def _valid_sessions(value: object) -> bool:
    """Handle sessions using the declared repository contract."""
    return (
        isinstance(value, list)
        and len(value) == len(set(str(item) for item in value))
        and all(
            isinstance(item, str) and SESSION_PATTERN.fullmatch(item) for item in value
        )
    )


def _ignored(relative: Path) -> bool:
    """Handle ignored using the declared repository contract."""
    if relative.parts[:1] == (".caprmadio_runtime",) or relative.parts[:2] == (
        ".caprmadio",
        "runtime",
    ):
        return True
    ignored = {".git", ".cache", ".venv", "__pycache__", "dist"}
    return any(
        part in ignored or (part.startswith(".") and part not in {".github", ".caprmadio"})
        for part in relative.parts
    )


def _digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _ledger_path(root: Path) -> Path:
    layout = discover_layout(root)
    return layout.structured_file(layout.project_state_root, "atoms.toml")


def _atom_diag(path: Path, message: str) -> Diagnostic:
    return Diagnostic("CAPRMADIO-E159", path, message)
