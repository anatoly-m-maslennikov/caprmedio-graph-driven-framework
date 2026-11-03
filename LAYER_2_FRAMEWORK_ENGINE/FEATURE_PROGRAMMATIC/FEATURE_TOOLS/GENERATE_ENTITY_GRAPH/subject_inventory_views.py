"""Pure Markdown views for the selected Current Subject inventory."""

from __future__ import annotations

from collections.abc import Iterable

import yaml


VIEW_SPECS = (
    ("CA-PROJ-014", "Named Selection//Current-MODEL-Primary-Nodes"),
    ("CA-PROJ-015", "Named Selection//Current-MODEL-Properties"),
    ("CA-PROJ-016", "Named Selection//Current-MODEL-Named-Relations"),
)


def _binding(row: dict) -> str:
    source = row["source"]
    return f"{source['atom_id']}@{source['version']}"


def _frontmatter(identifier: str, selection: str, sources: list[str], now: str) -> dict:
    return {
        "artifact_form": "Projection", "projection_id": identifier, "form": "Map",
        "source": {"named_selection": selection, "atoms": sources}, "updated_at": now,
    }


def _document(metadata: dict, lines: Iterable[str]) -> str:
    return "---\n" + yaml.safe_dump(metadata, allow_unicode=True, sort_keys=False) + "---\n\n" + "\n".join(lines).rstrip() + "\n"


def _rows(rows: list[dict]) -> list[tuple[str, str]]:
    return sorted((str(row["identity"]), _binding(row)) for row in rows)


def _other_expressions(model: dict, admitted: list[dict]) -> list[tuple[str, str]]:
    admitted_bindings = {(_binding(row), row["subject"]) for row in admitted}
    return sorted(
        (str(row["expression"]), _binding(row))
        for row in model["selected_subject_expressions"]
        if (_binding(row), row["expression"]) not in admitted_bindings
    )


def _primary_document(metadata: dict, model: dict, diagnostics: list[str]) -> str:
    primary = model["primary_nodes"]
    lines = [
        "# Subject Graph Primary Subjects", "",
        "A Map of declared Primary Nodes. Other current Subject expressions remain observations, not additional model Nodes.", "",
        "## Primary Nodes", "", "```text",
        *(f"{identity} [{binding}]" for identity, binding in _rows(primary)), "```", "",
        "## Other current Subject expressions", "",
        *(f"- `{expression}` — {binding}" for expression, binding in _other_expressions(model, primary)),
        "", "## Source diagnostics", "",
        *(f"- {diagnostic}" for diagnostic in sorted(diagnostics)),
    ]
    return _document(metadata, lines)


def _property_document(metadata: dict, model: dict) -> str:
    properties = model["properties"]
    lines = [
        "# Subject Graph Properties", "",
        "A Map of declared Properties. Literal formats and cardinalities remain CFEL constraints.", "",
        "## Properties", "",
        *(f"- `{identity}` — {binding}" for identity, binding in _rows(properties)), "",
        "## Preserved non-Node property expressions", "",
        *(f"- `{expression}` — {binding}" for expression, binding in _other_expressions(model, properties)),
    ]
    return _document(metadata, lines)


def _instances_document(metadata: dict, model: dict, constraints: list[dict]) -> str:
    """Render only declared named Relations; constraints remain source-local evidence."""
    lines = [
        "# Subject Graph Instances", "",
        "A Map of declared named Relation Types. CFEL constraints remain local to their source Atoms.", "",
        "## Named Relations", "", "```text",
        *(f"{identity} [{binding}]" for identity, binding in _rows(model["relations"])), "```",
    ]
    return _document(metadata, lines)
