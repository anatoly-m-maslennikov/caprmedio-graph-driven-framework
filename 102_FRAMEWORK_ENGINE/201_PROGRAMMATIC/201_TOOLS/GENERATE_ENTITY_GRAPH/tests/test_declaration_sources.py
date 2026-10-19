from __future__ import annotations

from pathlib import Path
import hashlib
import sys
import unittest
from unittest.mock import patch


TOOL = Path(__file__).resolve().parents[1]
TOOLS = TOOL.parent
sys.path[:0] = [str(TOOLS), str(TOOL)]

from declaration_sources import compose_declaration_catalog  # noqa: E402
from VALIDATE_ATOMS.validate_atoms_workers.check_sections import GRAPH_RULE_SOURCES  # noqa: E402


def relation_carrier(atom_id: str, subject: str, graph_scope: str, version: int = 1) -> dict:
    body = f"## Scope\n\n`{subject.split(': ')[-1]} Relation` in the **{graph_scope}**.\n\n## Claim\nText."
    raw_body = body + "\n"
    raw = (
        f"---\natom_id: {atom_id}\nversion: {version}\ncontent_role: Requirement\n"
        f"status: Active\n---\n{raw_body}"
    ).encode("utf-8")
    return {
        "source": {
            "atom_id": atom_id,
            "version": version,
            "path": f"{atom_id}.md",
            "sha256": hashlib.sha256(raw).hexdigest(),
        },
        "metadata": {
            "atom_id": atom_id,
            "version": version,
            "content_role": "Requirement",
            "status": "Active",
        },
        "subjects": {"governs": subject},
        "body": body,
        "raw_body": raw_body,
        "raw": raw,
    }


def refresh_raw(carrier: dict) -> None:
    source = carrier["source"]
    metadata = carrier["metadata"]
    body = carrier["body"]
    raw_body = body if body.endswith("\n") else body + "\n"
    carrier["raw_body"] = raw_body
    raw = (
        f"---\natom_id: {source['atom_id']}\nversion: {source['version']}\n"
        f"content_role: {metadata['content_role']}\nstatus: {metadata['status']}\n---\n{raw_body}"
    ).encode("utf-8")
    source["sha256"] = hashlib.sha256(raw).hexdigest()
    carrier["raw"] = raw


def graph_rule_carrier(atom_id: str = "CA-R-901021", version: int = 3, yaml_type: str = "whitelist") -> dict:
    yaml_block = (
        "```yaml\ngraph_rule_type: " + yaml_type + "\napplies_to:\n"
        "  relation_type: evaluation_for\ncondition:\n"
        '  source: ["Entity/Node/Continuant/Atom/Content Role: Evaluation"]\n'
        '  target: ["Entity/Node/Continuant/Atom/Content Role: Requirement"]\n```\n'
    )
    body = "# Summary\n\nPermit evaluation links.\n\n" + yaml_block
    metadata = {
        "atom_id": atom_id,
        "version": version,
        "content_role": "Requirement",
        "type": "Graph Rule",
        "status": "Active",
    }
    raw = (
        f"---\natom_id: {atom_id}\nversion: {version}\ncontent_role: Requirement\n"
        f"type: Graph Rule\nstatus: Active\n---\n{body}"
    ).encode("utf-8")
    return {
        "source": {
            "atom_id": atom_id,
            "version": version,
            "path": f"{atom_id}.md",
            "sha256": hashlib.sha256(raw).hexdigest(),
        },
        "metadata": metadata,
        "subjects": {"governs": "Entity/Node/Continuant/Atom.Relations"},
        "body": body,
        "raw_body": body,
        "raw": raw,
    }


def support_carriers() -> tuple[list[dict], dict[str, dict]]:
    rows = []
    entries = {}
    role_by_code = {"C": "Concern", "A": "Analysis", "P": "Plan", "R": "Requirement", "M": "Method", "E": "Evaluation", "D": "Delivery", "O": "Operations"}
    for identifier in GRAPH_RULE_SOURCES:
        role_code = identifier.rsplit("-", 2)[1]
        version = 1
        text = f"Current support evidence for {identifier} at {version}."
        raw = text.encode("utf-8")
        rows.append(
            {
                "source": {
                    "atom_id": identifier,
                    "version": version,
                    "path": f"{identifier}.md",
                    "sha256": hashlib.sha256(raw).hexdigest(),
                },
                "metadata": {
                    "atom_id": identifier,
                    "version": version,
                    "content_role": role_by_code[role_code],
                    "status": "Active",
                },
                "raw": raw,
            }
        )
        entries[identifier] = {}
    return rows, entries


class DeclarationSourcesTests(unittest.TestCase):
    def test_relation_identity_is_graph_kind_and_exact_literal_name(self):
        carriers = [
            relation_carrier(
                "CA-R-901001", "Entity/Relation/Type: NARROWER_THAN", "Entities Graph"
            ),
            relation_carrier(
                "CA-R-901002", "Entity/Relation/Type: NARROWER_THAN", "Terms Graph"
            ),
            relation_carrier("CA-R-901003", "IS_BORNE_BY", "Entities Graph", version=2),
            relation_carrier("CA-R-901004", "BORNE_BY", "Entities Graph"),
            relation_carrier("CA-R-901005", "Entity/Relation/Type: NARROWER_THAN", "Entities Graph"),
            relation_carrier("CA-R-901007", "IS_ALLOWED_VALUE_OF", "Entities Graph"),
            {
                **relation_carrier("CA-R-901006", "a prose topic", "Entities Graph"),
                "subjects": {"governs": "Entity/Node/Continuant/Atom"},
            },
        ]
        carriers[2]["body"] = (
            "## Scope\n\nAn IS_BORNE_BY Relation from Entity A to Entity B **in** the Entities Graph.\n"
            "\n## Claim\nText."
        )
        refresh_raw(carriers[2])
        carriers[-2]["body"] = carriers[-2]["body"].replace("in the", "within the")
        refresh_raw(carriers[-2])

        catalog = compose_declaration_catalog(carriers)
        rows = {(row["graph_kind"], row["canonical_name"]): row for row in catalog["relation_types"]}

        self.assertEqual(
            set(rows),
            {
                ("Entities Graph", "NARROWER_THAN"),
                ("Terms Graph", "NARROWER_THAN"),
                ("Entities Graph", "IS_BORNE_BY"),
                ("Entities Graph", "BORNE_BY"),
                ("Entities Graph", "IS_ALLOWED_VALUE_OF"),
            },
        )
        self.assertEqual(len(rows[("Entities Graph", "NARROWER_THAN")]["sources"]), 2)
        self.assertEqual(
            rows[("Entities Graph", "IS_BORNE_BY")]["sources"][0]["version"], 2
        )
        self.assertEqual(
            rows[("Entities Graph", "NARROWER_THAN")]["metadata"],
            {
                "meaning": None,
                "direction": None,
                "inverse": None,
                "authority_effect": None,
                "transitivity": None,
                "applicability": None,
                "status": None,
                "exclusive_purpose": None,
            },
        )
        self.assertTrue(rows[("Entities Graph", "NARROWER_THAN")]["evidence"])

    def test_relation_candidates_without_unique_scope_graph_remain_unresolved(self):
        missing_scope = relation_carrier(
            "CA-R-901011", "Entity/Relation/Type: CONTAINS", "Entities Graph"
        )
        missing_scope["body"] = "## Scope\n\nA named relation but no owner.\n"
        ambiguous_scope = relation_carrier(
            "CA-R-901012", "Entity/Relation/Type: CONTAINS", "Entities Graph"
        )
        ambiguous_scope["body"] = (
            "## Scope\n\nCONTAINS Relation in the Entities Graph and in the Terms Graph.\n"
        )
        refresh_raw(missing_scope)
        refresh_raw(ambiguous_scope)

        catalog = compose_declaration_catalog([missing_scope, ambiguous_scope])

        self.assertEqual(catalog["relation_types"], [])
        self.assertEqual(len(catalog["unresolved"]), 2)
        self.assertTrue(all("owning graph kind" in row["reason"] for row in catalog["unresolved"]))

    def test_scope_does_not_admit_incidental_graph_mention_or_fenced_fake_scope(self):
        incidental = relation_carrier("CA-R-901013", "IS_BORNE_BY", "Entities Graph")
        incidental["body"] = (
            "## Scope\n\nIS_BORNE_BY Relation is described here. The check applies to the Entities Graph.\n"
        )
        refresh_raw(incidental)
        fenced = relation_carrier("CA-R-901014", "IS_BORNE_BY", "Entities Graph")
        fenced["body"] = (
            "```markdown\n## Scope\n\nIS_BORNE_BY Relation in the Entities Graph.\n```\n"
            "## Claim\nReal body without a Scope.\n"
        )
        refresh_raw(fenced)

        catalog = compose_declaration_catalog([incidental, fenced])

        self.assertEqual(catalog["relation_types"], [])
        self.assertEqual(len(catalog["unresolved"]), 2)

    def test_current_support_sources_admit_valid_rule_and_input_order_is_irrelevant(self):
        supports, entries = support_carriers()
        carriers = [*supports, graph_rule_carrier()]
        with patch(
            "VALIDATE_ATOMS.validate_atoms_workers.support_authority.support_sources",
            return_value=entries,
        ):
            catalog = compose_declaration_catalog(carriers)
            reversed_catalog = compose_declaration_catalog(list(reversed(carriers)))

        self.assertEqual(catalog, reversed_catalog)
        self.assertEqual(len(catalog["graph_rules"]), 1)
        rule = catalog["graph_rules"][0]
        self.assertEqual(rule["source"]["atom_id"], "CA-R-901021")
        self.assertEqual(rule["subject"], "Entity/Node/Continuant/Atom.Relations")
        self.assertTrue(rule["yaml_block"].startswith("```yaml\n"))
        self.assertEqual(catalog["unresolved"], [])

    def test_rule_admission_preserves_crlf_and_requires_source_bound_raw_body(self):
        supports, entries = support_carriers()
        crlf = graph_rule_carrier("CA-R-901041")
        crlf["raw_body"] = crlf["raw_body"].replace("\n", "\r\n")
        prefix = crlf["raw"].split(b"# Summary", 1)[0]
        crlf["raw"] = prefix + crlf["raw_body"].encode("utf-8")
        crlf["source"]["sha256"] = hashlib.sha256(crlf["raw"]).hexdigest()
        missing_body = graph_rule_carrier("CA-R-901042")
        del missing_body["raw_body"]
        mismatched_body = graph_rule_carrier("CA-R-901043")
        mismatched_body["raw_body"] = mismatched_body["raw_body"].replace("Permit", "Alter")
        carriers = [*supports, crlf, missing_body, mismatched_body]

        with patch(
            "VALIDATE_ATOMS.validate_atoms_workers.support_authority.support_sources",
            return_value=entries,
        ):
            catalog = compose_declaration_catalog(carriers)

        self.assertEqual(len(catalog["graph_rules"]), 1)
        self.assertIn("\r\n", catalog["graph_rules"][0]["yaml_block"])
        block_start = crlf["raw_body"].index("```yaml")
        block_end = crlf["raw_body"].index("```", block_start + len("```yaml")) + 3
        expected_block = crlf["raw_body"][block_start : block_end + len("\r\n")]
        self.assertEqual(catalog["graph_rules"][0]["yaml_block"], expected_block)
        self.assertEqual(len(catalog["unresolved"]), 2)
        self.assertTrue(all("source" in row["reason"].lower() or "raw_body" in row["reason"] for row in catalog["unresolved"]))

    def test_optional_rule_docs_do_not_change_catalog_summary_or_operative_yaml(self):
        supports, entries = support_carriers()
        carrier = graph_rule_carrier("CA-R-901044")
        carrier["body"] = carrier["body"].replace("\n", "\r\n") + (
            "## Details\r\n\r\n"
            "Illustrative only; graph_rule_type: blacklist is not operative here.\r\n\r\n"
            "```yaml\r\n"
            "graph_rule_type: blacklist\r\n"
            "condition: {example: true}\r\n"
            "```\r\n\r\n"
            "## Semantics\r\n\r\n"
            "A readable explanation of the admitted whitelist.\r\n"
        )
        refresh_raw(carrier)
        body = carrier["raw_body"]
        block_start = body.index("```yaml")
        block_end = body.index("```", block_start + len("```yaml")) + 3
        expected_block = body[block_start : block_end + len("\r\n")]

        with patch(
            "VALIDATE_ATOMS.validate_atoms_workers.support_authority.support_sources",
            return_value=entries,
        ):
            catalog = compose_declaration_catalog([*supports, carrier])

        self.assertEqual(len(catalog["graph_rules"]), 1)
        rule = catalog["graph_rules"][0]
        self.assertEqual(rule["summary"], "Permit evaluation links.")
        self.assertEqual(rule["yaml_block"], expected_block)
        self.assertIn("\r\n", rule["yaml_block"])
        self.assertEqual(rule["evidence"], body)
        self.assertEqual(catalog["unresolved"], [])

    def test_malformed_and_unsupported_rules_remain_unresolved_examples_are_ignored(self):
        supports, entries = support_carriers()
        malformed = graph_rule_carrier("CA-R-901031")
        malformed["body"] = "# Summary\n\nBroken payload.\n\n```yaml\nnot: [valid\n```\n"
        refresh_raw(malformed)
        unsupported = graph_rule_carrier("CA-R-901032", yaml_type="blacklist")
        example = {
            **relation_carrier("CA-D-901033", "Entity/Node/Continuant/Atom", "Entities Graph"),
            "body": "## Scope\n\nD637 Graph Rule example only; not a declaration.\n",
        }
        refresh_raw(example)
        carriers = [*supports, malformed, unsupported, example]

        with patch(
            "VALIDATE_ATOMS.validate_atoms_workers.support_authority.support_sources",
            return_value=entries,
        ):
            catalog = compose_declaration_catalog(carriers)

        self.assertEqual(catalog["graph_rules"], [])
        self.assertEqual(len(catalog["unresolved"]), 2)
        self.assertTrue(any("structural validation" in row["reason"] for row in catalog["unresolved"]))

    def test_rule_does_not_drop_invalid_entries_from_governs_list(self):
        supports, entries = support_carriers()
        malformed_subjects = graph_rule_carrier("CA-R-901051")
        malformed_subjects["subjects"]["governs"] = [
            "Entity/Node/Continuant/Atom.Relations",
            7,
        ]
        with patch(
            "VALIDATE_ATOMS.validate_atoms_workers.support_authority.support_sources",
            return_value=entries,
        ):
            catalog = compose_declaration_catalog([*supports, malformed_subjects])

        self.assertEqual(catalog["graph_rules"], [])
        self.assertEqual(len(catalog["unresolved"]), 1)
        self.assertIn("exactly one nonempty valid governed Subject", catalog["unresolved"][0]["reason"])

    def test_graph_rule_keeps_exact_yaml_but_is_not_admitted_without_support_sources(self):
        yaml_block = (
            "```yaml\ngraph_rule_type: whitelist\napplies_to:\n"
            "  relation_type: evaluation_for\ncondition:\n"
            '  source: ["Entity/Node/Continuant/Atom/Content Role: Evaluation"]\n'
            '  target: ["Entity/Node/Continuant/Atom/Content Role: Requirement"]\n```'
        )
        body = "# Summary\n\nPermit evaluation links.\n\n" + yaml_block + "\n"
        raw = b"---\natom_id: CA-R-901021\nversion: 3\ncontent_role: Requirement\ntype: Graph Rule\nstatus: Active\n---\n" + body.encode("utf-8")
        carrier = {
            "source": {
                "atom_id": "CA-R-901021",
                "version": 3,
                "path": "CA-R-901021.md",
                "sha256": hashlib.sha256(raw).hexdigest(),
            },
            "metadata": {
                "atom_id": "CA-R-901021",
                "version": 3,
                "content_role": "Requirement",
                "type": "Graph Rule",
                "status": "Active",
            },
            "subjects": {"governs": "Entity/Node/Continuant/Atom.Relations"},
            "body": body,
            "raw_body": body,
            "raw": raw,
        }

        catalog = compose_declaration_catalog([carrier])

        self.assertEqual(catalog["graph_rules"], [])
        self.assertEqual(len(catalog["unresolved"]), 1)
        unresolved = catalog["unresolved"][0]
        self.assertIn("source-bound Graph Rule governing authority", unresolved["reason"])
        self.assertEqual(unresolved["yaml_block"], yaml_block + "\n")


if __name__ == "__main__":
    unittest.main()
