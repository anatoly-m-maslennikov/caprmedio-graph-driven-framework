# Candidate #6 — definition draft reconciliation

Status: review drafts only. No source Atoms are created, activated or relocated.

Reviewed: 2026-10-16. All 54 placeholders accounted for: 45 proposed definitions, 2 covered by existing Rs and 7 superseded. No placeholder meaning decisions remain. The last 9 Claims remain empty.

The 54 files in `empty-r-drafts/` are the original unassigned review placeholders. The directory and filenames are retained for traceability; the directory name no longer means every Claim is empty. Intended owner fields do not move a file into the authoritative source set.

## Changes

- Project Subjects use `Entity/Continuant/Project`, not `Entity/Continuant/Object/Project`.
- Project-specific Framework Settings definitions target `PROJECT_CONFIGURATION`. Generic definitions stay in `CORE_META_MODEL`.
- Fill only missing definitions supported by the accepted candidate and source evidence. Add no implementation, serialization or admission policies.
- Reuse existing defining Rs. Keep covered and superseded placeholders with empty Claims and explicit dispositions; do not admit them as duplicate definitions.
- Governance Origin has only Internal and External, covered by CA-R-1709. Containment is separate, not a third Origin.
- Metadata fields and Markdown sections both represent Atom properties. Semantics remains a dependent property; D governs its in-file representation and M governs authoring.
- Draft definitions do not close active R-coverage gaps or resolve contradictory current source content.

## Existing coverage — no duplicate draft Claim

- `Atom.Governance Origin`: CA-R-1709. The historical filename still says Governance Locus.
- `Project.Framework Settings.Tool Selections`: CA-R-1724. Its obsolete Extension clauses still need the separate content pass.

## Superseded placeholders — do not admit

- Carrier.Storage Boundary: dropped by the Operator. Preserve CA-D-341's storage-protection policy and review its Subject/old ownership terms during content migration; the active rule remains unchanged.
- Carrier.Ownership Class: dropped by the Operator. Review actual project-specific storage rules separately in Project Configuration during content migration; active CA-D-316 remains unchanged.
- Atom.Property: keep concrete properties, not an extra aggregate field. Their bearer relation is IS_BORNE_BY; shared Property meaning belongs in the Terms view.
- Framework Settings.Extension Selections: install Extension Atoms, then regenerate; no additional enablement layer.
- Framework Settings.Revision Binding and Project.Settings.Revision Binding: no separate binding entity is needed.
- Framework Settings.Parameter Resolution Validation: an Evaluation checks Parameter Resolution; that does not create another property.

## Next step

Placeholder reconciliation is complete. The [definition-admission package](definition-admission/README.md) lists all 45 definitions and exact Status, containment, Revision and Carrier source-alignment proposals. Reuse the 2 existing definitions and exclude the 7 superseded placeholders. On 2026-10-17, all tiers were resolved, all 45 parent links were proposed, and unused identities were checked without reservation. The narrow parent-rule correction, source alignment and executable admission remain pending; see the recorded tool blockers. Keep unrelated content migration separate; do not treat these drafts as active definitions.

## Source conflicts stay separate

- CA-R-1342 still assigns Carrier definitions to Delivery; new R drafts do not silently change that rule.
- Existing Status, collection/containment and Revision rules contain older model assumptions. Each affected draft records the relevant evidence; activation needs explicit content alignment.
- This review does not assign Atom IDs, promote drafts, rebuild projections or run migration.

## Checks

All 54 files parse as YAML-frontmatter Markdown, remain Draft without IDs and retain the four content sections. The tier pass updated 13 review drafts' tier, version and timestamp metadata only; their Claims and other content were preserved. Current versions for the 45 definitions are recorded in identity-proposal.json inside the admission package. All Subjects have full Entity paths; no old `Object/Project` path remains in these drafts. Forty-five Claims are populated and nine are intentionally empty. These checks validate the review package, not authoritative admission or runtime behavior.
