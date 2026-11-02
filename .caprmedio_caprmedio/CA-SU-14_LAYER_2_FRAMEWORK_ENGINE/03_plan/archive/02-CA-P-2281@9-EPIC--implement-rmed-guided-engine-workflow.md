---
atom_id: CA-P-2281@9
content_role: Plan
type: Plan
label: Epic
work_sequence_number: 2
current_scope_unit: FRAMEWORK_ENGINE
author: Anatoly Maslennikov
status: Archived
subjects:
  governs: 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Workflow'
  depends_on:
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Requirement'
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Method'
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Evaluation'
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Delivery'
  - Subject/Engineering/Tool
  - Subject/Domain/Node/Continuant/Projection
  - Subject/Engineering/Implementation
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Plan'
  - Subject/Domain/Node/Continuant/History/Journal
  - 'Subject/Domain/Node/Continuant/Actor/Type: Operator'
  - 'Subject/Domain/Node/Continuant/Actor/Type: AI Agent'
version: 9
updated_at: 2026-10-24 10:29:57 +0400
tier: 3
---
# Summary

Implement an RMED-guided Engine Workflow

## Objective

Provide a FRAMEWORK_ENGINE implementation Workflow that uses the new Tools to turn selected active RMED authority into tested Implementation, with each Step executed in its own subagent and all unresolved issues reported.

## Details

This is a new Engine Epic, not an extension of the completed release Epic. Author only this Plan and its Tasks now. Implementation, new governing O/RMED, runtime registration and effects happen when its Tasks are executed.

### Runtime flow

1. Gather all active Rs selected for implementation and assess their conflicts and gaps.
2. Compile all applicable active Ms into a derived projection.
3. Compile all applicable E policies into a separate derived projection; retain suitable existing E cases separately.
4. Compile all applicable Ds into a separate derived projection.
5. Review the R/M/E/D inputs together and report conflicts, gaps and ambiguity before affected implementation.
6. Reuse or create E test cases so every selected R has at least one case and all required behaviors are covered.
7. Implement the tests using the Ms, E policies and Ds.
8. Implement the Rs using the Ms and Ds, then run the agreed tests and report actual outcomes.

M/E/D preparation may run in parallel after selection. Each Step runs in a fresh subagent and consumes saved outputs from prior Steps. Each Epic Task is also assigned to its own subagent when executed. No extra reviewer-after-every-Step machinery is required.

### New Tools only

The runtime uses the accepted CONNECTOR_TOOLS query/read/create/modify contract and the receiving TOOL_WORKFLOWS policy boundaries. Explicitly select Active content, the requested scope and any descendant/applicability boundary; connectors do not invent those defaults. No legacy direct mutation/CLI fallback bypasses these boundaries.

New Tool implementation is presently pending. CA-P-2252/2253/2254/2259/2260/2268 and relevant consumer bindings under CA-P-2269–2272 are shared prerequisites, not duplicate work in this Epic. Source contracts or old installed routes do not establish new Tool readiness. Source/prompt preparation may proceed against accepted contracts; affected executable use remains blocked until the required new Tools are implemented and verified.

### Inputs and projections

Inputs identify the target Scope Unit or explicit R set and the implementation boundary. Resolve the declared Scope Unit tree through the new Scope Unit Query/Read bindings (CA-O-211/CA-O-212, implemented by CA-P-2254). Supply the resulting explicit unit frontier to Atom Query; neither folder traversal nor Atom Query derives the tree. Unit-based selection uses Targeting Atoms, or Subtree-targeting Atoms when descendants are selected: resolve Claim Target Scope Unit, with the current Scope Unit default, rather than confuse ownership with applicability. Include eligible parent-owned Goal/Demand Atoms targeting the selected unit and applicable ancestor constraints; keep these sets identified and deduplicate by Atom identity. Collect all applicable active authority, such as TOOLS plus TOOL_NAME and applicable ancestors, without collecting unrelated sibling Tools. Each compiler explicitly Queries identities, then full-Reads every selected Atom through CA-O-047. Preserve the complete operative content, actual current_state/source-view evidence and readable original-source reference/Version. Partial Query results, unreadable sources and incomplete selection do not become complete projections. It remains derived and is never a new source of truth. This Epic does not require a new hash/snapshot/sealing framework.

Projection agents and implementation agents report issues with Rs, Ms, E policies/cases and Ds throughout the Run. Reports identify affected originals, the ambiguity/conflict/gap, impact and any evidence-supported proposal. Blocking issues go to the Operator; the workflow does not silently rewrite authority or pretend incomplete inputs are ready. Changed source inputs require renewed affected preparation.

### Tests and completion

Maintain an R → E case → executable test coverage map. Count only verified current Evaluation cases whose direct evaluation_for relation includes the selected R. New creation must return confirmed identity/state/effects and recorded evidence; proposed, Draft, failed or effect-uncertain cases do not satisfy coverage. Functional/public-interface and focused integration checks are the default emphasis. Useful unit/semantic checks are retained for pure logic, without a fixed test ratio; installed end-to-end checks are used where the narrower boundary cannot expose the important behavior. Reuse current CA-E-389/CA-M-285 policy and suitable existing cases rather than duplicate them.

Tests are implemented before required behavior. Record genuine unmet-behavior baselines separately from broken test harnesses; existing correct behavior may already pass. Final completion requires actual execution of the selected tests, complete Requirement accounting and an honest remaining-issue/effect report. Confidence and permissions come from current applicable settings, Plan/Run inputs and Operator delegation.

CA-P-2292 owns the missing private Engine run-output writer and its supporting delivery contract. It writes the four derived inputs only under .caprmedio_caprmedio/_projection/ENGINE_IMPLEMENTATION/<run_id>/ and the full report at .caprmedio_tmp/ENGINE_IMPLEMENTATION/<run_id>.md, returns verified repository-relative references, and reuses workflow_run_support for shared Run/Step/Action Journal linkage. It does not use Atom Create to store projections, mutate authoritative Atoms or introduce a generic public artifact API. Outputs retain existing Run/Step/subagent identities and input current_state evidence; another Run's output is never overwritten. Do not add automatic release, retry/recovery, whole-project repair, live Subject migration or a new universal Tool family. Necessary missing capabilities are reported or linked to their existing owners.

## Definition of Done

- The O flow and its supporting Engine RMED have been reviewed against this Epic.
- Every Step has short instructions, declared new-Tool bindings and a fresh-subagent input/output contract.
- All selected Rs have linked E cases and implemented tests; prepared inputs preserve all applicable active Ms, E policies and Ds.
- Actual isolated fixtures prove the complete test-first path and truthful conflict, gap, missing-Tool and Implementation-issue reports.
- Workflow discovery/execution, full reports and shared Journal outcomes are verified through the new Tools; no source-only readiness or hidden legacy fallback is claimed.

### Decomposing Plans

1. [CA-P-2282 — Define the Engine implementation Workflow](02-CA-P-2281@9-EPIC--implement-rmed-guided-engine-workflow/01-CA-P-2282-TASK--define-the-engine-implementation-workflow.md)
2. [CA-P-2283 — Bind the Workflow to the new Tools](02-CA-P-2281@9-EPIC--implement-rmed-guided-engine-workflow/02-CA-P-2283-TASK--bind-the-workflow-to-the-new-tools.md)
3. [CA-P-2284 — Gather and check the Requirements](02-CA-P-2281@9-EPIC--implement-rmed-guided-engine-workflow/03-CA-P-2284-TASK--gather-and-check-the-requirements.md)
4. [CA-P-2285 — Compile the applicable Methods](02-CA-P-2281@9-EPIC--implement-rmed-guided-engine-workflow/04-CA-P-2285-TASK--compile-the-applicable-methods.md)
5. [CA-P-2286 — Compile the Evaluation policies](02-CA-P-2281@9-EPIC--implement-rmed-guided-engine-workflow/05-CA-P-2286-TASK--compile-the-evaluation-policies.md)
6. [CA-P-2287 — Compile the Delivery specifications](02-CA-P-2281@9-EPIC--implement-rmed-guided-engine-workflow/06-CA-P-2287-TASK--compile-the-delivery-specifications.md)
7. [CA-P-2288 — Assess the complete RMED input](02-CA-P-2281@9-EPIC--implement-rmed-guided-engine-workflow/07-CA-P-2288-TASK--assess-the-complete-rmed-input.md)
8. [CA-P-2289 — Create Requirement-linked test cases](02-CA-P-2281@9-EPIC--implement-rmed-guided-engine-workflow/08-CA-P-2289-TASK--create-requirement-linked-test-cases.md)
9. [CA-P-2290 — Implement the tests first](02-CA-P-2281@9-EPIC--implement-rmed-guided-engine-workflow/09-CA-P-2290-TASK--implement-the-tests-first.md)
10. [CA-P-2291 — Implement the required behavior](02-CA-P-2281@9-EPIC--implement-rmed-guided-engine-workflow/10-CA-P-2291-TASK--implement-the-required-behavior.md)
11. [CA-P-2292 — Deliver Step prompts and issue reports](02-CA-P-2281@9-EPIC--implement-rmed-guided-engine-workflow/11-CA-P-2292-TASK--deliver-step-prompts-and-issue-reports.md)
12. [CA-P-2293 — Verify the complete Workflow](02-CA-P-2281@9-EPIC--implement-rmed-guided-engine-workflow/12-CA-P-2293-TASK--verify-the-complete-workflow.md)

