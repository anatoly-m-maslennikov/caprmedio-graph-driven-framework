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
