"""Resolve one target's explicit Methodology selection from admitted bytes.

This module is deliberately a read-only boundary between package availability
and target applicability.  A package catalog can contain many admitted
Methodology roots; only the canonical Framework Instance Settings carrier for
one target selects the roots that its compiler may receive.
"""

from __future__ import annotations

from dataclasses import dataclass
import hashlib
import os
from pathlib import Path, PurePosixPath
import stat
import tomllib
from typing import Mapping


FRAMEWORK_INSTANCE_SETTINGS_RELATIVE = PurePosixPath(
    "000_CAPRMEDIO_framework/caprmedio_framework_settings.toml"
)
_ACTIVE_ROOT = PurePosixPath("methodology/active")
_BASE_ROOT = _ACTIVE_ROOT / "001_CORE_META_MODEL"
_EXTENSIONS_ROOT = _ACTIVE_ROOT / "002_INSTALLED_EXTENSIONS"
_CONFIGURATION_ROOT = _ACTIVE_ROOT / "003_PROJECT_CONFIGURATION"
_SUPPORT_ROOT = PurePosixPath("methodology/support")


class TargetMethodologySelectionError(ValueError):
    """Stable refusal while binding target applicability."""

    def __init__(self, code: str, message: str) -> None:
        self.code = code
        super().__init__(f"{code}: {message}")


@dataclass(frozen=True)
class TargetMethodologySelection:
    """The immutable selection to retain in a D600v3 target context."""

    framework_instance_settings_sha256: str
    source_catalog_sha256: str
    methodology_source_identities: tuple[str, ...]


def _refuse(code: str, message: str) -> None:
    raise TargetMethodologySelectionError(code, message)


def _sha256(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def _regular_toml(control: Path) -> tuple[bytes, dict[str, object]]:
    """Read the sole D359 carrier without crossing an alias."""

    cursor = control
    try:
        for index, part in enumerate(FRAMEWORK_INSTANCE_SETTINGS_RELATIVE.parts):
            cursor = cursor / part
            observed = os.lstat(cursor)
            expected = stat.S_ISREG if index == len(FRAMEWORK_INSTANCE_SETTINGS_RELATIVE.parts) - 1 else stat.S_ISDIR
            if stat.S_ISLNK(observed.st_mode) or not expected(observed.st_mode):
                _refuse("target-selection-settings-invalid", "Framework Instance Settings carrier is aliased or invalid")
        before = (observed.st_dev, observed.st_ino, observed.st_size, observed.st_mtime_ns)
        payload = cursor.read_bytes()
        after = cursor.stat()
        if before != (after.st_dev, after.st_ino, after.st_size, after.st_mtime_ns):
            _refuse("target-selection-settings-drift", "Framework Instance Settings changed while being reopened")
        document = tomllib.loads(payload.decode("utf-8"))
        if not isinstance(document, dict):
            _refuse("target-selection-settings-invalid", "Framework Instance Settings must be a TOML table")
        return payload, document
    except TargetMethodologySelectionError:
        raise
    except (OSError, UnicodeDecodeError, tomllib.TOMLDecodeError, ValueError) as error:
        raise TargetMethodologySelectionError(
            "target-selection-settings-invalid", "Framework Instance Settings carrier is unavailable or invalid"
        ) from error


def _safe_package_root(value: Path | str) -> Path:
    try:
        raw = Path(value)
        if not raw.is_absolute() or ".." in raw.parts:
            _refuse("target-selection-package-invalid", "package root must be an absolute normalized path")
        root = Path(os.path.abspath(raw))
        if root.resolve(strict=True) != root:
            _refuse("target-selection-package-invalid", "package root must not resolve through an alias")
        observed = root.stat()
        if not stat.S_ISDIR(observed.st_mode):
            _refuse("target-selection-package-invalid", "package root must be a directory")
        return root
    except TargetMethodologySelectionError:
        raise
    except (OSError, RuntimeError, TypeError, ValueError) as error:
        raise TargetMethodologySelectionError("target-selection-package-invalid", "package root is unavailable") from error


def _path(value: object, *, identity: str) -> PurePosixPath:
    if not isinstance(value, str) or not value or "\\" in value:
        _refuse("target-selection-catalog-invalid", f"catalog source path is invalid: {identity}")
    path = PurePosixPath(value)
    if path.is_absolute() or path == PurePosixPath(".") or any(part in {"", ".", ".."} for part in path.parts):
        _refuse("target-selection-catalog-invalid", f"catalog source path is unsafe: {identity}")
    return path


def _ensure_disjoint_active_roots(pins: tuple[object, ...]) -> None:
    active: list[tuple[str, PurePosixPath]] = []
    for pin in pins:
        path = _path(getattr(pin, "path", None), identity=str(getattr(pin, "identity", "")))
        if path == _ACTIVE_ROOT or path.is_relative_to(_ACTIVE_ROOT):
            active.append((str(getattr(pin, "identity", "")), path))
    for index, (identity, path) in enumerate(active):
        for other_identity, other in active[index + 1 :]:
            if path == other or path.is_relative_to(other) or other.is_relative_to(path):
                _refuse(
                    "target-selection-catalog-overlap",
                    f"catalog active roots overlap: {identity} and {other_identity}",
                )


def _one(
    pins: tuple[object, ...],
    *,
    label: str,
    predicate: object,
) -> object:
    matches = tuple(pin for pin in pins if predicate(pin))
    if len(matches) != 1:
        _refuse("target-selection-source-missing", f"{label} must match exactly one admitted catalog source")
    return matches[0]


def _extension_roots(pins: tuple[object, ...], identity: str, revision: str) -> object:
    def match(pin: object) -> bool:
        if getattr(pin, "kind", None) != "extension":
            return False
        path = _path(getattr(pin, "path", None), identity=str(getattr(pin, "identity", "")))
        suffix = path.relative_to(_EXTENSIONS_ROOT) if path.is_relative_to(_EXTENSIONS_ROOT) else None
        return suffix is not None and len(suffix.parts) == 2 and suffix.parts == (identity, revision)

    return _one(pins, label=f"selected Extension {identity}@{revision}", predicate=match)


def _configuration_selection(settings: Mapping[str, object]) -> tuple[str, str] | None:
    methodology = settings.get("methodology")
    if methodology is None:
        return None
    if not isinstance(methodology, Mapping):
        _refuse("target-selection-configuration-invalid", "methodology settings must be a table")
    configuration = methodology.get("configuration")
    if configuration is None:
        return None
    if not isinstance(configuration, Mapping) or set(configuration) != {"identity", "revision"}:
        _refuse("target-selection-configuration-invalid", "methodology.configuration must contain exactly identity and revision")
    identity = configuration.get("identity")
    revision = configuration.get("revision")
    if not isinstance(identity, str) or not identity or not isinstance(revision, str) or not revision:
        _refuse("target-selection-configuration-invalid", "methodology.configuration identity and revision must be strings")
    return identity, revision


def _reopen_evidence(package_root: Path, expected: object) -> object:
    """Reopen complete physical pins; the caller cannot assert a selection."""

    try:
        from framework_package import FrameworkPackageError, provide_installation_package_evidence
        from installation_context import VerifiedPackageEvidence
    except ImportError as error:  # pragma: no cover - isolated package composition guard.
        raise TargetMethodologySelectionError(
            "target-selection-provider-unavailable", "package evidence provider is unavailable"
        ) from error
    if not isinstance(expected, VerifiedPackageEvidence):
        _refuse("target-selection-evidence-invalid", "expected package evidence must be typed")
    try:
        reopened = provide_installation_package_evidence(package_root)
    except FrameworkPackageError as error:
        raise TargetMethodologySelectionError(
            "target-selection-evidence-invalid", "package evidence could not be reopened"
        ) from error
    if not isinstance(reopened, VerifiedPackageEvidence) or reopened != expected:
        _refuse("target-selection-evidence-drift", "expected package evidence differs from the complete physical package")
    return reopened


def resolve_target_methodology_selection(
    *,
    control_root: Path | str,
    package_root: Path | str,
    package_evidence: object,
) -> TargetMethodologySelection:
    """Resolve exact selected identities from actual target settings and package.

    ``package_evidence`` is only an expected physical package identity.  The
    provider is reopened here so package availability, every pin and its
    receipts are revalidated before this resolver turns target settings into a
    compiler selection.
    """

    try:
        control = Path(control_root)
        if not control.is_absolute() or ".." in control.parts:
            _refuse("target-selection-control-invalid", "control root must be absolute and normalized")
        control = Path(os.path.abspath(control))
        observed = control.lstat()
        if stat.S_ISLNK(observed.st_mode) or not stat.S_ISDIR(observed.st_mode) or control.resolve(strict=True) != control:
            _refuse("target-selection-control-invalid", "control root is aliased or invalid")
    except TargetMethodologySelectionError:
        raise
    except (OSError, RuntimeError, TypeError, ValueError) as error:
        raise TargetMethodologySelectionError("target-selection-control-invalid", "control root is unavailable") from error

    package = _safe_package_root(package_root)
    settings_bytes, settings = _regular_toml(control)
    evidence = _reopen_evidence(package, package_evidence)
    pins = tuple(evidence.source_pins)
    if not pins or any(not isinstance(getattr(pin, "identity", None), str) or not getattr(pin, "identity") for pin in pins):
        _refuse("target-selection-catalog-invalid", "package evidence has no exact catalog source identities")
    if len({pin.identity for pin in pins}) != len(pins):
        _refuse("target-selection-catalog-invalid", "package evidence has duplicate catalog source identities")
    _ensure_disjoint_active_roots(pins)

    base = _one(
        pins,
        label="Core Methodology",
        predicate=lambda pin: getattr(pin, "kind", None) == "methodology"
        and _path(getattr(pin, "path", None), identity=str(getattr(pin, "identity", ""))) == _BASE_ROOT,
    )
    support = tuple(
        pin
        for pin in pins
        if getattr(pin, "kind", None) == "support"
        and (
            _path(getattr(pin, "path", None), identity=str(getattr(pin, "identity", ""))) == _SUPPORT_ROOT
            or _path(getattr(pin, "path", None), identity=str(getattr(pin, "identity", ""))).is_relative_to(_SUPPORT_ROOT)
        )
    )
    if not support:
        _refuse("target-selection-source-missing", "declared Methodology support is required")
    if any(
        getattr(pin, "kind", None) == "support"
        and not (
            _path(getattr(pin, "path", None), identity=str(getattr(pin, "identity", ""))) == _SUPPORT_ROOT
            or _path(getattr(pin, "path", None), identity=str(getattr(pin, "identity", ""))).is_relative_to(_SUPPORT_ROOT)
        )
        for pin in pins
    ):
        _refuse("target-selection-catalog-invalid", "support source must be under methodology/support")

    try:
        from COMPILE_APPLICABLE_METHODOLOGY.compile_applicable_methodology import CompileError, extension_selections

        enabled = extension_selections(settings)
    except ImportError as error:  # pragma: no cover - installed composition guard.
        raise TargetMethodologySelectionError(
            "target-selection-parser-unavailable", "canonical Extension selection parser is unavailable"
        ) from error
    except CompileError as error:
        raise TargetMethodologySelectionError(error.code, error.message) from error

    selected = {base.identity, *(pin.identity for pin in support)}
    for identity, revision in enabled.items():
        selected.add(_extension_roots(pins, identity, revision).identity)
    configuration = _configuration_selection(settings)
    if configuration is not None:
        identity, revision = configuration
        selected.add(
            _one(
                pins,
                label=f"selected Configuration {identity}@{revision}",
                predicate=lambda pin: getattr(pin, "kind", None) == "configuration"
                and _path(getattr(pin, "path", None), identity=str(getattr(pin, "identity", ""))) == _CONFIGURATION_ROOT
                and getattr(pin, "identity", None) == identity
                and getattr(pin, "revision", None) == revision,
            ).identity
        )

    # Re-read the exact carrier after package reopening.  A mutation at either
    # point invalidates the target selection instead of binding a mixed view.
    reread, _ = _regular_toml(control)
    if reread != settings_bytes:
        _refuse("target-selection-settings-drift", "Framework Instance Settings changed during selection")
    return TargetMethodologySelection(
        framework_instance_settings_sha256=_sha256(settings_bytes),
        source_catalog_sha256=evidence.catalog_sha256,
        methodology_source_identities=tuple(sorted(selected)),
    )


__all__ = [
    "FRAMEWORK_INSTANCE_SETTINGS_RELATIVE",
    "TargetMethodologySelection",
    "TargetMethodologySelectionError",
    "resolve_target_methodology_selection",
]
