---
atom_id: CA-O-046
content_role: Operations
type: Action
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
author: Anatoly Maslennikov
status: Active
cce_version: cce_1
cce_form: definition
subjects:
  governs: "Search Atom Carriers"
  depends_on:
    - "Action"
    - "Tool/ATOM_SEARCH"
    - "Atom"
    - "Artifact/Carrier"
    - "Scope Unit"
version: 7
updated_at: "2026-10-12 23:17:22 +0400"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations: {}
---
# Summary

Search CAPRMEDIO Atom carriers

## Operation

Search Atom Carriers **means** the reusable read-only Action that returns the complete logical Atom match set for one declared Scope Unit frontier and explicit search request under CA-R-863. It does not require a subsequent Read or Modify Workflow, and neither reading complete Atoms nor changing them is an implicit result of discovery.

## Details

### Steps

1. resolve the requested declared Scope Unit identities and logical filters. Public filters concern Atom identity, Content Role, Type, Status, Properties and Subjects; storage paths, filename patterns and body-byte locators remain private. Apply every supplied filter conjunctively and reject unknown or malformed modes.
2. enumerate only authoritative Atom candidates within the declared frontier. Honor the explicitly selected lifecycle filter; an Active default view does not define currentness. Distinguish current non-archived originals, Drafts, archived history, delivered copies, Projections and non-Atom content. Report invalid or unreadable sources instead of silently treating them as non-matches.
3. for Subject matching select `governs`, `depends_on` or both and one explicit ordinary match mode: exact, prefix, suffix or contains. Exact matches the complete value; prefix matches only at the selected profile's lexical delimiter boundaries; suffix matches the literal end of the complete scalar value, without a delimiter-boundary requirement; contains is literal containment and implies no ontology or relation. Do not infer a profile, target meaning or selector instance.
4. resolve `subject_profile`: omission selects legacy, approved is explicit, and invalid profiles fail. Reuse the current grammar authority, preserve Atom/atom case distinction and reject unsupported syntax. Require flat scalar Subject fields and refuse malformed, ambiguous, symlinked or duplicate-dependency sources without repair.
5. return every and only matching Atom by ID and Version, its owning Scope Unit and the requested matched Properties or Subject values, with attributable completeness and private source/profile evidence. Dependency positions may be private evidence, never public target selectors. Stable logical ordering and explicit invalid/partial outcomes preserve the declared search frontier.
6. perform no mutation, repair, lifecycle transition, replacement, reference retargeting or Projection rebuild.

### Outcome

A successful result is the complete empty, singular or multiple logical match set within the requested frontier. A failed or incomplete discovery is not authority to guess the missing membership or execute a change. Find-reference use selects its explicit reference criterion and returns matching owning Atoms; it does not change references or automatically run O202. No native admission, runtime activation or migration effect is claimed.
