---
atom_id: CA-R-1937@4
content_role: Requirement
type: Requirement
current_scope_unit: CONNECTOR_TOOLS
claim_target_scope_unit: CONNECTOR_TOOLS
local_tier: Standard
global_tier: 11
status: Archived
author: Anatoly Maslennikov
version: 4
updated_at: "2026-10-13 02:01:49 +0400"
subjects:
  governs: "Tool"
  depends_on: ["Scope Unit", "Project", "Project Structure", "Project Settings"]
relations:
  relates_to: [CA-M-377, CA-E-629, CA-D-626, CA-O-211, CA-R-1936, CA-M-376, CA-E-628, CA-D-625, CA-R-1484, CA-D-442]
---
# Summary

Query declared Scope Units

## Scope

The read-only Query connector operation for declared Scope Units in one explicitly bound Project and source view.

## Claim

the Scope Unit Query result **must** contain **every** **and** **only** matching declared Scope Unit **in** the caller's explicit logical frontier, with stable canonical identities, requested matching facts, actual source-state evidence **and** truthful coverage. an empty match set is a valid complete result; one **or** several matches require no different operation. Query returns matching facts, **not** full declarations, **and** grants no effect permission.

logical identity **must** reuse the canonical Scope Unit Name within the explicitly bound owning Project, under CA-R-1484-CORE_META_MODEL-GENERAL-REQUIREMENT--establish-scope-units-through-project-structure-declarations. Project Settings supplies the root Project identity; Project Structure supplies non-Project declarations under CA-R-1483-CORE_META_MODEL-CORE--define-authoritative-project-structure. do **not** create another ID, infer a Scope Unit from a folder, hide an unmaterialized unit **or** missing Goal, use a Projection as independent authority, **or** invent an Atom Version.

the explicit frontier **and** conjunctive filters **must** use the operation schema **in** CA-D-626-CONNECTOR_TOOLS-STANDARD-DELIVERY--deliver-declared-scope-unit-query-data. the connector applies **only** supplied name, Type, Label **and** direct-parent criteria, with the expressly selected literal match mode. it **must not** infer a lifecycle filter, Subject relation, alias, omitted frontier, whole-Project default **or** subsequent Read/Modify. the caller owns selection policy; a standalone admitted Query requires no enclosing Workflow.

current **or** expressly pinned/historical source views **must** be resolved from bound context **and** exact applicable state evidence. invalid request **or** declaration schema, missing **or** ambiguous authority, stale supplied state, denied read permission, backend failure **or** incomplete coverage **must** yield the applicable structured error under CA-D-625-CONNECTOR_TOOLS-CORE-DELIVERY--deliver-coherent-connector-interface, **not** a complete successful result. duplicate identities, missing parents **or** cycles **must not** be disguised as ordinary non-matches. no declaration, Carrier, history, Version, timestamp **or** lifecycle effect is admitted.

## Details

CA-M-377-CONNECTOR_TOOLS-STANDARD-METHOD--construct-a-declared-scope-unit-query-adapter supplies the adapter convention; CA-O-211-CONNECTOR_TOOLS-STANDARD-ACTION--query-declared-scope-units defines the Action; CA-E-629-CONNECTOR_TOOLS-STANDARD-QA_CASE--verify-declared-scope-unit-queries supplies future conformance cases. The common API remains CA-R-1936-CONNECTOR_TOOLS-CORE-REQUIREMENT--use-one-coherent-connector-interface. This operation-specific source packet is not implementation, independent acceptance, an admitted runtime route or migration authority.
