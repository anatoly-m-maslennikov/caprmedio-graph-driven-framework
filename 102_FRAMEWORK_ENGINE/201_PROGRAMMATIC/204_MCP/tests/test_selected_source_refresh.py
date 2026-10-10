"""TDD contract for CA-D-588's closed selected-source pin successor."""
from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path
import re
import shutil
import sys
import tempfile
import unittest
from unittest.mock import patch

MCP = Path(__file__).resolve().parents[1]
if str(MCP) not in sys.path:
    sys.path.insert(0, str(MCP))

from selected_source_refresh import (  # noqa: E402
    RegisteredSourceRefreshError,
    derive_registered_source_refresh,
    derive_registered_source_successor,
    registered_source_refresh,
)
import selected_source_refresh as source_refresh_module  # noqa: E402
import selected_routes as selected_routes_module  # noqa: E402
from selected_routes import selected_manifest_ref  # noqa: E402

REPOSITORY = MCP.parents[2]
GOLDEN_INPUT = MCP / "tests/selected_source_refresh_golden/input_manifest.v7.json"
GOLDEN_SCHEMA4_INPUT = MCP / "tests/selected_source_refresh_golden/input_manifest.schema4.v1.json"
GOLDEN_CONTROLS = MCP / "tests/selected_source_refresh_golden/historical_controls.json"
GOLDEN_D572_READER = MCP / "tests/selected_source_refresh_golden/release_suite_reference_context.d572v13.py"
_HISTORICAL_READER_REF = "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/RELEASE_VERSION/release_suite_reference_context.py"
_M343_REF = (
    ".caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/"
    "201_FEATURE_TOOLS/05_method/"
    "CA-M-343-TOOLS-METHOD--discover-run-and-attest-the-declared-release-suite.md"
)
_O128_REF = (
    ".caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/"
    "000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/09_operations/"
    "CA-O-128-CORE_META_MODEL-ACTION--apply-authorized-atom-lifecycle-changes.md"
)
_O134_REF = (
    ".caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/"
    "000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/09_operations/"
    "CA-O-134-CORE_META_MODEL-ACTION--construct-entities-graph-projection.md"
)
_O137_REF = (
    ".caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/"
    "000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/09_operations/"
    "CA-O-137-CORE_META_MODEL-ACTION--construct-terms-graph-projection.md"
)
_D588_REF = (
    ".caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/"
    "204_FEATURE_MCP/07_delivery/"
    "CA-D-588-MCP-DELIVERY--register-the-prepared-successor-binding-refresh.md"
)
_D588_V1_REF = (
    ".caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/"
    "204_FEATURE_MCP/07_delivery/archive/"
    "CA-D-588-MCP-DELIVERY--register-the-prepared-successor-binding-refresh@1.md"
)
_FROZEN_CARRIERS = {
    _M343_REF: ("ca_m_343_v4.md", "2925b59a15bdacb57625d6492069022546290a6d9e8012cc67306a9329c3c089"),
    _O128_REF: ("ca_o_128_v4.md", "ea36b940a171676977507d366daca9400825e8685018d9c201c15fc5b97eea1c"),
    ".caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/"
    "000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/09_operations/archive/"
    "CA-O-128-CORE_META_MODEL-ACTION--apply-authorized-atom-lifecycle-changes@3.md":
        ("ca_o_128_v3.md", "b5d052e97bae6ada98849380199e5c67cbf090900beb33ca202f7872d56301e8"),
}
_FROZEN_D572_CARRIERS = {
    ".caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/05_method/CA-M-332-TOOLS-METHOD--derive-complete-release-delivery-plan.md": ("ca_m_332_v3.md", "88500268687e6b2c2a5736f0d767d071a085e9d612df83e9cabdd6588793fbfa"),
    ".caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/06_evaluation/CA-E-586-TOOLS-QA_CASE--verify-complete-and-source-bound-release-suite-evidence.md": ("ca_e_586_v3.md", "4be567eff47d0bda089091722bd8008c81b94765445fa1ed6ff10205bea0b7dd"),
    ".caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/07_delivery/CA-D-562-TOOLS-DELIVERY--bind-full-framework-runtime-installation-boundary.md": ("ca_d_562_v2.md", "d6509c48567ec4627616597950d892fb6fba5f287f86dbff2e828b1578f5190b"),
    ".caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/07_delivery/CA-D-567-TOOLS-DELIVERY--bind-validated-compiler-and-package-handoff.md": ("ca_d_567_v3.md", "e5bc56c0940b53699e9c25bb883ac42b24755fc0c1b65411ccc088c83dd76094"),
    ".caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/07_delivery/CA-D-579-TOOLS-DELIVERY--deliver-the-release-suite-driver-and-junit-report-boundary.md": ("ca_d_579_v6.md", "9f52377504f5a1beaa0668ddea62bdad532f3da3e506b8b41f402235591ccadd"),
    ".caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/07_delivery/CA-D-580-TOOLS-DELIVERY--encode-the-private-release-suite-reference-context.md": ("ca_d_580_v4.md", "30221b0d820e1f06022ee74ef2dda270bc4813da847c122f8d4dd64546973e95"),
    "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/203_APPS/WORKFLOW_ORCHESTRATOR/tests/test_docker_e2e.py": ("test_docker_e2e.d572v13.py", "a43359c6b3984c85d8399c5aa371120572a8f3b6fc492f8aad8af66b16e6dbda"),
    "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/203_APPS/WORKFLOW_ORCHESTRATOR/tests/test_selected_workflows_docker_e2e.py": ("test_selected_workflows_docker_e2e.d572v13.py", "48abd23bc8401149f17e1e299cf85b6183986f091bfae70274f2204881279f71"),
}
_MOVED_FIXTURE_SOURCES = {
    _D588_REF: _D588_V1_REF,
    _O134_REF: _O134_REF.replace("/09_operations/", "/09_operations/archive/").replace(".md", "@2.md"),
    _O137_REF: _O137_REF.replace("/09_operations/", "/09_operations/archive/").replace(".md", "@2.md"),
    (
        ".caprmedio_caprmedio/03_plan/15-CA-P-1117-EPIC--harvest-and-implement-session-derived-operations/"
        "08-CA-P-1520-TASK--deliver-read-only-artifact-and-journal-query-workflows/"
        "29-CA-P-1618-TASK--accept-current-artifact-query-source-frontier.md"
    ): (
        ".caprmedio_caprmedio/03_plan/done/15-CA-P-1117-EPIC--harvest-and-implement-session-derived-operations/"
        "08-CA-P-1520-TASK--deliver-read-only-artifact-and-journal-query-workflows/"
        "29-CA-P-1618-TASK--accept-current-artifact-query-source-frontier.md"
    ),
    (
        ".caprmedio_caprmedio/03_plan/15-CA-P-1117-EPIC--harvest-and-implement-session-derived-operations/"
        "10-CA-P-1620-TASK--deliver-release-version-workflow/done/"
        "02-CA-P-1622-TASK--review-release-version-source-and-admission.md"
    ): (
        ".caprmedio_caprmedio/03_plan/done/15-CA-P-1117-EPIC--harvest-and-implement-session-derived-operations/"
        "10-CA-P-1620-TASK--deliver-release-version-workflow/done/"
        "02-CA-P-1622-TASK--review-release-version-source-and-admission.md"
    ),
    (
        ".caprmedio_caprmedio/03_plan/15-CA-P-1117-EPIC--harvest-and-implement-session-derived-operations/"
        "08-CA-P-1520-TASK--deliver-read-only-artifact-and-journal-query-workflows/"
        "15-CA-P-1535-TASK--accept-final-journal-query-source.md"
    ): (
        ".caprmedio_caprmedio/03_plan/done/15-CA-P-1117-EPIC--harvest-and-implement-session-derived-operations/"
        "08-CA-P-1520-TASK--deliver-read-only-artifact-and-journal-query-workflows/"
        "15-CA-P-1535-TASK--accept-final-journal-query-source.md"
    ),
}


class RegisteredSelectedSourceRefreshTest(unittest.TestCase):
    """The derivation is pure; source and lifecycle checks belong at its boundaries."""

    @staticmethod
    def _v1_registration() -> dict[str, object]:
        text = (REPOSITORY / _D588_V1_REF).read_text(encoding="utf-8")
        match = re.search(r"(?ms)^### Accepted source revision\s*\n\s*```json\s*\n(.*?)\n```\s*$", text)
        assert match is not None
        value = json.loads(match.group(1))
        assert isinstance(value, dict)
        return value

    @staticmethod
    def _pin(*, version: int, digest: str) -> dict[str, object]:
        return {
            "atom_id": "CA-O-128",
            "version": version,
            "source_path": (
                ".caprmedio_caprmedio/000_CAPRMEDIO_framework/"
                "00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/"
                "001_CORE_META_MODEL/09_operations/"
                "CA-O-128-CORE_META_MODEL-ACTION--apply-authorized-atom-lifecycle-changes.md"
            ),
            "digest": digest,
        }

    def _manifest(self, registration: dict[str, object]) -> dict[str, object]:
        prior = registration["prior_pin"]
        assert isinstance(prior, dict)
        routes: list[dict[str, object]] = []
        for route_name in registration["routes"]:
            routes.append({
                "route": route_name,
                "workflow": {"atom_id": "CA-O-1", "version": 1, "source_path": "workflow.md", "digest": "a" * 64},
                "ordered_steps": [{"step": {"atom_id": "CA-O-2", "version": 1, "source_path": "step.md", "digest": "b" * 64},
                                   "action": copy.deepcopy(prior)}],
                "ordered_actions": [copy.deepcopy(prior)],
                "native_action_calls": [],
                "entry_step": "CA-O-2",
                "on_result": [{"from": "CA-O-2", "condition": "ok", "to": "complete"}],
                "mutation_capable": True,
            })
        routes.extend({"route": name, "unchanged": True} for name in ("other-a", "other-b"))
        return {
            "schema_version": 1,
            "source_freshness": {"selected_binding_digest": "0" * 64},
            "query_source_admissions": [{"route": "query", "unchanged": True}],
            "routes": routes,
            "canonical_manifest_sha256": "1" * 64,
            "release_source_admissions": [{"unchanged": True}],
        }

    def test_closed_registration_is_the_exact_d588_schema4_revision(self) -> None:
        registration = registered_source_refresh()
        self.assertEqual(4, registration["schema_version"])
        self.assertEqual("epic1848-exact-three-pin-binding-repair-20261011", registration["registration_id"])
        self.assertEqual("CA-P-1866", registration["repair_task_id"])
        self.assertEqual("bee103e7604ddbe5912bce5ea31d79d18c3e9efbec22bd6557ef0875222b78bf", registration["input_manifest_sha256"])
        self.assertEqual("80b0cecd066fa421608a517b296664580ffe575a56e8dbd4bdb28ea4df682774", registration["input_canonical_manifest_sha256"])
        self.assertEqual(17, registration["input_route_count"])
        self.assertEqual(3, registration["pin_occurrences"])
        self.assertEqual(["CA-O-030", "CA-M-343", "CA-D-579"], [row["prior_pin"]["atom_id"] for row in registration["replacements"]])
        self.assertEqual("6d1e3aaacf33d4c3cb645f9ed46641dac38b6480773a080074bac51249c143f4", registration["expected_manifest_sha256"])

    def test_successor_replaces_exactly_eight_registered_action_pins_and_rederives_only_digests(self) -> None:
        registration = self._v1_registration()
        manifest = self._manifest(registration)
        before = copy.deepcopy(manifest)

        candidate = derive_registered_source_successor(manifest, registration)

        self.assertEqual(before["query_source_admissions"], candidate["query_source_admissions"])
        self.assertEqual(before["release_source_admissions"], candidate["release_source_admissions"])
        self.assertEqual(before["routes"][4:], candidate["routes"][4:])
        self.assertNotEqual(before["source_freshness"]["selected_binding_digest"], candidate["source_freshness"]["selected_binding_digest"])
        self.assertNotEqual(before["canonical_manifest_sha256"], candidate["canonical_manifest_sha256"])
        for route in candidate["routes"][:4]:
            self.assertEqual(registration["current_pin"], route["ordered_steps"][0]["action"])
            self.assertEqual(registration["current_pin"], route["ordered_actions"][0])

    def test_topology_or_pin_occurrence_changes_refuse_without_mutating_input(self) -> None:
        registration = self._v1_registration()
        manifest = self._manifest(registration)
        manifest["routes"][0]["ordered_actions"] = []
        broken_before = copy.deepcopy(manifest)

        with self.assertRaises(RegisteredSourceRefreshError):
            derive_registered_source_successor(manifest, registration)

        self.assertEqual(broken_before, manifest)

    def test_schema4_replaces_only_three_registered_pins_and_rederives_only_digests(self) -> None:
        registration = registered_source_refresh()
        manifest = json.loads(GOLDEN_SCHEMA4_INPUT.read_text(encoding="utf-8"))
        before = copy.deepcopy(manifest)
        candidate = derive_registered_source_successor(manifest, registration)

        self.assertEqual([row["route"] for row in before["routes"]], [row["route"] for row in candidate["routes"]])
        self.assertEqual(before["routes"][:1], candidate["routes"][:1])
        self.assertEqual(before["routes"][2:], candidate["routes"][2:])
        self.assertEqual(before["query_source_admissions"], candidate["query_source_admissions"])
        self.assertEqual(before["public_release_source_admissions"], candidate["public_release_source_admissions"])
        self.assertEqual(registration["replacements"][0]["current_pin"], candidate["routes"][1]["native_action_calls"][0])
        frontier = candidate["release_source_admissions"][0]["rmed_frontier"]
        self.assertEqual(registration["replacements"][1]["current_pin"], frontier[11])
        self.assertEqual(registration["replacements"][2]["current_pin"], frontier[31])
        self.assertNotEqual(before["source_freshness"]["selected_binding_digest"], candidate["source_freshness"]["selected_binding_digest"])
        self.assertNotEqual(before["canonical_manifest_sha256"], candidate["canonical_manifest_sha256"])

    def test_schema4_refuses_nonregistered_route_drift_without_mutating_input(self) -> None:
        registration = registered_source_refresh()
        manifest = json.loads(GOLDEN_SCHEMA4_INPUT.read_text(encoding="utf-8"))
        manifest["routes"][0]["route"] = "other_route"
        before = copy.deepcopy(manifest)

        with self.assertRaises(RegisteredSourceRefreshError):
            derive_registered_source_successor(manifest, registration)

        self.assertEqual(before, manifest)

class RegisteredSchema4SourceRefreshTest(unittest.TestCase):
    """The current closed registration changes only three fixed seventeen-route Pins."""

    _PIN_FIELDS = {"atom_id", "version", "source_path", "digest"}

    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory(ignore_cleanup_errors=True)
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        self.registration = registered_source_refresh()
        self.assertEqual(4, self.registration["schema_version"])
        manifest_ref = selected_manifest_ref(REPOSITORY)
        self.manifest_bytes = GOLDEN_SCHEMA4_INPUT.read_bytes()
        self.assertEqual(self.registration["input_manifest_sha256"], hashlib.sha256(self.manifest_bytes).hexdigest())
        self.manifest = json.loads(self.manifest_bytes)
        target = self.root / manifest_ref
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(self.manifest_bytes)
        self._copy(_D588_REF)
        for source_path in self._pin_paths(self.manifest):
            self._copy(source_path)
        import release_source_admission as admission_module
        for source_root in (*admission_module._RMED_ROOTS.values(), *admission_module._TOOLS_RMED_ROOTS.values()):
            (self.root / source_root).mkdir(parents=True, exist_ok=True)
        for replacement in self.registration["replacements"]:
            self._copy(replacement["current_pin"]["source_path"])
            if "prior_receipt_ref" in replacement:
                self._copy(replacement["prior_receipt_ref"])
            else:
                self._copy(replacement["prior_archive_path"])
        public_release = MCP.parent / "201_TOOLS" / "PUBLIC_RELEASE"
        if str(public_release) not in sys.path:
            sys.path.insert(0, str(public_release))
        from selected_admission import AUTHORITY_REF as public_authority_ref
        for relative in (
            self.manifest["source_freshness"]["selected_source_registry_ref"],
            ".caprmedio_caprmedio/caprmedio_project_settings.toml",
            ".caprmedio_caprmedio/project_structure.toml",
            admission_module.AUTHORITY_REF,
            public_authority_ref,
        ):
            self._copy(relative)

    def _copy(self, relative: str) -> None:
        destination = self.root / relative
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(REPOSITORY / relative, destination)

    @classmethod
    def _pin_paths(cls, value: object) -> set[str]:
        if isinstance(value, dict):
            if set(value) == cls._PIN_FIELDS:
                return {value["source_path"]}
            return set().union(*(cls._pin_paths(item) for item in value.values()))
        if isinstance(value, list):
            return set().union(*(cls._pin_paths(item) for item in value))
        return set()

    def _derive(self) -> tuple[dict[str, object], dict[str, object], bytes, Path]:
        return derive_registered_source_refresh(self.root)

    def test_schema4_reader_preserves_routes_and_replaces_only_closed_pin_locations(self) -> None:
        current, candidate, payload, carrier = self._derive()
        self.assertEqual((self.root / selected_manifest_ref(REPOSITORY)).resolve(), carrier)
        self.assertEqual(self.manifest, current)
        self.assertEqual(self.manifest["routes"][:1], candidate["routes"][:1])
        self.assertEqual(self.manifest["routes"][2:], candidate["routes"][2:])
        for field in ("selected_binding_ref", "selected_source_registry_ref", "selected_source_registry_version", "selected_source_registry_digest"):
            self.assertEqual(self.manifest["source_freshness"][field], candidate["source_freshness"][field])
        self.assertEqual(self.registration["replacements"][0]["current_pin"], candidate["routes"][1]["native_action_calls"][0])
        frontier = candidate["release_source_admissions"][0]["rmed_frontier"]
        self.assertEqual(self.registration["replacements"][1]["current_pin"], frontier[11])
        self.assertEqual(self.registration["replacements"][2]["current_pin"], frontier[31])
        self.assertEqual(json.loads(payload), candidate)

    def test_schema4_current_plan_is_effect_free_and_propagates_registered_metadata(self) -> None:
        from release_manifest_publisher import plan_release_manifest_refresh

        path = self.root / selected_manifest_ref(self.root)
        before = path.read_bytes()
        plan = plan_release_manifest_refresh(self.root)

        self.assertEqual("plan", plan["mode"])
        self.assertEqual("refresh", plan["publication_operation"])
        self.assertEqual(hashlib.sha256(before).hexdigest(), plan["observed_input_sha256"])
        self.assertEqual(17, len(plan["current_route_names"]))
        self.assertEqual(plan["current_route_names"], plan["candidate_route_names"])
        self.assertEqual(4, plan["source_refresh_schema_version"])
        self.assertEqual(self.registration["registration_id"], plan["source_refresh_registration_id"])
        self.assertEqual("f903ad67c3b92d7edd2415107f467be42bce1c53d259f440ac1fdb513fa69d5f", plan["candidate_canonical_manifest_sha256"])
        self.assertEqual(before, path.read_bytes())

    def test_schema4_reader_refuses_input_byte_drift_before_derivation(self) -> None:
        manifest = self.root / selected_manifest_ref(REPOSITORY)
        manifest.write_bytes(manifest.read_bytes() + b"\ninput drift")
        with self.assertRaises(RegisteredSourceRefreshError):
            self._derive()

    def test_schema4_reader_requires_each_current_pin_before_validation(self) -> None:
        source = self.root / self.registration["replacements"][1]["current_pin"]["source_path"]
        source.write_bytes(source.read_bytes() + b"\ncurrent source drift")
        with patch.object(source_refresh_module, "validate_selected_manifest_document", side_effect=AssertionError("validation must not run")):
            with self.assertRaises(RegisteredSourceRefreshError):
                derive_registered_source_refresh(self.root)


class RegisteredSourceRefreshE2ETest(unittest.TestCase):
    """A disposable closure of the real D588 16-route historical carrier."""

    @staticmethod
    def _pin_paths(value: object) -> set[str]:
        found: set[str] = set()
        if isinstance(value, dict):
            source = value.get("source_path")
            if isinstance(source, str):
                found.add(source)
            for item in value.values():
                found.update(RegisteredSourceRefreshE2ETest._pin_paths(item))
        elif isinstance(value, list):
            for item in value:
                found.update(RegisteredSourceRefreshE2ETest._pin_paths(item))
        return found

    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory(ignore_cleanup_errors=True)
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        (self.root / ".git").mkdir()
        source_manifest = GOLDEN_INPUT
        self.manifest_bytes = source_manifest.read_bytes()
        self.manifest = json.loads(self.manifest_bytes)
        self.assertEqual("5ca6c9907a4dffbe84319b7d4e391c6242e1969cfea5902845e50f0bd8ae3012", hashlib.sha256(self.manifest_bytes).hexdigest())
        self.assertEqual(16, len(self.manifest["routes"]))
        # This D588 fixture predates the plan-path relocation.  Its immutable
        # raw manifest, not the current production frontier, is its authority.
        query_specs = tuple(copy.deepcopy(self.manifest["query_source_admissions"]))
        self.assertEqual(2, len(query_specs))
        query_patch = patch.object(selected_routes_module, "_QUERY_SOURCE_ADMISSION_SPECS", query_specs)
        query_patch.start()
        self.addCleanup(query_patch.stop)
        manifest_target = self.root / selected_manifest_ref(REPOSITORY)
        manifest_target.parent.mkdir(parents=True, exist_ok=True)
        manifest_target.write_bytes(self.manifest_bytes)
        controls = json.loads(GOLDEN_CONTROLS.read_text(encoding="utf-8"))["carriers"]
        for relative, contents in controls.items():
            target = self.root / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(contents, encoding="utf-8")
        # Schema 1's retained reader validates only its closed registration
        # carriers.  The current Project's D572 source tree is intentionally
        # outside this historical derivation and its final validation is
        # patched below.
        paths = {
            ".caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/204_FEATURE_MCP/07_delivery/CA-D-588-MCP-DELIVERY--register-the-prepared-successor-binding-refresh.md",
            ".caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/09_operations/archive/CA-O-128-CORE_META_MODEL-ACTION--apply-authorized-atom-lifecycle-changes@3.md",
            ".caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/REPLACE_ATOM/04_requirement/CA-R-1041-TOOLS--coordinate-atom-replacement-intent.md",
        }
        paths.difference_update(_FROZEN_CARRIERS | _FROZEN_D572_CARRIERS)
        for relative in paths:
            self._copy(relative)
        for relative, (fixture_name, digest) in _FROZEN_CARRIERS.items():
            source = GOLDEN_INPUT.parent / fixture_name
            raw = source.read_bytes()
            self.assertEqual(digest, hashlib.sha256(raw).hexdigest(), source)
            target = self.root / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(raw)
        for relative, (fixture_name, digest) in _FROZEN_D572_CARRIERS.items():
            raw = (GOLDEN_INPUT.parent / fixture_name).read_bytes()
            self.assertEqual(digest, hashlib.sha256(raw).hexdigest())
            target = self.root / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(raw)

    def _copy(self, relative: str) -> None:
        source = REPOSITORY / _MOVED_FIXTURE_SOURCES.get(relative, relative)
        destination = self.root / relative
        if destination.exists():
            return
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, destination)

    def test_archived_schema1_reader_derives_the_exact_successor_in_isolation(self) -> None:
        with patch.object(
            source_refresh_module, "validate_selected_manifest_document", side_effect=lambda _root, value: copy.deepcopy(value),
        ):
            current, candidate, payload, carrier = derive_registered_source_refresh(self.root)
        self.assertEqual(self.manifest_bytes, carrier.read_bytes())
        self.assertEqual(16, len(current["routes"]))
        self.assertEqual(16, len(candidate["routes"]))
        self.assertEqual("c0edfd130a32386258397da81796d9efab6c1154b17666419edc988d76efc9ba", current["canonical_manifest_sha256"])
        self.assertEqual("9671de66fd510f1c5d77a66e4376a9388e3448d5842ef54638d272da6f08bc9e", candidate["canonical_manifest_sha256"])
        self.assertEqual(102964, len(payload))

    def test_real_reader_refuses_tampered_input_and_registered_carriers_before_effects(self) -> None:
        carrier = self.root / selected_manifest_ref(self.root)
        checks = [
            (carrier, b"\nraw-input-drift"),
            (self.root / ".caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/09_operations/archive/CA-O-128-CORE_META_MODEL-ACTION--apply-authorized-atom-lifecycle-changes@3.md", b"\narchive-drift"),
            (self.root / ".caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/09_operations/CA-O-128-CORE_META_MODEL-ACTION--apply-authorized-atom-lifecycle-changes.md", b"\ncurrent-action-drift"),
            (self.root / ".caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/REPLACE_ATOM/04_requirement/CA-R-1041-TOOLS--coordinate-atom-replacement-intent.md", b"\nrequirement-drift"),
        ]
        for path, drift in checks:
            original = path.read_bytes()
            path.write_bytes(original + drift)
            with self.assertRaises(RegisteredSourceRefreshError):
                derive_registered_source_refresh(self.root)
            self.assertEqual(original + drift, path.read_bytes())
            path.write_bytes(original)

        registration = self.root / ".caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/204_FEATURE_MCP/07_delivery/CA-D-588-MCP-DELIVERY--register-the-prepared-successor-binding-refresh.md"
        original = registration.read_bytes()
        registration.write_bytes(original.replace(b'"schema_version": 1,', b'"schema_version": 1,\n  "schema_version": 1,', 1))
        with self.assertRaises(RegisteredSourceRefreshError):
            derive_registered_source_refresh(self.root)

if __name__ == "__main__":
    unittest.main()
