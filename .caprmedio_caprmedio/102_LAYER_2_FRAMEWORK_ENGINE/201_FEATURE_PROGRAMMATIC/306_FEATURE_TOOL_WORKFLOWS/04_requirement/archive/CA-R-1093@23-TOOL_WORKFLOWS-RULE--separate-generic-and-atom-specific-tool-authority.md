---
atom_id: CA-R-1093@23
subjects:
  governs: Subject/Graph Rule
  depends_on:
  - Subject/Graph Node/Implementation/Code/Tool
  - Subject/Graph Node/Engineering/Architecture/Communication
cce_version: cce_1
cce_form: obligation
version: 23
status: Archived
updated_at: 2026-10-27 06:04:45 +0400
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
content_role: Requirement
current_scope_unit: TOOL_WORKFLOWS
claim_target_scope_unit: TOOL_WORKFLOWS
tier: 1
type: Rule
author: Anatoly Maslennikov
---
# Summary

Separate generic and Atom-specific Tool authority

## Scope

Semantic operation ownership and logical operation/storage connector boundaries for Atom and Scope Unit Workflows.

## Claim

**every** public logical Tool operation **must** have **=1** Workflow semantic behavior owner. This is policy ownership, not a requirement for a new wrapper or a mandatory enclosing Workflow around standalone connector Query or Read. Admitted Find, Read and Modify remain independently callable with their required explicit caller/context, source, schema and authorization bindings. The Workflow owns target-selection policy, admitted domain schemas, identity, Version, lifecycle, authority and operation sequencing; a connector **must not** choose them. Generic Artifact Workflows own their admitted artifact-form-agnostic revision, naming and reference policies but **must not** define CAPRMEDIO Atom admission or lifecycle semantics. Atom Workflows own those semantics for their named operations and **may** reuse admitted generic helpers. Simple connectors own only explicit query, read, create or modify storage mechanics under CA-R-1936-CONNECTOR_TOOLS-RULE--use-one-coherent-connector-interface; mixed semantic Artifact procedures are Workflows, not connectors.

MCP owns discovery, projection, transport validation, request forwarding, **and** result transport. it **must** delegate **to** the canonical Tool **and** **must not** resolve an Atom target, reinterpret a Tool contract, decide a mutation, mutate a carrier, **or** recover an effect. a CAPRMEDIO Markdown Atom Doer's `--apply` entry point is callable **only** through an authorized project-local MCP delegation; direct execution **may** produce a mutation-free dry run but **must** reject `--apply`.

Find, Read and Modify **must** be independent logical operations. Find returns matching Atom or Scope Unit identities and matching facts; Read obtains the complete explicitly selected source with its exact identity and Version or revision; Modify accepts explicit targets and does not silently Find or replace them. CreateAtom and CreateScopeUnit are explicit logical creation operations. Workflows **must** express these operations in Atom and Scope Unit terms; storage connectors own the private mapping to Markdown, TOML, files, database records or another backend. Workflows bind the coherent logical connector interface, not paths, tables or backend query languages. A storage-backend change replaces the connector implementation or binding without changing Workflow meaning or sequence. An earlier Find or Read result does not grant effect permission.

Finders, including `ATOM_SEARCH` **and** `ATOM_READ`, are strictly read-only. Doers default **to** dry run **and** require explicit authorized application. **Each** Atom Action **must** affect **`=1`** explicit Atom target. A Workflow selecting several targets **must** invoke independent Atom Actions, stop at the first failed Action, retain completed Actions, and leave the remaining targets untouched. The Workflow **must not** promise a cross-Atom all-or-nothing transaction. This boundary preserves each Action's own preconditions, source checks and storage-effect safeguards; it does not weaken them.

Every actual changed same-ID Atom update, including Status-only and carrier-only edits, **must** advance Version by **`=1`** and use actual Updated At; a verified no-op changes neither. Every Summary or Type value change **must** use replacement with a new Atom ID and predecessor archival. Atom removal **must** use the applicable retire or archive lifecycle transition and preserve required history; Atom deletion is not admitted. General file cleanup belongs to a separate operation and is not implied by an Atom operation. Resume and retry policy for the independent Action sequence is deferred; this Requirement selects no such policy. This required Engine contract does not establish implementation or acceptance; alignment of differing legacy Core content remains separate.

`ATOM_ARCHIVE`, `ATOM_PROMOTE`, **and** `ATOM_UPGRADE` are distinct transitions. archive preserves the assigned Atom ID **and** historical carrier. promotion assigns an operator-supplied role-matching Atom ID **to** a draft **and** makes it active. upgrade preserves an active Atom ID, requires an explicit enabled target Tier of `core` **or** `standard` that is higher than the source Tier, **and** **may** move the Atom **only** **to** an explicitly named ancestor Scope Unit.

## Details

### Named direct Subject preparation boundary

ATOM_UPDATE's direct preview_subjects and stage_subjects operations under CA-R-866, CA-M-371, CA-D-425 and CA-O-030 may run without an enclosing lifecycle Workflow. Their existing Workflow semantic policy owner is unchanged. They are preparation Tool calls, not executions of an Atom-update Action: preview is zero-write; an explicit stage request permits only fresh derived candidates and a manifest in the fixed Project scratch location. They create no Session, Action Run, authoritative Artifact change or canonical Journal record. Actual enclosing-Step Tool-call recording remains required.

This named boundary preserves the existing local scratch policy, not a general exemption for Artifact changes or Action recording. It admits no connector Modify, source/history writes, generic direct Doer application, promotion or publication. Existing selected update_atom and every publication/recording safeguard remain unchanged; descriptors and prepared artifacts do not grant effect permission.
