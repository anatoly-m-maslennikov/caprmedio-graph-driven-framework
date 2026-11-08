# General Atom Carrier encoding update

Four reviewed Delivery sources are Current. The model’s canonical names remain semantic source names; this packet defines their Carrier representation.

- Header is delivered recursively to YAML frontmatter with its declared tree.
- YAML name keys and named values use lowercase words joined by single underscores.
- IDs, opaque references, typed scalar data, free text and physical Carrier metadata retain exact values.
- Declared Content keys render as Title Case headings: root Property `##`, one additional `#` per dependent level.
- Only declared headings are Properties. Collisions and unrepresentable heading depth are diagnosed.
- Legacy carrier spellings remain readable until a mechanical migration is explicitly selected.

## Current sources

- CA-D-664 v8
- CA-D-657 v9
- CA-D-479 v34
- CA-D-662 v6

[Source check](source-check.json) verifies 12 exact effects, four byte-exact predecessor snapshots and stable IDs/Summaries. [Examples](examples.json) include the Operator’s two Markdown paths; their heading-depth assertions pass. These are source/contract checks, not native adapter tests.

D662 now follows the common Header mapping instead of remapping Topics into old Subjects fields. D664, D657 and D479 own the general delivery, YAML naming and Markdown rendering contracts.

## Remaining work

No source-wide naming migration, carrier rewrite, Engine/Workbench change, runtime release or projection rebuild was performed. Adapters and affected legacy per-Role examples must follow these rules in their separately selected implementation/migration work.

## Follow-up archival repair

The original source check records raw predecessor snapshots before archival metadata repair. The [2026-11-09 cleanup](../carrier-logic-cleanup-20261109/README.md) corrects Status, Ref ID and destination on those four snapshots while preserving their ID, Version, Updated At and body. Its receipt/source check supersede the earlier archive file hashes; the original adoption plan and receipt remain unchanged as historical evidence. D479 is now v36 after adding its replacement link for retired D663. D657 is now v11 after correcting its remaining legacy wire example.
