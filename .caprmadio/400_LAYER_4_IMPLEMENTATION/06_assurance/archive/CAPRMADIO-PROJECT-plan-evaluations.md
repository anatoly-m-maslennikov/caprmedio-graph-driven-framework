# Evaluation case — Make DSET self-hosting and skills thin

Accepted qualitative criteria remain owned by their layer plans. This Change
runs them independently from deterministic tests and records disagreements by
case and criterion.

| Owning plan | Applicable Eval IDs |
|---|---|
| `plan-evaluations.md` | `CAPRMADIO-EVALUATION-CASE-META-008..009` |
| `plan-evaluations.md` | `CAPRMADIO-EVALUATION-CASE-GOV-007..022`, `CAPRMADIO-EVALUATION-CASE-GOV-025`, `CAPRMADIO-EVALUATION-CASE-GOV-026`, `CAPRMADIO-EVALUATION-CASE-GOV-028..029`, `CAPRMADIO-EVALUATION-CASE-GOV-032..034` |
| `plan-evaluations.md` | `CAPRMADIO-EVALUATION-CASE-TOOL-003..004` |
| `plan-evaluations.md` | `CAPRMADIO-EVALUATION-CASE-SKILL-002..008`, `CAPRMADIO-EVALUATION-CASE-SKILL-010..011` |
| `plan-evaluations.md` | `CAPRMADIO-EVALUATION-CASE-OPS-002..003`, `CAPRMADIO-EVALUATION-CASE-OPS-010` |

Connected accepted IDs are `CAPRMADIO-EVALUATION-CASE-META-008`, `CAPRMADIO-EVALUATION-CASE-META-009`,
`CAPRMADIO-EVALUATION-CASE-GOV-007`, `CAPRMADIO-EVALUATION-CASE-GOV-008`, `CAPRMADIO-EVALUATION-CASE-GOV-009`,
`CAPRMADIO-EVALUATION-CASE-GOV-010`, `CAPRMADIO-EVALUATION-CASE-GOV-011`, `CAPRMADIO-EVALUATION-CASE-GOV-012`,
`CAPRMADIO-EVALUATION-CASE-GOV-013`,
`CAPRMADIO-EVALUATION-CASE-GOV-014`, `CAPRMADIO-EVALUATION-CASE-GOV-015`, `CAPRMADIO-EVALUATION-CASE-GOV-016`,
`CAPRMADIO-EVALUATION-CASE-GOV-017`,
`CAPRMADIO-EVALUATION-CASE-GOV-018`,
`CAPRMADIO-EVALUATION-CASE-GOV-019`,
`CAPRMADIO-EVALUATION-CASE-GOV-020`, `CAPRMADIO-EVALUATION-CASE-GOV-021`, `CAPRMADIO-EVALUATION-CASE-GOV-022`,
`CAPRMADIO-EVALUATION-CASE-GOV-025`, `CAPRMADIO-EVALUATION-CASE-GOV-026`,
`CAPRMADIO-EVALUATION-CASE-TOOL-003`,
`CAPRMADIO-EVALUATION-CASE-TOOL-004`,
`CAPRMADIO-EVALUATION-CASE-SKILL-002`,
`CAPRMADIO-EVALUATION-CASE-SKILL-003`, `CAPRMADIO-EVALUATION-CASE-SKILL-004`, `CAPRMADIO-EVALUATION-CASE-SKILL-005`,
`CAPRMADIO-EVALUATION-CASE-SKILL-006`, `CAPRMADIO-EVALUATION-CASE-SKILL-007`, `CAPRMADIO-EVALUATION-CASE-SKILL-008`,
	`CAPRMADIO-EVALUATION-CASE-SKILL-010`, `CAPRMADIO-EVALUATION-CASE-SKILL-011`,
`CAPRMADIO-EVALUATION-CASE-OPS-002`, `CAPRMADIO-EVALUATION-CASE-OPS-003`, and `CAPRMADIO-EVALUATION-CASE-OPS-010`.

## Change-only qualitative proof

| Eval ID | Scenario | Threshold |
|---|---|---|
| `CAPRMADIO-EVALUATION-CASE-SKILL-009` | Clean declared Claude, Codex, and other-host fixtures use the published installation path. | Every operator installs or links the real skill, confirms discovery, invokes its trigger, reaches local rules, and identifies the stop boundary. |
| `CAPRMADIO-EVALUATION-CASE-TOOL-005` | Operators run the utility workflow on every declared platform, including spaces, Unicode, failures, and interrupted writes. | Outcomes are equivalent and safe; any narrower applicability is visible before execution. |
| `CAPRMADIO-EVALUATION-CASE-TOOL-006` | Reviewers assess allowed, denied, unknown-registry, incompatible-license, provenance-drift, and expired-exception dependencies. | Every reviewer reaches the same accept/stop result from the authoritative rule and does not invent approval. |
| `CAPRMADIO-EVALUATION-CASE-OPS-008` | A cold operator investigates the implementing PR's live GitHub workflow/run/check and protected-target state. | Every operator binds evidence to the actual PR SHA and selects a safe merge, block, or retry action without bypassing protection. |
| `CAPRMADIO-EVALUATION-CASE-OPS-009` | Projects use shared integration branches and optional isolated worktrees across concurrent Changes and one protected PR. | Every reviewer identifies branch roles, actual workspace mode, and proof owner without requiring a worktree by default, merging Change identities, or creating permanent layer branches. |

Use at least two independent reviewers where interpretation matters. Correct the
earliest ambiguous owner and rerun the failed case; do not average a blocker
into a pass.
