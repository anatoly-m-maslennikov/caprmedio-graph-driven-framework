---
atom_id: CA-M-433@1-draft
content_role: Method
type: Eng Policy
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
tier: 1
status: Draft
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-23 18:22:28 +0400"
subjects:
  governs: "Subject/Engineering/Runtime Architecture"
  depends_on: []
---
# Summary

Separate Tool module responsibilities

## Scope

The agreed TOOLS module partition for new or changed PROGRAMMATIC Tool design.

## Claim

Keep TOOLS as one modular runtime with shared queue and run state under
CA-M-432. Partition responsibility into:

- `ADAPTERS`: backend access, including governing Configuration.
- `SINGLE_ACTIONS`: target-specific operations.
- `SCHEDULERS`: batch and Workflow scheduling driven by recorded results.
- `WORKFLOWS`: concrete O sequences.
- `ACTION_ENGINE`: queue consumption, execution, and result recording.

## Details

These are responsibility boundaries inside one modular runtime, not service
boundaries. Do not introduce microservices for them or add a separate prompt
helper for Find+Fetch. Project-specific Tools use the same responsibility
classification rather than a special umbrella. Existing contracts are not
relocated by this Method, and this Method makes no runtime-completion claim.
