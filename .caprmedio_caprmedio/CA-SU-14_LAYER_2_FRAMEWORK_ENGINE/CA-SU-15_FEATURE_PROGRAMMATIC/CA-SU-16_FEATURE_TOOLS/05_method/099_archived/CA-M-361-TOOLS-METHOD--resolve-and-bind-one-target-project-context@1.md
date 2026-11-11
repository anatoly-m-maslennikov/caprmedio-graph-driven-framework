---
atom_id: CA-M-361
content_role: Method
current_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-09 16:24:06 +0400"
subjects:
  governs: "Framework Installation contribution/Target resolution"
  depends_on: [Tool, Project, Project Structure, Settings, Registry]
relations:
  method_for: [CA-R-1906, CA-R-1907, CA-R-1918]
---
# Summary

Resolve and bind one target-Project context

## Scope

the bootstrap, adoption and relocation resolution procedure for one target Project.

## Claim

the INSTALL_TOOLS facade **must** resolve and digest exactly supplied target controls **before** state staging, and **must not** infer missing Project identity or Operator intent.

## Details

1. Read supplied target root, control child, mode, settings, Structure and registry; distinguish non-git, sibling-project and relocation topology.
2. Reopen and digest all controls into CA-D-600; link relocation to its predecessor only after identity revalidation.
3. For first activation, verify the runtime selector, runtime state and public Skill boundary are empty; adoption permits metadata only.
4. Acquire the target lock after successful context binding. Changed, ambiguous or existing-active-runtime inputs refuse without effects.
