#!/usr/bin/env python3
"""Apply the reviewed Header grouping packet in one locked, reversible batch."""
import contextlib
import copy
from datetime import datetime
import importlib.util
import json
from pathlib import Path
import re
from zoneinfo import ZoneInfo


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
PACKET = HERE.parent
CONTROL = ROOT / ".caprmedio_caprmedio"
SNAPSHOT = PACKET / "native-snapshot.json"
MODEL_MANIFEST = PACKET / "model/manifest.json"
DELIVERY_MANIFEST = PACKET / "delivery/previews-manifest.json"
DRAFT_DELIVERY_MANIFEST = PACKET / "delivery/draft-previews-manifest.json"
PLAN_PATH = HERE / "adoption-plan.json"
MAX_PLAN_BYTES = 100 * 1024 * 1024
CORE_REQUIREMENT_DIR = (
    CONTROL / "CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY"
    / "CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES"
    / "CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement"
)
R2719 = CORE_REQUIREMENT_DIR / "CA-R-2719-CORE_META_MODEL-DECLARATION--declare-atom-header.md"

# These five records were changed concurrently.  Their fresh preimages are
# intentionally grouped from the live bytes; any other snapshot drift stops.
FRESH_PREIMAGE_IDS = {"CA-P-2710", "CA-D-675", "CA-M-465", "CA-E-677", "CA-D-672"}
NEW_GROUP_TEMPLATE_KEYS = (
    "atom_id", "ref_id", "container", "role", "form", "topics", "tier",
    "status", "version", "updated_at", "carrier_destination",
)


def load_module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    assert spec and spec.loader
    spec.loader.exec_module(module)
    return module


n = load_module(
    "header_group_adoption",
    CONTROL / "03_plan/CA-P-2694-EPIC--entity-graph-refactor-stage-4-polishing/model-header-content-20261103/integration/adopt.py",
)
g = load_module("header_group_data", PACKET / "data/prepare_groups.py")
# Contract owned by the reference lane: rewrite(path, text) -> text is pure
# and idempotent.  It is applied after every approved body and ID change.
references = load_module("header_group_references", PACKET / "references/prepare_reference_impact.py")
n.ROOT = ROOT


def rel(path):
    return path.relative_to(ROOT).as_posix()


def maybe_summary(body):
    match = re.search(r"(?ms)^## Summary\s*\n(.*?)(?=^## |\Z)", body)
    return match.group(1).strip() if match else None


def summary(body):
    result = maybe_summary(body)
    assert result is not None, "carrier lacks one Summary heading"
    return result


def assert_quoted_updated_at(rendered, expected):
    front, _ = g.split_frontmatter(rendered)
    document = g.yaml.compose(front)
    assert isinstance(document, g.MappingNode)
    state_node = next((value for key, value in document.value if key.value == "state"), None)
    timestamp_node = (next((value for key, value in state_node.value if key.value == "updated_at"), None)
                      if isinstance(state_node, g.MappingNode) else None)
    assert timestamp_node is not None and timestamp_node.style in ("'", '"')
    assert timestamp_node.value == expected


def render_final_metadata(meta, body):
    payload = body[1:] if body.startswith("\n") else body
    rendered = g.render_grouped_metadata(meta, payload)
    rendered_meta, rendered_body = n.read(rendered.encode("utf-8"))
    assert rendered_meta == meta
    assert rendered_body == "\n" + payload
    state = meta.get("state")
    if isinstance(state, dict) and isinstance(state.get("updated_at"), str):
        assert_quoted_updated_at(rendered, state["updated_at"])
    return rendered


def slug(value):
    result = re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")
    assert result, f"empty filename slug for {value!r}"
    return result


def assert_group_roundtrip(candidate):
    restored = g.flatten_metadata(candidate["meta"], candidate["original"])
    assert restored == candidate["expected"], candidate["source"]


def new_group_template(baseline):
    """Keep new declarations canonical; legacy extras belong only to existing carriers."""
    assert all(key in baseline for key in NEW_GROUP_TEMPLATE_KEYS)
    template = {key: copy.deepcopy(baseline[key]) for key in NEW_GROUP_TEMPLATE_KEYS}
    assert template["container"] == {"scope_unit": "CA-SU-11"}
    assert template["role"] == "Requirement" and template["form"] == "Declaration"
    grouped, _ = g.nested_metadata(template)
    assert set(grouped) == {"identity", "context", "state", "destination"}
    assert "relations" not in grouped and "label" not in grouped["context"]
    return template, grouped


def candidate(source, raw):
    original, _ = n.read(raw)
    grouped, _ = g.transform_text(raw.decode("utf-8"))
    meta, body = n.read(grouped.encode("utf-8"))
    result = {
        "source": source,
        "before": raw,
        "original": original,
        "expected": copy.deepcopy(original),
        "meta": meta,
        "body": body,
        "target": source,
        "archive": None,
        "kind": "grouped",
        "body_mode": "grouping_only",
    }
    assert_group_roundtrip(result)
    return result


def update_topics(candidate, topics):
    context = candidate["meta"].get("context")
    assert isinstance(context, dict) and isinstance(topics, dict), candidate["source"]
    context["topics"] = copy.deepcopy(topics)
    candidate["expected"]["topics"] = copy.deepcopy(topics)


def set_body(candidate, body, mode):
    candidate["body"] = body
    candidate["body_mode"] = mode


def set_identity(candidate, atom_id, ref_id):
    identity = candidate["meta"].get("identity")
    assert isinstance(identity, dict), candidate["source"]
    identity["atom_id"] = atom_id
    identity["ref_id"] = ref_id
    candidate["expected"]["atom_id"] = atom_id
    candidate["expected"]["ref_id"] = ref_id


def set_state(candidate, *, status=None, version=None, updated_at=None):
    state = candidate["meta"].get("state")
    assert isinstance(state, dict), candidate["source"]
    if status is not None:
        state["status"] = status
        candidate["expected"]["status"] = status
    if version is not None:
        assert type(version) is int and version >= 1
        state["version"] = version
        candidate["expected"]["version"] = version
    if updated_at is not None:
        state["updated_at"] = updated_at
        candidate["expected"]["updated_at"] = updated_at


def update_destination(candidate, target, *, required=False):
    destination = candidate["meta"].get("destination")
    if destination is None:
        assert not required, candidate["source"]
        return
    assert isinstance(destination, dict) and isinstance(destination.get("file"), dict), candidate["source"]
    destination["file"]["name"] = target.name
    destination["file"]["path"] = rel(target.parent)
    candidate["expected"]["carrier_destination"] = copy.deepcopy(destination)


def approved_model_preview(candidate, row):
    path = ROOT / row["preview"]
    raw = path.read_bytes()
    assert n.sha(raw) == row["preview_sha256"], path
    preview_meta, preview_body = n.read(raw)
    assert n.sha(candidate["before"]) == row["source_sha256"], candidate["source"]
    assert isinstance(candidate["original"].get("topics"), dict), candidate["source"]
    assert isinstance(preview_meta.get("topics"), dict), path
    assert "main_subject" in preview_meta["topics"], path
    expected_preview = copy.deepcopy(candidate["original"])
    expected_preview["topics"]["main_subject"] = preview_meta["topics"]["main_subject"]
    assert preview_meta == expected_preview, path
    return preview_meta, preview_body


def approved_delivery_preview(candidate, row):
    path = ROOT / row["preview"]
    raw = path.read_bytes()
    assert n.sha(raw) == row["preview_sha256"], path
    preview_meta, preview_body = n.read(raw)
    expected_source_sha = row["source_sha256"] if "source_sha256" in row else row["draft_sha256"]
    assert n.sha(candidate["before"]) == expected_source_sha, candidate["source"]
    rewritten_meta, _ = n.read(
        rewrite_header_references(candidate["source"], candidate["before"].decode("utf-8")).encode("utf-8"),
    )
    # Reviewed Delivery bodies change; only metadata is limited to reference rebasing.
    assert preview_meta in (candidate["original"], rewritten_meta), path
    return preview_body


def current_target(source, atom_id, body):
    assert source.parent == CORE_REQUIREMENT_DIR, source
    name = f"{atom_id}-CORE_META_MODEL-DECLARATION--{slug(summary(body))}.md"
    assert len(name) <= 255, name
    return source.with_name(name)


def draft_target(source, old_id, new_id, version, declaration_summary):
    marker = f"{old_id}@{version}-draft"
    assert source.name.startswith(marker + "-"), source
    name = f"{new_id}@{version}-draft-CORE_META_MODEL-DECLARATION--{slug(declaration_summary)}.md"
    target = source.with_name(name)
    assert len(target.name) <= 255, target.name
    return target


def next_requirement_ids():
    maximum = 0
    versions = {}
    for path in n.control_root(ROOT).rglob("CA-[CAPRMEDO]-*.md"):
        match = re.match(r"(CA-([CAPRMEDO])-(\d+))(?!\d)", path.name)
        if not match:
            continue
        identity, role, number = match.group(1), match.group(2), int(match.group(3))
        if role == "R":
            maximum = max(maximum, number)
        version = re.search(rb"(?m)^version:\s*(\d+)\s*$", path.read_bytes())
        if version:
            versions[identity] = max(versions.get(identity, 0), int(version.group(1)))

    def allocate():
        nonlocal maximum
        while True:
            maximum += 1
            identity = f"CA-R-{maximum}"
            if not n.atom_id_has_preserved_history_evidence(ROOT, identity):
                return identity

    return versions, allocate


def replace_renamed_references(text, identities, draft_refs, filenames):
    for old, new in identities.items():
        # Do not rewrite CA-R-1@2, CA-R-10 or CA-R-1-... historical forms.
        text = re.sub(
            rf"(?<![A-Za-z0-9_-]){re.escape(old)}(?![A-Za-z0-9_@-])",
            new,
            text,
        )
    for old, new in draft_refs.items():
        text = re.sub(
            rf"(?<!archive/)(?<!archived/)(?<![A-Za-z0-9_-]){re.escape(old)}(?![A-Za-z0-9_-])",
            new,
            text,
        )
    for old, new in filenames.items():
        # Historical archive links remain pinned to the exact predecessor.
        text = re.sub(
            rf"(?<!archive/)(?<!archived/)(?<![A-Za-z0-9_@-]){re.escape(old)}(?![A-Za-z0-9@-])",
            new,
            text,
        )
    return text


def rewrite_header_references(path, text):
    """Use the reference lane's path-aware final interface when present."""
    if hasattr(references, "rewrite"):
        return references.rewrite(rel(path), text)
    return references.transform(text)


def self_check():
    sample = {
        "atom_id": "CA-R-1", "ref_id": "CA-R-1", "role": "Plan",
        "autonomous_confidence_threshold": 0.8, "work_sequence_number": 1,
        "status": "Active", "version": 1,
    }
    grouped, _ = g.nested_metadata(sample)
    assert g.flatten_metadata(grouped, sample) == sample
    template, canonical = new_group_template({
        "atom_id": "CA-R-1", "ref_id": "CA-R-1", "container": {"scope_unit": "CA-SU-11"},
        "role": "Requirement", "form": "Declaration", "topics": {"main_subject": "X"},
        "tier": 3, "status": "Active", "version": 1, "updated_at": "2026-11-06 00:00:00 +0400",
        "carrier_destination": {"file": {"name": "x.md", "path": ".caprmedio_caprmedio"}},
        "current_scope_unit": "CORE_META_MODEL", "claim_target_scope_unit": "CORE_META_MODEL",
        "relations": {"implements": ["CA-R-2"]}, "label": "legacy",
    })
    assert set(template) == set(NEW_GROUP_TEMPLATE_KEYS)
    assert set(canonical) == {"identity", "context", "state", "destination"}
    quoted = render_final_metadata({
        "identity": {"atom_id": "CA-R-1", "ref_id": "CA-R-1"},
        "state": {"status": "Active", "version": 1, "updated_at": "2026-11-06 00:00:00 +0400"},
    }, "\n## Summary\n\nTimestamp test\n")
    assert_quoted_updated_at(quoted, "2026-11-06 00:00:00 +0400")
    before = "CA-R-1 CA-R-1@2 CA-R-10 CA-R-1-old CA-R-1x archive/CA-R-1@2-draft CA-R-1@2-draft archive/old.md old.md"
    after = replace_renamed_references(
        before, {"CA-R-1": "CA-R-99"}, {"CA-R-1@2-draft": "CA-R-99@2-draft"}, {"old.md": "new.md"},
    )
    assert after == "CA-R-99 CA-R-1@2 CA-R-10 CA-R-1-old CA-R-1x archive/CA-R-1@2-draft CA-R-99@2-draft archive/old.md new.md"
    if hasattr(references, "self_check"):
        references.self_check()


def build_plan():
    assert Path.cwd().resolve() == ROOT, f"run from repository root: {ROOT}"
    assert not PLAN_PATH.exists(), f"review existing plan: {PLAN_PATH}"
    assert not (HERE / "adoption-receipt.json").exists(), "batch already applied"
    snapshot = json.loads(SNAPSHOT.read_text())
    rows = snapshot["carriers"]
    expected_source_count = snapshot["expected_count"]
    assert type(expected_source_count) is int and expected_source_count >= snapshot["baseline_source_count"]
    assert len(rows) == expected_source_count and len({row["path"] for row in rows}) == expected_source_count
    supplemental_paths = {row["path"] for row in snapshot.get("supplemental_sources", [])}
    assert supplemental_paths <= {row["path"] for row in rows}
    assert len(supplemental_paths) == expected_source_count - snapshot["baseline_source_count"]
    model = json.loads(MODEL_MANIFEST.read_text())
    delivery = json.loads(DELIVERY_MANIFEST.read_text())
    draft_delivery = json.loads(DRAFT_DELIVERY_MANIFEST.read_text())
    assert len(model["new_group_candidates"]) == 5
    assert delivery["status"].startswith("SEVEN_CURRENT") and len(delivery["rows"]) == 7
    assert draft_delivery["status"].startswith("FOUR_EXISTING_DRAFT") and len(draft_delivery["rows"]) == 4
    now = datetime.now(ZoneInfo("Asia/Tbilisi")).strftime("%Y-%m-%d %H:%M:%S %z")
    candidates, pins = {}, []
    for row in rows:
        source = ROOT / row["path"]
        assert source.is_file() and not source.is_symlink(), source
        raw = source.read_bytes()
        actual = n.sha(raw)
        allowed = row["atom_id"] in FRESH_PREIMAGE_IDS
        if actual != row["sha256"]:
            assert allowed, f"unapproved baseline drift: {row['path']}"
        pins.append({
            "path": row["path"], "baseline_sha256": row["sha256"],
            "live_sha256": actual,
            "mode": "fresh_preimage_allowed" if actual != row["sha256"] else "baseline_match",
        })
        candidates[row["path"]] = candidate(source, raw)
    drift_ids = {row["atom_id"] for row, pin in zip(rows, pins) if pin["mode"] != "baseline_match"}
    assert drift_ids <= FRESH_PREIMAGE_IDS, drift_ids

    def source_candidate(path):
        assert path in candidates, f"out-of-snapshot source: {path}"
        return candidates[path]

    current_owners, draft_owners = [], []
    for row in model["owner_previews"]:
        item = source_candidate(row["source"])
        preview_meta, preview_body = approved_model_preview(item, row)
        changed = summary(item["body"]) != summary(preview_body)
        assert changed is row["summary_changed"], row["source"]
        update_topics(item, preview_meta["topics"])
        set_body(item, preview_body, "approved_model_preview")
        if item["original"]["status"] == "Draft":
            draft_owners.append((row, item))
        else:
            assert item["original"]["status"] == "Active", item["source"]
            current_owners.append((row, item))
    assert len(current_owners) + len(draft_owners) == len(model["owner_previews"])

    header = source_candidate(rel(R2719))
    replacement = PACKET / "model" / model["header_replacement"]
    replacement_raw = replacement.read_bytes()
    assert n.sha(replacement_raw) == model["supplemental_preview_hashes"][model["header_replacement"]]
    replacement_body = "\n" + replacement_raw.decode("utf-8")
    assert summary(header["body"]) == summary(replacement_body)
    set_body(header, replacement_body, "approved_header_replacement")

    delivery_current = []
    for row in delivery["rows"]:
        item = source_candidate(row["source"])
        preview_body = approved_delivery_preview(item, row)
        assert summary(item["body"]) == summary(preview_body), item["source"]
        set_body(item, preview_body, "approved_delivery_preview")
        delivery_current.append(item)
    delivery_drafts = []
    for row in draft_delivery["rows"]:
        item = source_candidate(row["draft"])
        preview_body = approved_delivery_preview(item, row)
        assert item["original"]["status"] == "Draft", item["source"]
        assert summary(item["body"]) == summary(preview_body), item["source"]
        set_body(item, preview_body, "approved_delivery_draft_preview")
        delivery_drafts.append(item)

    archives, replacements, draft_ref_replacements, replacement_summaries = [], {}, {}, {}
    # main() holds the single real identity lock through planning and apply.
    with contextlib.nullcontext():
        versions, allocate = next_requirement_ids()

        def archive(item):
            version = item["original"]["version"]
            assert type(version) is int and version >= 1
            destination = item["source"].parent / "archive" / f"{item['source'].stem}@{version}.md"
            assert not destination.exists(), destination
            item["archive"] = destination
            archives.append({"predecessor": rel(item["source"]), "archive": rel(destination), "sha256": n.sha(item["before"])})

        def bump(item):
            identity = item["original"]["atom_id"]
            version = versions.get(identity, 0) + 1
            assert version > item["original"]["version"], item["source"]
            archive(item)
            set_state(item, version=version, updated_at=now)
            item["kind"] = "semantic_current_successor"

        for row, item in current_owners:
            old_id = item["original"]["atom_id"]
            assert item["original"]["ref_id"] == old_id, item["source"]
            if row["summary_changed"]:
                new_id = allocate()
                replacements[old_id] = new_id
                replacement_summaries[old_id] = summary(item["body"])
                archive(item)
                set_identity(item, new_id, new_id)
                set_state(item, status="Active", version=1, updated_at=now)
                item["target"] = current_target(item["source"], new_id, item["body"])
                assert not item["target"].exists(), item["target"]
                update_destination(item, item["target"])
                item["kind"] = "summary_identity_replacement"
            else:
                bump(item)

        for row, item in draft_owners:
            old_id = item["original"]["atom_id"]
            new_id = replacements.get(old_id)
            assert new_id, f"Draft owner lacks Current replacement: {item['source']}"
            version = item["original"]["version"]
            old_ref = f"{old_id}@{version}-draft"
            new_ref = f"{new_id}@{version}-draft"
            assert item["original"]["ref_id"] == old_ref, item["source"]
            assert summary(item["body"]) == replacement_summaries[old_id], item["source"]
            set_identity(item, new_id, new_ref)
            draft_ref_replacements[old_ref] = new_ref
            item["target"] = draft_target(
                item["source"], old_id, new_id, version, replacement_summaries[old_id],
            )
            assert not item["target"].exists(), item["target"]
            update_destination(item, item["target"])
            item["kind"] = "paired_draft_identity_rebase"

        bump(header)
        for item in delivery_current:
            bump(item)

        new_candidates = []
        template, grouped_template = new_group_template(header["original"])
        for preview_name in model["new_group_candidates"]:
            preview = PACKET / "model" / preview_name
            raw = preview.read_bytes()
            assert n.sha(raw) == model["supplemental_preview_hashes"][preview_name], preview
            body = "\n" + raw.decode("utf-8")
            declared_summary = summary(body)
            assert declared_summary.startswith("Declare "), preview
            subject = f"CAPRMEDIO_MODEL <+ {declared_summary.removeprefix('Declare ')}"
            item = {
                "source": None,
                "before": None,
                "original": copy.deepcopy(template),
                "expected": copy.deepcopy(template),
                "meta": copy.deepcopy(grouped_template),
                "body": body,
                "target": None,
                "archive": None,
                "kind": "new_group_declaration",
                "body_mode": "approved_new_group_claim",
            }
            new_id = allocate()
            set_identity(item, new_id, new_id)
            set_state(item, status="Active", version=1, updated_at=now)
            update_topics(item, {"main_subject": subject})
            target = current_target(R2719, new_id, body)
            item["target"] = target
            assert not target.exists(), target
            update_destination(item, target, required=True)
            assert re.fullmatch(r"CA-R-\d+", new_id)
            assert_group_roundtrip(item)
            context = item["meta"]["context"]
            assert context["container"]["scope_unit"] == "CA-SU-11"
            assert context["role"] == "Requirement" and context["form"] == "Declaration"
            assert context["tier"] == 3 and item["meta"]["state"]["status"] == "Active"
            for group in ("identity", "context", "state", "destination"):
                assert item["meta"].get(group), (preview, group)
            assert set(item["meta"]) == {"identity", "context", "state", "destination"}
            new_candidates.append(item)

        assert len(replacements) == sum(row["summary_changed"] for row, _ in current_owners)
        assert len(new_candidates) == len(model["new_group_candidates"]) == 5

        filename_replacements = {
            item["source"].name: item["target"].name
            for _, item in [*current_owners, *draft_owners]
            if item["target"] != item["source"]
        }
        all_candidates = list(candidates.values()) + new_candidates
        for item in all_candidates:
            assert_group_roundtrip(item)
            rendered = render_final_metadata(item["meta"], item["body"])
            renamed = replace_renamed_references(
                rendered, replacements, draft_ref_replacements, filename_replacements,
            )
            after = rewrite_header_references(item["target"], renamed)
            assert rewrite_header_references(item["target"], after) == after, item["source"] or item["target"]
            _, rendered_body = n.read(rendered.encode("utf-8"))
            _, after_body = n.read(after.encode("utf-8"))
            assert maybe_summary(rendered_body) == maybe_summary(after_body)
            item["after"] = after.encode("utf-8")

        operations = {}

        def operation(path, after, expected_before):
            path = Path(path)
            relative = rel(path)
            assert relative not in operations, f"duplicate operation: {relative}"
            before = path.read_bytes() if path.exists() else None
            assert before == expected_before, f"concurrent drift while preparing: {path}"
            operations[relative] = {
                "path": relative,
                "before": before.decode("utf-8") if before is not None else None,
                "before_sha256": n.sha(before) if before is not None else None,
                "after": after.decode("utf-8") if after is not None else None,
                "after_sha256": n.sha(after) if after is not None else None,
            }

        for item in all_candidates:
            if item["archive"] is not None:
                operation(item["archive"], item["before"], None)
        for item in candidates.values():
            source, target = item["source"], item["target"]
            if source == target:
                operation(source, item["after"], item["before"])
            else:
                operation(source, None, item["before"])
                operation(target, item["after"], None)
        for item in new_candidates:
            operation(item["target"], item["after"], None)

        outputs = []
        for item in all_candidates:
            meta, body = n.read(item["after"])
            identity, state = meta["identity"], meta["state"]
            outputs.append({
                "source_path": rel(item["source"]) if item["source"] else None,
                "target_path": rel(item["target"]),
                "atom_id": identity["atom_id"], "ref_id": identity["ref_id"],
                "status": state["status"], "version": state["version"],
                "summary": maybe_summary(body), "sha256": n.sha(item["after"]), "kind": item["kind"],
            })
        assert len(outputs) == expected_source_count + len(new_candidates)
        fresh_requirement_count = sum(
            item["kind"] in {"summary_identity_replacement", "new_group_declaration"}
            for item in all_candidates
        )
        plan = {
            "status": "PREPARED_REVIEWED_HEADER_GROUPS_ADOPTION",
            "scope": "All pinned native Current and Draft sources plus five approved Header-group Declarations.",
            "prepared_at": now,
            "native_workflow_admission": False,
            "journal_append": False,
            "source_count": len(rows), "final_live_source_count": len(outputs),
            "fresh_requirement_count": fresh_requirement_count,
            "input_hashes": {
                "native_snapshot": n.sha(SNAPSHOT.read_bytes()),
                "model_manifest": n.sha(MODEL_MANIFEST.read_bytes()),
                "delivery_manifest": n.sha(DELIVERY_MANIFEST.read_bytes()),
                "draft_delivery_manifest": n.sha(DRAFT_DELIVERY_MANIFEST.read_bytes()),
                "reference_transformer": n.sha((PACKET / "references/prepare_reference_impact.py").read_bytes()),
            },
            "preimage_pins": pins,
            "allowed_fresh_preimage_ids": sorted(FRESH_PREIMAGE_IDS),
            "base_id_replacements": replacements,
            "draft_ref_replacements": draft_ref_replacements,
            "filename_replacements": filename_replacements,
            "archive_pins": archives,
            "metadata_roundtrip_checks": len(all_candidates),
            "outputs": outputs,
            "operations": list(operations.values()),
        }
        payload = (json.dumps(plan, indent=2) + "\n").encode("utf-8")
        assert len(payload) <= MAX_PLAN_BYTES, f"plan is {len(payload)} bytes; Git limit is {MAX_PLAN_BYTES}"
        with PLAN_PATH.open("xb") as stream:
            stream.write(payload)
        return plan


def main():
    self_check()
    with n.atom_identity_lock(ROOT):
        plan = build_plan()
        n.HERE = HERE
        nested_lock = n.atom_identity_lock
        n.atom_identity_lock = lambda _: contextlib.nullcontext()
        try:
            n.apply()
        finally:
            n.atom_identity_lock = nested_lock
    print(json.dumps({
        "status": "APPLIED_VERIFIED", "outputs": len(plan["outputs"]),
        "operations": len(plan["operations"]), "fresh_requirements": plan["fresh_requirement_count"],
    }))


if __name__ == "__main__":
    print("Review-only entry point: call main() explicitly after runtime-owner approval.")
