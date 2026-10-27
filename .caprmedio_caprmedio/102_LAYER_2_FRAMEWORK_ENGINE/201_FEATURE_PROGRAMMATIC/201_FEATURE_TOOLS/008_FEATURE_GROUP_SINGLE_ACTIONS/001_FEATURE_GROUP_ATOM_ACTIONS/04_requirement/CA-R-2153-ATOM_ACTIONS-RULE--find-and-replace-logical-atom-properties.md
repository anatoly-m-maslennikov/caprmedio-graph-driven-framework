---
atom_id: CA-R-2153
content_role: Requirement
type: Rule
current_scope_unit: ATOM_ACTIONS
status: Active
tier: 1
version: 4
updated_at: 2026-10-27 06:04:45 +0400
author: Anatoly Maslennikov
subjects:
  governs: Subject/Graph Node/Engineering/Data Handling/Data Validation
  depends_on:
  - Subject/Graph Node/Domain/Continuant/Atom
relations: {}
---
# Summary

Find and replace logical Atom Properties

## Scope

The Atom Find and Update interface. Target Atoms belong to the explicitly selected Scope and lifecycle frontier, not necessarily to the Tool's own Scope Unit.

## Claim

Find and replace **must** target admitted logical Atom Properties, including Markdown content sections, rather than unrestricted file text.

- Find **must** accept explicit Property paths and conjunctive conditions for Content Role, Type, Scope Unit and other admitted Property values. All supplied conditions combine with **AND**. Examples include `subjects.governs`, `subjects.depends_on`, `type`, `content.summary`, `content.substance`, `content.semantics` and `content.details`; these examples are not a closed Property list.
- A local Scope selection **must** match only the Atom's direct Local Scope Unit. A full selection **must** include the selected Scope Unit and its declared descendants. It **must not** add ancestors or siblings. Descendants come from Project Structure parentage, not directory-prefix matching. An explicitly selected Project-wide frontier is valid; implicit widening is not.
- Find **must** use the existing literal exact, prefix, suffix and contains matching where compatible with the selected value. Missing optional Properties are non-matches. Unknown paths, unreadable selected values or ambiguous sections **must** produce an explicit error or incomplete result, not invented matches.
- Find, Check and Change **must** remain separate Single Actions. Find returns explicit matching Atom identities and selected current values without mutating them or silently running a full Atom Check. Find **must not** widen its frontier or read unrelated Substance to infer a match.
- Text replacement **must** replace all occurrences of a nonempty literal search text inside the explicitly selected String value, String collection members or content section. It **must not** use regex, AI inference or unrestricted file replacement. Other value kinds use the existing explicit whole-value Update; they are not silently converted to text.
- Each Update **must** receive the exact Atom identity, expected current state, logical Property or section, full old value and full computed new value. Existing list-member or complete-set rules apply; caller indexes are not selectors. Unselected Properties, sections and collection entries **must** remain unchanged.
- Summary and Type changes **must** use the existing fresh-ID replacement path. Status changes **must** use Update and its existing cascade. Managed identity, Version and Updated At **must not** be changed through raw text replacement. Other changes and no-ops follow existing Version, timestamp and predecessor-archive rules.
- A batch **must** contain explicit finite targets and process its Single Actions in the supplied order. On the first failed or uncertain action it **must** stop, keep earlier completed effects and leave later targets untouched. This capability **must not** add per-Atom reports or confirmations, a new approval layer, a Journal-history gate, automatic retargeting or cross-Atom rollback.

## Details

Find supplies the selected current values. Literal replacement computes the full new values. Existing Property or section Update then receives those old/new pairs; no new connector effect schema or Property registry is required.

Existing contracts describe the components: CA-R-1067 and CA-R-863 for Find; CA-R-1933 and CA-R-1934 for section and Property edits; CA-D-623 for logical old/new deltas; CA-O-030, CA-O-202 and CA-O-208 for Update and independent batch progression. These contextual references do not invent cross-Scope governing relations.
