"""Read the current release places from the one Project Structure carrier."""
from __future__ import annotations

from dataclasses import dataclass
import hashlib
from pathlib import Path
import sys
import tomllib

_TOOLS = Path(__file__).resolve().parents[1]
if str(_TOOLS) not in sys.path:
    sys.path.insert(0, str(_TOOLS))

from COMPILE_APPLICABLE_METHODOLOGY.compile_applicable_methodology import configured_control_root


@dataclass(frozen=True)
class MethodologyLayout:
    source_root: str
    product_root: str
    source_copy_root: str
    applicable_root: str
    control_root: str
    installed_root: str
    structure_sha256: str


def _relative(root: Path, value: object) -> str:
    if not isinstance(value, str) or not value:
        raise ValueError("Methodology place must be a non-empty relative path")
    path = Path(value)
    if path.is_absolute() or ".." in path.parts or path == Path("."):
        raise ValueError("Methodology place must stay within the Project")
    current = root
    for part in path.parts:
        current /= part
        if current.is_symlink():
            raise ValueError("Methodology place must not traverse a symlink")
    current.resolve().relative_to(root)
    return path.as_posix()


def resolve_methodology_layout(project_root: Path | str) -> MethodologyLayout:
    root = Path(project_root).resolve(strict=True)
    control = configured_control_root(root)
    registry = root / control / "project_structure.toml"
    if registry.is_symlink():
        raise ValueError("Project Structure must be a regular authoritative carrier")
    payload = registry.read_bytes()
    rows = tomllib.loads(payload.decode("utf-8")).get("scope_units", [])

    def unit(name: str) -> dict:
        matches = [row for row in rows if isinstance(row, dict) and row.get("scope_unit_name") == name]
        if len(matches) != 1:
            raise ValueError(f"Project Structure must register exactly one {name}")
        return matches[0]

    framework = unit("FRAMEWORK_METHODOLOGY")
    sources = unit("METHODOLOGY_SOURCES")
    applicable = unit("APPLICABLE_METHODOLOGY")
    if sources.get("parent") != "FRAMEWORK_METHODOLOGY" or applicable.get("parent") != "FRAMEWORK_METHODOLOGY":
        raise ValueError("Methodology source and applicable places must belong to FRAMEWORK_METHODOLOGY")
    source = _relative(root, sources.get("authority_path"))
    product = _relative(root, framework.get("delivery_path"))
    copied = _relative(root, sources.get("delivery_path"))
    compiled = _relative(root, applicable.get("delivery_path"))
    installed = _relative(root, (control / "000_CAPRMEDIO_framework").as_posix())
    if not Path(source).is_relative_to(control) or Path(source).is_relative_to(Path(installed)):
        raise ValueError("Release sources must be Project authority, not installed Methodology")
    if Path(copied).parent != Path(product) or Path(compiled).parent != Path(product):
        raise ValueError("Methodology source and applicable deliveries must be product children")
    if Path(product).is_relative_to(control) or Path(source).is_relative_to(Path(product)):
        raise ValueError("Methodology product must not enclose Project authority")
    return MethodologyLayout(source, product, copied, compiled, control.as_posix(), installed,
                             hashlib.sha256(payload).hexdigest())
