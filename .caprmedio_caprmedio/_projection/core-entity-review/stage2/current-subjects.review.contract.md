# Current Subject review output — CA-P-1966

This contract covers candidate mapping evidence only. It does not adopt grammar, change sources, accept a graph or authorize migration. Read current-subjects.contract.md first.

## Input and ownership

One review Task owns its exact input batch and output file. Recheck the batch SHA, inventory SHA, frozen candidate and consolidated review pins, and every current source SHA before reading meaning. All occurrences of one source stay with its owner. Do not edit another batch or the captured review.

Use `reviews/current-subjects.batch-NNN.review.json`. JSON is a derived report, not an Atom or a new source of truth.

## Output

The output object contains:

- `schema_version: 1`, `non_authoritative: true`, `source_migration: "not_performed"`, `native_admission: "not_performed"`.
- `task_id`, exact input `batch_id`, `input_batch_path`, `input_batch_sha256`, `input_inventory_sha256`.
- `evidence_pins`: the frozen candidate, consolidated review, this contract and any captured evidence actually used; each has relative `path` and full-file `sha256`. A captured carrier also names its Git commit. An unchanged ID does not substitute for byte equality.
- `source_reviews`: one row per input source, including a source with no valid Subject occurrence. Copy `relative_path`, `full_file_sha256`, `atom_id`, `version`, `quarantined` and the exact input `findings` array; record `main_content_read`, `finding_dispositions` and concrete `questions`. Each disposition has `finding` and `reason`; its finding keys cover the exact input findings once each, with no extra or duplicate keys. A disposition explains a finding; it does not repair it.
- `occurrences`: exactly one row per input occurrence. Copy its full input row without alteration, then add the review fields below. Do not deduplicate by Subject text.

Each occurrence review adds:

- `decision`: `unchanged`, `proposed` or `unresolved`.
- `proposed_value`: the exact old value for unchanged; a nonempty candidate string for proposed; null for unresolved.
- `confidence`: a number from 0 to 1. Below 0.90, decision is unresolved and proposed_value is null.
- `reason`: the current content meaning and how it supports the decision.
- `evidence`: at least one current-content span for every occurrence, including unresolved rows. That span's `path` and full-file `sha256` must equal the owning input source's `relative_path` and `full_file_sha256`. Each span has one-based inclusive `start_line`/`end_line`, SHA-256 of those exact bytes including their original line endings, and `reason`. An unresolved span explains what the current content leaves unclear. Candidate/captured spans are additional evidence and do not replace current meaning.
- `candidate_basis`: for every proposed value, exact JSON pointers into the pinned candidate and a reason showing how those confirmed rules and the current content support each changed distinction. A referenced rule must actually support the mapping; merely citing a root list is not enough. Other rows may use an empty list. This does not require an exact display string already present in the candidate, but an unsupported new identity remains unresolved.
- `preserved_distinctions`: role, owner, allowed-value domain, qualification or other distinctions retained by the mapping.
- `question`: a concrete unresolved Operator choice, or null. Missing evidence is research work, not automatically an Operator question.
- `executable: false`: no review row is an approved mutation.

Quarantined sources remain in coverage. Do not disguise their metadata findings as repaired. Meaning can be reviewed separately, but no row from them becomes executable.

## Meaning boundary

Use the latest confirmed candidate: Artifact, Scope Unit, Actor, Relation, Revision, Carrier and Execution; dependent Entities stay with their bearer. Terms remain a separate graph. M/E are views over shared roots, not new roots. Revision is history, not Artifact.Revision or Artifact/Revision.

Candidate notation uses / for broader-to-narrower, . for bearer qualification and : for allowed values. @ is display/carrier notation, not an admitted Subject operator. A candidate string is not proof of native relation admission or supported Subject grammar.

Read each Atom's current Main Content. Do not globally replace every slash with a dot, rename storage keys or scopes, collapse qualified allowed-value domains, remove duplicate-looking Entities, or turn a D storage convention into a per-Property Carrier registry. Do not add an Artifact prefix merely for display consistency. If canonical identity or meaning is not supported, leave the proposed value null.

Substance is the umbrella; RMED Claim and O Operation retain their role meanings. Keep ownership Scope Unit distinct from Substance Scope. Do not rewrite those bodies during this review.

## Integration check

The integration Task checks all prerequisites, exact source/occurrence coverage, all input/source/evidence pins and exact span hashes. It checks decision/value/confidence consistency, preserves every quarantine finding and exposes unresolved rows. Deliberately changed or missing data must fail its check. No producer self-check substitutes for this acceptance.

A review Task may finish with explicit unresolved candidates, but unresolved research remains tracked work. Integration and CA-P-1966 cannot finish while required mapping research or concrete decisions remain unaccounted for. Work over 15 minutes gains bounded child Tasks before continuation. Root alone owns integration, Plan lifecycle and Git.
