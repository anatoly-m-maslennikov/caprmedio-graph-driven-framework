"""One-off CA-P-1983 repair of seven exact pinned legacy Tool carriers.

This is not a reusable Atom writer. Default is a read-only preview.
"""
import argparse
from datetime import datetime
import hashlib
import json
from pathlib import Path
import re
from zoneinfo import ZoneInfo


LEGACY_IDS = {"CA-R-863", "CA-E-301", "CA-D-038", "CA-D-424",
              "CA-O-046", "CA-D-041", "CA-D-425"}
ROLES = {"R": "Requirement", "E": "Evaluation", "D": "Delivery", "O": "Operations"}
BASE = Path(".caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS")
REPORT = Path(".caprmedio_caprmedio/_projection/core-entity-review/stage2/tool-rmedo-review.md")


def prepare(root, stamp):
    proposals = []
    rows = (line.split("|")[1:-1] for line in (root / REPORT).read_text().splitlines()
            if line.startswith("| CA-"))
    for row in rows:
        atom_id, old_version, relative, expected = (value.strip() for value in row)
        if atom_id not in LEGACY_IDS:
            continue
        path = root / BASE / relative
        if path.is_symlink() or not path.resolve().is_relative_to((root / BASE).resolve()):
            raise ValueError(f"Unsafe legacy source: {relative}")
        before = path.read_bytes()
        if hashlib.sha256(before).hexdigest() != expected:
            raise ValueError(f"Stale legacy source: {atom_id}")
        text = before.decode("utf-8")
        frontmatter, body = text[4:].split("\n---\n", 1)
        if not text.startswith("---\n") or re.search(r"^atom_id:", frontmatter, re.M):
            raise ValueError(f"Not the expected legacy carrier: {atom_id}")
        match = re.fullmatch(r"# ([^\n]+)\n(.*)", body, re.S)
        if not match or match.group(1) == "Summary":
            raise ValueError(f"Unexpected legacy title: {atom_id}")
        new_version = int(old_version) + 1
        frontmatter, count = re.subn(r"^version: \d+$", f"version: {new_version}", frontmatter, flags=re.M)
        if count != 1:
            raise ValueError(f"Invalid Version carrier: {atom_id}")
        frontmatter, count = re.subn(r"^updated_at:.*$", f'updated_at: "{stamp}"', frontmatter, flags=re.M)
        if count != 1:
            raise ValueError(f"Invalid updated_at carrier: {atom_id}")
        role = ROLES[atom_id.split("-")[1]]
        metadata = (f"atom_id: {atom_id}\ncontent_role: {role}\n"
                    + ("type: Action\n" if role == "Operations" else "")
                    + "current_scope_unit: TOOLS\nclaim_target_scope_unit: TOOLS\n"
                    "local_tier: Standard\nglobal_tier: 11\n"
                    "author: Anatoly Maslennikov\nstatus: Active\n")
        after = ("---\n" + metadata + frontmatter + "\n---\n# Summary\n\n"
                 + match.group(1) + "\n" + match.group(2)).encode("utf-8")
        proposals.append((path, before, after, {"atom_id": atom_id,
            "path": str(BASE / relative), "before_sha256": expected,
            "after_sha256": hashlib.sha256(after).hexdigest(),
            "before_version": int(old_version), "after_version": new_version}))
    if {item[3]["atom_id"] for item in proposals} != LEGACY_IDS or len(proposals) != 7:
        raise ValueError("The exact seven-carrier repair inventory is missing or duplicated")
    return proposals


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path.cwd())
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()
    root = args.root.resolve()
    stamp = datetime.now(ZoneInfo("Asia/Tbilisi")).strftime("%Y-%m-%d %H:%M:%S %z")
    proposals = prepare(root, stamp)
    if args.apply:
        # Validate every source before the first effect. Git retains prior contents.
        for path, before, _, _ in proposals:
            if path.read_bytes() != before:
                raise ValueError(f"Source changed during preview: {path}")
        for path, _, after, _ in proposals:
            path.write_bytes(after)
    print(json.dumps({"task": "CA-P-1983", "applied": args.apply,
        "updated_at": stamp, "timestamp_is_illustrative": not args.apply,
        "files": [item[3] for item in proposals]}, indent=2))


if __name__ == "__main__":
    main()
