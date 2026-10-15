"""Discover owned orphan images and remove only verified unused obsolete code."""

from pathlib import Path
import re
import subprocess

from release_cleanup_identity import (
    Cleanup,
    FINGERPRINT,
    IMAGE,
    SCHEMA,
    Runner,
    image_labels,
    run_docker,
)


def _has_owner(labels: dict[str, str], owner: dict[str, str]) -> bool:
    return bool(owner) and all(labels.get(key) == value for key, value in owner.items())


def _declares_owner(labels: dict[str, str]) -> bool:
    return any(
        key in labels
        for key in (
            "org.caprmedio.project",
            "org.caprmedio.control_root",
            "org.caprmedio.host_project_root",
        )
    )


def _foreign_owner(labels: dict[str, str], owner: dict[str, str]) -> bool:
    project_id = labels.get("org.caprmedio.project", "")
    root = labels.get("org.caprmedio.host_project_root", "")
    control = labels.get("org.caprmedio.control_root", "")
    return (
        bool(owner)
        and project_id != owner.get("org.caprmedio.project")
        and re.fullmatch(r"[0-9a-f]{64}", project_id) is not None
        and Path(root).is_absolute()
        and ".." not in Path(root).parts
        and control.startswith(".caprmedio_")
        and len(Path(control).parts) == 1
    )


def _remove_image(
    root: Path,
    runner: Runner | None,
    image: str,
    fingerprint: str,
    cleanup: Cleanup,
) -> None:
    labels = image_labels(root, runner, image)
    if labels[FINGERPRINT] == fingerprint:
        cleanup.notes.append(f"Image {image} retained: current code fingerprint.")
        return
    if _declares_owner(labels) and not _has_owner(labels, cleanup.owner):
        cleanup.pending |= not _foreign_owner(labels, cleanup.owner)
        cleanup.notes.append(
            f"Image {image} retained: declared ownership does not match the Project."
        )
        return
    references = run_docker(
        root, runner, "container", "ls", "--all", "--filter", f"ancestor={image}", "--quiet"
    )
    if references.strip():
        cleanup.notes.append(f"Image {image} retained: a container still uses it.")
        cleanup.pending = True
        return
    run_docker(root, runner, "image", "rm", image)
    cleanup.notes.append(f"Removed obsolete Project-owned or Project-linked image {image}.")


def _discover_images(
    root: Path, runner: Runner | None, current_image: str, cleanup: Cleanup
) -> None:
    observed = set(
        run_docker(
            root, runner, "image", "ls", "--no-trunc", "--quiet", "--filter", f"label={SCHEMA}=1"
        ).splitlines()
    )
    if any(IMAGE.fullmatch(image) is None for image in observed):
        raise ValueError("Docker cleanup identifiers are invalid")
    for image in sorted(observed - cleanup.images - {current_image}):
        try:
            labels = image_labels(root, runner, image)
            if _has_owner(labels, cleanup.owner):
                cleanup.images.add(image)
            elif _declares_owner(labels):
                cleanup.pending |= not _foreign_owner(labels, cleanup.owner)
                cleanup.notes.append(
                    f"Image {image} retained: foreign or incomplete declared ownership."
                )
            else:
                cleanup.pending = True
                cleanup.notes.append(f"Image {image} retained without Project ownership evidence.")
        except OSError, RuntimeError, ValueError, subprocess.TimeoutExpired:
            cleanup.pending = True
            cleanup.notes.append(f"Image {image} retained: ownership inspection failed.")


def cleanup_obsolete_images(
    root: Path,
    current_image: str,
    fingerprint: str,
    cleanup: Cleanup,
    runner: Runner | None = None,
) -> None:
    try:
        _discover_images(root, runner, current_image, cleanup)
    except OSError, RuntimeError, ValueError, subprocess.TimeoutExpired:
        cleanup.pending = True
        cleanup.notes.append("Runtime image discovery unavailable; unproven images retained.")
    for image in sorted(cleanup.images - {current_image}):
        try:
            _remove_image(root, runner, image, fingerprint, cleanup)
        except OSError, RuntimeError, ValueError, subprocess.TimeoutExpired:
            cleanup.pending = True
            cleanup.notes.append(f"Image {image} retained: inspection or removal failed.")
