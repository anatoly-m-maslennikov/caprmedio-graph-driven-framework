---
atom_id: CA-R-1849
content_role: Requirement
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
status: Active
author: Anatoly Maslennikov
version: 9
updated_at: 2026-10-27 06:04:45 +0400
subjects:
  governs: Subject/Graph Node/Domain/Continuant/Selection
  depends_on:
  - Subject/Graph Node/Domain/Continuant/Atom
  - 'Subject/Graph Node/Carrier/File.Format: Markdown'
  - Subject/Graph Node/Domain/Continuant/History/Journal
relations: {}
type: Rule
tier: 3
---
# Summary

Query and fetch Markdown Artifacts read-only

## Scope

The future `FIND_AND_FETCH_ARTIFACTS` Tool at
`102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/FIND_AND_FETCH_ARTIFACTS/`.
Its golden test is
`102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/FIND_AND_FETCH_ARTIFACTS/tests/test_find_and_fetch_artifacts.py`.

## Claim

FIND_AND_FETCH_ARTIFACTS **must** implement CA-O-158 through CA-O-160 as one
source-snapshot-stable, bounded, read-only Markdown query: it applies the
shared CA-R-1850 filter contract to every frontmatter and heading/section
property, defaults to canonical Artifact identities (`atom_id` for Atoms and
`artifact_id` for other Markdown Artifacts), fetches only caller-selected
fields/sections, preserves all caller-selected statuses/properties, and returns
explicit diagnostics instead of identity inference, secret access, mutation, or
a fictitious Run.

## Details

The Tool must use CA-R-1850 and CA-O-159's namespaces, RFC 6901 addressing,
JSON literals, collision, null/missing, identity uniqueness, single retained
snapshot ownership, coverage, cursor, and configurable budget rules exactly. It rejects malformed
or incomplete source input and invalid filters without an accepted partial
result. The pure native Tool creates no Run or Journal format. An actual
admitted selected Action/Workflow uses the existing RUN_SUPPORT and Work
Journal library of CA-D-527, CA-D-528, and CA-D-529; its query execution record
cannot alter or enlarge the captured source snapshot.
