# Candidate #7 — applied methodology increment

Date: 2026-10-22.
Status: this source increment is applied and checked; the full migration remains incomplete.

This is an authored change summary, not a generated graph, Workflow receipt, Journal event or new source of methodology authority. The defining Atoms remain the source of truth. The Operator authorized direct file edits for this methodology-only continuation; no MCP write operation is claimed.

## Applied

- Updated the Subject-root definitions and optional Subjects contract: at most one GOVERNS and any number of DEPENDS_ON links.
- Authored Current-Atom base property rules, incomplete Draft admission, Label fallback and Project Goal Local Tier rules.
- Aligned archive and Draft identity policies. New predecessor archives carry ID@Version and Archived Status, with old numeric Version, Updated At and unrelated content preserved. Old historical carriers were not bulk-normalized.
- Created seven Type definitions: R2110–R2116 cover Requirement/Definition, Method and Delivery Policy/Engineering Decision, and Evaluation Policy/Eval Case. An Eval Case is specification, not an executable test or prompt.
- Reclassified 34 current Evaluation policy Atoms: 33 in the Type lane and E449 in the Subject lane. Other QA Case classifications remain to be migrated.
- Retired R2005, R1201, R1393, D288 and R793 after their bounded operative consumers were addressed. Their prior Versions remain archived.
- Applied the reviewed Engine Subjects-only batch: 104 current M/E/D Atoms, 171 exact GOVERNS/DEPENDS_ON replacements. Bodies, Types, statuses, scopes and unrelated metadata were preserved in that batch.
- Recorded the increment and remaining work in CA-P-1959@131; the Epic remains Active.

The source lanes changed 184 distinct Atom identities; the Epic update makes 185 in this increment. The source records contain 170 update operations, 12 creations and 5 retirements before the Epic update. Three Type-rule identities have two successive update operations, so operation counts are not unique-Atom counts. Newly created source Atoms are R2100–R2103, R2110–R2116 and D650.

## Checked

Independent read-only checks passed for the final source hashes, YAML frontmatter, canonical Current IDs, predecessor ID@Version and Archived Status, Version chains, retained Summaries, preserved archive timestamps and bodies, and the actual relation rebindings. Engine checks covered all 208 Current/archive carriers in its 104-Atom batch. Type checks covered its repeated-version chains and mechanism-neutral Evaluation policy classifications.

The final integrated check covered all 188 recorded operations, 180 final Current carriers and 176 predecessor archives, including the Epic update. Final source/archive hashes, YAML, group IDs and scoped `git diff --check` passed.

Checks did not add implementation tests or run the runtime test suite. No code, implementation schemas, tool implementation, Settings values, MCP runtime, frozen fixtures, commit or release was changed by this increment. No Journal append is claimed; the files below are scratch change records only.

## Actual records

All are under `.caprmedio_tmp/candidate7-migration-20261022/`:

- `subject-source-changes.json`
- `property-source-changes.json`
- `identity-source-changes.json`
- `type-source-changes.json`
- `engine-subject-source-changes.json`
- `root-source-changes.json`
- `plan-source-changes.json`

Each identifies the applicable source paths, Versions, archives and hashes. The PROGRAMMATIC chat consumed the Engine manifest and separately refreshed its existing 39-Method bundle and compact policy-reference views. That separate bounded refresh is not a new full Subject graph or runtime admission.

## Still to apply

1. Finish exact Subject mappings outside the bounded Engine batch and edited source-rule set. Generic identity, old topic/property names and remaining Revision references need their actual source meaning, not guessed aliases. Mapping templates are not full occurrence coverage.
2. Finish Type classifications and required property/ID data migration for the remaining source Atoms and Drafts. The earlier 866 missing-Type count is a pre-increment bounded inventory, not a current post-migration total.
3. Review Engineering Decision continuity in R1668, R1670–R1672, R1767–R1768 and D404. Do not carry an old Type-to-tier restriction into the new model automatically; exact new restrictions remain deferred.
4. Align remaining filename Type/Label tokens, including D400 and existing QA_CASE/EVALUATION_APPROACH names. No bulk rename or historical carrier normalization was performed here.
5. Review remaining legacy relation references, including D568's pre-existing untyped relates_to links and A1196's historical reference. Do not invent dependencies merely to replace an untyped link.
6. Rebuild the full affected Subject graphs from the final source frontier. The older saved Core/Project Configuration graphs remain stale for that purpose.

No remaining source-specific classification is treated as a new Operator question until existing source evidence and the already settled decisions have been exhausted. UX/Design and other explicitly deferred design topics remain deferred.
