---
atom_id: CA-A-1234
content_role: Analysis
type: Specification Proposal
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
status: Active
author: Anatoly Maslennikov
subjects:
  governs: Subject
version: 2
updated_at: 2026-10-28 03:27:24 +0400
relations: {}
tier: 3
---
# Summary

Subject model Candidate #11

## Question

What is the next Subject model after separating containment/grouping from specialization?

## Status and authority

Candidate #11 is a Specification Proposal, not an adopted source migration or a rebuilt Projection. It refines Candidate #10 rather than replacing its accepted meanings. A1233 records the Operator's explicit decision: Project Model CONTAINS Actor; display this as Project Model > Actor, not a narrower-kind slash link.

The remaining edges below are source-backed proposals for consistent application of that distinction. They are not a claim that every edge was separately approved. Current RMED remains unchanged; the four Draft successors linked by A1233 are still Drafts.

## Relations and notation

- `>` means CONTAINS: organizational membership or an actual whole/part relation in its declared context. It supplies no property inheritance.
- `/` means broader-to-narrower classification in this proposed outline. Inheritance requires an actual source-backed specialization, not display ancestry.
- `.` retains bearer/dependent-property meaning.
- `:` retains allowed-value/qualified-kind meaning, not an instance assignment.
- `//` retains named-instance meaning; instances are not expanded in this candidate.

Keep IS_CONTAINED_BY as the authored direct direction and CONTAINS as its derived inverse. This candidate changes no relation direction or endpoint permission by notation alone. A type may permit containment without requiring every instance to have a contained part; cardinality remains a separate rule.

## Proposed primary outline

Labels are compact. Defining references are bare R IDs only; no Claim text is copied. `<Project Name>` is a namespace pattern, not an instance. The outline shows selected organizational and specialization links, not every relation in the graph.

```text
Subject [CA-R-1275]
	> CAPRMEDIO [CA-R-2206]
		> Graph [CA-R-2208]
			> Node [CA-R-1994]
				> Project Model [CA-R-2209]
					> Actor [CA-R-2218]
						/ AI Agent [CA-R-1959]
						/ Operator [CA-R-1422]
					> Atom [CA-R-655]
						/ Content Role: Analysis [CA-R-1337]
						/ Content Role: Concern [CA-R-1336]
						/ Content Role: Delivery [CA-R-1342]
						/ Content Role: Evaluation [CA-R-1341]
						/ Content Role: Method [CA-R-1340]
						/ Content Role: Operations [CA-R-1530]
						/ Content Role: Plan [CA-R-1338]
						/ Content Role: Requirement [CA-R-1339]
					> Continuant [CA-R-1967]
					> Governing Configuration [CA-R-1962]
					> History [CA-R-1961]
						> Journal [CA-R-1745]
						> Release [CA-R-2171]
					> Implementation [CA-R-2173]
						> Code [CA-R-2174]
							> Class [CA-R-2176]
							> Function [CA-R-2175]
							> Module [CA-R-2177]
							> Package [CA-R-2178]
							> Tool [CA-R-2197]
						> Documentation [CA-R-2180]
						> Prompts [CA-R-2179]
						> Resources [CA-R-2189]
					> Occurrent [CA-R-1972]
						/ Event [CA-R-1968]
						/ Execution [CA-R-1970]
							/ Action Run [CA-R-1969]
							/ Step Run [CA-R-1511]
							/ Workflow Run [CA-R-1510]
						/ Session [CA-R-1971]
					> Project [CA-R-2220]
					> Projection [CA-R-1746]
					> Runtime [CA-R-2194]
					> Scope Unit [CA-R-1757]
						/ Type: Ordered [CA-R-1760]
						/ Type: Unordered [CA-R-1761]
					> Selection [CA-R-1966]
					> Term [CA-R-1318]
				> Aspect [CA-R-2210]
					> Design [CA-R-2216]
					> Documentation [CA-R-2217]
					> Domain [CA-R-2213]
					> Engineering [CA-R-2214]
					> Product [CA-R-2211]
					> Project [CA-R-2212]
					> UX [CA-R-2215]
			> Relation [CA-R-1963]
			> Rule [CA-R-1995]
		> Carrier [CA-R-1958]
			/ Database [CA-R-1955]
			/ Directory [CA-R-1956]
			/ Docker Image [CA-R-2198]
			/ File [CA-R-1957]
			/ Git Branch [CA-R-2200]
			/ Git Commit [CA-R-2199]
			/ Git Index [CA-R-2202]
			/ Git Repository [CA-R-2203]
			/ Pull Request [CA-R-2201]
	> <Project Name> [namespace pattern; CA-R-2207]
```

## Important boundaries

- Project Model contains vocabulary entries for project things. Its Actor member is not a narrower Project Model kind and inherits no properties through that membership.
- The former Aspect branches organize topics. Engineering > Authoring > Code Authoring is topical grouping here, not automatic inheritance of object properties. Exact deeper topic links remain migration candidates rather than a blanket slash replacement.
- Implementation contains actual implementation material. Its Code branch groups existing Code subjects; it does not require every implementation to use every listed unit kind. Code remains distinct from a File Carrier or Directory Carrier.
- `Package > Module`, `Document > Section` and `Journal > Event Record` retain their source-supported part meanings. A particular Module may contain Functions; a Function is not therefore a narrower Module. The Journal/record meaning does not create a new primary Subject identity in this outline.
- A File is a narrower Carrier kind. A Directory containing a File and a Git Repository containing a Git Branch are independent containment relations. There is no blanket permission or requirement for every Carrier to contain another Carrier.
- Actor specializations use `Actor/AI Agent` and `Actor/Operator` directly; no `Type:` qualifier is used in this branch. Atom and Scope Unit kinds retain their complete classification syntax. A bare Content Role or Type axis is a Subject/parameter, not an extra inheriting entity. Do not replace `Atom/Content Role: Plan` with `Atom > Content Role > Plan`.
- Scope Unit is also explicitly a Continuant in R1757. It can participate in that classification while retaining its organizational position under Project Model. Multiple typed links do not create multiple Subject identities.
- Event/Execution/Session denote actual happenings; their records remain separate. Runtime denotes a live context. The old Runtime children Container Run/Process Run require a bounded check against their execution definitions before relocation; this candidate does not infer that they are Runtime subtypes from the old slash paths.
- Documentation under Aspect is an authoring/organization topic; Documentation under Implementation is actual content. Their names do not merge their identities.

## Scope and migration boundary

No named instances, property inventory, new Domain entity, generic Node.Type, Revision entity, Scope Unit reorganization, Terms Graph implementation or production Tool/runtime change is introduced.

The compact outline is not a replacement canonical-ID syntax. Source Subjects keep complete canonical selectors; abbreviated labels do not rename targets. The eventual migration needs a thin table: Atom ID | old Subject | new Subject | status. Resolve exact selectors and grouping links before changing sources; do not infer containment from folders or silently replace every slash.

## Existing Drafts and review follow-up

[A1233](CA-A-1233-SPECIFICATION_PROPOSAL--use-containment-for-organizational-subject-grouping.md) records the accepted containment decision and four prepared successors: R2209@3-draft, R1931@13-draft, R2150@11-draft and R2222@2-draft. They are not promoted.

This proposal supplies the structural correction direction for SG3-I02. It does not claim to resolve the other review findings: incorrect defining references, symbolic Tier vocabulary, omitted Relation Type directions, inconsistent formal-rule paths, or the eleven unresolved Relation Type names. Those retain their separate findings and proposed corrections. No new FPF review or authoritative migration has run for Candidate #11.

## Actor specialization decision

[A1235](CA-A-1235-SPECIFICATION_PROPOSAL--use-direct-actor-kind-paths.md) records the Operator's correction: `Actor / AI Agent` and `Actor / Operator`. These are narrower Actor kinds, not contained parts or named instances. This supersedes the Actor/Type: notation in the previous candidate only; it does not remove other Type or Content Role qualifiers. Candidate editing is not adoption of new Subjects in Current RMED.
