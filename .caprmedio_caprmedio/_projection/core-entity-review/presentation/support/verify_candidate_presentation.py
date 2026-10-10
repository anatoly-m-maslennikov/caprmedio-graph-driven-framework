"""CA-P-1958 independent presentation QA; never writes candidate artifacts.

Only isolated, automatically cleaned .caprmedio_tmp fixtures exercise the
producer's persistence path. The accepted semantic/source reviews are inputs,
not rerun or rebound to today's Core by this verifier.
"""
from __future__ import annotations

import collections
import contextlib
import hashlib
import importlib.util
import io
import json
import re
import subprocess
import sys
import tempfile
from pathlib import Path
from unittest import mock

ROOT = Path(__file__).resolve().parents[5]
BASE = ROOT / ".caprmedio_caprmedio/_projection/core-entity-review"
PRESENTATION = BASE / "presentation"
PRODUCER_SHA = "3b18039bbfe8292d012b1944d3567d055ae9874dfb64e457fbad15716ede4260"
OUTPUT_HASHES = {
    "candidate.entities.indented.txt": "f32588f6f9bc97e2180578c051bfbc73f39a7e80b7273bdf6702f9309778ed56",
    "candidate.review.md": "8b0d9c9ff3f940f3bfb4456aabda7b808060424a9910a194ff85a50073bcf975",
    "candidate.manifest.json": "fb9deec859a5f828e648d94da9d7888c50175872a70b9711e6a9f6a734ec81ce",
}
INPUTS = {
    "node_marks": ("nodes/nodes.dispositions.json", "1b9d751f95aa71486908b53b3d7f3f9825defae137be3d8792d45177587c48f8"),
    "ledger": ("nodes/relations.marked.ledger.json", "f6efdcaddfbbb4d9f4607084ee77ca83c75de2566fd9506da51dac2493e02371"),
    "structure": ("nodes/candidate.structure.marked.json", "04f2b8d3606ac30b74850ab9ff53ebebfcbcffd1cda1e5ad2d948662c085e34b"),
    "design": ("design/structure.design.json", "10733c9f1b6b8d5946acdc469e7cfe3ee710ed515f1de77eed765c2252652b9e"),
    "rmed": ("design/rmed.views.json", "d7fd113a408c3bb70e17ab55cc86fd6746c3d5c74ff27a9a864632ec6de999aa"),
    "snapshot": ("nodes/snapshot.context.md", "bfd6a7d93745d69432111df37ca139ba727a1ad06e821d94d3c059e44169ee23"),
    "operator": ("design/operator.decisions.md", "53eeb7a3fdaa002cd05170fe185cfb5baeea72814a1f32567d8eea6f56ac65cb"),
    "scope": ("nodes/scope.omission.decision.md", "d4ea636d540b0558c1a0fbb8263760947e1f0768840c43b3ed1d05c96b497453"),
    "acceptance": ("nodes/nodes.acceptance.md", "c2576865efcd2cfcc10a7075ad546b1c2d288cdae9f285eeaeb61f858bbf2e9b"),
}
RECEIPT_COMMIT = "94776a14a368827a758534eb9c5c0109d649f309"
PRESENTATION_COMMIT = "4b0468fab5b46e293ed4a9698b76fe47ad223c9b"


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def require(condition, label):
    if not condition:
        raise AssertionError(label)


def git_bytes(commit, path):
    return subprocess.check_output(["git", "show", f"{commit}:{path}"], cwd=ROOT)


def tree(commit):
    return subprocess.check_output(["git", "ls-tree", "-r", "--name-only", commit], cwd=ROOT, text=True).splitlines()


def plan_path(paths, atom_id):
    candidates = [p for p in paths if p.endswith(".md") and f"-{atom_id}-" in Path(p).name and "/archive/" not in p]
    require(len(candidates) == 1, f"unique Plan {atom_id}")
    return candidates[0]


def scalar(raw, key):
    text = raw.decode(); require(text.startswith("---\n"), "Plan frontmatter")
    body = text[4:text.index("\n---", 4)]
    values = re.findall(rf"^{re.escape(key)}:\s*(.*?)\s*$", body, re.MULTILINE)
    require(len(values) == 1, f"unique Plan {key}")
    return values[0].strip().strip("\"'")


def guards(producer):
    results = []
    expected = {"first.txt": b"first", "later.txt": b"later"}

    def rejects(function, label):
        try:
            function()
        except (SystemExit, ValueError, FileExistsError):
            results.append(label)
        else:
            raise AssertionError("guard did not reject " + label)

    with tempfile.TemporaryDirectory(prefix="candidate-qa-", dir=ROOT / ".caprmedio_tmp") as temporary:
        scratch = Path(temporary).resolve(); directory = scratch / "case/presentation"
        directory.mkdir(parents=True)
        with mock.patch.object(producer, "REPO_ROOT", scratch), mock.patch.object(producer, "PRESENTATION_DIR", directory):
            (directory / "later.txt").write_bytes(b"wrong")
            rejects(lambda: producer.persist_outputs(expected), "late mismatch preflight")
            require(not (directory / "first.txt").exists() and (directory / "later.txt").read_bytes() == b"wrong", "no early write on mismatch")
            (directory / "later.txt").unlink()
            producer.persist_outputs(expected)
            require(all((directory / name).read_bytes() == raw for name, raw in expected.items()), "exclusive creation")
            results.append("exclusive absent creation")
            times = {name: (directory / name).stat().st_mtime_ns for name in expected}
            producer.persist_outputs(expected)
            require(times == {name: (directory / name).stat().st_mtime_ns for name in expected}, "identical existing not rewritten")
            results.append("identical existing no rewrite")
            for name in expected:
                (directory / name).unlink()
            rejects(lambda: producer.verify_outputs(expected), "missing verify output")
            (directory / "first.txt").symlink_to(scratch / "missing-target")
            rejects(lambda: producer.persist_outputs(expected), "dangling output symlink")
            require(not (scratch / "missing-target").exists() and not (directory / "later.txt").exists(), "symlink rejection before writing")
            (directory / "first.txt").unlink()
            target = scratch / "existing-target"; target.write_bytes(b"do-not-touch")
            (directory / "first.txt").symlink_to(target)
            rejects(lambda: producer.persist_outputs(expected), "existing output symlink")
            require(target.read_bytes() == b"do-not-touch", "existing symlink target preserved")
            (directory / "first.txt").unlink()
            (directory / "first.txt").mkdir()
            rejects(lambda: producer.persist_outputs(expected), "directory output")
            (directory / "first.txt").rmdir()
            rejects(lambda: producer.persist_outputs({"../escape.txt": b"no"}), "output name escape")
            original_open = Path.open

            def race(path, *args, **kwargs):
                if path == directory / "later.txt" and args and args[0] == "xb":
                    with original_open(path, "wb") as handle:
                        handle.write(b"competitor")
                return original_open(path, *args, **kwargs)

            with mock.patch.object(Path, "open", race):
                rejects(lambda: producer.persist_outputs(expected), "exclusive creation race")
            require(not (directory / "first.txt").exists() and (directory / "later.txt").read_bytes() == b"competitor", "race rollback and competitor preservation")
            with mock.patch.object(producer, "expected_outputs", return_value=expected), mock.patch.object(sys, "argv", ["renderer"]), contextlib.redirect_stdout(io.StringIO()):
                producer.main()
            require(not (directory / "first.txt").exists(), "dry default never creates missing output")
            results.append("default dry no write")
            with mock.patch.object(sys, "argv", ["renderer", "--persist", "--verify-output"]), contextlib.redirect_stderr(io.StringIO()):
                rejects(producer.main, "mutually exclusive modes")
        # A separate routing fixture for every lexical ancestor inside root.
        for level in range(4):
            case = scratch / f"ancestor-{level}"; case.mkdir()
            parts = [".caprmedio_caprmedio", "_projection", "core-entity-review", "presentation"]
            parent = case
            for part in parts[:level]:
                parent = parent / part; parent.mkdir()
            target = scratch / f"target-{level}"; target.mkdir()
            link = parent / parts[level]; link.symlink_to(target, target_is_directory=True)
            routed = link
            for part in parts[level + 1:]:
                routed = routed / part; routed.mkdir()
            with mock.patch.object(producer, "REPO_ROOT", case), mock.patch.object(producer, "PRESENTATION_DIR", routed):
                rejects(producer.assert_safe_output_directory, f"ancestor symlink level {level}")
        target_root = scratch / "repository-target"; (target_root / "presentation").mkdir(parents=True)
        alias_root = scratch / "repository-alias"; alias_root.symlink_to(target_root, target_is_directory=True)
        with mock.patch.object(producer, "REPO_ROOT", alias_root), mock.patch.object(producer, "PRESENTATION_DIR", alias_root / "presentation"):
            rejects(producer.assert_safe_output_directory, "repository root symlink")
    return results


def main():
    watched = {}
    def read(path):
        raw = path.read_bytes(); watched[path] = raw; return raw
    inputs = {}
    for name, (relative, digest) in INPUTS.items():
        path = BASE / relative; raw = read(path)
        require(sha(raw) == digest, f"accepted input {name}")
        require(git_bytes(RECEIPT_COMMIT, path.relative_to(ROOT).as_posix()) == raw, f"committed accepted input {name}")
        value = json.loads(raw) if path.suffix == ".json" else {}
        inputs[name] = (value, {"path": path.relative_to(ROOT).as_posix(), "bytes": len(raw), "sha256": digest})
    saved = {name: read(PRESENTATION / name) for name in OUTPUT_HASHES}
    require({name: sha(raw) for name, raw in saved.items()} == OUTPUT_HASHES, "three frozen output hashes")
    manifest = json.loads(saved["candidate.manifest.json"]); review = saved["candidate.review.md"].decode(); inventory = saved["candidate.entities.indented.txt"].decode()
    marks = inputs["node_marks"][0]["node_disposition_marks"]; structure = inputs["structure"][0]; design = inputs["design"][0]
    mark_by_id = {r["identity"]: r for r in marks}; crosswalk = {r["preserved_identity"]: r for r in structure["node_identity_crosswalk"]}
    require(len(mark_by_id) == len(crosswalk) == 706 and set(mark_by_id) == set(crosswalk), "706 fixed input identities")
    bucket_titles = {"Continuant (display-only; 17 identities)": "Continuant", "Occurrent (display-only; 3 identities)": "Occurrent", "Broad model anchors (not temporally classified; 4 identities)": "anchors", "Explicitly unclassified (682 identities; no default parentage inferred)": "unclassified"}
    expected_groups = {g["display_group"]: {m["qualified_identity"] for m in g["members"]} for g in structure["display_groups"]}
    expected_groups["anchors"] = set(structure["non_temporal_broad_model_anchors"]["qualified_identities"])
    expected_groups["unclassified"] = set(mark_by_id) - set.union(*[expected_groups[k] for k in ("Continuant", "Occurrent", "anchors")])
    actual_groups = collections.defaultdict(set); seen = []; bucket = None; stack = []; top_labels = 0; blocked_count = 0
    drops = {r["identity"] for r in inputs["node_marks"][0]["unresolved_drop_annotations"]}
    labels = {"retain": "RETAIN", "question": "QUESTION", "consolidate": "CONSOLIDATE CANDIDATE", "generalize": "GENERALIZE CANDIDATE"}
    for line in inventory.splitlines():
        if line == "Candidate-only display supplements": break
        if line.startswith("  ") and not line.startswith("    ") and line.strip() in bucket_titles:
            bucket = bucket_titles[line.strip()]; stack = []; continue
        if bucket is None or not line.startswith("    "): continue
        indent = len(line) - len(line.lstrip(" ")); require(indent % 2 == 0, "two-space indentation")
        depth = (indent - 4) // 2; body = line[indent:]; is_identity = " [original identity: " in body
        if is_identity:
            label, suffix = body.rsplit(" [original identity: ", 1); identity, mark = suffix[:-1].split("; ", 1)
        else:
            require(body.endswith(" (prefix support only)"), "only explicitly labelled prefix supports")
            label = body.removesuffix(" (prefix support only)")
        require(depth <= len(stack), "no missing display parent")
        stack = stack[:depth] + [label]
        top_labels += depth == 0
        if is_identity:
            require(identity in mark_by_id and "".join(stack) == crosswalk[identity]["proposed_display_path"], "exact display crosswalk path")
            wanted_mark = "QUESTION; DROP CANDIDATE unresolved" if identity in drops else labels[mark_by_id[identity]["review_row"]["disposition"]]
            if crosswalk[identity]["display_rebase"] == "blocked_chain_original_preserved":
                wanted_mark += "; LEGACY RELATION UNRESOLVED"; blocked_count += 1
            require(mark == wanted_mark, "node mark not mistaken for relation clearance")
            seen.append(identity); actual_groups[bucket].add(identity)
    require(len(seen) == len(set(seen)) == 706 and set(seen) == set(mark_by_id), "each original identity once")
    require(dict(actual_groups) == expected_groups and [len(expected_groups[k]) for k in ("Continuant", "Occurrent", "anchors", "unclassified")] == [17, 3, 4, 682], "exact display bucket memberships")
    require(blocked_count == 123 and top_labels == 359, "blocked chains and display-label accounting")
    distribution = collections.Counter(r["review_row"]["disposition"] for r in marks)
    require(distribution == manifest["counts"]["dispositions"] == {"retain": 584, "consolidate": 3, "generalize": 2, "question": 117}, "exact review marks")
    require(manifest["counts"] == {"original_identity_count": 706, "primary_inventory_identity_count": 706, "continuant": 17, "occurrent": 3, "broad_non_temporal_anchors": 4, "unclassified": 682, "before_literal_syntactic_roots": 346, "before_standalone_roots": 293, "rendered_top_level_display_labels": 359, "dispositions": dict(distribution), "unresolved_drop_annotations": 2, "inherited_constraints": 7, "term_taxonomy_proposals": 10, "rmed_governs_pointers": 805, "rmed_depends_on_pointers": 2844}, "all manifest accounting fields")
    questions = [m for m in marks if m["review_row"]["disposition"] == "question"]
    require(len(questions) == 117 and all(m["review_row"]["question"] and m["review_row"]["proposal"] is None for m in questions) and len(drops) == 2, "questions and unresolved drops not adopted")
    proposal_section = review.split("## Candidate marks requiring an Operator decision", 1)[1].split("## Conditional inherited", 1)[0]
    proposed = [m for m in marks if m["review_row"]["disposition"] in {"consolidate", "generalize"}]
    require(len(proposed) == 5 and proposal_section.count("display target:") == 5, "five actual proposal targets")
    for row in proposed:
        p = row["review_row"]["proposal"]; target = next(p[k] for k in ("candidate_display_parent", "candidate_display_family", "candidate_display_name") if p.get(k))
        line = next(x for x in proposal_section.splitlines() if x.startswith(f"- `{row['identity']}` —"))
        require(f"display target: `{target}`" in line and p["candidate_basis"] in line and p["lost_distinctions_risk"] in line, "exact proposal target/basis/risk")
    for c in design["inherited_constraints"]:
        expected = f"- `{c['constraint_id']}` — applies when: {c['applies_when']} Rule: {c['rule']}"
        require(review.count(expected) == 1, "conditional rule retains applies_when")
    require(len(design["inherited_constraints"]) == 7, "seven conditions")
    for r in design["additional_relations"]:
        require(r["graph_kind"] == "terms" and r["canonical_relation"] == "NARROWER_THAN" and r["native_admission"] == "not_performed", "Terms ownership/nonadmission")
        expected = f"- `{r['qualified_parent']}` / `{r['qualified_child']}` — `/` display; canonical `NARROWER_THAN` `{r['qualified_child']} → {r['qualified_parent']}` (narrower→broader; terms candidate; not_performed)."
        require(review.count(expected) == 1, "parent/child display versus canonical direction")
    require(len(design["additional_relations"]) == 10, "ten separate Term proposals")
    for text in (inventory, review):
        require("separately evidenced display" in text and "LEGACY RELATION UNRESOLVED" in text and "does not approve" in text, "notation caveats")
    require("full governed Subject **and** full owning Scope Unit" in review and "otherwise Scope must remain explicit" in review and "not retroactive Core evidence" in review, "latest conjunctive Scope default")
    canonical = json.dumps(structure, ensure_ascii=False, sort_keys=True, separators=(",", ":"), allow_nan=False).encode()
    require(manifest["candidate_json"]["file_sha256"] == INPUTS["structure"][1] and manifest["candidate_json"]["canonical_sorted_compact_json_sha256"] == sha(canonical) == "0b26e7571ab4897f85e2b521255feb9f83e33c4f48ce86f02fd0a8f80c9303b1", "canonical/file SHA separation")
    mapping = {"nodes_dispositions": "node_marks", "relations_marked_ledger": "ledger", "candidate_structure_marked": "structure", "structure_design": "design", "rmed_views": "rmed", "nodes_acceptance": "acceptance"}
    for output_key, input_key in mapping.items():
        require(manifest["input_pins"][output_key] == inputs[input_key][1], "exact accepted input descriptor")
    require(manifest["captured_source_context"]["captured_context"] == inputs["snapshot"][1] and manifest["operator_directions"]["scope_omission"] == inputs["scope"][1] and manifest["operator_directions"]["substance_content"] == inputs["operator"][1], "separate context/direction pins")
    for pin in manifest["input_pins"]["rmed_text_views"]:
        raw = read(ROOT / pin["path"]); require(sha(raw) == pin["sha256"] and len(raw) == pin["bytes"], "RMED rendering pointer pin")
        require(git_bytes(RECEIPT_COMMIT, pin["path"]) == raw, "committed accepted RMED rendering")
    for link in ("../design/rmed.roles.indented.txt", "../design/rmed.entities.indented.txt", "../design/rmed.views.json", "../nodes/nodes.dispositions.json", "../nodes/relations.marked.ledger.json"):
        require(link in review and (PRESENTATION / link).is_file(), "all shared links resolve")
    require("M/E/D associations are not proven applicability" in review and "GOVERNS and DEPENDS_ON are separate" in review and "No empty M/E/D slot" in inventory, "no invented RMED applicability")
    receipts = manifest["completion_receipts"]; require(receipts["receipt_commit"] == RECEIPT_COMMIT, "receipt commit")
    captured_tree = tree(RECEIPT_COMMIT); live_tree = [p.relative_to(ROOT).as_posix() for p in (ROOT / ".caprmedio_caprmedio/03_plan").rglob("*.md")]
    plan_hashes = {}
    for key in ("ca_p_1907", "ca_p_1938"):
        pin = receipts[key]; location = plan_path(captured_tree, pin["atom_id"]); raw = git_bytes(RECEIPT_COMMIT, location)
        require(scalar(raw, "atom_id") == pin["atom_id"] and scalar(raw, "status") == pin["status"] == "Done" and int(scalar(raw, "version")) == pin["plan_version"] and sha(raw) == pin["plan_carrier_sha256"], "actual prerequisite Git blob")
        live_path = ROOT / plan_path(live_tree, pin["atom_id"]); require(read(live_path) == raw, "live Done prerequisite bytes")
        plan_hashes[pin["atom_id"]] = sha(raw)
    require(receipts["ca_p_1938"]["acceptance_record_sha256"] == INPUTS["acceptance"][1] and receipts["ca_p_1938"]["plan_carrier_sha256"] != INPUTS["acceptance"][1], "acceptance record is not Plan Carrier")
    start_path = ROOT / plan_path(live_tree, "CA-P-1957"); start_raw = read(start_path)
    require(start_raw == git_bytes(PRESENTATION_COMMIT, plan_path(tree(PRESENTATION_COMMIT), "CA-P-1957")) and scalar(start_raw, "status") == "Done", "1957 Done start prerequisite")
    producer_path = PRESENTATION / "support/render_candidate.py"; producer_raw = read(producer_path)
    require(sha(producer_raw) == PRODUCER_SHA == manifest["producer"]["sha256"], "frozen renderer")
    for name, raw in saved.items():
        require(git_bytes(PRESENTATION_COMMIT, (PRESENTATION / name).relative_to(ROOT).as_posix()) == raw, "committed saved presentation")
    for field, name in (("candidate_entities_indented", "candidate.entities.indented.txt"), ("candidate_review", "candidate.review.md")):
        require(manifest["rendered_outputs"][field] == {"path": name, "bytes": len(saved[name]), "sha256": sha(saved[name])}, "actual rendered-output pins")
    spec = importlib.util.spec_from_file_location("candidate_qa_renderer", producer_path); producer = importlib.util.module_from_spec(spec); spec.loader.exec_module(producer)
    require(producer.EXPECTED_INPUT_HASHES == {k: v[1] for k, v in INPUTS.items()}, "all nine frozen input guards")
    rejected_inputs = []
    for key in INPUTS:
        bad = dict(inputs); value, pin = bad[key]; bad[key] = (value, {**pin, "sha256": "f" * 64})
        try: producer.render(bad)
        except ValueError: rejected_inputs.append(key)
        else: raise AssertionError("changed input pin accepted " + key)
    require(producer.expected_outputs() == saved, "byte-exact read-only reproduction")
    with mock.patch.object(Path, "write_bytes", side_effect=AssertionError("production write forbidden")), mock.patch.object(Path, "write_text", side_effect=AssertionError("production write forbidden")), contextlib.redirect_stdout(io.StringIO()):
        for args in (["renderer"], ["renderer", "--verify-output"]):
            with mock.patch.object(sys, "argv", args): require(producer.main() == 0, "default/verify CLI")
    guard_results = guards(producer)
    for path, raw in watched.items(): require(path.read_bytes() == raw, "protected bytes unchanged " + str(path))
    require(manifest["presentation_status"] == "CANDIDATE" and manifest["non_authoritative"] is True and all(manifest[k] == "not_performed" for k in ("operator_acceptance", "native_admission", "semantic_admission", "source_migration")), "nonadoption boundary")
    context = manifest["captured_source_context"]
    require(context["git_commit"] == "a971d0e00c33c779f485fc8cad63194894d440fb" and context["current_core_claimed"] is False and context["source_pins_checked"] == 951, "historical context only")
    print(json.dumps({"outcome": "PASS", "scope": "CA-P-1958 presentation, not source or semantic re-admission", "outputs": OUTPUT_HASHES, "renderer_sha256": PRODUCER_SHA, "source_receipt_commit": RECEIPT_COMMIT, "presentation_commit": PRESENTATION_COMMIT, "identities_once": len(seen), "display_buckets": {k: len(v) for k, v in actual_groups.items()}, "dispositions": dict(distribution), "blocked_legacy_chains": blocked_count, "display_labels_not_ontology_roots": top_labels, "proposal_targets_with_risks": 5, "unresolved_questions": len(questions), "unresolved_drops": len(drops), "conditional_rules": 7, "Term_directions": 10, "input_pins_rejected": rejected_inputs, "actual_Plan_blob_hashes": plan_hashes, "canonical_candidate_json_sha256": sha(canonical), "file_candidate_json_sha256": INPUTS["structure"][1], "guards": guard_results, "watched_files_unchanged": len(watched), "live_Core_read": False}, sort_keys=True))


if __name__ == "__main__":
    main()
