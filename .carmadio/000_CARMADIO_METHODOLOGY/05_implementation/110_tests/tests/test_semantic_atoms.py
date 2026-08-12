"""Verify DSET semantic atoms behavior.

Assurance scope: deterministic behavior owned by this module.
Non-obvious fixtures: documented by the fixture that owns them.
Host requirements: an isolated supported Python environment.
"""

from __future__ import annotations

import hashlib
import unittest
from pathlib import Path

from dset_toolchain.adopter import create_adopter
from dset_toolchain.layout import discover_layout
from dset_toolchain.legacy_authority import (
    legacy_authority_ids,
    validate_legacy_authority_ledger,
)
from dset_toolchain.semantic_atoms import (
    archive_atom,
    build_semantic_atom_index,
    collect_semantic_atoms,
    seal_atom,
    validate_semantic_atoms,
)
from dset_toolchain.semantic_types import build_semantic_classification_index
from dset_toolchain.structured_data import dump, load
from dset_toolchain.temp_paths import temporary_directory
from dset_toolchain.toml_codec import loads as load_toml
from tests import repository_root

# ROOT locates the repository fixture; repository layout is authoritative.
ROOT = repository_root(Path(__file__))


class SemanticAtomTests(unittest.TestCase):
    """Verify semantic atom behavior."""

    def setUp(self) -> None:
        """Handle set up using the declared repository contract."""
        self.temporary = temporary_directory()
        self.root = create_adopter(ROOT, Path(self.temporary.name) / "adopter")
        self.atom_path = (
            self.root / "dset/changes/CARMADIO-ATOMIC-RECORD-001-output-contract.md"
        )

    def tearDown(self) -> None:
        """Handle tear down using the declared repository contract."""
        self.temporary.cleanup()

    def test_repository_atom_and_conflict_schemas_are_valid(self) -> None:
        self.assertEqual(validate_semantic_atoms(ROOT), [])
        schema_root = ROOT / "12_layer_gov/120_schemas"
        schemas = (
            "010_dset-gov-schemas-atom.schema.toml",
            "040_dset-gov-schemas-conflict-candidate.schema.toml",
            "050_dset-gov-schemas-conflict-result.schema.toml",
        )
        for name in schemas:
            with self.subTest(name=name):
                load_toml((schema_root / name).read_text(encoding="utf-8"))

    def test_legacy_authority_fragments_are_immutable(self) -> None:
        package_root = self.root / "dset/specs/packages/sample"
        package = discover_layout(self.root).structured_file(
            package_root, "package.toml"
        )
        data = load(package)
        assert isinstance(data, dict)
        data["contracts"] = []
        package.write_text(dump(data, package), encoding="utf-8")

        messages = [item.message for item in validate_semantic_atoms(self.root)]

        self.assertIn(
            "legacy Decision authority changed without native successors",
            messages,
        )

    def test_legacy_ledger_keeps_historical_yaml_identity_after_toml_cutover(
        self,
    ) -> None:
        with temporary_directory() as raw:
            root = Path(raw).resolve()
            governance = root / "dset/governance"
            package_root = root / "dset/specs/packages/sample"
            governance.mkdir(parents=True)
            package_root.mkdir(parents=True)
            (root / "dset/dset.yaml").write_text(
                'schema_version: "1.0"\n', encoding="utf-8"
            )
            historical = package_root / "package.yaml"
            historical.write_text(
                "contracts:\n  - CARMADIO-CONTRACT-GOV-001\n",
                encoding="utf-8",
            )
            (package_root / "package.toml").write_text(
                "contracts = []\n", encoding="utf-8"
            )
            selector = "contracts:CARMADIO-CONTRACT-GOV-001"
            digest = hashlib.sha256(f"{selector}\n".encode()).hexdigest()
            (governance / "legacy-authority.yaml").write_text(
                'schema_version: "1.0"\n'
                "records:\n"
                "  -\n"
                "    semantic_id: CARMADIO-CONTRACT-GOV-001\n"
                "    type: decision\n"
                "    subtype: contract\n"
                "    fragments:\n"
                "      -\n"
                "        path: dset/specs/packages/sample/package.yaml\n"
                f"        selector: {selector}\n"
                f"        sha256: {digest}\n",
                encoding="utf-8",
            )

            self.assertEqual(validate_legacy_authority_ledger(root), [])
            self.assertIn("CARMADIO-CONTRACT-GOV-001", legacy_authority_ids(root))
            rows = {
                str(item["id"]): item
                for item in build_semantic_classification_index(root)
            }
            self.assertEqual(rows["CARMADIO-CONTRACT-GOV-001"]["subtype"], "contract")
            self.assertTrue(rows["CARMADIO-CONTRACT-GOV-001"]["historical_carrier"])

            historical.write_text("contracts: []\n", encoding="utf-8")
            messages = [item.message for item in validate_legacy_authority_ledger(root)]
            self.assertIn(
                "legacy Decision authority changed without native successors",
                messages,
            )

    def test_four_type_atom_is_sealed_and_later_mutation_fails(self) -> None:
        self._write_atom()

        seal_atom(self.root, self.atom_path)

        atoms, diagnostics = collect_semantic_atoms(self.root)
        self.assertEqual(diagnostics, [])
        self.assertEqual(atoms["CARMADIO-DECISION-001"].semantic_type, "decision")
        self.assertEqual(atoms["CARMADIO-DECISION-001"].subtype, "contract")
        self.assertEqual(validate_semantic_atoms(self.root), [])

        self.atom_path.write_text(
            self.atom_path.read_text(encoding="utf-8") + "Changed.\n",
            encoding="utf-8",
        )
        messages = [item.message for item in validate_semantic_atoms(self.root)]
        self.assertIn(
            "sealed atom sha256 changed: CARMADIO-DECISION-001",
            messages,
        )

    def test_sealing_repeats_repository_backed_emission_gate(self) -> None:
        text = self._write_atom().replace('authority: "operator:test-operator"\n', "")
        self.atom_path.write_text(text, encoding="utf-8")

        with self.assertRaisesRegex(
            ValueError, "artifact emission is blocked: material field"
        ):
            seal_atom(self.root, self.atom_path)

    def test_new_atom_cannot_seal_legacy_child_of(self) -> None:
        text = self._write_atom().replace(
            "promotion:\n  parent_scope: null\n",
            "promotion:\n  parent_scope: null\nchild_of:\n  - CARMADIO-REQUIREMENT-001\n",
        )
        self.atom_path.write_text(text, encoding="utf-8")

        with self.assertRaisesRegex(ValueError, "sealed compatibility input only"):
            seal_atom(self.root, self.atom_path)

    def test_invalid_nested_or_qa_empty_subtype_fails(self) -> None:
        self._write_atom()
        self.atom_path.write_text(
            self.atom_path.read_text(encoding="utf-8").replace(
                "type: decision\nsubtype: contract",
                "type: qa\nsubtype: requirement/test",
            ),
            encoding="utf-8",
        )

        messages = [item.message for item in validate_semantic_atoms(self.root)]

        self.assertIn("atom has an invalid direct subtype", messages)

    def test_archive_moves_atom_byte_for_byte_and_updates_lookup(self) -> None:
        self._write_atom()
        original = self.atom_path.read_bytes()
        seal_atom(self.root, self.atom_path)

        destination = archive_atom(self.root, "CARMADIO-DECISION-001")

        self.assertEqual(destination.read_bytes(), original)
        self.assertFalse(self.atom_path.exists())
        self.assertEqual(validate_semantic_atoms(self.root), [])
        row = build_semantic_atom_index(self.root)[0]
        self.assertTrue(row["archived"])
        self.assertEqual(row["current_status"], "archived")
        self.assertEqual(row["path"], destination.relative_to(self.root).as_posix())

    def test_archive_rejects_active_structural_dependants(self) -> None:
        self._write_atom()
        seal_atom(self.root, self.atom_path)
        second = self.root / "dset/changes/CARMADIO-ATOMIC-RECORD-002-format.md"
        second.write_text(
            self._atom_text(
                carrier="CARMADIO-ATOMIC-RECORD-002",
                semantic="CARMADIO-CONTRACT-002",
            ).replace(
                "llm_session_ids:\n",
                "relations:\n"
                "  - type: child_of\n"
                "    target: CARMADIO-DECISION-001\n"
                "llm_session_ids:\n",
            ),
            encoding="utf-8",
        )
        seal_atom(self.root, second)

        with self.assertRaisesRegex(ValueError, "active child reliance"):
            archive_atom(self.root, "CARMADIO-DECISION-001")

    def _write_atom(self) -> str:
        """Write atom using the declared repository contract."""
        text = self._atom_text(
            carrier="CARMADIO-ATOMIC-RECORD-001",
            semantic="CARMADIO-DECISION-001",
        )
        self.atom_path.write_text(text, encoding="utf-8")
        return text

    @staticmethod
    def _atom_text(*, carrier: str, semantic: str) -> str:
        """Handle text using the declared repository contract."""
        return f"""---
artifact_type: atomic_record
artifact_id: {carrier}
type: decision
subtype: contract
semantic_id: {semantic}
status: accepted
priority: high
authority: "operator:test-operator"
claim: "The output contract governs this project."
scope:
  kind: project
  id: dset-temporary-adopter
promotion:
  parent_scope: null
llm_session_ids:
  - "codex:test-session"
---

# Contract
"""


if __name__ == "__main__":
    unittest.main()
