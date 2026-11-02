"""Project-bound transport for the plain native Journal appender."""

from __future__ import annotations

from pathlib import Path
from types import ModuleType
from typing import TYPE_CHECKING, Any, Mapping

if TYPE_CHECKING:
    from append_change_records import AppendChangeRecordsRequest


class AppendChangeRecordsAdapter:
    def __init__(self, root: Path, native: ModuleType) -> None:
        self.root = root
        self.native = native

    def invoke(self, request: AppendChangeRecordsRequest | Mapping[str, Any]) -> dict[str, Any]:
        if not isinstance(request, self.native.AppendChangeRecordsRequest):
            request = self.native.AppendChangeRecordsRequest.model_validate(request)
        return self.native.run(
            self.root, {"context": request.root.context}, apply=request.root.apply
        )
