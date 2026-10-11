"""Native portable inputs for the pre-package Release Unit runner."""

from __future__ import annotations

import unittest
from collections import defaultdict
from dataclasses import replace
import hashlib
from pathlib import Path
from unittest.mock import patch


RELEASE_ROOT = Path(__file__).resolve().parents[1]
TEST_ROOT = Path(__file__).resolve().parent
import sys

for path in (RELEASE_ROOT, TEST_ROOT):
    if str(path) not in sys.path:
        sys.path.insert(0, str(path))

from release_contract import ReleaseContractError  # noqa: E402
from release_suite import (  # noqa: E402
    PortableSuiteGateEvidence,
    execute_bound_release_suite,
    verify_bound_suite_evidence,
)
from release_suite_inputs import collect_portable_suite_inputs  # noqa: E402
from release_test_phases import CANDIDATE_E2E_MODULES  # noqa: E402
from portable_package_fixture import PortablePackageFixture  # noqa: E402


COMPILED_PROBE = (
    "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/RELEASE_VERSION/"
    "tests/test_release_compilation.py"
)
MODULE_RULES = (
    "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/RELEASE_VERSION/"
    "release_suite_bindings.json"
)


def _members() -> dict[str, bytes]:
    """Minimum physical test carriers needed solely for phase assignment."""

    members = {COMPILED_PROBE: b"# portable Unit carrier\n"}
    members.update({relative: b"# portable E2E carrier\n" for relative in CANDIDATE_E2E_MODULES})
    # The default-executor path does not materialize bindings, but keeping the
    # carrier in the candidate prevents a native fixture from relying on an
    # undeclared host file when this test grows an executor assertion.
    members[MODULE_RULES] = b'{"module_probes":[],"schema_version":1}'
    return members


class PortableReleaseSuiteTests(unittest.TestCase):
    def setUp(self) -> None:
        self.fixture = PortablePackageFixture(extra_engine_members=_members())
        self.addCleanup(self.fixture.cleanup)
        assert self.fixture.sealed is not None
        self.sealed = self.fixture.sealed

    def test_collects_real_portable_inputs_and_keeps_typed_origin_rules(self) -> None:
        before = {
            path.relative_to(self.fixture.root).as_posix(): hashlib.sha256(path.read_bytes()).hexdigest()
            for path in self.fixture.root.rglob("*") if path.is_file()
        }
        inputs = collect_portable_suite_inputs(self.fixture.candidate, self.sealed)
        after = {
            path.relative_to(self.fixture.root).as_posix(): hashlib.sha256(path.read_bytes()).hexdigest()
            for path in self.fixture.root.rglob("*") if path.is_file()
        }

        self.assertEqual(after, before)
        self.assertEqual(inputs.input_schema, "portable-1")
        self.assertEqual(inputs.candidate_run_id, self.fixture.run_id)
        self.assertEqual(inputs.input_manifest_sha256, self.sealed.input_manifest_sha256)
        self.assertEqual(inputs.source_catalog_sha256, self.sealed.source_catalog_sha256)
        self.assertEqual(inputs.framework_version, self.sealed.framework_version)
        self.assertEqual(inputs.version_toml_sha256, self.sealed.version_toml_sha256)
        self.assertIn(COMPILED_PROBE, inputs.phase_map.unit_paths)
        self.assertTrue(set(CANDIDATE_E2E_MODULES).isdisjoint(inputs.phase_map.unit_paths))

        rows_by_source = {row.source_path: row for row in inputs.source_paths}
        self.assertEqual(
            rows_by_source["102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/tool.py"].destination_path,
            "FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/tool.py",
        )
        self.assertEqual(
            rows_by_source["102_FRAMEWORK_ENGINE/202_AGENTIC/205_SKILLS/ca/SKILL.md"].destination_path,
            "SKILLS/ca/SKILL.md",
        )

        by_origin: dict[str, list] = defaultdict(list)
        for row in inputs.source_paths:
            by_origin[row.canonical_origin].append(row)
        self.assertTrue(any(row.origin_kind == "skill_projection" for row in inputs.source_paths))
        for origin, rows in by_origin.items():
            phase_rows = [row for row in rows if row.origin_kind != "skill_projection"]
            if len(phase_rows) > 1:
                self.assertTrue(
                    {row.origin_kind for row in phase_rows} <= {"candidate", "methodology", "support"},
                    origin,
                )
                self.assertEqual({row.sha256 for row in phase_rows}, {phase_rows[0].sha256})
                self.assertEqual({row.mode for row in phase_rows}, {phase_rows[0].mode})

    def test_same_byte_methodology_projection_allows_export_mode_normalization(self) -> None:
        # The candidate snapshot preserves a source carrier's restrictive
        # mode; the sealed export materializes its admissible regular-file
        # projection at 0644.  The runner must retain both checked carriers
        # while assigning their one canonical origin only once.
        self.fixture.atom_one.chmod(0o600)
        candidate = self.fixture._candidate()
        observed = replace(self.sealed, candidate=candidate)

        with (
            patch("release_suite_inputs._revalidate", return_value=candidate),
            patch("release_suite_inputs.revalidate_sealed_portable_compilation", return_value=observed),
        ):
            inputs = collect_portable_suite_inputs(candidate, observed)

        canonical = self.fixture.atom_one.relative_to(self.fixture.root).as_posix()
        projected = [
            row for row in inputs.source_paths
            if row.canonical_origin == canonical and row.origin_kind != "skill_projection"
        ]
        self.assertEqual({row.origin_kind for row in projected}, {"candidate", "methodology"})
        self.assertEqual({row.sha256 for row in projected}, {projected[0].sha256})
        self.assertEqual({row.mode for row in projected}, {0o600, 0o644})
        self.assertNotIn("defaults/runtime-config.toml", {row.source_path for row in inputs.source_paths})

    def test_methodology_projection_still_refuses_conflicting_bytes(self) -> None:
        self.fixture.atom_one.chmod(0o600)
        candidate = self.fixture._candidate()
        atom_relative = self.fixture.atom_one.relative_to(self.fixture.source).as_posix()
        original = next(
            row for row in self.sealed.portable_package_rows
            if row.resource == "METHODOLOGY" and row.source_path.endswith(atom_relative)
        )
        projection = self.fixture.root / original.source_path
        replacement = b"---\natom_id: CA-R-001\nstatus: Active\nversion: 1\n---\n# changed projection\n"
        projection.write_bytes(replacement)
        replacement_row = replace(original, sha256=hashlib.sha256(replacement).hexdigest())
        observed = replace(
            self.sealed,
            candidate=candidate,
            portable_package_rows=tuple(
                replacement_row if row == original else row
                for row in self.sealed.portable_package_rows
            ),
        )

        with (
            patch("release_suite_inputs._revalidate", return_value=candidate),
            patch("release_suite_inputs.revalidate_sealed_portable_compilation", return_value=observed),
            self.assertRaises(ReleaseContractError) as raised,
        ):
            collect_portable_suite_inputs(candidate, observed)
        self.assertEqual(raised.exception.code, "release-suite-portable-origin-conflict")

    def test_methodology_projection_still_refuses_wrong_declared_mode(self) -> None:
        atom_relative = self.fixture.atom_one.relative_to(self.fixture.source).as_posix()
        original = next(
            row for row in self.sealed.portable_package_rows
            if row.resource == "METHODOLOGY" and row.source_path.endswith(atom_relative)
        )
        observed = replace(
            self.sealed,
            portable_package_rows=tuple(
                replace(row, mode=0o600) if row == original else row
                for row in self.sealed.portable_package_rows
            ),
        )

        with (
            patch("release_suite_inputs._revalidate", return_value=self.fixture.candidate),
            patch("release_suite_inputs.revalidate_sealed_portable_compilation", return_value=observed),
            self.assertRaises(ReleaseContractError) as raised,
        ):
            collect_portable_suite_inputs(self.fixture.candidate, observed)
        self.assertEqual(raised.exception.code, "release-suite-portable-stale")

    def test_default_executor_retains_native_incomplete_evidence(self) -> None:
        # The portable fixture intentionally has no selected-N retained
        # package; that state is outside a Unit's pre-package input.  Patch it
        # only to exercise the executor-absence outcome, not an execution.
        with (
            patch("release_suite.require_declared_suite_command"),
            patch("release_suite._active_n_state", return_value=("a" * 64, "b" * 64, "c" * 64)),
        ):
            evidence = execute_bound_release_suite(self.fixture.candidate, self.sealed)

        self.assertIsInstance(evidence, PortableSuiteGateEvidence)
        self.assertEqual(evidence.input_schema, "portable-1")
        self.assertEqual(evidence.outcome, "incomplete")
        self.assertFalse(evidence.passed)
        self.assertEqual(evidence.candidate_run_id, self.fixture.run_id)
        self.assertEqual(evidence.input_manifest_sha256, self.sealed.input_manifest_sha256)
        self.assertEqual(evidence.source_catalog_sha256, self.sealed.source_catalog_sha256)
        self.assertEqual(evidence.framework_version, self.sealed.framework_version)
        self.assertEqual(evidence.version_toml_sha256, self.sealed.version_toml_sha256)

    def test_current_reverification_rejects_raw_or_unpassed_evidence(self) -> None:
        with self.assertRaises(ReleaseContractError) as raw:
            verify_bound_suite_evidence(self.fixture.candidate, self.sealed, {"passed": True})
        self.assertEqual(raw.exception.code, "release-suite-evidence-untrusted")

        with self.assertRaises(ReleaseContractError) as boolean:
            verify_bound_suite_evidence(self.fixture.candidate, self.sealed, True)
        self.assertEqual(boolean.exception.code, "release-suite-evidence-untrusted")

    def test_current_reverification_refuses_portable_source_drift(self) -> None:
        defaults = self.fixture.root / "defaults/runtime-config.toml"
        defaults.write_bytes(defaults.read_bytes() + b"changed = true\n")

        with self.assertRaises(ReleaseContractError) as raised:
            collect_portable_suite_inputs(self.fixture.candidate, self.sealed)
        self.assertEqual(raised.exception.code, "portable-contract-stale")

    def test_current_reverification_refuses_compiled_output_drift(self) -> None:
        compiled_root = self.fixture.root / self.sealed.private_compilation.compiled_root
        compiled = next(path for path in compiled_root.rglob("*") if path.is_file())
        compiled.write_bytes(compiled.read_bytes() + b"changed = true\n")

        with self.assertRaises(ReleaseContractError):
            collect_portable_suite_inputs(self.fixture.candidate, self.sealed)


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
