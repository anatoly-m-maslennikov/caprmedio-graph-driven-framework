# CA-D-675@17
# CA-M-500@12

"""Read the fixed Workbench runtime retention setting at startup."""

from __future__ import annotations

from pathlib import Path
import tomllib
import sys

TOOLS = Path(__file__).resolve().parents[3] / "FEATURE_TOOLS"
if str(TOOLS) not in sys.path:
    sys.path.insert(0, str(TOOLS))
from settings_carrier import read_settings_carrier


DEFAULT_RESULT_TTL_SECONDS = 3600
DEFAULT_SCHEMA_MODE = 2


def result_ttl_seconds(root: Path) -> int:
    """Return the declared positive TTL without changing runtime settings."""
    path = Path(root) / ".caprmedio_runtime" / "caprmedio_runtime_settings.toml"
    if not path.exists():
        return DEFAULT_RESULT_TTL_SECONDS
    try:
        document = read_settings_carrier(path)
    except (OSError, UnicodeError, tomllib.TOMLDecodeError) as error:
        raise ValueError("invalid Workbench runtime settings") from error
    workbench = document.get("workbench", {})
    if not isinstance(workbench, dict):
        raise ValueError("invalid Workbench runtime settings")
    value = workbench.get("result_ttl_seconds", DEFAULT_RESULT_TTL_SECONDS)
    if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
        raise ValueError("workbench.result_ttl_seconds must be a positive integer")
    return value


def schema_mode(root: Path) -> int:
    """Return the selected cold-start schema mode without a public query option."""
    path = Path(root) / ".caprmedio_runtime" / "caprmedio_runtime_settings.toml"
    if not path.exists():
        return DEFAULT_SCHEMA_MODE
    try:
        document = read_settings_carrier(path)
    except (OSError, UnicodeError, tomllib.TOMLDecodeError) as error:
        raise ValueError("invalid Workbench runtime settings") from error
    workbench = document.get("workbench", {})
    if not isinstance(workbench, dict):
        raise ValueError("invalid Workbench runtime settings")
    value = workbench.get("schema_mode", DEFAULT_SCHEMA_MODE)
    if type(value) is not int or value not in {1, 2}:
        raise ValueError("workbench.schema_mode must be 1 or 2")
    return value
