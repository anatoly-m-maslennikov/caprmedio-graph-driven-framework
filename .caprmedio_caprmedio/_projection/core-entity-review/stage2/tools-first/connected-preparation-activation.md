# Connected Subject preparation activation

Derived evidence, 2026-10-14. This is not an Atom, source authority, migration approval or installed-package release receipt.

## Activation

The Operator approved replacing only this Project's MCP HTTP container from reviewed commit `15f9ce76e02b3e8cced1f2c41cc5b40c3a3c5a21`. The source was exported into an isolated scratch directory; unrelated working-tree edits were not included. Its committed ImageManager reproduced fingerprint `825fc6750665988b349347c827282c96f65ebdb48a8fdb72be545dc3bf23e1ab`.

The launcher admitted image `sha256:372c1d6e54dcf2fa7f33e75e87f2523635edcf796a0beb6cc39d0abc98c79804` before stopping the old endpoint. Fresh inspection confirmed the old container's exact Project labels, service, host-root mount and port. Only container `8b8ba8ccd7b0925fb1d01adeb28a7f47c3308d277bc62f517f7a66060cf2a996` was stopped and removed. Project files and the previous image were preserved; other services were untouched.

The same launcher with `--no-build --port 56317` returned READY_STARTED for container `bad58cffa71c307f9c5f3681f52af0aef9ad82c831feffafe59417c05aec6c89` and `http://127.0.0.1:56317/mcp`, with the admitted image and fingerprint. Actual Codex MCP discovery reports ATOM_UPDATE as mcp. Actual get_execution_context reports both ATOM_SEARCH and ATOM_UPDATE as mcp with context_complete true and their current canonical source pins. This proves connected image activation, not an installed-package upgrade or successful operation execution.

## Prepared request

CA-P-2381 is Done. Independent review verified the public request preserves all 611 owners, 848 ordered patches, exact source pins and existing exclusions. Four focused checks passed. Request SHA-256: `b78ec349a222f2b51c8cf62a80b42a7b829807a97e629275e9463133fe38d6aa`. The frozen original remains unchanged.

## Separate structural blocker

Current-carrier structural preflight passed 567 of 611 targets. Forty-four failed existing checks: 29 Operations parent/layout cases, one role-folder mismatch, five missing target-Scope properties, seven body-section cases and two unadmitted Delivery Types. Source hashes remained unchanged. These are validation refusals, not a semantic review or a reason to waive validation. The full request is not admitted merely because its mapping is complete.

The Operator has been asked whether to hold these 44 unchanged and stage only targets that pass actual MCP preview. No answer is inferred. Content and structural repair remain separate; actual preview, staging and live publication are not established by this receipt.

Evidence lives under `.caprmedio_tmp/stage2-migration-20261014/`: `tool-readiness/committed-activation-preflight.md`, `tool-readiness/structural-preflight/report.md`, `tool-readiness/structural-preflight/machine-failures.json`, and `public-request/independent-review.md`.

## Actual connected lookup and preview — 2026-10-14 11:39 +0400

The actual HTTP MCP client listed 35 Tools, including atom_search and atom_update. Both discover/context calls succeeded. One exact legacy lookup returned CA-D-253 v12 under CORE_META_MODEL with complete true and no errors. The approved-profile preview returned one changed Atom, no staging and no errors; its original bytes and mode remained unchanged. Preview seal: `ba718c8d430ccb7a88c141705019762aa24aa28257171fb37520bcf28e437d06`. Illustrative timestamp: `2026-10-14 07:33:11 +0000`. The proposed delta contains only Subjects and illustrative Version/time; the candidate is not a source update.

Full request/response/schema/source evidence: `activation/connected-d253-probe.json`, SHA-256 `8ef8bdce97ef8b9e9bea9998c49c222eeec60e2c4a8f42a396cfe21d848505b6`. Root independently inspected the actual responses. A fresh no-write request check again verified all 906 source pins and reproduced the same 611-owner/848-patch request and provenance hashes.

The permission reviewer denied the proposed one-Atom stage command before process or MCP invocation because explicit trusted approval for that scratch mutation was not established. No stage request ran and no staged candidate or manifest was produced. Do not retry or substitute another route without direct approval. CA-P-2382 remains Active; the batch disposition question remains unanswered.

The 44-item structural ledger also passed independent bounded review: exact unique/disjoint IDs and one actual source per category were checked. All five reproduced pre-existing refusals with unchanged frozen/HEAD bytes. The other 39 were not independently rerun. Report: `tool-readiness/structural-preflight/independent-review.md`, SHA-256 `a48ae8e9b4893119ef6cd0d0d4a86b2db82120bb2e4cbb33a51f5c75e86eca32`.

## Independent preview readback

The saved actual CA-D-253 preview passed independent review. The reviewer recomputed both the preview and intent seals, checked strict request/result DTOs and text/structured parity, and constructed the expected proposed bytes independently. Complete equality confirms only the two approved Subject edits, Version 12 to 13 and illustrative Updated At changed; Summary, body, other metadata and all remaining bytes are preserved. The actual source remains at its frozen hash and mode 0644; all five grammar pins are current.

Report: `activation/connected-preview-independent-review.md`, SHA-256 `f72f65bcca5aaeb53de36c9a3a2dd492cd5fa2dd1b1547fd44465c52a7549c45`. This verifies the preview, not staging, semantic adoption or publication permission. The separate staging and 44-owner disposition questions remain unanswered.

## Actual stale-source refusal

One further actual HTTP MCP call used only `preview_subjects` for CA-D-253, changing the expected source SHA-256 to an intentionally wrong all-zero value. Identity, Version, profile and patches were unchanged. MCP returned `subject-pin-stale`, with preview and staging null, no stage root and empty retained/unverified artifact lists. The real source bytes and mode stayed unchanged; the staging-prefix inventory remained absent. This read-only check did not retry the denied stage operation or use an alternate write route.

Evidence: `activation/connected-stale-preview.json`, SHA-256 `f9087b9a6a35af7568dabaec748a8870f9aa9908dd17a08903ed307e3e484083`. Root inspected both the exact request and response. Successful and stale-source preview behavior is now verified against the connected endpoint. Scratch staging/readback, batch disposition and live migration remain unperformed and gated.

## Explicitly approved one-Atom staging attempt — 2026-10-14

The Operator explicitly approved staging only CA-D-253 using its verified preview. Root rechecked actual MCP discovery/context and the saved client/preview hashes, then sent exactly one stage_subjects request with the original preview seal and illustrative timestamp. The former permission blocker is resolved for this single attempt, not the 611-owner batch or live publication.

The call returned an uncertain MCP error, not a successful staging result: `Implementation call failed; no automatic replay`. Evidence `activation/connected-d253-stage.json` has SHA-256 `0989a8b84f26ca8b6861eedec77e3cf96dfa475eef4d24314b91f09e76cef0ef`. The request observation begins at 08:45:32 UTC, the saved error response was written at 08:47:02 UTC, and the manifest at 08:47:13 UTC. This matches the gateway's 90-second deadline and shows that effects continued beyond the error response. No retry, reload or cleanup was attempted.

Independent readback found one complete-shaped batch: `.caprmedio_tmp/subject-preview/e7e1dc30c56941b19c1e8ba0843daae4/`, containing only its 0001 directory, the CA-D-253 candidate and manifest.json. The candidate is byte-identical to the reviewed preview, SHA-256 `8a8b9ab42f45a671308dc3f85d71a3c7c2399d354d3fcd6d2d6bccc6f54881d2`. The canonical manifest hash is `4dd557fac6fb09175a5aa9ab603ad0cad96d06b2ba062cb19173389ecc11505e`; it binds only the exact source, candidate, preview and intent pins. Original CA-D-253 bytes/mode remain unchanged. A fresh no-write request check again verified all 906 Core source pins.

Readback report: `activation/connected-stage-independent-review.md`, SHA-256 `621d8575d67cb4f3ad5b4f0c4d7bfad5a1b6a76f62af55b01882255ce9e372d1`. This proves the persisted candidate and manifest, not successful completion of every provider post-check. P2382 remains Active pending transport/effect reconciliation. Preserve the batch; do not describe the uncertain call as zero effects, success or permission to replay. The separate 44-owner disposition and live migration approval remain open.

## Measured local timeout follow-up — 2026-10-14

The gateway has a 90-second implementation-call deadline. Its generic failure response discards the exception type and decrements in-flight bookkeeping even when child effects can continue. Timing and code strongly support deadline expiry for the earlier stage; the exact lost exception and final child post-checks remain unproved. No retry or cleanup occurred.

Commit d2740da53 adds real gateway-to-production-child fixture completion coverage and an event-controlled uncertain/late-effect/no-replay test. Both passed independently. These fixture tests do not simulate a full Core workload or prove the lost production exception.

A single pure preview in an isolated, byte-verified full control-tree copy identified repeated identity parsing as the dominant cost. Existing rules permit invocation-local parsing reuse; they still require fresh inventories, bounded no-follow reads, currentness, duplicate checks, independent candidate validation and seal/readback checks. No rule amendment, persistent cache, new dependency, timeout increase or authority-context redesign was needed.

Commit 63536837f changes only the two native Subject helpers plus tests. Exact-byte parse results, including parser failures, are reused only within one invocation. Every identity decision and fresh read remains. Fifty-five affected tests passed: authored reuse 6, independent reuse 6, direct guards 12, stage 14, provider 7, protocol/gateway 10. Root independently ran provider and protocol/gateway checks. Independent review passed on production hashes 68bd36aadc8e5971d5e4467c4ad7329cbb9fd3b6c5fc909ed93b99a74086b21c and b5eeb4bbcad96f4de3a84016ca1a4ed9d1c12776d9ddc3137f51ee4a42695f73.

Identical-input host profiling improved from 77.301 to 51.661 seconds (33.17%). Identity parses fell from 12,978 to 6,489. Both previews produced the original ba718c8d430ccb7a88c141705019762aa24aa28257171fb37520bcf28e437d06 seal. All four inventories, 26,994 fresh reads, 32,730 no-follow opens, ten currentness checks and two complete validations remained. These are instrumented host timings, not a Docker-stage or 611-owner batch guarantee; peak memory was not measured.

Scratch evidence: activation/performance-profile/report.md (e9df8d789d5998940717a20a31ab171db3f217d506e2c8d8bfb0c778d67849e6), activation/identity-reuse-independent-review.md (acc06415e39235c85edab762177dd5629c39d97b89b37c3bbfcb84441c676a4d), and tool-readiness/activation/identity-reuse-test-report.md. Before/after profiles and the frozen copy are retained with that report. Root rechecked the frozen request and all 906 Core pins, and the earlier staged candidate/manifest/source hashes remain unchanged.

CA-P-2383 is locally Done. CA-P-2382, P2167 and P1959 remain Active. The fix is not activated; the connected image still uses 15f9ce76e. Next approval is limited to activating the reviewed fix and a fresh read-only preview, not replaying the uncertain stage. The 44-owner disposition and live publication remain separate decisions. No push or installed-package release occurred.
