---
atom_id: CA-O-164
content_role: Operations
type: Workflow
current_scope_unit: PROJECT_CONFIGURATION
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
subjects:
  governs: "Release selected Framework Version"
  depends_on: [Workflow, Step, Action, Operator, Version, Methodology, Implementation, Skill, Test, Docker Image, Journal]
version: 8
updated_at: "2026-10-09 16:36:54 +0400"
relations:
  relates_to: [CA-O-011, CA-O-025, CA-O-165, CA-O-166, CA-O-167, CA-O-168, CA-O-169, CA-O-181, CA-O-183, CA-R-1525, CA-R-1720]
---
# Summary

Release a selected Framework Version

## Operation

Release selected Framework Version **means** the Operator-invoked, non-recursive Workflow that releases one frozen executing Framework/Methodology Version N by building and proving separately pinned candidate Version N+1. The current N definitions, source frontier, runtime and rollback evidence remain fixed for this Run; candidate N+1 never becomes this Workflow's definition or input authority mid-Run.

## Scope

The selected boundary binds one current N, one distinct candidate N+1, their exact source revisions and digests, canonical `version.toml` Version value and carrier-byte SHA-256, selected extension/configuration revisions from one admitted pinned available catalog, lock identity, complete active-source delivery, selected-snapshot compiler Tool boundary, Projection and runtime/package delivery contracts, the complete hook-free project-local `ca` Skill directory target `.agents/skills/ca`, full test declaration, candidate image identity, selected prior-image identity, permissions, recovery policy and Journal capability. **Only** selected active authoring Sources and admitted support artifacts enter the sealed private `.caprmedio_tmp/release_candidates/<run_id>/methodology/` export, whose logical root-delivery mapping is `methodology/`; it is not a live root delivery before the gate. After the gate CA-O-169 promotes those same sealed bytes to root `methodology/`, then carries the sealed source copy and compiled projection to the selected Project's installed `.caprmedio_<project>/000_CAPRMEDIO_framework` control tree. None becomes a second editable authority. Candidate compilation, package construction and image construction occur only under `.caprmedio_tmp/release_candidates/<run_id>/`. The reusable beta release is admitted only at `.caprmedio_install/releases/<package_manifest_sha256>/` with `.caprmedio_install/current.toml`; the selected Project's state, environment and selected-package binding are only under `.caprmedio_runtime/installation/current.toml`. No path, compiler layout, client target, image, tag, permission, secret or rollback point is inferred.

## Steps

| Step | Action | Bound phase |
| --- | --- | --- |
| CA-O-170 | CA-O-165 | freeze |
| CA-O-171 | CA-O-165 | validate |
| CA-O-172 | CA-O-166 | deliver_sources |
| CA-O-173 | CA-O-166 | compile |
| CA-O-185 | CA-O-168 | closed_unit_gate |
| CA-O-175 | CA-O-167 | stage_candidate |
| CA-O-176 | CA-O-168 | candidate_image_build |
| CA-O-186 | CA-O-168 | candidate_image_canary |
| CA-O-182 | CA-O-181 | host_candidate_e2e |
| CA-O-184 | CA-O-183 | aggregate_full_gate |
| CA-O-178 | CA-O-169 | promote |
| CA-O-179 | CA-O-169 | retire |

## Transitions

| Step result | Next step or outcome |
| --- | --- |
| CA-O-170 complete frozen N and candidate N+1 boundary | CA-O-171 |
| CA-O-171 complete exact delivery, compiler, package, Skill, test, image and Journal bindings | CA-O-172 |
| CA-O-172 complete sealed private candidate source export | CA-O-173 |
| CA-O-173 complete compilation from the sealed candidate frontier | CA-O-185 |
| CA-O-185 closed declared unit gate passed for that exact compiled candidate | CA-O-175 |
| CA-O-175 complete non-active candidate runtime/package and Skill staging | CA-O-176 |
| CA-O-176 exact candidate image built | CA-O-186 |
| CA-O-186 exact candidate image canary passed | CA-O-182 |
| CA-O-182 host-capable Candidate E2E passed | CA-O-184 |
| CA-O-184 complete bound Full Gate aggregate passed | CA-O-178 |
| CA-O-178 complete support-owned quiesce/state migration and exact N+1 runtime and project-local Skill promotion | CA-O-179 |
| CA-O-179 complete exact prior N-image disposition | complete |
| any missing, stale, unauthorized, failed, partial, recording-blocked, unsafe, or unmatched result | stop with its actual evidence; do not promote, retire, retry, or recurse implicitly |

## Details

CA-O-164 uses only its listed Step Atoms; it does not invoke another Workflow as a Step or invoke itself to prove a candidate. CA-O-011 remains the canonical Applicable Methodology compilation authority for declared Methodology Sources. The separately pinned candidate snapshot is sealed before compilation; its definitions, source/configuration/catalog/lock identity and byte identities **must not** change mid-Run. It may materialize only the sealed private candidate export and compilation; root `methodology/` and the installed Project control tree remain unchanged until the complete gate. After that gate, CA-O-169 promotes those same sealed source-export, source-copy, compiled, package and image bytes; it does not rebuild, re-export or recompile them. Neither delivery is a replacement authoring authority. CA-O-025 remains release readiness and is not substituted for this boundary. The final completion label is `exact prior N-image disposition`. Under a sealed `retain_prior` condition, it is complete only with an actual Docker-subprocess, SHA-256-valid retention receipt bound to the exact sealed condition reference and settings digest, that observes the exact required prior image, has `retaining_container_refs == ()`, and has no removal fields; retained is not labeled retired. A used, unavailable, unverified, mismatched or non-exact prior image remains partial with its actual evidence. Actual retirement remains pending until its separate exact removal effect has a canonical Journal record. The schema-V5 Journal retains only Workflow, Step and Action Runs with their exact definition revisions, inputs, parent lineage, start/terminal outcome, results and effects; Tool-call evidence attaches by evidence references and parentage and **must not** create a Tool Run type. Preview, rejection and a missing recording receipt never manufacture a Run or release success. This is a local-release Workflow: it grants no Git, public-release, publication, source mutation, arbitrary-worker termination, credential or retry authority.
