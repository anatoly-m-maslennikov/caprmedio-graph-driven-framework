# View actions acceptance

Source acceptance passed on 6 November 2026. This change is not deployed by this pass; actual Codex-host rendering and the full repository suite were not verified.

## Sources

- CA-R-2727@17
- CA-M-470@8
- CA-D-674@22
- CA-E-683@5
- CA-D-681@8
- CA-E-684@6

## Verification

23 real-backend browser cases passed in 33.7 seconds. Three native disposable-host bridge cases, five backend tests, 12 MCP/HTTP tests and 17 frontend Node tests passed. TypeScript, shared standalone/native builds, scoped code reviews and diff checks passed.

Saved links preserve the owning View and its edits/results. Open Saved reuses exact saved identity and keeps equal-SQL saved records distinct. Standalone reload retains saved identity. View context-menu and palette Rename/Duplicate work, with query/cursor-only independent copies, new IDs and first-free no-space suffixes. Duplication neither runs SQL nor copies a saved/result identity.

Checks also exposed and fixed missing callback binding, the New View click-event argument, delayed cached-result fetch on focus, and stale native-dialog close/cancel events. Existing browser cases protect the repaired flows. No retry, queue, shared-result clone or saved-Journal deduplication was added.

Detailed source, review and execution records are in `.caprmedio_tmp/workbench/view-actions-20261106/`.
