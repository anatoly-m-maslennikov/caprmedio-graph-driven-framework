# Issue 1: IS_CONTAINED_BY model rename

Applied and verified at 2026-11-03T17:08:42+04:00.

The Operator chose `IS_CONTAINED_BY` throughout MODEL and explicitly approved manual in-place application after the CA operation returned incomplete context and invalid binding evidence.

- Five Current Declarations: 17 model-name replacements.
- Open model proposal: three reference labels updated.
- IDs, versions, timestamps, value formats and cardinalities preserved.
- Three renamed Property paths parse and inherit correctly; no new coverage gaps, duplicate Declarations or inheritance diagnostics.
- Seven Subject projections rebuilt from the same 1,132 selected source identities with five refreshed source hashes.
- 107 unique applicable Formal Claim blocks verified verbatim.
- Original frontier and prior receipts preserved; old six projections unchanged.

Carrier key mappings, concrete instances, runtime/installed copies, source filenames and historical sources are outside this correction. No native Workflow Run, promotion, Journal event, commit or push is claimed.

`model-rename.patch` is the applied patch; `manifest.json` pins all before/after hashes. `verification.json` records the checks. Other review findings remain open.
