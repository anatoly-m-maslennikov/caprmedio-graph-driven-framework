"""Read only the Operator-selected captured Core bytes from immutable Git history."""
import hashlib
import json
import pathlib
import subprocess
from functools import lru_cache

ROOT = pathlib.Path(__file__).resolve().parents[5]
COMMIT = "a971d0e00c33c779f485fc8cad63194894d440fb"
BASELINE = ROOT / ".caprmedio_caprmedio/_projection/core-entity-review/baseline.inventory.json"
BASELINE_SHA256 = "bc5d99e91fb7dd4dcb42e59ff33cc24cff1d0901c5904764394c769aaa0a9430"

def sha(raw):
    return hashlib.sha256(raw).hexdigest()

@lru_cache(maxsize=1)
def source_pins():
    raw = BASELINE.read_bytes()
    assert sha(raw) == BASELINE_SHA256, "captured baseline changed"
    return {s["atom_id"]: s for s in json.loads(raw)["source_atoms"]}

@lru_cache(maxsize=None)
def read_source(atom_id):
    pin = source_pins()[atom_id]
    raw = subprocess.run(
        ["git", "show", f"{COMMIT}:{pin['carrier_path']}"],
        cwd=ROOT, check=True, capture_output=True,
    ).stdout
    assert sha(raw) == pin["carrier_sha256"], (atom_id, "captured source mismatch")
    return raw

def verify_snapshot():
    inventory = json.loads(BASELINE.read_bytes())
    pins = list(source_pins().values()) + inventory["excluded_sources"]
    queries = "".join(f"{COMMIT}:{s['carrier_path']}\n" for s in pins).encode()
    raw = subprocess.run(["git", "cat-file", "--batch"], cwd=ROOT,
                         input=queries, check=True, capture_output=True).stdout
    offset = 0
    for s in pins:
        end = raw.index(b"\n", offset)
        header = raw[offset:end].split()
        assert len(header) == 3 and header[1] == b"blob", (s["atom_id"], header)
        size = int(header[2]); offset = end + 1
        blob = raw[offset:offset + size]; offset += size
        assert sha(blob) == s["carrier_sha256"], (s["atom_id"], "snapshot pin mismatch")
        assert raw[offset:offset + 1] == b"\n"; offset += 1
    assert offset == len(raw)
    return {"source_context": "captured_snapshot", "git_commit": COMMIT,
            "source_pins_checked": len(pins), "verification": "pass",
            "current_core_claimed": False}

if __name__ == "__main__":
    print(json.dumps(verify_snapshot(), sort_keys=True))
