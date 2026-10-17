# Candidate #6 — definition admission package

Status: the bounded activation completed on 2026-10-17. All 79 operations passed independent readback: 51 creations (CA-R-1944–1993 and CA-D-636), 15 updates and 13 retirements. The 28 predecessors retain exact old bytes. The preparation notes below describe the earlier review state, not current pending deployment or identity allocation.

Current-source [Core](../../../CA-PROJ-002-CORE_META_MODEL--Entities-Graph--Current-Atoms.md) and [Project Configuration](../../../CA-PROJ-003-PROJECT_CONFIGURATION--Entities-Graph--Current-Atoms.md) projections were rebuilt. All 45 definitions and five supporting Rs passed the reviewed Claim/Subject/ownership check. Older Subject and model-wide semantic-definition gaps remain visible; this result does not claim complete graph acceptance or broad content migration. See the actual result in CA-P-1959 and [the executed plan](activation/execution-plan.json).

## Contents

- [Status alignment](status-alignment.md)
- [Containment alignment](containment-alignment.md)
- [Revision alignment](revision-alignment.md)
- [Carrier alignment](carrier-alignment.md)
- [Metadata readiness](metadata-readiness.md)
- [Tier resolution](tier-resolution.md)
- [Parent resolution](parent-resolution.md)
- [Identity proposal](identity-proposal.json)
- [Native preflight findings](preflight.md)

These proposals contain exact text for the necessary source changes and distinguish later content work. Current source Versions are observations for review, not permanent tool pins.

Supporting proposals are separate from the original 45: an owner-qualified Atom.Status definition replacing R1306; the already-approved Plan, Workflow and Step containment permissions; and a defining R for the existing CARRIES relation and its derived inverse. A separate D successor preserves representation/binding constraints from D256/D257. These are text proposals, not newly created Atoms. No blanket Operations containment permission or new per-property Carrier is added.

## Readiness limits

This is not yet an executable activation batch. All 45 tier recommendations are resolved: 10 Core/9, 3 General/10 and 32 Standard/11. Thirteen review drafts received metadata-only updates. All 45 have proposed parent links, with a narrow R796 correction grounded in existing ancestor topology. Fresh IDs are proposed after retained-source and Git-history checks, not reserved or assigned.

The two native validator defects have local fixes and focused regression coverage: bounded reference lookup skips clearly unrelated well-formed legacy TOML carriers, and tier-parent validation resolves declared ancestry. C/A migration remains deferred. See preflight.md for the integration result and remaining source alignment.

Independent review found and corrected two proposal gaps: missing Step-to-Step containment permission, and CARRIES still defined only in D. No active-source or runtime validation is claimed by those corrections.

The 2026-10-17 independent parent/tier review found no additional unsupported edge among all 45 proposals. All three selected parents are Active and lower-tier; 43 links use permitted ancestor placement and two use same-owner R1746. R796 source alignment and deployment of the local validator fix remain pending. Package checks confirm 45 matching draft versions, tier assignments and parent rows; whitespace checks pass. This is not a full-suite or successful-admission result.

## Definition inventory

45 proposed definitions: 38 intended for CORE_META_MODEL and 7 for PROJECT_CONFIGURATION. The nine empty review stubs are excluded: two already covered, seven superseded. Existing draft content is linked rather than copied.

| Proposed Subject | Intended owner | Review draft |
| --- | --- | --- |
| Entity/Continuant/Actor.Name | CORE_META_MODEL | [v2](../empty-r-drafts/CA-R--CORE_META_MODEL--define-actor-name.md) |
| Entity/Continuant/Object/Atom.Enabled Relations.Contains | CORE_META_MODEL | [v3](../empty-r-drafts/CA-R--CORE_META_MODEL--define-atom-enabled-relations-contains.md) |
| Entity/Continuant/Object/Atom.Semantics | CORE_META_MODEL | [v4](../empty-r-drafts/CA-R--CORE_META_MODEL--define-atom-semantics.md) |
| Entity/Continuant/Object/Atom.Status | CORE_META_MODEL | [v3](../empty-r-drafts/CA-R--CORE_META_MODEL--define-atom-status-allowed-values.md) |
| Entity/Carrier.Canonical Address.Segment | CORE_META_MODEL | [v2](../empty-r-drafts/CA-R--CORE_META_MODEL--define-carrier-canonical-address-segment.md) |
| Entity/Carrier.Canonical Address | CORE_META_MODEL | [v2](../empty-r-drafts/CA-R--CORE_META_MODEL--define-carrier-canonical-address.md) |
| Entity/Carrier.Format | CORE_META_MODEL | [v2](../empty-r-drafts/CA-R--CORE_META_MODEL--define-carrier-format.md) |
| Entity/Carrier.ID | CORE_META_MODEL | [v3](../empty-r-drafts/CA-R--CORE_META_MODEL--define-carrier-id.md) |
| Entity/Carrier/Directory Carrier.Name | CORE_META_MODEL | [v2](../empty-r-drafts/CA-R--CORE_META_MODEL--define-directory-carrier-name.md) |
| Entity/Carrier/Directory Carrier.Numeric Prefix | CORE_META_MODEL | [v2](../empty-r-drafts/CA-R--CORE_META_MODEL--define-directory-carrier-numeric-prefix.md) |
| Entity/Carrier/Directory Carrier.Path | CORE_META_MODEL | [v2](../empty-r-drafts/CA-R--CORE_META_MODEL--define-directory-carrier-path.md) |
| Entity/Carrier/Database Carrier | CORE_META_MODEL | [v2](../empty-r-drafts/CA-R--CORE_META_MODEL--define-entity-carrier-database-carrier.md) |
| Entity/Carrier/Directory Carrier | CORE_META_MODEL | [v2](../empty-r-drafts/CA-R--CORE_META_MODEL--define-entity-carrier-directory-carrier.md) |
| Entity/Carrier/File Carrier | CORE_META_MODEL | [v2](../empty-r-drafts/CA-R--CORE_META_MODEL--define-entity-carrier-file-carrier.md) |
| Entity/Carrier | CORE_META_MODEL | [v3](../empty-r-drafts/CA-R--CORE_META_MODEL--define-entity-carrier.md) |
| Entity/Continuant/Actor/Type: AI Agent | CORE_META_MODEL | [v2](../empty-r-drafts/CA-R--CORE_META_MODEL--define-entity-continuant-actor-type-ai-agent.md) |
| Entity/Continuant/History/Revision/Type: Atom | CORE_META_MODEL | [v2](../empty-r-drafts/CA-R--CORE_META_MODEL--define-entity-continuant-history-revision-type-atom.md) |
| Entity/Continuant/History | CORE_META_MODEL | [v3](../empty-r-drafts/CA-R--CORE_META_MODEL--define-entity-continuant-history.md) |
| Entity/Continuant/Object/Governing Configuration | CORE_META_MODEL | [v3](../empty-r-drafts/CA-R--CORE_META_MODEL--define-entity-continuant-object-governing-configuration.md) |
| Entity/Continuant/Object/Relation | CORE_META_MODEL | [v3](../empty-r-drafts/CA-R--CORE_META_MODEL--define-entity-continuant-object-relation.md) |
| Entity/Continuant/Object | CORE_META_MODEL | [v3](../empty-r-drafts/CA-R--CORE_META_MODEL--define-entity-continuant-object.md) |
| Entity/Continuant/Projection/Type: Direct Relation Registry | CORE_META_MODEL | [v2](../empty-r-drafts/CA-R--CORE_META_MODEL--define-entity-continuant-projection-type-direct-relation-registry.md) |
| Entity/Continuant/Selection | CORE_META_MODEL | [v3](../empty-r-drafts/CA-R--CORE_META_MODEL--define-entity-continuant-selection.md) |
| Entity/Continuant | CORE_META_MODEL | [v3](../empty-r-drafts/CA-R--CORE_META_MODEL--define-entity-continuant.md) |
| Entity/Occurrent/Event | CORE_META_MODEL | [v2](../empty-r-drafts/CA-R--CORE_META_MODEL--define-entity-occurrent-event.md) |
| Entity/Occurrent/Execution/Action Run | CORE_META_MODEL | [v2](../empty-r-drafts/CA-R--CORE_META_MODEL--define-entity-occurrent-execution-action-run.md) |
| Entity/Occurrent/Execution | CORE_META_MODEL | [v2](../empty-r-drafts/CA-R--CORE_META_MODEL--define-entity-occurrent-execution.md) |
| Entity/Occurrent/Session | CORE_META_MODEL | [v2](../empty-r-drafts/CA-R--CORE_META_MODEL--define-entity-occurrent-session.md) |
| Entity/Occurrent | CORE_META_MODEL | [v3](../empty-r-drafts/CA-R--CORE_META_MODEL--define-entity-occurrent.md) |
| Entity/Occurrent/Execution.Execution ID | CORE_META_MODEL | [v2](../empty-r-drafts/CA-R--CORE_META_MODEL--define-execution-execution-id.md) |
| Entity/Carrier/File Carrier.Extension | CORE_META_MODEL | [v2](../empty-r-drafts/CA-R--CORE_META_MODEL--define-file-carrier-extension.md) |
| Entity/Carrier/File Carrier.Filename | CORE_META_MODEL | [v2](../empty-r-drafts/CA-R--CORE_META_MODEL--define-file-carrier-filename.md) |
| Entity/Carrier/File Carrier.Path | CORE_META_MODEL | [v2](../empty-r-drafts/CA-R--CORE_META_MODEL--define-file-carrier-path.md) |
| Entity/Continuant/Project.Framework Settings.Artifact Timestamp Timezone | PROJECT_CONFIGURATION | [v2](../empty-r-drafts/CA-R--CORE_META_MODEL--define-project-framework-settings-artifact-timestamp-timezone.md) |
| Entity/Continuant/Project.Framework Settings.Code-Root Locators | PROJECT_CONFIGURATION | [v2](../empty-r-drafts/CA-R--CORE_META_MODEL--define-project-framework-settings-code-root-locators.md) |
| Entity/Continuant/Project.Framework Settings.Confidence | PROJECT_CONFIGURATION | [v2](../empty-r-drafts/CA-R--CORE_META_MODEL--define-project-framework-settings-confidence.md) |
| Entity/Continuant/Project.Framework Settings.Framework Control-Root Locator | PROJECT_CONFIGURATION | [v2](../empty-r-drafts/CA-R--CORE_META_MODEL--define-project-framework-settings-framework-control-root-locator.md) |
| Entity/Continuant/Project.Framework Settings.Identifier | PROJECT_CONFIGURATION | [v2](../empty-r-drafts/CA-R--CORE_META_MODEL--define-project-framework-settings-identifier.md) |
| Entity/Continuant/Project.Framework Settings.Interaction | PROJECT_CONFIGURATION | [v2](../empty-r-drafts/CA-R--CORE_META_MODEL--define-project-framework-settings-interaction.md) |
| Entity/Continuant/Project.Framework Settings.Parameter Resolution | PROJECT_CONFIGURATION | [v2](../empty-r-drafts/CA-R--CORE_META_MODEL--define-project-framework-settings-parameter-resolution.md) |
| Entity/Continuant/Project.Operator Registry | CORE_META_MODEL | [v2](../empty-r-drafts/CA-R--CORE_META_MODEL--define-project-operator-registry.md) |
| Entity/Continuant/Project.Settings.Identifier | CORE_META_MODEL | [v2](../empty-r-drafts/CA-R--CORE_META_MODEL--define-project-settings-identifier.md) |
| Entity/Continuant/Object/Relation.Source Reference | CORE_META_MODEL | [v2](../empty-r-drafts/CA-R--CORE_META_MODEL--define-relation-source-reference.md) |
| Entity/Continuant/Object/Relation.Target Reference | CORE_META_MODEL | [v2](../empty-r-drafts/CA-R--CORE_META_MODEL--define-relation-target-reference.md) |
| Entity/Continuant/Object/Scope Unit.ID | CORE_META_MODEL | [v3](../empty-r-drafts/CA-R--CORE_META_MODEL--define-scope-unit-id.md) |

## Publication boundary

1. Resolve only the source conflicts required by the selected definitions. Preserve compatible rules and unrelated content. Keep actual C/A carrier migration deferred.
2. Establish unused Requirement IDs through the existing identity-admission rules. These placeholders are not assigned Atoms; do not invent past identities or treat a maximum active ID as proof that a number was never used.
3. Prepare explicit creation/update requests with current source content, correct owners, admitted tiers and applicable representation. A new source Atom's initial lifecycle/version is determined by the creation route, not by copying the review document's edit counter.
4. Use the existing preview and execution route for the selected effects, then verify sources. Archiving an old rule and creating its replacement are separate explicit effects; do not silently reuse a D ID as an R.
5. Rebuild the graph from actual source Atoms and recheck defining R coverage only after successful admission. A review packet is not that evidence.

## Observed execution support

On 2026-10-16, MCP returned a complete execution context for CA-O-032, with `create_atom` preview/execute available. It requires an explicitly identified logical Atom, unused-ID evidence, complete content and the existing execution authorization. No preview or creation was run for these 45 definitions.

CA-O-066 returned its Draft-admission definition but no runnable tool binding or input schema. Its byte-preserving promotion procedure is not an automatic conversion of these ID-free files under `_projection` into active Atoms. This package does not claim promotion works or authorize a direct-file workaround.

The creation route can be considered for new definitions once its inputs are established; the missing promotion binding alone is not proof that all source creation is blocked. No tooling redesign, release or registry repair is included.

