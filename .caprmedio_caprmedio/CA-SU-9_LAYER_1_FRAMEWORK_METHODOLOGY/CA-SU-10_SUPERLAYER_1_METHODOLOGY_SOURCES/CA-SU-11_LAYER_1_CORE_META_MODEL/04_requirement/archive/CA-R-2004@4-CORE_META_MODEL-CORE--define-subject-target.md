---
subjects:
  governs: Subject/Domain/Node/Continuant/Atom.Subjects
  depends_on:
  - Subject
atom_id: CA-R-2004@4
content_role: Requirement
type: Definition
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
version: 4
updated_at: 2026-10-24 00:38:25 +0400
author: Anatoly Maslennikov
relations: {}
tier: 1
---
# Summary

Define Subject Target

## Scope

a direct GOVERNS or DEPENDS_ON target in an Atom's Subjects.

## Claim

a Subject Target **means** the topic addressed by a canonical Subject expression. its full path starts at Subject. a Subject can identify a kind, a dependent property, an allowed value or a named instance; it need not identify an independently carried object.

## Details

Subject says what an Atom concerns. Content Role says what its content does. They are independent by definition. An Atom of any RMED Role can govern a Domain topic, an Engineering topic or a global Graph topic. A topic about how work is performed does not require a separate Method root.

The Subject does not repeat or assign the Atom's Local Scope Unit, folder or Carrier. Topic meanings come from source use and Semantics; the Terms Graph derives definitions from those cases rather than creating another authority layer.
