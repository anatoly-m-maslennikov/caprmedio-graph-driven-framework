# Candidate #6 — resolved definition tiers

Status: review preparation, 2026-10-17. All 45 nonempty definition drafts accounted for: **10 Core / 9, 3 General / 10, 32 Standard / 11**. No tier question remains. This does not establish parent links, allocate IDs or admit source Atoms.

The previous table's three holds are resolved. Five earlier Core recommendations are corrected to Standard: Carrier.Canonical Address, Directory Carrier.Path, Atom Revision, Execution and Project.Operator Registry. An incidental “not identity”, “not the record” or “not permission” clause does not make the whole definition Core.

## Current authority and test

Read current CA-M-272 v14, CA-R-659 v21, CA-R-1431 v12, CA-R-660 v17 and CA-R-1573 v7. CA-R-1746 v22 already establishes Projection non-authority and source traceability. Their current clauses, rather than historic tier choices on similar Atoms, determine these proposals.

1. Core: identify the complete Claim's constitutive identity, authority or root separation premise. Do not elevate a narrower definition merely because it restates a premise established elsewhere.
2. General: a shared contract governs all Standard Atoms in the owning Scope Unit across roles, subject to its stated applicability; provide two materially different conforming realizations and a changed-contract witness preserving Core.
3. Standard: a bounded kind/property/parameter definition for which neither higher-tier test is established. Abstract wording and usefulness alone are insufficient for a higher tier.

The seven PROJECT_CONFIGURATION definitions stay there. The other 38 stay CORE_META_MODEL. Both Scope Units have structural level 3, giving Global Tiers 9/10/11. No Type-to-tier restriction is invented; Candidate #6 decision 26 defers new exact restrictions.

The existing parent-scope/admission issue remains separate. “Resolved” below means the complete-Claim tier recommendation is established, not that all current M272 admission prerequisites, parent edges or source conflicts are already repaired.

## Three former holds

The governance domain for each is **all Standard Atoms owned by CORE_META_MODEL, across all Content Roles** under R1573—not a selected set of matching Subjects or only RMED. Optional properties and unused capabilities do not become mandatory through that universal domain.

The witnesses below are logical realizations for M272's classification test. They are not adopted storage formats, new implementation tasks or changes to the approved Claims.

| Claim | Core test | Two conforming realizations | Changed shared contract preserving Core | Result |
| --- | --- | --- | --- | --- |
| Atom.Semantics | Explains meanings/applicability in an optional property distinct from Details. The Terms view's non-authority applies R1746's existing source/view boundary; it does not create a second Core premise. | **A:** authored Markdown Semantics content holds meanings and applicability, separate from Details; a derived Terms view gathers those source uses. **B:** structured meaning/applicability entries belong to each source Atom while Details remains separate; a derived Terms view aggregates those entries and other source usage. In both, the section/property need not exist on every Atom and the compiled view remains non-authoritative. | A shared content schema could combine meaning explanation with Details while retaining the same source authority, Atom identity and non-authoritative Terms view. That would change conformance to the current separate-Semantics contract, not the Core authority boundary. This alternative is a witness, not a proposal. | General / 10 |
| Atom.Enabled Relations.Contains | The complete Claim supplies a default-False kind capability and optional role/type enablement. It does not define Atom identity, ownership or the CONTAINS relation itself (R1368). | **A:** kind-level Boolean declarations say which Content Roles/Types enable containment, with omission resolving False. **B:** kind-level permission rules enumerate enabled roles/types; kinds without an enabling rule resolve False. Both admit False/True, have no required per-instance Boolean, and permit but do not require children when True. | Changing the shared default to True would alter conformance for kinds without an explicit grant while leaving typed Atoms, their identities and the CONTAINS relation intact. The accepted default remains False. | General / 10 |
| Atom.Status base domain | Defines a common allowed-value domain and additive inheritance, not Atom identity or the meanings/transitions of those statuses. R1412 separately requires one Status. | **A:** a single shared base-domain declaration plus narrower-kind additions validates Status in Atom-file frontmatter. **B:** a shared base-domain table plus kind-specific addition tables validates stored Atom records. Both inherit Draft/Active/Archived without repeated per-kind declarations and allow additions only through the applicable role/type rules. | Adding one further common allowed value would change the shared domain and therefore conformance while retaining Atom identity, one-Status structure, additive inheritance and source authority. No such value is adopted here. | General / 10 |

Each contract is independently revisable: optional semantic-content structure, kind containment permission policy, or common Status domain. None duplicates a concrete Concern, Plan, Workflow or implementation. The witnesses cover the complete Claim; they do not obtain General from reuse alone.

## All 45 recommendations

Draft filename prefix: `CA-R--CORE_META_MODEL--define-`; suffix: `.md`. C = CORE_META_MODEL; P = PROJECT_CONFIGURATION. “Reviewed v” identifies the review document before the tier-only metadata update, not a source Atom Version or new-Atom initial Version. Every draft was Standard/11 at the start of this tier pass.

| Draft key | Owner | Reviewed v | Final Local / Global Tier | Complete-Claim rationale |
| --- | --- | --- | --- | --- |
| actor-name | C | 2 | Standard / 11 | Optional named field, not Actor identity or authority. Candidate #5 optional Name; CA-R-1422 and CA-R-1552 define/govern narrower Actors, not this shared field. |
| atom-enabled-relations-contains | C | 2 | General / 10 | Reusable capability/default contract for Atom kinds across all roles, not one kind's enabling rule. It preserves the existing Atom/CONTAINS foundations. Two realizations and a changed-contract witness are recorded in tier-resolution.md. |
| atom-semantics | C | 3 | General / 10 | Shared optional meaning-content contract across all Atom roles. Projection non-authority is already established by CA-R-1746; this Clause applies that foundation rather than creating another. Full-contract witnesses are recorded in tier-resolution.md. |
| atom-status-allowed-values | C | 2 | General / 10 | Shared base domain and inheritance contract across all Atom roles, not a definition of identity or authority. Full-contract witnesses are recorded in tier-resolution.md; source Status alignment remains separate. |
| carrier-canonical-address-segment | C | 2 | Standard / 11 | Bounded component of a particular addressing model; changing segmentation need not change Carrier identity. CA-D-301, CA-D-352. |
| carrier-canonical-address | C | 2 | Standard / 11 | Defines a designated locator field; the final clause applies the separate Carrier-ID boundary. Changing address conventions does not change that foundation. CA-D-267, CA-D-301. |
| carrier-format | C | 2 | Standard / 11 | Defines one encoding/interpretation field; does not establish the Carrier/represented-thing boundary. CA-D-262, CA-D-507. |
| carrier-id | C | 2 | Core / 9 | Constitutive identity boundary independent of filename/path. Operator decision; CA-D-507. |
| directory-carrier-name | C | 2 | Standard / 11 | Bounded directory naming field, not a framework identity or authority premise. CA-D-297, CA-D-299, CA-D-445. |
| directory-carrier-numeric-prefix | C | 2 | Standard / 11 | Conditional naming-convention component; absent in valid alternative names. CA-D-300, CA-D-445. |
| directory-carrier-path | C | 2 | Standard / 11 | Defines one filesystem locator, consistently with File Carrier.Path and Canonical Address. Clauses excluding identity and Scope Unit parentage apply existing boundaries; they do not create a new Core foundation. CA-D-445, CA-R-1660. |
| entity-carrier-database-carrier | C | 2 | Standard / 11 | Concrete specialization by storage medium; changing supported media preserves the Carrier foundation. Candidate #5; CA-R-1745 permits database Journal representation. |
| entity-carrier-directory-carrier | C | 2 | Standard / 11 | Bounded specialization and qualification of directories as Carriers; not a new universal root boundary. CA-D-259, CA-D-451, CA-D-464. |
| entity-carrier-file-carrier | C | 2 | Standard / 11 | Concrete specialization by storage medium. CA-D-258, CA-D-283, CA-D-356. |
| entity-carrier | C | 2 | Core / 9 | Constitutive separation of representation from represented Continuant and actual Occurrent. Negation collapses independent roots. Candidate #6; CA-D-256, CA-D-414. |
| entity-continuant-actor-type-ai-agent | C | 2 | Standard / 11 | Defines a particular Actor kind; other Actors and the who/what boundary remain coherent without it. CA-R-852, CA-R-1552; accepted Actor branch. |
| entity-continuant-history-revision-type-atom | C | 2 | Standard / 11 | Specializes historical state as an archived Atom, applying the History/current-state distinction. It does not introduce that general boundary or a universal identity scheme. Candidate #6; CA-R-1371 requires separate alignment. |
| entity-continuant-history | C | 2 | Core / 9 | Constitutive distinction between historical state/records and actual events/executions. Candidate #6; CA-R-1051, CA-R-1371, CA-R-1745. |
| entity-continuant-object-governing-configuration | C | 2 | Core / 9 | Establishes non-Atom source authority versus derived Projection. Negation removes the declared authority boundary for structural facts/configuration. CA-R-1402, CA-R-1738, CA-R-1483. |
| entity-continuant-object-relation | C | 2 | Core / 9 | Establishes typed meaning/direction between identified endpoints; an untyped connection would violate the accepted graph premise. CA-R-806, CA-R-1246, CA-R-1437, CA-R-1472. |
| entity-continuant-object | C | 2 | Core / 9 | Constitutive what/who separation from Actor. Candidate #6; CA-R-1248 and CA-R-1191 define broader Entity/Primary Entity, not this distinction. |
| entity-continuant-projection-type-direct-relation-registry | C | 2 | Standard / 11 | Particular Projection kind with traceable relation metadata; generic Projection authority remains intact if this kind changes or is absent. CA-M-120, CA-R-806, CA-R-1246, CA-R-1437. |
| entity-continuant-selection | C | 2 | Core / 9 | Constitutive separation of selection criteria from selected Objects and copied instances. Candidate #6; CA-R-1447/CA-R-1448 supply concrete selection cases. |
| entity-continuant | C | 2 | Core / 9 | Constitutive persistent-thing versus actual-occurrence boundary of the accepted root model. Candidate #6; existing CA-R-1248 does not define this branch. |
| entity-occurrent-event | C | 2 | Standard / 11 | Defines a narrower occurrence kind under the Occurrent boundary; restates record distinction for this kind without adding a second universal foundation. Candidate #6; CA-R-1745. |
| entity-occurrent-execution-action-run | C | 2 | Standard / 11 | Bounded one-Action execution kind, not the general definition/run/record boundary. CA-R-1452, CA-R-853; existing CA-R-1510/CA-R-1511 cover other Runs. |
| entity-occurrent-execution | C | 2 | Standard / 11 | Defines work-performance occurrences under Occurrent. Its definition/record exclusions apply that existing root distinction, consistently with Event, Session and Action Run. Candidate #6; CA-R-1510/CA-R-1511 define narrower Runs. |
| entity-occurrent-session | C | 2 | Standard / 11 | Particular interaction occurrence; source/log distinction follows the general Occurrent premise. CA-R-1650 defines a stored envelope, not this actual Session. |
| entity-occurrent | C | 2 | Core / 9 | Constitutive actual-occurrence versus stored-record boundary. Candidate #6; CA-R-1510, CA-R-1511, CA-R-1745. |
| execution-execution-id | C | 2 | Standard / 11 | Names the identifying field without a new identity format, uniqueness domain or conservation rule. Operator Execution-ID decision. |
| file-carrier-extension | C | 2 | Standard / 11 | Bounded filename-format indicator; generic Carrier identity already remains distinct. CA-D-283, CA-D-284, CA-D-507. |
| file-carrier-filename | C | 2 | Standard / 11 | Bounded file naming field, not a new authority/identity foundation. CA-D-283, CA-D-284. |
| file-carrier-path | C | 2 | Standard / 11 | File-specific locator field applying the general Carrier locator/identity separation. CA-D-445; Operator Carrier-ID decision. |
| project-framework-settings-artifact-timestamp-timezone | P | 2 | Standard / 11 | Particular framework parameter; a different timestamp convention preserves Project authority. CA-D-390. |
| project-framework-settings-code-root-locators | P | 2 | Standard / 11 | Particular references used by this framework, not all Projects' model premise. CA-D-371; Core/project separation decision. |
| project-framework-settings-confidence | P | 2 | Standard / 11 | Particular defaults group, not a new universal authority or identity boundary. CA-R-1652, CA-R-380. |
| project-framework-settings-framework-control-root-locator | P | 2 | Standard / 11 | Concrete framework-control reference; Project authority is already established separately. CA-D-370, CA-D-317. |
| project-framework-settings-identifier | P | 2 | Standard / 11 | Identifying field for this framework's concrete configuration, not a newly declared generic identity system. CA-R-1402, CA-R-1404, CA-D-358. |
| project-framework-settings-interaction | P | 2 | Standard / 11 | Particular presentation settings group; not all Standard Atoms' shared conformance contract. CA-R-1628, CA-R-1439, CA-R-1440. |
| project-framework-settings-parameter-resolution | P | 2 | Standard / 11 | Defines this framework parameter-selection concept without new precedence rules, receipts or gates. CA-M-279, CA-R-1402, CA-R-1441. |
| project-operator-registry | C | 2 | Standard / 11 | Defines the Project's Operator-registration property. Registration not granting permission preserves the existing Actor authority distinction; it does not create the generic permission model. CA-D-494; accepted Actor/Project distinction. |
| project-settings-identifier | C | 2 | Standard / 11 | Identifying field of the already-authoritative Project Settings configuration; CA-R-1738/CA-R-1401 establish configuration authority. CA-D-362 supplies representation evidence. |
| relation-source-reference | C | 2 | Standard / 11 | Names one endpoint slot under the already-defined directed Relation; no new endpoint admission rule. CA-R-1017, CA-R-118, CA-D-268. |
| relation-target-reference | C | 2 | Standard / 11 | Names the opposite endpoint slot under the Relation foundation; no new endpoint restriction. CA-R-1017, CA-R-1472, CA-D-268. |
| scope-unit-id | C | 2 | Core / 9 | Establishes the Scope Unit identity key as distinct from Name, Label and Path. This is an identity premise, not a location-field definition; it adds no unclaimed persistence, allocation or rename procedure. Operator identity decision; CA-R-962/CA-R-970 only define naming. |

## Consistency and preservation

- Locator fields stay Standard consistently: Canonical Address, its Segment, File Path and Directory Path. They apply Carrier identity and Scope Unit hierarchy distinctions rather than independently establishing them.
- Carrier.ID and Scope Unit.ID stay Core because their complete purpose is to establish the identity key independently of representation/name/path. No permanence, allocation algorithm or rename procedure is inferred from those definitions. Execution ID and configuration Identifiers merely name a field of an already identified entity; they add no comparable identity-separation premise.
- Event, Execution, Session and Action Run stay Standard as narrower occurrence definitions. The actual-occurrence versus record boundary belongs to the Occurrent/History foundations. Atom Revision similarly specializes History; its archived-Atom representation does not make it another Core root.
- The Operator Registry stays Standard: its membership/permission exclusion preserves the existing Actor authority boundary. Governing Configuration stays Core because its whole Claim establishes a non-Atom authoritative source class, distinguished from a derived Projection.
- Source IDs in the table are evidence, not proposed parent relations. None of the definitions has been allocated an ID or promoted.
- Only the 13 review drafts moving from Standard to Core/General require metadata edits. Their review Versions increment once with the actual update timestamp; Claims, Summary, Subjects, ownership and all other fields remain unchanged. The 32 Standard drafts remain byte-for-byte unchanged.
- Current Status, containment, Revision and Carrier contradictions still need the already prepared source-alignment work. Classification does not imply those conflicts disappeared.

No new Operator question is needed for these tier choices. Remaining admission work is outside this classification: permitted parent links, fresh identities, executable requests, and the separately owned source-alignment packet.

