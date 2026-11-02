---
subjects:
  governs: Subject/Domain/Node/Continuant/Atom.Type
  depends_on: []
version: 24
updated_at: 2026-10-24 10:48:25 +0400
relations: {}
atom_id: CA-R-1700@24
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
type: Rule
tier: 1
---
# Summary

Admit Atoms only where a role has an atomic unit

## Scope

Content Role Type admission.

## Claim

a Content Role admits a Type value for an Atom **only** **when** that role has an independently governed atomic unit that benefits from stable identity, admission, **and** whole-unit lifecycle; CAPRMEDIO **must not** create a placeholder Type value merely **to** fill a semantic coordinate.

## Details

Every Current Atom has exactly one substantive admitted Type under its Content Role. A Draft Atom may remain incomplete while being authored. A Type value must not be invented merely to fill a semantic coordinate, and a Content Role name must not be copied as a Type value. This rule does not constrain Type values to a particular local tier. General-name Type fields whose admission or full Subject path is not established remain uncovered and held; this rule does not claim that all Subject paths are complete.
