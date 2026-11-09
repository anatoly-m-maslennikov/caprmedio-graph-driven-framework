"""Finding state for retained declaration Graph Rule checks."""

from __future__ import annotations

from .authority import AuthorityContext, Obligation, Record


class Check:
    def __init__(
        self, obligation: Obligation, context: AuthorityContext, inputs: Record | None = None
    ) -> None:
        self.obligation = obligation
        self.context = context
        self.inputs: Record = inputs or {}
        self.findings: list[Record] = []
        self.gaps: list[Record] = []

    def _record(self, records: list[Record], code: str, field: str, reason: str) -> None:
        records.append(
            {"code": code, "severity": "error", "path": None, "span": None,
             "property": field, "authority": self.obligation.authority,
             "reason": reason, "evidence": None}
        )

    def fail(self, code: str, field: str, reason: str) -> None:
        self._record(self.findings, code, field, reason)

    def gap(self, field: str, reason: str) -> None:
        self._record(self.gaps, "AUTHORITY_UNSUPPORTED", field, reason)
