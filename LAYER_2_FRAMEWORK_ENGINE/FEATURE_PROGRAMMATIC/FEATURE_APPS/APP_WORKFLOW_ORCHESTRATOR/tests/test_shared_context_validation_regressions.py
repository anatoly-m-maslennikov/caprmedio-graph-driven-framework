"""Source-backed regressions for current shared-context packet validation."""

from __future__ import annotations

import copy
import hashlib
from pathlib import Path
import sys
import tempfile
from typing import Any
import unittest


APP = Path(__file__).resolve().parents[1]
PROJECT_ROOT = APP.parents[3]
for location in (APP, APP / "tests"):
    if str(location) not in sys.path:
        sys.path.insert(0, str(location))

from shared_context_current_fixture import CurrentSharedContextFixture  # noqa: E402
from shared_context_packets import ACTIONS  # noqa: E402
from shared_context_validation import validate_current_shared_packet  # noqa: E402
from shared_context_validation_rmed import validate_rmed_inputs  # noqa: E402


class SharedContextValidationRegressionTests(unittest.TestCase):
    def setUp(self) -> None:
        self.fixture = CurrentSharedContextFixture.load()
        self.temporary = tempfile.TemporaryDirectory(
            dir=PROJECT_ROOT / ".caprmedio_tmp", ignore_cleanup_errors=True
        )
        self.addCleanup(self.temporary.cleanup)
        self.root = self.fixture.materialize(Path(self.temporary.name) / "project")
        for row in self.fixture._support_rows():
            target = self.root / str(row["path"])
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(self.fixture.support_source_bytes(str(row["atom_id"])))
        pins = {pin["atom_id"]: dict(pin) for pin in self.fixture.source_pins()}
        self.profile: dict[str, Any] = {
            "workflow": pins["CA-O-016"],
            "entry_step": "CA-O-231",
            "steps": {
                step: {"step": pins[step], "action": pins[action]}
                for step, action in ACTIONS.items()
            },
        }
        self.methods = self.fixture.support_inventory["method_projection"]

    def _packet(self, step: str = "CA-O-231") -> dict[str, Any]:
        parameters = self.fixture.native_implementation_parameters()
        return copy.deepcopy({**parameters["base_packet"], **parameters["step_packets"][step]})

    def _direct_packet(
        self, step: str = "CA-O-231", *, include_projection: bool = False
    ) -> dict[str, Any]:
        packet = self._packet(step)
        projection = packet.pop("method_projection")
        if include_projection:
            packet["method_projection"] = projection
        packet["methods"] = []
        for source in projection["sources"]:
            row = dict(source)
            row.pop("fixture_path", None)
            row["content"] = (self.root / str(row["path"])).read_text(encoding="utf-8")
            packet["methods"].append(row)
        return packet

    def _promote_workflow_to_v18(self, packet: dict[str, Any]) -> dict[str, Any]:
        source_bindings = packet["source_bindings"]
        workflow = next(row for row in source_bindings if row["atom_id"] == "CA-O-016")
        target = self.root / str(workflow["source_path"])
        content = target.read_text(encoding="utf-8")
        if content.count("version: 17") == 1:
            updated = content.replace("version: 17", "version: 18", 1)
            target.write_text(updated, encoding="utf-8")
        else:
            self.assertEqual(1, content.count("version: 18"))
            updated = content
        digest = hashlib.sha256(updated.encode()).hexdigest()
        profile = copy.deepcopy(self.profile)
        for row in profile["workflow"], workflow, *packet["selected_project"]["source_references"]:
            if row["atom_id"] == "CA-O-016":
                row["version"] = 18
                row["sha256"] = digest
        return profile

    def _trusted_direct_methods(self) -> dict[str, Any]:
        return {
            "sources": [
                {
                    **source,
                    "content": (self.root / str(source["path"])).read_text(encoding="utf-8"),
                }
                for source in self.methods["sources"]
            ]
        }

    def _validate_direct(self, packet: dict[str, Any], step: str = "CA-O-231") -> dict[str, Any]:
        profile = self._promote_workflow_to_v18(packet)
        row = profile["steps"][step]
        result = validate_current_shared_packet(
            packet,
            workflow_definition=profile["workflow"],
            step_definition=row["step"],
            action_definition=row["action"],
            trusted_workflow_binding=profile,
            selected_project_root=self.root,
            trusted_methods=self._trusted_direct_methods(),
        )
        return result.as_result()

    def _validate(
        self,
        packet: object,
        step: str = "CA-O-231",
        *,
        profile: object | None = None,
        methods: object | None = None,
    ) -> dict[str, Any]:
        selected = self.profile if profile is None else profile
        assert isinstance(selected, dict)
        row = selected["steps"][step]
        result = validate_current_shared_packet(
            packet,
            workflow_definition=selected["workflow"],
            step_definition=row["step"],
            action_definition=row["action"],
            trusted_workflow_binding=selected,
            selected_project_root=self.root,
            trusted_method_projection=self.methods if methods is None else methods,
        )
        return result.as_result()

    def _methods_content(self, packet: dict[str, Any]) -> str:
        rows = packet["method_projection"]["sources"]
        return "\n\n".join(
            (self.root / row["path"]).read_text(encoding="utf-8")
            for row in sorted(rows, key=lambda row: (row["atom_id"], row["version"]))
        )

    def test_initial_preparation_accepts_no_plan_and_review_needs_no_write_capability(self) -> None:
        initial = self._packet()
        initial.pop("plan_item")
        self.assertEqual("accepted", self._validate(initial)["status"])
        review = self._packet("CA-O-230")
        review["review_phase"] = "preliminary"
        review.pop("workspace")
        review["permissions"] = {"allowed": True}
        self.assertEqual("accepted", self._validate(review, "CA-O-230")["status"])

    def test_exhausted_retry_is_valid_blocked_outcome(self) -> None:
        packet = self._packet("CA-O-096")
        packet["retry"]["consumed"] = packet["retry"]["effective_limit"]
        self.assertEqual("retry_blocked", self._validate(packet, "CA-O-096")["status"])

    def test_pydantic_boundary_rejects_wrong_envelope_field_type(self) -> None:
        packet = self._packet()
        packet["requirements"] = "not-a-source-list"
        result = self._validate(packet)
        self.assertEqual("invalid_packet", result["status"])
        self.assertEqual("packet", result["warnings"][0]["code"])
        packet = self._packet()
        packet["typo_field"] = "never silently retained"
        result = self._validate(packet)
        self.assertEqual("invalid_packet", result["status"])
        self.assertEqual("packet", result["warnings"][0]["code"])

    def test_unreadable_project_artifact_is_a_structured_invalid_packet(self) -> None:
        settings = self.root / ".caprmedio_caprmedio/caprmedio_project_settings.toml"
        settings.write_bytes(b"\xff")
        result = self._validate(self._packet())
        self.assertEqual("invalid_packet", result["status"])
        self.assertEqual("project_artifact", result["warnings"][0]["code"])

    def test_method_projection_requires_external_complete_inventory(self) -> None:
        packet = self._packet()
        packet["method_projection"]["sources"] = packet["method_projection"]["sources"][:-1]
        packet["method_projection"]["content"] = self._methods_content(packet)
        self.assertEqual("method_authority", self._validate(packet)["warnings"][0]["code"])
        self.assertEqual(
            "method_authority", self._validate(self._packet(), methods={})["warnings"][0]["code"]
        )

    def test_direct_methods_accept_complete_current_inventory_without_projection(self) -> None:
        result = self._validate_direct(self._direct_packet())
        self.assertEqual("accepted", result["status"])

    def test_direct_methods_may_keep_a_legacy_projection_without_replacing_direct_rows(
        self,
    ) -> None:
        result = self._validate_direct(self._direct_packet(include_projection=True))
        self.assertEqual("accepted", result["status"])

    def test_direct_methods_require_complete_independent_inventory(self) -> None:
        packet = self._direct_packet()
        packet["methods"] = packet["methods"][:-1]
        self.assertEqual("method_authority", self._validate_direct(packet)["warnings"][0]["code"])

        trusted = {"sources": self.methods["sources"][:-1]}
        packet = self._direct_packet()
        profile = self._promote_workflow_to_v18(packet)
        row = profile["steps"]["CA-O-231"]
        result = validate_current_shared_packet(
            packet,
            workflow_definition=profile["workflow"],
            step_definition=row["step"],
            action_definition=row["action"],
            trusted_workflow_binding=profile,
            selected_project_root=self.root,
            trusted_methods=trusted,
        )
        self.assertEqual("method_authority", result.warnings[0]["code"])

    def test_direct_methods_reject_drift_and_invalid_role_or_path(self) -> None:
        drifted = self._direct_packet()
        drifted["methods"][0]["content"] += "\nchanged"
        self.assertEqual("rmed", self._validate_direct(drifted)["warnings"][0]["code"])

        wrong_role = self._direct_packet()
        wrong_role["methods"][0]["atom_id"] = "CA-R-431"
        self.assertEqual("rmed", self._validate_direct(wrong_role)["warnings"][0]["code"])

        unsafe = self._direct_packet()
        unsafe["methods"][0]["path"] = "../../outside.md"
        self.assertEqual("rmed", self._validate_direct(unsafe)["warnings"][0]["code"])

    def test_method_input_requires_direct_methods_or_legacy_projection(self) -> None:
        packet = self._packet()
        packet.pop("method_projection")
        self.assertEqual("methods", self._validate(packet)["warnings"][0]["code"])

    def test_method_shape_is_derived_from_exact_workflow_version(self) -> None:
        self.assertEqual(
            "methods",
            self._validate(self._direct_packet())["warnings"][0]["code"],
        )
        self.assertEqual(
            "methods",
            self._validate(self._direct_packet(include_projection=True))["warnings"][0]["code"],
        )
        packet = self._packet()
        profile = copy.deepcopy(self.profile)
        profile["workflow"]["version"] = 18
        row = profile["steps"]["CA-O-231"]
        result = validate_current_shared_packet(
            packet,
            workflow_definition=profile["workflow"],
            step_definition=row["step"],
            action_definition=row["action"],
            trusted_workflow_binding=profile,
            selected_project_root=self.root,
            trusted_method_projection=self.methods,
        )
        self.assertEqual("methods", result.warnings[0]["code"])

    def test_rmed_rejects_wrong_role_archived_source_and_invalid_utf8(self) -> None:
        packet = self._packet()
        row = packet["requirements"][0]
        target = self.root / row["path"]
        wrong_role = target.read_text(encoding="utf-8").replace("Requirement", "Method", 1)
        target.write_text(wrong_role, encoding="utf-8")
        row.update(content=wrong_role, sha256=hashlib.sha256(wrong_role.encode()).hexdigest())
        self.assertEqual("rmed", self._validate(packet)["warnings"][0]["code"])
        archive = self._packet()
        archived_row = archive["requirements"][0]
        archived_row["path"] = ".caprmedio_caprmedio/archive/CA-R-1843.md"
        self.assertEqual("rmed", self._validate(archive)["warnings"][0]["code"])
        invalid = self._packet()
        invalid_row = invalid["requirements"][0]
        invalid_target = self.root / invalid_row["path"]
        invalid_target.write_bytes(b"\xff")
        invalid_row["sha256"] = hashlib.sha256(b"\xff").hexdigest()
        self.assertEqual("rmed", self._validate(invalid)["warnings"][0]["code"])

    def test_write_steps_require_existing_canonical_workspace(self) -> None:
        packet = self._packet("CA-O-233")
        self.assertEqual("permissions", self._validate(packet, "CA-O-233")["warnings"][0]["code"])
        workspace = Path(self.temporary.name) / "disposable"
        workspace.mkdir()
        packet["workspace"] = str(workspace)
        packet["permissions"]["implementation_workspace"]["path"] = str(workspace)
        self.assertEqual("accepted", self._validate(packet, "CA-O-233")["status"])

    def test_project_configured_control_root_and_prefix_bound_rmed_sources(self) -> None:
        old = self.root / ".caprmedio_caprmedio"
        control = self.root / ".caprmedio_current"
        old.rename(control)
        (control / "caprmedio_project_settings.toml").write_text(
            '[project]\nname = "current"\n[artifacts.identity]\nproject_prefix = "TEST"\n'
            '[paths]\ncontrol_root = ".caprmedio_current"\n',
            encoding="utf-8",
        )
        packet: dict[str, Any] = {"requirements": [], "delivery": [], "evaluations": []}
        methods: list[dict[str, object]] = []
        for letter, role, field in (
            ("R", "Requirement", "requirements"),
            ("D", "Delivery", "delivery"),
            ("E", "Evaluation", "evaluations"),
            ("M", "Method", None),
        ):
            atom_id = f"TEST-{letter}-1"
            path = f".caprmedio_current/input/{atom_id}.md"
            text = (
                f"---\natom_id: {atom_id}\ncontent_role: {role}\nstatus: Active\nversion: 1\n---\n"
            )
            target = self.root / path
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(text, encoding="utf-8")
            row = {
                "atom_id": atom_id,
                "version": 1,
                "path": path,
                "sha256": hashlib.sha256(text.encode()).hexdigest(),
            }
            if field is None:
                methods.append(row)
            else:
                packet[field].append({**row, "content": text})
        packet["method_projection"] = {"content": methods and text, "sources": methods}
        self.assertEqual(
            {"TEST-R-1", "TEST-D-1", "TEST-E-1", "TEST-M-1"},
            validate_rmed_inputs(self.root, packet, {"sources": methods}),
        )


if __name__ == "__main__":
    unittest.main()
