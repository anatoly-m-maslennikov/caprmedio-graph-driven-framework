---
subjects:
  governs: "Subject/Domain/Node/Continuant/Atom.Subjects"
  depends_on:
    - "Subject"
atom_id: "CA-R-2004@2"
content_role: "Requirement"
type: "Definition"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Archived"
version: 2
updated_at: "2026-10-22 16:26:09 +0000"
author: "Anatoly Maslennikov"
global_tier: 9
relations: {}
---
# Summary

Define Subject Target

## Scope

a direct GOVERNS or DEPENDS_ON target in an Atom's Subjects.

## Claim

a Subject Target **means** the topic addressed by a canonical Subject expression. its full path starts at Subject. a Subject can identify a kind, a dependent property, an allowed value or a named instance; it need not identify an independently carried object.

## Details

Subject says what an Atom concerns. Content Role says what its content does. A Method Atom can govern a Domain topic, an Engineering topic or a Graph topic. A topic about how work is performed does not require a separate Method root.

The Subject does not repeat or assign the Atom's Local Scope Unit, folder or Carrier. Topic meanings come from source use and Semantics; the Terms Graph derives definitions from those cases rather than creating another authority layer.
