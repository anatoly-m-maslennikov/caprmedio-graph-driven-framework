"""Disposable Docker test inputs, not Release admission or sealed evidence."""

from dataclasses import dataclass
from pathlib import Path
import re
from typing import Mapping

_IMMUTABLE_IMAGE = re.compile(r"sha256:[0-9a-f]{64}\Z")
_IMAGE = "CAPRMEDIO_FIRST_CUT_HTTP_IMAGE"
_SCRATCH = "CAPRMEDIO_FIRST_CUT_HTTP_SCRATCH"


@dataclass(frozen=True)
class CurrentCodeE2EContext:
    """Only the image and fixture directory supplied by the test runner."""

    scratch_root: Path
    candidate_image_digest: str


def narrow_context(environ: Mapping[str, str], repository_tmp: Path) -> CurrentCodeE2EContext:
    image, scratch_text = environ.get(_IMAGE), environ.get(_SCRATCH)
    if not image or not scratch_text:
        raise ValueError(f"{_IMAGE} and {_SCRATCH} are both required")
    if not _IMMUTABLE_IMAGE.fullmatch(image):
        raise ValueError(f"{_IMAGE} must be a lowercase sha256 immutable digest")
    scratch = Path(scratch_text)
    if (
        not scratch.is_absolute()
        or not scratch.is_dir()
        or any(path.is_symlink() for path in (scratch, *scratch.parents))
    ):
        raise ValueError(f"{_SCRATCH} must be an existing, non-symlink absolute directory")
    try:
        scratch_resolved = scratch.resolve(strict=True)
        repository_tmp = repository_tmp.resolve(strict=True)
        scratch_resolved.relative_to(repository_tmp)
    except (OSError, ValueError) as error:
        raise ValueError(f"{_SCRATCH} must be below repository .caprmedio_tmp") from error
    if scratch_resolved == repository_tmp:
        raise ValueError(f"{_SCRATCH} must be a child of repository .caprmedio_tmp")
    return CurrentCodeE2EContext(scratch_resolved, image)


def load_test_context(
    environ: Mapping[str, str], repository_tmp: Path
) -> CurrentCodeE2EContext | None:
    """Use only the actual image and private scratch supplied by the test runner."""
    enabled = any(
        environ.get(flag) == "1"
        for flag in (
            "CAPRMEDIO_DOCKER_E2E",
            "CAPRMEDIO_DOCKER_QUERY_E2E",
        )
    )
    if enabled or _IMAGE in environ or _SCRATCH in environ:
        return narrow_context(environ, repository_tmp)
    return None
