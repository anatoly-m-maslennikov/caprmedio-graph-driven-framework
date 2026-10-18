---
atom_id: "CA-O-160"
content_role: "Operations"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
global_tier: 11
status: "Active"
author: "Anatoly Maslennikov"
type: "Step"
version: 3
updated_at: "2026-10-15 18:53:39 +0000"
subjects:
  governs: "Artifact query and fetch execution"
  depends_on: ["Entity/Continuant/Object/Atom/Content Role: Operations/Type: Workflow", "Entity/Continuant/Object/Atom/Content Role: Operations/Type: Action", "Artifact", "Markdown", "Entity/Continuant/History/Journal"]
relations:
  part_of: [CA-O-158]
  invokes: [CA-O-159]
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/09_operations/CA-O-160-CORE_META_MODEL-STEP--run-the-artifact-query-and-fetch.md
  source_atom_id: CA-O-160
  source_atom_revision: 3
  source_sha256: 45304b375babe3f70e7141fe57f87b296afa6364d990f24e0784a58220c6857e
  original_relations_sha256: e21b741a859af8b94c5d0468112727616d8819fc53b5399c17403d15fb10fcf5
---
# Summary

Run the Artifact query and fetch

## Step

This Step **must** validate and forward the read-only request once to CA-O-159,
which alone enumerates, retains, validates, and reuses its source snapshot.

## Details

The Step returns CA-O-159's result without mutation, snapshot creation, or retry substitution. It
does not dispatch another Workflow, infer an ID from a filename, admit an
unselected source root, or write query results as a Projection. It passes an
actual execution through the shared RUN_SUPPORT/Work Journal contract only as
defined by CA-D-527, CA-D-528, and CA-D-529; preview and every rejected request
have no Run or Event identity.
