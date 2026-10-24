# Current shared-context fixture

This fixture is a checked-in, source-pinned boundary for the current
`CA-O-016@17` implementation Workflow. It contains exact bytes for the
workflow, its eight current Steps, and their eight bound Actions. `manifest.json`
inventories that graph, while `support_inventory.json` explicitly maps the
selected R/D/E support and all 39 M source pins to frozen carrier bytes under
`support_sources/`. Tests must not discover or copy authority from the live
Project during a run.

The fixture is intentionally definition-only. It is not execution evidence and
does not claim that the native adapter or any Workflow behavior passes. A test
may materialize these bytes into a disposable Project, then use only that
materialized Project and a declared external-Agent transport stub. The fixture
must remain unchanged when live source definitions change; update it only as a
reviewed frozen-corpus revision.

The current graph enters at `CA-O-231`. The old selected route manifest still
starts at `CA-O-091`; the red boundary test records that mismatch explicitly
until the native current-graph adapter exists.

Materialization writes each declared current graph and method source pin to its
declared canonical Project-relative path. The raw method carriers are retained
separately from the concatenated method projection so freshness readers can
resolve and hash each source without a live authority read.
