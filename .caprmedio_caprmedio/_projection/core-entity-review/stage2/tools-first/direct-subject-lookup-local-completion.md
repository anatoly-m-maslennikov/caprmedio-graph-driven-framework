# Direct Subject lookup — local completion

Derived implementation evidence for CA-P-2374–2377, 2026-10-14. This is not an Atom or publication authorization.

## Delivered

Direct ATOM_SEARCH MCP lookup requires explicit Subject, field, match mode, notation profile, owning Scope Unit, Content Roles and lifecycle. Optional Atom IDs narrow the request. Exact, prefix, suffix and contains reuse the existing reader/matcher. Results contain logical matches and actual source hashes; no private paths or full content. No Session, Run or Journal record is created.

Current contract/grammar pins, selected Project boundary and retained provenance, bounded no-follow source reads, currentness and possible selected-ID conflicts remain checked. Selected directory symlinks, including dangling links, refuse incomplete lookup. Excluded malformed C/A content and absent Type in otherwise valid selected sources do not require migration. Existing CLI and Session calls remain supported; no live publication safeguard changed.

## Verification

- Eight-source rule packet independently reviewed; exact predecessor bytes preserved. Commit `8186f93a4`.
- Atom/Scope receiver pin-only refresh independently reviewed; 55 affected Session tests passed. Commit `e75005fe0`.
- Final ATOM_SEARCH suite: 71 passed. Independent reader and provider reviews passed, including the corrected Project-boundary and symlink gaps.
- Final real MCP protocol suite: 10 passed in 2.416 seconds, through production create_server and ClientSession with actual contract/grammar fixtures and no mocked freshness. Registration and calls preserve fixture bytes and directory membership.
- Adjacent MCP registry/descriptor/server checks: 26/30 passed. Four unchanged O199 tests fail before Tool invocation because their old source-fixture path is absent in HEAD. No unrelated repair or full-suite success is claimed.
- Read-only local Core reader diagnostic: 127 active matches, full coverage, zero diagnostics, 17.85 seconds. All 906 Core source hashes, Settings/Structure and control membership stayed unchanged. Explicit all-lifecycle inspection correctly reported incomplete coverage because old archived carriers remain invalid. This is not connected-MCP evidence.

Implementation commit: `2a40cb4c8`.

The six current affected Plans parse, their Status matches placement, and predecessor archives were compared byte-for-byte. Stage-specific implementation/test gates remain explicit in their Details and Epic; no Artifact depends_on relation is used to misrepresent whole-Task scheduling.

Final reader SHA-256: `3095a68ff644abd6d0cc1fa0de1d644b00f308bb367a135a71733c490658f9c4`.
Final provider SHA-256: `30beb88c076b2544c97ac2ec0f0f29c7ff5694b6d84ada45a73afeddd2abd1b7`.
Final protocol-test SHA-256: `816e57602d9727358fd197d9fd8c1650faaf87aabc4c57f730449efb8c93b10b`.

## Remaining boundary

The connected MCP at port 56317 still ran image-owned code when observed; its Subject discovery returned zero Tools before this implementation. No image rebuild, installation, restart or reload was performed. The installed-selector file was absent. Checkout tests do not prove that connected service exposes this Tool.

The Operator has not yet answered whether preview/staging should use separate direct MCP preparation calls. Lookup approval does not decide staging or live publication. Trusted human publication confirmation, selected-route manifest reconciliation and separately approved Core migration remain open. CA-P-1959 and CA-P-2167 remain Active. Ordinary content migration remains separate.
