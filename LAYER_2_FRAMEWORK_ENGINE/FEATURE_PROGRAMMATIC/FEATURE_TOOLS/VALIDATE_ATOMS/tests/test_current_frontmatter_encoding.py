"""D657 encoding semantics stay separate from explicitly loaded historical D276."""

import copy
import hashlib
import json
from pathlib import Path
import sys
import unittest

import yaml

sys.path[:0] = [str(Path(__file__).resolve().parents[2]), str(Path(__file__).resolve().parents[1])]
from validate_atoms_workers.authority import AuthorityContext, Obligation  # noqa: E402
from validate_atoms_workers.check_fields import _common  # noqa: E402
from validate_atoms_workers.check_support import Check  # noqa: E402
from test_authority_checks import source as historical_source  # noqa: E402


def current_source():
    captured = json.loads((Path(__file__).parent / "fixtures/current_encoding_authority.json").read_text())
    text = captured["text"]
    assert hashlib.sha256(text.encode()).hexdigest() == captured["sha256"]
    metadata = yaml.safe_load(text.split("---", 2)[1])
    return {"binding": {"atom_id": "CA-D-657", "version": metadata["version"],
                        "path": captured["source_path"], "sha256": captured["sha256"]},
            "text": text, "metadata": metadata}


def checked(metadata, rows=None):
    rows = [current_source()] if rows is None else rows
    context = AuthorityContext([row["binding"] for row in rows], 0, 0, 0, [], (), {}, False)
    check = Check(Obligation("frontmatter.common_encoding", [], True, "encoding fixture"), context,
                  {"sources": rows})
    _common(metadata, "", check)
    return check


CURRENT = {"content_role": "Requirement", "type": "Rule", "current_scope_unit": "CORE_META_MODEL", "tier": 2}


class CurrentFrontmatterEncodingTests(unittest.TestCase):
    def test_current_encoding_requires_type_and_numeric_tier_not_retired_tiers(self):
        self.assertEqual([], checked(CURRENT).findings)
        self.assertEqual([], checked(CURRENT).gaps)
        for field in ("type", "tier", "content_role", "current_scope_unit"):
            value = {key: item for key, item in CURRENT.items() if key != field}
            self.assertTrue(checked(value).findings)
        for field in ("local_tier", "global_tier", "operators", "identifier", "summary", "claim"):
            self.assertTrue(checked({**CURRENT, field: "legacy"}).findings)
        for value in (True, "2", None, -1):
            self.assertTrue(checked({**CURRENT, "tier": value}).findings)
        for value in (None, "", [], {}):
            self.assertTrue(checked({**CURRENT, "type": value}).findings)

    def test_current_optional_label_encoding_does_not_guess_tier_mapping(self):
        self.assertFalse(checked({**CURRENT, "label": "Explicit"}).findings)
        self.assertTrue(checked({**CURRENT, "label": ""}).findings)
        self.assertTrue(checked({**CURRENT, "tier_label": "Core"}).gaps)
        self.assertTrue(checked({**CURRENT, "type": "Project Goal", "tier": -1}).gaps)

    def test_explicit_historical_source_retains_legacy_encoding(self):
        old = {"content_role": "Requirement", "current_scope_unit": "CORE_META_MODEL",
               "local_tier": "Standard", "global_tier": 11}
        result = checked(old, [historical_source("CA-D-276")])
        self.assertEqual([], result.findings)
        self.assertEqual([], result.gaps)
        self.assertTrue(checked(CURRENT, [historical_source("CA-D-276")]).findings)
        self.assertTrue(checked(old).findings)

    def test_unknown_or_conflicting_authority_is_a_gap(self):
        changed = copy.deepcopy(current_source())
        changed["text"] += "\nAn unreviewed additional condition.\n"
        changed["binding"]["sha256"] = hashlib.sha256(changed["text"].encode()).hexdigest()
        for rows in ([], [current_source(), historical_source("CA-D-276")]):
            self.assertTrue(checked(CURRENT, rows).gaps)

    def test_current_authority_allows_metadata_and_subject_updates(self):
        stale = copy.deepcopy(current_source())
        stale["text"] = stale["text"].replace(
            "  governs: Entity/Carrier/File.YAML Frontmatter\n",
            "  governs: Entity/Carrier/File.YAML Frontmatter/Encoding\n",
        )
        stale["text"] = stale["text"].replace("tier: 3\n", "tier: 4\n", 1)
        stale["metadata"] = yaml.safe_load(stale["text"].split("---", 2)[1])
        stale["binding"]["version"] = stale["metadata"]["version"]
        stale["binding"]["sha256"] = hashlib.sha256(stale["text"].encode()).hexdigest()
        self.assertEqual([], checked(CURRENT, [stale]).findings)
        self.assertEqual([], checked(CURRENT, [stale]).gaps)


if __name__ == "__main__":
    unittest.main()
