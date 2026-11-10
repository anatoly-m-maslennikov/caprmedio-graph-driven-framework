"""Collision-safe display tagging for an already admitted immutable image."""

from __future__ import annotations

import json

try:
    from .image_metadata import display_image_tag
    from .image_reference import IMMUTABLE_IMAGE
except ImportError:  # direct execution/import with docker/ on sys.path
    from image_metadata import display_image_tag
    from image_reference import IMMUTABLE_IMAGE


def _unique_object(pairs):
    value = {}
    for key, item in pairs:
        if key in value:
            raise ValueError("duplicate image inspection member")
        value[key] = item
    return value


def _state(run, tag: str, refused):
    raw = run(("docker", "image", "inspect", tag), allow_failure=True)
    if raw is None:
        listed = run(("docker", "image", "ls", "--all", "--quiet", "--no-trunc", tag))
        if listed.strip():
            raise refused("Display tag inspection is unavailable")
        return None
    try:
        values = json.loads(raw, object_pairs_hook=_unique_object)
        if not isinstance(values, list) or len(values) != 1 or not isinstance(values[0], dict):
            raise ValueError("one display tag is required")
        value = values[0]
        image = value["Id"]
        repo_tags = value.get("RepoTags")
        if not isinstance(repo_tags, list) or any(not isinstance(item, str) for item in repo_tags):
            raise ValueError("display tag inventory is invalid")
        if tag not in repo_tags:
            raise refused("Display tag inventory is ambiguous")
        if IMMUTABLE_IMAGE.fullmatch(image) is None:
            raise ValueError("display tag identity is invalid")
        return image
    except (ValueError, TypeError, KeyError) as error:
        raise refused("Display tag inventory is invalid") from error


def ensure_display_tag(run, image: str, version: str, created: object, refused) -> str:
    """Add one display tag only when its Docker binding remains exact."""
    try:
        tag = display_image_tag(version, created, image)
    except ValueError as error:
        raise refused("Display tag metadata is invalid") from error
    existing = _state(run, tag, refused)
    if existing is not None:
        if existing != image:
            raise refused("Display tag is already bound to another image")
        return tag
    run(("docker", "image", "tag", image, tag), code="BUILD_FAILED")
    if _state(run, tag, refused) != image:
        raise refused("Docker did not retain the requested display tag")
    return tag
