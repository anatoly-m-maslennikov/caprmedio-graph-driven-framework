# Cross-kind relation lookup acceptance

Derived implementation evidence, 2026-10-13. Not source authority or whole-Project admission.

P2334 fixes a preexisting lookup failure: one Atom referenced by two different Relation Kinds was flattened into duplicate lookup IDs and rejected before graph validation. D268 scopes target uniqueness to each relation-kind collection; separate kinds can reference the same target.

The production change is one line in proposed_carrier.py: deduplicate the internal lookup request while preserving first-seen order. Authored metadata and relation lists stay unchanged. Complete carrier validation occurs first, and graph validation still processes the original Relations. No new public API, policy, source pin or publication path is introduced.

Author whitelist_impl reproduced the old failure in default and scoped validation, then passed three new regressions plus 18 reference-scope tests. Independent reviewer whitelist_tests reproduced the same failure and passed three independent controls after the fix: cross-kind reuse succeeds without metadata or filesystem changes; duplicates within a kind still refuse; missing and duplicate actual target carriers still refuse.

Production proposed_carrier.py SHA-256: `ed8bff7ec160550c83cf5e504bd31db936b53eb87b196091e4ade9d669e1ebf9`.
Author test_proposed_cross_kind_lookup.py SHA-256: `87289cffcbe11ae7dfcd77ccb730547dbd0bbcc0e14c3c7d5ec28782a9451ed9`.
Independent test_cross_kind_reference_independent.py SHA-256: `6ce9dd3730fd1e202e2ac43cee4859e5faf50c7cf35885e32681edf1cdc4223b`.

The independent acceptance is separate from P2333's unordered-target change. It does not resolve unsupported Relation Kinds, TOML packet admission, broader legacy migration or live publication.
