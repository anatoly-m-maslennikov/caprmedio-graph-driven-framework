---
identity:
  atom_id: CA-A-1385
  ref_id: CA-A-1385@1-draft
context:
  role: analysis_and_advisory
  form: Analysis Report
  tier: 3
  topics:
    main_subject: CAPRMEDIO_STRUCTURE <+ Aspects <+ Engineering <+ Development <+
      Authoring
  container:
    scope_unit: CA-SU-00
state:
  version: 1
  status: draft
  updated_at: '2026-11-12T15:37:46.107450+00:00'
destination:
  file:
    name: CA-A-1385@1-draft-ANALYSIS_REPORT--compare-atom-prose-rewrite-batch-e57-741425539647.md
    path: .caprmedio_caprmedio/02_analysis_and_advisory/000_draft
---
## Summary

Compare Atom prose rewrite batch e57 741425539647

## Details

```json
[
  {
    "ref": "CA-D-613",
    "version": 19,
    "summary": "Serialize public-release Workflow bindings\n\n## Scope\n\nThe Operation identities and execution boundary of one public release.\n\n## Claim\n\nPublic release **must** implement CA-O-188 through these declared Step/Action pairs in order: CA-O-189/CA-O-190, CA-O-191/CA-O-192, CA-O-195/CA-O-196 and CA-O-197/CA-O-198. These source identities describe the work. They do not require a closed manifest, fixed RMED pin set or whole-registry validation before the direct command runs.\n\n## Details\n\n| Step | Action | Result boundary |\n| --- | --- | --- |\n| CA-O-189 | CA-O-190 | Discover zero or one actual matching open `amm/dev` to `main` PR |\n| CA-O-191 | CA-O-192 | Obtain one content result: full PR body and concise Version History summary |\n| CA-O-195 | CA-O-196 | Apply the prepared documentation/history, commit and push, then create or update the matching Draft PR |\n| CA-O-197 | CA-O-198 | Add its actual URL to Version History when missing, then commit and push the follow-up |\n\nThe Operator's explicit command covers this public release for the selected Project and personal remote. Source bindings describe the Operations the implementation performs. They are not authorization, execution success or a caller-selected executor.\n\nBefore the first public push or PR write, run the full test suite with required integration tests built from current code. Failed tests or unavailable required test infrastructure stop release. Do not add separate Atom validation, closed-registry admission or a sealed-package Full Gate. Existing ordinary selected Workflows retain their own permission and admission boundary.\n\nFor actual-URL-only finalization, use the returned matching PR URL and preserve non-metadata inputs. Do not repeat the suite or content prompt. Do not guess a URL, merge, retarget the PR or replay an uncertain remote effect. Report actual failures and partial effects for manual handling. Version History records the released Version and actual PR. Journal records, when appended, describe real events without requiring earlier history or proof receipts.",
    "prose_claim": null,
    "details": null,
    "semantics": null,
    "operation": null
  },
  {
    "ref": "CA-E-812",
    "version": 3,
    "summary": "Quarantine invalid MCP registration entries",
    "prose_claim": "Verify that an invalid descriptor is quarantined with an explicit diagnostic and that independently valid descriptors publish. Unresolved generator integrity or the common activated descriptor frontier stops publication.",
    "details": "Introduce one invalid descriptor alongside an independent valid descriptor. Report and quarantine the invalid descriptor. Publish the valid descriptor. Separately verify that a broken generator or unresolved common descriptor frontier prevents activation.",
    "semantics": null,
    "operation": null
  },
  {
    "ref": "CA-D-667",
    "version": 4,
    "summary": "Derive Authority and Delivery Folder Names",
    "prose_claim": "The Project Authority Folder is `.caprmedio_<project name>`, without a Scope Unit ID.\n\nFor a non-root Scope Unit, derive folder names from its ID, Label, order.number and Name:\n\n| Scope Unit | Authority Folder name | Delivery Folder name |\n| --- | --- | --- |\n| Ordered | `<id>_<label>_<order>_<name>` | `<label>_<order>_<name>` |\n| Unordered | `<id>_<label>_<name>` | `<label>_<name>` |\n\n`<id>` is the stable Scope Unit ID. `<order>` is `order.number`. For an Unordered unit, omit the order segment and its separator. When Label is absent, omit its segment and separator.\n\nPlace each non-root folder under its respective parent's folder. Do not maintain derived folder paths as independent values in the Project Scope Unit Declaration or non-Project Scope Delegations.\n\nDerived paths are readability and placement values, not another structural source. Report conflicting derivations and leave them unresolved. Do not automatically choose a new Name, parent, number or binding. Do not author Structural Level or Structural Coordinate.",
    "details": null,
    "semantics": null,
    "operation": null
  },
  {
    "ref": "CA-R-1471",
    "version": 27,
    "summary": "Keep secondary graphs derived from source authority",
    "prose_claim": "secondary CAPRMEDIO Graphs.\n\nSecondary CAPRMEDIO Graphs **must** be Projections derived from their selected authoritative sources **or** source-traceable upstream Projections. Their nodes **and** Relations **must** preserve source identities **and** traceability **to** the governing derivation authority **and** source facts.\n\nStoring, composing, filtering, **or** rebuilding a secondary graph **must not** make its contents another source of authority. Correct a represented source fact **at** its authoritative source. Correct an incorrect derivation under its governing methodology. Do not independently edit the projected fact **or** fabricate source history to resolve either case.",
    "details": null,
    "semantics": null,
    "operation": null
  },
  {
    "ref": "CA-E-263",
    "version": 25,
    "summary": "Recover one partial file write",
    "prose_claim": "#### Claim checked\n\nOne interrupted PROGRAMMATIC file replacement preserves **or** explicitly reports its declared recovery boundary **without** guessing at a completed result.\n\n#### Applicable conditions\n\nApply **when** a component writes replacement content through a temporary carrier **or** **otherwise** has a declared partial-write recovery boundary.\n\n#### Test case\n\nInterrupt one replacement **after** its temporary carrier is prepared but **before** the declared replacement completes.\n\n#### Acceptance criteria\n\nPass **only** **when** the original target **or** a declared recoverable result remains identifiable, no false completion is reported, **and** the returned context makes the partial state diagnosable.\n\n#### Failure disposition\n\nStop the mutation path **until** its weaker recovery boundary is explicit **or** its atomic replacement guarantee is restored.\n\n#### Sources\n\n- [CA-M-409 — Bound file and subprocess effects](../05_method/CA-M-409-PROGRAMMATIC-ENG_POLICY--bound-file-and-subprocess-effects.md)",
    "details": null,
    "semantics": null,
    "operation": null
  },
  {
    "ref": "CA-O-123",
    "version": 15,
    "summary": "Calibrate evaluator evidence\n\n## Operation\n\nEvaluator Evidence Calibration **means** the optional Agentic Action that compares fresh, independently produced evaluator judgments with independently reviewed expected judgments on an exact frozen case universe for an admitted calibration request. It returns the bounded comparison evidence.\n\n1. Bind the caller's admitted purpose, Actor, permissions, evidence location **and** comparison criteria; the exact evaluator implementation/revision **and** configuration; the ordered cases with stable case/occurrence references, complete inputs **and** their revisions; applicable R/E/D **and** test bindings; **and** the expected judgments with their independent review evidence. A proposed **or** unreviewed expectation is **not** an accepted oracle. Missing authority, unresolved oracle disagreement **or** unavailable setup blocks the affected comparison.\n2. Freeze these bindings before obtaining the actual judgments. Retain original inputs/outputs **and** supplied, authorized corrected inputs/outputs as separate identified evidence. A correction does **not** silently replace the original case, output **or** expected judgment. Reuse CA-O-018 for admitted test preparation **and** CA-O-020 for actual selected check execution. Retain fresh evaluator output from the bound execution independently of the expected judgments. Do **not** substitute the oracle, corrected output **or** calibration assessment for what the evaluator actually produced.\n3. Compare **every** bound case **and** exact defect occurrence with the independently reviewed expectation. Account for expected findings, actual findings **and** their dispositions, including misses, false positives, duplicates **and** withdrawn findings. Preserve evidence references **and** reasons. Do not hide a difference by changing the oracle, dropping a case, merging distinct occurrences **or** discarding an initial finding. Report mechanical/schema results separately from semantic comparison.\n4. Return the case-level comparison, expected/actual evidence, complete/missing coverage, observed differences, setup/authority/currentness blockers **and** the outcome below. A complete matched comparison supports **only** its bound evaluator/configuration, inputs, oracle **and** criteria. Retain partial evidence **and** the exact unresolved case, binding **or** decision for a caller handoff. Do **not** claim the unfinished portion passed.\n\n## Details\n\n### Outcomes and currentness\n\n| Condition | Returned outcome and evidence |\n| --- | --- |\n| Complete, current actual evidence agrees with the independently reviewed expectations under the admitted criteria, with every case/occurrence and finding disposition accounted for | `matched`, with the exact bindings and case-level comparison; bounded semantic calibration evidence, not a universal evaluator pass |\n| Complete current evidence differs from the reviewed expectations under the admitted comparison criteria, including a seeded defect missed despite schema-valid output, an invented finding, an unsupported duplicate or an incorrectly withdrawn finding | `mismatch`, retaining the exact expected/actual occurrences and dispositions; explaining a difference or obtaining mechanical success does not make this calibrated |\n| Actual evidence or required case/occurrence coverage is missing, pending or unknown | `incomplete`, with completed comparisons and the exact missing evidence; no certification of the missing portion |\n| The independent oracle is missing, unreviewed or disputed; applicable authority, permission, setup or trustworthy execution evidence is unavailable | `blocked`, retaining available evidence and the required admitted resolution; the executor does not settle truth or invent permission to obtain a pass |\n| Evaluator, configuration, case inputs, oracle, criteria or applicable authority no longer matches the frozen execution/comparison binding | `blocked` for current calibration, with the binding mismatch; earlier evidence remains historical evidence for its original binding, not a current result |\n\nAn execution failure retains its actual failure evidence **and** incomplete coverage. Do **not** diagnose an evaluator defect from a failed command alone. A changed binding requires a separately admitted continuation **or** new request. This Action does **not** automatically rerun, repair **or** certify the changed candidate. Unresolved oracle disagreement remains blocked **until** an admitted decision resolves the affected expectation. Preserve the earlier judgment **and** the decision rather than silently rewriting it.\n\n### Actor, reuse and authority boundary\n\nThe caller supplies the authorized executor, independently reviewed oracle **and** evidence handoff location. The executor records actual comparisons **and** blockers. Unresolved authority **or** oracle decisions return **to** the caller/Operator through the admitted decision route. Neither the tested evaluator's assertion **nor** the comparison report replaces governing authority. Any supplied corrected case remains distinguishable from its original **and** must have its own expected/actual binding.\n\nSeparately requested local Atom selection/review reuses CA-O-105/CA-O-106. CA-O-118 checks accounting, **not** semantic correctness. Its coverage result **and** an implementation/schema test pass are **not** substitutes for this comparison. CA-O-104/CA-O-111 retain their existing no-automatic-saved-Atom-recheck boundaries. This Action adds no Workflow **or** Step **to** Base Revise **and** does **not** invoke local review merely because calibration was requested.\n\nNo fixed sample size, twenty-case rule, default discrepancy threshold **or** universal calibration gate is imposed. The admitted request determines the exact case universe **and** criteria. A complete result over that universe makes no unperformed wider-coverage claim. Matched **or** mismatched evidence grants no source correction, automatic repair, rollout, adoption, new source of truth, mandatory post-fix recheck **or** expansion beyond the admitted request.",
    "prose_claim": null,
    "details": null,
    "semantics": null,
    "operation": null
  },
  {
    "ref": "CA-M-504",
    "version": 4,
    "summary": "Remove AI Agent orchestration from the runtime",
    "prose_claim": "Remove automatic AI Agent dispatch and its Codex CLI adapters, AI-Agent transport, mock runners, agentic handlers, AI-Agent Docker service/image stage and credentials setup. Keep the main Docker runtime and MCP transports, the general Workflow engine, durable queue, deterministic Action handlers, MCP, Workbench and host Release commands. Retain RMED source Atoms and persisted historical Run data. A request requiring removed Agent execution must stop with an explicit unsupported result before it is queued or starts effects. Never substitute a mock Agent.",
    "details": null,
    "semantics": null,
    "operation": null
  },
  {
    "ref": "CA-R-1695",
    "version": 38,
    "summary": "Preserve Implementation traceability in the shared Project Journal",
    "prose_claim": "structural Scope Units that realize RMED Atoms.\n\n**Every** structural Scope Unit that realizes RMED Atoms **must** record its Implementation Bindings **in** the shared Project Work Journal. Its admitted Records establish, replace, correct, **or** remove Implementation Bindings. They bind exact Requirement, Method, Evaluation, **and** Delivery Atom Revisions **to** the native implementation targets that declare their realization.\n\nThe Journal is canonical for the declared implementation relationship. Native source, configuration, executable evaluation mechanisms, packages, **and** delivery automation remain canonical for the operative realization itself. Operations evidence **and** Verification remain the authorities for what occurred **and** whether the realization is sufficiently assured. Recording an implementation relationship never proves correctness **or** successful operation.\n\nAn Implementation Binding **must** survive transformations **or** migration of secondary storage history. The binding therefore identifies **every** source Atom by stable artifact identity plus revision digest **and** **every** native implementation target by a stable locator plus content digest. Secondary storage records, review records, Authors, sessions, **and** signatures remain useful provenance but are **not** the sole semantic identity of the binding.\n\nCorrections, replacements, target removal, **and** changed implementation coverage append new records. Accepted Journal records are never edited, reordered, **or** deleted. The effective implementation frontier is derived from the complete ordered record sequence.\n\nImplementation-role Projections are regenerated from the Journal **and** its declared current source **and** target frontier. They **may** present implementation coverage, mappings, missing realization, **and** potentially stale bindings. They remain rebuildable **and** non-authoritative over the Journal, normative Atoms, native implementation, **or** evaluation conclusions.",
    "details": "**Every** implementing Scope Unit **must** preserve storage-independent traceability from exact normative Atom Revisions **to** native implementation targets **in** the shared Project Work Journal **and** derive Implementation Projections from that Journal.",
    "semantics": null,
    "operation": null
  },
  {
    "ref": "CA-O-192",
    "version": 16,
    "summary": "Prepare bound public-release materials\n\n## Action\n\nPrepare bound public-release materials **means** the sole content prompt for one selected Version and source snapshot. It returns the full public PR body and concise Version History summary.\n\n## Details\n\nThe PR body distinguishes What’s new and What’s fixed. README, Version History edits, and all remote effects are mechanical later work. If the actual URL is not yet known, CA-O-198 appends it after PR creation. No placeholder is valid. A different Version or changed code, Methodology, or package requires a fresh full suite before public release.",
    "prose_claim": null,
    "details": null,
    "semantics": null,
    "operation": null
  },
  {
    "ref": "CA-M-125",
    "version": 47,
    "summary": "Assign Subjects from the Claim",
    "prose_claim": "Subject assignment for an Atom from its Claim **and** complete Markdown Main Content.\n\n**To** assign an Atom's Subjects, the Author **must** perform **all** of:\n\n1. Read the entire Markdown Main Content, including Summary, Scope, Claim, Details, other registered sections, nested headings, tables, examples, **and** reference labels. Build an inventory of canonical Subject Target mentions with exact locations **and** full resolved paths. Treat an Atom citation label rendered under `CA-M-444-CORE_META_MODEL-IMPLEMENTATION_METHOD--atom-claims-expose-their-meaning-conditions-and-consequences-clearly` as the referenced Atom's complete filename **without** its `.md` extension **or** directory path. Under `CA-R-1280-CORE_META_MODEL-RULE--reference-every-prerequisite-subject-through-depends-on`, the label is readable reference evidence, **not** a Subject Target mention **or** Subject target, including **when** it occurs **in** the same sentence as Subject Target language. Inventory a Subject Target **only** **when** surrounding prose independently uses it.\n\n   Recognize an evidenced reusable Term through its authoritative Method Atom of Type Term Definition, including the lexical Term `Term` at `Term//Term`. `Evaluation` remains a Term **when** used inside an Evaluation Atom. Use structural definitions, such as `CA-R-1318-CORE_META_MODEL-DEFINITION--define-term` for the Term kind and `CA-R-2514-CORE_META_MODEL-DEFINITION--define-evaluation-content-role` for the Evaluation Content Role, together with the usage context to resolve the referenced Entity target. Those structural definitions do **not** replace the lexical meaning owner. Self-reference alone does **not** remove a mentioned Subject Target from the inventory **or** establish a new Subject Target. A Term's spelling alone does **not** establish its Subject target. A source-admitted instance name after `//`, a selector literal, **or** syntax is **not** automatically a reusable Term. Retain unresolved meaning as an explicit gap rather than treating it as ordinary wording.\n2. Select the **`=1`** canonical Subject Target that the Claim governs **and** reference its narrowest exact Subject Path directly through GOVERNS.\n\n   - For a Claim about entry **or** exit criteria of a Property, apply this same narrowest-target rule rather than substituting its wider bearer.\n   - **When** the Atom has Content Role Evaluation **and** its Claim defines a conformance check, select the canonical target whose conformance is checked. Do **not** select a generic Evaluation label **or** the execution of the check merely from its Content Role. Bind the checked authority separately with `evaluation_for` under `CA-R-1018-CORE_META_MODEL--register-evaluation-targets`.\n3. Connect **every** other Subject Target **in** the mention inventory through DEPENDS_ON using its narrowest exact full Subject Path. Include mentions outside Claim. Do **not** repeat GOVERNS **or** add unmentioned Subject Targets. Unresolved mentions block completion rather than disappearing from the inventory.\n4. For a definition Claim, use its defined Term **in** the Subject Path that identifies the target being defined, under `CA-R-1279-CORE_META_MODEL-RULE--govern-every-defined-term`. Resolve evidenced reusable lexical components through their Method Term Definitions. Resolve a name after `//` through its instance-naming and source authority rather than automatically requiring a Term Definition. The path identifies the target **and** the GOVERNS link is the Subject Relation. The path does **not** define its component Terms.\n5. Split the Atom **before** assignment **when** the Claim governs **`>1`** canonical Subject Targets.\n6. Verify that the distinct GOVERNS **and** DEPENDS_ON targets equal the mention inventory. Record **every** reference once **without** creating an intermediate Subject object, repeating definitions, **or** treating path components **and** implicit bearer prefixes as separate Subject Target mentions.\n7. Serialize the direct references under `CA-D-269-CORE_META_MODEL-DELIVERY--serialize-atom-subjects-in-frontmatter`. Its migration-limited legacy compatibility preserves existing temporal carrier evidence. It does **not** add temporal nesting **to** a migrated flat Carrier.",
    "details": null,
    "semantics": null,
    "operation": null
  }
]

```