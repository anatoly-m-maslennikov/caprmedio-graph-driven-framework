"""Reusable request-shape helpers for selected routes."""

from __future__ import annotations

from typing import Any, Mapping

from selected_route_spec import _DIGEST, SelectedRouteError


def find_shadow_manifest_fields(
    value: Any, *, allowed_definition_manifest: bool = False, _path: tuple[str | int, ...] = ()
) -> bool:
    if isinstance(value, Mapping):
        for key, child in value.items():
            if key in {"definition_manifest_ref", "definition_manifest_digest"} or (
                key == "definition_manifest"
                and not (
                    allowed_definition_manifest
                    and _path in {(), ("operator_authorization",), ("proposal_receipt",)}
                )
            ):
                return True
            if find_shadow_manifest_fields(
                child, allowed_definition_manifest=allowed_definition_manifest, _path=(*_path, key)
            ):
                return True
    elif isinstance(value, list):
        return any(
            find_shadow_manifest_fields(
                item, allowed_definition_manifest=allowed_definition_manifest, _path=(*_path, index)
            )
            for index, item in enumerate(value)
        )
    return False


def require_digest(value: Any, message: str) -> str:
    if not isinstance(value, str) or not _DIGEST.fullmatch(value):
        raise SelectedRouteError(message)
    return value
