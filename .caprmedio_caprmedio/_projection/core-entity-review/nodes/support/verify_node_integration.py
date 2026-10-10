"""Independent, read-only CA-P-1938 integration checks (captured Core only).

Run from the repository root with uv/python -B. No persistence option exists.
The original RMED producer is replayed only with captured source reads and all
output writes intercepted. Its historical wording is preserved, not promoted
to a claim that today's Core matches the captured frontier.
"""

from __future__ import annotations

import collections
import hashlib
import importlib.util
import json
import re
import subprocess
import sys
import tomllib
import types
from pathlib import Path
from unittest import mock

ROOT = Path.cwd().resolve()
BASE = ROOT / ".caprmedio_caprmedio/_projection/core-entity-review"
NODES = BASE / "nodes"
DESIGN = BASE / "design"
CORE_COMMIT = "a971d0e00c33c779f485fc8cad63194894d440fb"
RECEIPT_COMMIT = "67d83ebaeeeae6cd2c2e260947c8ffc926d7a329"
INTEGRATION_COMMIT = "4f5850845a1a99ddf6bb620f9cb198181d682a53"
HASHES = {
    "nodes.dispositions.json": "1b9d751f95aa71486908b53b3d7f3f9825defae137be3d8792d45177587c48f8",
    "relations.marked.ledger.json": "f6efdcaddfbbb4d9f4607084ee77ca83c75de2566fd9506da51dac2493e02371",
    "candidate.structure.marked.json": "04f2b8d3606ac30b74850ab9ff53ebebfcbcffd1cda1e5ad2d948662c085e34b",
}
PRODUCER_SHA = "9f53c3bdeb5987522d2345cda2c8441f58b6903af9da8c198f2f91c67355a178"
ORIGINAL_HASHES = {
    "relations.ledger.json": "6ec53f14e64280815e5f57f8d00598913bc26b342102ca3acce5a7f4221d10bd",
    "candidate.structure.json": "eda055c887706454cfd2d52bee7196a818e8eb0b8e1710d587fcfc4ffa8d9071",
}
CHECK_NAMES = {"duplicates", "redundancy", "empty_definition", "distinct_meaning", "generalization"}


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def canonical(value):
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"), allow_nan=False).encode()


def require(condition, label):
    if not condition:
        raise AssertionError(label)


def git_bytes(commit, path):
    return subprocess.check_output(["git", "show", f"{commit}:{path}"], cwd=ROOT)


def tree(commit):
    return subprocess.check_output(["git", "ls-tree", "-r", "--name-only", commit], cwd=ROOT, text=True).splitlines()


def scalar(raw, key):
    text = raw.decode(); require(text.startswith("---\n"), "Plan frontmatter")
    end = text.index("\n---", 4)
    values = re.findall(rf"^{re.escape(key)}:\s*(.*?)\s*$", text[4:end], re.MULTILINE)
    require(len(values) == 1, f"single Plan {key}")
    return values[0].strip().strip("\"'")


def unique_plan(paths, atom_id):
    found = [p for p in paths if p.endswith(".md") and f"-{atom_id}-" in Path(p).name and "/archive/" not in p]
    require(len(found) == 1, f"unique Plan locator {atom_id}")
    return found[0]


def subset(original, marked, where="root"):
    """Every original key/value survives; additions are checked separately."""
    if isinstance(original, dict):
        require(isinstance(marked, dict), where)
        for key, value in original.items():
            require(key in marked, f"missing {where}.{key}")
            subset(value, marked[key], f"{where}.{key}")
    elif isinstance(original, list):
        require(isinstance(marked, list) and len(original) == len(marked), f"array size {where}")
        for index, (left, right) in enumerate(zip(original, marked)):
            subset(left, right, f"{where}[{index}]")
    else:
        require(type(original) is type(marked) and original == marked, f"original value changed {where}")


def load_module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def main():
    watched = {}
    observed_live_core = {}

    def read_only_audit(event, args):
        if event == "open":
            path, mode, flags = args
            if isinstance(path, int):  # subprocess pipes, not filesystem paths
                return
            require(not (isinstance(mode, str) and any(c in mode for c in "wax+")), "read-only verifier forbids file writes")
            require(not (isinstance(flags, int) and flags & 3), "read-only verifier forbids writable file descriptors")

    sys.addaudithook(read_only_audit)

    def read(path, expected=None):
        raw = path.read_bytes(); watched[path] = raw
        if expected:
            require(sha(raw) == expected, f"frozen SHA {path.name}")
        return json.loads(raw)

    baseline = read(BASE / "baseline.inventory.json", "bc5d99e91fb7dd4dcb42e59ff33cc24cff1d0901c5904764394c769aaa0a9430")
    require(sha(canonical({k: v for k, v in baseline.items() if k != "inventory_sha256"})) == baseline["inventory_sha256"], "inventory canonical SHA")
    packet, ledger, candidate = [read(NODES / name, HASHES[name]) for name in HASHES]
    old_ledger, old_candidate = [read(DESIGN / name, ORIGINAL_HASHES[name]) for name in ORIGINAL_HASHES]
    subset(old_ledger, ledger, "ledger"); subset(old_candidate, candidate, "candidate")
    require(set(ledger) - set(old_ledger) == {"integration_checks", "native_admission", "node_review_integration", "node_review_prerequisite_pins", "source_review"}, "only declared ledger additions")
    require(set(candidate) - set(old_candidate) == {"integration_checks", "marked_relation_ledger_ref", "native_admission", "node_dispositions_ref", "node_review_prerequisite_pins", "pinned_node_marks", "source_context", "source_context_pins"}, "only declared candidate additions")
    require(len(ledger["original_occurrences"]) == 4534 and len(ledger["original_segments"]) == 3093, "preserved incidence")
    require(collections.Counter(s["source_separator"] for s in ledger["original_segments"]) == {"/": 2275, ":": 818}, "original separators")
    require(ledger["original_occurrences"] == baseline["occurrences"] and ledger["original_nodes"] == baseline["nodes"], "baseline objects preserved")

    snapshot = load_module("acceptance_snapshot_sources", NODES / "support/snapshot_sources.py")
    # Share the unmodified reader and its exact-byte cache with the producer;
    # alias loading changes neither executed source nor the serialized proof.
    sys.modules.setdefault("snapshot_sources", snapshot)
    result = snapshot.verify_snapshot()
    require(result["source_pins_checked"] == 951 and result["git_commit"] == CORE_COMMIT and result["current_core_claimed"] is False, "historical source context")
    pins = snapshot.source_pins()
    registration = baseline["registration"]
    structure_raw = git_bytes(CORE_COMMIT, registration["source"]["carrier_path"])
    require(sha(structure_raw) == registration["source"]["carrier_sha256"], "captured Project Structure pin")
    core_records = [r for r in tomllib.loads(structure_raw.decode())["scope_units"] if r["scope_unit_name"] == "CORE_META_MODEL"]
    require(len(core_records) == 1 and core_records[0]["authority_path"] == registration["authority_path"], "captured registered Core authority path")
    require(baseline["source_binding"]["source_frontier_sha256"] == "7792e842cfe6c66320745660e69cd0df5525ec18bb22b5c060a6ddfff5fc97f7", "historical sealed frontier")
    require(len(pins) == 908 and len(baseline["excluded_sources"]) == 43 and set(baseline["selection"]["atom_ids"]) == set(pins), "exact captured selection")
    # Watch current files for nonmutation only; never require their bytes to be
    # the historical bytes. A later Core revision is explicitly outside scope.
    for pin in list(pins.values()) + baseline["excluded_sources"]:
        path = ROOT / pin["carrier_path"]
        if path.is_file():
            observed_live_core[path] = path.read_bytes()
    evidence_checks = 0
    contribution_checks = set()

    def evidence(item):
        nonlocal evidence_checks
        pin = pins[item["atom_id"]]
        require(all(item[k] == pin[k] for k in ("atom_revision", "carrier_path", "carrier_sha256")), "Main Content source pin")
        lines = snapshot.read_source(item["atom_id"]).decode().splitlines()
        start, end = item["start_line"], item["end_line"]
        require(type(start) is int and type(end) is int and 1 <= start <= end <= len(lines), "Main Content coordinates")
        fm_end = next(i for i, line in enumerate(lines[1:], 2) if line == "---")
        require(start > fm_end, "not frontmatter evidence")
        quote = "\n".join(lines[start - 1:end])
        require(item["quote"] in (quote, quote + "\n") and sha(item["quote"].encode()) == item["text_sha256"], "exact Main Content quotation")
        heads = [x for x in lines[:start] if x.startswith(("# ", "## ", "### "))]
        require(heads and not heads[-1].startswith("# Summary"), "not Summary-only evidence")
        evidence_checks += 1

    def contribution(ref):
        pin = pins[ref["atom_id"]]
        require(all(ref[k] == pin[k] for k in ("atom_revision", "carrier_path", "carrier_sha256")), "Subjects pin")
        c = ref["contribution"]; raw = snapshot.read_source(ref["atom_id"])
        span = b"".join(raw.splitlines(keepends=True)[c["start_line"] - 1:c["end_line"]])
        require(sha(span) == c["text_sha256"], "raw original-EOL Subjects contribution")
        require(c["kind"] == "canonical_atom_property" and c["property_path"] in {"subjects.governs", "subjects.depends_on"}, "canonical Subjects contribution")
        contribution_checks.add((ref["atom_id"], c["property_path"], c["start_line"], c["end_line"]))

    for occurrence in ledger["original_occurrences"]:
        contribution(occurrence["source_ref"])
    for segment in ledger["original_segments"]:
        contribution(segment["source_ref"])
    for case in ledger["case_reviews"]:
        for item in case["evidence"]:
            evidence(item)
    for item in ledger["additional_relations"]["evidence_catalogue"].values():
        evidence(item)

    marks = packet["node_disposition_marks"]
    require(len(marks) == 706 and len({m["identity"] for m in marks}) == 706, "706 distinct marks")
    by_identity = {m["identity"]: m for m in marks}
    require(set(by_identity) == {n["identity"] for n in baseline["nodes"]}, "exact baseline identity coverage")
    reviews = {}; expected_catalogue = {}; question_count = 0; fallbacks = 0
    receipt_paths = tree(RECEIPT_COMMIT)
    for batch in range(9):
        path = NODES / f"nodes.batch-{batch}.review.json"; review = read(path)
        rel = path.relative_to(ROOT).as_posix()
        require(git_bytes(RECEIPT_COMMIT, rel) == watched[path], f"committed final review {batch}")
        inp_path = NODES / f"inputs/nodes.batch-{batch}.input.json"; inp = read(inp_path)
        require(review["input_file_sha256"] == sha(watched[inp_path]), "input file binding")
        require(review["partition_sha256"] == inp["partition_sha256"] == sha(canonical({k: v for k, v in inp.items() if k != "partition_sha256"})), "partition binding")
        require(review["source_task"] == inp["source_task"] == f"CA-P-{1928 + batch}", "original review task")
        expected_nodes = {n["identity"]: n for n in inp["nodes"]}
        require(set(expected_nodes) == {r["identity"] for r in review["nodes"]} and len(expected_nodes) == len(review["nodes"]), "partition coverage")
        catalogue = review["evidence_catalogue"]
        if isinstance(catalogue, list):
            catalogue = {item["evidence_ref"]: item for item in catalogue}
        for local, item in catalogue.items():
            global_ref = f"{review['source_task']}/batch-{batch}/{local}"
            require(global_ref not in expected_catalogue, "namespaced catalogue collision")
            expected_catalogue[global_ref] = item; evidence(item)
        for row in review["nodes"]:
            mark = by_identity[row["identity"]]
            require(mark["review_row"] == row and mark["canonical_row_sha256"] == sha(canonical(row)), "exact nested review row/hash")
            require(mark["node_disposition_id"] == "node-disposition:" + sha(row["identity"].encode()), "stable node disposition ID")
            require(set(row["checks"]) == CHECK_NAMES and all(c.get("finding") and c.get("reason") for c in row["checks"].values()), "five substantive check fields")
            local_refs = list(dict.fromkeys([str(r) for r in row["evidence_refs"]] + [str(r) for c in row["checks"].values() for r in c.get("evidence_refs", [])]))
            require(all(r in catalogue for r in local_refs), "all row/check references closed")
            global_refs = [f"{review['source_task']}/batch-{batch}/{r}" for r in local_refs]
            scoped = mark["scoped_refs"]
            require(scoped["task"] == review["source_task"] and scoped["batch"] == batch and scoped["local_refs"] == local_refs and scoped["global_evidence_refs"] == global_refs, "scoped exact evidence refs")
            expected_occ = row.get("input_occurrence_ids", expected_nodes[row["identity"]]["occurrence_ids"])
            require(scoped["input_occurrence_ids"] == expected_occ and expected_occ, "incidence not silently empty")
            fallbacks += "input_occurrence_ids" not in row
            if "segment_ids" in row:
                require(scoped["segment_ids"] == row["segment_ids"], "scoped segment IDs")
            require(mark["source_review"] == {"source_context": "captured_snapshot", "git_commit": CORE_COMMIT, "checked_source_atom_ids": row["checked_source_atom_ids"], "evidence_refs": global_refs}, "mark source scope")
            for atom_id in row["checked_source_atom_ids"]:
                snapshot.read_source(atom_id)
            if row["disposition"] == "question":
                require(row["question"] and row["proposal"] is None, "unresolved has specific question/no proposal")
                question_count += 1
            else:
                require(row["confidence_percent"] >= 90 and row["evidence_refs"], "positive evidence gate")
            if row["disposition"] in {"consolidate", "generalize"}:
                prop = row["proposal"]
                require(prop["adoption"] == "not_performed" and prop["replacement_identity"] is None and prop["preserved_distinctions"] and prop["lost_distinctions_risk"], "reduction is candidate and preserves distinctions")
                require(all(prop.get(k) for k in ("relations_effect", "constraints_effect", "historical_references_effect", "queries_effect")), "documented reduction effects")
        receipt = packet["review_receipts"][str(batch)]
        require(receipt["receipt_commit"] == RECEIPT_COMMIT and receipt["review_captured_path"] == rel and receipt["review_sha256"] == sha(watched[path]), "review receipt binding")
        checked_receipt = packet["review_set"]["batches"][batch]["receipt"]
        require(checked_receipt == {**receipt, "live_review_hash_checked": True}, "batch report records performed live-byte check")
        plan_raw = git_bytes(RECEIPT_COMMIT, receipt["plan_captured_path"])
        require(sha(plan_raw) == receipt["plan_sha256"] and scalar(plan_raw, "atom_id") == receipt["plan_atom_id"] and scalar(plan_raw, "status") == "Done", "final review completion receipt")
        require(receipt["review_sha256"] in plan_raw.decode(), "review SHA in Done receipt")
        reviews[batch] = review
    require(packet["evidence_catalogue"] == expected_catalogue and len(expected_catalogue) == 836, "exact namespaced evidence catalogue")
    require(collections.Counter(m["review_row"]["disposition"] for m in marks) == {"retain": 584, "consolidate": 3, "generalize": 2, "question": 117}, "final distribution")
    require(question_count == 117 and len(packet["unresolved_drop_annotations"]) == 2, "questions/drop annotations remain unresolved")

    for segment, original in zip(ledger["original_segments"], old_ledger["original_segments"]):
        require(set(segment) - set(original) == {"endpoint_annotations", "node_disposition_ids", "native_relation_inferred"}, "only segment annotations added")
        ids = []
        for endpoint, field, annotation in zip(("parent", "child"), ("original_qualified_parent", "original_qualified_child"), segment["endpoint_annotations"]):
            mark = by_identity[segment[field]]; ids.append(mark["node_disposition_id"])
            require(annotation == {"endpoint": endpoint, "node_identity": segment[field], "node_disposition_id": mark["node_disposition_id"], "disposition": mark["review_row"]["disposition"], "canonical_row_sha256": mark["canonical_row_sha256"], "native_relation_inferred": False, "semantic_admission": "not_performed"}, "exact closed endpoint annotation")
        require(len(segment["endpoint_annotations"]) == 2 and segment["node_disposition_ids"] == ids and segment["native_relation_inferred"] is False, "two nonnative endpoint marks")
    expected_marks = [{"identity": m["identity"], "node_disposition_id": m["node_disposition_id"], "canonical_row_sha256": m["canonical_row_sha256"], "disposition": m["review_row"]["disposition"], "confidence_percent": m["review_row"]["confidence_percent"], "native_admission": "not_performed"} for m in marks]
    require(candidate["pinned_node_marks"] == expected_marks, "candidate exact marks")
    require(candidate["node_dispositions_ref"]["sha256"] == HASHES["nodes.dispositions.json"] and candidate["marked_relation_ledger_ref"]["sha256"] == HASHES["relations.marked.ledger.json"], "additive artifact links")

    live_plans = [p.relative_to(ROOT).as_posix() for p in (ROOT / ".caprmedio_caprmedio/03_plan").rglob("*.md")]
    prereqs = packet["prerequisite_completion_pins"]
    require({p["atom_id"] for p in prereqs} == {f"CA-P-{i}" for i in range(1928, 1937)} | {f"CA-P-{i}" for i in range(1952, 1957)}, "14 exact prerequisites")
    for pin in prereqs:
        loc = pin["captured_locator"]
        require(loc["git_commit"] == RECEIPT_COMMIT and loc["path"] == unique_plan(receipt_paths, pin["atom_id"]), "stable captured Plan locator")
        captured = git_bytes(RECEIPT_COMMIT, loc["path"])
        current_path = ROOT / unique_plan(live_plans, pin["atom_id"]); watched[current_path] = current_path.read_bytes()
        require(watched[current_path] == captured and sha(captured) == pin["carrier_sha256"] and scalar(captured, "atom_id") == pin["atom_id"] and scalar(captured, "status") == "Done" and int(scalar(captured, "version")) == pin["version"], "current Done Plan identity/hash/version")
    require(ledger["node_review_prerequisite_pins"] == candidate["node_review_prerequisite_pins"] == prereqs, "shared prerequisite pins")
    plan1937 = ROOT / unique_plan(live_plans, "CA-P-1937"); watched[plan1937] = plan1937.read_bytes()
    require(scalar(watched[plan1937], "status") == "Done", "1937 start gate Done")
    require(watched[plan1937] == git_bytes(INTEGRATION_COMMIT, unique_plan(tree(INTEGRATION_COMMIT), "CA-P-1937")), "1937 Done move does not change captured bytes")
    for batch in (0, 3):
        repair = reviews[batch]["review_repair_provenance"]; prior = repair["prior_review"]
        prior_raw = git_bytes(prior["git_commit"], prior["path"]); require(sha(prior_raw) == prior["sha256"], "historical pre-repair packet")
        prior_packet = json.loads(prior_raw); changed = set(repair["corrected_identities"])
        require(all(a == b for a, b in zip(reviews[batch]["nodes"], prior_packet["nodes"]) if a["identity"] not in changed), "unaffected historical rows preserved")
        require(sha(canonical(repair["prior_review_row"])) == repair["prior_row_canonical_sha256"], "historical changed-row proof")
        if batch == 3:
            require(reviews[batch]["post_join_correction"]["current_packet_is_original_join_verbatim"] is False, "postjoin correction is not original join reproduction")
            require(reviews[batch]["child_review_provenance"] == prior_packet["child_review_provenance"] and reviews[batch]["child_verifications"] == prior_packet["child_verifications"], "historical child join preserved")
    for document in (packet, ledger, candidate):
        require(document["semantic_admission"] == document["source_migration"] == document["Operator_acceptance"] == "not_performed" and document["non_authoritative"] is True, "no adoption/admission/migration")
    context = packet["source_context"]
    require(context["git_commit"] == CORE_COMMIT and context["current_core_claimed"] is False and context["source_pins_checked"] == 951, "no live Core claim")
    require(candidate["source_context"] == ledger["source_review"]["snapshot_context"] == context, "common historical context")
    for pin in packet["source_context_pins"]:
        path = ROOT / pin["path"]; watched[path] = path.read_bytes()
        require(sha(watched[path]) == pin["sha256"] and pin["not_core_evidence"] is True, "separate Operator/context pins")
    scope = next(p for p in packet["source_context_pins"] if p["kind"] == "operator_scope_omission_direction")
    require(scope["sha256"] == "d4ea636d540b0558c1a0fbb8263760947e1f0768840c43b3ed1d05c96b497453", "latest Scope default binding")

    views = read(DESIGN / "rmed.views.json", ledger["shared_RMED_views"]["input_pin"]["sha256"])
    role_map = {"Requirement": "R", "Method": "M", "Evaluation": "E", "Delivery": "D"}
    expected = collections.Counter()
    for occurrence in baseline["occurrences"]:
        ref = occurrence["source_ref"]; role = pins[ref["atom_id"]]["content_role"]
        if role in role_map:
            key = f"{ref['atom_id']}@{ref['atom_revision']}:{ref['carrier_sha256']}"
            expected[(role_map[role], occurrence["role"], occurrence["subject_path"], key, canonical(ref["contribution"]))] += 1
    actual_role = collections.Counter(); actual_entity = collections.Counter()
    for view in views["role_centered_overview"]["role_trees"]:
        for name, role in (("governing_claim_pointers", "GOVERNS"), ("dependency_pointers", "DEPENDS_ON")):
            for pointer in view[name]:
                require(pointer["subject_pointer_role"] == role and pointer["rmed_role"] == view["rmed_role"], "RMED separated channels")
                actual_role[(view["rmed_role"], role, pointer["target_identity"], pointer["source_ref_key"], canonical(pointer["source_ref"]["contribution"]))] += 1
    for view in views["entity_centered_view"]["entities"]:
        for name, role in (("governing_claim_pointers_by_rmed_role", "GOVERNS"), ("dependency_pointers_by_rmed_role", "DEPENDS_ON")):
            for rmed, pointers in view[name].items():
                for pointer in pointers:
                    actual_entity[(rmed, role, view["entity_identity"], pointer["source_ref_key"], canonical(pointer["source_ref"]["contribution"]))] += 1
        require(view["optional_M_E_D_governing_links"] == {r: v for r, v in view["governing_claim_pointers_by_rmed_role"].items() if r in "MED" and v}, "optional pointer links not applicability")
    require(expected == actual_role == actual_entity and sum(expected.values()) == 3649 and len(views["source_catalog"]) == 805 and len(views["entity_centered_view"]["entities"]) == 580, "both RMED pointer views")
    # Reproduce legacy renderings at the original producer location, with
    # captured reads substituted and every write intercepted in memory.
    legacy_path = ROOT / ".caprmedio_tmp/planning/core-entity-review/design/build_rmed_views_ca_p_1920.py"
    archived = DESIGN / "support/build_rmed_views_ca_p_1920.py"; watched[archived] = archived.read_bytes()
    legacy_raw = watched[archived]
    require(sha(legacy_raw) == "8d3f12653075ccfe6710d983dd206c8ff6ddf22920f3dcb0fdd2e4af33fbc75f", "archived RMED producer identity")
    if legacy_path.is_file():
        watched[legacy_path] = legacy_path.read_bytes()
        require(watched[legacy_path] == legacy_raw, "optional original RMED source copy")
    legacy = types.ModuleType("acceptance_rmed_producer")
    legacy.__file__ = str(legacy_path)  # virtual routing location, not a file dependency
    exec(compile(legacy_raw, str(legacy_path), "exec"), legacy.__dict__)
    historical_paths = {ROOT / p["carrier_path"]: aid for aid, p in pins.items()}
    original_read = Path.read_bytes; original_is_file = Path.is_file; captured_outputs = {}

    def captured_read(path):
        return snapshot.read_source(historical_paths[path]) if path in historical_paths else original_read(path)

    def captured_is_file(path):
        return True if path in historical_paths else original_is_file(path)

    def capture_write(path, text, *args, **kwargs):
        require(path.parent == legacy_path.parent and path.name in {"rmed.views.json", "rmed.views.md", "rmed.roles.indented.txt", "rmed.entities.indented.txt"}, "only known RMED output requests")
        captured_outputs[path.name] = text.encode(); return len(text)

    with mock.patch.object(Path, "read_bytes", captured_read), mock.patch.object(Path, "is_file", captured_is_file), mock.patch.object(Path, "write_text", capture_write), mock.patch.object(Path, "write_bytes", side_effect=AssertionError("unexpected write_bytes")):
        legacy.main()
    require(len(captured_outputs) == 4, "four captured RMED renderings")
    for name, raw in captured_outputs.items():
        path = DESIGN / name; watched[path] = path.read_bytes(); require(watched[path] == raw, "exact captured RMED reproduction " + name)
    require("not proven applicable" in watched[DESIGN / "rmed.entities.indented.txt"].decode() and "literal slash-qualified identities for display only" in watched[DESIGN / "rmed.roles.indented.txt"].decode(), "RMED caveats retained")

    producer_path = NODES / "support/integrate_node_reviews.py"; watched[producer_path] = producer_path.read_bytes()
    require(sha(watched[producer_path]) == PRODUCER_SHA, "integration producer SHA")
    producer = load_module("acceptance_integration_producer", producer_path)
    generated, _ = producer.build()
    require({Path(p).name: sha(raw) for p, raw in generated.items()} == HASHES, "fresh read-only integration reproduction")
    producer.persist_or_verify(generated, persist=False, verify_output=True)

    class VirtualPath:
        def __init__(self, raw=None):
            self.raw = raw
        def exists(self): return self.raw is not None
        def is_file(self): return True
        def is_symlink(self): return False
        def read_bytes(self): return self.raw
        def open(self, *args): raise AssertionError("guard attempted a write")

    guards = []
    def rejects(call, label):
        try: call()
        except AssertionError as exc:
            require("guard attempted a write" not in str(exc), "preflight before any write")
            guards.append(label)
        else: raise AssertionError("negative guard did not reject " + label)
    with mock.patch.object(producer, "safe_path", side_effect=lambda p: {"first": VirtualPath(), "later": VirtualPath(b"wrong")}[p]):
        rejects(lambda: producer.persist_or_verify({"first": b"a", "later": b"b"}, persist=True, verify_output=False), "late mismatch rejects before first write")
    with mock.patch.object(producer, "safe_path", return_value=VirtualPath()):
        rejects(lambda: producer.persist_or_verify({"first": b"a"}, persist=False, verify_output=True), "verify-output missing rejects")
        producer.persist_or_verify({"first": b"a"}, persist=False, verify_output=False); guards.append("dry-run missing never writes")
    with mock.patch.object(producer, "safe_path", return_value=VirtualPath(b"a")):
        producer.persist_or_verify({"first": b"a"}, persist=True, verify_output=False); guards.append("identical existing never writes")
    rejects(lambda: producer.persist_or_verify({}, persist=True, verify_output=True), "conflicting modes reject")
    for path, raw in watched.items():
        require(path.read_bytes() == raw, "input/source/Plan bytes unchanged " + str(path))
    external_drift = [p.relative_to(ROOT).as_posix() for p, raw in observed_live_core.items() if not p.is_file() or p.read_bytes() != raw]
    report = {"outcome": "PASS", "scope": "CA-P-1938 captured-snapshot integration, not semantic adoption", "outputs": HASHES, "producer_sha256": PRODUCER_SHA, "source_context": result, "captured_structure_sha256": sha(structure_raw), "historical_frontier_sha256": baseline["source_binding"]["source_frontier_sha256"], "review_receipt_commit": RECEIPT_COMMIT, "integration_commit": INTEGRATION_COMMIT, "nodes": 706, "dispositions": dict(packet["disposition_distribution"]), "evidence_catalogue_entries": len(expected_catalogue), "Main_Content_span_checks": evidence_checks, "unique_Subject_contributions_checked": len(contribution_checks), "occurrences": 4534, "segments": 3093, "endpoint_annotations": 6186, "input_occurrence_fallback_rows": fallbacks, "live_Done_prerequisites": len(prereqs), "committed_final_reviews": 9, "RMED_pointers": 3649, "RMED_entities": 580, "RMED_shared_sources": 805, "RMED_renderings_reproduced_in_memory": 4, "guard_checks": guards, "watched_files_unchanged": len(watched), "read_only_file_write_guard": "active", "live_Core_observations": len(observed_live_core), "concurrent_live_Core_drift": external_drift, "current_Core_claimed": False}
    print(json.dumps(report, ensure_ascii=False, sort_keys=True))


if __name__ == "__main__":
    main()
