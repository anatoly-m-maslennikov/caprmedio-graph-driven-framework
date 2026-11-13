"""Evaluation is separate from parsing and uses exact reviewed code."""

from dataclasses import dataclass
from hashlib import sha256
from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from FEATURE_FORMAL_MODEL_ENGINE.reviewed_instance_check import bind_reviewed_instance_check


@dataclass(frozen=True)
class ScopeUnit:
    structural_level: int
    container: "ScopeUnit | None" = None


CLAIM = """from caprmedio.formal_claims import declare_entity
from caprmedio.model import ScopeUnit

def check_structural_level(unit: ScopeUnit) -> bool:
    expected = 0 if unit.container is None else unit.container.structural_level + 1
    return unit.structural_level == expected

declare_entity(entity_name="structural_level", relation_name="IS_PROPERTY_OF",
               base_path="Scope Unit", instance_check=check_structural_level)
"""


class ReviewedInstanceCheckTests(unittest.TestCase):
    def bind(self, claim=CLAIM, *, reviewed_claim=CLAIM, model_types=None):
        if model_types is None:
            model_types = {"ScopeUnit": ScopeUnit}
        return bind_reviewed_instance_check(
            claim,
            reference="CA-R-2554",
            reviewed_claim_sha256=sha256(reviewed_claim.encode()).hexdigest(),
            model_types=model_types,
        )

    def test_evaluates_root_and_contained_instances(self):
        validate = self.bind()
        root = ScopeUnit(0)
        self.assertTrue(validate(root))
        self.assertTrue(validate(ScopeUnit(1, root)))
        self.assertFalse(validate(ScopeUnit(1)))
        self.assertFalse(validate(ScopeUnit(3, root)))
        with self.assertRaisesRegex(TypeError, "requires ScopeUnit"):
            validate({"structural_level": 0})

    def test_rejects_unreviewed_source_and_unbound_type(self):
        with self.assertRaisesRegex(ValueError, "differs from the reviewed source"):
            self.bind(CLAIM.replace("expected", "changed"))
        with self.assertRaisesRegex(ValueError, "unbound Model type"):
            self.bind(model_types={})

    def test_requires_a_boolean_result(self):
        claim = CLAIM.replace("return unit.structural_level == expected", "return 1")
        validate = self.bind(claim, reviewed_claim=claim)
        with self.assertRaisesRegex(TypeError, "must return bool"):
            validate(ScopeUnit(0))
