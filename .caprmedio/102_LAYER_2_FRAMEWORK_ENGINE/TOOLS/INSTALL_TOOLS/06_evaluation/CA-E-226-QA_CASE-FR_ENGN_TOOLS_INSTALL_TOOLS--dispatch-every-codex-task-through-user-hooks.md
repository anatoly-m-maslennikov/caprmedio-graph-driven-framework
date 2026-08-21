---
atom_id: CA-E-226
subject_scopes:
  - evaluation
version: 1
updated_at: 2026-08-21 04:52:02
relations:
  evaluation_for:
    - CA-R-856
    - CA-M-103
  check_of:
    - CA-D-011
---
# Dispatch every Codex task through user Hooks

## Claim checked

One installed user-level dispatcher makes the same CAPRMEDIO Hook boundaries available to every subsequently started or resumed Codex task without depending on project-local Hook discovery.

## Test case

Prepare a Codex user Hook carrier with unrelated groups, install Tools into two repositories, and invoke each managed Hook command once from each repository and once outside any repository.

## Acceptance criteria

Installation preserves every unrelated group and creates exactly one generic group for each of wildcard `PreToolUse`, wildcard `PostToolUse`, `SessionStart`, and `Stop`. Each in-repository invocation delegates only to that repository's executable `.caprmedio_install/bin/commit-trigger`; the outside invocation exits successfully without effect. No command embeds an absolute project path, release digest, or executable dependency in the Codex user directory.

## Failure disposition

Reject installation if it duplicates or removes unrelated groups, depends on project trust or a fixed repository path, invokes the wrong installation, or performs work outside an installed repository.
