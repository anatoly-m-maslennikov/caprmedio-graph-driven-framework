#!/usr/bin/env python3
"""Prepare a read-only Markdown-link rebase plan for a pinned move subset.

This analysis helper never writes Atom sources. It writes JSON containing
source/destination rows, exact href edits, observed hashes, and ambiguous syntax
holds so a separate owner can review/re-pin before any physical move.
"""
from __future__ import annotations

import hashlib
import json
import posixpath
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path, PurePosixPath
from urllib.parse import urlsplit


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[7]
CONTROL = ROOT / ".caprmedio_caprmedio"
PACKET = CONTROL / "02_analysis/draft/epic-completion-20261104"
MIGRATION = PACKET / "coverage/ordered-source-migration-20261105"
ELIGIBLE = MIGRATION / "verification/destination-eligible-subset.json"
SNAPSHOT = MIGRATION / "property-audit/snapshot.json"
FILL_PLAN = MIGRATION / "destinations/fill-application/adoption-plan.json"
FILL_RECEIPT = MIGRATION / "destinations/fill-application/adoption-receipt.json"
CFEL_PLAN = MIGRATION / "cfel-values/application/adoption-plan.json"
CFEL_RECEIPT = MIGRATION / "cfel-values/application/adoption-receipt.json"
CONTRACT_PLAN = MIGRATION / "cfel-values/contract-repair-application/adoption-plan.json"
CONTRACT_RECEIPT = MIGRATION / "cfel-values/contract-repair-application/adoption-receipt.json"
OUTPUT = HERE / "link-rebase-plan.json"
EXTRA_GROUPS = (
    "CA-SU-26_LAYER_4_CORE_EXTENSIONS/201_FEATURE_GIT",
    "CA-SU-26_LAYER_4_CORE_EXTENSIONS/202_FEATURE_FPF",
)
EXCLUDED_COMPONENTS = {
    "archive", "archived", "journal", "journals", "snapshot", "snapshots",
    "_journal", "_projection", "projections", "projection", "withdrawn",
    "000_caprmedio_framework",
}
TEST_PREFIX = "TEST-"
EXTERNAL_SCHEME = re.compile(r"^[A-Za-z][A-Za-z0-9+.-]*:")
FENCE_OPEN = re.compile(r"^ {0,3}(`{3,}|~{3,})(.*)$")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def repo_rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def safe_repo_path(value: str, allow_case_alias_from: Path | None = None) -> Path:
    p = PurePosixPath(value)
    if not value or p.is_absolute() or ".." in p.parts or "." in p.parts:
        raise ValueError(f"non-normal repository-relative path: {value}")
    result = ROOT.joinpath(*p.parts)
    if not result.resolve().is_relative_to(ROOT.resolve()):
        raise ValueError(f"symlink/path escapes repository: {value}")
    if result.resolve() != result:
        case_alias_ok = False
        if allow_case_alias_from is not None and result.exists() and not result.is_symlink():
            try:
                a, b = allow_case_alias_from.stat(), result.stat()
                case_alias_ok = (a.st_dev, a.st_ino) == (b.st_dev, b.st_ino)
            except OSError:
                pass
        if not case_alias_ok:
            raise ValueError(f"symlink path needs manual review: {value}")
    return result


def protected_source(path: str) -> bool:
    parts = PurePosixPath(path).parts
    return any(x.lower() in EXCLUDED_COMPONENTS or x.startswith(TEST_PREFIX) for x in parts)


def frontmatter_end(text: str) -> int:
    if not text.startswith("---\n"):
        return 0
    end = text.find("\n---\n", 4)
    return end + 5 if end >= 0 else 0


def code_mask(text: str, body_start: int) -> bytearray:
    """Mask fenced code and matched inline code spans while preserving offsets."""
    mask = bytearray(len(text))
    lines = text.splitlines(keepends=True)
    pos = 0
    fence_char = None
    fence_len = 0
    for line in lines:
        end = pos + len(line)
        if end <= body_start:
            pos = end
            continue
        visible = line.rstrip("\r\n")
        if fence_char is not None:
            mask[pos:end] = b"\x01" * (end - pos)
            close = re.match(r"^ {0,3}" + re.escape(fence_char) + r"{" + str(fence_len) + r",}\s*$", visible)
            if close:
                fence_char = None
                fence_len = 0
            pos = end
            continue
        opener = FENCE_OPEN.match(visible)
        if opener:
            run = opener.group(1)
            fence_char, fence_len = run[0], len(run)
            mask[pos:end] = b"\x01" * (end - pos)
        pos = end

    # CommonMark code spans may cross line breaks. Only use delimiters outside
    # fenced blocks; unmatched runs remain literal text.
    i = body_start
    while i < len(text):
        if mask[i]:
            i += 1
            continue
        if text[i] != "`" or (i > 0 and text[i - 1] == "\\"):
            i += 1
            continue
        j = i + 1
        while j < len(text) and text[j] == "`":
            j += 1
        width = j - i
        k = j
        close = None
        while k < len(text):
            if mask[k]:
                k += 1
                continue
            if text[k] == "`" and (k == 0 or text[k - 1] != "\\"):
                m = k + 1
                while m < len(text) and text[m] == "`":
                    m += 1
                if m - k == width:
                    close = m
                    break
                k = m
            else:
                k += 1
        if close is None:
            i = j
            continue
        mask[i:close] = b"\x01" * (close - i)
        i = close
    return mask


def escaped(text: str, index: int) -> bool:
    n = 0
    index -= 1
    while index >= 0 and text[index] == "\\":
        n += 1
        index -= 1
    return n % 2 == 1


def ref_label_key(label: str) -> str:
    return re.sub(r"\s+", " ", label.strip()).casefold()


def inline_link_close(text: str, pos: int, mask: bytearray):
    while pos < len(text) and text[pos] in " \t\r\n":
        pos += 1
    if pos < len(text) and text[pos] == ")":
        return pos
    if pos >= len(text) or text[pos] not in "\"'(":
        return None
    opener = text[pos]
    if opener in "\"'":
        i = pos + 1
        while i < len(text):
            if mask[i]:
                return None
            if text[i] == opener and not escaped(text, i):
                i += 1
                break
            i += 1
        else:
            return None
    else:
        depth = 1
        i = pos + 1
        while i < len(text):
            if mask[i]:
                return None
            if not escaped(text, i):
                if text[i] == "(":
                    depth += 1
                elif text[i] == ")":
                    depth -= 1
                    if depth == 0:
                        i += 1
                        break
            i += 1
        else:
            return None
    while i < len(text) and text[i] in " \t\r\n":
        i += 1
    return i if i < len(text) and text[i] == ")" else None


def parse_reference_definitions(text: str, mask: bytearray, body_start: int):
    refs = []
    ambiguous = []
    offset = 0
    for line_no, line in enumerate(text.splitlines(keepends=True), 1):
        end = offset + len(line)
        raw = line.rstrip("\r\n")
        if offset >= body_start and not any(mask[offset:end]):
            # Support standard one-line reference definitions, including
            # angle destinations and optional quoted/parenthesized titles.
            m = re.match(r"^ {0,3}\[([^\]]+)\]:[ \t]+", raw)
            if m:
                start = m.end()
                if start < len(raw) and raw[start] == "<":
                    i = start + 1
                    while i < len(raw) and (raw[i] != ">" or escaped(raw, i)):
                        i += 1
                    if i == len(raw):
                        ambiguous.append({"line": line_no, "reason": "unterminated angle reference destination"})
                    else:
                        refs.append({"label": m.group(1), "label_key": ref_label_key(m.group(1)), "start": offset + start + 1, "end": offset + i, "href": raw[start + 1:i], "syntax": "reference_definition_angle", "line": line_no})
                else:
                    i = start
                    while i < len(raw) and not raw[i].isspace():
                        if raw[i] == "\\" and i + 1 < len(raw):
                            i += 2
                        else:
                            i += 1
                    href = raw[start:i]
                    if not href:
                        ambiguous.append({"line": line_no, "reason": "empty reference destination"})
                    else:
                        refs.append({"label": m.group(1), "label_key": ref_label_key(m.group(1)), "start": offset + start, "end": offset + i, "href": href, "syntax": "reference_definition_bare", "line": line_no})
        offset = end
    keys = defaultdict(list)
    for r in refs:
        keys[r["label_key"]].append(r)
    for key, defs in keys.items():
        hrefs = {x["href"] for x in defs}
        if len(hrefs) > 1:
            ambiguous.append({"line": defs[0]["line"], "reason": "duplicate reference label has conflicting destinations", "label": key})
    return refs, ambiguous


def parse_inline_links(text: str, mask: bytearray, body_start: int):
    links = []
    ambiguous = []
    i = body_start
    while i < len(text):
        if mask[i] or text[i] != "[" or escaped(text, i):
            i += 1
            continue
        # Skip image marker; it is not part of the href span.
        label_start = i + 1
        depth = 1
        j = label_start
        while j < len(text):
            if mask[j]:
                j += 1
                continue
            if escaped(text, j):
                j += 1
                continue
            if text[j] == "[":
                depth += 1
            elif text[j] == "]":
                depth -= 1
                if depth == 0:
                    break
            j += 1
        if j >= len(text):
            i += 1
            continue
        if j + 1 >= len(text) or text[j + 1] != "(":
            i = j + 1
            continue
        k = j + 2
        while k < len(text) and text[k] in " \t\r\n":
            k += 1
        if k >= len(text):
            ambiguous.append({"offset": i, "reason": "inline link has no destination"})
            break
        if text[k] == "<":
            hstart = k + 1
            n = hstart
            while n < len(text) and (text[n] != ">" or escaped(text, n)):
                if mask[n]:
                    ambiguous.append({"offset": i, "reason": "inline link destination crosses code/fence boundary"})
                    break
                n += 1
            if n >= len(text) or text[n] != ">":
                ambiguous.append({"offset": i, "reason": "unterminated angle inline destination"})
                i = j + 2
                continue
            href = text[hstart:n]
            close = inline_link_close(text, n + 1, mask)
            if close is None:
                ambiguous.append({"offset": i, "reason": "ambiguous inline-link title/closing parenthesis"})
                i = j + 2
                continue
            links.append({"start": hstart, "end": n, "href": href, "syntax": "inline_angle", "offset": i})
            i = close + 1
            continue
        hstart = k
        n = k
        paren_depth = 0
        while n < len(text):
            if mask[n]:
                ambiguous.append({"offset": i, "reason": "inline link destination crosses code/fence boundary"})
                break
            if escaped(text, n):
                n += 1
                continue
            ch = text[n]
            if ch == "(" :
                paren_depth += 1
            elif ch == ")":
                if paren_depth == 0:
                    break
                paren_depth -= 1
            elif ch.isspace() and paren_depth == 0:
                break
            n += 1
        if n >= len(text) or (n < len(text) and mask[n]):
            i = j + 2
            continue
        href = text[hstart:n]
        if not href:
            ambiguous.append({"offset": i, "reason": "empty inline destination"})
            i = j + 2
            continue
        close = inline_link_close(text, n, mask)
        if close is None:
            ambiguous.append({"offset": i, "reason": "ambiguous inline-link title/closing parenthesis"})
            i = j + 2
            continue
        links.append({"start": hstart, "end": n, "href": href, "syntax": "inline_bare", "offset": i})
        i = close + 1
    return links, ambiguous


def resolve_href(href: str, old_referer: str, new_referer: str, move_map: dict[str, str]):
    if not href or href.startswith("#") or href.startswith("//") or EXTERNAL_SCHEME.match(href):
        return None
    if "\\" in href or "%" in href:
        return {"hold": "escaped_or_percent_encoded_relative_path"}
    parsed = urlsplit(href)
    if parsed.scheme or parsed.netloc or parsed.path.startswith("/") or not parsed.path:
        return None
    old_target = posixpath.normpath(posixpath.join(posixpath.dirname(old_referer), parsed.path))
    if old_target == ".." or old_target.startswith("../") or old_target.startswith("/"):
        return {"hold": "relative_target_escapes_repository"}
    if ".." in PurePosixPath(old_target).parts:
        return {"hold": "relative_target_escapes_repository"}
    new_target = move_map.get(old_target, old_target)
    new_path = posixpath.relpath(new_target, posixpath.dirname(new_referer))
    if href.startswith("./") and not new_path.startswith("../") and not new_path.startswith("./"):
        new_path = "./" + new_path
    new_href = new_path
    if parsed.query:
        new_href += "?" + parsed.query
    if parsed.fragment:
        new_href += "#" + parsed.fragment
    reason = []
    if old_referer != new_referer:
        reason.append("referer_path_changes")
    if new_target != old_target:
        reason.append("linked_target_moves")
    if new_href == href:
        return None
    return {"old_target": old_target, "new_target": new_target, "new_href": new_href, "reason": reason or ["normalized_relative_path"]}


def self_check():
    """Exercise only in-memory Markdown/link cases; no repository files touched."""
    moves = {"docs/old.md": "docs/new.md", "assets/pic.png": "assets/pic.png"}
    moved = resolve_href("old.md#part", "docs/old.md", "docs/new.md", moves)
    assert moved and moved["new_href"] == "new.md#part"
    unmoved_asset = resolve_href("../../shared/pic.png", "oldscope/sub/atom.md", "newscope/atom.md", moves)
    assert unmoved_asset and unmoved_asset["new_href"] == "../shared/pic.png"
    assert resolve_href("#anchor", "docs/old.md", "docs/new.md", moves) is None
    assert resolve_href("https://example.test/x", "docs/old.md", "docs/new.md", moves) is None
    assert resolve_href(r"../assets/a\ b.png", "docs/old.md", "docs/new.md", moves)["hold"] == "escaped_or_percent_encoded_relative_path"
    fixture = ('---\nmeta: yes\n---\n'
               '[inline](../assets/pic.png "title") and [angle](<../assets/pic.png> "t")\n'
               '[escaped title](<../assets/pic.png> "a \\"quote\\" and )")\n'
               '`[code](ignored.md)`\n'
               '```md\n[block](ignored.md)\n```\n'
               '[ref]: <../assets/pic.png> "ref title"\n')
    start = frontmatter_end(fixture)
    mask = code_mask(fixture, start)
    inline, ia = parse_inline_links(fixture, mask, start)
    refs, ra = parse_reference_definitions(fixture, mask, start)
    assert not ia and not ra
    assert [x["syntax"] for x in inline] == ["inline_bare", "inline_angle", "inline_angle"]
    assert len(refs) == 1 and refs[0]["syntax"] == "reference_definition_angle"
    assert "[code](ignored.md)" not in [fixture[x["start"]:x["end"]] for x in inline]
    assert "[block](ignored.md)" not in [fixture[x["start"]:x["end"]] for x in inline]
    return {
        "status": "PASS",
        "checks": ["moved target with fragment", "unmoved asset from renamed referer", "anchor-only unchanged", "URL unchanged", "escaped path held", "inline bare/angle titles preserved by href-span model", "reference definition angle/title supported", "frontmatter, inline code, and fenced code excluded"],
    }


def scalar_field(text: str, name: str):
    m = re.search(r"(?m)^" + re.escape(name) + r":[ \t]*(.*?)[ \t]*$", text)
    return m.group(1).strip().strip("'\"") if m else None


def nested_scalar(text: str, parent: str, child: str):
    m = re.search(r"(?ms)^" + re.escape(parent) + r":[ \t]*\n((?:[ \t]+.*\n?)*)", text)
    if not m:
        return None
    child_match = re.search(r"(?m)^  " + re.escape(child) + r":[ \t]*(.*?)[ \t]*$", m.group(1))
    return child_match.group(1).strip().strip("'\"") if child_match else None


def main():
    subset = json.loads(ELIGIBLE.read_text(encoding="utf-8"))
    snapshot = json.loads(SNAPSHOT.read_text(encoding="utf-8"))
    fill_plan = json.loads(FILL_PLAN.read_text(encoding="utf-8"))
    fill_receipt = json.loads(FILL_RECEIPT.read_text(encoding="utf-8"))
    cfel_plan = json.loads(CFEL_PLAN.read_text(encoding="utf-8"))
    cfel_receipt = json.loads(CFEL_RECEIPT.read_text(encoding="utf-8"))
    contract_plan = json.loads(CONTRACT_PLAN.read_text(encoding="utf-8"))
    contract_receipt = json.loads(CONTRACT_RECEIPT.read_text(encoding="utf-8"))
    rows = subset["eligible"]
    if len(rows) != 3123 or subset.get("eligible_count") != 3123:
        raise SystemExit("HOLD: eligible subset count changed; refresh this analysis first")
    plan_path = MIGRATION / "destinations/plan.json"
    if subset.get("plan_sha256") != sha256(plan_path):
        raise SystemExit("HOLD: eligible subset is pinned to a different destination plan")
    plan_by_source = {r["source"]: r for r in rows}
    if len(plan_by_source) != len(rows):
        raise SystemExit("HOLD: duplicate eligible sources")
    fill_ops = {x["path"]: x for x in fill_plan["operations"]}
    cfel_ops = {x["path"]: x for x in cfel_plan["operations"]}
    contract_ops = {x["path"]: x for x in contract_plan["operations"]}
    if len(fill_ops) != len(fill_plan["operations"]):
        raise SystemExit("HOLD: duplicate fill operations")
    fill_readback_issues = []
    fill_readback_verified = 0
    chain_counts = Counter()
    chain_expected_hashes = {}
    for r in rows:
        rel = r["source"]
        path = safe_repo_path(rel)
        current = path.read_text(encoding="utf-8")
        expected_hash = r["source_sha256"]
        fill_op = fill_ops.get(rel)
        if fill_op:
            if fill_op["before_sha256"] != expected_hash:
                fill_readback_issues.append({"source": rel, "reason": "destination_fill_preimage_does_not_match_eligible_pin"})
            else:
                chain_counts["fill_preimages_matched"] += 1
            expected_hash = fill_op["after_sha256"]
        cfel_op = cfel_ops.get(rel)
        if cfel_op:
            if cfel_op["before_sha256"] != expected_hash:
                fill_readback_issues.append({"source": rel, "reason": "CFEL_preimage_does_not_match_prior_application_output"})
            else:
                chain_counts["cfel_preimages_matched"] += 1
            expected_hash = cfel_op["after_sha256"]
        contract_op = contract_ops.get(rel)
        if contract_op:
            if contract_op["before_sha256"] != expected_hash:
                fill_readback_issues.append({"source": rel, "reason": "CFEL_contract_repair_preimage_does_not_match_prior_application_output"})
            else:
                chain_counts["cfel_contract_preimages_matched"] += 1
            expected_hash = contract_op["after_sha256"]
        current_hash = sha256(path)
        chain_expected_hashes[rel] = expected_hash
        if current_hash != expected_hash:
            fill_readback_issues.append({"source": rel, "reason": "current_source_does_not_match_application_chain_output", "expected_sha256": expected_hash, "observed_sha256": current_hash})
        else:
            chain_counts["current_outputs_matched"] += 1
        exp_name = PurePosixPath(r["destination"]).name
        exp_path = PurePosixPath(r["destination"]).parent.as_posix()
        actual_name = nested_scalar(current, "carrier_destination", "file")
        # The file mapping has two nested scalars; inspect its block explicitly.
        block = re.search(r"(?ms)^carrier_destination:[ \t]*\n((?:[ \t]+.*\n?)*)", current)
        file_block = re.search(r"(?ms)^  file:[ \t]*\n((?:[ \t]+.*\n?)*)", block.group(1)) if block else None
        actual_name = None
        actual_path = None
        if file_block:
            nm = re.search(r"(?m)^    name:[ \t]*(.*?)[ \t]*$", file_block.group(1))
            pm = re.search(r"(?m)^    path:[ \t]*(.*?)[ \t]*$", file_block.group(1))
            actual_name = nm.group(1).strip().strip("'\"") if nm else None
            actual_path = pm.group(1).strip().strip("'\"") if pm else None
        if (actual_name, actual_path) != (exp_name, exp_path):
            fill_readback_issues.append({"source": rel, "reason": "carrier_destination_does_not_match_eligible_target", "expected": {"name": exp_name, "path": exp_path}, "actual": {"name": actual_name, "path": actual_path}})
            continue
        op = fill_op
        if op:
            before = op["before"]
            after = op["after"]
            before_identity = (scalar_field(before, "atom_id"), scalar_field(before, "version"), scalar_field(before, "status"))
            after_identity = (scalar_field(after, "atom_id"), scalar_field(after, "version"), scalar_field(after, "status"))
            actual_identity = (scalar_field(current, "atom_id"), scalar_field(current, "version"), scalar_field(current, "status"))
            if before_identity != after_identity or after_identity != actual_identity:
                fill_readback_issues.append({"source": rel, "reason": "ID_version_or_status_changed_during_destination_fill", "before": before_identity, "fill_after": after_identity, "current": actual_identity})
                continue
        fill_readback_verified += 1
    move_map = {r["source"]: r["destination"] for r in rows if r["source"] != r["destination"]}
    move_safety_holds = []
    destination_owners = defaultdict(list)
    for r in rows:
        source_path = safe_repo_path(r["source"])
        destination_path = safe_repo_path(r["destination"], source_path if r.get("case_only_same_inode") else None)
        destination_owners[r["destination"].casefold()].append(r["source"])
        if not source_path.is_file() or source_path.is_symlink():
            move_safety_holds.append({"source": r["source"], "destination": r["destination"], "reason": "source_missing_or_symlink"})
        if destination_path.exists() and r["destination"] != r["source"]:
            same_inode = False
            try:
                a, b = source_path.stat(), destination_path.stat()
                same_inode = (a.st_dev, a.st_ino) == (b.st_dev, b.st_ino)
            except OSError:
                pass
            if not (r.get("case_only_same_inode") and same_inode):
                move_safety_holds.append({"source": r["source"], "destination": r["destination"], "reason": "destination_exists_overwrite_blocked"})
    for dest, owners in destination_owners.items():
        if len(owners) > 1:
            move_safety_holds.append({"destination_casefold": dest, "sources": owners, "reason": "multiple_sources_target_same_destination"})
    sources = {x["path"] for x in snapshot["carriers"]}
    # These active native source roots are deliberately outside the older
    # property snapshot's classifier, but still participate as link referers.
    for rel in EXTRA_GROUPS:
        for f in (CONTROL / rel).rglob("*.md"):
            parts = f.parts
            if any(x.lower() in EXCLUDED_COMPONENTS or x.startswith(TEST_PREFIX) for x in parts):
                continue
            sources.add(repo_rel(f))
    # Include all move-subset files even if a prior snapshot classifier missed one.
    sources.update(plan_by_source)
    source_records = []
    missing_target_preserved_records = []
    source_hashes = {}
    drift = []
    missing = []
    for rel in sorted(sources):
        if protected_source(rel):
            continue
        path = safe_repo_path(rel)
        if not path.is_file() or path.suffix.lower() != ".md":
            continue
        actual = sha256(path)
        source_hashes[rel] = actual
        eligible = plan_by_source.get(rel)
        if eligible and actual != eligible["source_sha256"]:
            drift.append({"source": rel, "pinned_sha256": eligible["source_sha256"], "observed_sha256": actual})
        text = path.read_text(encoding="utf-8")
        body_start = frontmatter_end(text)
        mask = code_mask(text, body_start)
        refs, ref_amb = parse_reference_definitions(text, mask, body_start)
        inline, inline_amb = parse_inline_links(text, mask, body_start)
        parser_holds = ref_amb + inline_amb
        link_holds = []
        # Duplicate reference labels with matching URLs need only one edit; retain
        # every definition span so both spellings can be updated consistently.
        candidates = refs + inline
        edits = []
        new_referer = move_map.get(rel, rel)
        for link in candidates:
            result = resolve_href(link["href"], rel, new_referer, move_map)
            if result is None:
                continue
            if "hold" in result:
                link_holds.append({"line": link.get("line"), "offset": link.get("offset"), "href": link["href"], "reason": result["hold"]})
                continue
            # Only rewrite if the old link resolves to an existing file/directory
            # or a known moved source. Missing local targets are reported, not guessed.
            try:
                old_target_path = safe_repo_path(result["old_target"])
            except ValueError:
                link_holds.append({"line": link.get("line"), "offset": link.get("offset"), "href": link["href"], "reason":"relative_target_symlink_or_outside_repo", "resolved_target":result["old_target"]})
                continue
            if result["old_target"] not in move_map and not old_target_path.exists():
                missing_target_preserved = {"source": rel, "line": link.get("line"), "offset": link.get("offset"), "original_href": link["href"], "rebased_href": result["new_href"], "normalized_unresolved_target": result["old_target"], "classification": "preexisting_missing_target_preserved"}
                # The referer path changes; preserve the exact normalized missing
                # target address rather than guessing an Atom by basename/ID.
                missing_target_preserved_records.append(missing_target_preserved)
            if old_target_path.exists() and (old_target_path.is_symlink() or not old_target_path.resolve().is_relative_to(ROOT.resolve())):
                link_holds.append({"line": link.get("line"), "offset": link.get("offset"), "href": link["href"], "reason":"relative_target_symlink_or_outside_repo", "resolved_target":result["old_target"]})
                continue
            line = text.count("\n", 0, link["start"]) + 1
            edits.append({'start':link['start'],'end':link['end'],'line':line,'syntax':link['syntax'],'before':link['href'],'after':result['new_href'],'old_target':result['old_target'],'new_target':result['new_target'],'reason':result['reason'],'preexisting_missing_target_preserved':result['old_target'] not in move_map and not old_target_path.exists()})
        # Verify replacement ranges are disjoint and apply from right to left.
        edits.sort(key=lambda e:e['start'])
        for a,b in zip(edits,edits[1:]):
            if a['end']>b['start']:
                parser_holds.append({'line':a['line'],'reason':'overlapping link parse spans'})
        after_text=text
        if not parser_holds:
            for e in reversed(edits):
                after_text=after_text[:e['start']]+e['after']+after_text[e['end']:]
        all_holds = parser_holds + link_holds
        record={'source':rel,'destination':new_referer,'source_sha256':actual,'eligible_move_sha256':eligible['source_sha256'] if eligible else None,'movement':('MOVE' if rel in move_map else 'NO_MOVE'),'link_edit_count':len(edits) if not parser_holds else 0,'edits':edits if not parser_holds else [],'ambiguous_or_unresolved_links':all_holds,'after_sha256':hashlib.sha256(after_text.encode('utf-8')).hexdigest() if edits and not parser_holds else actual}
        if edits and not parser_holds:
            record['before_text'] = text
            record['after_text'] = after_text
        source_records.append(record)
        if all_holds:
            missing.append({'source':rel,'holds':all_holds})
    move_rows=[]
    for r in rows:
        source=r['source']; dest=r['destination']; actual=source_hashes.get(source)
        status = 'MISSING' if actual is None else ('MATCH' if actual==r['source_sha256'] else ('HISTORICAL_PREIMAGE_RECONCILED' if actual==chain_expected_hashes.get(source) else 'DRIFT'))
        move_rows.append({'source':source,'destination':dest,'action':'MOVE' if source!=dest else 'NO_MOVE','case_only_same_inode':r.get('case_only_same_inode',False),'historical_eligible_subset_source_sha256':r['source_sha256'],'application_chain_output_sha256':chain_expected_hashes.get(source),'operational_source_sha256':actual,'source_pin_status':status})
    report={
      'status':'REVIEW_REQUIRED_MOVE_SAFETY_OR_APPLICATION_CHAIN_HOLDS' if move_safety_holds or missing or fill_readback_issues else 'READY_FOR_ROOT_REPIN_AND_MOVE_REVIEW',
      'scope':'Analysis only. No source files or directories written, moved, or renamed.',
      'input_pins':{'analysis_helper':{'path':repo_rel(Path(__file__).resolve()),'sha256':sha256(Path(__file__).resolve())},'eligible_subset':{'path':repo_rel(ELIGIBLE),'sha256':sha256(ELIGIBLE),'pinned_plan_sha256':subset.get('plan_sha256')},'destination_plan':{'path':repo_rel(plan_path),'sha256':sha256(plan_path)},'source_snapshot':{'path':repo_rel(SNAPSHOT),'sha256':sha256(SNAPSHOT)},'destination_fill_plan':{'path':repo_rel(FILL_PLAN),'sha256':sha256(FILL_PLAN)},'destination_fill_receipt':{'path':repo_rel(FILL_RECEIPT),'sha256':sha256(FILL_RECEIPT)},'cfel_application_plan':{'path':repo_rel(CFEL_PLAN),'sha256':sha256(CFEL_PLAN)},'cfel_application_receipt':{'path':repo_rel(CFEL_RECEIPT),'sha256':sha256(CFEL_RECEIPT)},'cfel_contract_repair_plan':{'path':repo_rel(CONTRACT_PLAN),'sha256':sha256(CONTRACT_PLAN)},'cfel_contract_repair_receipt':{'path':repo_rel(CONTRACT_RECEIPT),'sha256':sha256(CONTRACT_RECEIPT)}},
      'counts':{'eligible_rows':len(rows),'path_moves':sum(x['action']=='MOVE' for x in move_rows),'no_move_rows':sum(x['action']=='NO_MOVE' for x in move_rows),'historical_subset_pin_drift_reconciled':len(drift),'current_or_draft_referers_scanned':len(source_records),'referers_with_link_edits':sum(x['link_edit_count']>0 for x in source_records),'relative_href_edits':sum(x['link_edit_count'] for x in source_records),'preexisting_missing_targets_preserved':len(missing_target_preserved_records),'ambiguous_or_unresolved_referers':len(missing),'case_only_rows':sum(x['case_only_same_inode'] for x in move_rows)},
      'destination_and_cfel_application_chain_readback':{'destination_fill':{'receipt_status':fill_receipt.get('status'),'operation_count':fill_receipt.get('operation_count'),'output_count':fill_receipt.get('output_count')},'cfel':{'receipt_status':cfel_receipt.get('status'),'operation_count':cfel_receipt.get('operation_count'),'output_count':cfel_receipt.get('output_count')},'cfel_contract_repair':{'receipt_status':contract_receipt.get('status'),'operation_count':contract_receipt.get('operation_count'),'output_count':contract_receipt.get('output_count')},'chain_counts':dict(chain_counts),'verified_eligible_count':fill_readback_verified,'issues':fill_readback_issues},
      'moves':move_rows,'move_safety_holds':move_safety_holds,'referers':source_records,'historical_source_pin_drift':drift,'preexisting_missing_targets_preserved':missing_target_preserved_records,'link_holds':missing,'self_check':self_check(),
      'parser_policy':{'supported':['standard inline Markdown links/images','reference definition hrefs','angle and bare destinations','query/fragment preservation','fenced and inline code masking'],'untouched':['URLs and protocol-relative destinations','anchor-only hrefs','code fences and inline code','archives, Journal, projections, 000, and TEST roots'],'held':['percent-encoded/backslash-escaped relative hrefs','missing relative targets','symlink/out-of-repository targets','conflicting reference definitions','ambiguous inline syntax']},
      'limits':['Eligible-subset hashes remain historical pre-fill pins. Operational source hashes are refreshed from current bytes and verified against the destination-fill then CFEL application chain.','Links in frozen archive/Journal/projection trees are not parsed or modified; links from eligible referers to those targets preserve the same target path.','Missing relative targets remain unresolved: for moved referers, the href is rebased to the same normalized missing target path and separately counted; no target is inferred.','The plan does not authorize moves; root must re-pin the physical plan and run its separate approved move gate.']
    }
    OUTPUT.write_text(json.dumps(report,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
    print(json.dumps({'status':report['status'],'counts':report['counts'],'output':repo_rel(OUTPUT)},indent=2))


if __name__=='__main__':
    main()
