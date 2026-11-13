"""Project typed dataclass field contracts without executing Model code."""

from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from FEATURE_FORMAL_MODEL_ENGINE.compiler_claim import compiler_model_statements
from FEATURE_FORMAL_MODEL_ENGINE.native_model_claim import parse_native_model_claim


CLAIM = """from dataclasses import dataclass, field
from caprmedio.formal_claims import Cardinality, declare_entity

@dataclass
class Example:
    id: int = field(metadata={
        "property_occurrence_cardinality": 1,
        "value_cardinality": 1,
    })
    name: str = field(metadata={
        "property_occurrence_cardinality": Cardinality(minimum=0, maximum=1),
        "value_cardinality": Cardinality(minimum=0, maximum=1),
    })

declare_entity(entity_name="Example", entity_class=Example)
"""


class DataclassFieldContractsTests(unittest.TestCase):
    def test_projects_formats_and_both_cardinalities(self):
        declaration = parse_native_model_claim(CLAIM)
        self.assertEqual(
            ("Example.id{::1} :: [int]{::1}", "Example.name{::0..1} :: [string]{::0..1}"),
            compiler_model_statements(declaration),
        )

    def test_unconstrained_class_keeps_existing_behavior(self):
        claim = """from dataclasses import dataclass
from caprmedio.formal_claims import declare_entity

@dataclass
class Example:
    id: int

declare_entity(entity_name="Example", entity_class=Example)
"""
        self.assertEqual((), compiler_model_statements(parse_native_model_claim(claim)))

    def test_rejects_partial_contract_and_unsupported_format(self):
        for claim, error in (
            (CLAIM.replace("    id: int", "    extra: str\n    id: int"), "unsupported dataclass field contract"),
            (CLAIM.replace('"value_cardinality": 1', '"other": 1'), "require occurrence and value cardinalities"),
            (CLAIM.replace("id: int", "id: list[int]"), "unsupported compiler format"),
        ):
            with self.subTest(error=error), self.assertRaisesRegex(ValueError, error):
                compiler_model_statements(parse_native_model_claim(claim))
