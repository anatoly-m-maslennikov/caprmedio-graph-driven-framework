# Event-based Updated At pattern — 2026-11-01

Status: design candidate, not an admitted Event Record schema or CFEL extension.

The Operator proposed deriving both Atom and Projection Updated At from MAX of timestamps in Event Records filtered by object and update action. This is a reusable invariant; it does not prescribe Workflow steps.

Terra prepared generic filtered-instance selection plus MAX. Luna confirmed that the selected Event Record model currently declares only ID and Journal containment. No target-object, action or timestamp contract exists yet. The two live timestamp Declarations are unchanged.

## Resolved update qualification

The Operator confirmed that update records mean accepted completed updates, including completed Projection rebuilds. No-ops, failed attempts and archiving are excluded. An extra outcome filter is unnecessary under this meaning.

## Resolved creation policy

The Operator chose MAX over accepted create and update events. Creation supplies the initial timestamp; no additional update record is required solely for creation.

## Resolved promotion and change data

Promotion counts as update and advances the promoted Atom’s timestamp. Its one Event Record contains old/new values only for changed logical Properties, such as Version and Status. Carrier filenames and directory changes are excluded; Carrier-only changes create no business update record. Complete object copies are unnecessary.

A new Core RRule records this requirement and passed independent review. This restricts the change payload, not normal record metadata. The abstract instance/state question is retired; exact reference encoding remains a schema dependency.

## Derived timestamp capture

Updated At may be recorded in the change delta when changed. Its new value remains derived from accepted create/update event timestamps. The copy is audit evidence, not another input or business update. This follows the latest allowance after the earlier DRY omission suggestion. The amendment passed review.

## Subsequent checks

- Creation participates in the timestamp selection alongside accepted updates.
- Target references must identify the correct Atom version or Projection instance. Bare Atom.ID is insufficient. A Draft’s mutable Version also means a raw composite key cannot silently be treated as a permanently stable target reference.
- Real instance relations belong under Relations. Do not treat the pseudocode’s object filter as an already approved carrier field or canonical Relation name.
- Timestamp must have the intended event-time meaning. Complete current-Project Journal coverage must be available.
- Typed MAX must compare timestamp instants, not strings; empty, invalid and unknown inputs need explicit behavior.

Evidence: [query candidate](declaration-expansion/event-timestamps-query-candidate.json), [schema inventory](declaration-expansion/event-timestamps-schema-inventory.json), [root adjudication](declaration-expansion/event-timestamps-root-review-20261101.json).

All114 registered Draft hashes match. Thirteen Node descendant Declaration Claims retain prose. Parser, schema, actual Event Records and runtime remain unchanged.

## Reviewed generic language Draft

One Rule Draft defines filtered instance selection and MAX. Final review passed after explicit narrower-kind and outer-variable binding clarifications. The packet now has114 Drafts;13 Node descendant prose Claims remain. No timestamp consumer or Event Record schema was changed. [Review](declaration-expansion/event-timestamps-query-language-final-review-20261101.json).

Latest packet:115 Drafts. The business-delta Rule adds no Event Record schema field or timestamp consumer;13 prose Claims remain. [Review](declaration-expansion/business-update-delta-review-20261101.json).

## Two event times

The Operator named separate happened_at and inserted_at fields. Both now have required childless datetime Declarations and a shared Core meaning Rule. Updated At uses happened_at. The historical captured new Updated At is evaluated through its event happened_at, not future events or insertion time. Both time-field and audit-scope reviews passed. Author is the event performer; object input/output interpretation is the current question. There are118 Drafts and13 remaining prose Claims.

## Atom metadata descriptor decision

Each present Atom input/output captures ID, Version and Updated At before/after. IDs may differ. Content and descendants are excluded for now; accepted Content-only updates still have records. A metadata-capture Core Rule and the revised delta Rule passed review. Timestamp targeting uses output identity. Projection has no Version declaration, so its descriptor is the current question. Packet119 Drafts;13 prose Claims remain.
