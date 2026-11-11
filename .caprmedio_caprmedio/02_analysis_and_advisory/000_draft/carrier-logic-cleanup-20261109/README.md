# Carrier rule cleanup

Nine reviewed Current Core Delivery rules were amended: D269 v30, D446 v30, D472 v31, D473 v27, D483 v26, D650 v16, D470 v33, D479 v36 and D378 v31.

D663 is Archived; D479 replaces its heading-driven contract with declaration-first Content mapping. The replacement link is stored on D479.

Four earlier predecessor Headers were repaired. Ten additional predecessor/retirement records are properly Archived. All 14 retain their original base IDs, numeric Versions, Updated At values and bodies. Four existing legacy physical archive names remain unchanged.

[Source check](source-check.json), [review](review.json), [adoption receipt](adoption-receipt.json) and [archive repair receipt](archive-repair-receipt.json) record the exact selected scope. The plans retain full preimages.

This is a source-only manual cleanup. No native Run or Journal entry is claimed. No source-wide carrier migration, Engine/Workbench implementation, projection rebuild, commit or push was performed.

## Final residual examples

D565 v23, D568 v21, D570 v26 and D657 v11 now use the same declared Header paths and logical Status encoding. [Residual source check](residual-examples/source-check.json) verifies their twelve effects. Across both cleanup passes: 13 amended Current rules, one retired rule, and 18 properly Archived predecessor records (including the four initial repairs). No old `status: Draft` / `status: Archived` wire example remains in the selected Current Core Delivery bodies.

The human-requested **Atom carrier inconsistencies** query is saved through MCP, not just as a local file. [MCP evidence](mcp-query-evidence.json) records its ID, SQL and coverage. It checks indexed physical/stored destinations, aliases and identity/status/version markers. It does not calculate a complete expected folder path or Summary slug; Archived snapshots are excluded by the current index.
