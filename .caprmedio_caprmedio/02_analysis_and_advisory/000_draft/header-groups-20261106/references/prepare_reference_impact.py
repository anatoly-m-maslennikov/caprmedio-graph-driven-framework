#!/usr/bin/env python3
"""Prepare, but never apply, the Header-group reference migration."""
import hashlib
import json
import re
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[5]
PLAN = ROOT / ".caprmedio_caprmedio/02_analysis/draft/header-groups-20261106"
SNAPSHOT = PLAN / "native-snapshot.json"
OUT = Path(__file__).with_name("impact.json")
RESIDUAL_REVIEW = Path(__file__).with_name("residual-review.json")

COMMON = {
    "Carrier Destination": "Destination",
    "CarrierDestination": "Destination",
    "Updated At": "State.Updated At",
    "UpdatedAt": "State.UpdatedAt",
    "Ref ID": "Identity.Ref ID",
    "RefID": "Identity.RefID",
    "Container": "Context.Container",
    "Topics": "Context.Topics",
    "Subjects.Active": "Context.Topics.Main Subject",
    "Subjects.Passive": "Context.Topics.Dependencies",
    "Subjects": "Context.Topics",
    "Status": "State.Status",
    "Version": "State.Version",
    "Label": "Context.Label",
    "Tier": "Context.Tier",
    "Role": "Context.Role",
    "Form": "Context.Form",
    "ID": "Identity.ID",
}
ROLE_FIELDS = {
    "Concern": {"Priority"},
    "Plan": {
        "Work Sequence Number",
        "WorkSequenceNumber",
        "AI Agent Confidence Threshold",
        "AIAgentConfidenceThreshold",
    },
}
ALL_FIELDS = tuple(sorted((*COMMON, *(x for v in ROLE_FIELDS.values() for x in v)), key=len, reverse=True))
FIELD = "|".join(re.escape(x) for x in ALL_FIELDS)
BARE_COMMON_FIELDS = tuple(field for field in COMMON if not field.startswith("Subjects"))
BARE_COMMON_FIELD = "|".join(re.escape(x) for x in sorted(BARE_COMMON_FIELDS, key=len, reverse=True))
SPECIAL_FIELD = "|".join(
    re.escape(x) for x in sorted((x for v in ROLE_FIELDS.values() for x in v), key=len, reverse=True)
)
DIRECT_ATOM = re.compile(rf"(?<![A-Za-z0-9_$.])Atom\.Header\.(?P<field>{FIELD})\b")
DIRECT_VAR = re.compile(rf"(?P<var>\$[A-Za-z_][A-Za-z0-9_]*)\.Header\.(?P<field>{FIELD})\b")
DIRECT_ROLE = re.compile(rf"(?P<role>Concern|Plan)\.Header\.(?P<field>{SPECIAL_FIELD})\b")
RELATIVE = re.compile(rf"(?<![A-Za-z0-9_$.])\.Header\.(?P<field>{FIELD})\b")
ROLE_QUALIFIED = re.compile(rf"(?P<role>Concern|Plan)/\(\.Header\.(?P<field>{SPECIAL_FIELD})\b")
ATOM_CONTEXT = re.compile(r"(?<![A-Za-z0-9_])Atom/(?:/|\()|<Atom>")
ATOM_ROLE = re.compile(
    r"Atom/(?:/)?\(\.Header(?:\.Context)?\.Role\s*(?::=|:|=)\s*(?P<role>Concern|Plan)\s*\)"
)
ATOM_BINDING = re.compile(
    r"(?P<root>Atom|Concern|Plan)(?:/\(\.Header(?:\.Context)?\.Role\s*(?::=|:|=)\s*(?P<role>Concern|Plan)\s*\))?//(?P<var>\$[A-Za-z_][A-Za-z0-9_]*)"
)
TYPED_ATOM = re.compile(r"(?P<var>\$[A-Za-z_][A-Za-z0-9_]*)\s*\[\s*<Atom>\s*\]")
SUMMARY = re.compile(r"(?m)^## Summary\s*$")
E240_BARE = re.compile(r"(?<![A-Za-z0-9_.])Header\.(?P<field>Subjects\.Active)\b")
BARE_COMMON = re.compile(rf"(?<![A-Za-z0-9_$.])Header\.(?P<field>{BARE_COMMON_FIELD})\b")
BARE_COMMON_PATHS = frozenset(row[0] for row in json.loads(RESIDUAL_REVIEW.read_text()))
E240_PATHS = frozenset(
    {
        ".caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/06_evaluation/CA-E-240-CORE_META_MODEL-EVAL_CASE--validate-atom-scope-and-claim-scope.md",
        ".caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/06_evaluation/draft/CA-E-240@50-draft-CORE_META_MODEL-EVAL_CASE--validate-atom-scope-and-claim-scope.md",
    }
)


def sha256(text):
    return hashlib.sha256(text.encode()).hexdigest()


def protected_summary_spans(text):
    spans = []
    for match in SUMMARY.finditer(text):
        next_heading = re.search(r"(?m)^## (?!#)", text[match.end() :])
        spans.append((match.start(), match.end() + next_heading.start() if next_heading else len(text)))
    return spans


def in_spans(position, spans):
    return any(start <= position < end for start, end in spans)


def summary_texts(text):
    return [text[start:end] for start, end in protected_summary_spans(text)]


def frontmatter(text):
    if not text.startswith("---\n"):
        return ""
    end = text.find("\n---\n", 4)
    return text[: end + 5] if end >= 0 else ""


def protected_metadata(text):
    header = frontmatter(text)
    fields = re.findall(r"(?m)^(?:atom_id|ref_id|status|version|updated_at):[^\n]*$", header)
    relations = re.search(r"(?ms)^relations:\n(?:^[ \t].*(?:\n|$))*", header)
    return fields, relations.group(0) if relations else ""


def atom_bindings(text):
    """Return Atom variables and their proven role, if the source binds one."""
    bindings = {}
    for match in ATOM_BINDING.finditer(text):
        bindings[match.group("var")] = match.group("role") or (
            match.group("root") if match.group("root") in ROLE_FIELDS else None
        )
    for match in TYPED_ATOM.finditer(text):
        bindings.setdefault(match.group("var"), None)
    return bindings


def replacement(field, role=None):
    if field in COMMON:
        return COMMON[field]
    if role in ROLE_FIELDS and field in ROLE_FIELDS[role]:
        return f"Context.{role}.{field}"
    return None


def migrate(text, path=None):
    """Return proposed text, replacement counts, actual holds, and skipped refs."""
    counts = Counter()
    holds = []
    bindings = atom_bindings(text)
    summary_skips = 0

    def replace_match(pattern, source, make_replacement, kind):
        nonlocal summary_skips
        chunks = []
        last = 0
        source_protected = protected_summary_spans(source)
        for match in pattern.finditer(source):
            chunks.append(source[last : match.start()])
            if in_spans(match.start(), source_protected):
                chunks.append(match.group(0))
                summary_skips += 1
            else:
                new = make_replacement(match)
                if new is None:
                    chunks.append(match.group(0))
                else:
                    chunks.append(new)
                    counts[kind] += 1
                    counts[match.group("field")] += 1
            last = match.end()
        chunks.append(source[last:])
        return "".join(chunks)

    # Atom.Header.* is an Atom reference. Special role leaves are held below
    # unless the source gives an approved, proven Concern or Plan role.
    def direct_atom(match):
        mapped = replacement(match.group("field"))
        return f"Atom.Header.{mapped}" if mapped else None

    result = replace_match(DIRECT_ATOM, text, direct_atom, "direct_atom")

    # A variable is an Atom only when the source explicitly binds it as one.
    def direct_var(match):
        role = bindings.get(match.group("var"))
        if match.group("var") not in bindings:
            return None
        mapped = replacement(match.group("field"), role)
        return f"{match.group('var')}.Header.{mapped}" if mapped else None

    result = replace_match(DIRECT_VAR, result, direct_var, "typed_atom")

    # Existing role-root declarations are the authoritative contracts.
    def direct_role(match):
        mapped = replacement(match.group("field"), match.group("role"))
        return f"{match.group('role')}.Header.{mapped}" if mapped else None

    result = replace_match(DIRECT_ROLE, result, direct_role, "role_root")

    def role_qualified(match):
        mapped = replacement(match.group("field"), match.group("role"))
        return f"{match.group('role')}/(.Header.{mapped}" if mapped else None

    result = replace_match(ROLE_QUALIFIED, result, role_qualified, "role_qualified")

    # Relative .Header.X belongs to Atom only in a CFEL statement chained from
    # Atom. This handles both Atom/(...) and Atom/(...)/(.Header.Form ...).
    pieces = []
    offset = 0
    for statement in re.split(r"(;)", result):
        statement_start = offset
        offset += len(statement)
        if statement == ";" or not ATOM_CONTEXT.search(statement):
            pieces.append(statement)
            continue
        role_match = ATOM_ROLE.search(statement)
        role = role_match.group("role") if role_match else None

        def qualified(match):
            absolute = statement_start + match.start()
            if in_spans(absolute, protected_summary_spans(result)):
                return match.group(0)
            mapped = replacement(match.group("field"), role)
            if mapped is None:
                return match.group(0)
            counts["qualified_atom"] += 1
            counts[match.group("field")] += 1
            return f".Header.{mapped}"

        pieces.append(RELATIVE.sub(qualified, statement))
    result = "".join(pieces)

    # E240's prose claim is an explicit Atom claim despite omitting `Atom.`;
    # no other bare Header owner is inferred from text alone.
    if path in E240_PATHS:
        result = replace_match(
            E240_BARE,
            result,
            lambda match: "Header.Context.Topics.Main Subject",
            "known_e240_bare_atom",
        )

    # These paths were individually reviewed as Atom Header prose/plan claims.
    # Keep the path gate so generic Entity.Header.* references cannot move.
    if path in BARE_COMMON_PATHS:
        result = replace_match(
            BARE_COMMON,
            result,
            lambda match: f"Header.{replacement(match.group('field'))}",
            "known_reviewed_bare_atom",
        )

    # These holds have real source snippets: unproven variables and unsupported
    # role-specific properties are intentionally not guessed.
    def add_hold(match, reason):
        if in_spans(match.start(), protected_summary_spans(result)):
            return
        line_start = result.rfind("\n", 0, match.start()) + 1
        line_end = result.find("\n", match.end())
        holds.append(
            {
                "token": match.group(0),
                "reason": reason,
                "snippet": result[line_start : len(result) if line_end < 0 else line_end].strip(),
            }
        )

    for match in DIRECT_ATOM.finditer(result):
        if match.group("field") not in COMMON:
            add_hold(match, "role_specific_atom_header_has_no_proven_role")
    for match in DIRECT_VAR.finditer(result):
        field = match.group("field")
        role = bindings.get(match.group("var"))
        if match.group("var") not in bindings:
            add_hold(match, "variable_is_not_proven_Atom")
        elif field not in COMMON and replacement(field, role) is None:
            add_hold(match, "role_specific_atom_header_has_no_proven_matching_role")
    for match in DIRECT_ROLE.finditer(result):
        add_hold(match, "role_property_is_not_an_approved_existing_contract")
    for match in ROLE_QUALIFIED.finditer(result):
        add_hold(match, "role_property_is_not_an_approved_existing_contract")

    return result, counts, holds, summary_skips


def transform(text, path=None):
    """Pure, idempotent full-carrier transform; path enables only known E240 prose."""
    return migrate(text, path)[0]


def rewrite(path, text):
    """Composer interface: use the full carrier path and full carrier text."""
    return transform(text, path)


def self_check():
    assert replacement("Ref ID") == "Identity.Ref ID"
    assert replacement("RefID") == "Identity.RefID"
    assert replacement("Updated At") == "State.Updated At"
    assert replacement("UpdatedAt") == "State.UpdatedAt"
    assert replacement("Subjects") == "Context.Topics"
    assert replacement("Subjects.Active") == "Context.Topics.Main Subject"
    assert replacement("Subjects.Passive") == "Context.Topics.Dependencies"
    assert replacement("Priority", "Concern") == "Context.Concern.Priority"
    assert replacement("Priority", "Plan") is None
    text = "Atom/(.Header.Role: Plan)/(.Header.Form: X);"
    after, _, holds, _ = migrate(text)
    assert after == "Atom/(.Header.Context.Role: Plan)/(.Header.Context.Form: X);" and not holds
    typed = "Atom/(.Header.Role: Plan)//$atom; $atom.Header.Work Sequence Number"
    after, _, holds, _ = migrate(typed)
    assert "$atom.Header.Context.Plan.Work Sequence Number" in after and not holds
    assert transform(after) == after
    role, _, holds, _ = migrate("Atom/(.Header.Role: Concern).Header.Priority;")
    assert role == "Atom/(.Header.Context.Role: Concern).Header.Context.Concern.Priority;" and not holds
    relative, _, holds, _ = migrate("UNIQUE(Atom//$atom, (.Header.ID, .Header.Version));")
    assert "(.Header.Identity.ID, .Header.State.Version)" in relative and not holds
    subject, _, holds, _ = migrate("Atom//$atom; $atom.Header.Subjects.Passive")
    assert "$atom.Header.Context.Topics.Dependencies" in subject and not holds
    bare = "Header.Subjects.Active"
    assert transform(bare) == bare
    assert rewrite(next(iter(E240_PATHS)), bare) == "Header.Context.Topics.Main Subject"
    reviewed_path = next(iter(BARE_COMMON_PATHS))
    assert rewrite(reviewed_path, "Header.Container") == "Header.Context.Container"
    assert rewrite(reviewed_path, "Entity.Header.ID") == "Entity.Header.ID"
    assert transform("Header.Container") == "Header.Container"
    sql_columns = "header_context_plan header_context_plan_work_sequence_number"
    assert transform(sql_columns) == sql_columns
    unchanged, _, holds, _ = migrate("Atom.Header.Context.Role Entity.Header.ID Entity.Header.Status")
    assert unchanged == "Atom.Header.Context.Role Entity.Header.ID Entity.Header.Status" and not holds


def main():
    self_check()
    snapshot = json.loads(SNAPSHOT.read_text())
    carriers = snapshot["carriers"]
    expected_count = snapshot["expected_count"]
    baseline_source_count = snapshot["baseline_source_count"]
    supplemental_sources = snapshot.get("supplemental_sources", [])
    assert len(carriers) == expected_count
    assert len({row["path"] for row in carriers}) == expected_count
    assert expected_count == baseline_source_count + len(supplemental_sources)
    assert {
        (row["path"], row["sha256"]) for row in supplemental_sources
    } <= {(row["path"], row["sha256"]) for row in carriers}
    operations = []
    holds = []
    counts = Counter(native_current_draft_carriers=len(carriers))
    snapshot_hash_mismatches = 0

    for row in carriers:
        path = row["path"]
        before = (ROOT / path).read_text()
        before_hash = sha256(before)
        if before_hash != row["sha256"]:
            snapshot_hash_mismatches += 1
        after, local_counts, local_holds, summary_skips = migrate(before, path)
        after_check, _, after_holds, _ = migrate(after, path)
        assert after_check == after and not after_holds
        assert summary_texts(before) == summary_texts(after)
        assert protected_metadata(before) == protected_metadata(after)
        counts.update(local_counts)
        counts["summary_references_skipped"] += summary_skips
        for hold in local_holds:
            holds.append({"path": path, **hold})
        if before != after:
            counts["idempotent_operations"] += 1
            operations.append(
                {
                    "path": path,
                    "before": before,
                    "after": after,
                    "before_sha256": before_hash,
                    "after_sha256": sha256(after),
                }
            )

    counts["operations"] = len(operations)
    counts["reference_spans"] = sum(counts[field] for field in ALL_FIELDS)
    counts["snapshot_hash_mismatches"] = snapshot_hash_mismatches
    counts["supplemental_sources"] = len(supplemental_sources)
    plan = {"operations": operations, "holds": holds, "counts": dict(sorted(counts.items()))}
    OUT.write_text(json.dumps(plan, indent=2) + "\n")
    print(json.dumps({"operations": len(operations), "holds": len(holds), "counts": plan["counts"]}, indent=2))


if __name__ == "__main__":
    main()
