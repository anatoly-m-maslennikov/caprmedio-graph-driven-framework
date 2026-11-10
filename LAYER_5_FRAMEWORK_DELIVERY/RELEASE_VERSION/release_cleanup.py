"""Retire only inspected obsolete resources belonging to the selected Project."""

from pathlib import Path
import re
import subprocess

from release_cleanup_identity import (
    IMAGE,
    IDENTIFIER,
    Container,
    Cleanup as Cleanup,
    Runner,
    image_labels,
    owner_labels,
    run_docker,
)
from release_cleanup_images import cleanup_obsolete_images as cleanup_obsolete_images


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
        or row.State.Running
        or row.State.Status not in {"exited", "dead"}
    ):
        cleanup.notes.append(
            f"Container {identifier} retained: current, running or not proven stopped."
        )
        return
    if IMAGE.fullmatch(row.Image) is None:
        raise ValueError("Container image identity is invalid")
    image_labels(root, runner, row.Image)
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
        cleanup = Cleanup(owner=owner_labels(root, project_id, control))
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
