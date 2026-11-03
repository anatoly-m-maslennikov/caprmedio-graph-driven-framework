#!/usr/bin/env python3
"""Byte-preserving root namespace migration for an explicit Atom file list."""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import stat
import sys
import tempfile
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[4]
TOOLS = ROOT / "LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_TOOLS"
sys.path.insert(0, str(TOOLS))
from atom_operations import atom_identity_lock  # noqa: E402

OLD = {"CAPRMEDIO <+ MODEL": "CAPRMEDIO_MODEL", "CAPRMEDIO <+ STRUCTURE": "CAPRMEDIO_STRUCTURE"}


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def transform(raw: bytes) -> bytes:
    text = raw.decode("utf-8")
    delimiters = list(re.finditer(r"(?m)^---[ \t]*(?:\r?\n|$)", text))
    if len(delimiters) < 2 or delimiters[0].start() != 0:
        raise ValueError("expected YAML frontmatter")
    start, end = delimiters[0].end(), delimiters[1].start()
    fm = text[start:end]
    root = yaml.compose(fm, Loader=yaml.SafeLoader)
    yaml.safe_load(fm)  # Reject malformed or unsupported YAML before any write.
    if not isinstance(root, yaml.nodes.MappingNode):
        raise ValueError("frontmatter must be a mapping")
    subjects = [v for k, v in root.value if isinstance(k, yaml.nodes.ScalarNode) and k.value == "subjects"]
    if len(subjects) > 1:
        raise ValueError("duplicate subjects key")
    if not subjects:
        return raw
    node = subjects[0]
    if not isinstance(node, yaml.nodes.MappingNode):
        raise ValueError("subjects must be a mapping")
    edits: list[tuple[int, int, str]] = []
    for key, value in node.value:
        if not isinstance(key, yaml.nodes.ScalarNode) or key.value not in {"active", "passive"}:
            continue
        values = value.value if isinstance(value, yaml.nodes.SequenceNode) else [value]
        for scalar in values:
            if not isinstance(scalar, yaml.nodes.ScalarNode):
                raise ValueError("active/passive subjects must contain only scalars")
            if scalar.tag != "tag:yaml.org,2002:str":
                continue
            old = next((p for p in OLD if scalar.value == p or scalar.value.startswith(p + " ")), None)
            if old:
                raw_scalar = fm[scalar.start_mark.index:scalar.end_mark.index]
                if not raw_scalar.strip():
                    raise ValueError("unsupported empty scalar representation")
                edits.append((scalar.start_mark.index, scalar.end_mark.index, raw_scalar.replace(old, OLD[old], 1)))
    for a, b, replacement in sorted(edits, reverse=True):
        fm = fm[:a] + replacement + fm[b:]
    return (text[:start] + fm + text[end:]).encode("utf-8")


def atomic_replace(path: Path, data: bytes) -> None:
    mode = stat.S_IMODE(path.stat().st_mode)
    descriptor, temp_name = tempfile.mkstemp(dir=path.parent, prefix=f".{path.name}.")
    try:
        with os.fdopen(descriptor, "wb") as stream:
            stream.write(data)
            stream.flush()
            os.fsync(stream.fileno())
        os.chmod(temp_name, mode)
        os.replace(temp_name, path)
    finally:
        if os.path.exists(temp_name):
            os.unlink(temp_name)


def apply_records(records: list[dict]) -> int:
    pending = []
    for row in records:
        path = Path(row["path"])
        raw = path.read_bytes()
        current = digest(raw)
        if current == row["after_sha256"]:
            continue
        if current != row["before_sha256"]:
            raise ValueError(f"concurrent drift: {path}")
        candidate = row["candidate"].encode("utf-8")
        if digest(candidate) != row["after_sha256"] or transform(raw) != candidate:
            raise ValueError(f"invalid plan candidate: {path}")
        pending.append((path, raw, candidate, row["after_sha256"]))
    written = []
    with atom_identity_lock(ROOT):
        try:
            for path, before, candidate, after_hash in pending:
                if digest(path.read_bytes()) != digest(before):
                    raise ValueError(f"concurrent drift before replace: {path}")
                atomic_replace(path, candidate)
                written.append((path, before, after_hash))
        except BaseException:
            for path, before, after_hash in reversed(written):
                try:
                    if digest(path.read_bytes()) == after_hash:
                        atomic_replace(path, before)
                except OSError:
                    pass
            raise
    return len(written)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    plan = sub.add_parser("plan", help="create a hash-pinned plan from explicit files")
    plan.add_argument("--manifest", required=True, type=Path)
    plan.add_argument("files", nargs="+", type=Path)
    apply = sub.add_parser("apply", help="apply a plan after validating every file hash")
    apply.add_argument("manifest", type=Path)
    args = parser.parse_args()
    if args.command == "plan":
        records = []
        for path in args.files:
            raw = path.read_bytes()
            candidate = transform(raw)
            records.append({"path": str(path), "before_sha256": digest(raw), "after_sha256": digest(candidate), "candidate": candidate.decode("utf-8")})
        args.manifest.write_text(json.dumps({"records": records}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(f"planned {len(records)} explicit files: {args.manifest}")
    else:
        records = json.loads(args.manifest.read_text(encoding="utf-8"))["records"]
        print(f"applied {apply_records(records)} files")


if __name__ == "__main__":
    main()
