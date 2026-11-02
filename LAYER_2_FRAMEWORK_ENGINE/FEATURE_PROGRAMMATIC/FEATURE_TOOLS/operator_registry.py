"""Pure validation for the Project-root Operator registry."""

from __future__ import annotations

from dataclasses import dataclass
import tomllib
from typing import Any

from pydantic import BaseModel, ConfigDict, Field, ValidationError, field_validator, model_validator

from work_journal import AUTHOR_RE


class OperatorRegistryError(ValueError):
    """Stable failure for an invalid Operator registry payload."""

    def __init__(self, message: str) -> None:
        self.code = "operator-registry-invalid"
        super().__init__(message)


@dataclass(frozen=True)
class OperatorRegistryRecord:
    """One authoritative Operator, with optional Journal account attribution."""

    name: str
    role: str
    journal_author: str | None = None


class _OperatorRow(BaseModel):
    model_config = ConfigDict(extra="forbid", strict=True)

    name: str
    role: str
    journal_author: str | None = None

    @field_validator("name", "role")
    @classmethod
    def _nonblank(cls, value: str) -> str:
        if not value.strip():
            raise ValueError("Operator name and role must not be blank")
        return value

    @field_validator("journal_author")
    @classmethod
    def _journal_author_is_github_username(cls, value: str | None) -> str | None:
        if value is not None and not AUTHOR_RE.fullmatch(value):
            raise ValueError("journal_author must be a full GitHub username")
        return value


class _OperatorRegistry(BaseModel):
    model_config = ConfigDict(extra="forbid", strict=True)

    operators: list[_OperatorRow] = Field(min_length=1)

    @model_validator(mode="after")
    def _unique_identities(self) -> _OperatorRegistry:
        names = [entry.name for entry in self.operators]
        if len(names) != len(set(names)):
            raise ValueError("Operator names must be unique")
        journal_authors = [entry.journal_author for entry in self.operators if entry.journal_author]
        if len(journal_authors) != len(set(journal_authors)):
            raise ValueError("Journal authors must be unique")
        return self


def parse_operators_registry(payload: bytes) -> tuple[OperatorRegistryRecord, ...]:
    """Validate registry bytes without performing filesystem I/O.

    Membership remains tied to ``name``. ``journal_author`` is solely an
    explicitly declared mapping for Work Journal attribution.
    """
    if not isinstance(payload, bytes):
        raise OperatorRegistryError("Operator registry payload must be bytes")
    try:
        decoded: Any = tomllib.loads(payload.decode("utf-8"))
        registry = _OperatorRegistry.model_validate(decoded)
    except (UnicodeDecodeError, tomllib.TOMLDecodeError, ValidationError, TypeError) as error:
        raise OperatorRegistryError("Operator registry is malformed or ambiguous") from error
    return tuple(
        OperatorRegistryRecord(entry.name, entry.role, entry.journal_author)
        for entry in registry.operators
    )
