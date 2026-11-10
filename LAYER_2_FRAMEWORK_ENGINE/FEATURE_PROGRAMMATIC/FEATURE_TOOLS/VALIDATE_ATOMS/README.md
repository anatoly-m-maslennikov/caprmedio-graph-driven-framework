# Retained validation helpers

This directory no longer ships the retired `validate_atoms` CLI or its broad
adapter pipeline.

The remaining `validate_atoms_workers` package is an internal shared boundary
for Workbench and Subject/Topics projections. It provides:

- bounded, no-follow reads and safe YAML frontmatter parsing;
- Header grouping and carrier identity checks;
- pinned, byte-exact source admission for the current Graph Rule closure; and
- fence-aware structural validation of Graph Rule bodies.

`schema_authority.json` is the sole admitted support-source manifest. A missing,
changed, duplicated or unverified source remains a visible admission gap; parsing
does not admit it.

Run the focused checks from the repository root:

```sh
PYTHONPATH="$PWD/LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_TOOLS" \
  .venv/bin/python -B -m unittest discover \
  -s LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_TOOLS/VALIDATE_ATOMS/tests \
  -p test_graph_rule_body.py
```
