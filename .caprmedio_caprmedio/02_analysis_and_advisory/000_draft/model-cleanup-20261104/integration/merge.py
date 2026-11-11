#!/usr/bin/env python3
"""Build hash-pinned, review-only merges of the MODEL cleanup previews."""
from __future__ import annotations

import difflib
import hashlib
import importlib.util
import json
from pathlib import Path
import re

HERE = Path(__file__).resolve().parent
PACKETS = HERE.parent
ROOT = HERE.parents[4]
OLD_ADOPT = ROOT / ".caprmedio_caprmedio/03_plan/CA-P-2694-EPIC--entity-graph-refactor-stage-4-polishing/model-header-content-20261103/integration/adopt.py"


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def _native_guard():
    spec = importlib.util.spec_from_file_location("model_cleanup_native_adopt", OLD_ADOPT)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load native guard: {OLD_ADOPT}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    module.ROOT = ROOT
    return module


def read_pinned(path: Path, expected_sha256: str) -> bytes:
    raw = path.read_bytes()
    if sha(raw) != expected_sha256:
        raise ValueError(f"stale source pin: {path}")
    return raw


def _candidate_path(value: str) -> Path:
    path = Path(value)
    path = path if path.is_absolute() else ROOT / path
    path = path.resolve()
    if not path.is_relative_to(PACKETS.resolve()):
        raise ValueError(f"candidate outside cleanup packets: {path}")
    return path


def _edits(before: str, after: str):
    matcher = difflib.SequenceMatcher(a=before, b=after, autojunk=False)
    return [
        {"start": i1, "end": i2, "before": before[i1:i2], "after": after[j1:j2]}
        for tag, i1, i2, j1, j2 in matcher.get_opcodes()
        if tag != "equal"
    ]


def _overlap(left, right) -> bool:
    a, b = left["start"], left["end"]
    c, d = right["start"], right["end"]
    if a == b and c == d:
        return a == c
    if a == b:
        return c <= a <= d
    if c == d:
        return a <= c <= b
    return max(a, c) < min(b, d)


def merge_text(before: str, proposals: list[tuple[str, str]]):
    """Apply candidate texts derived from one exact before; reject overlapping edits."""
    edits = []
    for lane, after in proposals:
        for edit in _edits(before, after):
            edit = {**edit, "lane": lane}
            duplicate = next((old for old in edits if all(old[k] == edit[k] for k in ("start", "end", "before", "after"))), None)
            if duplicate:
                continue
            for old in edits:
                if _overlap(old, edit):
                    raise ValueError(f"overlapping source edits: {old['lane']} and {lane}")
            edits.append(edit)
    merged = before
    for edit in sorted(edits, key=lambda x: (x["start"], x["end"]), reverse=True):
        if merged[edit["start"]:edit["end"]] != edit["before"]:
            raise ValueError(f"merge preimage mismatch: {edit['lane']}")
        merged = merged[:edit["start"]] + edit["after"] + merged[edit["end"]:]
    return merged, edits


def _source_row(item, lane):
    if lane == "syntax":
        return {"id": item["pin"].split("@")[0], "pin": item["pin"], "source": item["source"],
                "before_sha256": item["source_sha256"], "preview": item["candidate"],
                "preview_sha256": item["candidate_sha256"], "transform_kind": "subjects-only syntax"}
    if lane in {"legacy", "namespace"}:
        atom_id = item["atom_id"]
        kind = "passive Subject alias correction" if lane == "legacy" else "exact-key Subject namespace correction"
        notes = list(item.get("held_values", []))
        if lane == "namespace" and atom_id == "CA-E-672":
            notes.append("existing malformed Subjects mapping retained; candidate remains invalid")
        return {"id": atom_id, "pin": atom_id, "source": item["source_path"],
                "before_sha256": item["source_sha256"], "preview": item["preview_path"],
                "preview_sha256": item["preview_sha256"], "transform_kind": kind,
                "notes": notes,
                "warnings": [item["scope"]] if lane == "legacy" and item.get("scope") else []}
    if lane == "projection":
        return item
    return {"id": item["id"], "pin": item["id"], "source": item["source_path"],
            "before_sha256": item["source_sha256"], "preview": item["candidate_path"],
            "preview_sha256": item["candidate_sha256"], "transform_kind": "substantive Relation declaration correction"}


def _frontmatter_meta(text: str):
    match = re.match(r"\A---\n(.*?)\n---(?=\n)", text, re.S)
    if not match:
        raise ValueError("source has no frontmatter")
    meta = {}
    for key in ("atom_id", "version", "updated_at", "status", "role", "form"):
        found = re.search(rf"(?m)^{key}:\s*(.*?)\s*$", match.group(1))
        if found:
            meta[key] = found.group(1)
    return meta


def _load_inputs(native):
    syntax_packet = json.loads((PACKETS / "syntax/overrides/manifest.json").read_text())
    legacy_packet = json.loads((PACKETS / "legacy/preview-manifest.json").read_text())
    relation_packet = json.loads((PACKETS / "relations/manifest.json").read_text())
    namespace_packet = json.loads((PACKETS / "legacy/namespace-manifest.json").read_text())
    projection_packet = json.loads((PACKETS / "legacy/projection-manifest.json").read_text())
    triage_path = ROOT / namespace_packet["triage_path"]
    if sha(triage_path.read_bytes()) != namespace_packet["triage_sha256"]:
        raise ValueError("namespace triage pin drift")
    admitted_values = {"Catalog", "Map", "Hub"}
    for authority in projection_packet["authority"]:
        path = ROOT / authority["path"]
        raw = read_pinned(path, authority["sha256"]).decode("utf-8")
        if Path(authority["path"]).name.startswith("CA-R-2538"):
            for value in admitted_values:
                if f"Projection.Form: {value}" not in raw:
                    raise ValueError(f"R2538 no longer admits Projection.Form value: {value}")
    syntax = syntax_packet["candidates"]
    legacy = legacy_packet["previews"]
    namespace = namespace_packet["previews"]
    projection = []
    held_projection = []
    for item in projection_packet["previews"]:
        source_path = native.checked_path(item["source_path"])
        before = read_pinned(source_path, item["source_sha256"]).decode("utf-8")
        full_candidate = _candidate_path(item["preview_path"])
        candidate = read_pinned(full_candidate, item["preview_sha256"]).decode("utf-8")
        safe_edits, held_edits = [], []
        for edit in item["edits"]:
            value = _projection_form_value(edit["old"])
            generic_type = "Projection/Type" in edit["old"] and edit["new"].endswith("Projection.Form")
            if is_projection_form_edit(edit, admitted_values):
                safe_edits.append(edit)
            else:
                held_edits.append(edit)
        # Confirm every declared replacement appears in the pinned candidate's Subjects block.
        candidate_fm = re.match(r"\A---\n(.*?)\n---(?=\n)", candidate, re.S)
        candidate_subject = re.search(r"^subjects:\n(?P<body>(?:(?:[ \t]+.*|)\n)*)", candidate_fm.group(1), re.M) if candidate_fm else None
        if not candidate_subject or any(edit["new"] not in candidate_subject.group("body") for edit in item["edits"]):
            raise ValueError(f"projection candidate does not contain its pinned Subject edits: {item['atom_id']}")
        safe = _replace_subject_text(before, safe_edits) if safe_edits else before
        for edit in held_edits:
            held_projection.append({
                "id": item["atom_id"], "pin": f"{item['atom_id']}@{_frontmatter_meta(before).get('version', '?')}", "source": item["source_path"],
                "before_sha256": item["source_sha256"], "candidate_sha256": item["preview_sha256"],
                "transform": {"from": edit["old"], "to": edit["new"], "role": edit["role"]},
                "reason": "FORM_VS_NAMED_SELECTION",
            })
        if safe_edits:
            notes = (["FORM_VS_NAMED_SELECTION edits in this source are held"] if held_edits else [])
            projection.append({
                "id": item["atom_id"], "pin": f"{item['atom_id']}@{_frontmatter_meta(before).get('version', '?')}", "source": item["source_path"],
                "before_sha256": item["source_sha256"],
                "preview": item["preview_path"], "candidate_input_sha256": item["preview_sha256"],
                "preview_sha256": sha(safe.encode()), "transform_kind": "R2538-admitted Projection.Form selection",
                "notes": notes, "warnings": [], "_preview_text": safe,
                "candidate_input": item["preview_path"], "candidate_input_sha256": item["preview_sha256"],
            })
    relations = [item for item in relation_packet if "candidate_path" in item and item["id"] in {"CA-R-1199", "CA-R-1200"}]
    relation_hold = [item for item in relation_packet if item.get("id") == "CA-R-2469" and "candidate_path" in item]
    return (syntax, legacy, namespace, projection, len(projection_packet["previews"]), held_projection,
            relations, relation_hold, projection_packet["authority"])


def is_projection_form_edit(edit, admitted_values):
    value = _projection_form_value(edit["old"])
    generic_type = re.search(r"Projection/Type\s*$", edit["old"]) and edit["new"].endswith("Projection.Form")
    return bool(generic_type or value in admitted_values)


def _projection_form_value(text):
    match = re.search(r"Projection/(?:\(\.Form:|Type:)\s*([^,)]+)", text)
    return match.group(1).strip() if match else None


def _replace_subject_text(source, edits):
    match = re.match(r"\A---\n(.*?)\n---(?=\n)", source, re.S)
    if not match:
        raise ValueError("source has no frontmatter")
    front = match.group(1)
    subject = re.search(r"^subjects:\n(?P<body>(?:(?:[ \t]+.*|)\n)*)", front, re.M)
    if not subject:
        raise ValueError("source has no Subjects mapping")
    body = subject.group("body")
    for edit in edits:
        old, new = edit["old"], edit["new"]
        count = body.count(old)
        if not count:
            raise ValueError(f"projection edit preimage missing: {old}")
        body = body.replace(old, new)
    a, b = match.span(1)
    changed_front = front[:subject.start("body")] + body + front[subject.end("body"):]
    return source[:a] + changed_front + source[b:]


def build():
    native = _native_guard()
    (syntax, legacy, namespace, projection, projection_manifest_count, held_projection,
     relations, relation_hold, projection_authority_pins) = _load_inputs(native)
    inputs = []
    gated_ids = set()
    for lane, items in (("syntax", syntax), ("legacy", legacy), ("namespace", namespace),
                        ("projection", projection), ("relations", relations)):
        for item in items:
            row = _source_row(item, lane)
            # Use the existing adoption path guard for every canonical source.
            source_path = native.checked_path(row["source"])
            before = read_pinned(source_path, row["before_sha256"]).decode("utf-8")
            if lane == "projection":
                preview = row.pop("_preview_text")
            else:
                preview_path = _candidate_path(row["preview"])
                preview = read_pinned(preview_path, row["preview_sha256"]).decode("utf-8")
            if "@" not in row["pin"]:
                row["pin"] = f"{row['id']}@{_frontmatter_meta(before).get('version', '?')}"
            row["lane"] = lane
            row["_before"] = before
            row["_preview"] = preview
            row["gated"] = lane == "syntax" and row["id"] in gated_ids
            inputs.append(row)

    by_source = {}
    for row in inputs:
        key = row["source"]
        prior = by_source.get(key)
        if prior and prior["before_sha256"] != row["before_sha256"]:
            raise ValueError(f"overlapping sources do not share one pinned before: {key}")
        by_source.setdefault(key, {"before_sha256": row["before_sha256"], "rows": []})["rows"].append(row)

    outputs, held, pending = [], held_projection[:], []
    out_dirs = {"ready": HERE / "previews", "gated": HERE / "gated"}
    for source, group in sorted(by_source.items()):
        rows = group["rows"]
        if any(r["gated"] for r in rows):
            # Keep only approved source syntax edits; do not import the separate R2469 count proposal.
            syntax_rows = [r for r in rows if r["lane"] == "syntax"]
            if len(syntax_rows) != 1 or any(r["lane"] == "relations" for r in rows):
                raise ValueError(f"unexpected gated source proposals: {source}")
            before = syntax_rows[0]["_before"]
            after = syntax_rows[0]["_preview"]
            edits = _edits(before, after)
            row = syntax_rows[0]
            target = out_dirs["gated"] / f"{row['id']}@{row['pin'].split('@')[-1]}.txt"
            pending.append((target, after))
            outputs.append(_output_record(row, source, target, before, after, edits, "GATED_UNTIL_PARSER_PASS"))
            continue
        before = rows[0]["_before"]
        merged, edits = merge_text(before, [(r["lane"], r["_preview"]) for r in rows])
        if merged == before:
            raise ValueError(f"empty merged preview: {source}")
        # Mechanical syntax and alias changes retain carrier identity and all version metadata.
        before_meta, after_meta = _frontmatter_meta(before), _frontmatter_meta(merged)
        if before_meta != after_meta:
            raise ValueError(f"merge changed metadata: {source}")
        atom_id = _frontmatter_meta(before).get("atom_id")
        target = out_dirs["ready"] / f"{atom_id}.txt"
        pending.append((target, merged))
        status = ("REVISION_AND_EXACT_ARCHIVE_REQUIRED" if any(r["lane"] == "relations" for r in rows)
                  else "PARTIAL_FORM_VS_NAMED_SELECTION" if any(any("FORM_VS_NAMED_SELECTION" in note for note in r.get("notes", [])) for r in rows)
                  else "PARTIAL_UNRECOGNIZED_SUBJECTS_RETAINED" if any(r.get("notes") for r in rows)
                  else "READY_FOR_ROOT_REVIEW")
        outputs.append(_output_record(rows[0], source, target, before, merged, edits, status, rows))

    for item in relation_hold:
        source = native.checked_path(item["source_path"])
        meta = _frontmatter_meta(read_pinned(source, item["source_sha256"]).decode("utf-8"))
        held.append({"id": item["id"], "pin": f"{item['id']}@{meta.get('version', '?')}",
                     "source": item["source_path"], "before_sha256": item["source_sha256"],
                     "candidate_sha256": item["candidate_sha256"],
                     "transform": "additional outgoing count on HAS_ACTIVE_SUBJECT",
                     "reason": "semantic reconciliation required; do not merge or adopt"})
    # Write candidates only after every source pin and merge has passed preflight.
    expected = {target.resolve() for target, _ in pending}
    for folder in out_dirs.values():
        for stale in folder.glob("*.txt"):
            if stale.resolve() not in expected:
                stale.unlink()
    for target, payload in pending:
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(payload)
    plan = {
        "status": "PREPARED_FOR_REVIEW_ONLY",
        "native_workflow_admission": False,
        "journal_append": False,
        "input_counts": {"syntax": len(syntax), "legacy": len(legacy), "namespace": len(namespace),
                         "projection_manifest": projection_manifest_count, "projection_selected": len(projection), "relations": len(relations),
                         "parser_gate_passed": 2},
        "parser_gate": {"status": "PASSED_BY_ROOT", "pins": ["CA-R-2469@4", "CA-R-2470@2"]},
        "projection_authority_pins": projection_authority_pins,
        "output_count": len(outputs),
        "gated": [],
        "held": held,
        "outputs": outputs,
        "previews": outputs,
    }
    (HERE / "merge-plan.json").write_text(json.dumps(plan, indent=2, ensure_ascii=False) + "\n")
    return plan


def _output_record(seed, source, target, before, after, edits, status, rows=None):
    transforms = []
    for edit in edits:
        transforms.append({"lane": edit.get("lane", seed["lane"]), "source_span": [edit["start"], edit["end"]],
                           "before": edit["before"], "after": edit["after"]})
    contributors = rows or [seed]
    return {"id": seed["id"], "pin": seed["pin"], "source": source, "before_sha256": seed["before_sha256"],
            "candidate": target.relative_to(ROOT).as_posix(), "candidate_sha256": sha(after.encode()), "metadata_preserved": True,
            "status": status, "revision_policy": "same-ID revision and exact predecessor archive required later" if status == "REVISION_AND_EXACT_ARCHIVE_REQUIRED" else None,
            "contributors": [{"lane": row["lane"], "pin": row["pin"], "preview": row["preview"],
                              "preview_sha256": row["preview_sha256"], "transform_kind": row["transform_kind"],
                              "candidate_input_sha256": row.get("candidate_input_sha256"),
                              "notes": row.get("notes", []), "warnings": row.get("warnings", [])}
                             for row in contributors], "transforms": transforms}


if __name__ == "__main__":
    result = build()
    print(json.dumps({"outputs": result["output_count"], "gated": len(result["gated"]), "held": len(result["held"])}, indent=2))
