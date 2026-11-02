# Generated Atom content — unified prompt test

These are the twelve actual v4 outputs. No output was applied to a source Atom. The bodies were preserved; the prompt generated the missing Summaries. Code blocks preserve the original heading levels.

## 1. CA-R-2446

````markdown
## Summary

Show gateway health, recent Tool and Workflow observations, and safe errors

## Claim scope

The existing MCP HTTP Gateway **and** its process-local diagnostic view, **without** replacing canonical execution history.

## Claim

MCP **must** expose a browser view at `/health` on the same listener. The view shows:

- bounded health observations;
- recent Tool calls;
- recent Workflow observations with status; **and**
- safe error details.

Preserve the current machine JSON `ready` boolean **and** readiness HTTP status semantics. The diagnostic view is non-authoritative. It **must not** infer successful Tool **or** Workflow execution from gateway liveness, scheduler completion, **or** absence of observations.

## Details

- Render the browser view for explicit `Accept: text/html`. Default, `application/json`, **and** `*/*` requests retain the existing machine representation. Preserve the existing loopback Host/Origin boundary; add no HTTP credential behavior.
- Observe actual Gateway calls **and** results **only**. Retain at most 32 recent Tool-call observations **and** at most 32 recent Workflow observations in process-local memory. Label since-start coverage **and** reset it on restart. This is **not** persistent, cross-process, **or** complete execution history.
- Tool observations identify the admitted Tool name, observation time, returned **or** observed outcome, **and** a fixed safe error category. Do **not** label an ordinary returned response as proof of completed domain effects. Preserve rejected, failed, partial, canceled, **and** uncertain outcomes **without** replay.
- Workflow observations use **only** known Run identities **and** actual call results. Keep `scheduler_status` separate from actual Workflow outcome **or** disposition; queued **or** pending is **not** successful completion. An unobserved actual outcome is unknown even **if** a scheduler reports `SUCCESS`.
- Show gateway generation/process availability **and** registry availability separately from provider-call observations **and** Workflow/worker observations. Last observations are historical facts, **not** live probes. Missing, stale, **or** untested state remains unknown **and** is **not** promoted to healthy.
- Retain **and** display none of: raw arguments, raw results, credentials, absolute paths, **or** provider exception text. Use fixed safe error categories with explanatory labels, including timeout, connection, returned-error, **and** uncertain **where** actually known. Escape **every** dynamic HTML field. Bounded history **must not** grow with arbitrary request sizes.
- A health GET reads the existing snapshot **only**. It does **none** of the following:
  - invoke a Tool **or** Workflow;
  - initialize DBOS/Docker state;
  - scan a Journal;
  - start, reload, **or** recover anything;
  - perform a mutation; **or**
  - replay an uncertain call **or** held Run.
- Keep canonical sources, Journals, **and** execution outcome evidence distinct from this convenience view.
````

## 2. CA-O-238

````markdown
## Summary

Check code candidates against the complete applicable Method-policy set and current Evaluation and diagnosis evidence

## Operation

Code Candidate Semantic Review **means** the read-only Action that checks:

- The candidate;
- actual Evaluation **and** diagnosis evidence; **and**
- selected current R/M/E/D **and** Project-owned Tier 0 Atom bindings.

It assesses the complete bound applicable Method-policy set **and** reuses its meaning. It does **not** create **or** duplicate policy. Map each applicable obligation to its Evaluation predicate **and** current evidence, **or** retain an explicit gap. Record inapplicability with a reason rather than silently omitting an obligation. Missing required coverage is unresolved; a selected subset of green linters is **not** complete review evidence.

The optional `review_phase` is final by default, preserving standalone review behavior. In preliminary phase, assess the available candidate **and** complete bound code/policy assessment **without** pretending pending final checks have run. Return `preliminary_clear` **only** when that assessment has no confirmed findings. List every pending check **and** current source/candidate binding. Preliminary clearance is neither `passed` nor acceptance. Return `findings` for confirmed defects, `partial` for unfinished selected assessment, **and** `unresolved` when required authority, context, coverage, **or** permissions are missing.

Final assessment requires actual complete current evidence bound to the same candidate, test definitions, applicable authority, portfolio, **and** inputs. Changed relevant bytes invalidate affected evidence.

Return:

- `passed` **only** when every selected assessment is current **and** complete with no findings;
- `findings` when selected assessment is complete **and** confirms implementation defects, test issues, **or** an admitted expected-phase observation;
- `partial` when actual selected assessment work remains unfinished; **or**
- `unresolved` **only** when required evidence, authority, context, **or** permission is missing **or** blocked. Retain completed findings **and** actual results.

For labels from `CA-O-089-PROJECT_CONFIGURATION-ACTION--diagnose-implementation-test-failures`, map implementation/test defect to `findings` **and** authority/environment/unresolved to `unresolved`. `expected_initial_failure` remains an expected-phase observation **and** cannot produce an accepted-candidate claim **unless** admitted expected-phase criteria genuinely hold.

## Details

Perform no automatic fix, source/Atom edit, expected-result edit, retry, promotion, release, **or** Journal-completeness gate. Read-only commands are allowed; temporary fixture writes require explicit permission. Distinguish test issue, implementation defect, authority/environment blocker, expected-phase observation, **and** non-proven concern.
````

## 3. CA-O-239

````markdown
## Summary

Review code candidate evidence and applicable Method policy during shared implementation of Evaluations before required behavior

## Operation

Shared Implementation Review Step **means** the node of `CA-O-016-PROJECT_CONFIGURATION-WORKFLOW--implement-evaluations-before-required-behavior` that invokes exactly one Action, `CA-O-238-PROJECT_CONFIGURATION-ACTION--review-code-candidate-evidence-and-applicable-method-policy-without-editing`, in explicit Integrated context under `CA-R-1527-CORE_META_MODEL-DEFINITION--define-agentic-step-execution-context`.

- Require explicit `review_phase` preliminary **or** final from `CA-O-231-PROJECT_CONFIGURATION-STEP--prepare-shared-context-implementation-work`. Do **not** derive the phase from absent evidence **or** use the standalone default.
- Bind:
  - the selected Project, bounded request **and** P/Plan;
  - the owned candidate **and** changed paths;
  - direct full `requirements`, `methods`, `evaluations`, **and** `delivery` rows with applicable Project-owned Tier 0 Atom sources;
  - the substantive obligation/coverage map;
  - actual check **and** diagnosis evidence with pending/stale outcomes;
  - relevant inputs **and** permissions; **and**
  - retained findings **and** remaining retry/resource state.
- An optional legacy `method_projection` **may** accompany direct rows but is **not** required.
- Retain the participating session **without** replacing complete source-bound inputs with conversational memory. Revalidate source/candidate/test/input bindings before assessment **and** preserve actual partial findings.
- Pass `preliminary_clear`, `passed`, `findings`, `partial`, **or** `unresolved` directly to `CA-O-016-PROJECT_CONFIGURATION-WORKFLOW--implement-evaluations-before-required-behavior`. Read-only review never edits code, changes authority, grants a retry, **or** launches release; repairs remain in the enclosing implementation Workflow.
- Preserve exact Action/Step revisions, candidate **and** evidence bindings, actual effects, **and** returned results.
````

## 4. CA-E-667

````markdown
## Summary

Check Project-wide foundation and Core commitments for valid ownership, support, and classification

## Claim

The Project-wide foundation and Core set Evaluation **must** return `fail` **if** **any** of the following applies:

- A known Project-wide invariant has no canonical owner;
- A Project-wide foundational commitment is **only** a narrow application rather than a broad commitment;
- A required supporting Core Claim is absent;
- Claims conflict **or** independently duplicate authority **in** the same context; **or**
- An Atom has an incompatible Local Tier **or** Content Role.

**otherwise**, the Evaluation **may** return `pass` for the reviewed frontier **without** claiming that undiscovered gaps are impossible.

Evaluate the Content Roles of Project-wide foundational commitments by checking whether each Atom's complete primary contribution matches its applicable Content Role definition. The former Actor-policy interpretation of Plan does **not** create an exception **to** current Content Role authority.

Faithful Core specialization **must not** count as duplicate authority. **none** of the following **may** be acceptance conditions:

- fixed child counts;
- A universal RMED checklist per Project-wide foundational commitment;
- expansion from Intent; **or**
- formula/text equivalence.

Report missing support **and** conflicting owners **to** the Operator **without** silently selecting a winner.
````

## 5. CA-R-2449

````markdown
## Summary

MCP owns provider-neutral discovery, schema, and dispatch for Tools, Prompts, and Workflows

## Claim scope

MCP.

## Claim

MCP **must** own the provider-neutral Model Context Protocol discovery, schema, **and** dispatch interface through which an agent:

- invokes active CAPRMEDIO Tools;
- receives ACTION_PROMPTS **or** OPERATOR_PROMPTS; **and**
- starts **or** resumes Workflows.

MCP **must not** own **any** of the following:

- Tool behavior;
- Prompt content;
- Workflow coordination;
- Skill procedures;
- application behavior; **or**
- agent-host-specific packaging.
````

## 6. CA-R-2450

````markdown
## Summary

The Project has exactly five ordered Layers

## Claim

The Project has **exactly** the following five ordered Layers:

1. FRAMEWORK_METHODOLOGY has Local Order `1`.
2. FRAMEWORK_ENGINE has Local Order `2`.
3. OPERATOR_DOCUMENTATION has Local Order `3`.
4. CORE_EXTENSIONS has Local Order `4`.
5. RELEASES has Local Order `5`.
````

## 7. CA-R-705

````markdown
## Summary

The CAPRMEDIO Framework includes all Project outputs delivered to root Implementation Folders; downstream Layers and direct Features have distinct Project roles

## Claim

The CAPRMEDIO Framework **must** comprise **all** outputs of the caprmedio Project delivered **to** the repository's root Implementation Folders. OPERATOR_DOCUMENTATION, CORE_EXTENSIONS, **and** RELEASES are downstream Project Layers; COMMUNITY_EXTENSIONS **and** FIELD are direct Project Features.
````

## 8. CA-R-2430

````markdown
## Summary

PROGRAMMATIC owns all and only deterministic behavior of FRAMEWORK_ENGINE

## Claim

PROGRAMMATIC owns all and only deterministic behavior of FRAMEWORK_ENGINE.
````

## 9. CA-R-2452

````markdown
## Summary

Create and evolve CAPRMEDIO so any Operator can create, deliver, run and maintain any feasible Project with AI Agents

## Claim

The caprmedio Project **must** create **and** evolve a working CAPRMEDIO Framework. Given enough resources, that Framework **must** let **any** Operator use AI Agents **to** do **all** of the following for **any** feasible Project:

- create the Project;
- deliver the Project;
- run the Project; **and**
- maintain the Project.
````

## 10. CA-M-005

````markdown
## Summary

Admit or retain only mechanisms needed to preserve required outcomes or material governed distinctions

## Claim

To govern the Project's mechanisms, admit **or** retain a mechanism **only** **when** the other admitted mechanisms cannot preserve a required outcome **or** a material governed distinction.
````

## 11. CA-M-006

````markdown
## Summary

Maintain coherence across Project governance and Implementation

## Claim

To govern the Project, keep the following mutually coherent **where** they share authority **or** interact:

- Terms;
- Claims;
- rules;
- structure; **and**
- Implementation.
````

## 12. CA-D-657

````markdown
## Summary

Minimal, governed YAML frontmatter for Markdown Atom Carriers

## Claim scope

YAML Frontmatter of Markdown Atom Carriers.

## Claim

The YAML Frontmatter of a Markdown Atom Carrier **must** use the least syntax **and** nesting that preserves **all** of the following:

- unambiguous deterministic parsing;
- validation;
- extensibility; **and**
- human readability.

## Details

### Common field encoding

Use the following field encodings for the applicable Atom Properties. Presence follows the applicable Property authority, **not** observed filename tokens. A String is a nonempty YAML string; an Integer excludes Booleans. a null value does **not** satisfy a required Property.

| Property | Top-level field | Encoding **and** applicable presence |
|---|---|---|
| Atom Identity | `atom_id` | String under the Atom ID Carrier definition; exactly one for every Current, Draft, **or** Archived Atom; Draft marker forms follow the Draft ID marker definition; carry Version separately |
| Content Role | `content_role` | **=1** String selecting its canonical Content Role; resolve the admitted domain from applicable authority |
| Type | `type` | **=1** String selecting the Atom's admitted Type under its applicable Type authority; a present field **must not** be null, empty, **or** a collection; filename Type tokens are **not** a second value |
| Local Scope Unit | `current_scope_unit` | **=1** String naming the registered Local Scope Unit that owns an ordinary Atom. For Type Project Goal only, carry its Operator Actor owner through the existing Author fallback under the resolved Target Scope Unit and Project Goal owner encoding; do not register that Actor as a Scope Unit or infer the value from filename |
| Target Scope Unit | `claim_target_scope_unit` | use the resolved Target Scope Unit and Project Goal owner encoding |
| Numeric Tier | `tier` | exactly one integer for every Current Atom under the base Atom Property cardinalities; ordinary Scope Unit-owned Atoms use **>=0** under the Project and non-Project Tier rules, and a verified Project Goal carries exactly `-1` under the Project Goal Tier rule |
| Tier Label | `tier_label` | **0..1** nonempty String for an explicitly carried `Atom.Tier.Label`; retain the integer `tier` field. Use the governed numeric-to-label mapping; omit the Label when not supplied, including for Tiers 5 and higher. This is distinct from the Atom's `label` property. |
| Version **and** Updated At | `version`, `updated_at` | use the Version and Updated At encoding |
| Author | `author` | use the Author encoding |
| Status | `status` | use the Status encoding |
| Label | `label` | **<=1** nonempty String for an explicit Label value; when absent, the effective Label is derived from the Atom Type name under the effective Label rule, without requiring a stored copy of that fallback |
| Summary | no frontmatter copy | exactly one body Property under the Markdown body section rules; its effective value is the nonempty Summary content |
| Claim | no frontmatter copy | exactly one direct prose body Claim for RMED under the Markdown body section rules; R may add one nested Formal claim under the Claim definition |
| Subjects | `subjects` | use the Subjects encoding; **only** the governed Subject keys **and** their admitted encodings |
| authored Atom Relations | `relations` | use the Atom Relations encoding; omission **or** an empty mapping represents no authored Relations; **every** present Relation Kind carries its nonempty target collection |

- `current_scope_unit` **must not** be null, a list, a joined set of names, **or** replaced by an `operators` field. It names the owning Local Scope Unit, except that Type Project Goal carries its Operator Actor owner under the resolved Target Scope Unit and Project Goal owner encoding. This exception does not apply to ordinary Goals. Never infer the value from its filename.
- The Atom ID and Version identify a Current or Archived Atom version under the Atom ID Carrier definition; do **not** duplicate them **in** an `identifier` field. Current, Draft, **and** Archived Atoms carry exactly one Atom ID; a Draft may remain incomplete in other required Properties until promotion. Draft marker forms follow the Draft ID marker definition.
- Every Current Atom satisfies the required and optional base Property cardinalities in the base Atom Property cardinalities. A Draft may be incomplete, but retains its mandatory Atom ID and reports missing required Properties; it must satisfy the full Current contract before promotion.
- Summary **and** Claim use their body sections under the Markdown body section rules, **not** `summary` **or** `claim` frontmatter copies. Other body Properties use their own registered section authority.

### Conditional fields and expansion

- A Plan's explicit `assignee` uses **<=1** String identifying an admitted Actor under the Plan Assignee encoding. `autonomous_confidence_threshold` **and** `implementation_retry_limit` use their integer encodings under the Plan confidence override and retry limit encodings. inherited values remain omitted unless explicitly selected; self-sufficiency does **not** copy them.
- `priority` follows the applicable Concern Priority authority for Concern Atoms **only**. additional Plan, Operations, proof, **or** other Type-specific fields require their applicable Delivery declarations; their occurrence **in** old Carriers does **not** admit them.
- The generated `projection` block is admitted **only** **in** a projected representation under the projection source-binding encoding, with **only** its defined `source_carrier_path` String. It is **not** an authored source Atom Property.
- A new field **or** nested key requires applicable authority that settles its canonical location, value type, cardinality, admission condition, **and** permitted values **or** reference resolution. unadmitted fields are invalid; an admitted Property with an unsettled encoding is a schema gap, **not** permission **to** guess **or** report full conformance.
- Apply explicitly governed migration exceptions **only** within their declared boundary. legacy presence alone is **not** an exception; retired fields under the canonical Property location rules remain rejected.

### Subjects-only edit-draft exception

The explicit source-pinned Subjects-only edit draft is a derived proposed next Revision of an existing Atom, not a new Atom Draft or another canonical original. It may carry `atom_id: <canonical-ID>@<proposed-version>-draft` (preferred) or the compatible `atom_id: <canonical-ID>@draft`, `status: Draft`, and a matching Draft-marker filename in the owning role's `draft/` folder while the exact canonical source remains untouched. The reviewed packet retains the canonical target/source pin and exact draft path/digest for that specific proposed edit. Approval restores the canonical ID and original Status, independently validates normalized Subjects-only materialization, and uses the existing exact predecessor archive plus N+1/actual-time update. Staging and publication require no retained Draft-history entry, `revision_lineage`, unique Draft head, origin chain or consuming successor. New-Atom Drafts and ordinary lifecycle Drafts carry exactly one Atom ID; marker and filename rules remain governed by the Draft ID marker and Draft filename marker rules. Canonical ID grammar and the normal source, schema, identity/collision, permission and exact actual-history safeguards are unchanged.
````
