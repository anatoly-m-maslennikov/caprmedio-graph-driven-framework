"""Pure image version, Docker timestamp and display-tag helpers."""

from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path
import re
import tomllib


IMAGE_REPOSITORY = "caprmedio-runtime"
OCI_VERSION_LABEL = "org.opencontainers.image.version"
_IMAGE_ID = re.compile(r"sha256:[0-9a-f]{64}")
_SAFE_VERSION = re.compile(r"[A-Za-z0-9][A-Za-z0-9_.-]{0,127}")


def read_framework_version(path: Path | str) -> str:
    """Read the exact tag-safe framework version from one admitted TOML file."""
    try:
        document = tomllib.loads(Path(path).read_text(encoding="utf-8"))
    except (OSError, TypeError, UnicodeError, ValueError) as error:
        raise ValueError("framework version input is unreadable or invalid") from error
    framework = document.get("framework")
    version = framework.get("version") if isinstance(framework, dict) else None
    if type(version) is not str or _SAFE_VERSION.fullmatch(version) is None:
        raise ValueError("framework version is not one exact Docker-safe value")
    return version


def docker_created_utc(value: object) -> str:
    """Render Docker's timezone-aware Created value as UTC tag text."""
    if not isinstance(value, str):
        raise ValueError("Docker image Created metadata is unavailable")
    source = value[:-1] + "+00:00" if value.endswith("Z") else value
    try:
        parsed = datetime.fromisoformat(source)
    except ValueError as error:
        raise ValueError("Docker image Created metadata is invalid") from error
    if parsed.tzinfo is None:
        raise ValueError("Docker image Created metadata has no timezone")
    return parsed.astimezone(timezone.utc).strftime("%Y%m%dT%H%M%SZ")


def display_image_tag(version: str, created: object, image_id: str) -> str:
    """Build the additive repository tag from verified image metadata."""
    if (
        not isinstance(version, str)
        or not isinstance(image_id, str)
        or _SAFE_VERSION.fullmatch(version) is None
        or _IMAGE_ID.fullmatch(image_id) is None
    ):
        raise ValueError("display-tag inputs are not exact safe image values")
    component = f"{version}-{docker_created_utc(created)}-{image_id[7:19]}"
    if len(component) > 128:
        raise ValueError("display tag exceeds Docker's tag length limit")
    return f"{IMAGE_REPOSITORY}:{component}"
