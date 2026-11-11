# CFEL specification review

Status: source repairs applied; open findings remain.

## Applied and verified

- `?==` assigns missing defaults. `=` tests conditions; `==` assigns values.
- Project Settings AI Agent Confidence Threshold defaults to integer 90 in 0..100. The optional Plan override declares that range too.
- LOOKUP, AND and OR have their own Declarations. Numeric range and format intersection have focused Rules on existing Format.
- Mixed AND/OR requires parentheses.
- Standalone typed bindings last through the CFEL block. IF bindings last through the condition and THEN group. New bindings use different names from bound outer variables.
- Bare unambiguous text is allowed. Double quotes protect syntax characters; only escaped quote and escaped backslash are admitted escapes.
- SPECIALIZES is Direct; IS_SPECIALIZED_BY is Derived. Their descriptors are Current; endpoint permissions and old-link migration remain separate.
- Structural-level comparisons remain tests of stored values.

## Evidence

- The original 142-source specification census has a per-Atom disposition in audit-index.json. Thirteen lexical exclusions were reassessed: twelve CFEL-owned sources returned to scope; one Workflow-owned source remains excluded.
- Actual operator/default packet: thirteen reviewed promotions, two exact predecessor retirements and the Current analysis dependency remap.
- Actual grouping/binding/range packet: three reviewed promotions.
- Specialization: two reviewed descriptor promotions.
- Seven MODEL views match 1,167 pinned selected Current suppliers. Their bounds remain explicit: 55 known missing and 23 unresolved coverage entries.
- Created specification proposal: CA-A-1318@1-draft.

## Open findings

- Legacy Subject paths and retired Entity-root exceptions.
- Relation-scoped rules that govern endpoint Nodes or unrelated business policies.
- Exact meanings and missing declarations for remaining legacy Relation names.
- 343 legacy child_of links: eight sampled, 335 unreviewed; no bulk rename.
- Remaining parser, runtime, data and integration evidence owned by the corresponding agents.

Workbench and Workflow files were excluded from source edits. No source receipt claims native Workflow admission or Journal append.

## Latest focused source repairs

- Five Relation cleanups preserve endpoint restrictions; the edge-identity rule now belongs to Relation.
- Entity remains a general Term, defined by M451@7.
- Relation and Term retain separate branches and explicitly allow Properties in R2247@11 and R1318@37.
- R1318 drops an unrelated Node Property selector from Passive Subjects. Its Claim remains unchanged.
- Final seven views use 1,167 pinned suppliers; coverage remains 55 missing and 23 unresolved. Property schema-instance permissions remain a separate audit finding.
