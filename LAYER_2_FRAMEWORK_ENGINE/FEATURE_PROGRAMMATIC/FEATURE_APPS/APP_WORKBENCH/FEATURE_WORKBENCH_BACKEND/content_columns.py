# CA-R-2726@9
# CA-M-500@3
# CA-D-672@22

"""Expose compiled Markdown Content properties as SQL row values."""

from __future__ import annotations

from collections.abc import Mapping
from typing import Any

from .content_schema import ContentSchema


def content_columns(row: Mapping[str, Any], schema: ContentSchema) -> dict[str, str | None]:
    """Return the declared Content values for one parsed source Atom."""
    return schema.values(row)
