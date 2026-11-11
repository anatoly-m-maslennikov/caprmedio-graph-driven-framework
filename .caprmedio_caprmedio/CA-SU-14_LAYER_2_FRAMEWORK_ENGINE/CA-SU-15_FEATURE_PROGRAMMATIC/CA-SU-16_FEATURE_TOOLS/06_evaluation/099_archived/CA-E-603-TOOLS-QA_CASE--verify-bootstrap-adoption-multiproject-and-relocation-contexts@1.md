---
atom_id: CA-E-603
content_role: Evaluation
type: QA Case
current_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-09 16:24:06 +0400"
subjects:
  governs: "Framework Installation contribution/Target topology acceptance"
  depends_on: [Tool, Project, Project Structure, Settings, Registry]
relations:
  evaluation_for: [CA-R-1906, CA-R-1907, CA-M-361, CA-D-600]
---
# Summary

Verify bootstrap, adoption, multi-project and relocation contexts

## Scope

the target-context fixture matrix.

## Claim

the QA case **must** verify distinct bound contexts for bootstrap, metadata adoption, non-git, two-Project repository and relocation cases, and **must not** accept inferred target controls.

## Details

Each positive fixture reopens root/control child, settings, Structure and registry digests. Adoption succeeds only with an empty runtime boundary; non-git uses false repository identity; siblings have different context/locks; relocation links prior context without retaining old absolute root as identity. Missing, ambiguous, changed or active-runtime inputs refuse without state writes.
