---
subjects:
  governs: "Subject/Domain/Node/Continuant/Atom.Local Tier"
  depends_on:
    ["Subject/Domain/Node/Continuant/Atom", "Subject/Domain/Node/Continuant/Atom/Content Role: Requirement/Type: Goal", "Subject/Domain/Node/Continuant/Project", "Subject/Domain/Node/Continuant/Atom.Local Tier: Principle", "Subject/Domain/Node/Continuant/Atom.Local Tier: Core", "Subject/Domain/Node/Continuant/Atom.Local Tier: General", "Subject/Domain/Node/Continuant/Atom.Local Tier: Standard"]
version: 35
updated_at: "2026-10-22 16:27:26 +0000"
relations: {}
atom_id: "CA-R-155@35"
content_role: "Requirement"
type: "Rule"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Archived"
author: "Anatoly Maslennikov"
global_tier: 9
---
# Summary
Give Every Non-Project-Goal Atom One Local Tier

## Scope
Atom other than a Project Goal Atom.

## Claim

**every** non-Project-Goal Atom **must** have **`=1`** Local Tier **in** (Principle, Core, General, Standard). A Project Goal instead has exactly one Local Tier whose value is `Project Goal`, under CA-R-2101. This distinction does not impose arbitrary Type-to-tier restrictions beyond the applicable tier authority.

## Details
