# Manual semantic adoption integration

This entrypoint normalizes the five reviewed packet schemas, rejects shared
source ownership or stale pins, and reuses the prior MODEL adoption helper's
native lock, SHA preflight, exact predecessor archives, exclusive creates,
atomic replacement and owned rollback. It allocates no IDs. The root supplies
the fresh numeric ID for the changed R2279 Summary and the adoption timestamp.
Same-Summary revisions retain their historical filenames and use the next
observed version. Retirements archive exact predecessor bytes, then remove the
Current file. Neither native workflow admission nor journal append is implied.

Run from the repository root; substitute the root-approved values below:

```bash
packet_root=.caprmedio_caprmedio/02_analysis/draft/model-completeness-audit-20261103/implementation
.venv/bin/python "$packet_root/integration/adopt.py" prepare \
  --manifest "$packet_root/declarations/manifest.json" \
  --manifest "$packet_root/relations/source-candidate-map.json" \
  --manifest "$packet_root/objects-carriers/manifest.json" \
  --manifest "$packet_root/carrier-declarations/manifest.json" \
  --manifest "$packet_root/variables/manifest.json" \
  --frontier "$packet_root/frontiers/model-supplier-frontier-refreshed.json" \
  --new-relation-id CA-R-2732 \
  --timestamp 'ROOT_APPROVED_TIMESTAMP'
.venv/bin/python "$packet_root/integration/adopt.py" check
.venv/bin/python "$packet_root/integration/adopt.py" references \
  --frontier "$packet_root/frontiers/model-supplier-frontier-refreshed.json" \
  --output "$packet_root/integration/reviewed-reference-map.json"
```

`prepare` writes only this folder's `adoption-plan.json`. `check` is read-only
and returns `before` or `after`; mixed or drifted states fail. Review the entire
plan, especially its full pinned before/after payloads, before the root applies:

```bash
.venv/bin/python "$packet_root/integration/adopt.py" apply
.venv/bin/python "$packet_root/integration/adopt.py" check
.venv/bin/python "$packet_root/integration/adopt.py" refresh \
  --frontier "$packet_root/../model-supplier-frontier.json" \
  --output "$packet_root/integration/post-adoption-frontier.json"
.venv/bin/python "$packet_root/migration/migrate.py" plan \
  --frontier "$packet_root/integration/post-adoption-frontier.json" \
  --map "$packet_root/integration/reviewed-reference-map.json" \
  --output "$packet_root/integration/mechanical-plan.json"
```

The references command generates prospective hash-pinned overrides without canonical writes. It rewrites current bare-ID and IS_DEFINED_BY tokens in Subject expressions and body references while preserving frozen @N references, carrier identity metadata, Summary and literal operands. Full-frontier pins are checked during prepare and under the native apply lock; a newly occupied fresh ID aborts before any write. The root reviews this map before mechanical application.
The adoption plan's `base_id_replacements` describes the changed R2279 authority;
current bare references may follow its new ID. Frozen `oldId@N`, archived
predecessors, quoted templates and carrier identity metadata remain unchanged.
Retired IDs have no guessed replacement: approved consumer changes must name
existing surviving authority explicitly. The mechanical migrator requires
reviewed overrides for reference changes it does not itself support. Confirm
zero held sources and review metadata/Summary invariants before applying that
separate mechanical plan. A complete semantic apply is required before
`refresh`; refresh changes only its requested frontier output.

Tests (all temporary repositories; no canonical writes):

```bash
.venv/bin/python -m unittest discover -s "$packet_root/integration" -v
```
