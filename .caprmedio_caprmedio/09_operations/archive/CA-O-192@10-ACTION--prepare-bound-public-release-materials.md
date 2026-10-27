---
atom_id: CA-O-192@10
content_role: Operations
type: Action
current_scope_unit: caprmedio
status: Archived
author: Anatoly Maslennikov
subjects:
  governs: 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Action//Prepare bound public release materials'
  depends_on:
  - Subject/Documentation/README
  - Subject/Engineering/Pull Request
  - Subject/Engineering/Release/Version History
  - Subject/Domain/Node/Occurrent/Execution
  - Subject/Engineering/Release Version
version: 10
updated_at: 2026-10-25 01:28:32 +0400
relations:
  relates_to:
  - CA-O-188
  - CA-O-191
  - CA-R-1922
  - CA-R-1923
  - CA-R-1928
tier: 3
---
# Summary

Prepare bound public-release materials

## Action

Prepare bound public-release materials **means** the sole content prompt for one selected Version and source snapshot. It returns the full public PR body and concise Version History summary.

## Details

The PR body distinguishes What’s new and What’s fixed. README, Version History edits, and all remote effects are mechanical later work. If the actual URL is not yet known, CA-O-198 appends it after PR creation; no placeholder is valid. A different Version or changed code, Methodology, or package requires a fresh full suite before public release.
