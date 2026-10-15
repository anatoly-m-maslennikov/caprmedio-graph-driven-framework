---
atom_id: CA-R-1913
content_role: Requirement
current_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-09 16:24:06 +0400"
subjects:
  governs: "Framework Installation contribution/Runtime process proof"
  depends_on: [Tool, Runtime, Command, Framework Package, Process]
relations:
  relates_to: [CA-D-604, CA-E-607]
---
# Summary

Prove runtime processes by generation, command and release

## Scope

the identity evidence for a process using an installed runtime.

## Claim

the INSTALL_TOOLS facade **must** prove a runtime process with generation, command and release bindings, and **must not** accept PID alone as proof of ownership, liveness or safe quiescence.

## Details

The proof joins target context, package and version digests, source catalog, Full Gate receipt, image, selector, wrapper, environment, command and invocation nonce. A PID and start token may supplement this evidence but never replace it. Changed or absent bindings make the process unsafe for switch, cleanup or recovery.
