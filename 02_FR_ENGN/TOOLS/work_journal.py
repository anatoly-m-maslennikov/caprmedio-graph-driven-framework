"""Compatibility import for legacy root-level Tool scripts.

The maintained implementation lives in the governed Framework Engine source
tree. Installed Tools do not use this carrier; their self-contained runtime
release contains its own content-identical copy.
"""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path


SOURCE = (
    Path(__file__).resolve().parents[2]
    / ".caprmedio"
    / "200_LAYER_2_FRAMEWORK_ENGINE"
    / "TOOLS"
    / "work_journal.py"
)
SPEC = importlib.util.spec_from_file_location("_caprmedio_work_journal", SOURCE)
if SPEC is None or SPEC.loader is None:
    raise ImportError(f"cannot load canonical Work Journal implementation: {SOURCE}")
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)

for name in dir(MODULE):
    if not name.startswith("_"):
        globals()[name] = getattr(MODULE, name)

