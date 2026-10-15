"""Retire only inspected obsolete resources belonging to the selected Project."""

from dataclasses import dataclass, field
from pathlib import Path
import re
import subprocess

from release_cleanup_identity import (
    IMAGE,
    IDENTIFIER,
    FINGERPRINT,
    SCHEMA,
    Container,
    Runner,
    image_fingerprint,
    image_has_current_code,
    run_docker,
)


@dataclass
class Cleanup:
    images: set[str] = field(default_factory=set)
    attempted: set[str] = field(default_factory=set)
    notes: list[str] = field(default_factory=list)
    pending: bool = False


def _identifiers(output: str, pattern: re.Pattern[str]) -> set[str]:
    identifiers = set(output.splitlines())
    if any(pattern.fullmatch(value) is None for value in identifiers):
        raise ValueError("Docker cleanup identifiers are invalid")
    return identifiers


def _owned(row: Container, root: Path, project_id: str, control: str) -> bool:
    labels = row.Config.Labels
    return all(
        labels.get(key) == value
        for key, value in {
            "org.caprmedio.project": project_id,
            "org.caprmedio.service": "mcp-http",
            "org.caprmedio.control_root": control,
            "org.caprmedio.host_project_root": str(root),
        }.items()
    )


def _remove_container(
    root: Path,
    runner: Runner | None,
    identifier: str,
    project_id: str,
    control: str,
    current_image: str,
    fingerprint: str,
    cleanup: Cleanup,
) -> None:
    projection = (
        '{"Image":{{json .Image}},"State":{"Running":{{json .State.Running}},'
        '"Status":{{json .State.Status}}},"Config":{"Labels":{{json .Config.Labels}}}}'
    )
    row = Container.model_validate_json(
        run_docker(root, runner, "container", "inspect", "--format", projection, identifier)
    )
    if not _owned(row, root, project_id, control):
        cleanup.notes.append(f"Container {identifier} retained: Project ownership unproven.")
        cleanup.pending = True
        return
    if (
        row.Image == current_image
        or row.Config.Labels.get(FINGERPRINT) == fingerprint
        or row.State.Running
        or row.State.Status not in {"exited", "dead"}
    ):
        cleanup.notes.append(
            f"Container {identifier} retained: current, running or not proven stopped."
        )
        return
    if IMAGE.fullmatch(row.Image) is None:
        raise ValueError("Container image identity is invalid")
    if image_has_current_code(root, row.Image, current_image, fingerprint, runner):
        cleanup.notes.append(
            f"Container {identifier} retained: image has current code fingerprint."
        )
        return
    cleanup.images.add(row.Image)
    cleanup.attempted.add(identifier)
    run_docker(root, runner, "container", "rm", identifier)
    cleanup.notes.append(f"Removed obsolete stopped Project container {identifier}.")


def cleanup_stopped_containers(
    root: Path,
    project_id: str,
    control: str,
    current_image: str,
    fingerprint: str,
    runner: Runner | None = None,
    *,
    cleanup: Cleanup | None = None,
) -> Cleanup:
    if cleanup is None:
        cleanup = Cleanup()
    try:
        identifiers = _identifiers(
            run_docker(
                root,
                runner,
                "container",
                "ls",
                "--all",
                "--no-trunc",
                "--filter",
                f"label=org.caprmedio.project={project_id}",
                "--quiet",
            ),
            IDENTIFIER,
        )
    except OSError, RuntimeError, ValueError, subprocess.TimeoutExpired:
        cleanup.pending = True
        cleanup.notes.append("Stopped-container discovery unavailable; resources retained.")
        return cleanup
    for identifier in sorted(identifiers):
        if identifier in cleanup.attempted:
            continue
        try:
            _remove_container(
                root, runner, identifier, project_id, control, current_image, fingerprint, cleanup
            )
        except OSError, RuntimeError, ValueError, subprocess.TimeoutExpired:
            cleanup.pending = True
            cleanup.notes.append(f"Container {identifier} retained: inspection or removal failed.")
    return cleanup


def _remove_image(
    root: Path,
    runner: Runner | None,
    image: str,
    fingerprint: str,
    cleanup: Cleanup,
) -> None:
    if image_fingerprint(root, runner, image) == fingerprint:
        cleanup.notes.append(f"Image {image} retained: current code fingerprint.")
        return
    references = run_docker(
        root, runner, "container", "ls", "--all", "--filter", f"ancestor={image}", "--quiet"
    )
    if references.strip():
        cleanup.notes.append(f"Image {image} retained: a container still uses it.")
        cleanup.pending = True
        return
    run_docker(root, runner, "image", "rm", image)
    cleanup.notes.append(f"Removed obsolete Project-linked image {image}.")


def cleanup_obsolete_images(
    root: Path,
    current_image: str,
    fingerprint: str,
    cleanup: Cleanup,
    runner: Runner | None = None,
) -> None:
    try:
        observed = _identifiers(
            run_docker(
                root,
                runner,
                "image",
                "ls",
                "--no-trunc",
                "--quiet",
                "--filter",
                f"label={SCHEMA}=1",
            ),
            IMAGE,
        )
        unproven = observed - cleanup.images - {current_image}
        if unproven:
            cleanup.pending = True
            cleanup.notes.append(
                "Retained runtime images without Project ownership evidence: "
                + ", ".join(sorted(unproven))
            )
    except OSError, RuntimeError, ValueError, subprocess.TimeoutExpired:
        cleanup.pending = True
        cleanup.notes.append("Runtime image discovery unavailable; unproven images retained.")
    for image in sorted(cleanup.images - {current_image}):
        try:
            _remove_image(root, runner, image, fingerprint, cleanup)
        except OSError, RuntimeError, ValueError, subprocess.TimeoutExpired:
            cleanup.pending = True
            cleanup.notes.append(f"Image {image} retained: inspection or removal failed.")
