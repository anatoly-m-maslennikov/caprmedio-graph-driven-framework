# CA-D-675@10

"""Read the fixed Workbench runtime retention setting at startup."""

from __future__ import annotations

from pathlib import Path
import tomllib


DEFAULT_RESULT_TTL_SECONDS = 3600


def result_ttl_seconds(root: Path) -> int:
    """Return the declared positive TTL without changing runtime settings."""
    path = Path(root) / ".caprmedio_runtime" / "caprmedio_runtime_settings.toml"
    if not path.exists():
        return DEFAULT_RESULT_TTL_SECONDS
    try:
        document = tomllib.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, tomllib.TOMLDecodeError) as error:
        raise ValueError("invalid Workbench runtime settings") from error
    workbench = document.get("workbench", {})
    if not isinstance(workbench, dict):
        raise ValueError("invalid Workbench runtime settings")
    value = workbench.get("result_ttl_seconds", DEFAULT_RESULT_TTL_SECONDS)
    if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
        raise ValueError("workbench.result_ttl_seconds must be a positive integer")
    return value
