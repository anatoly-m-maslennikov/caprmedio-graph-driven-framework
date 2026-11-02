---
atom_id: CA-C-560
content_role: Concern
type: Problem
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
local_tier: Standard
global_tier: 8
author: Anatoly Maslennikov
status: Resolved
priority: high
subjects:
  governs: Entity/Node/Continuant/Implementation
  depends_on: []
relations:
  concern_about: [CA-P-2518, CA-P-2520, CA-R-1901]
version: 2
updated_at: "2026-10-21T09:42:22Z"
---
# Summary

Name CAPRMEDIO images with verified version and build date

## Concern

Canonical CAPRMEDIO image builds capture immutable IDs and labels but do not assign readable repository names or version/build-date tags. Docker Desktop therefore displays none for both fields, including the installed healthy MCP image.

## Evidences

Read-only Docker inventory on desktop-linux found29images with org.caprmedio.runtime.schema=1, all RepoTags empty. Current image sha256:08f26a9b8b14b6884fb6a8011264ea2e7c99a12f687377c355e50b34c2e4f929 is running healthy. Canonical runtime_images._build uses iidfile/labels without a tag; legacy Runtime.build separately emits only a mutable local alias. Eleven historical/current images currently have version proof via their source-head label and exact version.toml; eighteen lack verified version evidence. Docker Created is descriptive timestamp evidence, not proof that every source/checkout byte was included.

Native create was attempted once and stopped before publication at its final Project-boundary recheck because the read-I/O timeout budget expired. Exact target absence and unused identity were checked before this Operator-authorized manual save. This is not a passed native admission receipt; the separate bounded admission-performance Problem is C561.

## Blast radius

P2518–P2521 own the Operator-prioritized fix, consistent regression coverage, additive exact-image maintenance and acceptance before recursive-container continuation. Preserve immutable SHA/fingerprint/platform/Project admission, occupied tags, existing containers and unknown historical version evidence. No guessed version/date, deletion/prune, tag movement, runtime restart/replacement, new release or production mutation test is authorized. R1901@4/M356@4/D594@6/E600@5 encode the adopted display-only metadata permission. C555/C545 and other lifecycle Problems remain separate.

### Resolution evidence

P2518/P2522 source accepted;109root focused tests and actual isolated canonicalbuild/same-IDreuse pass. All11historical source-proven images plus1newbuild are named caprmedio-runtime with exact version/DockerCreatedUTC/sha12 tags. Approved18unknown-versionimages+6stoppedtestcontainers removed, then separately approved696-byte image27b9017daa69 removed non-force after fresh metadata/no-reference checks. Final fresh readback:12CAPRMEDIO images, allnamed, no unnamed; original e812container/08fimage unchangedhealthy. No version/date guessed; no release/deployment/restart. ExactIDs/actualreceipts retained in Journal event4ad64079-e23e-431b-93c5-02063dae88c7; final additional deletion recorded separately. C561/C562/C555/C545 remain independent open issues; this bounded naming defect is resolved, not all runtime issues.
