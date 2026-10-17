# Candidate #6 — definition metadata readiness

Status: preparation only. Tier review updated 2026-10-17. No source Atom, identity or parent relation was changed. Review-draft tier metadata is updated separately under the Operator-authorized preparation task.

Scope: the 45 nonempty Claims in `../empty-r-drafts/`. The 9 empty covered/superseded placeholders are excluded. This packet proposes metadata; it is **not an executable admission packet**.

## Basis and common blockers

- CA-M-272 v14 classifies the complete Claim, not its Subject label. CA-R-659 defines Core foundations; CA-R-1431 defines General; CA-R-660 makes Standard the default only after the higher-tier tests. CA-R-1234 separates the CORE_META_MODEL source layer from Core Local Tier.
- Both intended owners have structural level 3 in current `project_structure.toml`: Core = Global Tier 9, General = 10, Standard = 11. The original Standard/11 placeholders have been reviewed; the final proposals are 10 Core, 3 General and 32 Standard.
- The seven concrete Framework Settings definitions belong to PROJECT_CONFIGURATION. The other 38 belong to CORE_META_MODEL. Historical filenames do not override intended ownership.
- Core recommendations below identify a constitutive identity or separation boundary. Standard recommendations identify a bounded specialization or named field, not a contract governing all higher-tier Atoms. Repeating an existing boundary does not raise a definition to Core. The three General recommendations and their complete-contract witnesses are recorded in [tier resolution](tier-resolution.md).
- **All 45 parent candidates are now mapped** in [parent resolution](parent-resolution.md): 36 to CA-R-1174, two to CA-R-1746 and seven to CA-R-1176. Existing rules permit applicable same-owner and topology-permitted ancestor parents. R796's conflicting equality condition still needs the proposed narrow source correction. R920 does not explicitly define a composite Scope.
- The parent map is a proposal, not an admission result. A same-owner Core/9 Atom cannot parent another Core/9 Atom through a lower-tier edge, and sibling source-layer authority is not structural parentage. The evidence IDs in the table below are classification evidence; use the separate parent map for proposed `child_of` links.
- New-definition Drafts intentionally have no Atom IDs (CA-D-288). Admission needs fresh IDs and canonical source carriers under CA-D-446; an existing-source `@draft` edit is not the applicable case. No IDs are reserved here.
- Status, containment, Revision and Carrier source contradictions remain in their dedicated alignment packets. A tier recommendation does not resolve those conflicts.

## Per-definition recommendations

Filename key: `CA-R--CORE_META_MODEL--define-<key>.md` in `../empty-r-drafts/`. C = CORE_META_MODEL; P = PROJECT_CONFIGURATION. Every row has a parent proposal in parent-resolution.md; native admission remains unverified.

| Draft key | Owner | Proposed Local / Global Tier | Complete-Claim basis and evidence |
| --- | --- | --- | --- |
| actor-name | C | Standard / 11 | Optional named field, not Actor identity or authority. Candidate #5 optional Name; CA-R-1422 and CA-R-1552 define/govern narrower Actors, not this shared field. |
| atom-enabled-relations-contains | C | General / 10 | Reusable capability/default contract for Atom kinds across all roles, not one kind's enabling rule. It preserves the existing Atom/CONTAINS foundations. Two realizations and a changed-contract witness are recorded in tier-resolution.md. |
| atom-semantics | C | General / 10 | Shared optional meaning-content contract across all Atom roles. Projection non-authority is already established by CA-R-1746; this Clause applies that foundation rather than creating another. Full-contract witnesses are recorded in tier-resolution.md. |
| atom-status-allowed-values | C | General / 10 | Shared base domain and inheritance contract across all Atom roles, not a definition of identity or authority. Full-contract witnesses are recorded in tier-resolution.md; source Status alignment remains separate. |
| carrier-canonical-address-segment | C | Standard / 11 | Bounded component of a particular addressing model; changing segmentation need not change Carrier identity. CA-D-301, CA-D-352. |
| carrier-canonical-address | C | Standard / 11 | Defines a designated locator field; the final clause applies the separate Carrier-ID boundary. Changing address conventions does not change that foundation. CA-D-267, CA-D-301. |
| carrier-format | C | Standard / 11 | Defines one encoding/interpretation field; does not establish the Carrier/represented-thing boundary. CA-D-262, CA-D-507. |
| carrier-id | C | Core / 9 | Constitutive identity boundary independent of filename/path. Operator decision; CA-D-507. |
| directory-carrier-name | C | Standard / 11 | Bounded directory naming field, not a framework identity or authority premise. CA-D-297, CA-D-299, CA-D-445. |
| directory-carrier-numeric-prefix | C | Standard / 11 | Conditional naming-convention component; absent in valid alternative names. CA-D-300, CA-D-445. |
| directory-carrier-path | C | Standard / 11 | Defines one filesystem locator, consistently with File Carrier.Path and Canonical Address. Clauses excluding identity and Scope Unit parentage apply existing boundaries; they do not create a new Core foundation. CA-D-445, CA-R-1660. |
| entity-carrier-database-carrier | C | Standard / 11 | Concrete specialization by storage medium; changing supported media preserves the Carrier foundation. Candidate #5; CA-R-1745 permits database Journal representation. |
| entity-carrier-directory-carrier | C | Standard / 11 | Bounded specialization and qualification of directories as Carriers; not a new universal root boundary. CA-D-259, CA-D-451, CA-D-464. |
| entity-carrier-file-carrier | C | Standard / 11 | Concrete specialization by storage medium. CA-D-258, CA-D-283, CA-D-356. |
| entity-carrier | C | Core / 9 | Constitutive separation of representation from represented Continuant and actual Occurrent. Negation collapses independent roots. Candidate #6; CA-D-256, CA-D-414. |
| entity-continuant-actor-type-ai-agent | C | Standard / 11 | Defines a particular Actor kind; other Actors and the who/what boundary remain coherent without it. CA-R-852, CA-R-1552; accepted Actor branch. |
| entity-continuant-history-revision-type-atom | C | Standard / 11 | Specializes historical state as an archived Atom, applying the History/current-state distinction. It does not introduce that general boundary or a universal identity scheme. Candidate #6; CA-R-1371 requires separate alignment. |
| entity-continuant-history | C | Core / 9 | Constitutive distinction between historical state/records and actual events/executions. Candidate #6; CA-R-1051, CA-R-1371, CA-R-1745. |
| entity-continuant-object-governing-configuration | C | Core / 9 | Establishes non-Atom source authority versus derived Projection. Negation removes the declared authority boundary for structural facts/configuration. CA-R-1402, CA-R-1738, CA-R-1483. |
| entity-continuant-object-relation | C | Core / 9 | Establishes typed meaning/direction between identified endpoints; an untyped connection would violate the accepted graph premise. CA-R-806, CA-R-1246, CA-R-1437, CA-R-1472. |
| entity-continuant-object | C | Core / 9 | Constitutive what/who separation from Actor. Candidate #6; CA-R-1248 and CA-R-1191 define broader Entity/Primary Entity, not this distinction. |
| entity-continuant-projection-type-direct-relation-registry | C | Standard / 11 | Particular Projection kind with traceable relation metadata; generic Projection authority remains intact if this kind changes or is absent. CA-M-120, CA-R-806, CA-R-1246, CA-R-1437. |
| entity-continuant-selection | C | Core / 9 | Constitutive separation of selection criteria from selected Objects and copied instances. Candidate #6; CA-R-1447/CA-R-1448 supply concrete selection cases. |
| entity-continuant | C | Core / 9 | Constitutive persistent-thing versus actual-occurrence boundary of the accepted root model. Candidate #6; existing CA-R-1248 does not define this branch. |
| entity-occurrent-event | C | Standard / 11 | Defines a narrower occurrence kind under the Occurrent boundary; restates record distinction for this kind without adding a second universal foundation. Candidate #6; CA-R-1745. |
| entity-occurrent-execution-action-run | C | Standard / 11 | Bounded one-Action execution kind, not the general definition/run/record boundary. CA-R-1452, CA-R-853; existing CA-R-1510/CA-R-1511 cover other Runs. |
| entity-occurrent-execution | C | Standard / 11 | Defines work-performance occurrences under Occurrent. Its definition/record exclusions apply that existing root distinction, consistently with Event, Session and Action Run. Candidate #6; CA-R-1510/CA-R-1511 define narrower Runs. |
| entity-occurrent-session | C | Standard / 11 | Particular interaction occurrence; source/log distinction follows the general Occurrent premise. CA-R-1650 defines a stored envelope, not this actual Session. |
| entity-occurrent | C | Core / 9 | Constitutive actual-occurrence versus stored-record boundary. Candidate #6; CA-R-1510, CA-R-1511, CA-R-1745. |
| execution-execution-id | C | Standard / 11 | Names the identifying field without a new identity format, uniqueness domain or conservation rule. Operator Execution-ID decision. |
| file-carrier-extension | C | Standard / 11 | Bounded filename-format indicator; generic Carrier identity already remains distinct. CA-D-283, CA-D-284, CA-D-507. |
| file-carrier-filename | C | Standard / 11 | Bounded file naming field, not a new authority/identity foundation. CA-D-283, CA-D-284. |
| file-carrier-path | C | Standard / 11 | File-specific locator field applying the general Carrier locator/identity separation. CA-D-445; Operator Carrier-ID decision. |
| project-framework-settings-artifact-timestamp-timezone | P | Standard / 11 | Particular framework parameter; a different timestamp convention preserves Project authority. CA-D-390. |
| project-framework-settings-code-root-locators | P | Standard / 11 | Particular references used by this framework, not all Projects' model premise. CA-D-371; Core/project separation decision. |
| project-framework-settings-confidence | P | Standard / 11 | Particular defaults group, not a new universal authority or identity boundary. CA-R-1652, CA-R-380. |
| project-framework-settings-framework-control-root-locator | P | Standard / 11 | Concrete framework-control reference; Project authority is already established separately. CA-D-370, CA-D-317. |
| project-framework-settings-identifier | P | Standard / 11 | Identifying field for this framework's concrete configuration, not a newly declared generic identity system. CA-R-1402, CA-R-1404, CA-D-358. |
| project-framework-settings-interaction | P | Standard / 11 | Particular presentation settings group; not all Standard Atoms' shared conformance contract. CA-R-1628, CA-R-1439, CA-R-1440. |
| project-framework-settings-parameter-resolution | P | Standard / 11 | Defines this framework parameter-selection concept without new precedence rules, receipts or gates. CA-M-279, CA-R-1402, CA-R-1441. |
| project-operator-registry | C | Standard / 11 | Defines the Project's Operator-registration property. Registration not granting permission preserves the existing Actor authority distinction; it does not create the generic permission model. CA-D-494; accepted Actor/Project distinction. |
| project-settings-identifier | C | Standard / 11 | Identifying field of the already-authoritative Project Settings configuration; CA-R-1738/CA-R-1401 establish configuration authority. CA-D-362 supplies representation evidence. |
| relation-source-reference | C | Standard / 11 | Names one endpoint slot under the already-defined directed Relation; no new endpoint admission rule. CA-R-1017, CA-R-118, CA-D-268. |
| relation-target-reference | C | Standard / 11 | Names the opposite endpoint slot under the Relation foundation; no new endpoint restriction. CA-R-1017, CA-R-1472, CA-D-268. |
| scope-unit-id | C | Core / 9 | Establishes the Scope Unit identity key as distinct from Name, Label and Path. This is an identity premise, not a location-field definition; it adds no unclaimed persistence, allocation or rename procedure. Operator identity decision; CA-R-962/CA-R-970 only define naming. |

## Bounded next step

The three tier holds are resolved in tier-resolution.md. Parent candidates and the narrow R796 correction are recorded in parent-resolution.md. Unused identity candidates are recorded in identity-proposal.json, without reserving them. The remaining source and tool blockers are recorded in preflight.md; do not omit required relations or use direct writes to bypass them.

This packet does not check full topology, alter current rules, or authorize creation, promotion, migration or runtime changes.

