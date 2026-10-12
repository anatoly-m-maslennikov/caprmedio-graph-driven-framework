"""Prepare sealed disjoint review batches; no semantic classification or source writes."""
import hashlib
import json
import pathlib
from collections import Counter

REPOSITORY = pathlib.Path.cwd()
BASELINE = REPOSITORY / ".caprmedio_caprmedio/_projection/core-entity-review/baseline.inventory.json"
OLD = REPOSITORY / ".caprmedio_tmp/planning/core-subject-notation/inventory.json"
OUTPUT = REPOSITORY / ".caprmedio_tmp/planning/core-entity-review/design"
def digest(raw):
    return hashlib.sha256(raw).hexdigest()
def canonical(value):
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode()
def write_new(path, value):
    raw = json.dumps(value, ensure_ascii=False, sort_keys=True, indent=2).encode() + b"\n"
    if path.exists():
        assert path.read_bytes() == raw, f"existing output differs: {path}"
    else:
        with path.open("xb") as handle:
            handle.write(raw)
    return digest(raw)
def main():
    b = json.loads(BASELINE.read_bytes())
    old = json.loads(OLD.read_bytes())
    assert digest(BASELINE.read_bytes()) == "bc5d99e91fb7dd4dcb42e59ff33cc24cff1d0901c5904764394c769aaa0a9430"
    assert digest(OLD.read_bytes()) == "4d3eaeef9170fb372d629741997b782945445e32da60a6e05fad3c0cdc700d7a"
    assert digest(canonical({k:v for k,v in b.items() if k != "inventory_sha256"})) == b["inventory_sha256"]
    for ref in b["source_atoms"] + b["excluded_sources"]:
        assert digest((REPOSITORY / ref["carrier_path"]).read_bytes()) == ref["carrier_sha256"], ref["atom_id"]
    pairs = {(r["original_qualified_parent"], r["original_qualified_child"]) for r in b["relation_segment_inventory"] if r["source_separator"] == "/"}
    assert len(pairs) == 294
    cases = sorted(old["cases"], key=lambda r:r["case_id"])
    assert {(r["old_parent"], r["old_child"]) for r in cases} == pairs
    assert len({r["case_id"] for r in cases}) == 294
    sources = {r["atom_id"]:r for r in b["source_atoms"]}
    for case in cases:
        for row in case["occurrences"]:
            ref = row["source_ref"]
            assert sources[ref["atom_id"]]["carrier_sha256"] == ref["carrier_sha256"]
    buckets = {n:sorted([r for r in cases if r["bucket"] == n], key=lambda r:r["case_id"]) for n in (1,2,3)}
    assert {n:len(rows) for n,rows in buckets.items()} == {1:141,2:22,3:131}
    partitions = [buckets[1][:47], buckets[1][47:94], buckets[1][94:], buckets[2], buckets[3][:66], buckets[3][66:]]
    assert Counter(r["case_id"] for rows in partitions for r in rows) == Counter(r["case_id"] for r in cases)
    OUTPUT.mkdir(parents=True, exist_ok=True)
    pins = []
    for number, rows in enumerate(partitions,1):
        used_ids = {r["source_ref"]["atom_id"] for case in rows for r in case["occurrences"]}
        used_ids.update(a for case in rows for a in case["content_source_candidates"] if a in sources)
        payload = {
            "schema_version":1, "projection_kind":"caprmedio.core_graph_design.review_partition",
            "source_task":f"CA-P-{1912+number}", "non_authoritative":True,
            "semantic_admission":"not_performed", "source_migration":"not_performed",
            "baseline_path":str(BASELINE.relative_to(REPOSITORY)),
            "baseline_file_sha256":digest(BASELINE.read_bytes()), "baseline_inventory_sha256":b["inventory_sha256"],
            "source_binding":b["source_binding"], "legacy_case_inventory_sha256":digest(OLD.read_bytes()),
            "sort_rule":"case_id lexicographic within original bucket",
            "batch_number":number, "case_count":len(rows), "cases":rows,
            "current_source_pins":[sources[a] for a in sorted(used_ids)],
            "confidence_threshold_percent":90
        }
        payload["partition_sha256"] = digest(canonical(payload))
        path = OUTPUT / f"batch-{number}.input.json"
        pins.append({"path":str(path.relative_to(REPOSITORY)), "file_sha256":write_new(path,payload),
                     "partition_sha256":payload["partition_sha256"], "source_task":payload["source_task"],
                     "case_count":len(rows), "case_ids":[r["case_id"] for r in rows]})
    manifest = {"schema_version":1, "source_task":"CA-P-1906", "non_authoritative":True,
                "baseline_inventory_sha256":b["inventory_sha256"], "partitions":pins, "total_cases":294,
                "source_binding":b["source_binding"], "no_semantic_classification":True}
    manifest["manifest_sha256"] = digest(canonical(manifest))
    write_new(OUTPUT / "partition.manifest.json", manifest)
    print(json.dumps({"outcome":"verified", "total_cases":294, "batch_counts":[len(x) for x in partitions],
                      "manifest_sha256":manifest["manifest_sha256"]}))
if __name__ == "__main__":
    main()
