# CA-E-804@1

"""Generated relation metadata uses the runtime declaration compiler."""

from __future__ import annotations

import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch


sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND.generate_relation_registry import (
    _source_pin,
    registry_asset,
    write_registry,
)  # noqa: E402
from APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND.relation_registry import compile_registry  # noqa: E402
from APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND.relation_registry_asset import (  # noqa: E402
    load_registry_asset,
)
from APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND.relations import compile_relation_registry  # noqa: E402
import APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND.relation_registry as compiler  # noqa: E402


def declaration(reference: str, name: str, body: str) -> dict:
    return {
        "source_path": f"declarations/{reference}.md",
        "status_group": "Current",
        "id": reference,
        "ref": reference,
        "version": 1,
        "status": "Active",
        "current_scope_unit": None,
        "claim_target_scope_unit": None,
        "role": "Requirement",
        "form": "Relation Declaration",
        "tier": 1,
        "updated_at": None,
        "header_json": {"subjects": {"active": f"CFEL <+ Relation//{name}"}, "relations": {}},
        "_content_bytes": body.encode("utf-8"),
        "content_properties_json": [],
        "relation_edges_json": [],
        "hash": None,
    }


class GeneratedRelationRegistryTests(unittest.TestCase):
    def test_asset_is_deterministic_and_pins_literal_declaration_inputs(self) -> None:
        direct = declaration(
            "CA-R-1",
            "IS_CONTAINED_BY",
            "```CFEL\nRelation//IS_CONTAINED_BY ((HAS_INVERSE)) Relation//CONTAINS;\n```\n",
        )
        inverse = declaration(
            "CA-R-2",
            "CONTAINS",
            "```CFEL\nRelation//CONTAINS <((HAS_INVERSE)) Relation//IS_CONTAINED_BY;\n```\n",
        )

        first = registry_asset([direct, inverse])
        self.assertEqual(first, registry_asset([direct, inverse]))
        payload = json.loads(first)
        self.assertEqual(1, payload["schema_version"])
        self.assertEqual(["CONTAINS", "IS_CONTAINED_BY"], payload["registered_names"])
        self.assertEqual(
            [{"direct": "IS_CONTAINED_BY", "inverse": "CONTAINS"}], payload["inverse_bindings"]
        )
        self.assertEqual(["CA-R-1", "CA-R-2"], [source["atom_id"] for source in payload["sources"]])
        self.assertEqual(64, len(payload["input_digest"]))

        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "canonical_relation_registry.json"
            write_registry(output, first)
            self.assertEqual(first, output.read_bytes())

    def test_invalid_declaration_identity_is_omitted_before_asset_pinning(self) -> None:
        valid = declaration("CA-R-1", "DIRECT", "```CFEL\n```\n")
        invalid = declaration("CA-R-2", "INVERSE", "```CFEL\n```\n")
        invalid["id"] = None
        invalid["version"] = True

        registry = compile_relation_registry([valid, invalid])
        payload = json.loads(registry_asset([valid, invalid]))
        self.assertEqual({"DIRECT"}, set(registry.names))
        self.assertEqual(["CA-R-1"], [source["atom_id"] for source in payload["sources"]])
        self.assertTrue(
            all(
                type(source["version"]) is int and source["version"] > 0
                for source in payload["sources"]
            )
        )
        with self.assertRaisesRegex(ValueError, "positive integer Version"):
            _source_pin(dict(valid, version=True))

    def test_delivered_asset_is_consumed_only_when_its_source_pins_match(self) -> None:
        direct = declaration("CA-R-1", "DIRECT", "```CFEL\n```\n")
        compiled = compile_registry([direct])
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "canonical_relation_registry.json"
            path.write_bytes(registry_asset([direct], compiled))
            delivered = load_registry_asset(path, [direct], compiled)
            self.assertIsNotNone(delivered)
            self.assertIsNot(delivered, compiled.registry)
            self.assertEqual(compiled.registry.names, delivered.names)

            changed = dict(direct, _content_bytes=b"```CFEL\n\n```\n")
            self.assertIsNone(load_registry_asset(path, [changed], compile_registry([changed])))

    def test_asset_source_pins_reuse_the_existing_compilation(self) -> None:
        rows = [
            declaration("CA-R-1", "DIRECT", "```CFEL\n```\n"),
            declaration("CA-R-2", "OTHER", "```CFEL\n```\n"),
        ]
        original = compiler.registry_contribution
        with patch.object(compiler, "registry_contribution", wraps=original) as contribution:
            compiled = compile_registry(rows)
            registry_asset(rows, compiled)
        self.assertEqual(len(rows), contribution.call_count)


if __name__ == "__main__":
    unittest.main()
