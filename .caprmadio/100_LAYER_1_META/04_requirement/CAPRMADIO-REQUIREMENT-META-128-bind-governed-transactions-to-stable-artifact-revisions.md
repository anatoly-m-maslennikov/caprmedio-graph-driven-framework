---
artifact_type: requirement
artifact_id: CAPRMADIO-REQUIREMENT-META-128
scope_path: layer:meta
subject_scopes:
  - lifecycle-traceability
tier: core
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  replacement_of:
    - CAPRMADIO-REQUIREMENT-META-075-revision-bound-parent-child-transactions
  child_of:
    - CAPRMADIO-REQUIREMENT-META-122-require-falsifiable-claims-and-stop-conditions
    - CAPRMADIO-REQUIREMENT-META-163-semantic-irreducibility
---

# Bind governed transactions to stable artifact revisions

Every governed change is a directed provenance transaction from exact parent
artifact revisions to new or updated children. A parent revision is identified
by stable artifact identity plus a governed revision digest; a child is a
governed artifact or native project target produced or revised by the
transaction.

The transaction distinguishes children created for the first time from
existing children revised by the transaction. All children in one transaction
belong to exactly one `scope_path`; parents may come from multiple scopes when
one bounded child scope integrates their authority.

Parent revisions pre-exist the transaction. Creating or refining an Atom and
producing children that consume that revision therefore require separate,
ordered transactions. A same-ID Atom refinement creates a new addressable
revision while existing dependents remain bound to the earlier revision they
consumed.

Every parent-to-child edge is preserved in governed history independently of a
particular version-control graph shape. Repository commits remain provenance,
but squash, rebase, cherry-pick, or repository migration must not erase the
stable artifact-revision identities and semantic edges needed to replay the
transaction. GOV owns concrete revision, transaction, and carrier syntax.
