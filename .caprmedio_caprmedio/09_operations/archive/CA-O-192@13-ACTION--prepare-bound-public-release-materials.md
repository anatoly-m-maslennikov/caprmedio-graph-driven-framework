---
atom_id: CA-O-192@13
content_role: Operations
type: Action
current_scope_unit: caprmedio
status: Archived
author: Anatoly Maslennikov
subjects:
  governs: 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations/Type: Action//Prepare bound public release materials'
  depends_on:
  - Subject/Graph Node/Documentation
  - Subject/Graph Node/Engineering/Pull Request
  - Subject/Graph Node/Engineering/Release/Version History
  - Subject/Graph Node/Domain/Occurrent/Execution
  - Subject/Graph Node/Engineering/Release Version
version: 13
updated_at: 2026-10-26 05:59:45 +0400
relations: {}
tier: 3
---
# Summary

Prepare bound public-release materials

## Action

Prepare bound public-release materials **means** the sole content prompt for one selected Version and source snapshot. It returns the full public PR body and concise Version History summary.

## Details

The PR body distinguishes What’s new and What’s fixed. README, Version History edits, and all remote effects are mechanical later work. If the actual URL is not yet known, CA-O-198 appends it after PR creation; no placeholder is valid. A different Version or changed code, Methodology, or package requires a fresh full suite before public release.
