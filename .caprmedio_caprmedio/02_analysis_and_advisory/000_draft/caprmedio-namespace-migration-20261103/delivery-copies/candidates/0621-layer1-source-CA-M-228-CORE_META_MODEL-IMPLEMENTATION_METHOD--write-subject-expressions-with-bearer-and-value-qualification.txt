---
subjects:
  active: CAPRMEDIO <+ MODEL <+ Entity
  passive:
  - CAPRMEDIO <+ MODEL <+ CFEL <+ Relation
  - CAPRMEDIO <+ MODEL <+ Term
  - CAPRMEDIO <+ MODEL <+ Atom/(.Role := Method)
  - CAPRMEDIO <+ MODEL <+ Entity/Object/Continuant/Actor/Operator
  - CAPRMEDIO <+ MODEL <+ CFEL <+ Relation//GOVERNS
  - CAPRMEDIO <+ MODEL <+ CFEL <+ Relation//DEPENDS_ON
version: 34
updated_at: 2026-11-02 00:55:09 +0400
relations: {}
atom_id: CA-M-228
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 3
role: Method
form: Implementation Method
---
## Summary

Write Subject Expressions with Bearer and Value Qualification

## Claim scope

authoring one Entity Expression.

## Claim

Under A1296, follow YAML value interpretation and count null and empty strings as direct values. State any necessary restrictions through the value Format and applicable prose conditions rather than treating them as omitted properties or inventing a universal empty-value policy.

Use prose for cases that do not justify new formal machinery. Keep Tier integer-valued and express its numeric bounds and owner-specific conditions in prose for this review under A1297.

Use string for an Entity value and apply the admitted Entity notation. Do not add a special ref Format or a prior-existence requirement to this basic format check. A defining Atom can introduce its governed entity and path together under CA-A-1285; the path alone supplies no defining authority.

Under CA-A-1283, write a count for each addressed property’s direct values only. Use an explicit {0} on grouping paths such as subjects, while giving their children independent counts. A Claim may carry its formal content directly in a CFEL fence without prose or a separate Formal Claim child. Do not count nested keys as parent values.

Use `{n}` for an exact count, `{n+}` for an unbounded lower limit and `{n..m}` for an inclusive bounded range under CA-A-1280. Use non-negative integer bounds with n <= m; prefer `{0}`, `{0+}`, `{1+}` and `{0..1}` for the common cases. Direct values use `Property[format]{count}`. Relations use two independent slots: `Source {forward-count}RELATION{reverse-count} Target`. For example, `Step {1}+>{1+} Workflow` and `Workflow {1+}<+{1} Step` are equivalent; the first count constrains outgoing links per Source and the second reverse links per Target. Missing slots remain unspecified, and neither slot changes the exactly-one-immediate-whole rule.

**to** write an Entity Expression, start with either a canonical Entity Target reference **or** the exact approved initial lowercase `atom(...)` selector under CA-R-1321, **and** apply `/` in broader-to-narrower order, `//` from an Entity kind to its following named instance, `.` in bearer-to-dependent order, `:` from any X to its allowed value Y, `Part +> Whole` or `Whole <+ Part` for containment, **and** `X >| Y` or `Y |< X` for classification-axis applicability, where Y is the Entity serving as X's Classification. Resolve ordinary named components **other than** the RHS instance name after `//` as Term references under CA-R-1321. The RHS is the instance's name under its separately governed naming/source authority, not an Atom ID and not automatically a Term; the whole qualified path must resolve to exactly one canonical Entity Target that already exists or is explicitly introduced by applicable defining authority under CA-R-1194 and CA-R-1321. In `atom(content_role="Plan").Status`, `Status` is the dependent Property borne by the selected Atom; `Plan` remains the Content Role allowed value qualifying that Atom, **not** Status's bearer **or** Status's allowed value. `.` retains the mechanical native fact Property IS_PROPERTY_OF Bearer; `/` admits no native Entity relation; and `:` does not assign a value. `//` denotes the separate kind/instance Entity connection but syntax alone does not assert or admit an INSTANCE_OF fact, which requires its own Core definition. A defining Atom may introduce the target and path it governs; `@` calls an already declared Entity and `//` names an instance under its applicable source authority. Syntax alone neither creates nor admits a target. The resulting qualified path identifies its canonical target **without** copying it; connecting the Atom **to** that target through GOVERNS **or** DEPENDS_ON creates the Entity Relation, **not** another target Entity.

Use `X/(.Y: Z)` for a Property qualification in this proposal. It identifies an `X` qualified by its own Property `Y` and admitted value `Z`; the qualified `X` is narrower than `X` and inherits applicable `X` features and constraints. `.Y` is neither a primary Entity nor a Property subtype of `X`. The older bare `X/Y: Z` qualification spelling is superseded in this proposal; Current sources and runtime remain unchanged. Method is already a Content Role, so use `Entity/Object/Continuant/Governing Objects/Atom/(.Content Role: Method)` as the concrete canonical example; that syntax alone does not admit Method as a Type. Under [CA-D-478](../../07_delivery/CA-D-478-CORE_META_MODEL-ENG_DECISION--store-every-atom-property-in-one-internal-location.md), the qualified Atom Property maps to its existing metadata property such as `content_role` or `type`, without a nested classification object.

`+>` and `<+` are opposite notation writings of the same containment fact, represented by direct IS_CONTAINED_BY and derived CONTAINS; neither denotes inheritance. Use `>|` and `|<` for the HAS_CLASSIFICATION axis, not membership through IS_CLASSIFIED_BY. The Classification endpoint is an Entity serving that role, not a new Classification kind; IS_CLASSIFIED_BY is a separate membership Relation, not the inverse of HAS_CLASSIFICATION. For Status classification, write:

```text
Entity/Object/Continuant/Governing Objects/Atom.Status >| Status Group: Draft <+ Draft
Entity/Object/Continuant/Governing Objects/Atom.Status >| Status Group: Archived <+ Archived
Entity/Object/Continuant/Governing Objects/Atom.Status >| Status Group: Current <+ * not in (Draft, Archived)
```

Here `*` ranges only over admitted Atom Status values, and Current excludes Draft and Archived within that set. This is proposed Draft authoring guidance, not a parser or runtime claim.

## Details

For actual specialization use `Entity/Object/Continuant/Actor/Operator`. Treat `//` as a single separator token. Structural containment through `+>` or `<+` does not transfer properties. Preserve qualified Atom kinds such as `Atom/(.Content Role: Plan)` rather than treating the relative Property qualification as an intermediate axis or inheriting entity kind. Alternative target resolution, literal delimiters and containment constraints remain pending in CA-A-1236; this Draft does not choose them.

### Existing-target reference marker

Use `@` to call an already declared Entity instead of declaring it at that schema position. Preserve the base relation meaning and resolve the intended canonical target. Do not create a new target or infer independent existence merely from the reference marker.

### Literal-character escaping

Use backslash escaping for literal operator characters in names, such as `Engineering/CI\/CD` or `Workflow//Release 0\.4` in abbreviated explanatory paths. Use `\\` for a literal backslash. Do not add a second Entity-name quoting syntax; YAML string quoting is carrier syntax. Preserve the escape through serialization, and do not use a final unmatched backslash.

### Reference boundary

Use `@` for an already declared Entity. Parentheses group the intended expression before any outer continuation. For example, the explanatory `Entity/Object/Continuant/@(Scope Unit).ID` calls Scope Unit first, then addresses its ID property. Full ordinary Entity spelling remains in sources; an @ call does not declare another Entity.

### Canonical path changes

When a kind's canonical declaration path changes, migrate affected Current ordinary Entity paths and full-path references; @ references using an unchanged unique primary-kind name remain valid. A primary-kind rename requires migrating its name-based references as well. Keep no old-path aliases or alias registry for now. Preserve the distinction between Current reference maintenance and unchanged archived historical evidence; this Draft does not perform a migration.

### Unique primary-kind names

Distinct primary-kind declarations have unique names across the effective Entity model, not only the selected projection. Repeated references to the same kind do not declare duplicates. Properties may reuse names under different bearers. `@(Module)` is therefore an admitted existing-kind reference. A branch move preserves name-based references when the primary-kind name is unchanged; a rename requires their migration. Keep no aliases. This naming rule does not automatically rename conflicting Current kinds or waive the full structure of ordinary Entity paths.

### General named-relation notation

When a formal Claim or model view needs a Relation without a short operator, write `Source ((RELATION_TYPE)) Target`. Resolve the exact declared type and its source/target constraints; keep its declared direction. For the opposite navigation use its defined derived inverse type in the same syntax. Do not invent a backward operator, register a type by writing its name, duplicate the stored inverse, or place the whole statement in subjects.governs when that field identifies a node. CA-R-1931's successor Draft owns this syntax; CA-A-1240 records its acceptance for this Draft package.
