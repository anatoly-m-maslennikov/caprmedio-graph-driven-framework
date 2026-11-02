"""Strict Docker observations and immutable runtime-image identity checks."""

from collections.abc import Callable
from dataclasses import dataclass, field
from pathlib import Path
import re
import subprocess

from pydantic import BaseModel, ConfigDict

Runner = Callable[[tuple[str, ...], Path], subprocess.CompletedProcess[str]]
IMAGE = re.compile(r"sha256:[0-9a-f]{64}")
IDENTIFIER = re.compile(r"[0-9a-f]{64}")
FINGERPRINT = "org.caprmedio.runtime.fingerprint"
SCHEMA = "org.caprmedio.runtime.schema"


@dataclass
class Cleanup:
    images: set[str] = field(default_factory=set)
    attempted: set[str] = field(default_factory=set)
    notes: list[str] = field(default_factory=list)
    pending: bool = False
    owner: dict[str, str] = field(default_factory=dict)


def owner_labels(root: Path, project_id: str, control: str) -> dict[str, str]:
    return {
        "org.caprmedio.project": project_id,
        "org.caprmedio.control_root": control,
        "org.caprmedio.host_project_root": str(root),
    }


class Configuration(BaseModel):
    model_config = ConfigDict(strict=True, extra="forbid")
    Labels: dict[str, str]


class ContainerState(BaseModel):
    model_config = ConfigDict(strict=True, extra="forbid")
    Running: bool
    Status: str


class Container(BaseModel):
    model_config = ConfigDict(strict=True, extra="forbid")
    Image: str
    State: ContainerState
    Config: Configuration


class ImageMetadata(BaseModel):
    model_config = ConfigDict(strict=True, extra="forbid")
    Id: str
    Config: Configuration


def run_docker(root: Path, runner: Runner | None, *arguments: str) -> str:
    argv = ("docker", *arguments)
    result = (
        runner(argv, root)
        if runner is not None
        else subprocess.run(
            argv,
            cwd=root,
            capture_output=True,
            text=True,
            timeout=30,
            check=False,
        )
    )
    if result.returncode != 0 or len(result.stdout) > 1_048_576:
        raise RuntimeError("Docker cleanup observation or removal failed")
    return result.stdout


def image_labels(root: Path, runner: Runner | None, image: str) -> dict[str, str]:
    if not isinstance(image, str) or IMAGE.fullmatch(image) is None:
        raise ValueError("Image identity is invalid")
    projection = '{"Id":{{json .Id}},"Config":{"Labels":{{json .Config.Labels}}}}'
    row = ImageMetadata.model_validate_json(
        run_docker(root, runner, "image", "inspect", "--format", projection, image)
    )
    labels = row.Config.Labels
    if (
        row.Id != image
        or labels.get(SCHEMA) != "1"
        or re.fullmatch(r"[0-9a-f]{64}", labels.get(FINGERPRINT, "")) is None
    ):
        raise ValueError("Image runtime ownership unproven")
    return labels
