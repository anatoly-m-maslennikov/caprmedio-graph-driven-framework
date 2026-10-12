"""D602 receipt codec and explicit local package-source admission tests."""

from __future__ import annotations

from dataclasses import replace
import hashlib
import json
import sys
import unittest
from pathlib import Path, PurePosixPath


TOOLS_ROOT = Path(__file__).resolve().parents[1]
RELEASE_ROOT = TOOLS_ROOT / "RELEASE_VERSION"
RELEASE_TEST_ROOT = RELEASE_ROOT / "tests"
for candidate in (TOOLS_ROOT, RELEASE_ROOT, RELEASE_TEST_ROOT):
    if str(candidate) not in sys.path:
        sys.path.insert(0, str(candidate))

from portable_package_fixture import PortablePackageFixture  # noqa: E402
from release_portable_contract import (  # noqa: E402
    collect_portable_source_snapshot,
    seal_portable_source_snapshot,
)
import source_catalog_admission as source_admission  # noqa: E402
from source_catalog_admission import (  # noqa: E402
    SourceAdmissionDescriptor,
    SourceCatalogAdmissionError,
    TrustedSourceAdmissionInvocation,
    admit_package_sources,
    build_source_admission_receipt,
    read_source_admission_receipt,
    render_source_catalog,
    source_snapshot_sha256,
)


def _digest(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def _sources() -> tuple[SourceAdmissionDescriptor, ...]:
    return (
        SourceAdmissionDescriptor("core-meta-model", "methodology", _digest("active"), _digest("active"), "public", False, "methodology/active/001_CORE_META_MODEL"),
        SourceAdmissionDescriptor("local-core", "core", _digest("core"), _digest("core"), "public", False, "102_FRAMEWORK_ENGINE"),
        SourceAdmissionDescriptor("methodology-support", "support", _digest("support"), _digest("support"), "public", False, "methodology/support"),
    )


class _BindingPortablePackageFixture(PortablePackageFixture):
    """Real source fixture with one exporter-frozen Delivery binding."""

    def _seed_project(self, extra_engine_members: dict[str, bytes]) -> None:
        super()._seed_project(extra_engine_members)
        self.write(
            ".caprmedio_caprmedio/07_delivery/CA-D-901--binding.md",
            b"---\natom_id: CA-D-901\nstatus: Active\ncontent_role: Delivery\n"
            b"version: 1\nupdated_at: 2026-10-10 00:00:00 +0000\nrelations: {}\n---\n"
            b"# CA-D-901\n\n```toml\n[tool_binding]\n"
            b'entrypoint = "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/tool.py"\n```\n',
        )


class SourceCatalogAdmissionTests(unittest.TestCase):
    def test_binding_receipt_is_pinned_non_selectable_discovery_metadata(self) -> None:
        binding = SourceAdmissionDescriptor(
            "tool-bindings", "binding", _digest("bindings"), _digest("bindings"),
            "public", False, "methodology/bindings",
        )
        payload = build_source_admission_receipt(
            operator="operator/fixture", command_ref="command/fixture",
            action_run_id="run/fixture", sources=(binding,),
        )
        self.assertEqual((binding,), read_source_admission_receipt(payload).sources)
        for default, path in ((True, "methodology/bindings"), (False, "methodology/active")):
            with self.subTest(default=default, path=path), self.assertRaises(SourceCatalogAdmissionError):
                source_snapshot_sha256((SourceAdmissionDescriptor(
                    binding.identity, binding.kind, binding.revision, binding.sha256,
                    binding.visibility, default, path,
                ),))

    def test_canonical_receipt_round_trips_and_catalog_uses_its_actual_bytes_digest(self) -> None:
        sources = _sources()
        payload = build_source_admission_receipt(
            operator="operator/fixture",
            command_ref="command/fixture",
            action_run_id="run/fixture",
            sources=sources,
        )

        receipt = read_source_admission_receipt(payload)
        catalog = render_source_catalog(receipt.sources, admission_receipt_sha256=receipt.sha256)
        expected_lines = ["schema_version = 1", ""]
        for source in receipt.sources:
            expected_lines.extend(
                [
                    f"[source.{source.identity}]",
                    f'kind = "{source.kind}"',
                    f'revision = "{source.revision}"',
                    f'sha256 = "{source.sha256}"',
                    f'admission_receipt_sha256 = "{receipt.sha256}"',
                    f'visibility = "{source.visibility}"',
                    "selection_default = false",
                    f'path = "{source.path}"',
                    "",
                ]
            )

        self.assertEqual(receipt.snapshot_sha256, source_snapshot_sha256(sources))
        self.assertEqual(receipt.sha256, hashlib.sha256(payload).hexdigest())
        self.assertEqual(catalog, "\n".join(expected_lines).encode("utf-8"))

    def test_receipt_refuses_noncanonical_extra_and_snapshot_mismatches(self) -> None:
        sources = _sources()
        payload = build_source_admission_receipt(
            operator="operator/fixture",
            command_ref="command/fixture",
            action_run_id="run/fixture",
            sources=sources,
        )
        variants = (
            payload + b"\n",
            payload.replace(b'"operation":"admit_package_sources",', b'"operation":"admit_package_sources","extra":true,', 1),
        )
        for value in variants:
            with self.subTest(value=value[:32]), self.assertRaises(SourceCatalogAdmissionError):
                read_source_admission_receipt(value)
        tampered = json.loads(payload.decode("utf-8"))
        tampered["snapshot_sha256"] = "0" * 64
        with self.assertRaises(SourceCatalogAdmissionError) as mismatched:
            read_source_admission_receipt(
                json.dumps(tampered, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")
            )
        self.assertEqual(mismatched.exception.code, "source-admission-receipt-snapshot-mismatch")

    def test_writer_uses_real_pre_catalog_snapshot_and_only_typed_invocation(self) -> None:
        fixture = PortablePackageFixture()
        (fixture.root / "catalog.toml").unlink()
        snapshot = collect_portable_source_snapshot(
            fixture.candidate,
            fixture.private_compilation,
            candidate_run_id=fixture.run_id,
        )

        def admit(request):
            return TrustedSourceAdmissionInvocation(
                request.snapshot_sha256,
                "operator/fixture",
                "command/fixture",
                "run/fixture",
            )

        outcome = admit_package_sources(fixture.root, snapshot, invocation_admitter=admit)
        repeat = admit_package_sources(fixture.root, snapshot, invocation_admitter=admit)

        self.assertEqual(outcome, repeat)
        self.assertEqual(outcome.receipt_path.name, f"{outcome.receipt.sha256}.json")
        self.assertEqual(outcome.receipt_path.parent, fixture.root / "admissions")
        self.assertEqual(outcome.receipt.snapshot_sha256, source_snapshot_sha256(outcome.sources))
        self.assertEqual(outcome.catalog_sha256, hashlib.sha256(outcome.catalog_path.read_bytes()).hexdigest())
        self.assertTrue(all(source.revision == source.sha256 for source in outcome.sources))
        self.assertEqual(
            tuple(source.identity for source in outcome.sources),
            ("core-meta-model", "local-core", "methodology-support", "project-configuration"),
        )

        second_fixture = PortablePackageFixture()
        (second_fixture.root / "catalog.toml").unlink()
        second_snapshot = collect_portable_source_snapshot(
            second_fixture.candidate,
            second_fixture.private_compilation,
            candidate_run_id=second_fixture.run_id,
        )
        with self.assertRaises(SourceCatalogAdmissionError) as refused:
            admit_package_sources(second_fixture.root, second_snapshot, invocation_admitter=lambda _request: True)  # type: ignore[return-value]
        self.assertEqual(refused.exception.code, "source-admission-invocation-untrusted")
        self.assertFalse((second_fixture.root / "catalog.toml").exists())

    def test_writer_derives_one_binding_descriptor_from_the_real_frozen_frontier(self) -> None:
        fixture = _BindingPortablePackageFixture(admit=False)
        self.addCleanup(fixture.cleanup)
        self.assertTrue(fixture.source_snapshot.binding_atoms)

        outcome = fixture.admit_sources()
        binding = tuple(source for source in outcome.sources if source.kind == "binding")
        self.assertEqual(1, len(binding))
        self.assertEqual("delivery-bindings", binding[0].identity)
        self.assertEqual("methodology/bindings", binding[0].path)
        self.assertFalse(binding[0].selection_default)
        expected_digest = source_admission._logical_digest(
            fixture.source_snapshot.portable_package_rows,
            resource="BINDING_PROJECTION",
            root=PurePosixPath("methodology/bindings"),
        )
        self.assertEqual(expected_digest, binding[0].revision)
        self.assertEqual(expected_digest, binding[0].sha256)
        self.assertEqual(outcome.receipt.sources, outcome.sources)

        sealed = seal_portable_source_snapshot(fixture.source_snapshot)
        self.assertEqual(fixture.source_snapshot.binding_atoms, sealed.binding_atoms)

    def test_binding_descriptor_refuses_row_frontier_cardinality_mismatch(self) -> None:
        fixture = _BindingPortablePackageFixture(admit=False)
        self.addCleanup(fixture.cleanup)
        without_projection_rows = replace(
            fixture.source_snapshot,
            portable_package_rows=tuple(
                row
                for row in fixture.source_snapshot.portable_package_rows
                if row.resource != "BINDING_PROJECTION"
            ),
        )

        with self.assertRaises(SourceCatalogAdmissionError) as refused:
            source_admission._descriptors_from_snapshot(without_projection_rows)
        self.assertEqual("source-admission-snapshot-invalid", refused.exception.code)

    def test_writer_refuses_typed_invocation_for_a_different_snapshot_before_effects(self) -> None:
        fixture = PortablePackageFixture(admit=False)

        def wrong_snapshot(_request):
            return TrustedSourceAdmissionInvocation(
                "0" * 64,
                "operator/fixture",
                "command/fixture",
                "run/fixture",
            )

        with self.assertRaises(SourceCatalogAdmissionError) as refused:
            admit_package_sources(fixture.root, fixture.source_snapshot, invocation_admitter=wrong_snapshot)
        self.assertEqual(refused.exception.code, "source-admission-invocation-mismatch")
        self.assertFalse((fixture.root / "catalog.toml").exists())
        self.assertFalse((fixture.root / "admissions").exists())

    def test_writer_refuses_existing_different_catalog_without_replacement(self) -> None:
        fixture = PortablePackageFixture()
        original = (fixture.root / "catalog.toml").read_bytes()
        original_admissions = {
            path.name: path.read_bytes()
            for path in (fixture.root / "admissions").iterdir()
            if path.is_file()
        }
        snapshot = collect_portable_source_snapshot(
            fixture.candidate,
            fixture.private_compilation,
            candidate_run_id=fixture.run_id,
        )

        def admit(request):
            return TrustedSourceAdmissionInvocation(request.snapshot_sha256, "operator/fixture", "command/fixture", "run/fixture")

        with self.assertRaises(SourceCatalogAdmissionError) as refused:
            admit_package_sources(fixture.root, snapshot, invocation_admitter=admit)
        self.assertEqual(refused.exception.code, "source-admission-catalog-conflict")
        self.assertEqual((fixture.root / "catalog.toml").read_bytes(), original)
        self.assertEqual(
            {
                path.name: path.read_bytes()
                for path in (fixture.root / "admissions").iterdir()
                if path.is_file()
            },
            original_admissions,
        )


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
