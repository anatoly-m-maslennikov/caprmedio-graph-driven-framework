---
atom_id: CA-M-202
ref_id: CA-M-202
container:
  scope_unit: CA-SU-16
role: Method
form: Eng Policy
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Rule
tier: 2
relations:
  method_for:
  - CA-R-1123
  derived_from:
  - CA-A-058
status: Active
version: 16
updated_at: 2026-11-02 19:44:26 +0400
cce_version: cce_1
cce_form: method
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
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
