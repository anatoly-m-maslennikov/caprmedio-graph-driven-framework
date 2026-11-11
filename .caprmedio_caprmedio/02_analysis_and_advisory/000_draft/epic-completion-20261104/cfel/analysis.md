# Declaration CFEL coverage review

## Scope and evidence

Recomputed the Declaration-only contract graph from the 1,151 selected Current source paths in `property-instances-20261104/post-application-frontier.json`. All 1,151 on-disk source hashes match the frontier. The exact 113 diagnostics, expressions, source identities, versions, paths, hashes and assigned pattern groups are in `inventory.json`. This is a Declaration-only projection reader audit, not a general CFEL validity or runtime evaluation audit. The formal fenced Claims are retained verbatim in the contract graph even when structured extraction is unsupported.

The initial direct full-frontier reader call included 211 Declaration sources. Reproducing the actual generator pipeline selects 977 carriers with active/governs Subjects and 210 Declaration sources; CA-R-2256 is excluded by that display scope. The scoped reader exactly matches the published manifest: 210 candidates, 209 bound, 143 entity targets, 113 unsupported clauses, one coverage gap and one narrowing diagnostic. The 113-clause inventory is unchanged.

## Pattern inventory

| Pattern | Count | Reader implication |
|---|---:|---|
| Standalone model Subject | 33 | All 33 are already accepted by the existing approved subject-notation parser. They can be retained as source-bound declarative expressions; they do not independently authorize invented model nodes or relations. |
| Qualified Property selector | 13 | Existing Property constraint, wildcard name-count and literal patterns are blocked by a `/(.Header.Role: Value)` qualifier. Reuse the approved AST and preserve the condition; never apply it unconditionally to the unqualified Property. |
| Qualified instance binder | 2 | Preserve kind selector, qualifier and variable separately; avoid creating an instance or treating the kind selector as a project-wide cardinality. |
| Operator spelling Declaration | 23 | Registered operator/glyph expressions, not Relation aliases; preserve exact quoted syntax, including escapes, and source. Do not create Relation kinds or assume all declared operators are semantically evaluated. |
| Symbolic grammar examples | 4 | CA-R-2487 writes placeholder names in count slots as notation examples. Treat as source examples, not executable cardinalities; do not coerce placeholders to numbers. |
| Conditional expressions | 19 | Includes IF/THEN, one IF/THEN/ELSE and embedded tests. Preserve complete opaque structured expression and group; splitting antecedent from consequent or adding unconditional edges loses meaning. |
| Functions and aggregate expressions | 10 | UNIQUE, DETERMINES, COUNT/DISTINCT and MAX. Preserve complete expression with its lexical inputs and source; do not claim evaluation. |
| Comparisons and assignments | 7 | Numeric guards and instance assertions; avoid interpreting tests as constraints or derived facts without their operator semantics. |
| Fallback expressions | 2 | `?=`/LOOKUP chains. Preserve precedence and explicit scoped sources; do not materialize fallback values or turn them into required authored occurrences. |

Counts are a partition of the observed diagnostics, not a claim that every expression is validated CFEL. No clause was established as malformed solely because this bounded extractor rejected it. Possible source-level semantic issues, such as CA-R-2499's `(.ID)` relative selector versus other Header-qualified references, require a targeted authority review before calling them defects. Expressions for controls, aggregates and grammar placeholders should stay diagnostic or explicitly opaque until the relevant profile is specified; merely relabeling every diagnostic as understood is not completeness.

## Independent gaps and candidate fixes

1. **Event Record parent is explicitly declared, but the reader misses it (high confidence).** CA-R-2557@4 declares `Event Record ((NARROWER_THAN)) Continuant`; the graph reader currently filters Claim targets unless they begin with `@`, and emits `Event Record: no explicit NARROWER_THAN parent; rendered as a root.` Admit the already-declared, uniquely resolved bare named target using the same ambiguity and declaration-provenance checks as reference targets. Do not invent the parent if it is absent, ambiguous or outside the selected frontier. Test the real source shape, missing and ambiguous targets, and duplicate-proof parent rendering. The Current declaration, not this report, supplies the edge.

2. **CAPRMEDIO_MODEL Declaration coverage (high confidence in reader gap; model binding needs care).** CA-R-2559@2 has active Subject `CAPRMEDIO_MODEL` and describes MODEL and its inheritance. The contract graph rejects this namespace-root Declaration as outside its target categories. Preserve the namespace Declaration and its Claim as an explicit source-bound namespace entry. Do not create a primary Node from the namespace or equate the namespace with the distinct `MODEL` Subject without authority. Test exact namespace only, rejected unrecognized namespaces, original Claim/prose and no extra Node.

3. **Read valid existing paths and bounded qualified Property syntax (high confidence).** Reuse `subject_notation.parse_subject_expression` for standalone model expressions. For the 13 selected scoped Property expressions, parse and retain approved qualification AST with occurrence/value bounds and literal channel intact. Test Role: Concern/Plan/Operations, malformed qualifiers and unsupported control syntax; confirm Condition remains attached, no global/unqualified constraint and no synthetic nodes. Qualified instance binders need a separate exact grammar and tests for variable scoping. These are reader changes only, not promotion of selected source clauses into universal authority.

4. **Bounded operator declarations (high confidence if needed by requested view).** Extract only the observed exact `Operator//Name == "..."` form with proper escaped-string handling and exact literal evidence, not new relation metadata. Test semicolon inside a quoted token, escaped inner quotes and malformed/unclosed strings. The raw source block already preserves these statements; structured extraction is useful only if the intended projection needs operator lookup.

5. **Controls, aggregates, fallback and placeholder forms (do not guess semantics).** Existing views already retain the complete fenced block; document explicit raw-versus-structured coverage and source binding. If consumers require structured access, introduce an expressly opaque tagged expression record that preserves group/source/text and a bounded diagnostic for unsupported semantics; do not call it evaluation or imply clause validation. Tests should ensure IF/THEN/ELSE, nested parentheses, quoted semicolons and incomplete/unbalanced input are not split, evaluated or silently accepted. More detailed AST/evaluation is a separate design decision, not necessary to make the raw projection source-faithful.

## Boundaries

No Current source, Git state, projection or shared code was changed for this investigation. Suggested fixes need implementation, focused tests, full selected-frontier checks, and actual projection regeneration before any completion claim. Graph source coverage and CFEL structured coverage are distinct; runtime semantics, graph policy decisions, and the other Subject audit remain out of scope.
