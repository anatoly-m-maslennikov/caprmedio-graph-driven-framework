# In-memory DuckDB + DuckPGQ compatibility probe — 4 November 2026

This is runtime research, not a Workbench implementation or release. No project Python environment, source Atom, live container, or Git state was changed by the probes. Probe scripts and isolated environments are under `/private/tmp`.

## Observed native-host result

macOS arm64; Python 3.12.16; DuckDB 2.0.0; DuckPGQ community extension for `v2.0.0/osx_arm64`.

| Check | Result |
| --- | --- |
| In-memory connection, extension installation/loading, grammar activation | Passed |
| Property graph creation and direct/inverse `GRAPH_TABLE` matching | Passed; direct `(1, 2)`, inverse `(2, 1)` |
| Empty `temp_directory`, external access disabled, configuration locked | Settings retained; enabling external access later was rejected. This does not prove memory-pressure no-spill behavior. |
| Native read-only transaction | `BEGIN TRANSACTION READ ONLY` accepted; a direct INSERT was rejected. |
| `SELECT delete_csr(1)` | Classified SELECT; returned false; registered graph remained present. No universal cache-purity claim follows. |
| `SELECT * FROM drop_property_graph()` | Classified SELECT; entered the extension and raised an internal error that invalidated the connection, including inside a read-only transaction. |
| Native JSON SQL AST | Works for plain SELECT; GRAPH_TABLE serialization is not implemented for process-local bind input. |
| Catalog side-effect metadata | False/NULL on relevant extension functions; insufficient for a reliable function-purity rule. |
| `disabled_functions` configuration | Not recognized in the probed DuckDB version. |

A native SELECT classifier is necessary but insufficient evidence for the full declared graph-query boundary. Ordinary internal query caching is distinct from changing logical rows or registered graph definitions. The earlier broad cache-mutation wording needs care; this probe did not establish that ordinary graph reads change logical Projection facts.

## Reader investigation

Reusable helpers exist for safe YAML parsing, stable reads/inventory, and Current Scope Unit Declarations. There is no admitted mechanically readable Declaration-to-reader-schema mapping for Header storage keys, Content applicability, and generic inverse declarations. The Operator has been asked whether the MVP should parse the existing YAML and Markdown rules directly rather than introduce a schema compiler. No inferred mapping or compiler was implemented.

## Linux Docker result

Passed on the project-pinned Python 3.14.7-slim base, Linux/aarch64, DuckDB 2.0.0 and DuckPGQ community extension `9c11bc192a`. The in-memory graph query returned `[('Ada', 'Grace')]` after extension loading and grammar activation with an empty temporary directory. The disposable container used `--rm`; the labeled probe image remains available for inspection. No running project container was replaced or restarted.

Evidence: `/private/tmp/workbench-duckpgq-docker-probe-20261104/RESULT.md`, `Dockerfile`, and `probe.py`. This establishes dependency/grammar availability, not the public-query boundary, no-spill behavior under memory pressure, or the complete Workbench MVP.

## Retained probe scripts

- `/private/tmp/workbench-duckpgq-probe-20261104/probe.py` — SHA-256 `4bafd9ded329144b6339684bbf97c2144bed006637c4424aa45a06aa664711b8`
- `/private/tmp/workbench-duckpgq-probe-20261104/ast_probe.py` — SHA-256 `0d1d9df23f4914b955a3771ef0d84649beb0b0cc6a87b603b3350f6b4f0c01f1`
