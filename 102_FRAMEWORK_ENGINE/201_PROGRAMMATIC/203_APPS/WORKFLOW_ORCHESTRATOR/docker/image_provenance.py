"""Explicit build provenance, separate from source and immutable image identity."""

from dataclasses import dataclass
from pathlib import PurePosixPath
import re


@dataclass(frozen=True)
class ImageBuildProvenance:
    project_id: str
    project_root: str
    control_root: str
    project_name: str
    head_commit: str

    def __post_init__(self) -> None:
        if (
            not all(
                isinstance(value, str) and value and "\x00" not in value
                for value in (
                    self.project_id,
                    self.project_root,
                    self.control_root,
                    self.project_name,
                    self.head_commit,
                )
            )
            or re.fullmatch(r"[0-9a-f]{64}", self.project_id) is None
            or re.fullmatch(r"(?:[0-9a-f]{40}|[0-9a-f]{64})", self.head_commit) is None
            or not self.project_name.strip()
            or not PurePosixPath(self.project_root).is_absolute()
            or ".." in PurePosixPath(self.project_root).parts
            or len(PurePosixPath(self.control_root).parts) != 1
            or not self.control_root.startswith(".caprmedio_")
        ):
            raise ValueError("Image build provenance is invalid")

    def labels(self) -> dict[str, str]:
        return {
            "org.caprmedio.project": self.project_id,
            "org.caprmedio.host_project_root": self.project_root,
            "org.caprmedio.control_root": self.control_root,
            "org.caprmedio.project.name": self.project_name,
            "org.caprmedio.source.head_commit": self.head_commit,
        }


def label_arguments(provenance: ImageBuildProvenance | None) -> tuple[str, ...]:
    return tuple(
        argument
        for key, value in (provenance.labels().items() if provenance else ())
        for argument in ("--label", f"{key}={value}")
    )
