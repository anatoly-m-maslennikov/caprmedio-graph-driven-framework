---
identity:
  atom_id: CA-P-3021
  ref_id: CA-P-3021
context:
  role: plan
  form: Plan
  label: Task
  tier: 3
  container:
    atom: CA-P-3018
  topics:
    main_subject: CAPRMEDIO_MODEL <+ Atom
state:
  version: 1
  status: done
  updated_at: '2026-11-12T01:47:42.847318+00:00'
destination:
  file:
    name: CA-P-3021-TASK--pilot-python-workflows-on-atom-lifecycle.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/03_plan/CA-P-3018-EPIC--adopt-the-workflow-engine-and-migrate-cfel-claims-to-python/020_done
---
## Summary

Pilot Python Workflows on Atom Lifecycle

## Objective

Use the adopted Engine RMED to run Change Current Status as a Python Workflow. Compare the pilot with the verified baseline for accepted behavior.

## Implementation handoff

- Author the business logic and Action order in the Formal Claim of the successor to CA-O-10011@3. Pin the admitted Workflow, CA-O-10010@1 Step and CA-O-10007@1 Action revisions.
- Route the existing Change Current Status operation through the Engine. Keep Project locking, source selection, preflight, destination checks and the per-Atom Action effect boundary.
- Give the reviewed Python Workflow typed input and read data. The Workflow decides which Actions to invoke and in what order. Each Action keeps the existing source rechecks and carrier relocation behavior. Keep the same API and MCP entry points.
- Return confirmed effects and actionable failure details through both entry points. Stop further dispatch when an Action fails. Report the Actions left unrun when the Workflow had already selected them.

## Acceptance

Use CA-E-825 and CA-A-1337 on disposable Projects. Compare accepted behavior for ordering, identity, Version and carrier destinations. Verify recursive Backlog-to-Active activation for Current Tasks at two or more levels, including an attached Draft that does not block activation. Verify field-specific rejection before effects and failure after a committed effect. Check successful result details through MCP. Record the Workflow and code revisions and repeat the checks in the staged release.

## Result

Implemented Change Current Status as the reviewed Python Formal Claim in CA-O-10011@4. The existing lifecycle API and MCP route dispatch its ordered plan through CA-O-10010@1 and CA-O-10007@1. The existing backend retains Project locking. The per-Atom Action retains source and destination checks and carrier relocation. A definition change, withdrawal or disappearance blocks further dispatch and returns confirmed effects and Actions left unrun. The Project Journal records actual Run and Step observations at the selected control root. An append failure returns a warning without altering the business result.

### Accepted source and code

| Input | SHA-256 |
| --- | --- |
| CA-O-10011@4 | `e86a64552bfa47ad162b58adf64aaa919fc6ade7b69a277fc98c2bb4adc49c37` |
| CA-O-10010@1 | `6eaa0d360e322a82fdfad60ff4399bd9d32c67f0f6483c16dfa440709cd70272` |
| CA-O-10007@1 | `adfc8492bcc26e21935496ebcb382fef99b373578fd91206953937deb8aeac3f` |
| Generated Python entry point | `2b0d5ecac9432c1a59f8071371329fc939cb3dc33e451dca72be99809ff7067a` |
| Image definition snapshot | `24b6abe61323cedc7406cfa56c55b3142d92b9172584ab0841983689ec7b7820` |
| Status executor | `8acb5f2df33d4b0e86c7923916eee69a00a0839ef78f43ddead74075f1fa774d` |
| Definition verifier | `4a95625fb0597462f962f17e01b9dff589f9409aeb460f713ab92ca706a34ce0` |
| Workflow Journal observer | `89942174761ef2f520ddc1e3439fa0e14535c3b77d228c24039c8f4b3793eedc` |
| Shared Journal writer | `eac7db675258ef83ef81c9c457916ca71b16f5c774e5e569696cf3550c1e9a4f` |
| MCP lifecycle provider | `970414dd1a17fd06bd8bcc9cda0e5e144d83b196911c689dd2c239eda5ea02c2` |

The staged code came from the working tree based on Git `f8aab16bf1aa9edad8ecfc6a81c55bba41f3230d`. The CA-A-1337 comparison used pre-pilot status executor SHA-256 `8120a5c439ee0d8f66972e4565295b91c870ea54f2757bc718480e4bcadb5ba2`.

### Verification

- Four disposable baseline comparisons matched saved references, ordered effects, and final Markdown bytes. The cases covered recursive Backlog to Active with an attached Draft, Active to Done, Done to Active, and a single Requirement status change.
- Eight API tests passed from the final staged package. They checked recursive activation, field-specific rejection before effects, stale, withdrawn and unavailable definitions, a changed definition after a committed Action, and known and uncertain effects after an Action failure. A separate staged check verified explicit Journal control selection and safe behavior when its settings disappear.
- Five MCP stdio scenarios passed from the final staged package. The success case activated the Epic and two levels of Tasks in order, returned 12 confirmed effects and preserved the attached Draft byte for byte. Rejected inputs created no business observations. Partial failures preserved confirmed and uncertain effects and reported the unrun Actions. Run IDs, Step Run IDs and exact bindings matched the Journal observations for success, failure and blocked dispatch.
- The release builder verified 2,454 package files and 241 sealed Docker context inputs. Image input fingerprint `66b6b83a5dfabf00e645615ac555008084e3e279daa28b3f8d1102f2d8ce8b01`. The staged runtime resolved the installed definition bindings from both layouts.

Package evidence `.caprmedio_tmp/CA-P-3021/staged-release-journal-binding-53hy9jkx/release-evidence.json` has SHA-256 `a54172e99029750e5135bcd42b1154dd0f05268a165698895d1ab774e4323315`. MCP evidence `.caprmedio_tmp/CA-P-3021/mcp-acceptance/result-journal-binding-final.json` has SHA-256 `c98bf609c9c7f8dbc11807f6c7cb85bf4302dc6d07f0adca0023b0631f5c5b29`.

The MCP harness used cached DuckPGQ, a polling watcher and an explicit SDK stdout stream. The stock stdio launcher sent its protocol output to stderr in this environment. Acceptance used disposable Projects and a sealed release context. Live deployment and the broader CFEL migration are outside this Task.
