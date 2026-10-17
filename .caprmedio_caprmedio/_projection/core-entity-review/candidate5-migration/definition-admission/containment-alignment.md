# Containment — minimal definition-admission alignment

Review packet, 2026-10-16. Proposed text only; no source changes, ID allocation or activation.

## Boundary

This packet covers containment conflicts affecting the proposed `Atom.Enabled Relations.Contains` definition, not all 45 definition drafts. Candidate #6 decisions 1, 17, 20 and 28 apply: a Container Atom remains an Atom; Plan, Workflow and nested Step containment is admitted; named Operations remain project configuration; construction/CONTAINS graph implementation stays deferred. Plan labels are not Types or subtypes. Containment does not replace Scope Unit ownership, Goal/Demand targets, or semantic parent/child relations.

The current review draft is:

`../empty-r-drafts/CA-R--CORE_META_MODEL--define-atom-enabled-relations-contains.md` — Version 2, Draft, no Atom ID.

Its Claim defines a kind-level Boolean capability with default False. True permits children but does not require them. It does not yet enable any particular Content Role or Type.

## Source evidence

All paths below are relative to the repository root. `R/` abbreviates:

`.caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/`

| Source | Version | Exact path after `R/` | Relevant current claim |
| --- | --- | --- | --- |
| CA-R-1378 | 11 | `CA-R-1378-CORE_META_MODEL-CORE--define-atom-collection.md` | Collection is a Structural Entity grouping Atoms, without becoming their owning Scope Unit. |
| CA-R-1379 | 11 | `CA-R-1379-CORE_META_MODEL-CORE--classify-atom-collection-as-a-structural-entity.md` | Atom Collection is NARROWER_THAN Structural Entity. |
| CA-R-1265 | 14 | `CA-R-1265-CORE_META_MODEL-CORE-REQUIREMENT--keep-atom-collection-outside-the-atom-taxonomy.md` | Atom Collection must not be NARROWER_THAN Atom. |
| CA-R-1368 | 10 | `CA-R-1368-CORE_META_MODEL-CORE--define-containment-relation-pair.md` | CONTAINS and inverse-derived IS_CONTAINED_BY belong to the Structural Entity containment domain. |
| CA-R-1383 | 11 | `CA-R-1383-CORE_META_MODEL-GENERAL--permit-nested-atom-collections.md` | An Atom Collection may directly contain another Atom Collection. |
| CA-R-1381 | 10 | `CA-R-1381-CORE_META_MODEL-CORE--define-ad-hoc-as-an-atom-collection-type.md` | Ad Hoc is an Atom Collection Type. |
| CA-R-1546 | 5 | `CA-R-1546-CORE_META_MODEL-GENERAL-REQUIREMENT--register-core-atom-collection-type-values.md` | Core collection Types must be Ad Hoc; Plan labels must not create collection Types. |
| CA-R-1376 | 13 | `CA-R-1376-CORE_META_MODEL-CORE--define-structural-entity.md` | Old Structural Entity organizes other Entities through containment. |
| CA-R-1498 | 5 | `CA-R-1498-CORE_META_MODEL-CORE-REQUIREMENT--derive-recursive-containment-from-direct-containment.md` | Recursive Structural Entity containment is the transitive closure of direct containment. |
| CA-R-1576 | 7 | `CA-R-1576-CORE_META_MODEL-CORE-REQUIREMENT--define-plan-labels.md` | Version, Objective, Epic, Task and related names are navigation Labels, not authoring subtypes. |
| CA-R-1578 | 6 | `CA-R-1578-CORE_META_MODEL-CORE-REQUIREMENT--define-hub-atom-as-a-derived-description.md` | Hub is derived from DECOMPOSES_INTO, not another Type. |
| CA-R-1508 | 10 | `CA-R-1508-CORE_META_MODEL-CORE-REQUIREMENT--define-workflow.md` | Workflow is an Operations Atom defining a reusable Step graph; Step references do not copy definitions. |
| CA-R-1509 | 8 | `CA-R-1509-CORE_META_MODEL-CORE-REQUIREMENT--define-step.md` | Step references one Action; different Steps may reuse an Action without copying it. |
| CA-R-1570 | 6 | `CA-R-1570-CORE_META_MODEL-GENERAL-REQUIREMENT--keep-workflow-graphs-separate-from-step-bindings.md` | Workflow owns its scheme; Steps own bindings; Actions own behavior; nesting does not replace control flow. |

## Direct admission blockers

### 1. Retire the contradictory non-Atom collection definitions

CA-R-1378, CA-R-1379 and CA-R-1265 currently govern `Container Atom`, but their Claims describe the rejected non-Atom model. Keeping them Active while admitting the proposed capability would retain a direct contradiction.

Proposed disposition: archive these three sources through the normal lifecycle path; preserve their previous bytes/history. Do not rewrite their old Summaries to describe the opposite model under their existing IDs.

- CA-R-1378 Summary `Define Atom Collection` would need changing to `Define Container Atom` to represent the new meaning. Under the accepted identity rule that requires a new ID; no ID is allocated here. The smaller option is no separate replacement: include the Container Atom meaning in the capability draft's Details below.
- CA-R-1379 Summary explicitly classifies the old collection under Structural Entity. Retire without a replacement classification Atom.
- CA-R-1265 Summary explicitly excludes collections from Atom. Retire without a replacement inverse prohibition.

The valid ownership distinction in CA-R-1378 is preserved in the capability draft's proposed Details. Folder-only groupings and named Selections are not silently converted into Atoms by this retirement.

### 2. Align the existing containment pair, preserving its identity

CA-R-1368 Version 10: keep ID and Summary `Define Containment Relation Pair`. The same relation pair remains; only the obsolete domain and Subject are aligned. The successor would be Version 11 on actual update.

Exact proposed Subjects:

```yaml
subjects:
  governs: "Entity/Continuant/Object/Relation/Type: CONTAINS"
  depends_on:
    - "Entity/Continuant/Object/Atom.Enabled Relations.Contains"
    - "Entity/Continuant/Object/Scope Unit"
```

Exact proposed Scope:

> Direct containment and its derived inverse, including Scope Unit containment and enabled Atom containment.

Exact proposed Claim:

> the Containment Relation Pair **means** direct relation `CONTAINS` **and** its inverse-derived relation `IS_CONTAINED_BY`. a Scope Unit **may** contain other Scope Units **and** governed content. an Atom **may** contain other Atoms **when** containment is enabled for its Content Role **or** Type.

Exact proposed Details:

> `IS_CONTAINED_BY` is derived from `CONTAINS`; it is not independently authored. Containment does not make a contained Atom part of the containing Atom's Substance or change its owning Scope Unit. This relation definition does not implement or require a construction graph projection.

The exact inverse spelling is preserved from the existing R; do not introduce a second primitive inverse. This change does not assign a mandatory file layout or conflate filesystem nesting with all semantic relations.

### 3. Complete the capability draft without inventing a Container Type

Keep the capability draft's current Summary, Subject, Scope and Claim. Append this exact text to its Details when preparing the revised draft:

> Container Atom describes an Atom whose Content Role or Type permits it to contain other Atoms. It is not another artifact form or an additional Content Role or Type. Contained Atoms retain their own Substance and owning Scope Unit. Permitting containment does not require the Atom to contain anything.

No new draft or ID is needed solely to repeat that meaning.

### 4. Enable only the already-approved kinds

The default-False capability alone does not enable Plan, Workflow or Step containment. Three narrow new R drafts are needed if this admission includes those approved permissions. In particular, leaving Step containment disabled would contradict Candidate #6 decision 17, which retains nested substeps. These drafts have no existing IDs to preserve; allocate only during the authorized creation workflow.

#### Plan permission

Summary: `Enable containment for Plan Atoms`.

```yaml
subjects:
  governs: "Entity/Continuant/Object/Atom/Content Role: Plan.Enabled Relations.Contains"
  depends_on:
    - "Entity/Continuant/Object/Atom.Enabled Relations.Contains"
```

Scope: `Containment capability of Plan Atoms.`

Claim:

> `Atom/Content Role: Plan.Enabled Relations.Contains` **must** be True. a Plan Atom **may** contain other Plan Atoms.

Details:

> Plan labels such as Epic, Task and Version do not create different containment Types. Containment is optional and can nest. This permission does not implement a Plan projection or replace other typed relations between Plans.

#### Workflow permission

Summary: `Enable containment for Workflow Atoms`.

```yaml
subjects:
  governs: "Entity/Continuant/Object/Atom/Content Role: Operations/Type: Workflow.Enabled Relations.Contains"
  depends_on:
    - "Entity/Continuant/Object/Atom.Enabled Relations.Contains"
    - "Entity/Continuant/Object/Atom/Content Role: Operations/Type: Step"
```

Scope: `Containment capability of Workflow Atoms.`

Claim:

> `Atom/Content Role: Operations/Type: Workflow.Enabled Relations.Contains` **must** be True. a Workflow Atom **may** contain Step Atoms.

Details:

> The Workflow remains an Atom. Its Steps retain their own definitions and Action references. This permission does not copy shared Actions into a Workflow or replace its declared control flow with folder order.

#### Step permission

Summary: `Enable containment for Step Atoms`.

```yaml
subjects:
  governs: "Entity/Continuant/Object/Atom/Content Role: Operations/Type: Step.Enabled Relations.Contains"
  depends_on:
    - "Entity/Continuant/Object/Atom.Enabled Relations.Contains"
```

Scope: `Containment capability of Step Atoms, including nested substeps.`

Claim:

> `Atom/Content Role: Operations/Type: Step.Enabled Relations.Contains` **must** be True. a Step Atom **may** contain other Step Atoms.

Details:

> A substep is a nested Step, not a separate Type. Containment is optional and can nest. This permission does not change a Step's Action reference or input bindings, prescribe how internal tool calls are modeled, or introduce a storage layout or execution protocol.

No blanket permission for every Operations Type is added. Step-to-Step containment implements the already-approved nested-substep permission; serialization and unrelated Action containment are not introduced here.

## Related rules — exact limits on this admission

- **CA-R-1383:** its permission to nest the old collection kind is not a valid substitute for the three new enabling rules. Retire it with the obsolete collection definition if that concept is retired in this batch. Renaming it to `Permit Nested Container Atoms` changes its Summary and needs a new ID; no such extra Atom is necessary for the minimal packet because the approved Plan and Step nesting permissions above cover the concrete requirements.
- **CA-R-1381:** dedicated Ad Hoc collection Type definition belongs with retirement of the obsolete collection concept. No replacement Container Type is proposed.
- **CA-R-1546:** mixed content, not safe whole-Atom deletion. Its mandatory Ad Hoc registry is obsolete, but its Plan-label distinction remains valid and already has substantive coverage in CA-R-1576. A later retirement can rely on CA-R-1576 after checking references; do not rewrite the old registry into a different claim under the same Summary merely to admit the capability. It does not prohibit Plan containment and is not a prerequisite for admitting the generic Boolean definition.
- **CA-R-1376:** general old partition retirement is a separate lane. Do not turn Structural Entity into a new Container Atom root. Removing the dependency from R1368 avoids relying on it for the new permission; retaining it temporarily does not define Containers as non-Atoms once R1378/R1379/R1265 are retired.
- **CA-R-1498:** later relation-content alignment. Recursive reachability can remain derived; no new recursive relation, stored field or graph implementation is needed to admit the capability. Its stale Structural Entity names should not expand this admission into construction-graph work.
- **CA-R-1576:** no content change needed here; it already rejects Plan-label subtypes. Its older Subject notation in the Claim is later text migration.
- **CA-R-1578:** do not replace `DECOMPOSES_INTO` with `CONTAINS` mechanically. It describes another relation and is outside this minimal admission.
- **CA-R-1508, CA-R-1509 and CA-R-1570:** preserve reusable definitions, Step bindings, shared Actions and declared control flow. Allowing a Workflow to contain Steps or a Step to contain substeps does not transfer their content into the containing Atom's Substance. These definitions need no additional capability field or serialization clause; the separate Workflow and Step permission rules above provide the required enablement.
- **CA-R-1409 and construction projection RMED:** remain deferred. They are not required to define or use `CONTAINS`.

## Acceptance check for the future apply

1. The three contradictory container/non-Atom Claims are no longer Active before the new definition is admitted; no historical bytes are rewritten.
2. R1368 retains its identity, Summary and inverse-derived pair, with the obsolete domain removed.
3. Container remains an Atom description, not a new primary entity, artifact form, Type or Label subtype.
4. The generic default remains False; only explicitly approved kind permissions are enabled. No per-instance Boolean field is required.
5. Containment preserves Atom Substance, Scope Unit ownership and shared Action references; it does not replace unrelated parent/child, decomposition or control-flow relations.
6. No construction graph, Plan projection, code change or blanket source migration is included.

This packet does not certify active R coverage or perform the changes. Re-read source Versions before preparing the actual updates.
