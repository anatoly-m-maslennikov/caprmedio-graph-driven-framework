"""An explicit scheduler namespace; native state is never silently imported."""

import os
import re


_ISOLATED_NAMESPACE = re.compile(r"isolated:([a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?)")


def _runtime_namespace():
    """Return the one explicit scheduler namespace selected for this process."""
    value = os.environ.get("CAPRMEDIO_RUNTIME_NAMESPACE", "")
    if value in ("", "docker") or _ISOLATED_NAMESPACE.fullmatch(value):
        return value
    raise ValueError("Unsupported runtime namespace")


def docker_runtime():
    return _runtime_namespace() == "docker"


def isolated_runtime():
    """Whether this process uses a private, native scheduler namespace."""
    return _runtime_namespace().startswith("isolated:")


def implementation_mock_runtime():
    """Only the explicit Docker mock startup selects the fixed mock callback."""
    _runtime_namespace()
    mode = os.environ.get("CAPRMEDIO_AGENT_MODE", "")
    if mode not in ("", "codex", "mock"):
        raise ValueError("Unsupported Agent runtime mode")
    if mode == "mock" and not docker_runtime():
        raise ValueError("Implementation mock requires explicit Docker startup")
    return mode == "mock"


def control_directory():
    base = ".caprmedio_install/workflow_orchestrator"
    namespace = _runtime_namespace()
    if namespace == "docker":
        return base + "/docker"
    if namespace.startswith("isolated:"):
        return base + "/isolated/" + namespace.removeprefix("isolated:")
    return base
