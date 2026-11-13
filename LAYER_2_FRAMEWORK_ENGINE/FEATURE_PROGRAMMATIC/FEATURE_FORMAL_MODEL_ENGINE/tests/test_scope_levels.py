"""The reviewed check uses stored levels from Scope declarations."""

from hashlib import sha256
from pathlib import Path
from types import SimpleNamespace
import sys
import unittest

PROGRAMMATIC = Path(__file__).resolve().parents[2]
sys.path[:0] = [str(PROGRAMMATIC), str(PROGRAMMATIC / "FEATURE_TOOLS")]

from FEATURE_FORMAL_MODEL_ENGINE.scope_levels import check_scope_levels
from scope_declaration_parse import ScopeUnitDeclaration


CLAIM = """from caprmedio.formal_claims import declare_entity
from caprmedio.model import ScopeUnit

def check_structural_level(unit: ScopeUnit) -> bool:
    return unit.structural_level == (0 if unit.container is None else unit.container.structural_level + 1)

declare_entity(entity_name="structural_level", relation_name="IS_PROPERTY_OF",
               base_path="Scope Unit", instance_check=check_structural_level)
"""


class ScopeLevelsTests(unittest.TestCase):
    def test_checks_authored_levels_and_reports_missing_parent_data(self):
        def record(name, level, parent=None):
            return ScopeUnitDeclaration(name, "CA-R-1", 1, Path("scope.md"), parent=parent, structural_level=level)

        declarations = SimpleNamespace(by_name={
            "root": record("root", 0),
            "valid": record("valid", 1, "root"),
            "wrong": record("wrong", 2, "root"),
            "legacy": record("legacy", None, "root"),
            "missing_container_level": record("missing_container_level", 2, "legacy"),
        })
        self.assertEqual({
            "wrong": "Structural level violates the reviewed Claim",
            "legacy": "Missing structural_level",
            "missing_container_level": "Container is missing structural_level",
        }, check_scope_levels(declarations, CLAIM, reference="CA-R-2554",
                              reviewed_claim_sha256=sha256(CLAIM.encode()).hexdigest()))
