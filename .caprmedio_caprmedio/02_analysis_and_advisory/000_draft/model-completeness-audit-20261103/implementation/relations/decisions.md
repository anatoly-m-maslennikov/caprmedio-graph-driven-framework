# Prospective Relation fixes

Seven full carrier previews are `.txt` files under `previews/`; source and candidate SHA-256 pins are in `source-candidate-map.json`. No Active Markdown Atom, canonical source, Journal, lifecycle record, ID allocation or Git mutation is created here.

R2278 keeps its exact Summary and changes the declaring-owner qualification from retired Entity Definition/Relation Definition forms to Requirement/Form Declaration. It counts effective ownership after inheritance and local replacements. R2279 becomes a fresh-ID-needed `CA-R-draft` / version 1 preview with Summary “Declare IS_DECLARED_BY”. It selects the qualified Declaration-source GOVERNS fact, reverses only that selected fact and retains its qualification. GOVERNS itself stays unchanged; its general endpoint semantics already supports this subset. The only selected Current textual references to IS_DEFINED_BY were R2278 and R2279, and both previews now use IS_DECLARED_BY. Historical references are outside this replacement.

R2618 drops its Declaration-specific Node-only target constraint. Its generic signature covers declared model entities and instances, with prose excluding literal values and glyphs. It retains canonical sourcing from the active Subject field; no ownership cardinality is invented by this signature.

R2588 preserves independent left outgoing and right incoming count slots and omitted counts as unspecified. Reverse writing swaps endpoints and their slots. The wildcard default remains outgoing only, and a direct permission still does not grant an inverse permission. Existing three formal expressions gain missing semicolon separators so the first two terminate as complete expressions; their bounds and endpoint populations are unchanged. Legal short classification aliases remain legal.

R2486 now applies the minimal reverse-HAS_INVERSE carrier rule only to inverse views. A qualified or other non-inverse derived view retains its source, endpoint transformation and qualification in its own Declaration or cited governing rule. It does not force the general source Relation to adopt a subset qualification. The equivalent R2487 correction is recorded as a recommended fragment for its entity-lane owner; this lane does not edit that source.

`verify_packet.py` passes the seven exact pins, unchanged stable Summaries, formal-first named Claim children, fresh-ID marker, qualified GOVERNS derivation, non-Node endpoint admission, independent count slots and inverse-only policy. Root must allocate the fresh ID and integrate the old-source lifecycle and R2487 fragment before adoption. Runtime/evaluator and graph acceptance are not established by this preview check.

## Carrier endpoint-permission relocation

R1020 and R1021 retain their exact Summaries and receive the existing R1958 endpoint permissions. implementation_of remains direct from the governed Implementation Carrier to the specification Atom it implements. evidence_for remains direct from the evidence Carrier to the Evaluation or Implementation Carrier it supports. Both signatures use explicit Carrier// and Atom// variable binders plus the exact prose restrictions; no new kind or formal grouping is inferred. Both retain the existing prohibition on treating these endpoint permissions as Relation-Type fields or additional inverse storage facts.

The combined manifest pins R1958 and quotes its exact original paragraph. Header's owner has been asked to remove only that paragraph from its R1958 candidate after these destination previews passed preservation checks. This is relocation of the existing restriction, not a new global policy or a claim that Current already contains the relocation.
