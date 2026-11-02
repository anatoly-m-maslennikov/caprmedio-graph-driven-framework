"""Frozen source inputs for golden workflow behavior tests.

The production binding frontier is checked separately against the current
Project.  These fixtures keep behavior tests independent of unrelated
authority-carrier revisions while they exercise the current implementation.
"""
import importlib.util
import json
from pathlib import Path


HERE = Path(__file__).resolve().parents[1]
FROZEN_PROJECT_ROOT = HERE / "tests" / "fixtures" / "frozen_project"
FROZEN_BINDINGS = FROZEN_PROJECT_ROOT / "source_bindings.json"


def load_actions():
    spec = importlib.util.spec_from_file_location("implementation_actions", HERE / "implementation_actions.py")
    actions = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(actions)
    actions.ROOT = FROZEN_PROJECT_ROOT

    def frozen_rows():
        return json.loads(FROZEN_BINDINGS.read_text(encoding="utf-8"))["sources"]

    actions._reviewed_binding_rows = frozen_rows
    return actions
