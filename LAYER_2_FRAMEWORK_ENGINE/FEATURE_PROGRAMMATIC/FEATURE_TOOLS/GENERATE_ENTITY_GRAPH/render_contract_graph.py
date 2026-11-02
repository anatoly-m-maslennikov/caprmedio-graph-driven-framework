#!/usr/bin/env python3
"""Render a source-bound formal-contract graph to standard output only.

Usage: render_contract_graph.py source-folder [--repository REPOSITORY]
"""

from __future__ import annotations

import argparse
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from contract_graph import compose_contract_graph, render_contract_graph
from current_entity_sources import read_current_carriers


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source_folder", type=Path)
    parser.add_argument("--repository", type=Path, default=Path.cwd())
    args = parser.parse_args(argv)
    repository = args.repository.resolve()
    carriers = read_current_carriers(args.source_folder, repository)
    print(render_contract_graph(compose_contract_graph(carriers)), end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
