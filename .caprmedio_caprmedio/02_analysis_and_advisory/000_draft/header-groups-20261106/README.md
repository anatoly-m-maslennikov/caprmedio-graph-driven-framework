# Header groups — 2026-11-06

Status: reviewed checkpoint `8ffaff048` requires rebasing to the newer `identity.id` decision and filename/CFEL work. Live Header layout remains unchanged. The checkpoint is not eligible for live application under the newer contract.

Epic P2694@81 records the approved task, completed preparation and remaining technical cutover gate. Its Header layout remains flat.

## Approved structure

- Header.Identity: ID, Ref ID.
- Header.Context: Container, Role, Form, Label, Topics, Tier.
- Header.Context.Concern: Priority.
- Header.Context.Plan: Work Sequence Number, AI Agent Confidence Threshold.
- Header.Context.Role.Form: declared Form-specific groups, when needed.
- Header.Relations: optional direct Relation facts.
- Header.State: Status, Version, Updated At.
- Header.Destination: File.Name, File.Path.

Frontmatter directly contains `identity`, `context`, optional `relations`, `state`, and `destination`; it has no `header` wrapper. Unordered Role-specific fields use the existing R2967 default. No extra order is introduced.

The threshold's canonical serialized key is `context.plan.ai_agent_confidence_threshold`. The 284 old `autonomous_confidence_threshold` values are integers in 0..100 and are preserved at that canonical location.

## Scope and preservation

The refreshed root snapshot contains 4,677 native sources: the previously verified 4,669 sources plus eight Workbench review Drafts. Seven concurrent source edits are pinned at their reviewed live bytes. Five new group Declarations yield 4,682 live outputs. Twenty-three renamed Current declarations require fresh IDs under the Summary identity rule. With the five new groups, 28 new Requirement identities are required. The retained Work Sequence Draft keeps Version 3 under the replacement declaration identity.

Current semantic replacements retain exact predecessor snapshots. Other Current/Draft grouping and reference changes preserve business values, Versions and Updated At. Existing unadmitted legacy fields remain untouched; four old Done/Canceled Plans keep their undeclared root Priority values. Existing missing groups or values are not synthesized. These exceptions prevent data loss and do not admit new Properties.

All present timestamp strings are explicitly quoted. Twelve old YAML timestamp scalars retain their exact lexical timestamp in quoted form; inverse parsing verifies the same original temporal value. This is the existing D270 representation rule, not a new time value.

Historical archives, Journals, projections, runtime code and Workflow business definitions are outside the source application. Source-level checks do not establish full schema conformance, runtime readiness or a completed Epic.

## Lanes

| Deliverable | Owner | Exclusive files | Dependencies | Acceptance | State |
|---|---|---|---|---|---|
| Model claims and owner previews | model_property_contracts | model/ | Operator decisions | Property counts, exact names, identity disposition | Reviewed |
| Native data transform | model_subject_syntax | data/ | Root snapshot | Metadata/body round-trip on 4,671 sources | Verified |
| CFEL, Subject and prose references | header_reference_migration | references/ | Root snapshot | Path-aware, idempotent; no unresolved holds | Verified |
| Delivery revisions | model_legacy_cleanup | delivery/ | Canonical encoding | Seven Current and four own-Draft rebases | Reviewed |
| Model review | header_model_review | review/ | Model and Delivery packets | No introduced model contradiction | Cleared |
| Guarded composition/application | root, header_integration | integration/ | All source packets and runtime readiness | Exact preimages, ID lock, rollback, readback | Rehearsal passed; not applied |
| Shared adapters and implementation checks | CA #3: WFs | Implementation-owned files | Adapter handoff | Nested readers/writers; frozen archives preserved | Complete; chat subsequently stopped by human |
| Workbench reader/index readiness | CA #8: Workbench | Workbench-owned files | Shared adapter and its schema work | Actual nested-source and query evidence | Not ready |

The Operator previously authorized coordination and implementation handoff. Both implementation owners received the concrete [adapter handoff](adapter-handoff.md). Their readiness is an external dependency; this source lane runs no production tests.

## Refreshed preflight

All 4,677 pinned sources pass metadata/body round-trip checks with no parse errors, pin mismatches or held transforms. The reference plan has 496 affected sources, 1,792 spans and no holds. The no-write rehearsal produces 4,682 outputs, 4,737 file operations, 28 fresh Requirement identities and 31 exact predecessor archives; it allocates no real IDs.

The Role/Form specialization review is clear. The prepared readback now derives counts from the source snapshot and model manifest, preserves four omitted timestamps, and checks the exact lexical form of twelve legacy timestamps.

Workbench's shared-reader alias conflict was fixed by its owner after direct Operator approval. Its narrow code verdict is ready for the previous Header contract; the installed old runtime remains a cutover blocker. The newer `identity.id` decision also requires rebasing this packet and checking its readers. See the [current formula decisions](../atom-identity-destination-formulas-20261106/README.md). Live Header cutover and actual postimage readback remain pending. The obsolete extra simulation was interrupted without a plan or readback result.
