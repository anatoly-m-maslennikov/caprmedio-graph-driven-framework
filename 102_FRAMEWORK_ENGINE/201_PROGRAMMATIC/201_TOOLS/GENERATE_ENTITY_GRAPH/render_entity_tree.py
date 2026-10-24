#!/usr/bin/env python3
"""Build readable Markdown directly from current Atom Subjects in a folder.

Usage: render_entity_tree.py source-folder --projection-id ID --named-selection NAME
       --scope-name SCOPE [--view inherency|declarations] [--output projection.md]
Draft and archived folders are excluded. Output defaults to stdout.
"""

from __future__ import annotations



import argparse
from pathlib import Path
import re
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from artifact_metadata import SETTINGS_PATH, current_timestamp, repository_root  # noqa: E402
from current_entity_sources import read_current_carriers  # noqa: E402
from current_subject_graph import compose_current_graph  # noqa: E402
from declaration_sources import compose_declaration_catalog  # noqa: E402
from declaration_view import render_declarations  # noqa: E402
from generate_entity_graph import atomic_write  # noqa: E402
from readable_entity_tree import render_inherency  # noqa: E402
from VALIDATE_ATOMS.validate_atoms_workers.parsing import parse_carrier  # noqa: E402
from VALIDATE_ATOMS.validate_atoms_workers.settings import CEILINGS  # noqa: E402


def output_path(path: Path, root: Path) -> Path:
    destination = path.absolute()
    projection_root = root / SETTINGS_PATH.parent / "_projection"
    if destination.resolve() != destination or not destination.is_relative_to(projection_root):
        raise ValueError("Output must be a non-symlink path inside the Project _projection folder")
    if destination.suffix != ".md":
        raise ValueError("Output must be a Markdown Projection")
    return destination


def _filename(identity: dict, scope_name: str) -> str:
    projection_id = identity["projection_id"]
    if not re.fullmatch(r"[A-Z][A-Z0-9]*-PROJ-[0-9]+", projection_id):
        raise ValueError("Invalid Projection ID")
    parts = [scope_name, identity["named_selection"]]
    if any(not re.fullmatch(r"[A-Za-z0-9_ -]+", part) or not part.strip() for part in parts):
        raise ValueError("Scope name and named selection must be filename-safe text")
    scope, selection = (re.sub(r" +", "-", part.strip()) for part in parts)
    return f"{projection_id}-{scope}--Entities-Graph--{selection}.md"


def _check_existing(destination: Path, identity: dict, view: str) -> None:
    if not destination.exists():
        return
    maximum = CEILINGS["max_file_bytes"]
    with destination.open("rb") as handle:
        raw = handle.read(maximum + 1)
    if len(raw) > maximum:
        raise ValueError("Existing Projection exceeds max_file_bytes")
    existing = parse_carrier(raw, destination)
    metadata = existing.metadata
    expected = {"artifact_form": "Projection", "type": "Entities Graph", **identity}
    if any(metadata.get(field) != value for field, value in expected.items()):
        raise ValueError("Existing Projection identity or source selection differs")
    other_view = "## Relation Types" if view == "inherency" else "## Inherency tree"
    if other_view in existing.body.splitlines():
        raise ValueError("A different display selection requires a distinct Projection identity")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source_folder", type=Path)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--projection-id", required=True)
    parser.add_argument("--named-selection", required=True)
    parser.add_argument("--scope-name", required=True)
    parser.add_argument("--view", choices=("inherency", "declarations"), default="inherency")
    args = parser.parse_args(argv)
    try:
        source_folder = args.source_folder.absolute()
        root = repository_root(source_folder)
        carriers = read_current_carriers(source_folder, root)
        graph, provenance = compose_current_graph(carriers)
        graph["native_admission"] = "not_performed; structural paths are derived from Subject notation"
        identity = {
            "projection_id": args.projection_id,
            "named_selection": args.named_selection,
            "source_of_truth": [source_folder.relative_to(root).as_posix()],
        }
        filename = _filename(identity, args.scope_name)
        destination = None if args.output is None else output_path(args.output, root)
        if destination is not None:
            if destination.name != filename:
                raise ValueError(f"Projection filename must be {filename}")
            _check_existing(destination, identity, args.view)
        renderer = render_inherency if args.view == "inherency" else render_declarations
        content = graph if args.view == "inherency" else compose_declaration_catalog(carriers)
        result = renderer(
            content,
            provenance,
            updated_at=current_timestamp(root),
            source_selection=f"Current Atoms in {source_folder.relative_to(root).as_posix()}; "
            "draft and archived folders excluded. Subjects and Versions read from the Atom files.",
            projection_identity=identity,
        )
        if destination is None:
            sys.stdout.write(result)
        else:
            atomic_write(destination, result)
    except (OSError, ValueError, RuntimeError, KeyError, TypeError) as error:
        print(f"Cannot render Entities Graph: {error}", file=sys.stderr)
        return 1
    return 0


def _image_main():
    return main()


if __name__ == "__main__":
    # Direct script execution needs the shared process boundary available from the tools root.
    import sys
    from pathlib import Path
    _TOOLS_ROOT = next(p for p in Path(__file__).resolve().parents if p.name in {"201_TOOLS", "TOOLS"})
    if str(_TOOLS_ROOT) not in sys.path:
        sys.path.insert(0, str(_TOOLS_ROOT))
    from runtime_process_boundary import run_process
    raise SystemExit(run_process(_image_main, operation="GENERATE_ENTITY_GRAPH/render_entity_tree"))
