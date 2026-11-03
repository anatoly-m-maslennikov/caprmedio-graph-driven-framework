# Alias and counterpart packet review

## Source boundary

`source-map.json` pins exact Current source bytes and candidate bytes. Candidates retain physical flat YAML fields: Header is the model Property group, and this packet does not infer a physical YAML wrapper migration. Candidate model Subject roots use `CAPRMEDIO_MODEL`; role/form selectors qualify `Header`. No Current, projection, runtime, Git index or release state is modified by this packet.

## Proposed contract

- Every graph Relation keeps a distinct identity and one Declaration, including every derived counterpart.
- Direct Declarations own shared meaning, endpoint constraints and `Relation//DIRECT ((HAS_INVERSE)) Relation//DERIVED` binding. Derived declarations infer reversed endpoints, meaning, Derived classification and `IS_DERIVED_RELATION_OF`; their Claim contains the reverse written counterpart binding and their own alias, when one exists.
- `alias(Relation//CONTAINS) == "<+"` is lexical notation metadata. `alias(Relation//HAS_INVERSE) == "<-->"` makes the new counterpart spelling precise without inventing an equality of Subject identities or a literal-to-Node Relation.
- Canonical containment remains IS_CONTAINED_BY. CONTAINS remains its distinct derived inverse. Reverse written views and aliases grant no permission or cardinality.
- Names and tokens resolve exactly; undeclared aliases, case-folded names, ambiguous bindings, self-pairs and conflicting sources are rejected. Endpoint signatures exclude literals; narrowing specifically connects MODEL kinds. Other new layer restrictions are not adopted here.
- All operative existing direct endpoint populations and conditions are retained. This packet does not treat generic variables as Node-only selectors. Additional prose headings inside Prose Claim remain Markdown text, not newly declared child Properties.

## Minimal derived Claims

Every inverse Declaration now has a Formal Claim containing `Relation//DERIVED <((HAS_INVERSE)) Relation//DIRECT`, plus its own alias when one exists. This is reverse writing of the same binding owned by the direct Declaration; normalize it once, do not create another binding fact. No Claim exception is required. All ordinary Claims retain 1..2 unique named children. Existing canonical `NARROWER_THAN` is retained; tentative alternative spelling is not adopted.

Relation objects at the endpoints are typed references `Relation//NAME`. The middle `((HAS_INVERSE))` invokes the graph Relation; endpoint references do not invoke their named Relations as operators.

## Qualified derivation retained

R2279 IS_DEFINED_BY retains its full existing qualified meaning and GOVERNS/R2278 ownership condition. It is a non-inverse derived view and falls outside the minimal inverse-counterpart policy. Its Formal Claim uses Relation//IS_DEFINED_BY and Relation//GOVERNS as Relation-object endpoints, and named HAS_CLASSIFICATION / IS_DERIVED_RELATION_OF operators. No unconditional inverse is invented. Disposition: qualified-retained.

## Additional declaration

The new lexical `alias()` CFEL operator has a complete `NEW--declare-cfel-operator-alias.md` candidate with `atom_id: CA-R-draft`, version 1. R2486 specifies its exact grammar and checks; numeric ID allocation remains with the integration owner. No operator descriptor is equated with its literal token or with a graph Relation.

## Validation boundary

The source hash and structural checks in `verify_packet.py` check this bounded packet only. Existing parser/evaluator, VALIDATE_ATOMS, ENTITY_GRAPH and semantic-profile changes are a later consumer migration. No passing packet check demonstrates those consumers accept the new syntax.

## Reference-operator retirement

CA-R-2595 (Operator//DeclaredReference), version 1, is pinned for retirement on adoption. Bare qualified addresses reference their declared objects; `((NAME))` uses the Relation as an operator. New candidate grammar removes the `@` reference operator. Identity/version `@N` tags and historical bytes remain unchanged.

## Final syntax and source-pin audit

The original 30 source pins are rebased only through the namespace1178 receipt exact before-to-after hashes; original source pins remain recorded. Formal Relation-object endpoints use Relation//NAME, and actual Relation use uses ((NAME)). Direct/Derived metadata uses named HAS_CLASSIFICATION. NARROWER_THAN explicitly preserves “A Property does not narrow.” The verifier checks these forms and each Claim child contract.

## Complete Relation Declaration coverage

`coverage.json` selects all 41 Current canonical Active Requirement / Declaration carriers whose active Subject ends in Relation//NAME. Every selected Declaration has a full candidate; no unchanged disposition is used. The original 30 candidate sources remain, with 16 additional directly pinned post-namespace Current sources (46 source-backed candidates total), plus the new Alias operator draft. Added candidates preserve their original prose, applicability and endpoint constraints, moving Claim Scope text into Prose Claim applicability. Only Relation-object metadata syntax, alias notation, Claim layout and Header-qualified paths change. All 41 candidates pass the same syntax/Claim audit.

Canonical alias operands are qualified Relation objects, for example `alias(Relation//CONTAINS) == "<+"`. Predicate operators retain `((NAME))`. Historical readers may accept legacy alias(NAME) syntax without making it canonical in this packet.
