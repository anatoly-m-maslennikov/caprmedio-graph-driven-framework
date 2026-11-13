#!/usr/bin/env python3
# CA-D-634@23
# CA-D-635@17

"""Build readable Markdown directly from current Atom Subjects in a folder.

Usage: render_entity_tree.py source-folder --projection-id ID --named-selection NAME
       --scope-name SCOPE [--view inherency|declarations|model] [--output projection.md | --stdout]
Draft and archived folders are excluded. Output defaults to the Project _projection folder.
"""

from __future__ import annotations



import argparse
from pathlib import Path
import re
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from artifact_metadata import SETTINGS_PATH, atomic_write, current_timestamp, repository_root  # noqa: E402
from carrier_aliases import carrier_read_view  # noqa: E402
from current_entity_sources import read_current_carriers, read_current_model_carriers  # noqa: E402
from current_subject_graph import compose_current_graph, compose_enhanced_current_graph  # noqa: E402
from declaration_sources import compose_declaration_catalog  # noqa: E402
from declaration_view import render_declarations  # noqa: E402
from readable_entity_tree import named_selection_reference, render_inherency, render_model  # noqa: E402
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


def _filename(identity: dict, scope_name: str, view: str) -> str:
    projection_id = identity["projection_id"]
    if not re.fullmatch(r"[A-Z][A-Z0-9]*-PROJ-[0-9]+", projection_id):
        raise ValueError("Invalid Projection ID")
    parts = [scope_name, identity["named_selection"]]
    if any(not re.fullmatch(r"[A-Za-z0-9_ -]+", part) or not part.strip() for part in parts):
        raise ValueError("Scope name and named selection must be filename-safe text")
    scope, selection = (re.sub(r" +", "-", part.strip()) for part in parts)
    graph_name = "Model-Graph" if view == "model" else "Entities-Graph"
    return f"{projection_id}-{scope}--{graph_name}--{selection}.md"


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
    compatible = carrier_read_view(metadata)
    if compatible.get("artifact_form") != "Projection" or metadata.get("projection_id") != identity["projection_id"]:
        raise ValueError("Existing Projection identity or source selection differs")

    expected_forms = {"inherency": "Map", "declarations": "Catalog", "model": "Map"}
    if "form" in metadata:
        source = metadata.get("source")
        if (
            not isinstance(source, dict)
            or set(source) != {"named_selection", "atoms"}
            or source.get("named_selection") != named_selection_reference(identity["named_selection"])
            or not isinstance(source.get("atoms"), list)
            or not all(isinstance(value, str) and value for value in source["atoms"])
        ):
            raise ValueError("Existing Projection identity or source selection differs")
    else:
        expected = {"type": "Entities Graph", **identity}
        if any(compatible.get(field) != value for field, value in expected.items()):
            raise ValueError("Existing Projection identity or source selection differs")
    headings = {
        "inherency": "## Inherency tree",
        "declarations": "## Relation Types",
        "model": "## Model graph",
    }
    if any(heading in existing.body.splitlines() for name, heading in headings.items() if name != view):
        raise ValueError("A different display selection requires a distinct Projection identity")
    if "form" in metadata and compatible.get("type") != expected_forms[view]:
        raise ValueError("Existing Projection identity or source selection differs")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source_folder", type=Path)
    output = parser.add_mutually_exclusive_group()
    output.add_argument("--output", type=Path)
    output.add_argument("--stdout", action="store_true")
    parser.add_argument("--projection-id", required=True)
    parser.add_argument("--named-selection", required=True)
    parser.add_argument("--scope-name", required=True)
    parser.add_argument("--view", choices=("inherency", "declarations", "model"), default="inherency")
    args = parser.parse_args(argv)
    try:
        source_folder = args.source_folder.absolute()
        root = repository_root(source_folder)
        carriers = (read_current_model_carriers(source_folder, root) if args.view == "model"
                    else read_current_carriers(source_folder, root))
        graph, provenance = (
            compose_enhanced_current_graph(carriers)
            if args.view == "model" else compose_current_graph(carriers)
        )
        graph["native_admission"] = "not_performed; structural paths are derived from Subject notation"
        identity = {
            "projection_id": args.projection_id,
            "named_selection": args.named_selection,
            "source_of_truth": [source_folder.relative_to(root).as_posix()],
        }
        filename = _filename(identity, args.scope_name, args.view)
        destination = None if args.stdout else output_path(
            args.output or root / SETTINGS_PATH.parent / "_projection" / filename, root
        )
        if destination is not None:
            if destination.name != filename:
                raise ValueError(f"Projection filename must be {filename}")
            _check_existing(destination, identity, args.view)
        renderer = {
            "inherency": render_inherency,
            "declarations": render_declarations,
            "model": render_model,
        }[args.view]
        content = graph if args.view != "declarations" else compose_declaration_catalog(carriers)
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
    _TOOLS_ROOT = next(p for p in Path(__file__).resolve().parents if p.name in {"FEATURE_TOOLS", "TOOLS"})
    if str(_TOOLS_ROOT) not in sys.path:
        sys.path.insert(0, str(_TOOLS_ROOT))
    from runtime_process_boundary import run_process
    raise SystemExit(run_process(_image_main, operation="GENERATE_ENTITY_GRAPH/render_entity_tree"))
