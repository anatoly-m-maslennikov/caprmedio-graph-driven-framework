"""Private Release-suite control-reference context tests.

The fixtures copy the current, admitted source closure into a disposable
Project.  They never turn the fixture into a candidate input or a public
request field.
"""

from __future__ import annotations

import hashlib
import json
import os
import shutil
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch


RELEASE_ROOT = Path(__file__).resolve().parents[1]
REPOSITORY = RELEASE_ROOT.parents[3]
MCP_ROOT = REPOSITORY / "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/204_MCP"
TEST_ROOT = Path(__file__).resolve().parent
for path in (RELEASE_ROOT, MCP_ROOT, TEST_ROOT):
    if str(path) not in sys.path:
        sys.path.insert(0, str(path))

import release_source_admission  # noqa: E402
from release_source_admission import AUTHORITY_REF, derive_release_source_admission  # noqa: E402
import release_suite_reference_context as reference_context  # noqa: E402
import selected_routes  # noqa: E402
from release_suite_reference_context import (  # noqa: E402
    ReferenceRow,
    ReleaseSuiteReferenceContext,
    ReleaseSuiteReferenceContextError,
    capture_context,
    copy_verified_bytes,
    revalidate_context,
    validate_reference_rows,
    validate_schema2_context,
)
from release_suite_limits import MAX_UNIT_TIMEOUT_SECONDS, resolve_unit_deadline  # noqa: E402
from selected_routes import PROJECT_SETTINGS_REF, canonical_json, load_selected_manifest, selected_manifest_ref  # noqa: E402
import full_suite_golden.control_fixture as control_fixture  # noqa: E402
from full_suite_golden.control_fixture import copy_control_closure  # noqa: E402


_UNIT_DEADLINE_SETTINGS = frozenset({
    ".caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/"
    "000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/"
    "caprmedio_framework_default_settings.toml",
    ".caprmedio_caprmedio/000_CAPRMEDIO_framework/caprmedio_framework_settings.toml",
})


def _source_paths(value: object) -> set[str]:
    if isinstance(value, dict):
        paths = {value["source_path"]} if isinstance(value.get("source_path"), str) else set()
        for child in value.values():
            paths |= _source_paths(child)
        return paths
    if isinstance(value, list):
        paths: set[str] = set()
        for child in value:
            paths |= _source_paths(child)
        return paths
    return set()


def _replace_first_source_path(value: object) -> bool:
    if isinstance(value, dict):
        if isinstance(value.get("source_path"), str):
            value["source_path"] = ".env"
            return True
        return any(_replace_first_source_path(child) for child in value.values())
    if isinstance(value, list):
        return any(_replace_first_source_path(child) for child in value)
    return False


def _prompt_source(atom_id: str, version: int, *, status: str = "Active") -> bytes:
    return (
        f'---\natom_id: "{atom_id}"\nversion: {version}\nstatus: "{status}"\n---\n'.encode("utf-8")
    )


def _prompt_frontier_carrier(rows: list[tuple[str, bytes]]) -> tuple[bytes, dict[str, tuple[bytes, int]]]:
    bindings: list[tuple[str, bytes]] = []
    captured: dict[str, tuple[bytes, int]] = {}
    atom_ids: dict[str, str] = {}
    for index, (path, source) in enumerate(rows, 1):
        digest = hashlib.sha256(source).hexdigest()
        atom_id = atom_ids.setdefault(path, f"CA-R-{index}")
        binding_path = f"102_FRAMEWORK_ENGINE/202_AGENTIC/202_PROMPTS/ACTION_PROMPTS/P{index}/source_bindings.json"
        binding = json.dumps({"schema_version": 1, "sources": [{
            "atom_id": atom_id, "version": 1, "path": path, "sha256": digest,
        }]}, sort_keys=True, separators=(",", ":")).encode("utf-8")
        bindings.append((binding_path, binding))
        captured[binding_path] = (binding, 0o644)
        captured[path] = (source, 0o644)
    d580 = (
        b"### Prompt binding frontier\n\n"
        b"| Package | Binding carrier | SHA-256 |\n"
        b"| --- | --- | --- |\n"
        + b"| IMPLEMENTATION_WORKFLOW | `" + bindings[0][0].encode() + b"` | `" + hashlib.sha256(bindings[0][1]).hexdigest().encode() + b"` |\n"
        + b"| RMED_ATOM_REVIEW | `" + bindings[1][0].encode() + b"` | `" + hashlib.sha256(bindings[1][1]).hexdigest().encode() + b"` |\n"
    )
    return d580, captured


class PromptBindingFrontierTests(unittest.TestCase):
    def test_accepts_active_exact_pins_and_unions_identical_shared_source_once(self) -> None:
        shared = ".caprmedio_caprmedio/04_requirement/CA-R-1-CORE--shared.md"
        d580, captured = _prompt_frontier_carrier([(shared, _prompt_source("CA-R-1", 1)), (shared, _prompt_source("CA-R-1", 1))])
        paths = reference_context._prompt_binding_frontier(d580, captured)
        self.assertEqual(paths.count(shared), 1)
        self.assertEqual(len(paths), 3)

    def test_refuses_inactive_or_conflicting_shared_pin(self) -> None:
        source = ".caprmedio_caprmedio/04_requirement/CA-R-1-CORE--shared.md"
        d580, captured = _prompt_frontier_carrier([(source, _prompt_source("CA-R-1", 1, status="Archived")), (source, _prompt_source("CA-R-1", 1, status="Archived"))])
        with self.assertRaises(ReleaseSuiteReferenceContextError):
            reference_context._prompt_binding_frontier(d580, captured)
        d580, captured = _prompt_frontier_carrier([(source, _prompt_source("CA-R-1", 1)), (source, _prompt_source("CA-R-1", 1))])
        second = sorted(path for path in captured if path.endswith("source_bindings.json"))[1]
        binding = json.loads(captured[second][0])
        binding["sources"][0]["sha256"] = "0" * 64
        changed = json.dumps(binding, sort_keys=True, separators=(",", ":")).encode("utf-8")
        captured[second] = (changed, 0o644)
        d580 = d580.replace(
            hashlib.sha256(json.dumps({"schema_version": 1, "sources": [{"atom_id": "CA-R-1", "version": 1, "path": source, "sha256": hashlib.sha256(_prompt_source("CA-R-1", 1)).hexdigest()}]}, sort_keys=True, separators=(",", ":")).encode()).hexdigest().encode(),
            hashlib.sha256(changed).hexdigest().encode(), 1,
        )
        with self.assertRaises(ReleaseSuiteReferenceContextError):
            reference_context._prompt_binding_frontier(d580, captured)

    def test_selected_source_refresh_frontier_requires_exact_active_rows(self) -> None:
        d580_path = REPOSITORY / reference_context._D580_REFERENCE
        d580 = d580_path.read_bytes()
        paths = reference_context._selected_source_refresh_frontier(d580, {})
        self.assertEqual(5, len(paths))
        self.assertEqual(paths, tuple(sorted(paths)))
        captured = {
            path: ((REPOSITORY / path).read_bytes(), (REPOSITORY / path).stat().st_mode & 0o777)
            for path in paths
        }
        self.assertEqual(paths, reference_context._selected_source_refresh_frontier(d580, captured))
        tampered = dict(captured)
        target = paths[-1]
        tampered[target] = (captured[target][0] + b"\nchanged\n", captured[target][1])
        with self.assertRaises(ReleaseSuiteReferenceContextError):
            reference_context._selected_source_refresh_frontier(d580, tampered)


class RetainedGoldenControlSourceTests(unittest.TestCase):
    """Historic Prompt pins are fixture evidence, not current source authority."""

    def test_closed_fixture_rows_reopen_only_their_exact_historic_pins(self) -> None:
        document = json.loads(control_fixture._RETAINED_CONTROL_SOURCES_MANIFEST.read_bytes())
        self.assertEqual({
            "package_manifest_ref": control_fixture._RETAINED_PACKAGE_MANIFEST_REF,
            "package_manifest_sha256": control_fixture._RETAINED_PACKAGE_MANIFEST_SHA256,
        }, document["provenance"])
        self.assertEqual(2, len(document["sources"]))
        for row in document["sources"]:
            with self.subTest(source_path=row["source_path"]):
                source = control_fixture._retained_source(REPOSITORY, row["source_path"], row["sha256"])
                self.assertEqual(
                    control_fixture._RETAINED_CONTROL_SOURCES_ROOT / row["fixture_path"],
                    source,
                )
                self.assertTrue(source.is_file())
                self.assertFalse(source.is_symlink())
                self.assertEqual(row["sha256"], hashlib.sha256(source.read_bytes()).hexdigest())
                self.assertEqual(row["mode"], source.stat().st_mode & 0o777)
                self.assertIsNone(control_fixture._retained_fixture_source(row["source_path"], "0" * 64))

    def test_retained_fixture_symlink_refuses_instead_of_sourcing_a_package(self) -> None:
        # Managed macOS refuses recursive cleanup of directories containing a
        # symlink.  This disposable root is intentionally retained.
        temporary = Path(tempfile.mkdtemp(prefix="release-suite-retained-fixture-"))
        fixture_root = temporary / "retained"
        fixture_root.mkdir()
        target = temporary / "target.md"
        target.write_bytes(b"retained bytes\n")
        (fixture_root / "carrier.md").symlink_to(target)
        source_path = ".caprmedio_caprmedio/historic.md"
        digest = hashlib.sha256(target.read_bytes()).hexdigest()
        manifest = {
            "schema_version": 1,
            "provenance": {
                "package_manifest_ref": control_fixture._RETAINED_PACKAGE_MANIFEST_REF,
                "package_manifest_sha256": control_fixture._RETAINED_PACKAGE_MANIFEST_SHA256,
            },
            "sources": [{
                "source_path": source_path,
                "fixture_path": "carrier.md",
                "sha256": digest,
                "mode": 0o644,
            }],
        }
        manifest_path = fixture_root / "manifest.json"
        manifest_path.write_bytes(json.dumps(manifest).encode("utf-8"))
        with patch.object(control_fixture, "_RETAINED_CONTROL_SOURCES_ROOT", fixture_root), \
                patch.object(control_fixture, "_RETAINED_CONTROL_SOURCES_MANIFEST", manifest_path), \
                self.assertRaisesRegex(RuntimeError, "retained fixture"):
            control_fixture._retained_source(temporary / "empty-project", source_path, digest)

    def test_retained_source_refuses_unsafe_prompt_paths_before_project_join(self) -> None:
        class NoProjectJoin:
            def __truediv__(self, _relative: object) -> Path:
                raise AssertionError("unsafe Prompt path reached Project filesystem join")

        for source_path in (
            "/102_FRAMEWORK_ENGINE/202_AGENTIC/202_PROMPTS/ACTION_PROMPTS/RMED_ATOM_REVIEW/source_bindings.json",
            "../102_FRAMEWORK_ENGINE/202_AGENTIC/202_PROMPTS/ACTION_PROMPTS/RMED_ATOM_REVIEW/source_bindings.json",
        ):
            with self.subTest(source_path=source_path), \
                    self.assertRaises(ReleaseSuiteReferenceContextError):
                control_fixture._retained_source(NoProjectJoin(), source_path, "0" * 64)

    def test_retained_fixture_refuses_unsafe_manifest_source_paths(self) -> None:
        temporary = Path(tempfile.mkdtemp(prefix="release-suite-retained-manifest-"))
        requested_path = (
            "102_FRAMEWORK_ENGINE/202_AGENTIC/202_PROMPTS/ACTION_PROMPTS/"
            "RMED_ATOM_REVIEW/missing-historic.md"
        )
        for index, source_path in enumerate((
            "/102_FRAMEWORK_ENGINE/202_AGENTIC/202_PROMPTS/ACTION_PROMPTS/RMED_ATOM_REVIEW/source_bindings.json",
            "../102_FRAMEWORK_ENGINE/202_AGENTIC/202_PROMPTS/ACTION_PROMPTS/RMED_ATOM_REVIEW/source_bindings.json",
        )):
            with self.subTest(source_path=source_path):
                fixture_root = temporary / str(index)
                fixture_root.mkdir()
                manifest = {
                    "schema_version": 1,
                    "provenance": {
                        "package_manifest_ref": control_fixture._RETAINED_PACKAGE_MANIFEST_REF,
                        "package_manifest_sha256": control_fixture._RETAINED_PACKAGE_MANIFEST_SHA256,
                    },
                    "sources": [{
                        "source_path": source_path,
                        "fixture_path": "must-not-be-accessed.md",
                        "sha256": "0" * 64,
                        "mode": 0o644,
                    }],
                }
                manifest_path = fixture_root / "manifest.json"
                manifest_path.write_bytes(json.dumps(manifest).encode("utf-8"))
                with patch.object(control_fixture, "_RETAINED_CONTROL_SOURCES_ROOT", fixture_root), \
                        patch.object(control_fixture, "_RETAINED_CONTROL_SOURCES_MANIFEST", manifest_path), \
                        self.assertRaisesRegex(RuntimeError, "retained fixture"):
                    control_fixture._retained_fixture_source(requested_path, "0" * 64)


class UnitDeadlineTests(unittest.TestCase):
    def context(self, *, default: bytes, instance: bytes) -> ReleaseSuiteReferenceContext:
        return ReleaseSuiteReferenceContext(
            root="/fixture",
            trusted_binding_values=(
                ("candidate_snapshot_manifest_sha256", "a" * 64),
                ("compiled_candidate_root", "compiled"),
                ("selected_n_identity", "n"),
                ("selected_n_image_context", "sha256:" + "b" * 64),
            ),
            reference_rows=(), control_context_digest="c" * 64,
            _verified_bytes=tuple(zip(sorted(_UNIT_DEADLINE_SETTINGS), (default, instance))),
        )

    def test_resolves_captured_default_or_instance_and_binds_canonical_snapshot(self) -> None:
        default = b"[release_suite]\nunit_timeout_seconds = 3600\n"
        instance = b"[rmed_review]\ncontext_headroom_fraction = 0.10\n"
        frozen = resolve_unit_deadline(self.context(default=default, instance=instance))
        self.assertEqual(3600.0, frozen.timeout_seconds)
        self.assertEqual(3600.0, frozen.configured_timeout_seconds)
        self.assertEqual(float(MAX_UNIT_TIMEOUT_SECONDS), frozen.maximum_timeout_seconds)
        snapshot = json.loads(frozen.snapshot)
        self.assertEqual(3600.0, snapshot["configured_unit_timeout_seconds"])
        self.assertEqual(3600.0, snapshot["effective_unit_timeout_seconds"])
        self.assertEqual(hashlib.sha256(frozen.snapshot).hexdigest(), frozen.snapshot_sha256)
        empty_instance = resolve_unit_deadline(self.context(
            default=default, instance=b"[release_suite]\n",
        ))
        self.assertEqual(3600.0, empty_instance.timeout_seconds)

        overridden = resolve_unit_deadline(self.context(
            default=default, instance=b"[release_suite]\nunit_timeout_seconds = 5400\n",
        ), fixture_timeout_seconds=120)
        self.assertEqual(5400.0, overridden.configured_timeout_seconds)
        self.assertEqual(120.0, overridden.timeout_seconds)

    def test_refuses_malformed_or_widening_deadline_controls(self) -> None:
        default = b"[release_suite]\nunit_timeout_seconds = 3600\n"
        for instance in (
            b"[release_suite]\nunit_timeout_seconds = true\n",
            b"[release_suite]\nunit_timeout_seconds = 7201\n",
            b"[release_suite]\nunit_timeout_seconds = 999999999999999999999999999999999999999999999999999999999999999999999999999999\n",
            b"[release_suite]\nunit_timeout_seconds = 3600\nextra = 1\n",
        ):
            with self.subTest(instance=instance):
                with self.assertRaises(Exception):
                    resolve_unit_deadline(self.context(default=default, instance=instance))
        with self.assertRaises(Exception):
            resolve_unit_deadline(self.context(default=default, instance=b""), fixture_timeout_seconds=3601)


class ReleaseSuiteReferenceContextTests(unittest.TestCase):
    """Capture derives a current closure and never trusts a supplied one."""

    def setUp(self) -> None:
        temporary_root = REPOSITORY / ".caprmedio_tmp/tests/release-suite-reference-context"
        temporary_root.mkdir(parents=True, exist_ok=True)
        # This managed macOS profile can refuse removal of nested fixture
        # directories; retain these tiny, disposable test inputs like the
        # neighbouring release tests rather than turning cleanup into a test
        # outcome.
        self.root = Path(tempfile.mkdtemp(prefix="release-suite-reference-", dir=temporary_root))
        copy_control_closure(REPOSITORY, self.root)
        self.copy_prompt_binding_frontier()
        self.manifest_ref = selected_manifest_ref(REPOSITORY)
        self.bindings = {
            "candidate_snapshot_manifest_sha256": "a" * 64,
            "compiled_candidate_root": ".caprmedio_caprmedio/_release_materialized/a",
            "selected_n_identity": "selected-N-fixture",
            "selected_n_image_context": "sha256:" + "b" * 64,
        }

    def copy_prompt_binding_frontier(self) -> None:
        """Fixture only: copy D580's already-authorized exact binding leaves."""
        for relative in (
            "102_FRAMEWORK_ENGINE/202_AGENTIC/202_PROMPTS/ACTION_PROMPTS/IMPLEMENTATION_WORKFLOW/source_bindings.json",
            "102_FRAMEWORK_ENGINE/202_AGENTIC/202_PROMPTS/ACTION_PROMPTS/RMED_ATOM_REVIEW/source_bindings.json",
        ):
            source = REPOSITORY / relative
            target = self.root / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(source, target)
            target.chmod(source.stat().st_mode & 0o777)
            for pin in json.loads(source.read_text(encoding="utf-8"))["sources"]:
                source_atom = REPOSITORY / pin["path"]
                target_atom = self.root / pin["path"]
                target_atom.parent.mkdir(parents=True, exist_ok=True)
                shutil.copyfile(source_atom, target_atom)
                target_atom.chmod(source_atom.stat().st_mode & 0o777)

    def capture(self) -> ReleaseSuiteReferenceContext:
        return capture_context(self.root, self.bindings)

    def project_structure_ref(self) -> str:
        return reference_context._project_structure_ref(
            (self.root / PROJECT_SETTINGS_REF).read_bytes()
        )

    def admitted_control_roots(self) -> dict[str, str]:
        """The D580/E587 roots plus one actually admitted transitive pin."""
        manifest = load_selected_manifest(self.root)
        project_structure_ref = self.project_structure_ref()
        roots = {
            "selected_manifest": self.manifest_ref,
            "operators_registry": ".caprmedio_caprmedio/operators_registry.toml",
            "project_settings": PROJECT_SETTINGS_REF.as_posix(),
            "project_structure": project_structure_ref,
            "source_registry": manifest["source_freshness"]["selected_source_registry_ref"],
            "d572_carrier": AUTHORITY_REF,
            "d580_carrier": reference_context._D580_REFERENCE,
        }
        excluded = set(roots.values())
        transitive = next(
            path for path in sorted(_source_paths(derive_release_source_admission(self.root)))
            if path not in excluded
        )
        prompt_binding = "102_FRAMEWORK_ENGINE/202_AGENTIC/202_PROMPTS/ACTION_PROMPTS/IMPLEMENTATION_WORKFLOW/source_bindings.json"
        prompt_source = json.loads((self.root / prompt_binding).read_text(encoding="utf-8"))["sources"][0]["path"]
        return {**roots, "transitive_pin": transitive, "prompt_binding": prompt_binding,
                "prompt_source": prompt_source}

    def assert_mutation_blocks_rederivation(self, *, phase: str, copy_before_mutation: bool) -> None:
        context = self.capture()
        if copy_before_mutation:
            workspace = Path(tempfile.mkdtemp(prefix="release-suite-phase-workspace-"))
            copy_verified_bytes(context, workspace)
        for name, relative in self.admitted_control_roots().items():
            with self.subTest(phase=phase, root=name):
                path = self.root / relative
                original = path.read_bytes()
                path.write_bytes(original + f"\n{phase}-{name}-changed\n".encode("utf-8"))
                try:
                    with self.assertRaises(Exception):
                        revalidate_context(self.root, context, self.bindings)
                finally:
                    path.write_bytes(original)

    def test_each_admitted_root_mutation_blocks_before_execution_rederivation(self) -> None:
        self.assert_mutation_blocks_rederivation(
            phase="before_execution", copy_before_mutation=False,
        )

    def test_each_admitted_root_mutation_blocks_after_execution_rederivation(self) -> None:
        # The workspace copy represents inputs already issued to the suite;
        # post-run rederivation must still refuse changed live authority.
        self.assert_mutation_blocks_rederivation(
            phase="after_execution", copy_before_mutation=True,
        )

    def test_capture_contains_current_roots_transitive_pins_and_canonical_digest(self) -> None:
        context = self.capture()
        paths = [row.source_path for row in context.reference_rows]
        self.assertEqual(sorted(paths), paths)
        self.assertEqual(len(paths), len(set(paths)))
        self.assertTrue({
            self.manifest_ref,
            ".caprmedio_caprmedio/operators_registry.toml",
            PROJECT_SETTINGS_REF.as_posix(),
            self.project_structure_ref(),
            AUTHORITY_REF,
        }.issubset(paths))
        self.assertTrue(_source_paths(derive_release_source_admission(self.root)).issubset(paths))
        self.assertTrue(_UNIT_DEADLINE_SETTINGS.issubset(paths))
        refresh_authorities = reference_context._selected_source_refresh_frontier(
            (self.root / reference_context._D580_REFERENCE).read_bytes(), {},
        )
        self.assertTrue(set(refresh_authorities).issubset(paths))
        for relative in (
            "102_FRAMEWORK_ENGINE/202_AGENTIC/202_PROMPTS/ACTION_PROMPTS/IMPLEMENTATION_WORKFLOW/source_bindings.json",
            "102_FRAMEWORK_ENGINE/202_AGENTIC/202_PROMPTS/ACTION_PROMPTS/RMED_ATOM_REVIEW/source_bindings.json",
        ):
            binding = json.loads((self.root / relative).read_text(encoding="utf-8"))
            self.assertIn(relative, paths)
            self.assertTrue({pin["path"] for pin in binding["sources"]}.issubset(paths))
        for row in context.reference_rows:
            source = self.root / row.source_path
            self.assertEqual(hashlib.sha256(source.read_bytes()).hexdigest(), row.sha256)
            self.assertEqual(source.stat().st_mode & 0o777, row.mode)
        # Independently reconstruct D580's flat, self-excluding preimage;
        # this must not call the helper's digest implementation.
        payload = {
            "schema_version": 1,
            **dict(context.trusted_binding_values),
            "reference_rows": [row.as_dict() for row in context.reference_rows],
        }
        self.assertEqual(hashlib.sha256(canonical_json(payload).encode("utf-8")).hexdigest(),
                         context.control_context_digest)

    def test_reader_snapshot_materializes_registered_empty_rmed_namespaces(self) -> None:
        """Current D572 lookup must work from immutable bytes and empty roots."""
        structure = (self.root / self.project_structure_ref()).read_bytes()
        expected = reference_context._admission_namespace_dirs(structure)
        self.assertEqual(8, len(expected))
        with reference_context._reader_snapshot(self.root) as (snapshot, _captured):
            for relative in expected:
                with self.subTest(relative=relative):
                    target = snapshot / relative
                    self.assertTrue(target.is_dir())
                    self.assertFalse(target.is_symlink())
            self.assertTrue(reference_context._closure_paths(snapshot))

    def test_current_d572_needs_no_retired_private_or_resolver_blocks(self) -> None:
        authority = (self.root / AUTHORITY_REF).read_text(encoding="utf-8")
        self.assertNotIn("## Private implementation carriers", authority)
        self.assertNotIn("## Unknown-effect resolver authority", authority)
        self.assertIn(reference_context._D580_REFERENCE,
                      [row.source_path for row in self.capture().reference_rows])

    def test_control_fixture_copies_selected_source_refresh_authority_frontier(self) -> None:
        d580 = (REPOSITORY / reference_context._D580_REFERENCE).read_bytes()
        paths = reference_context._selected_source_refresh_frontier(d580, {})
        captured = {
            path: ((self.root / path).read_bytes(), (self.root / path).stat().st_mode & 0o777)
            for path in paths
        }
        self.assertEqual(paths, reference_context._selected_source_refresh_frontier(
            (self.root / reference_context._D580_REFERENCE).read_bytes(), captured,
        ))
        for path in paths:
            self.assertEqual((REPOSITORY / path).read_bytes(), (self.root / path).read_bytes())

    def test_copy_preserves_only_captured_bytes_at_identical_relative_paths(self) -> None:
        context = self.capture()
        workspace = Path(tempfile.mkdtemp(prefix="release-suite-workspace-"))
        copy_verified_bytes(context, workspace)
        self.assertFalse((workspace / "arbitrary-caller-file").exists())
        for row in context.reference_rows:
            self.assertEqual((workspace / row.source_path).read_bytes(), (self.root / row.source_path).read_bytes())
            self.assertEqual((workspace / row.source_path).stat().st_mode & 0o777, row.mode)
        structure = self.project_structure_ref()
        self.assertEqual((workspace / structure).read_bytes(), (self.root / structure).read_bytes())
        self.assertEqual(
            (workspace / structure).stat().st_mode & 0o777,
            (self.root / structure).stat().st_mode & 0o777,
        )

    def test_capture_refuses_missing_project_structure_before_execution(self) -> None:
        structure = self.root / self.project_structure_ref()
        original = structure.read_bytes()
        mode = structure.stat().st_mode & 0o777
        structure.unlink()
        try:
            with self.assertRaises(ReleaseSuiteReferenceContextError):
                self.capture()
        finally:
            structure.write_bytes(original)
            structure.chmod(mode)

    def test_revalidation_refuses_mutated_transitive_pin_before_or_after_execution(self) -> None:
        context = self.capture()
        transitive = next(path for path in _source_paths(derive_release_source_admission(self.root))
                          if path != AUTHORITY_REF)
        source = self.root / transitive
        original = source.read_bytes()
        source.write_bytes(original + b"\nchanged\n")
        with self.assertRaises(Exception):
            revalidate_context(self.root, context, self.bindings)
        source.write_bytes(original)
        self.assertEqual(context, revalidate_context(self.root, context, self.bindings))
        (self.root / self.manifest_ref).write_bytes((self.root / self.manifest_ref).read_bytes() + b"\n")
        with self.assertRaises(Exception):
            revalidate_context(self.root, context, self.bindings)

    def test_capture_refuses_symlinked_or_secret_shaped_injected_reference_without_reading_it(self) -> None:
        target = self.root / AUTHORITY_REF
        saved = target.read_bytes()
        target.unlink()
        target.symlink_to(self.root / ".caprmedio_caprmedio/operators_registry.toml")
        with self.assertRaises(Exception):
            self.capture()
        target.unlink()
        target.write_bytes(saved)

        context = self.capture()
        forged = ReleaseSuiteReferenceContext(
            root=context.root,
            trusted_binding_values=context.trusted_binding_values,
            reference_rows=(ReferenceRow(".env", hashlib.sha256(b"secret").hexdigest(), 0o600),),
            control_context_digest=context.control_context_digest,
            _verified_bytes=((".env", b"secret"),),
        )
        workspace = Path(tempfile.mkdtemp(prefix="release-suite-secret-"))
        with self.assertRaises(ReleaseSuiteReferenceContextError):
            copy_verified_bytes(forged, workspace)
        self.assertFalse((workspace / ".env").exists())

    def test_schema2_requires_exact_reference_rows_and_context_digest(self) -> None:
        context = self.capture()
        envelope = {
            "schema_version": 2,
            "candidate_snapshot_manifest_sha256": self.bindings["candidate_snapshot_manifest_sha256"],
            "reference_rows": [row.as_dict() for row in context.reference_rows],
            "control_context_digest": context.control_context_digest,
        }
        self.assertEqual(envelope, dict(validate_schema2_context(envelope, context)))
        envelope["control_context_digest"] = "0" * 64
        with self.assertRaises(ReleaseSuiteReferenceContextError):
            validate_schema2_context(envelope, context)

    def test_secret_shaped_envelope_row_refuses_before_any_reader_access(self) -> None:
        with patch("release_suite_reference_context._read_regular", side_effect=AssertionError("must not read")):
            with self.assertRaises(ReleaseSuiteReferenceContextError):
                validate_reference_rows(self.root, [{
                    "source_path": ".env",
                    "sha256": "a" * 64,
                    "mode": 0o600,
                }])

    def test_capture_refuses_bytes_mode_race_from_one_control_file(self) -> None:
        target = self.root / ".caprmedio_caprmedio/operators_registry.toml"
        target_inode = target.stat().st_ino
        original_read = os.read
        raced = False

        def read_then_change_mode(fd: int, size: int) -> bytes:
            nonlocal raced
            if os.fstat(fd).st_ino == target_inode and not raced:
                raced = True
                target.chmod(0o600)
            return original_read(fd, size)

        with patch("release_suite_reference_context.os.read", side_effect=read_then_change_mode):
            with self.assertRaises(ReleaseSuiteReferenceContextError):
                self.capture()
        self.assertTrue(raced)

    def test_revalidation_requires_fresh_suite_owner_bindings_not_context_copy(self) -> None:
        context = self.capture()
        self.assertEqual(context, revalidate_context(self.root, context, self.bindings))
        cases = {
            "candidate_snapshot_manifest_sha256": "c" * 64,
            "compiled_candidate_root": ".caprmedio_caprmedio/_release_materialized/c",
            "selected_n_identity": "selected-N-other",
            "selected_n_image_context": "sha256:" + "c" * 64,
        }
        for field, changed in cases.items():
            with self.subTest(field=field):
                fresh = dict(self.bindings)
                fresh[field] = changed
                with self.assertRaises(ReleaseSuiteReferenceContextError):
                    revalidate_context(self.root, context, fresh)

    def test_reader_race_uses_preflight_snapshot_and_never_reads_injected_secret_path(self) -> None:
        """A root-backed reread after preflight must not gain a new source path."""
        manifest_path = self.root / self.manifest_ref
        original_preflight = reference_context._preflight_reader_paths
        original_read_regular = reference_context._read_regular
        raced = False

        def preflight_then_mutate(root: Path) -> object:
            nonlocal raced
            result = original_preflight(root)
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
            self.assertTrue(_replace_first_source_path(manifest))
            manifest_path.write_text(json.dumps(manifest, sort_keys=True, separators=(",", ":")), encoding="utf-8")
            raced = True
            return result

        def guard_secret_read(root: Path, relative: str) -> tuple[bytes, int]:
            if relative == ".env":
                raise AssertionError("reader attempted forbidden secret-shaped path")
            return original_read_regular(root, relative)

        with patch.object(reference_context, "_preflight_reader_paths", side_effect=preflight_then_mutate), \
                patch.object(reference_context, "_read_regular", side_effect=guard_secret_read):
            context = self.capture()
        self.assertTrue(raced)
        self.assertIn(self.manifest_ref, [row.source_path for row in context.reference_rows])

    def test_capture_keeps_other_control_reader_path_bindings_unchanged(self) -> None:
        """Snapshot isolation is local; it must not patch shared reader modules."""
        selected_path_type = selected_routes.Path
        admission_path_type = release_source_admission.Path
        original_preflight = reference_context._preflight_reader_paths
        observed = False

        def observe_shared_readers(root: Path) -> object:
            nonlocal observed
            self.assertIs(selected_routes.Path, selected_path_type)
            self.assertIs(release_source_admission.Path, admission_path_type)
            self.assertEqual(self.manifest_ref, selected_routes.selected_manifest_ref(root))
            observed = True
            return original_preflight(root)

        with patch.object(reference_context, "_preflight_reader_paths", side_effect=observe_shared_readers):
            self.capture()
        self.assertTrue(observed)
        self.assertIs(selected_routes.Path, selected_path_type)
        self.assertIs(release_source_admission.Path, admission_path_type)


class ReaderSnapshotCleanupTests(unittest.TestCase):
    _CONTROL_REF = ".caprmedio_caprmedio/control.json"
    _SETTINGS = b'[paths]\ncontrol_root = ".caprmedio_caprmedio"\n'
    _STRUCTURE = (
        b'[[scope_units]]\n'
        b'scope_unit_name = "PROJECT_TOOLS"\n'
        b'authority_path = ".caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/'
        b'201_FEATURE_PROGRAMMATIC/205_FEATURE_PROJECT_TOOLS"\n\n'
        b'[[scope_units]]\n'
        b'scope_unit_name = "TOOLS"\n'
        b'authority_path = ".caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/'
        b'201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS"\n'
    )

    def _captured(self, payload: bytes, mode: int) -> dict[str, tuple[bytes, int]]:
        return {
            PROJECT_SETTINGS_REF.as_posix(): (self._SETTINGS, 0o644),
            ".caprmedio_caprmedio/project_structure.toml": (self._STRUCTURE, 0o644),
            self._CONTROL_REF: (payload, mode),
        }

    def test_disposable_snapshot_cleanup_targets_only_exact_reader_snapshot(self) -> None:
        captured = self._captured(b'captured evidence', 0o600)
        removed = []
        def successful_cleanup(path):
            removed.append(path)
        successful_cleanup.avoids_symlink_attacks = True
        with patch.object(reference_context, '_preflight_reader_paths',
                          return_value=(captured, tuple(captured))), \
                patch.object(reference_context.shutil, 'rmtree', successful_cleanup):
            with reference_context._reader_snapshot(REPOSITORY) as (snapshot, verified):
                self.assertEqual(verified, captured)
                self.assertEqual(removed, [])
        self.assertEqual(removed, [snapshot])
        self.assertEqual(verified, captured)

    def test_disposable_snapshot_removed_after_reader_with_readonly_file(self) -> None:
        captured = self._captured(b'captured evidence', 0o444)
        remover = shutil.rmtree
        denied = []
        def observe_cleanup(path):
            try:
                return remover(path)
            except PermissionError as error:
                denied.append(error)
                raise
        observe_cleanup.avoids_symlink_attacks = remover.avoids_symlink_attacks
        with patch.object(reference_context, '_preflight_reader_paths',
                          return_value=(captured, tuple(captured))), \
                patch.object(reference_context.shutil, 'rmtree', observe_cleanup):
            with reference_context._reader_snapshot(REPOSITORY) as (snapshot, verified):
                self.assertEqual(snapshot.stat().st_mode & 0o777, 0o700)
                self.assertEqual((snapshot / self._CONTROL_REF).stat().st_mode & 0o777, 0o444)
                self.assertEqual(verified, captured)
        if snapshot.exists():
            self.assertTrue(denied, 'snapshot retained without observed permission denial')
            self.skipTest('host profile denied deletion of the read-only snapshot; retained without retry')
        self.assertFalse(snapshot.exists())
        self.assertEqual(verified, captured)

    def test_permission_denied_cleanup_retains_exact_snapshot_and_captured_evidence(self) -> None:
        captured = self._captured(b'captured evidence', 0o444)
        def denied(path):
            raise PermissionError('profile denied fixture cleanup')
        denied.avoids_symlink_attacks = True
        with patch.object(reference_context, '_preflight_reader_paths',
                          return_value=(captured, tuple(captured))), \
                patch.object(reference_context.shutil, 'rmtree', denied):
            with reference_context._reader_snapshot(REPOSITORY) as (snapshot, verified):
                pass
        self.assertTrue(snapshot.is_dir())
        self.assertEqual((snapshot / self._CONTROL_REF).read_bytes(), b'captured evidence')
        self.assertEqual(verified, captured)
        # Leave the denied snapshot as requested; no cleanup retry.


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
