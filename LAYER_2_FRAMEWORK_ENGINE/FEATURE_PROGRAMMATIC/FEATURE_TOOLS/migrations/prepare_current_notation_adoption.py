"""SHA-pinned, dry-run-only Current Subject migration; no carrier writer."""
from __future__ import annotations

import argparse
from dataclasses import replace
import hashlib
import json
from pathlib import Path
import re
import sys
from typing import Any

TOOLS = Path(__file__).resolve().parents[1]
if str(TOOLS) not in sys.path:
    sys.path.insert(0, str(TOOLS))

from subject_notation import (Name, Path as SubjectPath, PathStep, Qualification,
                              RelationChain, SubjectNotationError, ValueLiteral,
                              parse_subject_expression, render_subject)
from VALIDATE_ATOMS.validate_atoms_workers.parsing import CarrierError, parse_carrier

PRUNED = frozenset({"draft", "drafts", "archive", "archived", "_journal", "_projection",
                   "execution_evidence", "done", "cancelled", "canceled", "resolved", "solved",
                   "000_CAPRMEDIO_framework", "002_INSTALLED_EXTENSIONS"})
PROPERTY_NAMES = frozenset({"Content Role", "Type"})
REVIEWED_PROPERTY_SOURCES = {
    "CA-R-1284": (23, "ed846912a5858e8103dfb5189cf574379488dcfde81d52521fafe48a4c7d0622"),
    "CA-R-1531": (20, "d249d9f4de10a47522a3f7f377ad43ee87a2cf9eb31f534bf53898e8c4d3b622"),
    "CA-D-478": (29, "7ad522f00eb7af8995c0f97519b74dfd89c90b00defbac0bc20bc2e041c23ec3"),
    "CA-R-2397": (1, "f672c42a80ca28f1d623135be29a75ca135934f2ba3f767b384fb63e40fdbb15"),
    "CA-R-1758": (34, "7ce62f78d7090f06de789d50a6985abd1989231910c3ae5f3f45fbde4bbff51e"),
}

ATOM_OWNERS = frozenset({"Atom", "Entity/Object/Continuant/Atom", "Entity/Object/Continuant/Governing Objects/Atom", "Entity/Node/Continuant/Atom", "Subject/CAPRMEDIO/Graph/Node/Project Model/Atom", "Subject/Graph Node/Domain/Continuant/Atom"})
CURRENT_STATUSES = frozenset({"backlog", "active", "done", "canceled"})


def _current(metadata: dict[str, Any]) -> bool:
    return str(metadata.get("status", "")).casefold() in CURRENT_STATUSES
CANDIDATE = re.compile(r"/(?:Content Role|Type)\s*:|(?<![+])>(?![|])|::")


def digest(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def _containment(text: str) -> tuple[str, int]:
    """Recognize the old relation token outside escaped/quoted names."""
    result: list[str] = []
    index, count = 0, 0
    quoted = False
    while index < len(text):
        char = text[index]
        if char == "\\":
            result.append(text[index:index + 2])
            index += 2
            continue
        if char == '"':
            quoted = not quoted
        if char != ">" or quoted or text[index:index + 2] == ">|" or (index and text[index - 1] == "+"):
            result.append(char)
            index += 1
            continue
        if index and text[index - 1] in "-=<>":
            raise ValueError("unknown operator before legacy containment token")
        index += 1
        match = re.match(r"\s*(\{[0-9]+(?:\+|\.\.[0-9]+)?\})", text[index:])
        cardinality = match[1] if match else ""
        if match:
            index += match.end()
        result.append(" " + cardinality + "<+ ")
        count += 1
    return "".join(result), count


def _qualify(expression: SubjectPath | RelationChain, unresolved: list[str], property_owners: dict[str, frozenset[str]], accesses: list[int]) -> tuple[SubjectPath | RelationChain, int]:
    if isinstance(expression, RelationChain):
        endpoints, count = [], 0
        for endpoint in expression.endpoints:
            converted, changes = _qualify(endpoint, unresolved, property_owners, accesses)
            endpoints.append(converted)
            count += changes
        return replace(expression, endpoints=tuple(endpoints)), count
    head = expression.head
    count = 0
    if isinstance(head, (SubjectPath, RelationChain)):
        head, count = _qualify(head, unresolved, property_owners, accesses)
    steps: list[PathStep] = []
    bound_properties: frozenset[str] = frozenset()
    index = 0
    while index < len(expression.steps):
        step = expression.steps[index]
        if (step.operator == "/" and isinstance(step.operand, Name)
                and index + 1 < len(expression.steps)
                and expression.steps[index + 1].operator == ":"
                and isinstance(expression.steps[index + 1].operand, ValueLiteral)):
            value = expression.steps[index + 1]
            bearer = render_subject(replace(expression, head=head, steps=tuple(steps), value_format=None, value_cardinality=None))
            bound_properties = bound_properties or property_owners.get(bearer, frozenset())
            if step.operand.value in bound_properties:
                relative = SubjectPath(step.operand, (value,), None, None, step.span)
                steps.append(replace(step, operand=Qualification(relative, step.span)))
                index += 2
                count += 1
                continue
            unresolved.append(step.operand.value)
        if step.operator == "/" and isinstance(step.operand, Name) and step.operand.value in PROPERTY_NAMES:
            bearer = render_subject(replace(expression, head=head, steps=tuple(steps), value_format=None, value_cardinality=None))
            if step.operand.value in (bound_properties or property_owners.get(bearer, frozenset())):
                steps.append(replace(step, operator="."))
                accesses[0] += 1
                bound_properties = frozenset()
                index += 1
                continue
        if isinstance(step.operand, (SubjectPath, RelationChain)):
            operand, changes = _qualify(step.operand, unresolved, property_owners, accesses)
            step = replace(step, operand=operand)
            count += changes
        steps.append(step)
        bound_properties = frozenset()
        index += 1
    return replace(expression, head=head, steps=tuple(steps)), count


def convert_subject(text: str, *, property_owners: dict[str, frozenset[str]] | None = None) -> dict[str, Any]:
    """Convert only established tokens; uncertain Property ownership blocks patching."""
    try:
        tokenized, containment_count = _containment(text)
        parsed = parse_subject_expression(tokenized)
        unresolved: list[str] = []
        accesses = [0]
        expression, qualifier_count = _qualify(parsed.expression, unresolved, property_owners or {}, accesses)
        after = render_subject(expression)
        if render_subject(parse_subject_expression(after)) != after:
            raise ValueError("rendering is not idempotent")
    except (SubjectNotationError, ValueError) as error:
        return {"before": text, "state": "review-needed", "reason": str(error)}
    if unresolved:
        return {"before": text, "state": "unresolved-qualifier", "properties": sorted(set(unresolved)), "candidate": after}
    changed = bool(containment_count or qualifier_count or accesses[0])
    return {"before": text, "after": after if changed else text, "state": "safe" if changed else "unchanged",
            "containment_tokens": containment_count, "property_qualifiers": qualifier_count, "property_accesses": accesses[0],
            "classification": "syntax-preserving candidate; no canonical Entity or fact admission",
            "semantics": "Containment keeps written Whole-to-Part orientation; old postfix count moves to source/forward slot; reverse slot remains unspecified. Property predicates qualify the complete accumulated bearer."}


def prepare_manifest(repository: Path, frontier_path: Path) -> dict[str, Any]:
    repository = repository.resolve()
    frontier_raw = frontier_path.read_bytes()
    frontier = json.loads(frontier_raw)
    parser_digest = digest((TOOLS / "subject_notation.py").read_bytes())
    converter_digest = digest(Path(__file__).read_bytes())
    control = repository / ".caprmedio_caprmedio"
    targets: set[Path] = set()
    for relative in frontier["roots"]:
        path = Path(relative)
        if path.is_absolute() or ".." in path.parts:
            raise ValueError("frontier root must be relative to the control root")
        root = control / path
        if not root.is_dir() or root.is_symlink():
            raise ValueError("frontier root unavailable or symlinked: " + relative)
        for source in root.rglob("*.md"):
            if not any(part.casefold() in PRUNED for part in source.relative_to(root).parts[:-1]):
                if source.is_symlink() or source.resolve() != source:
                    raise ValueError("symlinked carrier frontier")
                targets.add(source)
    subjects, bodies, payload, blockers, pins = [], [], [], [], []
    frontier_pins, excluded, parsed_sources = [], [], []
    for path in sorted(targets):
        raw = path.read_bytes()
        relative = path.relative_to(repository).as_posix()
        frontier_pins.append({"path": relative, "sha256": digest(raw)})
        try:
            parsed = parse_carrier(raw, path)
        except CarrierError as error:
            excluded.append({"path": relative, "reason": error.code})
            continue
        parsed_sources.append((path, raw, parsed))
    declarations = {entry.metadata.get("subjects", {}).get("governs")
                    for _, _, entry in parsed_sources if isinstance(entry.metadata.get("subjects"), dict)
                    and isinstance(entry.metadata["subjects"].get("governs"), str)
                    and _current(entry.metadata)}
    atom_owners = frozenset(owner for owner in ATOM_OWNERS if owner in declarations)
    # R1931 independently uses bare Atom selectors as the historical form.
    if any(entry.metadata.get("atom_id") == "CA-R-1931" and "Atom/Content Role:" in entry.body
           for _, _, entry in parsed_sources):
        atom_owners = atom_owners | {"Atom"}
    owner_evidence = [{"path": path.relative_to(repository).as_posix(), "sha256": digest(raw),
                       "atom_id": entry.metadata.get("atom_id"), "governs": entry.metadata.get("subjects", {}).get("governs")}
                      for path, raw, entry in parsed_sources
                      if isinstance(entry.metadata.get("subjects"), dict)
                      and (isinstance(entry.metadata["subjects"].get("governs"), str) and entry.metadata["subjects"].get("governs") in atom_owners
                           or entry.metadata.get("atom_id") == "CA-R-1931")
                      and _current(entry.metadata)]
    property_authorities = [{"path": path.relative_to(repository).as_posix(), "sha256": digest(raw), "atom_id": entry.metadata.get("atom_id"), "version": entry.metadata.get("version")}
                            for path, raw, entry in parsed_sources
                            if entry.metadata.get("atom_id") in REVIEWED_PROPERTY_SOURCES and _current(entry.metadata)]
    checked_authorities = {entry["atom_id"] for entry in property_authorities
                           if (entry["version"], entry["sha256"]) == REVIEWED_PROPERTY_SOURCES[entry["atom_id"]]}
    property_owners: dict[str, frozenset[str]] = {}
    if {"CA-R-1531", "CA-R-1284", "CA-D-478"} <= checked_authorities and atom_owners:
        atom_owners = ATOM_OWNERS
        property_owners.update({owner: PROPERTY_NAMES for owner in atom_owners})
    if {"CA-R-1284", "CA-R-2397"} <= checked_authorities:
        property_owners.update({owner: frozenset({"Type"}) for owner in (
            "Entity/Object/Continuant/Projection", "Subject/CAPRMEDIO/Graph/Node/Project Model/Projection")})
    if {"CA-R-1284", "CA-R-1758"} <= checked_authorities:
        property_owners["Entity/Object/Continuant/Structural Unit/Scope Unit"] = frozenset({"Type"})
    active = 0
    statuses: dict[str, int] = {}
    obsolete_roots = []
    for path, raw, parsed in parsed_sources:
        metadata = parsed.metadata
        if not _current(metadata) or "projection" in metadata:
            excluded.append({"path": path.relative_to(repository).as_posix(), "reason": "non-Current or unrecognized status", "status": metadata.get("status")})
            continue
        statuses[metadata["status"]] = statuses.get(metadata["status"], 0) + 1
        active += 1
        relative = path.relative_to(repository).as_posix()
        pin = {"path": relative, "sha256": digest(raw), "atom_id": metadata.get("atom_id"), "version": metadata.get("version")}
        pins.append(pin)
        values = metadata.get("subjects", {})
        if not isinstance(values, dict):
            blockers.append({**pin, "reason": "non-mapping subjects"})
            continue
        patches = []
        old_approved = True
        for field, collection in (("governs", [values.get("governs")]), ("depends_on", values.get("depends_on", []))):
            if not isinstance(collection, list):
                blockers.append({**pin, "field": field, "reason": "non-scalar dependency collection"})
                continue
            for index, value in enumerate(collection):
                if not isinstance(value, str):
                    blockers.append({**pin, "field": field, "reason": "non-string subject"})
                    continue
                try:
                    parse_subject_expression(value)
                except SubjectNotationError:
                    old_approved = False
                converted = convert_subject(value, property_owners=property_owners)
                if value.startswith("Subject/"):
                    obsolete_roots.append({**pin, "field": field, "index": index if field == "depends_on" else None, "before": value, "reason": "obsolete root spelling retained; any taxonomy/root migration needs separate reviewed identity mapping"})
                if converted["state"] == "unchanged":
                    continue
                subjects.append({**pin, "field": field, "index": index if field == "depends_on" else None, **converted})
                if converted["state"] == "safe":
                    patches.append({"field": field, "old": value, "new": converted["after"], **({"index": index} if field == "depends_on" else {})})
        if patches:
            payload.append({"selector": relative, "expected": {key: pin[key] for key in ("atom_id", "version", "sha256")}, "subject_patches": patches})
            if not old_approved:
                blockers.append({**pin, "reason": "approved whole-carrier preview rejects existing old syntax before patching; requires reviewed migration admission, never legacy fallback"})
        body_start = parsed.text.find(parsed.body)
        offset = parsed.text[:body_start].count("\n")
        formal = False
        for line_number, line in enumerate(parsed.body.splitlines(), offset + 1):
            if re.match(r"^#{1,6}\s+", line):
                formal = "formal claim" in line.casefold()
            if CANDIDATE.search(line):
                bodies.append({**pin, "line": line_number, "text": line, "state": "review-needed", "position": "formal-claim" if formal else "body", "reason": "not a parsed whole Subject scalar; prose, examples, literals and operative claims need source-position review"})
    manifest = {"kind": "current_notation_adoption_dry_run", "writes_current": False, "entity_admission": "not_performed",
                "frontier": {"path": str(frontier_path.resolve()), "sha256": digest(frontier_raw)},
                "converter_sha256": converter_digest,
                "parser_sha256": parser_digest,
                "coverage": {"markdown_frontier": len(targets), "current_carriers": active, "statuses": statuses, "excluded_or_unrecognized": len(excluded), "safe_subject_occurrences": sum(row["state"] == "safe" for row in subjects), "unresolved_qualifiers": sum(row["state"] == "unresolved-qualifier" for row in subjects), "subject_review_needed": sum(row["state"] == "review-needed" for row in subjects), "property_predicate_rewrites": sum(row.get("property_qualifiers", 0) for row in subjects if row["state"] == "safe"), "property_access_rewrites": sum(row.get("property_accesses", 0) for row in subjects if row["state"] == "safe"), "containment_rewrites": sum(row.get("containment_tokens", 0) for row in subjects if row["state"] == "safe"), "body_candidates": len(bodies), "patch_carriers": len(payload)},
                "frontier_pins": frontier_pins, "source_pins": pins, "excluded": excluded, "established_atom_owners": sorted(atom_owners), "owner_evidence": owner_evidence, "property_authorities": property_authorities, "checked_property_authorities": sorted(checked_authorities), "property_owners": {key: sorted(value) for key, value in sorted(property_owners.items())}, "typed_property_declaration_completeness": {"Projection.Type": "Current R2397 Entity Definition bound" if {"CA-R-1284", "CA-R-2397"} <= checked_authorities else "unresolved: reviewed authority pins unavailable", "Scope Unit.Type": "Current R1758 admission/constraint bound; no standalone typed Property Entity Definition established; full adoption completeness remains separate" if {"CA-R-1284", "CA-R-1758"} <= checked_authorities else "unresolved: reviewed authority pins unavailable"}, "obsolete_root_concerns": obsolete_roots, "subjects": subjects, "body_candidates": bodies, "preview_blockers": blockers,
                "subject_patch_payload": payload, "preview_api": "atom_subject_patch.preview_subject_patches(repository, subject_patch_payload, subject_profile='approved')"}
    if (frontier_path.read_bytes() != frontier_raw or digest((TOOLS / "subject_notation.py").read_bytes()) != parser_digest
            or digest(Path(__file__).read_bytes()) != converter_digest):
        raise ValueError("frontier or parser changed while preparing dry-run")
    current_targets = {source for relative in frontier["roots"] for source in (control / relative).rglob("*.md")
                       if not any(part.casefold() in PRUNED for part in source.relative_to(control / relative).parts[:-1])}
    if current_targets != targets:
        raise ValueError("carrier frontier changed while preparing dry-run")
    for pin in frontier_pins:
        if digest((repository / pin["path"]).read_bytes()) != pin["sha256"]:
            raise ValueError("carrier changed while preparing dry-run: " + pin["path"])
    return manifest


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repository", type=Path, required=True)
    parser.add_argument("--frontier", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    manifest = prepare_manifest(args.repository, args.frontier)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps(manifest["coverage"], sort_keys=True))


if __name__ == "__main__":
    main()
