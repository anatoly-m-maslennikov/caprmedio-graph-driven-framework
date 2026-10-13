"""Independent complete Settings file reads; Journal history stays separate."""

from __future__ import annotations

import copy
import dataclasses
import hashlib
from pathlib import Path
import sys
import tempfile
import unittest
from unittest import mock


TOOLS = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(TOOLS))
from connector_bindings import FileSource, capture_source  # noqa: E402
from connector_toml_parse import parse_source, render_document  # noqa: E402
import project_settings_reader as reader  # noqa: E402
import project_settings_schema as schema  # noqa: E402


REPOSITORY = Path.cwd()
AUTHORITY_ROOTS = (
    REPOSITORY / ".caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL",
    REPOSITORY / ".caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC",
)
SCHEMA_IDS = ("CA-D-366", "CA-D-375", "CA-D-376", "CA-D-378", "CA-D-364", "CA-D-520",
              "CA-D-392", "CA-E-459", "CA-M-284")


class ProjectSettingsSchemaIndependentTests(unittest.TestCase):
    def setUp(self):
        self.document = {"schema_version": "2.0", "project": {"name": "independent"},
                         "artifacts": {"identity": {"project_prefix": "TEST"}},
                         "paths": {"control_root": ".caprmedio_independent"}}

    def parse(self, document):
        before = copy.deepcopy(document)
        try:
            return schema._parse_settings(document)
        finally:
            self.assertEqual(before, document)

    def test_valid_optional_and_unicode_values_are_exact_without_defaults_or_normalization(self):
        for prior in (None, [], ["OLD", "OLD", "independent", " Mixed ", "   "]):
            with self.subTest(prior=prior):
                document = copy.deepcopy(self.document)
                if prior is not None:
                    document["project"]["obsolete_names"] = prior
                self.assertEqual(("independent", "TEST", ".caprmedio_independent",
                                  None if prior is None else tuple(prior)), self.parse(document))
        document = copy.deepcopy(self.document)
        document["project"]["name"] = "indépendant"
        document["artifacts"]["identity"]["project_prefix"] = "ÄΩ_7"
        document["paths"]["control_root"] = ".caprmedio_indépendant"
        self.assertEqual(("indépendant", "ÄΩ_7", ".caprmedio_indépendant", None), self.parse(document))

    def test_missing_required_and_extra_keys_refuse_every_level(self):
        for location in ((), ("project",), ("artifacts",), ("artifacts", "identity"), ("paths",)):
            base = self.document
            for key in location:
                base = base[key]
            for missing in [*base.keys(), None]:
                with self.subTest(location=location, missing=missing):
                    document = copy.deepcopy(self.document)
                    target = document
                    for key in location:
                        target = target[key]
                    if missing is None:
                        target["unregistered"] = True
                    else:
                        target.pop(missing)
                    with self.assertRaises(schema._SchemaError) as raised:
                        self.parse(document)
                    self.assertTrue(raised.exception.field)

    def test_wrong_types_invalid_values_and_ownership_refuse_without_coercion(self):
        cases = []
        for field in ("schema_version", "project.name", "artifacts.identity.project_prefix", "paths.control_root"):
            cases += [(field, value) for value in (1, 2.0, True, [], {}, "")]
        cases += [("project.obsolete_names", value) for value in ("OLD", 1, True, [""], [1])]
        cases += [(field, value) for field in ("project", "artifacts", "artifacts.identity", "paths")
                  for value in ("table", [], 1)]
        cases += [("schema_version", "3.0"), ("project.name", "Independent"),
                  ("artifacts.identity.project_prefix", "Test"), ("paths.control_root", ".caprmedio_other"),
                  ("paths.control_root", "./.caprmedio_independent"), ("paths.control_root", ".caprmedio_independent/"),
                  ("paths.control_root", "../.caprmedio_independent")]
        for field, value in cases:
            with self.subTest(field=field, value=value):
                document = copy.deepcopy(self.document)
                keys = field.split(".")
                target = document
                for key in keys[:-1]:
                    target = target[key]
                target[keys[-1]] = value
                with self.assertRaises(schema._SchemaError) as raised:
                    self.parse(document)
                self.assertTrue(raised.exception.field)
        for field in ("projection", "authority_modes", "scope_units", "git", "atom_id", "content_role"):
            with self.subTest(forbidden=field):
                document = copy.deepcopy(self.document)
                document[field] = "forbidden-owner"
                with self.assertRaises(schema._SchemaError):
                    self.parse(document)

    def test_actual_live_legacy_document_refuses_at_complete_schema_without_effects(self):
        path = REPOSITORY / ".caprmedio_caprmedio/caprmedio_project_settings.toml"
        before = path.read_bytes()
        _, document = parse_source(before)
        with self.assertRaises(schema._SchemaError) as raised:
            self.parse(document)
        self.assertTrue(raised.exception.field)
        self.assertEqual(before, path.read_bytes())


class ProjectSettingsReaderIndependentTests(unittest.TestCase):
    def setUp(self):
        scratch = REPOSITORY / ".caprmedio_tmp/tests/project-settings-reader-independent"
        scratch.mkdir(parents=True, exist_ok=True)
        temporary = tempfile.TemporaryDirectory(dir=scratch)
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)
        self.control = self.root / ".caprmedio_independent"
        self.control.mkdir()
        self.settings = self.control / "caprmedio_project_settings.toml"
        self.document = {"schema_version": "2.0", "project": {"name": "independent"},
                         "artifacts": {"identity": {"project_prefix": "TEST"}},
                         "paths": {"control_root": ".caprmedio_independent"}}
        self.write_document(self.document)
        self.authorities = []
        for atom_id in SCHEMA_IDS:
            matches = [path for base in AUTHORITY_ROOTS for path in base.rglob(atom_id + "-*.md")
                       if "archive" not in path.parts]
            self.assertEqual(1, len(matches), atom_id)
            target = self.root / "accepted-authority" / matches[0].name
            target.parent.mkdir(exist_ok=True)
            target.write_bytes(matches[0].read_bytes())
            self.authorities.append(capture_source(self.root, target.relative_to(self.root)))
        self.journal = self.control / "_journal"

    def write_document(self, document):
        self.settings.write_bytes(render_document(document))
        self.source = capture_source(self.root, self.settings.relative_to(self.root))

    def snapshot_files(self):
        return {path.relative_to(self.root): path.read_bytes() for path in self.root.rglob("*")
                if path.is_file() and not path.is_symlink()}

    def read(self, source=None, authorities=None):
        before = self.snapshot_files()
        result = reader.read_project_settings(self.source if source is None else source,
                                             schema_sources=self.authorities if authorities is None else authorities)
        self.assertEqual(before, self.snapshot_files(), "Reader must have zero file effects")
        return result

    def assert_read(self, result):
        self.assertEqual((), result.errors)
        self.assertIsNotNone(result.snapshot)
        self.assertFalse(hasattr(result.snapshot, "history"))
        return result.snapshot

    def assert_refused(self, result):
        self.assertIsNone(result.snapshot)
        self.assertTrue(result.errors)
        self.assertTrue(all(item.code and item.message and item.field for item in result.errors))

    def test_complete_file_values_and_exact_source_schema_pins_need_no_journal(self):
        value = self.assert_read(self.read())
        self.assertEqual(self.document, value.to_document())
        self.assertEqual(("2.0", "independent", "TEST", ".caprmedio_independent", None),
                         (value.schema_version, value.name, value.project_prefix, value.control_root, value.obsolete_names))
        self.assertEqual(self.settings.relative_to(self.root).as_posix(), value.source.path)
        self.assertEqual(hashlib.sha256(self.settings.read_bytes()).hexdigest(), value.source.sha256)
        expected = {(authority.relative_path.as_posix(), authority.sha256) for authority in self.authorities}
        self.assertEqual(expected, {(pin.path, pin.sha256) for pin in value.schema_sources})
        self.assertEqual(set(SCHEMA_IDS), {pin.atom_id for pin in value.schema_sources})
        self.assertFalse(self.journal.exists())

    def test_optional_values_and_unicode_are_preserved_exactly(self):
        for prior in (None, [], ["OLD", "OLD", "independent", " Mixed ", "   "]):
            with self.subTest(prior=prior):
                document = copy.deepcopy(self.document)
                if prior is not None:
                    document["project"]["obsolete_names"] = prior
                self.write_document(document)
                value = self.assert_read(self.read())
                self.assertEqual(None if prior is None else tuple(prior), value.obsolete_names)
                self.assertEqual(document, value.to_document())
        self.control.rename(self.root / ".caprmedio_indépendant")
        self.control = self.root / ".caprmedio_indépendant"
        self.settings = self.control / self.settings.name
        document = copy.deepcopy(self.document)
        document["project"]["name"] = "indépendant"
        document["artifacts"]["identity"]["project_prefix"] = "ÄΩ_7"
        document["paths"]["control_root"] = self.control.name
        self.write_document(document)
        self.assertEqual(document, self.assert_read(self.read()).to_document())

    def test_complete_document_refuses_schema_errors_and_legacy_bytes(self):
        for payload in (b"not TOML", b"\xff", b'schema_version="2.0"\nschema_version="2.0"\n'):
            with self.subTest(payload=payload):
                self.settings.write_bytes(payload)
                self.source = capture_source(self.root, self.settings.relative_to(self.root))
                self.assert_refused(self.read())
        cases = [("schema_version", 2.0), ("project.name", "Independent"),
                 ("artifacts.identity.project_prefix", "Test"), ("paths.control_root", ".caprmedio_other")]
        for field, value in cases:
            with self.subTest(field=field):
                document = copy.deepcopy(self.document)
                keys = field.split(".")
                target = document
                for key in keys[:-1]:
                    target = target[key]
                target[keys[-1]] = value
                self.write_document(document)
                self.assert_refused(self.read())
        legacy = REPOSITORY / ".caprmedio_caprmedio/caprmedio_project_settings.toml"
        before = legacy.read_bytes()
        self.settings.write_bytes(before)
        self.source = capture_source(self.root, self.settings.relative_to(self.root))
        self.assert_refused(self.read())
        self.assertEqual(before, legacy.read_bytes())

    def test_complete_distinct_actual_schema_authority_and_stale_sources_are_required(self):
        for authorities in ([], self.authorities[:-1], self.authorities + [self.authorities[0]]):
            with self.subTest(count=len(authorities)):
                self.assert_refused(self.read(authorities=authorities))
        authority = self.authorities[0]
        path = self.root / authority.relative_path
        original = path.read_bytes()
        path.write_bytes(original + b"\n# authority drift\n")
        self.assert_refused(self.read())
        changed = capture_source(self.root, authority.relative_path)
        self.assert_refused(self.read(authorities=[changed, *self.authorities[1:]]))
        path.write_bytes(original)
        self.settings.write_bytes(self.settings.read_bytes() + b"\n# changed after selection\n")
        self.assert_refused(self.read())

    def test_metadata_only_schema_substitution_cannot_supply_authority(self):
        authority = self.authorities[0]
        path = self.root / authority.relative_path
        path.write_text("---\natom_id: CA-D-366\nversion: 9\n---\n# Fabricated policy\n")
        self.assert_refused(self.read(authorities=[capture_source(self.root, authority.relative_path), *self.authorities[1:]]))

    def test_snapshot_provenance_and_exported_documents_are_immutable(self):
        document = copy.deepcopy(self.document)
        document["project"]["obsolete_names"] = ["OLD"]
        self.write_document(document)
        value = self.assert_read(self.read())
        for target, field, replacement in (
            (value, "name", "changed"), (value.source, "sha256", "changed"),
            (value.schema_sources[0], "version", 999),
        ):
            with self.subTest(target=type(target).__name__, field=field), self.assertRaises(dataclasses.FrozenInstanceError):
                setattr(target, field, replacement)
        self.assertIsInstance(value.obsolete_names, tuple)
        self.assertIsInstance(value.schema_sources, tuple)
        exported = value.to_document()
        exported["project"]["obsolete_names"].append("ADDED")
        exported["artifacts"]["identity"]["project_prefix"] = "WRONG"
        self.assertEqual(document, value.to_document())
        self.settings.write_bytes(self.settings.read_bytes() + b"\n# later source drift\n")
        self.assertEqual(document, value.to_document())

    def test_invalid_unrelated_journal_is_never_read_and_cannot_change_values(self):
        import connector_bindings
        baseline = self.assert_read(self.read())
        self.journal.mkdir()
        (self.journal / "invalid.ndjson").write_bytes(b"not-json\n")
        (self.journal / "directory.ndjson").mkdir()
        (self.journal / "linked.ndjson").symlink_to(self.settings)
        original = connector_bindings._read_source
        observed = []

        def read_source(path):
            self.assertFalse(path.is_relative_to(self.journal), "Settings Reader accessed Journal history")
            observed.append(path)
            return original(path)

        with mock.patch.object(connector_bindings, "_read_source", read_source):
            current = self.assert_read(self.read())
        self.assertTrue(observed)
        self.assertEqual(baseline, current)

    def test_mid_read_source_change_refuses_without_resealing(self):
        original = FileSource.read_bytes
        changed = False

        def change_settings(source):
            nonlocal changed
            raw = original(source)
            if source.relative_path == self.source.relative_path and not changed:
                changed = True
                self.settings.write_bytes(raw + b"\n# external settings change\n")
            return raw

        with mock.patch.object(FileSource, "read_bytes", change_settings):
            self.assert_refused(reader.read_project_settings(self.source, schema_sources=self.authorities))

    def test_noncanonical_or_missing_selected_carrier_has_no_legacy_fallback(self):
        original = self.settings.read_bytes()
        for relative in ("legacy.toml", ".caprmedio_independent/project_settings.toml",
                         "nested/.caprmedio_independent/caprmedio_project_settings.toml"):
            with self.subTest(relative=relative):
                path = self.root / relative
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_bytes(original)
                self.assert_refused(self.read(source=capture_source(self.root, relative)))
        self.settings.unlink()
        self.assert_refused(self.read(source=capture_source(self.root, self.settings.relative_to(self.root))))

    def test_retained_settings_and_schema_pins_refuse_new_symlinks(self):
        external = self.root / "external-settings.toml"
        external.write_bytes(self.settings.read_bytes())
        self.settings.unlink()
        self.settings.symlink_to(external)
        self.assert_refused(self.read())
        self.settings.unlink()
        self.settings.write_bytes(external.read_bytes())
        authority = self.authorities[0]
        path = self.root / authority.relative_path
        external_authority = self.root / "external-authority.md"
        external_authority.write_bytes(path.read_bytes())
        path.unlink()
        path.symlink_to(external_authority)
        self.assert_refused(self.read())


if __name__ == "__main__":
    unittest.main()
