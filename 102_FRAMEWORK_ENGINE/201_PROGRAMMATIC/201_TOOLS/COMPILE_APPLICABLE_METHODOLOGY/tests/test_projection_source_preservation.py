from __future__ import annotations

import importlib.util
import sys
import unittest
from pathlib import Path
from unittest import mock


TOOL = Path(__file__).resolve().parents[1] / "compile_applicable_methodology.py"
SPEC = importlib.util.spec_from_file_location("compile_applicable_methodology_projection", TOOL)
assert SPEC and SPEC.loader
compiler = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = compiler
SPEC.loader.exec_module(compiler)


class ProjectionSourcePreservationTest(unittest.TestCase):
    def setUp(self) -> None:
        self.candidate = compiler.Candidate(
            layer="CORE_META_MODEL",
            layer_order=0,
            role="REQUIREMENT",
            role_directory="04_requirement",
            atom_id="CA-R-001",
            version=2,
            source_path=".control/sources/001_CORE_META_MODEL/04_requirement/CA-R-001.md",
            source_sha256="a" * 64,
            basename="CA-R-001.md",
            priority=None,
            priority_group=None,
            replacements=(),
            incompatibilities=(),
            definition_term=None,
            definition_subject_path=None,
            original_relations_sha256="b" * 64,
        )
        self.source = (
            b"---\n"
            b"atom_id: CA-R-001\n"
            b"version: 2\n"
            b"relations: {}\n"
            b"---\n"
            b"# Claim\n\n"
            b"Original body.\n"
        )
        self.relative = "../../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-001.md"

    def test_metadata_formatter_preserves_projection_bytes_exactly(self) -> None:
        expected = compiler.projection_bytes(self.source, self.relative, self.candidate)
        metadata = compiler.projection_metadata_bytes(self.relative, self.candidate)

        self.assertEqual(self.source.replace(b"\n---\n", metadata + b"\n---\n", 1), expected)
        compiler.validate_projection_source_preservation(self.source, expected, self.relative, self.candidate)

        with mock.patch.object(compiler, "projection_bytes", side_effect=AssertionError("renderer must not run")):
            compiler.validate_projection_source_preservation(self.source, expected, self.relative, self.candidate)

    def test_rejects_any_metadata_or_source_byte_change(self) -> None:
        projected = compiler.projection_bytes(self.source, self.relative, self.candidate)
        changed_metadata = projected.replace(b"source_atom_revision: 2", b"source_atom_revision: 3")
        changed_body = projected.replace(b"Original body.", b"Changed body.")

        for changed in (changed_metadata, changed_body):
            with self.assertRaises(compiler.CompileError) as raised:
                compiler.validate_projection_source_preservation(self.source, changed, self.relative, self.candidate)
            self.assertEqual("projection-source-preservation-invalid", raised.exception.code)

    def test_rejects_source_that_already_declares_projection_metadata(self) -> None:
        source = self.source.replace(b"relations: {}\n", b"relations: {}\nprojection:\n")

        with self.assertRaises(compiler.CompileError) as raised:
            compiler.validate_projection_source_preservation(source, source, self.relative, self.candidate)

        self.assertEqual("source-projection-metadata-present", raised.exception.code)


if __name__ == "__main__":
    unittest.main()
