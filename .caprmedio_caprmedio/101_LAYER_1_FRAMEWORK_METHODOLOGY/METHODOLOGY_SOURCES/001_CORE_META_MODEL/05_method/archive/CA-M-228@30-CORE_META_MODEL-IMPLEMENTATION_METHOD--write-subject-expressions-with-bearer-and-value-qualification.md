---
subjects:
  governs: Entity
  depends_on:
  - Entity
  - Entity/Graph Syntax > Relation
  - Entity/Object/Continuant/Term
  - Entity/Graph Syntax > Relation//GOVERNS
  - Entity/Graph Syntax > Relation//DEPENDS_ON
version: 30
updated_at: 2026-10-29 07:32:39 +0400
relations: {}
atom_id: CA-M-228@30
content_role: Method
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 3
type: Implementation Method
---
## Summary

Write Entity Expressions with Bearer and Value Qualification

## Claim scope

authoring one Entity Expression.

## Claim

Under A1296, follow YAML value interpretation and count null and empty strings as direct values. State any necessary restrictions through the value Format and applicable prose conditions rather than treating them as omitted properties or inventing a universal empty-value policy.

Use prose for cases that do not justify new formal machinery. Keep Tier integer-valued and express its numeric bounds and owner-specific conditions in prose for this review under A1297.

Use string for an Entity value and apply the admitted Entity notation. Do not add a special ref Format or a prior-existence requirement to this basic format check. A defining Atom can introduce its governed entity and path together under CA-A-1285; the path alone supplies no defining authority.

Under CA-A-1283, write a count for each addressed property’s direct values only. Use an explicit {0} on grouping paths such as subjects, while giving their children independent counts. Required direct Claim prose is not supplied by its optional Formal claim child. Do not count nested keys as parent values.

Use `{n}` for an exact count, `{n+}` for an unbounded lower limit and `{n..m}` for an inclusive bounded range under CA-A-1280. Use non-negative integer bounds with n <= m; prefer `{0}`, `{0+}`, `{1+}` and `{0..1}` for the common cases. Attach property counts to the property and containment counts to >, without conflating parts-per-whole with the immediate-whole count.

**to** write an Entity Expression, start with either a canonical Entity Target reference **or** the exact approved initial lowercase `atom(...)` selector under CA-R-1321, **and** apply `/` in broader-to-narrower order, `//` from an Entity kind to its following named instance, `.` in bearer-to-dependent order, `:` in Property-to-allowed-value order, **and** `>` from a structural whole to its part. Resolve ordinary named components **other than** the RHS instance name after `//` as Term references under CA-R-1321. The RHS is the existing instance's name under its separately governed naming/source authority, not an Atom ID and not automatically a Term; the whole qualified path must still resolve to one existing canonical Entity Target. In `atom(content_role="Plan").Status`, `Status` is the dependent Property borne by the selected Atom; `Plan` remains the Content Role allowed value qualifying that Atom, **not** Status's bearer **or** Status's allowed value. `.` retains the mechanical native fact Dependent IS_BORNE_BY Bearer, **and** `:` retains AllowedValue IS_ALLOWED_VALUE_OF Property; `/` admits no native Entity relation. `//` denotes the separate kind/instance Entity connection but syntax alone does not assert or admit an INSTANCE_OF fact, which requires its own Core definition. A defining Atom may introduce the target and path it governs; only explicit `@(...)` existing-kind references and `//` named-instance references require their referenced target or instance to exist. The resulting qualified path identifies its existing canonical target **without** copying it; connecting the Atom **to** that target through GOVERNS **or** DEPENDS_ON creates the Entity Relation, **not** another target Entity.

## Details

For actual specialization use `Entity/Object/Continuant/Actor/Operator`. Treat `//` as a single separator token. Structural containment does not transfer properties. Preserve qualified Atom kinds such as `Atom/Content Role: Plan` rather than treating the intermediate axis as an inheriting entity kind. Alternative target resolution, literal delimiters and containment constraints remain pending in CA-A-1236; this Draft does not choose them.

### Existing-target reference marker

Use `@` after `/` or `>` when referencing an existing kind instead of declaring it at that schema position. Preserve the base relation meaning and resolve the intended canonical target. Do not create a new target or infer independent existence merely from the reference marker.

### Literal-character escaping

Use backslash escaping for literal operator characters in names, such as `Engineering/CI\/CD` or `Workflow//Release 0\.4` in abbreviated explanatory paths. Use `\\` for a literal backslash. Do not add a second Entity-name quoting syntax; YAML string quoting is carrier syntax. Preserve the escape through serialization, and do not use a final unmatched backslash.

### Reference boundary

Use `@(...)` for an existing-kind reference after `/` or `>`, with a unique primary-kind name or its current canonical path. Keep the matching closing parenthesis before any outer continuation. For example, the explanatory `Entity/Object/Continuant/@(Scope Unit).ID` references Scope Unit first, then addresses its ID property. Full ordinary Entity spelling remains in sources; a unique primary-kind name is now an admitted @ reference payload, not merely a shortened display.

### Canonical path changes

When a kind's canonical declaration path changes, migrate affected Current ordinary Entity paths and full-path references; @ references using an unchanged unique primary-kind name remain valid. A primary-kind rename requires migrating its name-based references as well. Keep no old-path aliases or alias registry for now. Preserve the distinction between Current reference maintenance and unchanged archived historical evidence; this Draft does not perform a migration.

### Unique primary-kind names

Distinct primary-kind declarations have unique names across the effective Entity model, not only the selected projection. Repeated references to the same kind do not declare duplicates. Properties may reuse names under different bearers. `@(Module)` is therefore an admitted existing-kind reference. A branch move preserves name-based references when the primary-kind name is unchanged; a rename requires their migration. Keep no aliases. This naming rule does not automatically rename conflicting Current kinds or waive the full structure of ordinary Entity paths.

### General named-relation notation

When a formal Claim or model view needs a Relation without a short operator, write `Source ((RELATION_TYPE)) Target`. Resolve the exact declared type and its source/target constraints; keep its declared direction. For the opposite navigation use its defined derived inverse type in the same syntax. Do not invent a backward operator, register a type by writing its name, duplicate the stored inverse, or place the whole statement in subjects.governs when that field identifies a node. CA-R-1931's successor Draft owns this syntax; CA-A-1240 records its acceptance for this Draft package.
