# Scope Unit Declaration adoption preparation

## Verified starting point

- One governing Project Structure TOML contains **44 non-root Scope Unit rows**: 10 Ordered and 34 Unordered. The root Project is implicit in Project Settings, so the observed inventory is **45 units**, including that root. The Operator then confirmed Applicable Methodology is a special Projection: retire its separate hosting Scope Unit at adoption. The retained Declaration set is **44 units** (43 non-root plus Project).
- The Operator removed Navigation Number from Scope Units. Keep Local Order; retire the legacy `navigational_order_number` field and its Scope Unit rules during the actual migration. Navigation Number remains only for Steps and P Atoms.
- Five explicit authority-mode overrides and nine Local Order values remain in the retained Declaration set. The withdrawn APPLICABLE_METHODOLOGY row accounts for the other override and Local Order value. Preserve delivered Projection content and its Carrier places; retiring a Scope Unit does not delete those artifacts.
- The TOML does not carry authoritative Scope Unit IDs or the external Goal/Constraint and local Contract Atom bindings. Generated projection node IDs are not an ID registry.
- The reviewed predicate uses Role Requirement, Form Scope Unit Declaration and the active Subject of the specific Scope Unit. No Atom.Status predicate is added.

## Ordered work

1. Finalize methodology and Carrier declarations. Keep the Operator expression verbatim; reuse the shared Role/Form/active-Subject model and its proposed Carrier keys. [Three successor Drafts](source-amendments.md) amend R1484, D442 and D297; they do not finish the disposition of other TOML-only sources such as D440/D441. Do not make accepted methodology depend on an old Engine validator accepting it.
2. Review the [completed source field map](field-mapping.md) against the 44 TOML rows plus the root Project, recording the separate APPLICABLE_METHODOLOGY row as planned retirement. Local Order is retained; Scope Unit Navigation Number is omitted. Parentage, authority/delivery places and explicit authority modes are preserved without invented defaults. No authoritative ID registry was found in these source files; no IDs are inferred from a Projection.
3. Review the [44 retained Declaration Drafts](instance-drafts.md), each bound by its active Subject. Their recorded facts pass source/hash checks. Existing separate Goals and local Tier-0 Contracts are inventoried in [Goal coverage](goal-coverage.md): 18 retained units have explicit Goal targets and 26 have none observed; six Goal targets remain unmapped. Do not invent missing Goal content. Local Tier-0 Contracts remain optional. The Project Declaration is externally Operator-owned; settle final discovery without silently making central staging its adopted place.
4. Review the complete source replacement and Carrier normalization. Assign unique canonical IDs to new Drafts at promotion, retain history and preserve reference bindings. Existing CA-R-draft placeholders are not canonical IDs.
5. Adopt the reviewed sources through an explicit publication step. Once the Declarations cover all governed facts, they become authority; any retained TOML is derived compatibility output. Do not independently maintain both.
6. Hand reader/writer, parser and compatibility-generation implementation to the Engine work. Coordinate actual writer cutover before using old tools against new source formats. Rebuild projections only from the adopted authoritative sources.

## Boundary

The original 45-unit instance inventory is checked; 44 Declaration Drafts remain after withdrawing the separate APPLICABLE_METHODOLOGY Scope Unit. That withdrawal is recorded, not silently omitted. Adoption remains incomplete: no promotion, configuration deletion, code change, runtime release or projection rebuild has been performed by this packet. [Instance verification](instance-draft-verification.json), [source coverage](toml-coverage.json) and [corrected binding review](corrected-binding-review.json) record the evidence and remaining checks.
