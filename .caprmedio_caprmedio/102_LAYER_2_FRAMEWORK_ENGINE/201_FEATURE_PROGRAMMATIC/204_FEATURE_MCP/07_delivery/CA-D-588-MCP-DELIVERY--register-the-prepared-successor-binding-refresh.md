---
atom_id: CA-D-588
content_role: Delivery
current_scope_unit: MCP
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 2
updated_at: "2026-10-10 07:11:33 +0400"
subjects:
  governs: "MCP/selected source pin refresh"
  depends_on: [MCP, Projection, Workflow, Action, Operator, Journal, Atom, Source Carrier]
relations:
  relates_to: [CA-P-1866, CA-D-572]
---
# Summary

Register the prepared successor binding refresh

## Scope

the exact admitted selected-source revision refresh under the current Epic.

## Claim

the selected-source refresh registration **must** use the closed serialization below for this exact prepared-successor authority revision.

## Details

The only current registration is the JSON object under `### Accepted source revision`. Its keys, replacement rows and nested pin shapes are exact; duplicate or unknown fields are invalid. Versions, occurrence counts and schema version are strict integers. Paths are safe regular Project-relative carriers with no symlink ancestry.

The exact input binding bytes, both prior Action archives and both current Active Action sources must match their registered identities, versions and raw-byte digests. Each replacement occurs at exactly the two named structural positions in its one named route. The four replacements repair only CA-O-134 and CA-O-137; no other non-Release pin or route field is replaced.

The same candidate includes the current `release_version` route and its sole source admission, freshly derived from current CA-D-572 authority and its actual declared source/private carriers. Missing or stale Release authority stops derivation. A non-Release-only intermediate is never published. After composition, recalculate both derived digests and validate all 16 routes and current source pins before any write.

The private reader is `102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/204_MCP/selected_source_refresh.py`. It feeds the existing `release_manifest_publisher.py` refresh boundary, trusted Operator context, intent, atomic write, readback and Journal receipt. No new public MCP route or caller-supplied registration is introduced. Historical schema-1 fixtures may reopen the archived authority; they do not admit the current Project's different input bytes.

### Accepted source revision

```json
{
  "schema_version": 2,
  "registration_id": "epic1848-graph-successors-release-frontier-20261010",
  "authorization_ref": ".caprmedio_caprmedio/03_plan/17-CA-P-1848-EPIC--unify-installation-and-local-public-release-cycles.md",
  "repair_task_id": "CA-P-1866",
  "input_manifest_ref": ".caprmedio_caprmedio/_projection/selected_workflow_bindings.json",
  "input_manifest_sha256": "dc75baa2d7748ced0683067e5de0047b09bc990b842355334cc877e7f6df4839",
  "input_canonical_manifest_sha256": "f944ead9f582956a1d74b6cbe07255d09586ddb13cb7ef01687992bc1a23a8f5",
  "pin_occurrences": 4,
  "replacements": [
    {
      "route": "build_entities_graph",
      "occurrences": [
        "ordered_steps[0].action",
        "ordered_actions[0]"
      ],
      "prior_pin": {
        "atom_id": "CA-O-134",
        "version": 2,
        "source_path": ".caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/09_operations/CA-O-134-CORE_META_MODEL-ACTION--construct-entities-graph-projection.md",
        "digest": "b94eebdd85eab9f7080680e85999c68022e82cdfa7945bf0d840b429ebad037a"
      },
      "prior_archive_path": ".caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/09_operations/archive/CA-O-134-CORE_META_MODEL-ACTION--construct-entities-graph-projection@2.md",
      "current_pin": {
        "atom_id": "CA-O-134",
        "version": 3,
        "source_path": ".caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/09_operations/CA-O-134-CORE_META_MODEL-ACTION--construct-entities-graph-projection.md",
        "digest": "8a3dcb7cfdb3369ec268726cc54f3f0e0c1bfbc947841792deb87bb844245414"
      }
    },
    {
      "route": "build_terms_graph",
      "occurrences": [
        "ordered_steps[0].action",
        "ordered_actions[0]"
      ],
      "prior_pin": {
        "atom_id": "CA-O-137",
        "version": 2,
        "source_path": ".caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/09_operations/CA-O-137-CORE_META_MODEL-ACTION--construct-terms-graph-projection.md",
        "digest": "6c154852b99df16961fe63c8fd869dbf86f8d75ecc950b25b189e41c3c1c5dad"
      },
      "prior_archive_path": ".caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/09_operations/archive/CA-O-137-CORE_META_MODEL-ACTION--construct-terms-graph-projection@2.md",
      "current_pin": {
        "atom_id": "CA-O-137",
        "version": 3,
        "source_path": ".caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/09_operations/CA-O-137-CORE_META_MODEL-ACTION--construct-terms-graph-projection.md",
        "digest": "8ea08ef172a82515db7f145bf642a3943ecc41fc6decf4a86a69bea78ce494fd"
      }
    }
  ],
  "release_frontier": {
    "authority_atom_id": "CA-D-572",
    "route": "release_version",
    "admission_occurrences": 1
  }
}
```
