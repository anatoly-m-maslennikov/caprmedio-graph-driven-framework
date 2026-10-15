#!/usr/bin/env python3
"""Build readable Markdown directly from current Atom Subjects in a folder.

Usage: render_entity_tree.py source-folder [--output projection.md]
Draft and archived folders are excluded. Output defaults to stdout.
"""

from __future__ import annotations

import argparse
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from artifact_metadata import SETTINGS_PATH, current_timestamp, repository_root  # noqa: E402
from current_entity_sources import build_current_graph  # noqa: E402
from generate_entity_graph import atomic_write  # noqa: E402
from readable_entity_tree import render_inherency  # noqa: E402


def output_path(path: Path, root: Path) -> Path:
    destination = path.absolute()
    projection_root = root / SETTINGS_PATH.parent / "_projection"
    if destination.resolve() != destination or not destination.is_relative_to(projection_root):
        raise ValueError("Output must be a non-symlink path inside the Project _projection folder")
    if destination.suffix != ".md":
        raise ValueError("Output must be a Markdown Projection")
    return destination


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source_folder", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args(argv)
    try:
        source_folder = args.source_folder.absolute()
        root = repository_root(source_folder)
        graph, provenance = build_current_graph(source_folder, root)
        result = render_inherency(
            graph,
            provenance,
            updated_at=current_timestamp(root),
            source_selection=f"Current Atoms in {source_folder.relative_to(root).as_posix()}; "
            "draft and archived folders excluded. Subjects and Versions read from the Atom files.",
        )
        if args.output is None:
            sys.stdout.write(result)
        else:
            atomic_write(output_path(args.output, root), result)
    except (OSError, ValueError, RuntimeError, KeyError, TypeError) as error:
        print(f"Cannot render Entities Graph: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
