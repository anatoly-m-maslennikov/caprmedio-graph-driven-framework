---
atom_id: CA-P-2683@2
content_role: Plan
type: Plan
label: Epic
current_scope_unit: caprmedio
author: Anatoly Maslennikov
status: Archived
subjects:
  governs: Formal Model
version: 2
updated_at: 2026-10-28 20:04:15 +0400
relations: {}
tier: 3
---
# Summary

Migrate Formal Model syntax and Claims

## Objective

Adopt the latest Formal Model syntax, value Formats, Relations and RMED Claim layout in Current Methodology and direct project-local RMED; formalize all in-scope Requirement Claims fully or partially where their meaning can be preserved; then rebuild the primary and property views from the actual adopted sources.

## Details

### Scope

Include Current Requirement, Method, Evaluation and Delivery sources in Methodology plus the Project's direct local RMED. Declare the exact source boundary in P2684. Preserve existing Archives and unrelated Drafts; selected Current updates create normal predecessors. This Epic does not migrate C/A/P/O content, Engine RMED, Scope Unit structure, code, Tools/MCP/runtime, getter APIs, Terms Graph implementation or releases. [P2637 owns the later Engine RMED migration](CA-P-2637-EPIC--migrate-engine-rmed-atoms.md).

### Latest decisions

The latest Operator input overrides older candidates and packet wording. Formal Model replaces the Subject root. Its base branches are Continuant, Occurrent, Aspect, Format, Carrier and Graph Syntax. Graph Syntax includes Relations and other formal constructs. Structural constraints belong to Definition Claims; there is no separate Graph Rule instance population or replacement Rule population.

Every complete RMED Atom has content.claim{1}, with prose directly under ## Claim. Only R admits optional ### Formal claim at content.claim.formal_claim{0..1}; M/E/D keep prose Claims for now. At least one substantive part is present. Their combination is one Claim unit under its Role/Type. Semantics is separate optional meaning/explanation and adds no operative constraints. YAML access stays atom.version_number; Markdown access stays atom.content.claim. No new property/text grouping layer is introduced.

Use ((RELATION_TYPE)) for Relations without short notation; derive inverse views instead of adding backwards syntax or duplicate stored facts. Format concerns value types, including explicitly scoped uniqueness, not Carrier serialization formats. Full subjects.governs identifies the governed node/property; a formal Claim states its definition and constraints.

### Execution order and lanes

P2684 establishes the source set. P2685 (syntax) and P2686 (Formats) may then run in parallel with exclusive file ownership. P2687 completes Relation definitions; P2688 adopts foundations; P2689 migrates paths/links; P2690 migrates the body/property layout; P2691 formalizes only the Requirement Claims; P2692 retires superseded sources; P2693 rebuilds and verifies. Keep publication, shared Journal writes and Git integration under one owner; reuse suitable workers for independent source groups and reviews.

Each leaf Task/Subtask targets at most 15 minutes of agent work. Container stages must create bounded children before a large corpus pass. Use simple batches and the supported existing source-update path, or the already-authorized direct file route when MCP cannot support the operation. Do not add per-Atom reports, Analysis Atoms, confirmations or a new security/history framework. Ask the Operator only for concrete meaning decisions below 95% confidence; never invent missing policy to force a formalization.

### Tasks

- [P2684 — Inventory Current sources and reconcile migration Drafts](CA-P-2683-EPIC--migrate-formal-model-syntax-and-claims/01-CA-P-2684-TASK--inventory-current-sources-and-reconcile-migration-drafts.md)
- [P2685 — Complete syntax RMED and Markdown property contracts](CA-P-2683-EPIC--migrate-formal-model-syntax-and-claims/02-CA-P-2685-TASK--complete-syntax-rmed-and-markdown-property-contracts.md)
- [P2686 — Complete value Format definitions and constraints](CA-P-2683-EPIC--migrate-formal-model-syntax-and-claims/03-CA-P-2686-TASK--complete-value-format-definitions-and-constraints.md)
- [P2687 — Define new Relations and their derived inverses](CA-P-2683-EPIC--migrate-formal-model-syntax-and-claims/04-CA-P-2687-TASK--define-new-relations-and-their-derived-inverses.md)
- [P2688 — Adopt the Formal Model foundations](CA-P-2683-EPIC--migrate-formal-model-syntax-and-claims/05-CA-P-2688-TASK--adopt-the-formal-model-foundations.md)
- [P2689 — Migrate governing paths and apply the new Relations](CA-P-2683-EPIC--migrate-formal-model-syntax-and-claims/06-CA-P-2689-TASK--migrate-governing-paths-and-apply-the-new-relations.md)
- [P2690 — Migrate RMED body sections to logical properties](CA-P-2683-EPIC--migrate-formal-model-syntax-and-claims/07-CA-P-2690-TASK--migrate-rmed-body-sections-to-logical-properties.md)
- [P2691 — Formalize in-scope Claims in bounded batches](CA-P-2683-EPIC--migrate-formal-model-syntax-and-claims/08-CA-P-2691-TASK--formalize-in-scope-claims-in-bounded-batches.md)
- [P2692 — Retire superseded contracts after preserving their meanings](CA-P-2683-EPIC--migrate-formal-model-syntax-and-claims/09-CA-P-2692-TASK--retire-superseded-contracts-after-preserving-their-meanings.md)
- [P2693 — Rebuild the actual Formal Model views and close the migration](CA-P-2683-EPIC--migrate-formal-model-syntax-and-claims/10-CA-P-2693-TASK--rebuild-the-actual-formal-model-views-and-close-the-migration.md)

### Prepared evidence, not migration results

CA-A-1239 holds the current primary/property Draft. A1240–A1243 record the accepted notation, model-Definition, Claim/layout and heading decisions. Successor Drafts already exist, but their existence is not adoption. Five special Graph Rule packet entries were marked superseded, not retired from Current. Primitive Format definitions, ID-reference bindings and remaining syntax details need completion before migration. No task in this Epic is marked Done based solely on those preparations.

The thin [Governs table](CA-P-2683-EPIC--migrate-formal-model-syntax-and-claims/governs.tsv) and [Depends On table](CA-P-2683-EPIC--migrate-formal-model-syntax-and-claims/depends_on.tsv) track source dispositions. No copied Claims or large mapping report is introduced. The seeded Governs rows represent known prepared Drafts only; Depends On remains unstarted.

### Sources

- [formal-model-primary-kinds-and-properties](../02_analysis/draft/CA-A-1239@1-draft-SPECIFICATION_PROPOSAL--formal-model-primary-kinds-and-properties.md)
- [use-named-relation-notation](../02_analysis/CA-A-1240-SPECIFICATION_PROPOSAL--use-named-relation-notation.md)
- [use-one-content-claim-and-stable-rmed-headings](../02_analysis/CA-A-1241-SPECIFICATION_PROPOSAL--use-one-content-claim-and-stable-rmed-headings.md)
- [define-model-constraints-with-one-formal-claim](../02_analysis/CA-A-1242-SPECIFICATION_PROPOSAL--define-model-constraints-with-one-formal-claim.md)
- [define-type-specific-claim-and-formal-child](../02_analysis/CA-A-1243-SPECIFICATION_PROPOSAL--define-type-specific-claim-and-formal-child.md)

## Definition of Done

The declared Current Methodology/direct-project-local RMED frontier has adopted the needed syntax, Format and Relation contracts; governing/dependency paths and necessary formal references are migrated; body properties use the chosen Markdown hierarchy; every selected R Claim has a full/partial/prose-retained disposition while M/E/D remain prose without meaning loss; obsolete contracts are retired only after preserving their needed meaning and repairing consumers; and actual-source primary/property views agree. No unresolved required case, Engine dependency, unimplemented consumer or partial frontier is hidden by a Done status.

## Progress

Active planning and prepared-Draft state. The preceding P2673 Epic remains Done. This follow-up records the authorized migration sequence; no Current RMED source has been promoted or migrated by creating it.

## R-only formalization refinement

[A1244](../02_analysis/CA-A-1244-SPECIFICATION_PROPOSAL--limit-operative-formal-claims-to-requirements.md) limits operative formal Claims to R for now. M/E/D remain in syntax/format RMED, path and layout migration, but are not converted to operative formal_claim fields.
