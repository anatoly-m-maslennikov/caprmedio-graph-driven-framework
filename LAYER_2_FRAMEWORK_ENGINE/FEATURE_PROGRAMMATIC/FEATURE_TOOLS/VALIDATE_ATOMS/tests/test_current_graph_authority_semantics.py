"""Frozen current graph-source contracts and their mechanical adapter controls."""

from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path
import sys
import tempfile
import unittest
from typing import Any


HERE = Path(__file__).resolve().parent
TOOL = HERE.parent
PROGRAMMATIC_TOOLS = TOOL.parent
REPOSITORY = PROGRAMMATIC_TOOLS.parents[2]
sys.path.insert(0, str(TOOL))
sys.path.insert(0, str(PROGRAMMATIC_TOOLS))
sys.path.insert(0, str(HERE))

from authoritative_status_models import (  # noqa: E402
    StatusModelError,
    declarations_from_sources,
    resolve_status_domain,
)
from scope_declaration_test_support import write_scope_unit_declarations  # noqa: E402
from scope_unit_declarations import read_scope_unit_declarations  # noqa: E402
from validate_atoms_workers.authority import AuthorityContext, Obligation  # noqa: E402
from validate_atoms_workers.check_graph_extended import (  # noqa: E402
    _INVERSES,
    _TYPED,
    relations_resolution,
)
from validate_atoms_workers.check_support import Check  # noqa: E402
from validate_atoms_workers.graph_authority_refresh import (  # noqa: E402
    APPROVED_GRAPH_AUTHORITY_IDS,
)
from validate_atoms_workers.parsing import parse_carrier  # noqa: E402
from golden_authority import frozen_source, frozen_sources  # noqa: E402


FIXTURES = HERE / "fixtures" / "current_graph_authority"
MANIFEST = TOOL / "validate_atoms_workers" / "graph_authority.json"
EXTRAS = frozenset(
    {"CA-R-1194", "CA-R-1199", "CA-R-1202", "CA-R-1247", "CA-R-1248", "CA-R-1456"}
)

# The four behavior-changing contracts are asserted from exact local bytes.
# The remaining metadata-only refreshes are checked by graph_authority_refresh.
CHANGED_PINS = {
    "CA-D-268": (18, "eb33ffdb1ae992b8db8ea50dbb332ab3fd91b90040096c5be4965d89afc96888", "07_delivery/CA-D-268-CORE_META_MODEL-DELIVERY--serialize-authored-direct-relations-on-their-owning-atoms.md"),
    "CA-R-796": (23, "0a3a51c9f7854d1d22894b2afba837f9cbc919f8cb35b11ea15a4179de77b580", "04_requirement/CA-R-796-CORE_META_MODEL-CORE-REQUIREMENT--keep-tier-parent-relations-within-atom-scope.md"),
    "CA-R-1040": (17, "b8db24215ede0bfe54316b71ef915df0281d0ab910aab5de34bf3af3b6749f41", "04_requirement/CA-R-1040-CORE_META_MODEL-CORE--reject-authored-inverse-relations.md"),
    "CA-R-1539": (9, "13b63bfdf55480496b734a408c3632d33c68b9522426ca8092b52038e7adbe0a", "04_requirement/CA-R-1539-CORE_META_MODEL-GENERAL-REQUIREMENT--register-core-plan-status-values.md"),
}
SNAPSHOT_PINS = {
    **{key: (value[0], value[1]) for key, value in CHANGED_PINS.items()},
    "CA-R-1947": (3, "ca65ea189912acb3605517a2a8dbe3e76cb402dc018df6d6ca167decd16b218f"),
}


def _fixture_source(identifier: str) -> dict[str, Any]:
    path = FIXTURES / f"{identifier}.md"
    raw = path.read_bytes()
    parsed = parse_carrier(raw, path)
    expected_version, expected_hash = SNAPSHOT_PINS[identifier]
    if parsed.metadata.get("atom_id") != identifier or parsed.metadata.get("version") != expected_version:
        raise AssertionError(f"fixture identity changed: {identifier}")
    if hashlib.sha256(raw).hexdigest() != expected_hash:
        raise AssertionError(f"fixture hash changed: {identifier}")
    return {
        "binding": {
            "atom_id": identifier,
            "version": expected_version,
            "path": str(path),
            "sha256": expected_hash,
        },
        "text": parsed.text,
        "metadata": parsed.metadata,
    }


def _check(
    metadata: dict[str, Any], sources: list[dict[str, Any]], *,
    references: tuple[dict[str, Any], ...] = (), structure: Any = None,
) -> Check:
    check = Check(Obligation("relations.resolution", [], True, "frozen current graph fixture"), AuthorityContext([], 0, 0, 0, [], (), {}, False))
    check.inputs = {
        "sources": sources,
        "references": list(references),
        "reference_complete": True,
        "path": Path("/inventory/child.md"),
        "_project_identity": {"project": {"name": "demo"}},
    }
    if structure is not None:
        check.inputs["scope_unit_declarations"] = structure
    relations_resolution(metadata, "", check)
    return check


def _scope_units() -> Any:
    if not hasattr(_scope_units, "fixture"):
        scratch = REPOSITORY / ".caprmedio_tmp/tests/current-graph-authority"
        scratch.mkdir(parents=True, exist_ok=True)
        directory = tempfile.TemporaryDirectory(dir=scratch)
        root = Path(directory.name)
        control = root / ".caprmedio_demo"
        control.mkdir()
        (control / "caprmedio_project_settings.toml").write_text(
            '[project]\nname = "demo"\n[paths]\ncontrol_root = ".caprmedio_demo"\n',
            encoding="utf-8",
        )
        write_scope_unit_declarations(
            root,
            (
                {"scope_unit_name": "SOURCES", "scope_unit_label": "Layer"},
                {"scope_unit_name": "CORE", "parent": "SOURCES", "scope_unit_label": "Layer"},
                {"scope_unit_name": "CONFIG", "parent": "SOURCES", "scope_unit_label": "Layer"},
            ),
            control_root=control,
        )
        _scope_units.fixture = (directory, read_scope_unit_declarations(root, control))
    return _scope_units.fixture[1]


def _rmed_atom(atom_id: str, scope: str, tier: int, **changes: Any) -> dict[str, Any]:
    return {
        "atom_id": atom_id, "version": 1, "content_role": "Requirement", "status": "Active",
        "current_scope_unit": scope, "tier": tier, **changes,
    }


def _r796_fixture() -> tuple[dict[str, Any], dict[str, Any], dict[str, Any], list[dict[str, Any]]]:
    r796 = _fixture_source("CA-R-796")
    child = _rmed_atom("X-R-1", "CORE", 9, subjects={"governs": "Entity/Continuant"}, relations={"child_of": ["X-R-2"]})
    parent = _rmed_atom("X-R-2", "SOURCES", 8, type="Goal", claim_target_scope_unit="CORE", subjects={"governs": "CORE/Goal"})
    sources = [r796, _fixture_source("CA-D-268"), frozen_source("CA-R-879", graph=True), frozen_source("CA-R-1676", graph=True), *frozen_sources(("structure_authority",))]
    return r796, child, parent, sources


def _parent_reference(metadata: dict[str, Any]) -> tuple[dict[str, Any], ...]:
    return ({"metadata": metadata, "path": Path("/inventory/parent.md")},)


class CurrentGraphAuthoritySemanticsTests(unittest.TestCase):
    def test_manifest_has_all_26_approved_pins_and_preserves_six_extras(self) -> None:
        manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
        sources = manifest["sources"]
        self.assertEqual(set(sources), set(APPROVED_GRAPH_AUTHORITY_IDS) | EXTRAS)
        self.assertEqual(len(APPROVED_GRAPH_AUTHORITY_IDS), 26)
        for identifier, (version, digest, suffix) in CHANGED_PINS.items():
            with self.subTest(identifier=identifier):
                self.assertEqual(sources[identifier]["version"], version)
                self.assertEqual(sources[identifier]["sha256"], digest)
                self.assertTrue(sources[identifier]["source_path"].endswith(suffix))
        self.assertEqual(
            sources["CA-D-305"],
            {
                "version": 16,
                "sha256": "7b1c4f96426e7907c90e5a949b037f26f39458fd769ed04e2b451a16376cdd39",
                "source_path": ".caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/"
                "CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/"
                "CA-SU-13_LAYER_3_PROJECT_CONFIGURATION/07_delivery/"
                "CA-D-305-PROJECT_CONFIGURATION-CORE--carry-projected-atoms-without-new-identity.md",
            },
        )

    def test_current_changed_snapshots_are_exact_and_plan_inherits_six_statuses(self) -> None:
        sources = [_fixture_source("CA-R-1947"), _fixture_source("CA-R-1539")]
        domain = resolve_status_domain(declarations_from_sources(sources), "Plan")
        self.assertEqual(domain["statuses"], ["Draft", "Active", "Archived", "Backlog", "Done", "Canceled"])
        self.assertNotIn("Planned", domain["statuses"])
        self.assertEqual([row["atom_id"] for row in domain["model_sources"]], ["CA-R-1947", "CA-R-1539"])

    def test_plan_status_requires_one_current_base_and_rejects_ambiguous_base(self) -> None:
        plan = declarations_from_sources([_fixture_source("CA-R-1539")])
        with self.assertRaises(StatusModelError) as missing:
            resolve_status_domain(plan, "Plan")
        self.assertEqual(missing.exception.code, "model-missing")

        base = _fixture_source("CA-R-1947")
        with self.assertRaises(StatusModelError) as ambiguous:
            resolve_status_domain(
                declarations_from_sources([base, _fixture_source("CA-R-1539"), copy.deepcopy(base)]),
                "Plan",
            )
        self.assertEqual(ambiguous.exception.code, "model-ambiguous")

    def test_d268_and_r1040_do_not_register_containment_runtime_keys(self) -> None:
        self.assertIn("This source contract does not itself register a new runtime relation key.", _fixture_source("CA-D-268")["text"])
        self.assertIn("does not admit a new runtime relation key", _fixture_source("CA-R-1040")["text"])
        self.assertNotIn("CONTAINS", _INVERSES | _TYPED)
        self.assertNotIn("IS_CONTAINED_BY", _INVERSES | _TYPED)

        metadata = {
            "atom_id": "X-R-1",
            "version": 1,
            "content_role": "Requirement",
            "status": "Active",
            "current_scope_unit": "CORE",
            "tier": 9,
            "relations": {"IS_CONTAINED_BY": ["X-R-2"]},
        }
        result = _check(metadata, [_fixture_source("CA-D-268")])
        self.assertFalse(result.findings)
        self.assertTrue(any("No exact reviewed Relation Kind admission" in row["reason"] for row in result.gaps))

    def test_r796_structural_admission_does_not_claim_parenthood(self) -> None:
        r796, child, parent, sources = _r796_fixture()
        self.assertIn("Structural eligibility alone does not establish parenthood.", r796["text"])
        self.assertIn("parent actually governs the child's contribution", r796["text"])
        # No semantic evidence is supplied or required: this is structural only.
        positive = _check(child, sources, references=_parent_reference(parent), structure=_scope_units())
        self.assertFalse(positive.findings + positive.gaps)

        greater = _check(
            child, sources, references=_parent_reference({**parent, "tier": 10}), structure=_scope_units()
        )
        self.assertFalse(greater.findings + greater.gaps)

        negative_cases = (
            ("sibling", {**parent, "current_scope_unit": "CONFIG"}, _scope_units()),
            ("missing-structure", parent, None),
        )
        for defect, candidate, structure in negative_cases:
            with self.subTest(defect=defect):
                negative = _check(child, sources, references=_parent_reference(candidate), structure=structure)
                self.assertTrue(negative.findings or negative.gaps)


if __name__ == "__main__":
    unittest.main()
