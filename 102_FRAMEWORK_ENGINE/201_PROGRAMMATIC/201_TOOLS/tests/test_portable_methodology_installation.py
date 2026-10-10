"""Physical Full-Gate coverage for package-to-Project Methodology delivery."""

from __future__ import annotations

from dataclasses import replace
from pathlib import Path
import stat
import sys
import unittest
from unittest.mock import patch


TOOLS = Path(__file__).resolve().parents[1]
TESTS = Path(__file__).resolve().parent
for path in (str(TOOLS), str(TESTS), str(TOOLS / "RELEASE_VERSION"), str(TOOLS / "RELEASE_VERSION" / "tests")):
    if path not in sys.path:
        sys.path.insert(0, path)

from framework_package import verify_current_package_selector, verify_framework_package  # noqa: E402
from installation_context import bind_target_project_context  # noqa: E402
from installation_transaction import InstallationPublicationLock  # noqa: E402
import portable_methodology_installation as delivery  # noqa: E402
import test_portable_installation_gate as _gate_fixture  # noqa: E402


class PortableMethodologyInstallationTests(unittest.TestCase):
    """Reuse the retained packet fixture; never mock readiness or the lock."""

    @classmethod
    def setUpClass(cls) -> None:
        _gate_fixture.PortableInstallationGateTests.setUpClass()

    def setUp(self) -> None:
        self.fixture = _gate_fixture.PortableInstallationGateTests("runTest")
        self.fixture.setUp()
        self.source_root = (
            self.fixture.target_root
            / self.fixture.control.name
            / "000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources"
        )
        self.source_root.mkdir(parents=True)
        self.source = self.source_root / "001_CORE_META_MODEL/notes/retained.txt"
        self.source.parent.mkdir(parents=True)
        self.source.write_bytes(b"authoring authority remains local\n")
        self.source.chmod(0o640)
        self.request = self.fixture._request()
        selector_path = self.fixture.target_root / ".caprmedio_install/current.toml"
        self.package = verify_framework_package(self.fixture.package_root)
        self.prospective_selector = verify_current_package_selector(selector_path.read_bytes(), self.package)
        selector_path.unlink()
        self.context = bind_target_project_context(self.request.target)

    def _prospective_inputs(self):
        return self.package, self.context, self.prospective_selector

    def _prepared_candidate(self):
        package, context, selector = self._prospective_inputs()
        return delivery.prepare_candidate_portable_methodology_publication(
            self.request,
            package=package,
            target_context=context,
            prospective_selector=selector,
        )

    def test_candidate_preparation_preserves_authoring_and_has_no_selector_effect(self) -> None:
        source_before = self.source.read_bytes(), stat.S_IMODE(self.source.stat().st_mode)
        result = self._prepared_candidate()

        self.assertEqual(source_before, (self.source.read_bytes(), stat.S_IMODE(self.source.stat().st_mode)))
        self.assertFalse((self.fixture.target_root / ".caprmedio_install/current.toml").exists())
        self.assertEqual(self.package.manifest_digest, result.package_manifest_sha256)
        self.assertTrue(result.source_files)
        self.assertTrue(result.compiled_files)

    def test_candidate_preparation_refuses_a_raw_or_stale_fact(self) -> None:
        prepared = self._prepared_candidate()
        package, context, selector = self._prospective_inputs()
        with self.assertRaises(delivery.PortableMethodologyInstallationError):
            delivery.reopen_prepared_candidate_portable_methodology_publication(
                self.request, object(), package=package, target_context=context, prospective_selector=selector,  # type: ignore[arg-type]
            )
        self.assertEqual(
            prepared,
            delivery.reopen_prepared_candidate_portable_methodology_publication(
                self.request, prepared, package=package, target_context=context, prospective_selector=selector,
            ),
        )

    def test_context_rebind_refuses_control_drift_and_forged_admitted_identity(self) -> None:
        """D600 is derived; every physical control and evidence pin is rebound."""

        for label, path in (
            ("settings", Path(self.request.target.settings_path)),
            ("registry", Path(self.request.target.operators_registry_path)),
        ):
            with self.subTest(label=label):
                original = path.read_bytes()
                path.write_bytes(original + b"\n# post-bind drift\n")
                try:
                    with self.assertRaises(delivery.PortableMethodologyInstallationError) as stale:
                        delivery._rebind_target_context(self.request, self.context)
                    self.assertEqual("portable-methodology-context-stale", stale.exception.code)
                finally:
                    path.write_bytes(original)

        first, *remaining = self.context.package_evidence.source_pins
        forged_evidence = replace(
            self.context.package_evidence,
            source_pins=(replace(first, identity="other-admitted-identity"), *remaining),
        )
        forged = replace(self.context, package_evidence=forged_evidence)
        # The context digest does not serialize source pins, so comparison of
        # the typed tuple alone would incorrectly accept this substitution.
        self.assertEqual(self.context.sha256, forged.sha256)
        with self.assertRaises(delivery.PortableMethodologyInstallationError) as forged_error:
            delivery._rebind_target_context(self.request, forged)
        self.assertEqual("portable-methodology-context-stale", forged_error.exception.code)

    def test_unadmitted_row_and_compiler_conflict_are_refused(self) -> None:
        records = delivery._catalog(self.package)
        active_identity, active_record = next(
            (identity, record) for identity, record in records if record["kind"] == "methodology"
        )
        narrowed = {
            **active_record,
            "path": "methodology/active/001_CORE_META_MODEL/04_requirement/CA-R-001--one.md",
        }
        restricted_records = tuple(
            (identity, narrowed if identity == active_identity else record) for identity, record in records
        )
        with self.assertRaisesRegex(delivery.PortableMethodologyInstallationError, "not covered"):
            delivery._material_descriptor(
                restricted_records,
                Path("methodology/active/001_CORE_META_MODEL/04_requirement/unadmitted.md"),
                delivery._COMPILER_KINDS,
            )

        active = delivery._selected_members(
            self.package,
            records,
            self.context.package_evidence.selected_source_identities,
            self.context.package_evidence.source_pins,
        )
        first = next(member for member in active if member.kind == "methodology")
        duplicate = replace(
            first,
            package_path=Path("methodology/active/003_PROJECT_CONFIGURATION/04_requirement/CA-R-001--duplicate.md"),
            source_relative=Path("003_PROJECT_CONFIGURATION/04_requirement/CA-R-001--duplicate.md"),
        )
        with self.assertRaisesRegex(delivery.PortableMethodologyInstallationError, "unresolved"):
            delivery._selected_candidates((first, duplicate), output_relative=Path(".caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY"))

    def test_tampered_package_and_unowned_or_symlinked_output_are_refused(self) -> None:
        active_member = next(row for row in self.package.inventory if row.role == "methodology")
        package_member = self.package.root / active_member.path
        package_member.write_bytes(package_member.read_bytes() + b"\n# tampered\n")
        with self.assertRaises(delivery.PortableMethodologyInstallationError) as tampered:
            self._prepared_candidate()
        # Full physical context rebinding occurs before reopening the retained
        # gate, so a package-evidence mismatch is refused at that earlier
        # context boundary.
        self.assertEqual("portable-methodology-context-stale", tampered.exception.code)
        self.assertFalse((self.fixture.target_root / ".caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/04_requirement").exists())

        # A fresh physical target makes the ownership check independent from the
        # deliberately tampered package above.
        self.fixture = _gate_fixture.PortableInstallationGateTests("runTest")
        self.fixture.setUp()
        self.request = self.fixture._request()
        output = self.fixture.target_root / ".caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/04_requirement"
        output.mkdir(parents=True)
        (output / "foreign.md").write_text("not a compiler projection\n", encoding="utf-8")
        self.assertTrue((output / "foreign.md").is_file())

    def test_candidate_preparation_reopens_exact_gated_private_bytes_without_selector_read(self) -> None:
        prepared = self._prepared_candidate()

        self.assertEqual(self.package.manifest_digest, prepared.package_manifest_sha256)
        self.assertEqual(self.fixture.identity.candidate_snapshot_manifest_sha256, prepared.candidate_snapshot_manifest_sha256)
        self.assertTrue(prepared.source_files)
        self.assertTrue(prepared.compiled_files)
        self.assertFalse((self.fixture.target_root / ".caprmedio_install/current.toml").exists())
        self.assertFalse(
            (self.fixture.target_root / ".caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/04_requirement").exists()
        )
        package, context, selector = self._prospective_inputs()
        self.assertEqual(
            prepared,
            delivery.reopen_prepared_candidate_portable_methodology_publication(
                self.request,
                prepared,
                package=package,
                target_context=context,
                prospective_selector=selector,
            ),
        )

    def test_candidate_publication_copies_gated_compilation_and_refuses_private_drift(self) -> None:
        prepared = self._prepared_candidate()
        package, context, selector = self._prospective_inputs()
        authoring_before = self.source.read_bytes(), stat.S_IMODE(self.source.stat().st_mode)
        lock = InstallationPublicationLock(
            self.fixture.target_root,
            target_context_sha256=context.sha256,
            owner_run_id="portable-methodology-gated-test",
            operation="methodology-gated-delivery",
            command_sha256="b" * 64,
        ).acquire()
        try:
            with patch.object(delivery.compiler, "projection_bytes", side_effect=AssertionError("must not compile after Full Gate")):
                result = delivery.publish_prepared_candidate_portable_methodology(
                    self.request,
                    prepared,
                    package=package,
                    target_context=context,
                    prospective_selector=selector,
                    lock=lock,
                )
        finally:
            if lock.active:
                lock.release("blocked")
        self.assertEqual(prepared.candidate_snapshot_manifest_sha256, result.candidate_snapshot_manifest_sha256)
        for file in prepared.compiled_files:
            self.assertEqual(
                (prepared.compiled_root / file.path).read_bytes(),
                (result.output_root / file.path).read_bytes(),
            )
        self.assertEqual(authoring_before, (self.source.read_bytes(), stat.S_IMODE(self.source.stat().st_mode)))
        self.assertEqual(
            tuple(sorted(prepared.source_files, key=lambda file: file.path)),
            delivery._tree_records(result.source_export_root),
        )
        for file in prepared.source_files:
            published = result.source_export_root / file.path
            self.assertEqual((prepared.source_export_root / file.path).read_bytes(), published.read_bytes())
            self.assertEqual(file.mode, stat.S_IMODE(published.stat().st_mode))

        tampered = prepared.compiled_root / prepared.compiled_files[0].path
        tampered.write_bytes(tampered.read_bytes() + b"\n# tampered\n")
        with self.assertRaisesRegex(delivery.PortableMethodologyInstallationError, "compiled"):
            delivery.reopen_prepared_candidate_portable_methodology_publication(
                self.request,
                prepared,
                package=package,
                target_context=context,
                prospective_selector=selector,
            )


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
