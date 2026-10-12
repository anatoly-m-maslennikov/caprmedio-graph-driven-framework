"""Normalize authored review narration only; preserve exact source quotations."""
import argparse
import hashlib
import json
import pathlib
import re
from snapshot_sources import COMMIT

ROOT = pathlib.Path.cwd()
D = ROOT / ".caprmedio_caprmedio/_projection/core-entity-review/nodes"
PATTERNS = [
    (r"\bcurrent Main Content\b", "captured Main Content"),
    (r"\bcurrent(?: pinned| selected| candidate| governing| Core)* source\b", "captured source"),
    (r"\bcurrent Core\b", "captured Core"),
    (r"\bcurrent Claim\b", "captured Claim"),
    (r"\bcurrent pin\b", "captured pin"),
]
FIELDS = {"reason", "question", "finding", "application", "positive_gate"}

def normalize(value, key=None):
    if isinstance(value, dict):
        return {k: normalize(v, k) for k, v in value.items()}
    if isinstance(value, list):
        return [normalize(v, key) for v in value]
    if isinstance(value, str) and key in FIELDS:
        for pattern, replacement in PATTERNS:
            value = re.sub(pattern, replacement, value, flags=re.IGNORECASE)
    return value

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("batches", nargs="+", type=int)
    ap.add_argument("--persist", action="store_true")
    args = ap.parse_args()
    report = []
    for batch in args.batches:
        assert batch in range(9)
        path = D / f"nodes.batch-{batch}.review.json"
        assert not path.is_symlink()
        raw = path.read_bytes(); old = json.loads(raw); new = normalize(old)
        new["review_context"] = {"kind": "captured_snapshot", "git_commit": COMMIT,
                                 "current_core_claimed": False}
        def quotes(x):
            cat = x["evidence_catalogue"]
            return [e["quote"] for e in (cat.values() if isinstance(cat, dict) else cat)]
        assert quotes(old) == quotes(new)
        payload = json.dumps(new, ensure_ascii=False, indent=2, sort_keys=True).encode() + b"\n"
        if args.persist and payload != raw:
            assert path.read_bytes() == raw, "concurrent review changed"
            path.write_bytes(payload)
        report.append({"batch": batch, "sha256": hashlib.sha256(payload).hexdigest(),
                       "quotes_unchanged": True, "outcome": "persisted" if args.persist else "dry_run"})
    print(json.dumps(report, sort_keys=True))

if __name__ == "__main__":
    main()
