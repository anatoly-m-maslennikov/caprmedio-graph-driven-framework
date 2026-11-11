# Settings and capability reconciliation

## Result

Prepared pinned source previews and retirement candidates only. No Current carrier, Project setting, Git state, Tool catalog, Extension instance, or implementation was changed.

Current `CA-R-2532@8` lists the allowed children of `Project.Settings` and excludes both Tool Selections and Extension Selections. The prior property schema IDs `CA-R-2408` and `CA-R-2411` have no active canonical source carriers; their archive references remain historical. Do not recreate those fields. Current Confidence contracts remain separate and active: `CA-R-1979@16`, `CA-R-2624@2`, and `CA-R-2625@2`; defaults remain governed by `CA-R-1652@41` and `CA-R-380@44`, with Framework Instance default serialization still in `CA-D-368@29` / `CA-D-369@28`.

## Preview decisions

- Keep broad `CA-R-1421` and `CA-R-831` configuration/extensibility authority unchanged as future-facing governance; this packet adds no Extension or Tool behavior.
- `CA-R-832`, `CA-R-1207`, `CA-R-1375`, and `CA-R-1724` previews remove field-specific Extension/Tool selection claims while retaining capability configuration, ownership separation, Core permission boundaries, and configuration precedence.
- `CA-R-2624` and `CA-R-2625` previews explicitly preserve integer-percentage semantics while retaining optional single values and the inherited integer format. They add no numeric range.
- The `CA-R-2271` preview is confidence-only. Its former schema constraints duplicate R1979/R2624/R2625, while the integer-percentage override statement is preserved in the new Rule. Because the Summary changes, the candidate uses `NEW_ID_REQUIRED` and `NEW_VERSION_REQUIRED`; it is not an allocated Draft.
- `CA-D-372` and `CA-D-373` are field-only Tool/Extension selection serialization decisions for the Framework Instance Settings TOML Carrier. Their retirement is conditional on replacing R2271 and preserving every frozen `@version` reference. Their only active unversioned Atom-reference owner is R2271.
- `CA-R-2277` is **held**, not retired. Its abstract `Extension Sources` Selection address remains on 15 active canonical source owners. This address supports source-authority boundaries even though no Tool/Extension Settings or installed Extension behavior is added here.

## Cross-scope gate

The proposed narrowing of `CA-R-1228` and `CA-E-379` is blocked pending reconciliation with active source-selection consumers outside this lane. In particular, Engine `CA-R-1839` still includes activated installed Extension sources in the applicable frontier; `CA-E-559`, `CA-R-1226`, `CA-R-1286`, `CA-R-1313`, `CA-R-1515`, `CA-R-1748`, `CA-R-1874`, and `CA-R-1875` also retain relevant selection/source-auth references. Apply neither preview until those current obligations have a coordinated disposition. Keep `CA-R-2277` and unrelated source-auth Subjects intact.

`CA-R-1175@3` is archived only and was not restored. Full unversioned/pinned Atom-reference and subject-address inventories, source hashes, candidate hashes, conditional retirements, and the cross-scope hold are in `manifest.json`, `reference-inventory.json`, `subject-address-inventory.json`, and the active-reference indexes.
