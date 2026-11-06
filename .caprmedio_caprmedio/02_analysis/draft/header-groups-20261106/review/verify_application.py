#!/usr/bin/env python3
"""Read back a completed Header-groups adoption; this never changes carriers."""
from __future__ import annotations

import datetime as dt
import hashlib
import importlib.util
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
PACKET = HERE.parent
ROOT = PACKET.parents[3]
INTEGRATION = PACKET / "integration"
PLAN_PATH = INTEGRATION / "adoption-plan.json"
RECEIPT_PATH = INTEGRATION / "adoption-receipt.json"
SNAPSHOT_PATH = PACKET / "native-snapshot.json"
MODEL_MANIFEST_PATH = PACKET / "model/manifest.json"
REPORT_PATH = HERE / "application-verification.json"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    assert spec and spec.loader
    spec.loader.exec_module(module)
    return module


n = load_module(
    "header_group_adoption_base",
    ROOT / ".caprmedio_caprmedio/03_plan/CA-P-2694-EPIC--entity-graph-refactor-stage-4-polishing/model-header-content-20261103/integration/adopt.py",
)
g = load_module("header_group_data", PACKET / "data/prepare_groups.py")
references = load_module("header_group_references", PACKET / "references/prepare_reference_impact.py")


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def read_json(path: Path) -> dict:
    assert path.is_file(), f"required cutover artifact is missing: {path.relative_to(ROOT)}"
    return json.loads(path.read_text(encoding="utf-8"))


def bytes_at(relative: str) -> bytes | None:
    path = ROOT / relative
    return path.read_bytes() if path.exists() else None


def metadata(raw: bytes) -> tuple[dict, str]:
    return n.read(raw)


def grouped_timestamp_is_quoted(raw: bytes) -> bool:
    front, _ = g.split_frontmatter(raw.decode("utf-8"))
    document = g.yaml.compose(front)
    state = next((value for key, value in document.value if key.value == "state"), None)
    timestamp = next((value for key, value in state.value if key.value == "updated_at"), None)
    return timestamp is not None and timestamp.style in ("'", '"')


def raw_root_scalar(raw: bytes, name: str) -> str | None:
    front, _ = g.split_frontmatter(raw.decode("utf-8"))
    document = g.yaml.compose(front)
    node = next((value for key, value in document.value if key.value == name), None)
    return getattr(node, "value", None)


def source_preimage(plan: dict, source_path: str) -> bytes:
    row = next(row for row in plan["operations"] if row["path"] == source_path)
    assert row["before"] is not None, f"output source lacks predecessor: {source_path}"
    return row["before"].encode("utf-8")


def check_operations(plan: dict) -> None:
    operations = plan["operations"]
    assert len({row["path"] for row in operations}) == len(operations)
    outputs = plan["outputs"]
    renamed = sum(row["source_path"] != row["target_path"] for row in outputs if row["source_path"])
    in_place_sources = plan["source_count"] - renamed
    new_groups = sum(row["kind"] == "new_group_declaration" for row in outputs)
    assert len(operations) == in_place_sources + 2 * renamed + len(plan["archive_pins"]) + new_groups
    for row in operations:
        actual = bytes_at(row["path"])
        expected = row["after_sha256"]
        assert (sha(actual) if actual is not None else None) == expected, row["path"]
        if row["after"] is None:
            assert actual is None, f"retired path remains: {row['path']}"
        elif row["before"] is None:
            assert actual is not None, f"created path absent: {row['path']}"


def check_outputs(plan: dict) -> None:
    outputs = plan["outputs"]
    snapshot = read_json(SNAPSHOT_PATH)
    source_count = snapshot["expected_count"]
    assert snapshot["baseline_source_count"] + len(snapshot["supplemental_sources"]) == source_count
    assert plan["source_count"] == source_count == len(snapshot["carriers"])
    new_groups = sum(row["kind"] == "new_group_declaration" for row in outputs)
    assert new_groups == 5
    assert len(outputs) == plan["final_live_source_count"] == source_count + new_groups
    assert len({row["target_path"] for row in outputs}) == len(outputs)

    fresh_ids = {row["atom_id"] for row in outputs if row["kind"] in {"summary_identity_replacement", "new_group_declaration"}}
    model = read_json(MODEL_MANIFEST_PATH)
    current_replacements = sum(
        row["summary_changed"] and "/draft/" not in row["source"]
        for row in model["owner_previews"]
    )
    expected_fresh = current_replacements + new_groups
    assert expected_fresh == 28
    assert len(fresh_ids) == plan["fresh_requirement_count"] == expected_fresh
    assert not fresh_ids & {row["atom_id"] for row in snapshot["carriers"]}
    fresh_coordinates = [(row["atom_id"], row["version"]) for row in outputs if row["atom_id"] in fresh_ids]
    assert len(fresh_coordinates) == len(set(fresh_coordinates)), "new ID/version collision"

    r2712 = next(row for row in outputs if row["source_path"] and "CA-R-2712@3-draft" in row["source_path"])
    assert r2712["kind"] == "paired_draft_identity_rebase"
    assert r2712["status"] == "Draft" and r2712["version"] == 3
    assert r2712["ref_id"].endswith("@3-draft") and r2712["atom_id"] in fresh_ids

    for row in outputs:
        actual = bytes_at(row["target_path"])
        assert actual is not None and sha(actual) == row["sha256"], row["target_path"]
        actual_meta, _ = metadata(actual)
        assert actual_meta["identity"]["atom_id"] == row["atom_id"]
        assert actual_meta["identity"]["ref_id"] == row["ref_id"]
        assert actual_meta["state"]["status"] == row["status"]
        assert actual_meta["state"]["version"] == row["version"]
        if "updated_at" in actual_meta.get("state", {}):
            assert grouped_timestamp_is_quoted(actual), row["target_path"]
        assert references.rewrite(row["target_path"], actual.decode("utf-8")) == actual.decode("utf-8"), row["target_path"]
        if row["source_path"]:
            before_meta, _ = metadata(source_preimage(plan, row["source_path"]))
            if before_meta["status"] == "Draft":
                assert row["status"] == "Draft" and row["version"] == before_meta["version"], row["source_path"]


def check_metadata_preservation(plan: dict) -> None:
    aliases = timestamps = absent_timestamps = legacy_priorities = 0
    moved = {
        "atom_id", "ref_id", "container", "role", "form", "label", "topics", "tier",
        "relations", "status", "version", "updated_at", "carrier_destination",
    }
    for output in plan["outputs"]:
        if not output["source_path"]:
            continue
        before = source_preimage(plan, output["source_path"])
        original, _ = metadata(before)
        actual = bytes_at(output["target_path"])
        assert actual is not None
        grouped, _ = metadata(actual)
        assert not moved & set(grouped), output["target_path"]
        restored = g.flatten_metadata(grouped, original)
        expected_grouped, _ = metadata(next(row for row in plan["operations"] if row["path"] == output["target_path"])["after"].encode("utf-8"))
        assert restored == g.flatten_metadata(expected_grouped, original), output["target_path"]
        if original.get("role") == "Plan" and "autonomous_confidence_threshold" in original:
            aliases += 1
            assert grouped["context"]["plan"]["ai_agent_confidence_threshold"] == original["autonomous_confidence_threshold"]
        if isinstance(original.get("updated_at"), dt.datetime):
            timestamps += 1
            assert grouped["state"]["updated_at"] == raw_root_scalar(before, "updated_at")
        elif "updated_at" not in original:
            absent_timestamps += 1
            assert "updated_at" not in grouped.get("state", {})
        if "priority" in original and g.role_evidence(original)[0] != "Concern":
            legacy_priorities += 1
            assert grouped.get("priority") == original["priority"]
    assert aliases == 284
    assert timestamps == 12
    assert absent_timestamps == 4
    assert legacy_priorities == 4


def check_new_groups(plan: dict) -> None:
    rows = [row for row in plan["outputs"] if row["kind"] == "new_group_declaration"]
    assert len(rows) == 5
    for row in rows:
        meta, _ = metadata(bytes_at(row["target_path"]))
        assert set(meta) == {"identity", "context", "state", "destination"}
        assert meta["context"]["container"] == {"scope_unit": "CA-SU-11"}
        assert meta["context"]["role"] == "Requirement" and meta["context"]["form"] == "Declaration"
        assert meta["state"]["status"] == "Active" and meta["state"]["version"] == 1


def check_archives(plan: dict) -> None:
    pins = plan["archive_pins"]
    assert len(pins) == 31
    for pin in pins:
        actual = bytes_at(pin["archive"])
        assert actual is not None and sha(actual) == pin["sha256"], pin["archive"]
        operation = next(row for row in plan["operations"] if row["path"] == pin["archive"])
        assert operation["before"] is None and operation["after_sha256"] == pin["sha256"]


def verify() -> dict:
    assert Path.cwd().resolve() == ROOT, f"run from repository root: {ROOT}"
    plan, receipt = read_json(PLAN_PATH), read_json(RECEIPT_PATH)
    assert plan["status"] == "PREPARED_REVIEWED_HEADER_GROUPS_ADOPTION"
    assert receipt["status"] == "APPLIED_VERIFIED"
    assert receipt["plan_sha256"] == sha(PLAN_PATH.read_bytes())
    assert receipt["output_count"] == len(plan["outputs"])
    assert receipt["operation_count"] == len(plan["operations"])
    check_operations(plan)
    check_outputs(plan)
    check_metadata_preservation(plan)
    check_new_groups(plan)
    check_archives(plan)
    return {"status": "READBACK_VERIFIED", "plan_sha256": receipt["plan_sha256"], "outputs": len(plan["outputs"]), "operations": len(plan["operations"])}


def main() -> None:
    report = verify()
    REPORT_PATH.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report))


if __name__ == "__main__":
    main()
