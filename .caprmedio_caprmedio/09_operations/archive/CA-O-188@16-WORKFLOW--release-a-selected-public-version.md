---
atom_id: CA-O-188@16
content_role: Operations
type: Workflow
current_scope_unit: caprmedio
status: Archived
author: Anatoly Maslennikov
subjects:
  governs: 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations/Type: Workflow//Release a selected public Version'
  depends_on:
  - 'Subject/Graph Node/Domain/Continuant/Actor/Type: Operator'
  - Subject/Graph Node/Engineering/Release Version
  - Subject/Graph Node/Documentation
  - Subject/Graph Node/Engineering/Pull Request
  - Subject/Graph Node/Engineering/Release/Version History
  - Subject/Graph Node/Engineering/Continuant/Tool
version: 16
updated_at: 2026-10-26 02:39:08 +0400
relations:
  invokes:
  - CA-O-189
  - CA-O-191
  - CA-O-195
  - CA-O-197
tier: 3
---
# Summary

Release a selected public Version

## Operation

Release a selected public Version **means** the **Operator**-invoked, non-recursive Workflow that prepares one selected Version for the personal remote from `amm/dev` to `main`, creates or updates its public Pull Request, and never merges it.

## Scope

One selected Version, one personal remote identity, `amm/dev`, `main`, the selected README, one full PR description, and one concise Version History summary.

## Steps

| Step | Action | Result boundary |
| --- | --- | --- |
| CA-O-189 | CA-O-190 | discover at most one matching open PR |
| CA-O-191 | CA-O-192 | make the one content prompt for the PR body and concise Version History summary |
| CA-O-195 | CA-O-196 | mechanically apply documentation and history, commit/push, and create or update its `main` PR |
| CA-O-197 | CA-O-198 | when newly known, append the exact PR URL mechanically and refresh that same PR |

## Transitions

| Step result | Next result |
| --- | --- |
| a unique existing matching PR or no matching PR is evidenced | CA-O-191 |
| one content result is complete | CA-O-195 |
| commit is pushed and one actual open PR URL is available | CA-O-197 |
| exact URL is already present, or mechanically appended and pushed to the same PR | complete |
| failed or unsafe result | stop and report it for manual handling; do not merge |

## Details

Invoke this Workflow from the repository host through `PROJECT_TOOLS/release.py public --project-root <project-root> --run-id <run-id> [--content-draft <json-path>]` in the governed uv environment; `--project-root` defaults to the repository root. The optional UTF-8 JSON file contains exactly `description` and `summary`. Without it, the runner returns `input_required` and its content prompt without publication. The Project's MCP blacklist disables `public.release` exposure and invocation while preserving its adapter for later reuse. Full-suite verification, Draft PR behavior, actual-link follow-up and no merge remain required.

This Workflow starts only on the Operator's command for the selected public-release Run. It runs Git before every listed Step and after final completion. Public release increments the third numeric Version component and drops the fourth/internal suffix, producing exactly three numeric components: `0.4.1.xxx` becomes `0.4.2`. There is no rollover: `0.4.9.x` becomes `0.4.10`. CA-O-192 is its sole content prompt; README, Version History, Git, and PR mechanics are programmatic. Adding only the actual PR URL after the PR exists requires its mechanical follow-up commit and push. It never merges.

After the one content result and before the first public push or PR write, the native Tool completes and retains the fresh complete public suite required by CA-M-365/CA-M-366 for the fixed selected source and prepared materials. This is internal Tool work, not another named Step/Action or a restored CA-O-193/CA-O-194 source-proof phase. A failed, stale, incomplete or unsafe result stops for manual handling. Creating a new PR uses Draft; an existing matching open PR is converted to Draft before body editing. Actual-URL-only finalization, or a no-op when that URL is already present, preserves all non-metadata bindings and does not rerun the suite or content prompt.
