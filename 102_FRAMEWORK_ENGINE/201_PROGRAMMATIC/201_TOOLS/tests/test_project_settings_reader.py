"""Standalone Settings reader: complete schema and retained physical byte pins."""

from __future__ import annotations

import copy
from dataclasses import FrozenInstanceError
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

TOOLS = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(TOOLS))
from connector_bindings import FileSource, capture_source
from connector_toml_parse import render_document
from project_settings_reader import SCHEMA_PINS, read_project_settings
from project_settings_schema import _SchemaError, _parse_settings, mcp_tool_blacklist


REPOSITORY = TOOLS.parents[2]
CONTROL = REPOSITORY / ".caprmedio_caprmedio"
CORE = CONTROL / "101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL"
ENGINE = CONTROL / "102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC"
DOCUMENT = {"schema_version": "2.0", "project": {"name": "reader"},
            "artifacts": {"identity": {"project_prefix": "READ"}},
            "paths": {"control_root": ".caprmedio_reader"}}


class ProjectSettingsReaderTests(unittest.TestCase):
    def setUp(self):
        scratch = Path.cwd() / ".caprmedio_tmp/tests/project-settings-reader"
        scratch.mkdir(parents=True, exist_ok=True)
        temporary = tempfile.TemporaryDirectory(dir=scratch)
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name).resolve()
        self.control = self.root / ".caprmedio_reader"
        self.control.mkdir()
        self.path = self.control / "caprmedio_project_settings.toml"
        self.path.write_bytes(render_document(DOCUMENT))
        self.schemas = []
        authority = self.root / "authority"
        authority.mkdir()
        for identity in SCHEMA_PINS:
            base = ENGINE if identity in {"CA-M-284", "CA-D-520"} else CORE
            candidates = [path for path in base.rglob(identity + "-*.md") if "archive" not in path.parts]
            self.assertEqual(1, len(candidates), identity)
            target = authority / candidates[0].name
            target.write_bytes(candidates[0].read_bytes())
            self.schemas.append(capture_source(self.root, target.relative_to(self.root)))
        self.source = capture_source(self.root, self.path.relative_to(self.root))

    def snapshot(self):
        return {path.relative_to(self.root).as_posix(): path.read_bytes()
                for path in self.root.rglob("*") if path.is_file()}

    def read(self):
        before = self.snapshot()
        result = read_project_settings(self.source, schema_sources=self.schemas)
        self.assertEqual(before, self.snapshot())
        return result

    def test_complete_schema_optional_absence_and_exact_value_copy(self):
        self.assertEqual(("reader", "READ", ".caprmedio_reader", None, None, None), _parse_settings(copy.deepcopy(DOCUMENT)))
        document = copy.deepcopy(DOCUMENT)
        document["project"]["obsolete_names"] = [" reader ", "reader", "reader"]
        self.assertEqual(tuple(document["project"]["obsolete_names"]), _parse_settings(document)[3])
        document["project"]["obsolete_names"] = []
        self.assertEqual((), _parse_settings(document)[3])

    def test_closed_complete_schema_refuses_each_level_and_wrong_types(self):
        cases = []
        for path in ((), ("project",), ("artifacts",), ("artifacts", "identity"), ("paths",)):
            document = copy.deepcopy(DOCUMENT)
            target = document
            for key in path:
                target = target[key]
            target["legacy"] = "unchanged"
            cases.append(document)
        for field, value in (("schema_version", 2.0), ("schema_version", "1"),
                             ("project", "reader"), ("artifacts", []), ("paths", False)):
            document = copy.deepcopy(DOCUMENT); document[field] = value; cases.append(document)
        for name, prefix, control in (("Reader", "READ", ".caprmedio_Reader"),
                                      ("reader", "read", ".caprmedio_reader"),
                                      ("reader", "READ", "../.caprmedio_reader")):
            document = copy.deepcopy(DOCUMENT)
            document["project"]["name"] = name
            document["artifacts"]["identity"]["project_prefix"] = prefix
            document["paths"]["control_root"] = control
            cases.append(document)
        for document in cases:
            with self.subTest(document=document), self.assertRaises(_SchemaError):
                _parse_settings(document)

    def test_values_and_physical_provenance_are_deeply_immutable(self):
        result = self.read()
        self.assertEqual((), result.errors)
        snapshot = result.snapshot
        self.assertIsNotNone(snapshot)
        self.assertFalse(hasattr(snapshot, "history"))
        self.assertFalse(hasattr(snapshot, "revision"))
        self.assertIsNone(snapshot.project_mcp_http_port)
        self.assertEqual(self.source.sha256, snapshot.source.sha256)
        self.assertEqual(self.source.relative_path.as_posix(), snapshot.source.path)
        self.assertEqual(DOCUMENT, snapshot.to_document())
        changed = snapshot.to_document(); changed["project"]["name"] = "mutated"
        self.assertEqual("reader", snapshot.name)
        for target, field, value in ((snapshot, "name", "mutated"), (snapshot.source, "sha256", "0" * 64),
                                     (snapshot.schema_sources[0], "version", 100)):
            with self.assertRaises(FrozenInstanceError):
                setattr(target, field, value)

    def test_optional_mcp_port_exact_values_presence_and_immutability(self):
        for port in (1, 56317, 65535):
            with self.subTest(port=port):
                document = copy.deepcopy(DOCUMENT)
                document["project_mcp"] = {"http_port": port}
                self.path.write_bytes(render_document(document))
                self.source = capture_source(self.root, self.path.relative_to(self.root))
                result = self.read()
                self.assertEqual((), result.errors)
                self.assertEqual(port, result.snapshot.project_mcp_http_port)
                self.assertEqual(document, result.snapshot.to_document())
                copy_document = result.snapshot.to_document()
                copy_document["project_mcp"]["http_port"] = 1
                self.assertEqual(port, result.snapshot.project_mcp_http_port)
                with self.assertRaises(FrozenInstanceError):
                    result.snapshot.project_mcp_http_port = 1

    def test_optional_mcp_port_refuses_types_range_missing_and_extra_fields(self):
        for value in (None, False, [], "56317", {}, {"http_port": True}, {"http_port": False},
                      {"http_port": 0}, {"http_port": 65536}, {"http_port": -1},
                      {"http_port": 56317.0}, {"http_port": "56317"},
                      {"http_port": 56317, "extra": 1}):
            with self.subTest(value=value):
                document = copy.deepcopy(DOCUMENT)
                document["project_mcp"] = value
                with self.assertRaises(_SchemaError):
                    _parse_settings(document)

    def test_mcp_blacklist_absence_empty_and_exact_names_roundtrip(self):
        for names in (None, [], ["release_version", "public.release", " Release ", "public.release"]):
            with self.subTest(names=names):
                document = copy.deepcopy(DOCUMENT)
                document["project_mcp"] = {"http_port": 56317}
                if names is not None:
                    document["project_mcp"]["tool_blacklist"] = names
                self.path.write_bytes(render_document(document))
                self.source = capture_source(self.root, self.path.relative_to(self.root))
                result = self.read()
                self.assertEqual((), result.errors)
                snapshot = result.snapshot
                self.assertEqual(56317, snapshot.project_mcp_http_port)
                self.assertEqual(None if names is None else tuple(names), snapshot.project_mcp_tool_blacklist)
                self.assertEqual(document, snapshot.to_document())
                self.assertEqual(frozenset(names or ()), mcp_tool_blacklist(snapshot.to_document()))
                exported = snapshot.to_document()
                exported["project_mcp"]["tool_blacklist"] = ["changed"]
                self.assertEqual(document, snapshot.to_document())
        self.assertEqual(frozenset(), mcp_tool_blacklist(DOCUMENT))

    def test_mcp_blacklist_rejects_wrong_types_and_empty_names_without_coercion(self):
        for names in (None, False, 1, "release_version", {}, (), [""], [1], [False], [[]]):
            with self.subTest(names=names):
                document = copy.deepcopy(DOCUMENT)
                document["project_mcp"] = {"http_port": 56317, "tool_blacklist": names}
                with self.assertRaises(_SchemaError) as raised:
                    _parse_settings(document)
                self.assertEqual("project_mcp.tool_blacklist", raised.exception.field)
        with self.assertRaises(_SchemaError):
            _parse_settings({**DOCUMENT, "project_mcp": {"tool_blacklist": []}})

    def test_mcp_blacklist_consumes_frozen_values_without_normalization(self):
        from types import MappingProxyType

        settings = MappingProxyType({"project_mcp": MappingProxyType({"tool_blacklist": ("Public.Release", " public.release ")})})
        self.assertEqual(frozenset({"Public.Release", " public.release "}), mcp_tool_blacklist(settings))
        for settings in ({"project_mcp": False}, {"project_mcp": {"tool_blacklist": "public.release"}},
                         {"project_mcp": {"tool_blacklist": ("",)}}, {"project_mcp": {"tool_blacklist": (False,)}}):
            with self.subTest(settings=settings), self.assertRaises(_SchemaError):
                mcp_tool_blacklist(settings)

    def test_journal_is_never_enumerated_or_read_even_when_malformed(self):
        journal = self.control / "_journal"
        journal.mkdir()
        (journal / "malformed.ndjson").write_bytes(b"not-json\n")
        (journal / "unsafe.ndjson").symlink_to(self.path)
        before = self.snapshot()
        observed = []
        original = FileSource._observe

        def observe(source):
            observed.append(source.relative_path)
            self.assertNotIn("_journal", source.relative_path.parts)
            return original(source)

        with patch.object(FileSource, "_observe", observe), patch("os.scandir", side_effect=AssertionError("Unexpected enumeration")):
            result = read_project_settings(self.source, schema_sources=self.schemas)
        self.assertEqual((), result.errors)
        self.assertTrue(observed)
        self.assertEqual(before, self.snapshot())
        self.assertEqual(DOCUMENT, result.snapshot.to_document())

    def test_unaccepted_or_malformed_schema_sources_have_structured_refusal(self):
        authority = self.root / "authority/malformed.md"
        authority.write_bytes(b"no frontmatter\n")
        malformed = capture_source(self.root, authority.relative_to(self.root))
        result = read_project_settings(self.source, schema_sources=[malformed])
        self.assertIsNone(result.snapshot)
        self.assertEqual("schema_sources", result.errors[0].field)

    def test_original_settings_or_schema_drift_refuses_without_resealing(self):
        self.path.write_bytes(self.path.read_bytes() + b"\n# changed\n")
        self.assertEqual("stale_state", self.read().errors[0].code)
        self.source = capture_source(self.root, self.path.relative_to(self.root))
        authority = self.root / self.schemas[0].relative_path
        authority.write_bytes(authority.read_bytes() + b"\n# changed\n")
        self.assertEqual("stale_state", self.read().errors[0].code)


if __name__ == "__main__":
    unittest.main()
