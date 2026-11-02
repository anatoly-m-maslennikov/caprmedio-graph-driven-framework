---
subjects:
  governs: "tool-authority"
  depends_on:
    - "artifact-operations"
    - "mcp"
cce_version: cce_1
cce_form: obligation
version: 10
updated_at: "2026-10-12 23:13:45 +0400"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Summary

Separate generic and Atom-specific Tool authority

## Scope

Semantic operation ownership and logical operation/storage connector boundaries for Atom and Scope Unit Workflows.

## Claim

**every** public Tool operation **must** have **=1** semantic behavior owner. a generic Artifact Tool owns **only** artifact-form-agnostic carrier mechanics **and** contracts. it **must not** define CAPRMEDIO Markdown Atom identity, admission, authority, lifecycle-transition, **or** target-effect semantics. a CAPRMEDIO Markdown Atom Tool owns those semantics for its named Atom operation **and** **may** use a generic Artifact Tool **only** as an internal helper.

MCP owns discovery, projection, transport validation, request forwarding, **and** result transport. it **must** delegate **to** the canonical Tool **and** **must not** resolve an Atom target, reinterpret a Tool contract, decide a mutation, mutate a carrier, **or** recover an effect. a CAPRMEDIO Markdown Atom Doer's `--apply` entry point is callable **only** through an authorized project-local MCP delegation; direct execution **may** produce a mutation-free dry run but **must** reject `--apply`.

Find, Read and Modify **must** be independent logical operations. Find returns matching Atom or Scope Unit identities and matching facts; Read obtains the complete explicitly selected source with its exact identity and Version or revision; Modify accepts explicit targets and does not silently Find or replace them. CreateAtom and CreateScopeUnit are explicit logical creation operations. Workflows **must** express these operations in Atom and Scope Unit terms; storage connectors own the mapping to Markdown, TOML, files and locations. An earlier Find or Read result does not grant effect permission.

Finders, including `ATOM_SEARCH` **and** `ATOM_READ`, are strictly read-only. Doers default **to** dry run **and** require explicit authorized application. **Each** Atom Action **must** affect **`=1`** explicit Atom target. A Workflow selecting several targets **must** invoke independent Atom Actions, stop at the first failed Action, retain completed Actions, and leave the remaining targets untouched. The Workflow **must not** promise a cross-Atom all-or-nothing transaction. This boundary preserves each Action's own preconditions, source checks and storage-effect safeguards; it does not weaken them.

Every actual changed same-ID Atom update, including Status-only and carrier-only edits, **must** advance Version by **`=1`** and use actual Updated At; a verified no-op changes neither. Every Summary or Type value change **must** use replacement with a new Atom ID and predecessor archival. Atom removal **must** use the applicable retire or archive lifecycle transition and preserve required history; Atom deletion is not admitted. General file cleanup belongs to a separate operation and is not implied by an Atom operation. Resume and retry policy for the independent Action sequence is deferred; this Requirement selects no such policy. This required Engine contract does not establish implementation or acceptance; alignment of differing legacy Core content remains separate.

`ATOM_ARCHIVE`, `ATOM_PROMOTE`, **and** `ATOM_UPGRADE` are distinct transitions. archive preserves the assigned Atom ID **and** historical carrier. promotion assigns an operator-supplied role-matching Atom ID **to** a draft **and** makes it active. upgrade preserves an active Atom ID, requires an explicit enabled target Tier of `core` **or** `standard` that is higher than the source Tier, **and** **may** move the Atom **only** **to** an explicitly named ancestor Scope Unit.

## Details
