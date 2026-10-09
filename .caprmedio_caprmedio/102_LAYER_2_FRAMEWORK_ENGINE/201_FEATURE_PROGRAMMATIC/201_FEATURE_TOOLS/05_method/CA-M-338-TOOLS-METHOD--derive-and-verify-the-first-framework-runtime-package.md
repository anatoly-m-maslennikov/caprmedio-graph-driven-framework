---
atom_id: CA-M-338
content_role: Method
current_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 5
updated_at: "2026-10-09 16:57:27 +0400"
subjects:
  governs: "Tool/INSTALL_TOOLS/First-initialization package derivation"
  depends_on: [Tool, Framework Package, Runtime, Methodology, Skill, Docker Image, Journal]
relations:
  method_for: [CA-R-1881]
---
# Summary

Derive and verify the first Framework runtime package

## Scope

The bounded construction, verification and selection of one reusable Framework package and one isolated target-Project installation.

## Claim

the INSTALL_TOOLS first-initialization variant **must** seal a reusable package **before** any first target-Project runtime state is made active, **must** prove the Full Gate and image against those exact bytes, and **must** publish the target selector under its declared lock **only after** all admission records reopen successfully.

## Details

1. Read-verify the current canonical compiled Methodology and its conflict-free source frontier, then require the closed Unit Gate evidence for that compiled candidate. A catalog entry without an admitted pinned revision, a changed source snapshot, a missing support carrier or an unresolved compiled output refuses before effects.
2. Copy the complete `102_FRAMEWORK_ENGINE/`, exact sealed `pyproject.toml`, `uv.lock` and `version.toml`, admitted defaults, `ca` payload, active Methodology source catalog and declared support into `.caprmedio_tmp/release_candidates/<run_id>/package/`. Seal ordered path, digest and mode rows into `manifest.toml`; reopen every row and freeze the candidate manifest digest.
3. Build, immutable-ID inspect and complete-package/MCP canary the exact sealed package bytes; retain the observed image and command evidence without rebuilding the candidate.
4. Run the exact three host-capable Candidate E2E harnesses against that immutable image, then aggregate their evidence with the prior Unit Gate, image build and canary into the existing Full Gate. A result JSON, mutable tag, package copy, source checkout, partial suite or post-gate rebuild is not gate admission.
5. Reopen the preexisting admitted package selector at `.caprmedio_install/current.toml`; a later package-producing contribution, not this first-runtime Action, may publish it. Candidate evidence remains private and retained.
6. Resolve an explicit target Project root and its control child from bootstrap or adopt input; validate the target settings, Project Structure and registry without inventing an Operator, then require that the target runtime boundary is empty. A non-git root, two target Projects in one repository, relocation and adoption are distinct supported paths, each with its own bound context.
7. Under the same target-Project installation lock used by wrappers, Skill, projection and state, stage all package-derived runtime state and environment, publish the complete Skill, then atomically write `.caprmedio_runtime/installation/current.toml` as the final activation point. Its generation is monotonic and command/process evidence binds generation, command, package and target context, never a PID alone.
8. For legacy migration, quiesce only positively identified owned processes, copy the three owned subtrees, verify bytes and ownership, switch the selector, retain old state and N/history, and stop on unsafe quiescence. Cleanup needs a later exact approved cleanup input.

This Method **must not** select a Release Version candidate, require an existing N, promote or retire a Release Version image, change authoring sources, register MCP, install hooks, create a selected-workflow route, or infer a source or image from mutable labels.
