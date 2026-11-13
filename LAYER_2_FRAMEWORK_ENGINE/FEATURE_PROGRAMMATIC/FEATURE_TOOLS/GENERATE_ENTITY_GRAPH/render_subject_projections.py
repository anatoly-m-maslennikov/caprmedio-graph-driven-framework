#!/usr/bin/env python3
"""Render one of seven current Subject/Topics views to standard output."""

from __future__ import annotations

import argparse
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from current_entity_sources import read_current_carriers
from subject_projection_audits import build_subject_audits, render_subject_audit, select_model_subjects
from subject_projection_data import build_subject_projection_data
from subject_projection_views import render_primary_projection


VIEWS = {
    "primary-tree": 1,
    "direct-properties": 2,
    "inherited-contracts": 3,
    "formal-claims": 4,
    "passive-only-subjects": "passive_only_subjects",
    "subjects-without-declarations": "subjects_without_declaration_coverage",
    "entity-definition-coverage": "entity_definition_summary",
}


def render_view(carriers: list[dict], view: str) -> str:
    """Render source-bound MODEL occurrences without granting admission."""
    scoped, diagnostics = select_model_subjects(carriers)
    model_carriers = [carrier for carrier in scoped
                      if any(key in carrier.get("subjects", {}) for key in ("active", "governs"))]
    data = build_subject_projection_data(model_carriers)
    mode = VIEWS[view]
    if isinstance(mode, int):
        return render_primary_projection(data, mode)
    audits = build_subject_audits(scoped, data, scope_diagnostics=diagnostics)
    return render_subject_audit(audits, mode)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source_folder", type=Path, help="Explicit current Atom selection; relative to the repository")
    parser.add_argument("--repository", type=Path, required=True)
    parser.add_argument("--view", choices=VIEWS, required=True)
    parser.add_argument("--model-draft-manifest", type=Path,
                        help="Preview Model Drafts over their exact Current predecessors")
    args = parser.parse_args(argv)
    repository = args.repository.resolve()
    source = (repository / args.source_folder).absolute()
    try:
        if not source.resolve().is_relative_to(repository):
            raise ValueError("Source folder must be inside the selected repository")
        carriers = read_current_carriers(
            source, repository, model_draft_manifest=args.model_draft_manifest,
        )
        rendered = render_view(carriers, args.view)
        if args.model_draft_manifest is not None:
            sys.stdout.write("> **Draft preview.** Model declarations are selected by the supplied manifest.\n\n")
        sys.stdout.write(rendered)
    except (OSError, ValueError, RuntimeError, KeyError, TypeError) as error:
        print(f"Cannot render Subject projection: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
