"""Closed reader checks for the one O030@6 -> @7 selected-source repair."""
from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path
import shutil
import sys
import tempfile
import unittest

MCP = Path(__file__).resolve().parents[1]
if str(MCP) not in sys.path:
    sys.path.insert(0, str(MCP))

from release_manifest_publisher import plan_release_manifest_refresh  # noqa: E402
from selected_routes import selected_manifest_ref  # noqa: E402
from selected_source_refresh import (  # noqa: E402
    RegisteredSourceRefreshError,
    derive_registered_source_refresh,
    derive_registered_source_successor,
    registered_source_refresh,
)


REPOSITORY = MCP.parents[2]
GOLDEN_SCHEMA4_INPUT = MCP / "tests/selected_source_refresh_golden/input_manifest.schema4.v1.json"
_D588_REF = (
    ".caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/"
    "204_FEATURE_MCP/07_delivery/"
    "CA-D-588-MCP-DELIVERY--register-the-prepared-successor-binding-refresh.md"
)
_D588_V4_REF = (
    ".caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/"
    "204_FEATURE_MCP/07_delivery/archive/"
    "CA-D-588-MCP-DELIVERY--register-the-prepared-successor-binding-refresh@5.md"
)
_O030_REF = (
    ".caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/"
    "201_FEATURE_TOOLS/ATOM_UPDATE/09_operations/"
    "CA-O-030-TOOLS-ACTION--update-sealed-caprmedio-atom-carriers.md"
)
_O030_V6_REF = _O030_REF.replace("/09_operations/", "/09_operations/archive/").replace(".md", "@6.md")
_PIN_FIELDS = {"atom_id", "version", "source_path", "digest"}


class RegisteredSchema5SourceRefreshTest(unittest.TestCase):
    """Schema 5 has one non-discoverable, read-only candidate derivation."""

    def setUp(self) -> None:
        self.raw = self._schema5_input_bytes()
        self.manifest = json.loads(self.raw)
        self.root = self._project_with_schema5_input()
        self.registration = registered_source_refresh(self.root)
        self.assertEqual(5, self.registration["schema_version"])
        self.assertEqual(self.registration["input_manifest_sha256"], hashlib.sha256(self.raw).hexdigest())

    @staticmethod
    def _registration_from(relative: str) -> dict[str, object]:
        text = (REPOSITORY / relative).read_text(encoding="utf-8")
        _, _, json_text = text.partition("```json\n")
        json_text, _, _ = json_text.partition("\n```")
        value = json.loads(json_text)
        assert isinstance(value, dict)
        return value

    @classmethod
    def _schema5_input_bytes(cls) -> bytes:
        """Reconstruct immutable O030@6 input from the frozen schema-4 carrier."""
        schema4 = cls._registration_from(_D588_V4_REF)
        manifest = json.loads(GOLDEN_SCHEMA4_INPUT.read_text(encoding="utf-8"))
        candidate = derive_registered_source_successor(manifest, schema4)
        payload = (json.dumps(candidate, ensure_ascii=False, allow_nan=False, sort_keys=True, separators=(",", ":")) + "\n").encode("utf-8")
        assert hashlib.sha256(payload).hexdigest() == "6d1e3aaacf33d4c3cb645f9ed46641dac38b6480773a080074bac51249c143f4"
        return payload

    @staticmethod
    def _pin_paths(value: object) -> set[str]:
        if isinstance(value, dict):
            if set(value) == _PIN_FIELDS:
                source_path = value["source_path"]
                return {source_path} if isinstance(source_path, str) else set()
            return set().union(*(RegisteredSchema5SourceRefreshTest._pin_paths(item) for item in value.values()))
        if isinstance(value, list):
            return set().union(*(RegisteredSchema5SourceRefreshTest._pin_paths(item) for item in value))
        return set()

    @staticmethod
    def _copy_into(root: Path, relative: str) -> None:
        destination = root / relative
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(REPOSITORY / relative, destination)

    def _project_with_schema5_input(self) -> Path:
        temporary = tempfile.TemporaryDirectory(ignore_cleanup_errors=True)
        self.addCleanup(temporary.cleanup)
        root = Path(temporary.name)
        manifest_ref = selected_manifest_ref(REPOSITORY)
        target = root / manifest_ref
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(self.raw)
        self._copy_into(root, _D588_REF)
        for source_path in self._pin_paths(self.manifest):
            self._copy_into(root, source_path)
        self._copy_into(root, _O030_V6_REF)
        import release_source_admission as admission_module
        for source_root in (*admission_module._RMED_ROOTS.values(), *admission_module._TOOLS_RMED_ROOTS.values()):
            (root / source_root).mkdir(parents=True, exist_ok=True)
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
            self._copy_into(root, relative)
        return root

    def test_closed_registration_and_exact_one_pin_candidate(self) -> None:
        self.assertEqual("epic1848-exact-o030-v7-binding-repair-20261011", self.registration["registration_id"])
        self.assertEqual(17, self.registration["input_route_count"])
        self.assertEqual(1, self.registration["pin_occurrences"])
        row = self.registration["replacements"][0]
        self.assertEqual("update_atom", row["route"])
        self.assertEqual(["native_action_calls[0]"], row["occurrences"])
        self.assertEqual(6, row["prior_pin"]["version"])
        self.assertEqual("19097af83287005dae4d55e4b4da2234acce9e9f92b0f70671afb831bd8b256b", row["prior_pin"]["digest"])
        self.assertEqual(7, row["current_pin"]["version"])
        self.assertEqual("c2d70fa275a075d2fbc978cab246158cfd8413cec88716521336736d0bf060cc", row["current_pin"]["digest"])

        before = copy.deepcopy(self.manifest)
        candidate = derive_registered_source_successor(self.manifest, self.registration)
        self.assertEqual(before, self.manifest)
        self.assertEqual([route["route"] for route in before["routes"]], [route["route"] for route in candidate["routes"]])
        update_index = [route["route"] for route in before["routes"]].index("update_atom")
        self.assertEqual(before["routes"][:update_index], candidate["routes"][:update_index])
        self.assertEqual(before["routes"][update_index + 1:], candidate["routes"][update_index + 1:])
        old_route = copy.deepcopy(before["routes"][update_index])
        new_route = copy.deepcopy(candidate["routes"][update_index])
        old_route["native_action_calls"][0] = new_route["native_action_calls"][0]
        self.assertEqual(old_route, new_route)
        self.assertEqual(row["current_pin"], candidate["routes"][update_index]["native_action_calls"][0])
        self.assertEqual("cd05362d6f805902cf922151bc5135a91cb7ef267b0e85bfadf8e5d265a09284", candidate["source_freshness"]["selected_binding_digest"])
        self.assertEqual("2c1bd6a93b1362fe1b2a457c2f5bf413a825748825027e607bb4d0f17ec55e25", candidate["canonical_manifest_sha256"])
        payload = (json.dumps(candidate, ensure_ascii=False, allow_nan=False, sort_keys=True, separators=(",", ":")) + "\n").encode("utf-8")
        self.assertEqual("f898d30aeabe712ee8ae2545d732e6acde94efc8a5597db11229380937fbff52", hashlib.sha256(payload).hexdigest())

    def test_planner_is_effect_free_and_marks_only_the_exact_schema5_candidate(self) -> None:
        path = self.root / selected_manifest_ref(REPOSITORY)
        before = path.read_bytes()
        plan = plan_release_manifest_refresh(self.root)
        self.assertEqual("plan", plan["mode"])
        self.assertEqual(hashlib.sha256(before).hexdigest(), plan["observed_input_sha256"])
        self.assertEqual(5, plan["source_refresh_schema_version"])
        self.assertEqual("epic1848-exact-o030-v7-binding-repair-20261011", plan["source_refresh_registration_id"])
        self.assertEqual(before, path.read_bytes())

    def test_duplicate_other_pin_route_and_already_repaired_inputs_refuse_without_mutation(self) -> None:
        row = self.registration["replacements"][0]
        update_index = [route["route"] for route in self.manifest["routes"]].index("update_atom")
        cases: list[tuple[str, dict[str, object]]] = []
        duplicate = copy.deepcopy(self.manifest)
        duplicate["routes"][0]["native_action_calls"].append(copy.deepcopy(row["prior_pin"]))
        cases.append(("duplicate", duplicate))
        other_pin = copy.deepcopy(self.manifest)
        other_pin["routes"][update_index]["native_action_calls"][0] = copy.deepcopy(row["current_pin"])
        cases.append(("other-pin", other_pin))
        route = copy.deepcopy(self.manifest)
        route["routes"][update_index]["route"] = "not_update_atom"
        cases.append(("route", route))
        repaired = derive_registered_source_successor(self.manifest, self.registration)
        cases.append(("already-repaired", repaired))
        for label, manifest in cases:
            with self.subTest(label=label):
                before = copy.deepcopy(manifest)
                with self.assertRaises(RegisteredSourceRefreshError):
                    derive_registered_source_successor(manifest, self.registration)
                self.assertEqual(before, manifest)

    def test_reader_refuses_input_current_and_prior_archive_drift_before_effects(self) -> None:
        for label, relative in (
            ("input", selected_manifest_ref(REPOSITORY)),
            ("current", _O030_REF),
            ("archive", _O030_V6_REF),
        ):
            with self.subTest(label=label):
                root = self._project_with_schema5_input()
                path = root / relative
                original = path.read_bytes()
                path.write_bytes(original + b"\ndrift")
                with self.assertRaises(RegisteredSourceRefreshError):
                    derive_registered_source_refresh(root)
                self.assertEqual(original + b"\ndrift", path.read_bytes())


if __name__ == "__main__":
    unittest.main()
