# VALIDATE_ATOMS

Read-only implementation of the **Check Atoms** Action (CA-O-087).

## Current readiness

This is an initial, conservative implementation, **not a complete conformance gate**.
It reports supported checks and known failures, but returns `incomplete` while
methodology composition, schema admission, Actor/Entity references, placement,
or another required rule cannot be established. It currently cannot certify a
complete `valid` or `invalid` assessment. An incomplete result is not a pass.

Implemented boundaries include strict JSON request/result models (Pydantic),
bounded safe YAML parsing (PyYAML), duplicate keys, protected paths, no-follow
filesystem reads, independent settings fallback, carried-property selectors,
source revision/digest-bound checks, byte-preserving projection comparison,
duplicate source revisions, deterministic diagnostics, and input currentness.

## Run

Requires Python 3.14 and the `validate-atoms` dependency group in the repository's
`pyproject.toml`. Development checks use `validate-atoms-dev`.

```sh
uv sync --group validate-atoms --group validate-atoms-dev
uv run --group validate-atoms python \
  102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/VALIDATE_ATOMS/validate_atoms.py \
  --input /absolute/path/request.json
```

`--input -` reads JSON from stdin. Exactly one JSON report goes to stdout.
Exit codes: `0 valid`, `1 invalid`, `2 incomplete`, `3 error`.
Request and result authority: CA-D-492 and CA-D-493. No request content is executed.

```json
{
  "schema_version": 1,
  "source_roots": ["/absolute/project/atoms"],
  "allowed_read_roots": ["/absolute/project"],
  "methodology": {
    "kind": "sources",
    "roots": ["/absolute/project/methodology_sources"]
  },
  "selection": {
    "atoms": [{"carrier_path": "/absolute/project/atoms/example.md"}]
  },
  "default_settings": {"path": "/absolute/project/default_settings.toml"}
}
```

The five `[atom_validation]` limits resolve independently from request overrides,
then Framework Instance Settings, then explicitly selected Default Settings.
Default settings auto-location is not implemented. Host safety ceilings remain
upper bounds. Ordinary Scope Unit/tier selectors default to active status;
explicit Atom selectors do not add a Status filter. No Atom property is inferred
from its filename or placement. Scope Unit selection requires Project Structure.

For legacy **authority inputs** without carried identity/status, an exact
`methodology.frontier` binding can enable conditional checks, but leaves admission
incomplete. This never supplies missing properties on validation targets.

## Verification and remaining coverage

```sh
uv run --group validate-atoms --group validate-atoms-dev python -m unittest discover \
  -s 102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/VALIDATE_ATOMS/tests
uv run --group validate-atoms-dev ruff check \
  102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/VALIDATE_ATOMS
uv run --group validate-atoms-dev mypy --no-incremental --cache-dir=/dev/null \
  102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/VALIDATE_ATOMS
```

Tests include independently authored JSON golden reports, good/bad mock carriers,
byte-exact source fixtures, actual CLI subprocess calls, read-only fingerprints,
unsafe inputs, and targeted regressions. Test fixtures are created only beneath
`.caprmedio_tmp`; the command creates no files or bytecode. Host-denied cleanup
leaves fixture directories there and emits a warning.

Remaining work includes complete source composition/admission, extensible Property
contracts and reference resolution, full address/placement rules, executable
coverage of every rule/boundary, and a complete-positive golden report. Supplied
Rule Bundles are currently reported as unsupported, never executed. YAML aliases,
merge keys, and unsupported projection binding encodings produce visible gaps.
Source spans are currently null; the command does not invent coordinates.

CA-P-1106 and its child Plans remain Active. No full-acceptance claim is made.
