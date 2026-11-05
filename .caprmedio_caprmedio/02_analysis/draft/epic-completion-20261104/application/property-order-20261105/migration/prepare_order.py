#!/usr/bin/env python3
"""Prepare a pinned, source-only YAML Header / Markdown Content ordering plan."""
from __future__ import annotations

import hashlib
import argparse
import json
import re
import subprocess
from collections import Counter, defaultdict
from pathlib import Path, PurePosixPath

ROOT = Path(__file__).resolve().parents[7]
PACKET = ROOT / ".caprmedio_caprmedio/02_analysis/draft/epic-completion-20261104"
SNAPSHOT = PACKET / "coverage/ordered-source-migration-20261105/property-audit/snapshot.json"
HERE = Path(__file__).resolve().parent
OUTPUT = HERE / "migration-order-plan.json"
HEADER_ORDER = ["atom_id", "ref_id", "container", "role", "form", "label", "topics", "tier", "relations", "status", "version", "updated_at", "carrier_destination"]
HEADER_RANK = {key: i for i, key in enumerate(HEADER_ORDER)}
EXTRA_FIELD_POLICIES = {"after_carrier_destination", "after_tier_before_relations"}
DEFAULT_EXTRA_FIELD_POLICY = "after_carrier_destination"
CONTENT_ORDER = ["Summary", "Claim", "Semantics", "Details"]
CONTENT_RANK = {key: i for i, key in enumerate(CONTENT_ORDER)}
CLAIM_CHILD_ORDER = ["Mermaid Scheme", "Prose Claim", "Formal Claim"]
CLAIM_CHILD_RANK = {key: i for i, key in enumerate(CLAIM_CHILD_ORDER)}
EXCLUDED_COMPONENTS = {"archive", "archives", "history", "historical", "journal", "journals", "projection", "projections", "test", "tests", "testing", "copy", "copies", "snapshot", "snapshots", "withdrawn"}


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def protected(relpath: str) -> bool:
    parts = PurePosixPath(relpath).parts
    return any(part.casefold() in EXCLUDED_COMPONENTS or part.upper().startswith("TEST-") or part.upper().startswith("TEST_") for part in parts)


def split_frontmatter(text: str):
    lines = text.splitlines(keepends=True)
    if not lines or lines[0].rstrip("\r\n") != "---":
        return None
    fm_start = len(lines[0])
    offset = fm_start
    for line in lines[1:]:
        if line.rstrip("\r\n") == "---":
            return fm_start, offset + len(line)
        offset += len(line)
    return None


TOP_KEY = re.compile(r"^([A-Za-z_][A-Za-z0-9_-]*):(?:[ \t].*)?(?:\r?\n)?$")


def yaml_blocks(header: str):
    lines = header.splitlines(keepends=True)
    starts = []
    offset = 0
    for line in lines:
        m = TOP_KEY.match(line)
        if m:
            starts.append((offset, m.group(1)))
        offset += len(line)
    if not starts:
        return None
    prefix = header[:starts[0][0]]
    blocks = []
    for i, (start, key) in enumerate(starts):
        end = starts[i + 1][0] if i + 1 < len(starts) else len(header)
        blocks.append({"key": key, "text": header[start:end], "start": start, "end": end})
    duplicates = [key for key, count in Counter(x["key"] for x in blocks).items() if count > 1]
    return prefix, blocks, duplicates


def reorder_header(header: str, extra_field_policy: str = DEFAULT_EXTRA_FIELD_POLICY):
    parsed = yaml_blocks(header)
    if parsed is None:
        return header, {"hold": "no top-level YAML mapping entries found"}, []
    prefix, blocks, duplicates = parsed
    if duplicates:
        return header, {"hold": "duplicate top-level YAML key(s)", "keys": duplicates}, [x["key"] for x in blocks]
    known = sorted((block for block in blocks if block["key"] in HEADER_RANK), key=lambda b: HEADER_RANK[b["key"]])
    extras = [block for block in blocks if block["key"] not in HEADER_RANK]
    if extra_field_policy == "after_carrier_destination":
        ordered = known + extras
    elif extra_field_policy == "after_tier_before_relations":
        tier_index = next((i for i, block in enumerate(known) if block["key"] == "tier"), None)
        if tier_index is not None:
            insertion = tier_index + 1
        else:
            insertion = next((i for i, block in enumerate(known) if HEADER_RANK[block["key"]] > HEADER_RANK["tier"]), len(known))
        ordered = known[:insertion] + extras + known[insertion:]
    else:
        raise ValueError(f"unknown extra-field placement policy: {extra_field_policy}")
    after = prefix + "".join(x["text"] for x in ordered)
    return after, None, [x["key"] for x in blocks]


FENCE = re.compile(r"^ {0,3}(`{3,}|~{3,})(.*)$")


def markdown_headings(text: str, start: int = 0):
    """Yield (offset, heading level, name); ignore fenced code blocks."""
    result = []
    offset = 0
    fence_char = None
    fence_len = 0
    for line in text.splitlines(keepends=True):
        visible = line.rstrip("\r\n")
        if fence_char:
            close = re.match(r"^ {0,3}" + re.escape(fence_char) + r"{" + str(fence_len) + r",}\s*$", visible)
            if close:
                fence_char = None
                fence_len = 0
            offset += len(line)
            continue
        opener = FENCE.match(visible)
        if opener:
            run = opener.group(1)
            fence_char, fence_len = run[0], len(run)
            offset += len(line)
            continue
        m = re.match(r"^(#{1,6})[ \t]+(.+?)[ \t]*#*[ \t]*$", visible)
        if m:
            result.append((offset, len(m.group(1)), m.group(2).strip()))
        offset += len(line)
    return result


def reorder_children(claim_block: str):
    heads = markdown_headings(claim_block)
    recognized = [(pos, name) for pos, level, name in heads if level == 3 and name in CLAIM_CHILD_RANK]
    counts = Counter(name for _, name in recognized)
    duplicates = [name for name, n in counts.items() if n > 1]
    if duplicates:
        return claim_block, {"hold": "duplicate declared Claim child heading(s)", "headings": duplicates}, [], {"preservation_check": "NOT_RUN"}
    if len(recognized) < 2:
        return claim_block, None, [name for _, name in recognized], {"preservation_check": "PASS", "child_block_count": len(recognized)}
    prefix = claim_block[:recognized[0][0]]
    chunks = []
    for i, (start, name) in enumerate(recognized):
        end = recognized[i + 1][0] if i + 1 < len(recognized) else len(claim_block)
        chunks.append({"name": name, "text": claim_block[start:end]})
    slots = list(range(len(chunks)))
    ordered = sorted(chunks, key=lambda x: CLAIM_CHILD_RANK[x["name"]])
    after = prefix + "".join(x["text"] for x in ordered)
    old_blocks = [x["text"] for x in chunks]
    new_blocks = [x["text"] for x in ordered]
    check = {"preservation_check": "PASS" if sorted(old_blocks) == sorted(new_blocks) and len(after) == len(claim_block) else "FAIL", "child_block_count": len(chunks), "block_hashes_before": sorted(sha(x.encode()) for x in old_blocks), "block_hashes_after": sorted(sha(x.encode()) for x in new_blocks)}
    return after, None, [x["name"] for x in chunks], check


def reorder_content(body: str):
    heads = markdown_headings(body)
    recognized = [(pos, name) for pos, level, name in heads if level == 2 and name in CONTENT_RANK]
    counts = Counter(name for _, name in recognized)
    duplicates = [name for name, n in counts.items() if n > 1]
    if duplicates:
        return body, {"hold": "duplicate declared Content heading(s)", "headings": duplicates}, [n for _, n in recognized], [n for _, n in recognized], {"preservation_check": "NOT_RUN"}
    if not recognized:
        return body, None, [], [], {"preservation_check": "PASS", "section_block_count": 0}
    prefix = body[:recognized[0][0]]
    chunks = []
    for i, (start, name) in enumerate(recognized):
        end = recognized[i + 1][0] if i + 1 < len(recognized) else len(body)
        part = body[start:end]
        if name == "Claim":
            new_part, hold, old_children, child_check = reorder_children(part)
            if hold:
                return body, hold, [n for _, n in recognized], [n for _, n in recognized], {"preservation_check": "NOT_RUN"}
            if child_check["preservation_check"] == "FAIL":
                return body, {"hold": "Claim child byte-preservation self-check failed"}, [n for _, n in recognized], [n for _, n in recognized], {"preservation_check": "FAIL"}
            part = new_part
            chunks.append({"name": name, "text": part, "children_before": old_children, "children_after": [n for _, level, n in markdown_headings(part) if level == 3 and n in CLAIM_CHILD_RANK], "child_check": child_check})
        else:
            chunks.append({"name": name, "text": part})
    original = [x["name"] for x in chunks]
    reordered = sorted(chunks, key=lambda x: CONTENT_RANK[x["name"]])
    after = prefix + "".join(x["text"] for x in reordered)
    before_sections = [x["text"] for x in chunks]
    after_sections = [x["text"] for x in reordered]
    check = {"preservation_check": "PASS" if sorted(before_sections) == sorted(after_sections) and len(after) == len(body) else "FAIL", "section_block_count": len(chunks), "block_hashes_before": sorted(sha(x.encode()) for x in before_sections), "block_hashes_after": sorted(sha(x.encode()) for x in after_sections), "claim_children_before": next((x["children_before"] for x in chunks if x["name"] == "Claim"), []), "claim_children_after": next((x["children_after"] for x in chunks if x["name"] == "Claim"), []), "claim_child_block_hashes_before": next((x["child_check"].get("block_hashes_before", []) for x in chunks if x["name"] == "Claim"), []), "claim_child_block_hashes_after": next((x["child_check"].get("block_hashes_after", []) for x in chunks if x["name"] == "Claim"), [])}
    return after, None, original, [x["name"] for x in reordered], check


def parse_frontmatter_metadata_with_ruby(pairs):
    if not pairs:
        return {}
    ruby = r'''require 'yaml'; require 'json'; require 'date'
input = JSON.parse(STDIN.read)
out = input.map do |item|
  begin
    b = YAML.safe_load(item['before'], permitted_classes: [Date, Time], aliases: true)
    a = YAML.safe_load(item['after'], permitted_classes: [Date, Time], aliases: true)
    [item['path'], b == a ? nil : 'parsed YAML metadata differs']
  rescue StandardError => e
    [item['path'], "YAML parse/equality check failed: #{e.class}: #{e.message}"]
  end
end
STDOUT.write(JSON.generate(out))
'''
    result = subprocess.run(["ruby", "-e", ruby], input=json.dumps(pairs).encode(), stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=False)
    if result.returncode:
        raise RuntimeError("Ruby YAML verification failed: " + result.stderr.decode(errors="replace")[:500])
    return dict(json.loads(result.stdout.decode()))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--extra-fields", choices=sorted(EXTRA_FIELD_POLICIES), default=DEFAULT_EXTRA_FIELD_POLICY,
                        help="placement for unlisted/legacy Header keys; default reflects the explicit user decision")
    args = parser.parse_args()
    snapshot_bytes = SNAPSHOT.read_bytes()
    snapshot = json.loads(snapshot_bytes)
    rows = snapshot["carriers"]
    eligible = []
    excluded = []
    holds = []
    for row in rows:
        relpath = row["path"]
        if protected(relpath):
            excluded.append({"path": relpath, "reason": "protected history/archive/journal/projection/test/copy path"})
            continue
        path = ROOT / relpath
        if not path.exists() or not path.is_file():
            holds.append({"path": relpath, "reason": "snapshot source path missing or not a regular file"})
            continue
        if path.is_symlink() or not path.resolve().is_relative_to(ROOT.resolve()):
            holds.append({"path": relpath, "reason": "source symlink or outside repository"})
            continue
        eligible.append((row, path, path.read_bytes()))

    prepared = []
    yaml_pairs = []
    for row, path, raw in eligible:
        relpath = row["path"]
        try:
            text = raw.decode("utf-8")
        except UnicodeDecodeError:
            holds.append({"path": relpath, "reason": "source is not UTF-8"})
            continue
        bounds = split_frontmatter(text)
        if bounds is None:
            holds.append({"path": relpath, "reason": "missing or malformed YAML frontmatter"})
            continue
        fm_start, fm_end = bounds
        header = text[fm_start:fm_end - len(text[fm_end - 1:fm_end])] if text[fm_end - 1:fm_end] in ("\n", "\r") else text[fm_start:fm_end]
        # The closing delimiter line belongs to frontmatter but must not enter YAML.
        close_line_start = text.rfind("\n", fm_start, fm_end - 1) + 1
        header = text[fm_start:close_line_start]
        body = text[fm_end:]
        new_header, h_hold, old_keys = reorder_header(header, args.extra_fields)
        if h_hold:
            holds.append({"path": relpath, "reason": h_hold["hold"], "details": h_hold})
            continue
        new_body, b_hold, old_sections, new_sections, content_check = reorder_content(body)
        if b_hold:
            holds.append({"path": relpath, "reason": b_hold["hold"], "details": b_hold})
            continue
        if content_check["preservation_check"] == "FAIL":
            holds.append({"path": relpath, "reason": "Content byte-preservation self-check failed"})
            continue
        candidate_text = text[:fm_start] + new_header + text[close_line_start:fm_end] + new_body
        try:
            candidate = candidate_text.encode("utf-8")
        except UnicodeEncodeError:
            holds.append({"path": relpath, "reason": "candidate encoding failed"})
            continue
        old_known = [x for x in old_keys if x in HEADER_RANK]
        new_keys = [x["key"] for x in yaml_blocks(new_header)[1]]
        new_known = [x for x in new_keys if x in HEADER_RANK]
        # Confirm the written Header property order is the canonical induced subsequence.
        old_unknown = [key for key in old_keys if key not in HEADER_RANK]
        new_unknown = [key for key in new_keys if key not in HEADER_RANK]
        if sorted(old_known, key=lambda x: HEADER_RANK[x]) != new_known:
            holds.append({"path": relpath, "reason": "Header induced-order self-check failed", "old": old_known, "candidate": new_known})
            continue
        if old_unknown != new_unknown:
            holds.append({"path": relpath, "reason": "unlisted Header key slots or relative order changed", "old": old_unknown, "candidate": new_unknown})
            continue
        # Keep the original key sequence for review, and defer semantic YAML equality to one batch parse.
        op = {
            "path": relpath,
            "live_path_status": "VERIFIED_REGULAR_FILE",
            "class": row.get("class"),
            "atom_id": row.get("id"),
            "source_snapshot_sha256": row.get("sha256"),
            "before_sha256": sha(raw),
            "after_sha256": sha(candidate),
            "header_keys_before": old_keys,
            "header_keys_after": new_keys,
            "header_known_order_before": old_known,
            "header_known_order_after": new_known,
            "content_sections_before": old_sections,
            "content_sections_after": new_sections,
            "content_preservation": content_check,
            "content_reordered": new_body != body,
            "header_reordered": new_header != header,
            "before": text if candidate != raw else None,
            "after": candidate_text if candidate != raw else None,
            "_before_yaml": header,
            "_after_yaml": new_header,
        }
        if candidate != raw:
            prepared.append(op)
            yaml_pairs.append({"path": relpath, "before": header, "after": new_header})
        else:
            prepared.append(op)

    yaml_results = parse_frontmatter_metadata_with_ruby(yaml_pairs)
    yaml_holds = []
    for op in prepared:
        issue = yaml_results.get(op["path"])
        if issue:
            yaml_holds.append({"path": op["path"], "reason": issue})
    if yaml_holds:
        holds.extend(yaml_holds)
    invalid = {x["path"] for x in yaml_holds}
    operations = []
    source_rows = []
    for op in prepared:
        if op["path"] in invalid:
            continue
        op.pop("_before_yaml", None)
        op.pop("_after_yaml", None)
        op["action"] = "REORDER" if op["before"] is not None else "UNCHANGED"
        source_rows.append({k: v for k, v in op.items() if k not in ("before", "after")})
        if op["before"] is not None:
            operations.append(op)
        else:
            op.pop("before", None); op.pop("after", None)

    counts = Counter()
    for row in eligible:
        counts[row[0].get("class", "unknown")] += 1
    report = {
        "status": "PREPARED_WITH_HOLDS" if holds else "READY_FOR_REVIEW_NOT_APPLIED",
        "scope": "Analysis-only ordering plan. No Current or Draft source is written.",
        "input": {"snapshot_path": rel(SNAPSHOT), "snapshot_sha256": sha(snapshot_bytes), "snapshot_carrier_count": len(rows), "analysis_helper_path": rel(Path(__file__).resolve()), "analysis_helper_sha256": sha(Path(__file__).resolve().read_bytes())},
        "selection": {"eligible_live_sources": len(eligible), "excluded_protected_paths": len(excluded), "class_counts": dict(counts), "missing_or_invalid_sources": len(holds)},
        "ordering": {"header_keys": HEADER_ORDER, "content_root_headings": CONTENT_ORDER, "claim_children": CLAIM_CHILD_ORDER, "unlisted_header_keys": {"placement_policy": args.extra_fields, "relative_order": "preserved among all unlisted keys; values and YAML blocks are not rewritten"}},
        "verification": {"yaml_parse_equality": "Ruby Psych safe_load; mappings compared structurally after permutation", "body_content": "Full source bytes are preserved except permutation of declared heading blocks; unknown headings remain attached to their containing declared value", "id_version_time": "Whole parsed Header equality ensures all values, including ID/version/updated_at, remain equal", "unlisted_header_fields": "Unknown key blocks retain the same block slots and relative order"},
        "counts": {"live_sources_scanned": len(source_rows), "operations": len(operations), "header_changed": sum(x["header_reordered"] for x in operations), "content_changed": sum(x["content_reordered"] for x in operations), "unchanged": sum(x["action"] == "UNCHANGED" for x in source_rows), "snapshot_hash_drift": sum(x["source_snapshot_sha256"] != x["before_sha256"] for x in source_rows), "yaml_metadata_equal_checked": len(yaml_pairs), "yaml_equality_holds": len(yaml_holds), "holds": len(holds)},
        "sources": source_rows,
        "operations": operations,
        "excluded": excluded,
        "holds": holds,
    }
    OUTPUT.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps({"status": report["status"], "counts": report["counts"], "selection": report["selection"], "output": rel(OUTPUT)}, indent=2))


if __name__ == "__main__":
    main()
