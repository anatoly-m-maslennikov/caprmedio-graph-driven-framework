---
atom_id: CA-O-200
content_role: Operations
type: Action
current_scope_unit: PROJECT_CONFIGURATION
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-10 03:51:36 +0400"
subjects:
  governs: "Install one admitted Project runtime"
  depends_on: [Action, Operator, Project, Framework Package, Runtime, Command, Skill, Projection, Journal]
relations:
  relates_to: [CA-O-164, CA-O-169, CA-R-1904, CA-M-362, CA-D-562, CA-D-599, CA-D-600, CA-D-603, CA-D-604]
---
# Summary

Install one admitted Project runtime

## Action

Install one admitted Project runtime **means** the explicitly commanded Action that installs one unchanged, fully gated Framework package into its declared Project, preserving configuration and Project-owned history.

## Scope

One sealed package and retained Full Gate, one declared target Project, one installation command, and one same-byte bootstrap or quiesced replacement. This is neither source admission nor image restoration.

## Details

1. Reopen the package, exact retained Full Gate/image evidence, current target controls and registered Operator. Retain the command input and record/reopen this actual direct Action start before any installation effect. Source admission or an available gate is not the command to install.
2. Under the shared installation lock, bind and persist the target context, stage the package-relative command/environment/wrapper, hook-free ca, and source-bound Methodology delivery. Reopen all staged bytes, modes, prospective selectors and generation proof. Existing configuration remains byte-for-byte unchanged; defaults are created only when it is absent.
3. For replacement, reopen the exact selected old package and the migration/quiescence evidence. If an input changes or a process is not proven quiescent, stop before deletion. After all checks pass, remove only that selected installed package, never configuration, authoring authority, Journal or transaction evidence.
4. Install the same staged bytes. Publish the package selector and native runtime selector only after complete final carriers have been reopened, with runtime activation last. A pre-deletion failure preserves the old selection; a post-deletion failure leaves the runtime honestly unavailable and no selector pointing at removed or partial installation.
5. Reopen the installed package, native selector, generation proof, ca and Methodology delivery; record the actual terminal result in the shared Journal. A recording failure preserves actual installed state and original pending evidence. Recovery records only that exact missing terminal; it does not reinstall or replay unknown effects.

The Action does not start a workflow or container automatically. Runtime startup and release publication remain separately commanded capabilities. Caller strings, a PID, a lock record or a syntactically valid receipt hash do not substitute for physical gate, command or quiescence evidence.
