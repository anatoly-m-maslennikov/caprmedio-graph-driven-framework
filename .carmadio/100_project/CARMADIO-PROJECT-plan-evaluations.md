# Evaluation case — Make DSET self-hosting and skills thin

Accepted qualitative criteria remain owned by their layer plans. This Change
runs them independently from deterministic tests and records disagreements by
case and criterion.

| Owning plan | Applicable Eval IDs |
|---|---|
| `plan-evaluations.md` | `CARMADIO-EVALUATION-CASE-META-008..009` |
| `plan-evaluations.md` | `CARMADIO-EVALUATION-CASE-GOV-007..022`, `CARMADIO-EVALUATION-CASE-GOV-025`, `CARMADIO-EVALUATION-CASE-GOV-026`, `CARMADIO-EVALUATION-CASE-GOV-028..029`, `CARMADIO-EVALUATION-CASE-GOV-032..034` |
| `plan-evaluations.md` | `CARMADIO-EVALUATION-CASE-TOOL-003..004` |
| `plan-evaluations.md` | `CARMADIO-EVALUATION-CASE-SKILL-002..008`, `CARMADIO-EVALUATION-CASE-SKILL-010..011` |
| `plan-evaluations.md` | `CARMADIO-EVALUATION-CASE-OPS-002..003`, `CARMADIO-EVALUATION-CASE-OPS-010` |

Connected accepted IDs are `CARMADIO-EVALUATION-CASE-META-008`, `CARMADIO-EVALUATION-CASE-META-009`,
`CARMADIO-EVALUATION-CASE-GOV-007`, `CARMADIO-EVALUATION-CASE-GOV-008`, `CARMADIO-EVALUATION-CASE-GOV-009`,
`CARMADIO-EVALUATION-CASE-GOV-010`, `CARMADIO-EVALUATION-CASE-GOV-011`, `CARMADIO-EVALUATION-CASE-GOV-012`,
`CARMADIO-EVALUATION-CASE-GOV-013`,
`CARMADIO-EVALUATION-CASE-GOV-014`, `CARMADIO-EVALUATION-CASE-GOV-015`, `CARMADIO-EVALUATION-CASE-GOV-016`,
`CARMADIO-EVALUATION-CASE-GOV-017`,
`CARMADIO-EVALUATION-CASE-GOV-018`,
`CARMADIO-EVALUATION-CASE-GOV-019`,
`CARMADIO-EVALUATION-CASE-GOV-020`, `CARMADIO-EVALUATION-CASE-GOV-021`, `CARMADIO-EVALUATION-CASE-GOV-022`,
`CARMADIO-EVALUATION-CASE-GOV-025`, `CARMADIO-EVALUATION-CASE-GOV-026`,
`CARMADIO-EVALUATION-CASE-TOOL-003`,
`CARMADIO-EVALUATION-CASE-TOOL-004`,
`CARMADIO-EVALUATION-CASE-SKILL-002`,
`CARMADIO-EVALUATION-CASE-SKILL-003`, `CARMADIO-EVALUATION-CASE-SKILL-004`, `CARMADIO-EVALUATION-CASE-SKILL-005`,
`CARMADIO-EVALUATION-CASE-SKILL-006`, `CARMADIO-EVALUATION-CASE-SKILL-007`, `CARMADIO-EVALUATION-CASE-SKILL-008`,
	`CARMADIO-EVALUATION-CASE-SKILL-010`, `CARMADIO-EVALUATION-CASE-SKILL-011`,
`CARMADIO-EVALUATION-CASE-OPS-002`, `CARMADIO-EVALUATION-CASE-OPS-003`, and `CARMADIO-EVALUATION-CASE-OPS-010`.

## Change-only qualitative proof

| Eval ID | Scenario | Threshold |
|---|---|---|
| `CARMADIO-EVALUATION-CASE-SKILL-009` | Clean declared Claude, Codex, and other-host fixtures use the published installation path. | Every operator installs or links the real skill, confirms discovery, invokes its trigger, reaches local rules, and identifies the stop boundary. |
| `CARMADIO-EVALUATION-CASE-TOOL-005` | Operators run the utility workflow on every declared platform, including spaces, Unicode, failures, and interrupted writes. | Outcomes are equivalent and safe; any narrower applicability is visible before execution. |
| `CARMADIO-EVALUATION-CASE-TOOL-006` | Reviewers assess allowed, denied, unknown-registry, incompatible-license, provenance-drift, and expired-exception dependencies. | Every reviewer reaches the same accept/stop result from the authoritative rule and does not invent approval. |
| `CARMADIO-EVALUATION-CASE-OPS-008` | A cold operator investigates the implementing PR's live GitHub workflow/run/check and protected-target state. | Every operator binds evidence to the actual PR SHA and selects a safe merge, block, or retry action without bypassing protection. |
| `CARMADIO-EVALUATION-CASE-OPS-009` | Projects use shared integration branches and optional isolated worktrees across concurrent Changes and one protected PR. | Every reviewer identifies branch roles, actual workspace mode, and proof owner without requiring a worktree by default, merging Change identities, or creating permanent layer branches. |

Use at least two independent reviewers where interpretation matters. Correct the
earliest ambiguous owner and rerun the failed case; do not average a blocker
into a pass.
