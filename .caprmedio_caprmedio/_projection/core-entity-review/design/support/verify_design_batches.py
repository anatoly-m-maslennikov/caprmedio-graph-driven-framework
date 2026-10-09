"""Read-only structural and pin checks for candidate relation batches."""
import argparse
import hashlib
import json
import pathlib
from collections import Counter
ROOT = pathlib.Path.cwd()
DESIGN = ROOT / ".caprmedio_tmp/planning/core-entity-review/design"
BASELINE = ROOT / ".caprmedio_caprmedio/_projection/core-entity-review/baseline.inventory.json"
def sha(raw):
    return hashlib.sha256(raw).hexdigest()
def load(path):
    return json.loads(path.read_bytes())
def canonical(value):
    return json.dumps(value,ensure_ascii=False,sort_keys=True,separators=(",",":")).encode()
def verify_sources(b):
    for source in b["source_atoms"] + b["excluded_sources"]:
        assert sha((ROOT/source["carrier_path"]).read_bytes()) == source["carrier_sha256"], source["atom_id"]
    source = b["registration"]["source"]
    assert sha((ROOT/source["carrier_path"]).read_bytes()) == source["carrier_sha256"]
def verify_evidence(e,pins):
    ref = pins[e["atom_id"]]
    for key in ("atom_revision","carrier_path","carrier_sha256"):
        assert e[key] == ref[key], (e["atom_id"],key)
    raw = (ROOT/ref["carrier_path"]).read_text()
    lines = raw.splitlines()
    start,end = e["start_line"],e["end_line"]
    assert type(start) is int and type(end) is int and 1 <= start <= end <= len(lines)
    frontmatter_end = next(i for i,line in enumerate(lines[1:],2) if line == "---")
    assert start > frontmatter_end, "metadata-only evidence"
    expected = "\n".join(lines[start-1:end])
    quote = e["quote"]
    assert quote in (expected,expected+"\n"), (e["atom_id"],start,end,"quote mismatch")
    assert sha(quote.encode()) == e["text_sha256"], (e["atom_id"],"span hash")
    assert any(heading in raw.splitlines()[:start] for heading in ("## Claim","## Procedure","## Condition","## Operation","## Definition","## Details","## Scope","## Evaluation")), (e["atom_id"],"no Main Content heading before evidence")
def verify_batch(number,input_path=None,output_path=None):
    b = load(BASELINE); verify_sources(b)
    inp = load(input_path or DESIGN / f"batch-{number}.input.json")
    path = output_path or DESIGN / f"relations.batch-{number}.json"
    out = load(path)
    assert out["source_task"] == inp["source_task"]
    assert out["batch_number"] == number
    assert out["baseline_inventory_sha256"] == b["inventory_sha256"]
    assert out["source_binding"] == b["source_binding"]
    assert out["partition_sha256"] == inp["partition_sha256"]
    assert out["non_authoritative"] is True
    assert out["semantic_admission"] == "not_performed"
    assert out["source_migration"] == "not_performed"
    rows = out["cases"]
    assert Counter(r["case_id"] for r in rows) == Counter(r["case_id"] for r in inp["cases"])
    originals = {r["case_id"]:r for r in inp["cases"]}
    pins = {r["atom_id"]:r for r in b["source_atoms"]}
    for r in rows:
        original = originals[r["case_id"]]
        assert r["old_parent"] == original["old_parent"] and r["old_child"] == original["old_child"]
        assert r["disposition"] in ("proposed","unresolved","not-native")
        assert type(r["confidence_percent"]) is int and 0 <= r["confidence_percent"] <= 100
        assert isinstance(r["reason"],str) and r["reason"].strip()
        assert isinstance(r["checks_performed"],list) and r["checks_performed"]
        assert isinstance(r["evidence"],list)
        if r["display_candidate"] if "display_candidate" in r else False:
            assert r["evidence"], "display qualification lacks Main Content evidence"
        if not r["evidence"]:
            assert r["disposition"] == "unresolved", "unevidenced asserted disposition"
            reviewed = r.get("reviewed_candidate_atom_ids", [])
            assert reviewed and all(a in pins for a in reviewed), "missing negative-review source checks"
        for e in r["evidence"]:
            verify_evidence(e,pins)
        if r["disposition"] == "proposed":
            proposal = r["proposal"]
            assert r["confidence_percent"] >= 90 and r["evidence"]
            assert proposal["display_operator"] in ("/",".","@")
            assert proposal["canonical_relation"] == {"/":"NARROWER_THAN",".":"IS_BORNE_BY","@":"IS_CARRIED_BY"}[proposal["display_operator"]]
            assert proposal["qualified_parent"] == r["old_parent"] and proposal["qualified_child"] == r["old_child"]
            assert proposal["native_admission"] == "not_performed"
            assert proposal["graph_kind"] in ("entities","terms","Entities Graph","Terms Graph")
            expected_graph = "terms" if proposal["display_operator"] == "/" else "entities"
            actual = {"Entities Graph":"entities","Terms Graph":"terms"}.get(proposal["graph_kind"],proposal["graph_kind"])
            assert actual == expected_graph, "graph ownership mismatch"
            assert proposal["canonical_direction"] in ("child_to_parent","dependent_to_bearer","narrower_to_broader","entity_to_carrier")
        else:
            assert r["proposal"] is None, "unresolved row asserts native proposal"
            if r["disposition"] == "unresolved":
                assert isinstance(r["question"],str) and r["question"].strip()
    return {"batch":number,"file_sha256":sha(path.read_bytes()),"case_count":len(rows),
            "dispositions":dict(Counter(r["disposition"] for r in rows)),
            "operators":dict(Counter(r["proposal"]["display_operator"] for r in rows if r["proposal"])),
            "evidence_spans":sum(len(r["evidence"]) for r in rows),
            "mechanical_checks":"pass","semantic_acceptance":"not_performed"}
def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("batches",type=int,nargs="+")
    args=parser.parse_args()
    print(json.dumps([verify_batch(n) for n in args.batches],sort_keys=True,indent=2))
if __name__ == "__main__":
    main()
