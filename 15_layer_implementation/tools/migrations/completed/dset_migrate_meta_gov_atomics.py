#!/usr/bin/env python3
"""Historical, bounded replay tool for META/GOV atomic frontmatter migration.

Invocation: ``python dset_migrate_meta_gov_atomics.py [ROOT] (--check | --apply)``.
ROOT defaults to the repository containing this completed tool. The tool
classifies and normalizes only ``.dset/101_layer_meta`` and
``.dset/102_layer_gov``. ``--check`` validates without writing; ``--apply``
rechecks its manifest and rewrites atomic Markdown carriers. ``--expected-count``
defaults to 319 for exact replay. Ambiguity, parse failures, source changes, or
failed idempotency return non-zero; success returns 0. This is not an active CLI.
"""

from __future__ import annotations

import argparse
import hashlib
import re
import shutil
import subprocess
import sys
from pathlib import Path
from typing import Any

sys.dont_write_bytecode = True

REPO = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(REPO))
VOCAB = {
    "meta": {
        "artifact-model",
        "assurance",
        "authority",
        "external-boundary",
        "governance-surface",
        "interaction",
        "lifecycle",
        "profile",
        "scope",
        "self-hosting",
        "topology",
    },
    "gov": {
        "artifact-catalog",
        "assurance",
        "carrier-format",
        "external-boundary",
        "interaction",
        "layout",
        "lifecycle",
        "methodology",
        "priority",
        "provenance",
        "relation-model",
        "runtime",
        "settings",
        "subject-scope",
    },
}
KEY_ORDER = (
    "artifact_type",
    "artifact_subtype",
    "artifact_id",
    "scope_path",
    "subject_scopes",
    "priority",
    "llm_session_ids",
    "relation_kind",
    "endpoints",
    "relations",
)
SUBJECT_OVERRIDES = {
    **{
        f"DSET-REQUIREMENT-META-{k:03d}": v
        for k, v in {
            3: "profile",
            4: "lifecycle",
            5: "artifact-model",
            26: "authority",
            35: "artifact-model",
            38: "artifact-model",
            50: "profile",
            51: "artifact-model",
            55: "authority",
            59: "topology",
            66: "authority",
            9: "profile",
            10: "profile",
            12: "artifact-model",
            13: "artifact-model",
            14: "artifact-model",
            16: "artifact-model",
            18: "artifact-model",
            20: "governance-surface",
            22: "authority",
            27: "topology",
            32: "governance-surface",
            34: "authority",
            42: "governance-surface",
            43: "artifact-model",
            45: "artifact-model",
            46: "artifact-model",
        }.items()
    },
    **{
        f"DSET-QUESTION-META-{k:03d}": v
        for k, v in {1: "profile", 2: "profile", 3: "profile", 5: "scope"}.items()
    },
    "DSET-DECISION-GOV-004": "artifact-catalog",
    "DSET-REQUIREMENT-GOV-031": "layout",
    "DSET-REQUIREMENT-GOV-033": "relation-model",
    "DSET-REQUIREMENT-GOV-046": "layout",
    "DSET-REQUIREMENT-GOV-048": "lifecycle",
    "DSET-REQUIREMENT-GOV-050": "lifecycle",
    "DSET-DEFECT-GOV-002": "lifecycle",
    "DSET-DEFECT-GOV-003": "lifecycle",
    "DSET-GAP-GOV-001": "lifecycle",
    "DSET-PROBLEM-GOV-001": "artifact-catalog",
    "DSET-PROBLEM-GOV-004": "external-boundary",
    "DSET-OPPORTUNITY-GOV-001": "assurance",
    "DSET-QUESTION-GOV-001": "artifact-catalog",
    "DSET-QUESTION-GOV-003": "lifecycle",
    "DSET-QUESTION-GOV-006": "relation-model",
}

# These overrides are deliberately small and claim-specific.  They preserve the
# previously reviewed 46 assignments above and cover only titles where the
# deterministic title vocabulary would leave two equally plausible subjects.
TITLE_OVERRIDES = {
    "DSET-ANALYSIS-REPORT-003": ["artifact-model"],
    "DSET-ANALYSIS-REPORT-004": ["carrier-format"],
    "DSET-REQUIREMENT-META-028": ["authority"],
    "DSET-REQUIREMENT-META-029": ["profile"],
    "DSET-REQUIREMENT-META-065": ["topology"],
    "DSET-REQUIREMENT-META-067": ["topology"],
    "DSET-REQUIREMENT-META-069": ["artifact-model"],
    "DSET-REQUIREMENT-META-071": ["scope"],
    "DSET-REQUIREMENT-META-072": ["governance-surface"],
    "DSET-CONTRACT-META-001": ["scope"],
    "DSET-QUESTION-META-004": ["scope"],
    "DSET-QUESTION-META-005": ["scope"],
    "DSET-DECISION-GOV-027": ["carrier-format"],
    "DSET-DECISION-GOV-029": ["layout"],
    "DSET-DECISION-GOV-035": ["lifecycle"],
    "DSET-IMPL-GOV-004": ["relation-model"],
    "DSET-IMPL-GOV-005": ["methodology"],
    "DSET-IMPL-GOV-006": ["provenance"],
    "DSET-IMPL-GOV-008": ["artifact-catalog"],
    "DSET-REQUIREMENT-GOV-052": ["methodology"],
    "DSET-REQUIREMENT-GOV-057": ["external-boundary"],
    "DSET-REQUIREMENT-GOV-070": ["lifecycle"],
    "DSET-REQUIREMENT-GOV-078": ["artifact-catalog"],
    "DSET-REQUIREMENT-GOV-096": ["provenance"],
    "DSET-REQUIREMENT-GOV-098": ["interaction"],
    "DSET-REQUIREMENT-GOV-101": ["relation-model"],
    "DSET-REQUIREMENT-GOV-102": ["artifact-catalog"],
    "DSET-REQUIREMENT-GOV-103": ["provenance"],
    "DSET-REQUIREMENT-GOV-104": ["layout"],
    "DSET-REQUIREMENT-GOV-106": ["layout"],
    "DSET-REQUIREMENT-GOV-107": ["priority"],
    "DSET-REQUIREMENT-GOV-108": ["lifecycle"],
    "DSET-REQUIREMENT-GOV-109": ["interaction"],
    "DSET-REQUIREMENT-GOV-111": ["runtime"],
    "DSET-REQUIREMENT-GOV-112": ["lifecycle"],
    "DSET-REQUIREMENT-GOV-114": ["subject-scope"],
    "DSET-REQUIREMENT-GOV-116": ["carrier-format"],
    "DSET-REQUIREMENT-GOV-120": ["lifecycle"],
    "DSET-REQUIREMENT-GOV-121": ["artifact-catalog"],
    "DSET-REQUIREMENT-GOV-122": ["subject-scope"],
    "DSET-REQUIREMENT-GOV-123": ["carrier-format"],
    "DSET-REQUIREMENT-GOV-124": ["subject-scope"],
    "DSET-PROBLEM-GOV-009": ["artifact-catalog"],
    "DSET-PROBLEM-GOV-010": ["layout"],
    "DSET-PROBLEM-GOV-011": ["carrier-format"],
    "DSET-PROBLEM-GOV-012": ["artifact-catalog"],
    "DSET-QUESTION-GOV-015": ["external-boundary"],
    "DSET-QUESTION-GOV-016": ["provenance"],
    "DSET-QUESTION-GOV-017": ["artifact-catalog"],
    "DSET-REQUIREMENT-META-041": ["artifact-model"],
    "DSET-REQUIREMENT-META-070": ["artifact-model"],
    "DSET-REQUIREMENT-META-001": ["artifact-model"],
    "DSET-REQUIREMENT-META-008": ["external-boundary"],
    "DSET-REQUIREMENT-META-017": ["artifact-model"],
    "DSET-REQUIREMENT-META-039": ["artifact-model"],
    "DSET-REQUIREMENT-META-040": ["artifact-model"],
    "DSET-IMPL-GOV-001": ["methodology"],
    "DSET-IMPL-GOV-002": ["methodology"],
    "DSET-REQUIREMENT-GOV-105": ["subject-scope"],
    "DSET-REQUIREMENT-GOV-113": ["artifact-catalog"],
    "DSET-REQUIREMENT-GOV-115": ["settings"],
    "DSET-DECISION-GOV-001": ["provenance"],
    "DSET-DECISION-GOV-006": ["artifact-catalog"],
    "DSET-DECISION-GOV-007": ["artifact-catalog"],
    "DSET-DECISION-GOV-008": ["artifact-catalog"],
    "DSET-DECISION-GOV-009": ["artifact-catalog"],
    "DSET-DECISION-GOV-016": ["settings"],
    "DSET-DECISION-GOV-017": ["settings"],
    "DSET-DECISION-GOV-018": ["carrier-format"],
    "DSET-DECISION-GOV-022": ["methodology"],
    "DSET-DECISION-GOV-024": ["methodology"],
    "DSET-DECISION-GOV-030": ["methodology"],
    "DSET-DECISION-GOV-031": ["methodology"],
    "DSET-DECISION-GOV-032": ["artifact-catalog"],
    "DSET-REQUIREMENT-GOV-032": ["subject-scope"],
    "DSET-REQUIREMENT-GOV-044": ["layout"],
    "DSET-REQUIREMENT-GOV-045": ["layout"],
    "DSET-REQUIREMENT-GOV-049": ["settings"],
    "DSET-REQUIREMENT-GOV-054": ["artifact-catalog"],
    "DSET-REQUIREMENT-GOV-055": ["artifact-catalog"],
    "DSET-REQUIREMENT-GOV-064": ["artifact-catalog"],
    "DSET-REQUIREMENT-GOV-071": ["subject-scope"],
    "DSET-REQUIREMENT-GOV-072": ["lifecycle"],
    "DSET-REQUIREMENT-GOV-087": ["artifact-catalog"],
    "DSET-REQUIREMENT-GOV-089": ["artifact-catalog"],
    "DSET-REQUIREMENT-GOV-090": ["artifact-catalog"],
    "DSET-REQUIREMENT-GOV-091": ["artifact-catalog"],
    "DSET-REQUIREMENT-GOV-092": ["settings"],
    "DSET-REQUIREMENT-GOV-094": ["artifact-catalog"],
    "DSET-REQUIREMENT-GOV-117": ["assurance"],
    "DSET-DEFECT-GOV-006": ["assurance"],
    "DSET-DEFECT-GOV-007": ["provenance"],
    "DSET-PROBLEM-GOV-002": ["assurance"],
    "DSET-PROBLEM-GOV-003": ["assurance"],
    "DSET-QUESTION-GOV-013": ["artifact-catalog"],
    "DSET-QUESTION-GOV-005": ["lifecycle"],
    "DSET-QUESTION-GOV-008": ["artifact-catalog"],
    "DSET-QUESTION-GOV-009": ["artifact-catalog"],
    "DSET-QUESTION-GOV-011": ["artifact-catalog"],
    "DSET-REQUIREMENT-META-048": ["artifact-model"],
    "DSET-REQUIREMENT-META-053": ["governance-surface"],
    "DSET-REQUIREMENT-META-032": ["governance-surface"],
    "DSET-REQUIREMENT-GOV-077": ["artifact-catalog"],
    "DSET-DECISION-GOV-033": ["artifact-catalog"],
}

# Ordered only for terms that have one unambiguous primary meaning in a title.
# A title that matches multiple groups is rejected unless it has an override.
TITLE_RULES = (
    (
        "carrier-format",
        ("carrier", "toml", "yaml", "json", "frontmatter", "ndjson", "format"),
    ),
    ("external-boundary", ("external", "github-preview")),
    (
        "artifact-catalog",
        (
            "artifact-type",
            "artifact-types",
            "type-name",
            "type-prefix",
            "identity",
            "classification",
            "route-catalog",
            "semantic-route",
            "artifact-classes",
        ),
    ),
    (
        "relation-model",
        ("relation", "relations", "relational", "endpoint", "inheritance", "lineage"),
    ),
    ("subject-scope", ("subject-scope",)),
    ("provenance", ("provenance", "commit", "session", "archive-commit")),
    (
        "assurance",
        ("assurance", "test-and-evaluation", "test-evaluation", "verification"),
    ),
    (
        "lifecycle",
        (
            "lifecycle",
            "draft",
            "atomic-admission",
            "promotion",
            "immutability",
            "immutable",
            "reopen",
        ),
    ),
    ("methodology", ("methodology", "methodologies")),
    ("settings", ("settings", "setting", "config", "schema")),
    ("layout", ("layout", "folder", "directory", "root-directory", "control-plane")),
    ("runtime", ("runtime", "journal", "scratch", "log")),
    (
        "interaction",
        (
            "interaction",
            "exploration-mode",
            "input-routing",
            "question-input",
            "idea-input",
        ),
    ),
    ("authority", ("authority", "constitutional", "owner", "precedence")),
    ("topology", ("topology", "layer", "dependency", "handoff")),
    ("profile", ("profile", "python")),
    ("governance-surface", ("governance-surface", "governance-phase")),
    ("scope", ("scope", "work-area", "feature")),
    ("self-hosting", ("self-host", "recursive")),
    ("priority", ("priority", "importance")),
)


def raw_blocks(raw: str) -> dict[str, str]:
    lines = raw.splitlines(keepends=True)
    starts = [
        i
        for i, line in enumerate(lines)
        if line and not line[0].isspace() and re.match(r"^[A-Za-z0-9_-]+:", line)
    ]
    out: dict[str, str] = {}
    for n, start in enumerate(starts):
        end = starts[n + 1] if n + 1 < len(starts) else len(lines)
        key = lines[start].split(":", 1)[0].strip()
        out[key] = "".join(lines[start:end])
    return out


def title_subjects(path: Path, metadata: dict[str, Any], layer: str) -> list[str]:
    """Classify only the authored title/identity, never relation serialization."""
    aid = str(metadata["artifact_id"])
    if aid in SUBJECT_OVERRIDES:
        return [SUBJECT_OVERRIDES[aid]]
    if aid in TITLE_OVERRIDES:
        return TITLE_OVERRIDES[aid]
    # The title lives in the filename.  The declared Type/subtype is included
    # only as a narrow classifier for assurance and evidence carriers.
    title = path.stem.lower()
    declared = " ".join(
        str(metadata.get(key, "")).lower()
        for key in ("artifact_type", "artifact_subtype")
    )
    if "evidence_record" in declared:
        return []
    if any(
        token in declared
        for token in ("test_case", "evaluation_case", "test_plan", "evaluation_plan")
    ):
        return ["assurance"]
    candidates = [
        subject
        for subject, tokens in TITLE_RULES
        if subject in VOCAB[layer] and any(token in title for token in tokens)
    ]
    candidates = list(dict.fromkeys(candidates))
    if len(candidates) <= 1:
        return candidates
    # Multiple title concepts mean the primary claim needs a reviewed override.
    return []


def relation_targets(metadata: dict[str, Any], kinds: set[str]) -> list[str]:
    targets: list[str] = []
    for relation in metadata.get("relations", []) or []:
        if not isinstance(relation, dict) or str(relation.get("type", "")) not in kinds:
            continue
        raw = relation.get("targets", relation.get("target", []))
        if isinstance(raw, str):
            raw = [raw]
        targets.extend(str(item) for item in raw or [])
    return targets


def inherited_subject(
    record: dict[str, Any],
    direct_by_id: dict[str, list[str]],
    successor_by_id: dict[str, list[list[str]]],
) -> list[str]:
    """Use graph data only to inherit a subject from an authoritative target."""
    metadata = record["metadata"]
    declared = str(metadata.get("artifact_type", ""))
    if direct_by_id.get(str(metadata["artifact_id"])):
        return []
    # QA Cases check a named authority; its subject is the QA Case subject.
    if declared in {"test_case", "evaluation_case", "test_plan", "evaluation_plan"}:
        candidates = [
            direct_by_id.get(target, [])
            for target in relation_targets(metadata, {"check_of"})
        ]
        candidates = [candidate for candidate in candidates if candidate]
        if len(candidates) == 1:
            return candidates[0]
    # An archived predecessor often has no forward edge.  Invert current
    # replacement/child edges and inherit only when all successor subjects agree.
    if "archive" in record["path"].parts:
        candidates = successor_by_id.get(str(metadata["artifact_id"]), [])
        flattened = {item for candidate in candidates for item in candidate}
        if len(flattened) == 1:
            return sorted(flattened)
    return []


def inspect(layer: str, root: Path) -> tuple[list[dict[str, Any]], list[str]]:
    records, issues = _load_records(layer, root)
    direct_by_id, successor_by_id = _subject_maps(records, layer)
    _assign_subjects(records, direct_by_id, successor_by_id, issues)
    return records, issues


def _load_records(
    layer: str,
    root: Path,
) -> tuple[list[dict[str, Any]], list[str]]:
    records: list[dict[str, Any]] = []
    issues: list[str] = []
    for path in sorted(root.rglob("*.md")):
        text = path.read_text(encoding="utf-8")
        try:
            parsed = __import__("dset_toolchain.frontmatter", fromlist=["parse"]).parse(
                text
            )
        except Exception as exc:
            issues.append(f"{path}: parse error: {exc}")
            continue
        if not parsed or not parsed[0].get("artifact_id"):
            issues.append(f"{path}: ID-bearing Markdown required")
            continue
        metadata, body, fmt = parsed
        if fmt != "yaml":
            issues.append(f"{path}: YAML frontmatter required")
        raw = (
            text.split("---", 2)[1]
            if text.startswith("---") and text.count("---") >= 2
            else ""
        )
        records.append(
            {
                "path": path,
                "text": text,
                "metadata": metadata,
                "body": body,
                "raw": raw,
                "layer": layer,
            }
        )
    return records, issues


def _subject_maps(
    records: list[dict[str, Any]],
    layer: str,
) -> tuple[dict[str, list[str]], dict[str, list[list[str]]]]:
    direct_by_id = {
        str(record["metadata"]["artifact_id"]): title_subjects(
            record["path"], record["metadata"], layer
        )
        for record in records
    }
    successor_by_id: dict[str, list[list[str]]] = {}
    for record in records:
        subject = direct_by_id[str(record["metadata"]["artifact_id"])]
        if not subject:
            continue
        for target in relation_targets(record["metadata"], {"replacement_of"}):
            successor_by_id.setdefault(target, []).append(subject)
    return direct_by_id, successor_by_id


def _assign_subjects(
    records: list[dict[str, Any]],
    direct_by_id: dict[str, list[str]],
    successor_by_id: dict[str, list[list[str]]],
    issues: list[str],
) -> None:
    for r in records:
        m = r["metadata"]
        aid = str(m["artifact_id"])
        subjects = direct_by_id[aid]
        inherited = inherited_subject(r, direct_by_id, successor_by_id)
        if inherited:
            subjects = inherited
        typ = str(m.get("artifact_type", ""))
        if typ == "evidence_record":
            subjects = []  # evidence may omit scope entirely
        if not subjects and typ != "evidence_record":
            issues.append(f"{r['path']}: unresolved subject_scopes")
        if len(subjects) > 1 and typ not in {"analysis_report"}:
            issues.append(f"{r['path']}: ambiguous subject_scopes {subjects}")
        if any(s not in VOCAB[r["layer"]] for s in subjects):
            issues.append(f"{r['path']}: invalid subject scope {subjects}")
        r["subjects"] = subjects


def manifest(records: list[dict[str, Any]]) -> str:
    return "\n".join(
        f"{r['path']}\0{hashlib.sha256(r['text'].encode()).hexdigest()}"
        for r in records
    )


def _frontmatter_payload(text: str) -> str:
    lines = text.splitlines(keepends=True)
    if not lines or lines[0].strip() != "---":
        raise ValueError("YAML frontmatter opening delimiter is missing")
    for index, line in enumerate(lines[1:], start=1):
        if line.strip() == "---":
            return "".join(lines[1:index])
    raise ValueError("YAML frontmatter closing delimiter is missing")


def _relation_signature(metadata: dict[str, Any]) -> tuple[Any, Any, Any]:
    """Keep authored relation records and their endpoint-bearing fields intact."""
    return (
        metadata.get("relation_kind"),
        metadata.get("endpoints"),
        metadata.get("relations"),
    )


def _style_issues(payload: str) -> list[str]:
    issues: list[str] = []
    ambiguous = re.compile(
        r"^(?:|~|null|true|false|yes|no|on|off|"
        r"[-+]?\d+(?:\.\d+)?|\d{4}-\d{2}-\d{2})$",
        re.IGNORECASE,
    )
    for number, line in enumerate(payload.splitlines(), start=1):
        content = line.strip()
        if not content or content.startswith("#"):
            continue
        if '"' in content or "'" in content:
            issues.append(f"line {number}: quoted frontmatter scalar is forbidden")
        if re.search(r":\s*[\[{]", content):
            issues.append(f"line {number}: inline YAML collection is forbidden")
        if content.startswith("-") or ":" not in content:
            continue
        _, raw = content.split(":", 1)
        scalar = raw.strip()
        if scalar and not scalar.startswith(("-",)) and ambiguous.fullmatch(scalar):
            issues.append(f"line {number}: ambiguous plain scalar {scalar!r}")
    return issues


def _ruby_yaml_issues(payload: str) -> list[str]:
    ruby = shutil.which("ruby")
    if ruby is None:
        return []
    program = (
        "require 'yaml'; "
        "value = YAML.safe_load(STDIN.read, aliases: false); "
        "exit(value.is_a?(Hash) ? 0 : 1)"
    )
    completed = subprocess.run(
        [ruby, "-e", program],
        input=payload,
        text=True,
        capture_output=True,
        check=False,
    )
    if completed.returncode:
        detail = (completed.stderr or completed.stdout).strip().replace("\n", " ")
        return [f"Ruby YAML parse failed: {detail}"]
    return []


def validate_render(record: dict[str, Any], rendered: str) -> list[str]:
    """Verify a candidate rewrite without relying on one YAML implementation."""
    issues: list[str] = []
    try:
        parsed = __import__("dset_toolchain.frontmatter", fromlist=["parse"]).parse(
            rendered
        )
    except Exception as exc:
        return [f"DSET parser rejected rendered carrier: {exc}"]
    if not parsed:
        return ["DSET parser found no rendered carrier"]
    metadata, body, fmt = parsed
    if fmt != "yaml":
        issues.append("rendered carrier is not YAML")
    original = record["metadata"]
    if metadata.get("artifact_id") != original.get("artifact_id"):
        issues.append("artifact_id changed during render")
    if _relation_signature(metadata) != _relation_signature(original):
        issues.append("relations or endpoints changed during render")
    if not body.startswith(record["body"]):
        issues.append("original body is not the exact rendered body prefix")
    payload = _frontmatter_payload(rendered)
    issues.extend(_style_issues(payload))
    issues.extend(_ruby_yaml_issues(payload))
    extras = {
        key: value
        for key, value in raw_blocks(record["raw"]).items()
        if key not in set(KEY_ORDER)
    }
    if extras:
        expected = "".join(extras.values())
        marker = "## Historical frontmatter metadata\n\n```yaml\n" + expected + "```"
        if marker not in rendered:
            issues.append("removed frontmatter metadata was not retained byte-for-byte")
    return issues


def render(r: dict[str, Any]) -> str:
    from dset_toolchain.yaml_properties import dumps

    m = r["metadata"]
    out: dict[str, Any] = {}
    for key in KEY_ORDER:
        if key == "artifact_subtype" and key not in m:
            continue
        if key == "scope_path":
            out[key] = f"layer:{r['layer']}"
        elif key == "subject_scopes":
            if r["subjects"]:
                out[key] = r["subjects"]
        elif key in m:
            out[key] = m[key]
    known = set(KEY_ORDER)
    extras = {k: v for k, v in raw_blocks(r["raw"]).items() if k not in known}
    result = "---\n" + dumps(out) + "---\n" + r["body"]
    if extras:
        result += (
            "\n\n## Historical frontmatter metadata\n\n```yaml\n"
            + "".join(extras.values())
            + "```\n"
        )
    return result


def _arguments() -> argparse.Namespace:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("root", nargs="?", type=Path, default=REPO)
    ap.add_argument("--expected-count", type=int, default=319)
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--apply", action="store_true")
    args = ap.parse_args()
    if args.check == args.apply:
        ap.error("choose exactly one of --check or --apply")
    return args


def _roots(root: Path) -> tuple[tuple[str, Path], ...]:
    return (
        ("meta", root / ".dset/101_layer_meta"),
        ("gov", root / ".dset/102_layer_gov"),
    )


def _collect_records(
    roots: tuple[tuple[str, Path], ...],
) -> tuple[list[dict[str, Any]], list[str]]:
    all_records: list[dict[str, Any]] = []
    issues: list[str] = []
    for layer, root in roots:
        records, found = inspect(layer, root)
        all_records += records
        issues += found
    return all_records, issues


def _validation_issues(
    records: list[dict[str, Any]],
    issues: list[str],
    expected_count: int,
) -> list[str]:
    if len(records) != expected_count:
        issues.append(
            f"expected {expected_count} ID-bearing atoms, found {len(records)}"
        )
    for record in records:
        issues.extend(
            f"{record['path']}: {issue}"
            for issue in validate_render(record, render(record))
        )
    return issues


def _apply_records(
    roots: tuple[tuple[str, Path], ...],
    records: list[dict[str, Any]],
    before: str,
) -> int:
    fresh_records, fresh_issues = _collect_records(roots)
    if fresh_issues or manifest(fresh_records) != before:
        print("ERROR: source changed after preflight; rerun --check")
        return 3
    for record in records:
        record["path"].write_text(render(record), encoding="utf-8")
    return _verify_apply(roots, records, before)


def _verify_apply(
    roots: tuple[tuple[str, Path], ...],
    records: list[dict[str, Any]],
    before: str,
) -> int:
    check_records, check_issues = _collect_records(roots)
    if check_issues or len(check_records) != len(records):
        print("ERROR: post-apply inspection failed")
        return 3
    idempotency_issues = [
        str(record["path"])
        for record in check_records
        if render(record) != record["text"]
    ]
    if idempotency_issues:
        print("ERROR: apply is not idempotent:\n" + "\n".join(idempotency_issues))
        return 3
    changed = _changed_count(before, manifest(check_records))
    print(f"applied {len(records)} atoms; changed {changed}; idempotency OK")
    return 0


def _changed_count(before: str, after: str) -> int:
    return sum(
        before_line != after_line
        for before_line, after_line in zip(
            before.splitlines(),
            after.splitlines(),
            strict=False,
        )
    )


def main() -> int:
    """Run the bounded historical check or apply operation."""
    args = _arguments()
    roots = _roots(args.root)
    all_records, issues = _collect_records(roots)
    issues = _validation_issues(all_records, issues, args.expected_count)
    if issues:
        print("UNRESOLVED:")
        print("\n".join(issues))
        return 2
    before = manifest(all_records)
    if args.apply:
        return _apply_records(roots, all_records, before)
    else:
        manifest_digest = hashlib.sha256(before.encode()).hexdigest()
        print(f"check OK: {len(all_records)} atoms; manifest {manifest_digest}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
