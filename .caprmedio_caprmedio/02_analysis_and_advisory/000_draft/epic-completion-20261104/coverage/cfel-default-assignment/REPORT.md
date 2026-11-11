# CFEL fallback assignment and Project confidence default

**Source-only previews; no Current carrier changed.**

- Current operator descriptor CA-R-2598@1 binds `Operator//Fallback` to `?=`; CA-R-2550@2 defines ordered fallback. Candidate spelling is `?==`, with conditional assignment semantics: retain an authored value or assign the first valid default to the missing Object Property in the Model. CA-R-2487 lists the same operator family; R2705 Label and R2711 Plan-confidence declarations are the two Current CFEL consumers.
- Previewed affected sources R2550, R2598, R2487, R2705, R2711 and R2564. R2550 and R2598 use fresh-ID successor drafts because their Summary changes; the old Current carriers and frozen references remain intact. Current native search found 5 matching source atoms and 10 exact token mentions. No Current Workflow or Workbench carrier contains `?=` (0 excluded uses); none is edited. Draft/history/mirror copies are not Current authority.
- The existing canonical property is `Project.Settings.AI Agent Confidence Threshold` (R2564@2). R2711 already uses that full path as fallback. R1045 allows integer percentages 0–100; 90 is within range.
- R2564 keeps its required occurrence and one-value cardinality, uses the approved `[int, 0..100]` format constraint, and adds `?== 90`. Source-only format-grammar previews define the inclusive range and intersection with `int`; existing cardinality ranges remain unchanged. R2550’s revised semantics set the missing effective Model value; they do not imply a Carrier/file write or a stored authored occurrence. The canonical property name remains unchanged.

Current-source and candidate hashes are in `manifest.json` and `../cfel-spec-audit/operators/successor-format-manifest.json`. No workflow/workbench instances or runtime behavior were changed.

The User pattern uses a shortened `Project.Settings.Confidence Threshold` phrase; the exact current canonical Property is `Project.Settings.AI Agent Confidence Threshold`, which all previews retain. R2711 calls this Project Property directly, while R1428/M271 name the final-precedence source “Framework Instance Settings default”; no new identity is inferred.
