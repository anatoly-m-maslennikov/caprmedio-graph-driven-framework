# CA-D-578@2
# CA-D-639@14

"""Use the MCP service's fixed routes without importing its server runtime."""

from __future__ import annotations

import sys
from pathlib import Path


def _canonical_paths() -> tuple[str, str]:
    feature_mcp = Path(__file__).resolve().parents[1]
    if str(feature_mcp) not in sys.path:
        sys.path.insert(0, str(feature_mcp))
    from http_paths import HEALTH_PATH, MCP_PATH

    return MCP_PATH, HEALTH_PATH


MCP_PATH, HEALTH_PATH = _canonical_paths()

__all__ = ["HEALTH_PATH", "MCP_PATH"]
