---
cce_version: cce_1
cce_form: method
subjects:
  governs: Subject/Graph/Rule
  depends_on: []
version: 10
updated_at: 2026-10-24 00:51:05 +0400
relations:
  method_for:
  - CA-R-1123
  derived_from:
  - CA-A-058
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
atom_id: CA-M-202@10
status: Archived
content_role: Method
author: Anatoly Maslennikov
current_scope_unit: TOOLS
---
# Validate the governed routing tree

## Applicable when

use this Method **before** a governed router selects **or** traverses a route **in** the current routing tree.

## Procedure

1. load the current routing-tree authority **and** its declared node, edge, root, leaf, priority, **and** fallback constraints.
2. resolve **every** referenced target against the current active graph **without** following derived inverse relations as authored edges.
3. check root uniqueness, reachability, permitted edge types, cycle rules, selector exclusivity, fallback completeness, **and** terminal-route validity.
4. emit one stable issue per violated constraint with source carrier **and** exact route location.
5. permit routing **only** **when** the selected tree frontier has no blocking issue.

## Outcome

routing receives a deterministic valid verdict **or** an attributable set of structural violations **before** **any** route is used.

## Failure or stop

treat unreadable authority, unresolved targets, ambiguous roots, **and** stale frontiers as blocking validation failures.
