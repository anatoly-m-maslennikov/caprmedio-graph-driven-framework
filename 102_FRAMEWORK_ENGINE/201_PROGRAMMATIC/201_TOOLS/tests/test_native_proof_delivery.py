"""Fast physical delivery-binding tests; no installation or Full Gate claim."""
from dataclasses import replace
import hashlib
import json
from pathlib import Path
import sys
import tomllib
import unittest
from unittest.mock import Mock, patch

TOOLS = Path(__file__).resolve().parents[1]
for path in (TOOLS, TOOLS / "tests", TOOLS / "RELEASE_VERSION", TOOLS / "RELEASE_VERSION/tests"):
    if str(path) not in sys.path:
        sys.path.insert(0, str(path))

import test_portable_runtime_materialization as runtime_fixture
import portable_methodology_installation as methodology
from portable_package_fixture import atom
from source_admission_fixture import write_source_admission_receipt
from framework_package import _path_digest
from native_installation_proof import NativeInstallationProofError, reopen_native_methodology_delivery, read_native_methodology_delivery


class DeliveryRuntimeFixture(runtime_fixture.PortableRuntimeMaterializationTests):
    """Admit fixture source bytes before package sealing, never mutate a package."""

    def _target(self):
        target, control = super()._target()
        from target_methodology_selection import FRAMEWORK_INSTANCE_SETTINGS_RELATIVE
        if not (control / FRAMEWORK_INSTANCE_SETTINGS_RELATIVE).exists():
            self._write(control, FRAMEWORK_INSTANCE_SETTINGS_RELATIVE.as_posix(), b"")
        return target, control

    def _write(self, root, relative, payload, *, mode=0o644):
        if relative == "project_structure.toml":
            payload = ("schema_version = 1\n[[scope_units]]\n"
                       'scope_unit_name = "METHODOLOGY_SOURCES"\n'
                       'authority_path = ".caprmedio_target/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources"\n').encode()
        if relative in {"methodology/active/CA-R-001--fixture.md", "methodology/active/001_CORE_META_MODEL/04_requirement/CA-R-001--fixture.md"}:
            payload = atom("CA-R-001", version=1)
        if relative == "methodology/active/003_PROJECT_CONFIGURATION/05_method/CA-M-001--fixture.md":
            payload = atom("CA-M-001", version=1)
        if relative == "catalog.toml":
            super()._write(root,
                "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/COMPILE_APPLICABLE_METHODOLOGY/compile_applicable_methodology.py",
                Path(methodology.compiler.__file__).read_bytes() + getattr(self, "package_compiler_suffix", b""), mode=0o755)
            old = root / "methodology/active/CA-R-001--fixture.md"
            target = root / "methodology/active/001_CORE_META_MODEL/04_requirement/CA-R-001--fixture.md"
            target.parent.mkdir(parents=True, exist_ok=True)
            if old.exists():
                old.rename(target)
            payload = payload.replace(b"methodology/active/CA-R-001--fixture.md", b"methodology/active/001_CORE_META_MODEL/04_requirement/CA-R-001--fixture.md")
            rows = tomllib.loads(payload.decode())["source"]
            old_receipts = {row["admission_receipt_sha256"] for row in rows.values()}
            canonical_roots = {"core": "102_FRAMEWORK_ENGINE", "methodology": "methodology/active/001_CORE_META_MODEL", "support": "methodology/support",
                "configuration": "methodology/active/003_PROJECT_CONFIGURATION"}
            for row in rows.values():
                row["path"] = canonical_roots[row["kind"]]
                row["sha256"] = _path_digest(root, Path(row["path"]), code="fixture-source-invalid")
                row["revision"] = row["sha256"]
            receipt = write_source_admission_receipt(root, tuple({"identity": identity,
                **{key: value for key, value in row.items() if key != "admission_receipt_sha256"}}
                for identity, row in rows.items()))
            for old_digest in old_receipts - {receipt.sha256}:
                (root / "admissions" / f"{old_digest}.json").rename(self.base / f"unsealed-old-admission-{old_digest}.json")
            lines = ["schema_version = 1", ""]
            for identity, row in rows.items():
                row["admission_receipt_sha256"] = receipt.sha256
                lines.append(f"[source.{identity}]")
                lines.extend(f"{key} = {json.dumps(value)}" for key, value in row.items())
                lines.append("")
            payload = ("\n".join(lines) + "\n").encode()
        super()._write(root, relative, payload, mode=mode)


def physical_delivery(fixture, lock):
    """Use the real projection/staging/publishing implementation on test bytes.

    The synthetic fixture's selector receipt is not a Full Gate. These carriers
    exercise the read-only proof binding, not publication authorization.
    """
    root = fixture.target
    package_compiler, compiler_binding = methodology.open_admitted_package_compiler(fixture.package)
    output_relative = Path(fixture.context.control_child_relpath) / methodology._DEFAULT_OUTPUT_SUFFIX
    members = methodology._selected_members(fixture.package, methodology._catalog(fixture.package),
        fixture.context.methodology_source_identities, fixture.context.package_evidence.source_pins)
    candidates, frontier = methodology._selected_candidates(members, output_relative=output_relative,
                                                           compiler_module=package_compiler)
    authoring = methodology._tree_digest(None)
    with patch.object(methodology, "compiler", package_compiler):
        stage, files, source_view, semantic = methodology._stage(root, lock, output_relative, fixture.package,
            members, candidates, frontier, authoring, fixture.context.sha256)
    payload = methodology._verify_staged(stage, files, semantic)
    methodology._publish(stage, root, output_relative, payload, compiler_module=package_compiler)
    output_digest, manifest = methodology._reopen_delivery(root / output_relative, files, semantic,
                                                         compiler_module=package_compiler)
    return methodology.PortableMethodologyDelivery(fixture.package.manifest_digest, fixture.package.source_catalog_sha256,
        fixture.context.sha256, compiler_binding.sha256,
        frontier, source_view, authoring, output_digest, semantic, root / output_relative, manifest, files)


class NativeProofDeliveryTests(unittest.TestCase):
    def setUp(self):
        self.fixture = DeliveryRuntimeFixture("runTest")
        self.fixture.setUp()
        self.lock = self.fixture._lock()
        self.addCleanup(lambda: self.lock.active and self.lock.release("completed"))
        self.delivery = physical_delivery(self.fixture, self.lock)

    def reopen(self, delivery=None):
        return reopen_native_methodology_delivery(self.fixture.target, self.fixture.package, self.fixture.context,
            self.delivery if delivery is None else delivery)

    def test_exact_delivery_binds_raw_not_semantic_manifest_hash(self):
        result = self.reopen()
        raw = self.delivery.delivery_manifest_path.read_bytes()
        self.assertEqual(hashlib.sha256(raw).hexdigest(), result.manifest_sha256)
        self.assertNotEqual(self.delivery.delivery_manifest_sha256, result.manifest_sha256)
        self.assertEqual(self.delivery, result.delivery)
        with self.assertRaises(NativeInstallationProofError):
            read_native_methodology_delivery(self.fixture.target, self.fixture.package,
                target_context_sha256=self.fixture.context.sha256, manifest_ref=result.manifest_ref,
                expected_manifest_sha256=self.delivery.delivery_manifest_sha256)

    def test_tampered_manifest_refused(self):
        self.delivery.delivery_manifest_path.write_bytes(self.delivery.delivery_manifest_path.read_bytes() + b" ")
        with self.assertRaises(NativeInstallationProofError):
            self.reopen()

    def test_tampered_output_refused(self):
        (self.delivery.output_root / self.delivery.files[0].path).write_bytes(b"forged projection")
        with self.assertRaises(NativeInstallationProofError):
            self.reopen()

    def test_tampered_output_mode_refused(self):
        (self.delivery.output_root / self.delivery.files[0].path).chmod(0o600)
        with self.assertRaises(NativeInstallationProofError):
            self.reopen()

    def test_context_changed_refused(self):
        (self.fixture.control / "project_structure.toml").write_bytes(b"schema_version = 1\n")
        with self.assertRaises(NativeInstallationProofError):
            self.reopen()

    def test_resealed_context_selection_must_match_actual_framework_settings(self):
        # Keep every actual control hash and a real admitted identity, but
        # reseal a caller-chosen subset. Canonical bytes alone are not D600
        # selection authority.
        forged = replace(self.fixture.context, methodology_source_identities=("core-methodology",))
        carrier = self.fixture.target / ".caprmedio_runtime/installation/contexts" / f"{forged.sha256}.toml"
        carrier.write_bytes(forged.with_digest_toml())
        raw = self.delivery.delivery_manifest_path.read_bytes()
        with self.assertRaises(NativeInstallationProofError) as refused:
            read_native_methodology_delivery(self.fixture.target, self.fixture.package,
                target_context_sha256=forged.sha256,
                manifest_ref=self.delivery.delivery_manifest_path.relative_to(self.fixture.target).as_posix(),
                expected_manifest_sha256=hashlib.sha256(raw).hexdigest())
        self.assertIn("target Methodology selection changed", str(refused.exception.__cause__))

    def test_wrong_target_manifest_refused(self):
        with self.assertRaises(NativeInstallationProofError):
            self.reopen(replace(self.delivery, delivery_manifest_path=self.fixture.base / "foreign.json"))

    def test_mapping_and_boolean_do_not_substitute_for_actual_delivery(self):
        for supplied in (True, {"delivery_manifest_sha256": self.delivery.delivery_manifest_sha256}):
            with self.subTest(supplied=supplied), self.assertRaises(NativeInstallationProofError):
                self.reopen(supplied)

    def test_resealed_caller_compiler_digest_does_not_replace_actual_compiler(self):
        document = json.loads(self.delivery.delivery_manifest_path.read_bytes())
        document["compiler_sha256"] = "f" * 64
        unsigned = {key: value for key, value in document.items() if key != "sha256"}
        document["sha256"] = methodology._digest(methodology._canonical_json(unsigned))
        self.delivery.delivery_manifest_path.write_bytes(methodology._canonical_json(document) + b"\n")
        forged = replace(self.delivery, compiler_sha256="f" * 64, delivery_manifest_sha256=document["sha256"])
        with self.assertRaises(NativeInstallationProofError):
            self.reopen(forged)

    def test_resealed_arbitrary_output_does_not_replace_admitted_source(self):
        carrier = self.delivery.output_root / self.delivery.files[0].path
        carrier.write_bytes(carrier.read_bytes().replace(b"fixture claim", b"forged arbitrary claim"))
        actual = methodology._projection_records(self.delivery.output_root)
        document = json.loads(self.delivery.delivery_manifest_path.read_bytes())
        document["files"] = [file.__dict__ for file in actual]
        document["output_tree_sha256"] = methodology._digest(methodology._canonical_json(document["files"]))
        unsigned = {key: value for key, value in document.items() if key != "sha256"}
        document["sha256"] = methodology._digest(methodology._canonical_json(unsigned))
        self.delivery.delivery_manifest_path.write_bytes(methodology._canonical_json(document) + b"\n")
        forged = replace(self.delivery, files=actual, output_tree_sha256=document["output_tree_sha256"],
            delivery_manifest_sha256=document["sha256"])
        with self.assertRaises(NativeInstallationProofError):
            self.reopen(forged)

    def test_reader_checks_source_preservation_without_rendering_or_selection(self):
        original = methodology.open_admitted_package_compiler

        def read_only_compiler(package):
            module, binding = original(package)
            module.projection_bytes = Mock(side_effect=AssertionError("must not render after publication"))
            module.resolve_conflicts = Mock(side_effect=AssertionError("must not select after publication"))
            return module, binding

        with patch.object(methodology, "open_admitted_package_compiler", side_effect=read_only_compiler):
            self.assertEqual(self.delivery, self.reopen().delivery)

    def test_n_plus_one_package_compiler_survives_different_current_n_module(self):
        fixture = DeliveryRuntimeFixture("runTest")
        fixture.package_compiler_suffix = b"\n# Immutable N+1 compiler revision differs from current N.\n"
        fixture.setUp()
        lock = fixture._lock()
        self.addCleanup(lambda: lock.active and lock.release("completed"))
        delivery = physical_delivery(fixture, lock)
        current_digest = hashlib.sha256(Path(methodology.compiler.__file__).read_bytes()).hexdigest()
        self.assertNotEqual(current_digest, delivery.compiler_sha256)
        different_current = fixture.base / "different-current-n-compiler.py"
        different_current.write_bytes(b"# unrelated old installed compiler identity\n")
        with patch.object(methodology.compiler, "__file__", str(different_current)), \
             patch.object(methodology.compiler, "Candidate", side_effect=AssertionError("must not use current N compiler")), \
             patch.object(methodology.compiler, "validate_projection_source_preservation", side_effect=AssertionError("must use admitted package validator")):
            observed = reopen_native_methodology_delivery(fixture.target, fixture.package, fixture.context, delivery)
        self.assertEqual(delivery, observed.delivery)

    def test_package_compiler_tamper_cannot_fall_back_to_current_n(self):
        compiler_path = self.fixture.package.root / methodology.PACKAGE_COMPILER_RELATIVE
        compiler_path.write_bytes(compiler_path.read_bytes() + b"\n# tampered after package seal\n")
        with self.assertRaises(NativeInstallationProofError):
            self.reopen()


def load_tests(loader, tests, pattern):
    # The package fixture subclass is a helper, not a second runtime suite.
    return loader.loadTestsFromTestCase(NativeProofDeliveryTests)
