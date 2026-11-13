---
identity:
  atom_id: CA-A-1444
  ref_id: CA-A-1444@1-draft
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
  updated_at: '2026-11-12T20:51:58.643605+00:00'
destination:
  file:
    name: CA-A-1444@1-draft-ANALYSIS_REPORT--atom-escalation-benchmark-mzfs9fvs-batch-1.md
    path: .caprmedio_caprmedio/02_analysis_and_advisory/000_draft
---
## Summary

Atom escalation benchmark mzfs9fvs batch 1

## Details

```json
{
  "batch": 1,
  "atoms": [
    {
      "source_ref": "CA-E-633",
      "source_version": 14,
      "candidate": {
        "ref": "CA-E-633",
        "version": 14,
        "summary": "Verify private carrier storage changes\n\n## Scope\n\nThese are required, falsifiable cases for CA-R-1941, CA-D-630, and O215/O216/O217. Use independently authored expected requests and before-and-after ledgers. No test is claimed to have run.\n\n## Claim\n\nThe private variant passes only when independent evidence verifies both its explicitly admitted storage result and its preservation frontier. Missing or contradictory evidence means unresolved or failure. It never means pass or an invented effect.\n\n## Details\n\n### Fixtures and accepted cases\n\nPrepare a bounded temporary root. Include a file, an empty folder, a nested folder with a complete explicit inventory, an unrelated sibling, an occupied destination, a symlinked source/ancestor/destination, an escaping locator, and a deliberately substituted entry. Supply independent evidence of identity, type, content, mode, parent, and permission, plus the expected exact map. Do not derive expected output from the helper.\n\n- Rename a file and an explicitly inventoried folder within the same parent. Require the exact requested new binding, source absence, preserved contents/modes/inventory, and unchanged unrelated entries.\n- Move a file and an explicitly inventoried folder to the exact bound destination. Require source absence, the exact destination, and preservation evidence. Any basename change must be explicit in the approved binding. An inferred rename or merge does not pass.\n- Remove one explicitly approved non-Atom file and one independently confirmed empty non-Atom folder. Require observed absence and unchanged unrelated, protected, and history carriers. No child-removal effect is admitted.\n\n### Exclusive-window fixtures\n\nSupply the exact staged location/absence change, independently resolved private bindings, the complete affected frontier, and a genuine recorded selected Session/Action. Bind the Operator's reviewed change and recorded outside-edits-paused confirmation through the existing trusted authorization binding. Do not use a caller flag, JSON/hash-derived approval, or arbitrary approving callback. Exercise the accepted cases above within the confirmed exclusive window, using independent before-and-after evidence. Raw-helper successes and refusal-only admission tests do not establish positive receiving acceptance.\n\nChange the bound evidence before final revalidation and require refusal without a Carrier effect. Refuse missing, stale, mismatched, or fabricated review/window confirmation before effects. A project-wide Engine write lock or replacement is not required. Other Engine writers are not excluded. A writer that ignores the confirmed window is outside this model; do not claim that a last-moment check prevents that race.\n\n### Refusal and uncertainty cases\n\n1. Reject an unknown private variant, public physical path target, malformed binding, missing permission, unresolved roots, root/ancestor target, escape, missing or ambiguous source, wrong kind, or stale source/parent/destination state without effects.\n2. Reject every symlink/substitution case, destination collision, occupied distinct destination, source-subtree/invalid-overlap destination, overwrite, or merge proposal. Include changes after preview. Do not report refusal as success.\n3. Add, remove, or substitute a folder entry after its approved inventory. Reject the changed frontier; do not expand it. Reject nonempty-folder removal even when a caller supplies a recursive flag or wildcard. Unknown fields fail.\n4. Present current/archived Atom carriers, required history, protected sources, and malformed/uncertain removal classification. Reject all of them. The absence of a recognizable Atom ID alone does not establish non-Atom eligibility.\n5. Supply an internal carrier move from an admitted Atom lifecycle context. Verify only the private storage contribution; the helper does not choose lifecycle metadata or claim that the Atom transition completed. Reject missing or stale lifecycle/history context. Compare every referrer byte before and after: neither rename nor move may invoke O040 or rewrite references.\n6. Verify an already satisfied, unchanged rename/move request as a no-op only with current evidence. A missing expected-present source is failure, not proof of a previous effect. For removal, a bound already-absent cleanup state is a no-op only when that exact absence was expected and permission/eligibility remains valid.\n7. Inject effect, readback, and verification failures. Preserve attributable known partial effects; unknown effects require `effect_uncertain`. Nonempty errors cannot indicate success. An exception-free, unverified result cannot return empty errors. A no-op must prove the requested state is unchanged.\n\n### Acceptance and disposition\n\nCompare exact independent before/proposed/after ledgers, resolved bindings, and actual effect/error evidence. Reject any widened set, hidden reference/lifecycle decision, lost preservation evidence, or false completion. Retain unresolved evidence and known effects, including failed verification after an effect. Unknown effects require `effect_uncertain` and no automatic retry. Reuse only the approved exclusive-window boundary. Do not infer automatic rollback, cleanup restoration, retry, resume, replay, or a stronger concurrent-publication guarantee. These are rules and isolated test-fixture requirements only. They establish neither live cleanup nor production activation. This source specifies future functional checks, not packet acceptance.",
        "prose_claim": null,
        "details": null,
        "semantics": null,
        "operation": null
      },
      "gate": {
        "ref": "CA-E-633",
        "confidence": "high",
        "escalate": false,
        "reason": "No material change found. Source requires independent verification of the admitted storage result and preservation frontier; Draft retains both, the refusal boundaries, the outside-edits-paused window, and the limits on effects and concurrency claims."
      },
      "final": {
        "ref": "CA-E-633",
        "version": 14,
        "summary": "Verify private carrier storage changes\n\n## Scope\n\nThese are required, falsifiable cases for CA-R-1941, CA-D-630, and O215/O216/O217. Use independently authored expected requests and before-and-after ledgers. No test is claimed to have run.\n\n## Claim\n\nThe private variant passes only when independent evidence verifies both its explicitly admitted storage result and its preservation frontier. Missing or contradictory evidence means unresolved or failure. It never means pass or an invented effect.\n\n## Details\n\n### Fixtures and accepted cases\n\nPrepare a bounded temporary root. Include a file, an empty folder, a nested folder with a complete explicit inventory, an unrelated sibling, an occupied destination, a symlinked source/ancestor/destination, an escaping locator, and a deliberately substituted entry. Supply independent evidence of identity, type, content, mode, parent, and permission, plus the expected exact map. Do not derive expected output from the helper.\n\n- Rename a file and an explicitly inventoried folder within the same parent. Require the exact requested new binding, source absence, preserved contents/modes/inventory, and unchanged unrelated entries.\n- Move a file and an explicitly inventoried folder to the exact bound destination. Require source absence, the exact destination, and preservation evidence. Any basename change must be explicit in the approved binding. An inferred rename or merge does not pass.\n- Remove one explicitly approved non-Atom file and one independently confirmed empty non-Atom folder. Require observed absence and unchanged unrelated, protected, and history carriers. No child-removal effect is admitted.\n\n### Exclusive-window fixtures\n\nSupply the exact staged location/absence change, independently resolved private bindings, the complete affected frontier, and a genuine recorded selected Session/Action. Bind the Operator's reviewed change and recorded outside-edits-paused confirmation through the existing trusted authorization binding. Do not use a caller flag, JSON/hash-derived approval, or arbitrary approving callback. Exercise the accepted cases above within the confirmed exclusive window, using independent before-and-after evidence. Raw-helper successes and refusal-only admission tests do not establish positive receiving acceptance.\n\nChange the bound evidence before final revalidation and require refusal without a Carrier effect. Refuse missing, stale, mismatched, or fabricated review/window confirmation before effects. A project-wide Engine write lock or replacement is not required. Other Engine writers are not excluded. A writer that ignores the confirmed window is outside this model; do not claim that a last-moment check prevents that race.\n\n### Refusal and uncertainty cases\n\n1. Reject an unknown private variant, public physical path target, malformed binding, missing permission, unresolved roots, root/ancestor target, escape, missing or ambiguous source, wrong kind, or stale source/parent/destination state without effects.\n2. Reject every symlink/substitution case, destination collision, occupied distinct destination, source-subtree/invalid-overlap destination, overwrite, or merge proposal. Include changes after preview. Do not report refusal as success.\n3. Add, remove, or substitute a folder entry after its approved inventory. Reject the changed frontier; do not expand it. Reject nonempty-folder removal even when a caller supplies a recursive flag or wildcard. Unknown fields fail.\n4. Present current/archived Atom carriers, required history, protected sources, and malformed/uncertain removal classification. Reject all of them. The absence of a recognizable Atom ID alone does not establish non-Atom eligibility.\n5. Supply an internal carrier move from an admitted Atom lifecycle context. Verify only the private storage contribution; the helper does not choose lifecycle metadata or claim that the Atom transition completed. Reject missing or stale lifecycle/history context. Compare every referrer byte before and after: neither rename nor move may invoke O040 or rewrite references.\n6. Verify an already satisfied, unchanged rename/move request as a no-op only with current evidence. A missing expected-present source is failure, not proof of a previous effect. For removal, a bound already-absent cleanup state is a no-op only when that exact absence was expected and permission/eligibility remains valid.\n7. Inject effect, readback, and verification failures. Preserve attributable known partial effects; unknown effects require `effect_uncertain`. Nonempty errors cannot indicate success. An exception-free, unverified result cannot return empty errors. A no-op must prove the requested state is unchanged.\n\n### Acceptance and disposition\n\nCompare exact independent before/proposed/after ledgers, resolved bindings, and actual effect/error evidence. Reject any widened set, hidden reference/lifecycle decision, lost preservation evidence, or false completion. Retain unresolved evidence and known effects, including failed verification after an effect. Unknown effects require `effect_uncertain` and no automatic retry. Reuse only the approved exclusive-window boundary. Do not infer automatic rollback, cleanup restoration, retry, resume, replay, or a stronger concurrent-publication guarantee. These are rules and isolated test-fixture requirements only. They establish neither live cleanup nor production activation. This source specifies future functional checks, not packet acceptance.",
        "prose_claim": null,
        "details": null,
        "semantics": null,
        "operation": null
      },
      "terra_issues": []
    },
    {
      "source_ref": "CA-E-287",
      "source_version": 19,
      "candidate": {
        "ref": "CA-E-287",
        "version": 19,
        "summary": "Distinguish one protocol failure from one Tool failure",
        "prose_claim": "MCP returns stable, model-readable responses that distinguish a protocol failure from a canonical Tool failure.",
        "details": "### Test case\n\nProduce one invalid protocol message and one valid message whose canonical Tool returns a structured failure.\n\n### Acceptance criteria\n\nThe responses are distinct, retain applicable provenance, and expose no internal implementation detail.\n\n### Failure disposition\n\nReject the result adapter until it preserves this distinction.",
        "semantics": null,
        "operation": null
      },
      "gate": {
        "ref": "CA-E-287",
        "confidence": "high",
        "escalate": false,
        "reason": "No material change found. Source's invalid protocol message and valid message with a structured Tool failure remain distinct test inputs; provenance, no-internal-detail, and reject-until-preserved criteria remain intact."
      },
      "final": {
        "ref": "CA-E-287",
        "version": 19,
        "summary": "Distinguish one protocol failure from one Tool failure",
        "prose_claim": "MCP returns stable, model-readable responses that distinguish a protocol failure from a canonical Tool failure.",
        "details": "### Test case\n\nProduce one invalid protocol message and one valid message whose canonical Tool returns a structured failure.\n\n### Acceptance criteria\n\nThe responses are distinct, retain applicable provenance, and expose no internal implementation detail.\n\n### Failure disposition\n\nReject the result adapter until it preserves this distinction.",
        "semantics": null,
        "operation": null
      },
      "terra_issues": []
    },
    {
      "source_ref": "CA-R-1692",
      "source_version": 39,
      "candidate": {
        "ref": "CA-R-1692",
        "version": 39,
        "summary": "Requirement — Freeze a version only at release",
        "prose_claim": "Target Versions and their selected authorized release events.\n\nA target Version must remain mutable until its selected authorized release event succeeds and the shared Journal records that outcome for the exact released candidate.\n\n- Under CA-R-1712, the release record is a factual Journal Record, not an Operations Atom.\n- Its exact manifest binds the released governing Atom Revisions, Implementation and Delivery Revisions, applicable Evaluations and evidence, and the release identifier.\n- The selected release policy defines the event boundary. Applicable Delivery authority defines the manifest and Journal representation. A selected Extension owns mechanism-specific references.\n- Planning allocation, implementation completion, readiness acceptance, or release-candidate naming does not freeze the Version before the successful event.",
        "details": "This Project Configuration Claim does not impose its release Workflow on every Project.",
        "semantics": null,
        "operation": null
      },
      "gate": {
        "ref": "CA-R-1692",
        "confidence": "high",
        "escalate": false,
        "reason": "No material change found. The Draft retains the freeze condition: successful selected authorized release plus shared Journal recording for the exact candidate; manifest, authority, event boundary, and non-universal scope remain."
      },
      "final": {
        "ref": "CA-R-1692",
        "version": 39,
        "summary": "Requirement — Freeze a version only at release",
        "prose_claim": "Target Versions and their selected authorized release events.\n\nA target Version must remain mutable until its selected authorized release event succeeds and the shared Journal records that outcome for the exact released candidate.\n\n- Under CA-R-1712, the release record is a factual Journal Record, not an Operations Atom.\n- Its exact manifest binds the released governing Atom Revisions, Implementation and Delivery Revisions, applicable Evaluations and evidence, and the release identifier.\n- The selected release policy defines the event boundary. Applicable Delivery authority defines the manifest and Journal representation. A selected Extension owns mechanism-specific references.\n- Planning allocation, implementation completion, readiness acceptance, or release-candidate naming does not freeze the Version before the successful event.",
        "details": "This Project Configuration Claim does not impose its release Workflow on every Project.",
        "semantics": null,
        "operation": null
      },
      "terra_issues": []
    },
    {
      "source_ref": "CA-O-165",
      "source_version": 23,
      "candidate": {
        "ref": "CA-O-165",
        "version": 23,
        "summary": "Validate local release inputs\n\n## Action\n\nValidate local release inputs is the Action that checks explicit local-release inputs and configured delivery paths for file/path safety before the declared local validation scope. The complete discovered suite is the default. A focused scope requires the explicit current Operator record admitted by CA-O-164.\n\n## Scope\n\nCheck the configured source and delivery paths, Project Structure, protected settings, compiler, and target paths `LAYER_1_FRAMEWORK_METHODOLOGY/` and `.caprmedio_caprmedio/000_CAPRMEDIO_framework/` for ordinary input and file/path safety. This Action does not separately validate Active Atom metadata, placement, or relations. Release verification uses the declared scope and records whether it is complete or focused.\n\n## Details\n\nMissing, ambiguous, or unsafe required input stops processing before tests or delivery writes and is reported for manual handling. This Action does not copy or clear product or installed contents, compile, install, push, or open a PR.",
        "prose_claim": null,
        "details": null,
        "semantics": null,
        "operation": null
      },
      "gate": {
        "ref": "CA-O-165",
        "confidence": "high",
        "escalate": false,
        "reason": "No material change found. The complete discovered suite remains default, focused scope still requires the explicit current Operator record, and unsafe or missing inputs still stop before tests or delivery writes."
      },
      "final": {
        "ref": "CA-O-165",
        "version": 23,
        "summary": "Validate local release inputs\n\n## Action\n\nValidate local release inputs is the Action that checks explicit local-release inputs and configured delivery paths for file/path safety before the declared local validation scope. The complete discovered suite is the default. A focused scope requires the explicit current Operator record admitted by CA-O-164.\n\n## Scope\n\nCheck the configured source and delivery paths, Project Structure, protected settings, compiler, and target paths `LAYER_1_FRAMEWORK_METHODOLOGY/` and `.caprmedio_caprmedio/000_CAPRMEDIO_framework/` for ordinary input and file/path safety. This Action does not separately validate Active Atom metadata, placement, or relations. Release verification uses the declared scope and records whether it is complete or focused.\n\n## Details\n\nMissing, ambiguous, or unsafe required input stops processing before tests or delivery writes and is reported for manual handling. This Action does not copy or clear product or installed contents, compile, install, push, or open a PR.",
        "prose_claim": null,
        "details": null,
        "semantics": null,
        "operation": null
      },
      "terra_issues": []
    },
    {
      "source_ref": "CA-M-468",
      "source_version": 8,
      "candidate": {
        "ref": "CA-M-468",
        "version": 8,
        "summary": "Use a simple SQL editor for Workbench",
        "prose_claim": "Use CodeMirror 6 SQL support and read-only `query_schema({})` metadata. The metadata includes `atoms` name/type/optional values, `scope_units` name/type, and technical `change_log` fields `observed_at`, `operation`, `old_path`, and `new_path` only. Complete actual tables and declared dotted snake_case `content.*` columns, and quote identifiers as needed. Do not read saved SQL for suggestions or expose space-based Content names.\n\nEach Tab holds one query. Preserve quotes, comments, and CTEs, and distinguish delimiters inside them. Under CA-R-2728, send the complete query for Run or Check. CodeMirror provides editing, highlighting, and completion. Cmd+Enter runs; Shift+Cmd+Enter checks. Run & Save follows a successful Run, and Save snapshots the complete text. Completion never executes SQL, saves, or changes results. For a single-quoted equality prefix on actual Header Status, offer the metadata value with correct escaping and a closing quote.\n\nFormat with DuckDB dialect `@dlh.io/dlh-sql-formatter` 1.3.0 through a small token-aware adapter and the existing CodeMirror parser. Use two-space indentation, leading commas, uppercase SELECT, lowercase clauses, and a newline before the semicolon. Keep FROM/WHERE attached to the following expression when no separating comment exists. Preserve expressions, identifiers, strings, comments, CTEs, and nesting. Apply formatting through the normal editor change path; accepted formatting is idempotent. On failure, show an error and preserve the editor and results. Do not add parser, formatter, or backend capability. Native execution verification remains future work and has not run.",
        "details": null,
        "semantics": null,
        "operation": null
      },
      "gate": {
        "ref": "CA-M-468",
        "confidence": "high",
        "escalate": false,
        "reason": "No material change found. The Draft preserves query behavior, shortcuts, completion limits, formatter constraints, failure behavior, and the statement that native execution verification has not run."
      },
      "final": {
        "ref": "CA-M-468",
        "version": 8,
        "summary": "Use a simple SQL editor for Workbench",
        "prose_claim": "Use CodeMirror 6 SQL support and read-only `query_schema({})` metadata. The metadata includes `atoms` name/type/optional values, `scope_units` name/type, and technical `change_log` fields `observed_at`, `operation`, `old_path`, and `new_path` only. Complete actual tables and declared dotted snake_case `content.*` columns, and quote identifiers as needed. Do not read saved SQL for suggestions or expose space-based Content names.\n\nEach Tab holds one query. Preserve quotes, comments, and CTEs, and distinguish delimiters inside them. Under CA-R-2728, send the complete query for Run or Check. CodeMirror provides editing, highlighting, and completion. Cmd+Enter runs; Shift+Cmd+Enter checks. Run & Save follows a successful Run, and Save snapshots the complete text. Completion never executes SQL, saves, or changes results. For a single-quoted equality prefix on actual Header Status, offer the metadata value with correct escaping and a closing quote.\n\nFormat with DuckDB dialect `@dlh.io/dlh-sql-formatter` 1.3.0 through a small token-aware adapter and the existing CodeMirror parser. Use two-space indentation, leading commas, uppercase SELECT, lowercase clauses, and a newline before the semicolon. Keep FROM/WHERE attached to the following expression when no separating comment exists. Preserve expressions, identifiers, strings, comments, CTEs, and nesting. Apply formatting through the normal editor change path; accepted formatting is idempotent. On failure, show an error and preserve the editor and results. Do not add parser, formatter, or backend capability. Native execution verification remains future work and has not run.",
        "details": null,
        "semantics": null,
        "operation": null
      },
      "terra_issues": []
    },
    {
      "source_ref": "CA-R-1349",
      "source_version": 21,
      "candidate": {
        "ref": "CA-R-1349",
        "version": 21,
        "summary": "Identify one Type Property slot",
        "prose_claim": "Qualified Type Subjects of an Entity occurrence.\n\nAll qualified Type Subjects of `=1` Entity occurrence must identify the same Type Property.",
        "details": null,
        "semantics": null,
        "operation": null
      },
      "gate": {
        "ref": "CA-R-1349",
        "confidence": "high",
        "escalate": false,
        "reason": "No material change found. Source and Draft both require all qualified Type Subjects of a `=1` Entity occurrence to identify the same Type Property."
      },
      "final": {
        "ref": "CA-R-1349",
        "version": 21,
        "summary": "Identify one Type Property slot",
        "prose_claim": "Qualified Type Subjects of an Entity occurrence.\n\nAll qualified Type Subjects of `=1` Entity occurrence must identify the same Type Property.",
        "details": null,
        "semantics": null,
        "operation": null
      },
      "terra_issues": []
    },
    {
      "source_ref": "CA-O-217",
      "source_version": 12,
      "candidate": {
        "ref": "CA-O-217",
        "version": 12,
        "summary": "Remove one non-Atom storage carrier\n\n## Operation\n\nRemove One Non-Atom Storage Carrier is the reusable private cleanup Action. It removes exactly one explicitly approved non-Atom file or empty folder behind an admitted logical connector `modify`. It is not an Atom deletion or a recursively selected cleanup set.\n\n### Inputs and preconditions\n\nRequire CA-D-630's private remove binding, approved root/parent, exact expected state, positive non-Atom cleanup eligibility, and explicit permission/context. Reject a root/ancestor, escape, symlink/substitution, nonempty folder, current or historical Atom carrier, required history, protected source, missing eligibility, or stale/ambiguous state. An unrecognized or absent ID does not prove non-Atom status.\n\n### Action and result\n\nRequire CA-R-1941's exact staged-cleanup review and fresh trusted authorization/window record, including recorded outside-edits-paused confirmation. Within that confirmed window, recheck exact positive non-Atom eligibility, classification, root/parent, source state, empty-folder evidence, preservation, authority, and permission frontier before the effect. Retain independent readback and verification. Remove only the bound file or empty folder. Never discover child targets, follow a symlink, accept a wildcard/recursive flag, or touch a destination, referrer, or unrelated carrier. Independently verify observed absence and the unchanged preservation frontier.\n\nReturn CA-D-625's actual data/current_state/effects/errors. A bound already-absent cleanup state is a no-op only when that exact absence was expected, eligibility and permission remain valid, and unchanged requested state is independently verified. A missing expected-present source is failure, not inferred completion. Retain known partial effects. Unknown effects require `effect_uncertain`, and errors cannot indicate success.\n\n## Details\n\nAtom removal remains the existing admitted Archive/retire lifecycle with required history. O217 supplies no delete-Atom operation. No automatic set expansion, recovery/retry/resume policy, implementation, or runtime route is established.",
        "prose_claim": null,
        "details": null,
        "semantics": null,
        "operation": null
      },
      "gate": {
        "ref": "CA-O-217",
        "confidence": "high",
        "escalate": false,
        "reason": "No material change found. The Draft retains exactly-one-file-or-empty-folder removal, eligibility and authorization/window checks, no-op conditions, failure handling, and the existing Atom lifecycle boundary."
      },
      "final": {
        "ref": "CA-O-217",
        "version": 12,
        "summary": "Remove one non-Atom storage carrier\n\n## Operation\n\nRemove One Non-Atom Storage Carrier is the reusable private cleanup Action. It removes exactly one explicitly approved non-Atom file or empty folder behind an admitted logical connector `modify`. It is not an Atom deletion or a recursively selected cleanup set.\n\n### Inputs and preconditions\n\nRequire CA-D-630's private remove binding, approved root/parent, exact expected state, positive non-Atom cleanup eligibility, and explicit permission/context. Reject a root/ancestor, escape, symlink/substitution, nonempty folder, current or historical Atom carrier, required history, protected source, missing eligibility, or stale/ambiguous state. An unrecognized or absent ID does not prove non-Atom status.\n\n### Action and result\n\nRequire CA-R-1941's exact staged-cleanup review and fresh trusted authorization/window record, including recorded outside-edits-paused confirmation. Within that confirmed window, recheck exact positive non-Atom eligibility, classification, root/parent, source state, empty-folder evidence, preservation, authority, and permission frontier before the effect. Retain independent readback and verification. Remove only the bound file or empty folder. Never discover child targets, follow a symlink, accept a wildcard/recursive flag, or touch a destination, referrer, or unrelated carrier. Independently verify observed absence and the unchanged preservation frontier.\n\nReturn CA-D-625's actual data/current_state/effects/errors. A bound already-absent cleanup state is a no-op only when that exact absence was expected, eligibility and permission remain valid, and unchanged requested state is independently verified. A missing expected-present source is failure, not inferred completion. Retain known partial effects. Unknown effects require `effect_uncertain`, and errors cannot indicate success.\n\n## Details\n\nAtom removal remains the existing admitted Archive/retire lifecycle with required history. O217 supplies no delete-Atom operation. No automatic set expansion, recovery/retry/resume policy, implementation, or runtime route is established.",
        "prose_claim": null,
        "details": null,
        "semantics": null,
        "operation": null
      },
      "terra_issues": []
    },
    {
      "source_ref": "CA-D-309",
      "source_version": 27,
      "candidate": {
        "ref": "CA-D-309",
        "version": 27,
        "summary": "Bind Materialized Representations to Regeneration Sources",
        "prose_claim": "Admitted materialized representation Carriers.\n\nEvery admitted materialized representation Carrier must have a recoverable binding to its exact canonical source Revision and `=1` deterministic regeneration or reconciliation rule.\n\nThe binding may be recovered through the selected authoritative source frontier and governing derivation authority. Source metadata does not have to be embedded in every resulting Carrier. An applicable Carrier specification determines whether and how an explicit binding is serialized.\n\nFor Applicable Methodology projected Atom Carriers, CA-D-305 requires an explicit one-way binding to the original source Atom Carrier. Preserve its authored content, identity, and Revision. This specific binding must not create duplicate source authority or impose a blanket persisted source frontier on other Projections contrary to CA-R-1494.",
        "details": null,
        "semantics": null,
        "operation": null
      },
      "gate": {
        "ref": "CA-D-309",
        "confidence": "high",
        "escalate": false,
        "reason": "No material change found. The Draft preserves the recoverable exact-source and deterministic-rule binding, the allowance for recovered rather than embedded metadata, and the specific one-way projected-Atom binding without imposing a blanket frontier."
      },
      "final": {
        "ref": "CA-D-309",
        "version": 27,
        "summary": "Bind Materialized Representations to Regeneration Sources",
        "prose_claim": "Admitted materialized representation Carriers.\n\nEvery admitted materialized representation Carrier must have a recoverable binding to its exact canonical source Revision and `=1` deterministic regeneration or reconciliation rule.\n\nThe binding may be recovered through the selected authoritative source frontier and governing derivation authority. Source metadata does not have to be embedded in every resulting Carrier. An applicable Carrier specification determines whether and how an explicit binding is serialized.\n\nFor Applicable Methodology projected Atom Carriers, CA-D-305 requires an explicit one-way binding to the original source Atom Carrier. Preserve its authored content, identity, and Revision. This specific binding must not create duplicate source authority or impose a blanket persisted source frontier on other Projections contrary to CA-R-1494.",
        "details": null,
        "semantics": null,
        "operation": null
      },
      "terra_issues": []
    },
    {
      "source_ref": "CA-M-442",
      "source_version": 5,
      "candidate": {
        "ref": "CA-M-442",
        "version": 5,
        "summary": "An Atom's content expresses one scoped contribution with a faithful Summary and Translations.",
        "prose_claim": "Authoring an Atom's prose CCE primary contribution, its applicability, and its derived Summary. The same Claim may contain readable prose and an optional R-only nested Formal claim under the Claim definition.\n\nTo author one CCE Claim and its derived Summary, an Author must follow these constraints:\n\n- Express `=1` coherent contribution. Its full meaning must be covered by one precise Summary that uses the applicable CCE Content Role profile. Carry the contribution under the primary contribution heading registered for that Content Role. Do not impose the literal heading Claim on every role.\n- Resolve `=1` Claim Target Scope Unit independently of ownership. Use the current Scope Unit as the authoring default, or select a different target when explicitly permitted. Carry the resolved value under the target Scope Unit carrier definition. Express applicability under the applicability carrier definition. For RMED, describe in Scope what the Claim applies to, including applicable conditions and exclusions. Do not merely repeat the carried current or target Scope Unit. Those restrictions alone do not make the Atom Relational.\n- Keep Details within the primary contribution. For RMED, read the Claim within its Scope; Details must not change either. If supporting content reveals an incomplete or inaccurate contribution or applicability, revise the affected Scope or primary contribution explicitly and recheck agreement. Do not hide the change in Details.\n- Write the Summary only after completing the other body sections and contribution review. Shorten the finalized primary contribution. Use plain wording that expresses the Claim's meaning. Preserve established principle names such as DRY and MECE instead of paraphrasing them. A familiar name or short instruction may be the Summary; do not force it into a declarative sentence. For RMED, summarize the Claim within its finalized Scope, not the Scope alone. Do not use supporting Results or TLDR as the source.\n- For an existing Atom, retain the established Summary and check that it is faithful. If it needs to change, use a new Atom identity under the Atom identity rule.\n- Derive every Translation from the full corresponding source content, not the Summary.",
        "details": null,
        "semantics": null,
        "operation": null
      },
      "gate": {
        "ref": "CA-M-442",
        "confidence": "high",
        "escalate": false,
        "reason": "No material change found. The Draft retains the contribution, scope, applicability, details, summary, existing-Atom identity, and full-source Translation constraints; pronouns such as 'Its full meaning' and 'If it needs to change' have clear antecedents in context."
      },
      "final": {
        "ref": "CA-M-442",
        "version": 5,
        "summary": "An Atom's content expresses one scoped contribution with a faithful Summary and Translations.",
        "prose_claim": "Authoring an Atom's prose CCE primary contribution, its applicability, and its derived Summary. The same Claim may contain readable prose and an optional R-only nested Formal claim under the Claim definition.\n\nTo author one CCE Claim and its derived Summary, an Author must follow these constraints:\n\n- Express `=1` coherent contribution. Its full meaning must be covered by one precise Summary that uses the applicable CCE Content Role profile. Carry the contribution under the primary contribution heading registered for that Content Role. Do not impose the literal heading Claim on every role.\n- Resolve `=1` Claim Target Scope Unit independently of ownership. Use the current Scope Unit as the authoring default, or select a different target when explicitly permitted. Carry the resolved value under the target Scope Unit carrier definition. Express applicability under the applicability carrier definition. For RMED, describe in Scope what the Claim applies to, including applicable conditions and exclusions. Do not merely repeat the carried current or target Scope Unit. Those restrictions alone do not make the Atom Relational.\n- Keep Details within the primary contribution. For RMED, read the Claim within its Scope; Details must not change either. If supporting content reveals an incomplete or inaccurate contribution or applicability, revise the affected Scope or primary contribution explicitly and recheck agreement. Do not hide the change in Details.\n- Write the Summary only after completing the other body sections and contribution review. Shorten the finalized primary contribution. Use plain wording that expresses the Claim's meaning. Preserve established principle names such as DRY and MECE instead of paraphrasing them. A familiar name or short instruction may be the Summary; do not force it into a declarative sentence. For RMED, summarize the Claim within its finalized Scope, not the Scope alone. Do not use supporting Results or TLDR as the source.\n- For an existing Atom, retain the established Summary and check that it is faithful. If it needs to change, use a new Atom identity under the Atom identity rule.\n- Derive every Translation from the full corresponding source content, not the Summary.",
        "details": null,
        "semantics": null,
        "operation": null
      },
      "terra_issues": []
    },
    {
      "source_ref": "CA-D-282",
      "source_version": 26,
      "candidate": {
        "ref": "CA-D-282",
        "version": 26,
        "summary": "Serialize Filename Summary Slug from Summary",
        "prose_claim": "Atom Filenames and their Summary Slugs.\n\nEvery Atom Filename Summary Slug must be the lowercase ASCII kebab-case serialization of the complete Atom Summary.",
        "details": null,
        "semantics": null,
        "operation": null
      },
      "gate": {
        "ref": "CA-D-282",
        "confidence": "high",
        "escalate": false,
        "reason": "No material change found. The Draft preserves the requirement that every Atom Filename Summary Slug be the lowercase ASCII kebab-case serialization of the complete Atom Summary."
      },
      "final": {
        "ref": "CA-D-282",
        "version": 26,
        "summary": "Serialize Filename Summary Slug from Summary",
        "prose_claim": "Atom Filenames and their Summary Slugs.\n\nEvery Atom Filename Summary Slug must be the lowercase ASCII kebab-case serialization of the complete Atom Summary.",
        "details": null,
        "semantics": null,
        "operation": null
      },
      "terra_issues": []
    }
  ]
}
```
