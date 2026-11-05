# Property order and references

Latest Operator decisions:

- `x ;> y`: x immediately before y. `x <; y`: x immediately after y.
- Canonical `IS_ORDERED_RIGHT_AFTER` uses `<;`. `IS_ORDERED_RIGHT_BEFORE` is its inverse alias and uses `;>`.
- Explicit sibling order belongs in the applicable Declaration. A separate Rule with Subject `Node.**` puts nonparticipants last; their mutual order is unspecified. Participation includes either endpoint.
- Header order: ID, Ref ID, Container, Role, Form, Label, Topics, Tier, Relations, Status, Version, Updated At, Carrier Destination. Other Header fields follow, with no required mutual order.
- Content: Summary, Claim, Semantics, Details. Claim: Prose Claim then Formal Claim. Where declared, Workflow Mermaid Scheme comes first.
- Ref ID: base Atom ID for Current; ID@Version for Archived; ID@Version-draft for Draft.
- Relations is optional. Present canonical Relation keys have nonempty YAML sequences of base Atom IDs. Scalar/null values and empty target sequences are invalid.
- A present Property has a value or populated child structure. Empty optional Properties are omitted.

| Lane | Owner | Scope | Acceptance | State |
| --- | --- | --- | --- | --- |
| Relation and syntax | model_relation_contracts; root applies | Relation/prerequisite previews and selected Core sources | Explicit aliases, endpoints, inverse permission, Current source readback | Done |
| Layout and references | model_property_contracts; root applies | Header/Content declarations and Delivery | Exact chosen order; separate default Rule; no Workflow schema promotion | Done |
| Data | root | Native Current/Draft Header metadata | Ref ID derived from explicit inputs; remove only empty optional Properties | Applied; independent check running |
| Ordering | model_subject_syntax; root applies | Native Current/Draft Header and declared Content sections | Same YAML values and section bytes; unknown Header fields last | Prepared |
| Independent review | property_instance_relations_review | Read-only source, data and ordering checks | Exact plans/receipts and preserved predecessors | Running |

The model application has 61 checked operations, 33 outputs and 20 exact predecessor snapshots. New Current IDs: R2965 (ordering Relation), R2966 (Ref ID), R2967 (default ordering Rule).

The successful Ref ID application adds 4,448 values; 25 were already correct. 206 records remain held: 177 lack explicit ID or Status, and 29 have unallocated or invalid identity. No missing input was invented. The first Ref ID attempt failed before any writes because a concurrent edit changed M397; its plan is preserved separately.

The empty-property pass removes 1,594 empty Relations mappings and 254 empty dependency lists across 1,841 files. It preserves all other Header data and body bytes.

Ordering and final data verification are pending in this checkpoint. Existing invalid legacy Relation targets remain separate findings. Parser/runtime implementation and its tests belong to CA #3. No native workflow admission or Journal append is claimed.
