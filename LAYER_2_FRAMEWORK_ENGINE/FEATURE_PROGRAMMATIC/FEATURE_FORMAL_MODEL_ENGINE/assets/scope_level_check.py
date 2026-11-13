# Generated from the selected reviewed Formal Claim.
SOURCE_REFERENCE = 'CA-R-2554@3'
SOURCE_SHA256 = 'f530d8653e4159f042c8ab8658b63d52767b2905a0a6ada53b3d25d1789838c5'
CLAIM_SHA256 = '786908c62264680d015c5843833a2c588304c31cc799369549fca3a0e1e6cf5f'
from FEATURE_FORMAL_MODEL_ENGINE.scope_levels import ScopeUnit

def check_structural_level(unit: ScopeUnit) -> bool:
    if unit.structural_level is None:
        return False
    if unit.container is None:
        return unit.structural_level == 0
    return (
        unit.container.structural_level is not None
        and unit.structural_level == unit.container.structural_level + 1
    )
