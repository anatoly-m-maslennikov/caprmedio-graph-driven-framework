#!/usr/bin/env python3
"""Prepare pinned CFEL notation operations without changing any source carrier.

The only census is live-census.json:inventory. Each edit is an
absolute character span in a current inventory carrier; the generated packet
also contains the predicted complete-file postimage digest.
"""
import hashlib
import json
import re
from collections import Counter, defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[6]
PLAN = ROOT / ".caprmedio_caprmedio/02_analysis/draft/epic-completion-20261104/coverage/ordered-source-migration-20261105/live-census.json"
OUT = HERE / "prepared-operations.json"
LITERAL = re.compile(r'"(?:\\.|[^"\\\r\n])*"|\'(?:\\.|[^\'\\\r\n])*\'')


def digest(text):
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def protect(text):
    """Mask quotes/comments while preserving positions (migrate.py discipline)."""
    values, out, index = [], [], 0
    while index < len(text):
        match = LITERAL.match(text, index)
        if match:
            value = match.group(0)
            values.append((index, value))
            out.append(" " * len(value))
            index = match.end()
        elif text[index] == "#":
            stop = text.find("\n", index)
            stop = len(text) if stop == -1 else stop
            values.append((index, text[index:stop]))
            out.append(" " * (stop - index))
            index = stop
        else:
            out.append(text[index])
            index += 1
    return "".join(out), values


def restore(text, values):
    """Restore a same-length masked carrier, matching migrate.py's contract."""
    restored = list(text)
    for start, value in values:
        restored[start:start + len(value)] = value
    return "".join(restored)


def claim_fence_spans(text):
    """Return CFEL/GFEL bodies only when their fence is inside a Claim section."""
    spans = []
    for claim in re.finditer(r"(?ms)^## Claim[ \t]*\r?\n(.*?)(?=^## |\Z)", text):
        body_start = claim.start(1)
        for fence in re.finditer(r"(?ms)^```(?:CFEL|GFEL)[ \t]*\r?\n(.*?)(?=^```)", claim.group(1)):
            spans.append((body_start + fence.start(1), body_start + fence.end(1)))
    return spans


def line_number(text, position):
    return text.count("\n", 0, position) + 1


def add(operations, text, path, start, end, replacement, kind, fence_start):
    old = text[start:end]
    if old == replacement:
        return
    operations.append({
        "path": path,
        "before_sha256": digest(text),
        "char_span": [start, end],
        "line": line_number(text, start),
        "before": old,
        "after": replacement,
        "kind": kind,
        "scope": "Claim CFEL/GFEL fence; unquoted and uncommented",
        "fence_start": fence_start,
    })


def cfel_operations(text, path):
    operations = []
    for start, end in claim_fence_spans(text):
        body = text[start:end]
        visible, _ = protect(body)
        patterns = (
            (r"(\$[A-Za-z_]\w*)\.Header\.Subjects\.Active\b", None, "variable_header_active_to_main_subject"),
            (r"(\$[A-Za-z_]\w*)\.Header\.Subjects\.Passive\b", None, "variable_header_passive_to_dependencies"),
            (r"(\$[A-Za-z_]\w*)\.Header\.Subjects\b", None, "variable_header_subjects_to_topics"),
            (r"(?<![\w.])Atom\.Header\.Subjects\.Active\b", "Atom.Header.Topics.Main Subject", "header_active_to_main_subject"),
            (r"(?<![\w.])Atom\.Header\.Subjects\.Passive\b", "Atom.Header.Topics.Dependencies", "header_passive_to_dependencies"),
            (r"(?<![\w.])Atom\.Header\.Subjects\b", "Atom.Header.Topics", "header_subjects_to_topics"),
            (r"\{:(\d+(?:\+|\.\.\d+)?)\}", None, "qualified_count_colon_to_double_colon"),
            (r"(?<![:=])(:)(?![:=])(?=[ \t]*\[)", None, "property_format_colon_to_double_colon"),
        )
        occupied = []
        for pattern, replacement, kind in patterns:
            for match in re.finditer(pattern, visible):
                left, right = start + match.start(), start + match.end()
                if any(left < used_right and right > used_left for used_left, used_right in occupied):
                    continue
                candidate = replacement
                if kind == "qualified_count_colon_to_double_colon":
                    candidate = "{::" + match.group(1) + "}"
                elif kind == "property_format_colon_to_double_colon":
                    left, right, candidate = start + match.start(1), start + match.end(1), "::"
                elif kind.startswith("variable_header_"):
                    suffix = {
                        "variable_header_active_to_main_subject": ".Header.Topics.Main Subject",
                        "variable_header_passive_to_dependencies": ".Header.Topics.Dependencies",
                        "variable_header_subjects_to_topics": ".Header.Topics",
                    }[kind]
                    candidate = match.group(1) + suffix
                add(operations, text, path, left, right, candidate, kind, start)
                occupied.append((left, right))
    return operations


def metadata_operations(text, path):
    """Plan only unquoted front-matter Subjects -> Topics field migration."""
    front = re.match(r"\A---\r?\n(.*?)(?:^---\r?\n)", text, re.M | re.S)
    if not front:
        return []
    content = front.group(1)
    match = re.search(r"(?m)^subjects:\r?\n((?:^[ \t]+[^\r\n]*(?:\r?\n|$))*)", content)
    operations = []
    if match:
        block_start = front.start(1) + match.start()
        old = match.group(0)
        lines = old.splitlines(keepends=True)
        converted = [re.sub(r"^subjects:", "topics:", lines[0])]
        for line in lines[1:]:
            line = re.sub(r"^(\s*)active:", r"\1main_subject:", line)
            converted.append(re.sub(r"^(\s*)passive:", r"\1dependencies:", line))
        new = "".join(converted)
        if old != new:
            operations.append({
                "path": path, "before_sha256": digest(text),
                "char_span": [block_start, block_start + len(old)], "line": line_number(text, block_start),
                "before": old, "after": new, "kind": "frontmatter_subjects_to_topics",
                "scope": "front-matter keys only; never quoted data",
            })
    # Address values in an existing Topics mapping are scalars, not prose. Edit
    # the address substring only, retaining the original YAML quote encoding.
    topics = re.search(r"(?m)^topics:\r?\n((?:^[ \t]+[^\r\n]*(?:\r?\n|$))*)", content)
    if not topics:
        return operations
    topics_start = front.start(1) + topics.start(1)
    for scalar in re.finditer(r"(?m)^(?:[ \t]*main_subject:[ \t]*|[ \t]*-[ \t]*)([^\r\n#]+)", topics.group(1)):
        value_start = topics_start + scalar.start(1)
        value = scalar.group(1)
        for old, new, kind in (
            ("Atom.Header.Subjects.Active", "Atom.Header.Topics.Main Subject", "yaml_topic_active_address"),
            ("Atom.Header.Subjects.Passive", "Atom.Header.Topics.Dependencies", "yaml_topic_passive_address"),
            ("Atom.Header.Subjects", "Atom.Header.Topics", "yaml_topic_subjects_address"),
        ):
            tail = r"\b(?!\.(?:Active|Passive)\b)" if old == "Atom.Header.Subjects" else r"\b"
            for found in re.finditer(r"(?<![\w.])" + re.escape(old) + tail, value):
                operations.append({
                    "path": path, "before_sha256": digest(text),
                    "char_span": [value_start + found.start(), value_start + found.end()],
                    "line": line_number(text, value_start + found.start()),
                    "before": found.group(0), "after": new, "kind": kind,
                    "scope": "Topics main_subject/dependencies scalar address; YAML quote encoding retained",
                })
    return operations


def apply_spans(text, operations):
    for operation in sorted(operations, key=lambda item: item["char_span"][0], reverse=True):
        start, end = operation["char_span"]
        assert text[start:end] == operation["before"], operation
        text = text[:start] + operation["after"] + text[end:]
    return text


def self_test():
    sample = (
        "---\r\nsubjects:\r\n  active: x\r\n---\r\n\r\n## Claim\r\n"
        "```CFEL\r\nactual{:1}; quoted '{:1}'; p: [in(\"a\", \"b\")] # comment {:1}\r\n```\r\n"
        "```python\r\nnon_cfel{:1}\r\n```\r\n## Analysis\r\noutside{:1}\r\n"
    )
    changed = apply_spans(sample, cfel_operations(sample, "sample.md"))
    assert "actual{::1}" in changed
    assert "'{:1}'" in changed and "# comment {:1}" in changed
    assert 'p:: [in("a", "b")]' in changed
    assert "non_cfel{:1}" in changed and "outside{:1}" in changed
    assert "\r\n" in changed and changed.count("{::1}") == 1


def main():
    self_test()
    plan = json.loads(PLAN.read_text(encoding="utf-8"))
    inventory = plan["inventory"]
    all_operations, by_path = [], defaultdict(list)
    census_snapshot_drift = 0
    for row in inventory:
        path = row["path"]
        raw = (ROOT / path).read_bytes()
        text = raw.decode("utf-8")
        if digest(text) != row["sha256"]:
            census_snapshot_drift += 1
        if "\r\n" in text:
            assert raw.count(b"\r\n") == text.count("\r\n")
        operations = metadata_operations(text, path) + cfel_operations(text, path)
        spans = sorted(item["char_span"] for item in operations)
        assert all(left[1] <= right[0] for left, right in zip(spans, spans[1:])), path
        postimage = apply_spans(text, operations) if operations else text
        for operation in operations:
            operation["after_sha256"] = digest(postimage)
            operation["census_sha256"] = row["sha256"]
            operation["census_sha256_matches_current"] = operation["before_sha256"] == row["sha256"]
            operation["guard"] = "90% deterministic context gate: exact selected scope, unmasked token, and pinned current preimage required"
        if operations:
            all_operations.extend(operations)
            by_path[path].extend(operations)
    result = {
        "status": "PREPARED_NOT_APPLIED",
        "inventory_source": str(PLAN.relative_to(ROOT)),
        "inventory_key": "inventory",
        "logical_path_mapping": {
            "Atom.Header.Subjects.Active": "Atom.Header.Topics.Main Subject",
            "Atom.Header.Subjects.Passive": "Atom.Header.Topics.Dependencies",
            "Atom.Header.Subjects": "Atom.Header.Topics",
        },
        "counts": {
            "inventory": len(inventory), "operations": len(all_operations),
            "changed_sources": len(by_path),
            "census_snapshot_drift_sources": census_snapshot_drift,
            "by_kind": dict(sorted(Counter(item["kind"] for item in all_operations).items())),
        },
        "operations": all_operations,
        "per_span_log": all_operations,
        "holds": [
            "quoted literals and comments", "non-CFEL/GFEL fences", "content outside Claim",
            "ambiguous admission/condition/slash notation", "source writes (this packet is prepare-only)",
            "live-census snapshot drift is recorded; current per-operation source pins govern any future apply",
        ],
        "assertions": [
            "quoted {:1} unchanged", "comments unchanged", "non-CFEL fence unchanged",
            "CRLF retained", "body outside selected Claim fence unchanged",
        ],
    }
    OUT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
