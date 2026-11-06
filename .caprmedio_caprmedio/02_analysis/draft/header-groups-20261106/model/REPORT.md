# Header grouping: model impact

This packet is review material, not native Drafts or Current authority. The manifest pins each source and proposed content, with an inventory of 256 native Core Meta-Model Requirement files containing an exact legacy `Header.<field>` reference. It includes Current candidates and Drafts and excludes archived carriers. This is a lexical inventory for follow-up semantic review, not proof of full model or repository coverage.

The proposed Header owner claim declares and orders the sibling groups Identity, Context, Relations, State, Destination. Existing role-specific Properties move under their applicable Context role group; other already-declared extras require their own disposition. Relations remains the existing optional container. When an optional group or child is absent, serialization filters it rather than creating a value to satisfy the model order.

Five new container Declaration Claims are prepared, with no IDs allocated:

- Identity: one container with exactly ID and Ref ID, in that order.
- Context: one container with Container, Role, Form, optional Label, Topics and Tier, in that order, plus an applicable role-specific group. The 5..7 direct-child bound covers the common mandatory fields and optional Label and role group; it does not constrain direct values.
- State: one container with Status, Version and Updated At, in that order.
- Context.Plan: optional for Plan-role Atoms; when present it contains one or both Work Sequence Number and AI Agent Confidence Threshold, preserving their existing optionality.
- Context.Concern: required for Concern-role Atoms, containing the existing required Concern Priority. No Plan Priority is introduced.

Destination replaces Carrier Destination. The existing CA-R-2715 and its File, Name and Path declarations must be reconciled at the new paths; their existing direct-value and nesting constraints are preserved in the previews. CA-R-2717 and CA-R-2718 currently state exactly one direct value without an explicit Format in their Formal Claims. Their previews make the previously accepted string Format explicit, without adding a separate occurrence bound.

The 24 pinned owner-declaration previews demonstrate path and scoped-selector changes while retaining unrelated Claim text. They preserve old identity metadata solely to make each change reviewable; they are not ready for promotion as written. Changed Summaries require review. A changed Summary or identity-bearing Subject requires the applicable identity/successor decision rather than silently reusing an ID for a different contribution. CA-R-2713 already has a Summary saying `Subjects` while its main Subject and Formal Claim say `Topics`; its preview corrects the Summary to `Atom.Header.Context.Topics`, which requires identity handling. CA-R-2719 is supplied as a Claim-body preview, not a replacement carrier. Its Current and existing Draft are independently recorded in the inventory.

Other model consumers require semantic review, not mechanical promotion: status and identity rules, Role/Form qualifications, inherited scopes, IS_CONTAINED_BY and Context.Container defaults, Subject/Topics rules, CFEL examples and instance selectors. The 256-item inventory includes source pins and line numbers to route those changes. It does not include Delivery encodings, runtime implementation, projections, external Workbench state, historical archives, or other Scope Units.

Acceptance requires: (1) each child has exactly its intended immediate bearer and existing effective occurrence/direct-value/Format constraints; (2) model sibling order and absent-optional serialization agree; (3) role-qualified selectors and instance conditions use the new paths consistently; (4) every changed Summary/identity and affected inbound reference has an explicit disposition; (5) no duplicate declaration or retired Carrier Destination reference remains in the selected promoted model; (6) native source history and external/runtime state are handled by their respective owners.
