# Property contract review

Read-only review of the current Property rules and selected Declaration
examples. It does not change Current sources.

## Existing facets

1. Property occurrence cardinality: `p{:n}`.
   Example: `Atom.Status{:1}`.
   Source: `CA-R-2472`, Claim lines 21-22; `CA-R-2488`, Claim line 21.

2. Direct value format and value cardinality: `p: [format]{:n}`.
   Example: `asdf: [string]{:1}`.
   Source: `CA-R-2472`, Claim lines 22 and 37.

3. Immediate dependent-Property name format and name cardinality:
   `p.*[name format]{:n}`.
   Example: `asdf.*[in (aaa, bbb)]{:1}`.
   Source: `CA-R-2472`, Claim lines 23 and 38.

4. Recursive dependent-Property name format and aggregate selected-name
   cardinality: `p.**[name format]{:n}`.
   Example: `Atom.Content.**[string]{:0+}`.
   Source: `CA-R-2472`, Claim lines 24 and 44.

5. Selected dependent Property value format and per-Property value
   cardinality: `p.*[name format]{:n}: [value format]{:m}`.
   Example: `asdf.aaa{:0..1}: [atom id]{:1}`.
   Source: `CA-R-2472`, Claim lines 25 and 39-40.

6. Full-path identity and sibling-name uniqueness.
   `x.y.z` and `x.z` are distinct; names are unique within one bearer.
   Source: `CA-R-2472`, Claim line 30.

7. Explicit empty dependent-Property set.
   Use `p.*[]{:0}` when no dependent names are declared.
   Source: `CA-R-2472`, Claim line 32. This is the current source wording;
   the latest contract decision strengthens the closed-world interpretation
   to forbid undeclared dependent entities.

8. Allowed values are distinct from assigned instance values.
   `X:Y` admits one `IS_ALLOWED_VALUE_OF` fact; it does not assign a value or
   set direct-value cardinality. A `HAS_VALUE` binding assigns a literal to a
   Property instance. Literals are not graph Nodes.
   Sources: `CA-R-1245`, Claim line 28; `CA-R-2474`, Claim lines 21-23.

9. Immediate bearer cardinality is distinct from value cardinality.
   A declared Property occurrence has exactly one immediate bearer through
   `IS_PROPERTY_OF`; this does not constrain how many values the Property has.
   Source: `CA-R-2003`, Claim lines 29 and 33.

10. Effective inherited rules apply to instances.
    Inheritance carries declared Properties, Formats, value domains, direct
    value cardinalities, nested-Property cardinalities and Relation
    cardinalities. It does not copy actual values or Relation facts.
    Source: `CA-R-2470`, Claim lines 22-31.

## Smallest complete Property checklist

For a Property declaration, keep these separate:

- Property occurrence cardinality on its bearer.
- Direct literal value format.
- Direct literal value cardinality.
- Allowed literal-value set, when restricted.
- Immediate child-Property name format or whitelist.
- Immediate child-Property name cardinality.
- Recursive child-Property name format or whitelist.
- Recursive selected-name cardinality.
- Per-child direct value format.
- Per-child direct value cardinality.
- `IS_PROPERTY_OF` bearer binding/cardinality.
- Permitted dependent-Property relations, through the effective Relation
  whitelist.

At instance level, `HAS_VALUE` is a literal binding, not a Node-to-Node
Relation. `HAS_PROPERTY` is the reverse graph view of `IS_PROPERTY_OF` only
when explicitly declared as such; its permission and cardinality are not
inferred automatically.

## Remaining precision gaps

- The source uses `{:n}` while the latest notation discussion uses `{n}` for
  allowed cardinality and reserves `{:x}` for allowed values. Migration must
  choose one canonical spelling before parser adoption.
- `p.**` needs one explicit sentence that its count is over selected full
  Property occurrences/names across all descendant depths, not a separate
  count per depth.
- A Property declaration should state whether its child-name selector is an
  exhaustive whitelist. The latest decision is to close undeclared child
  slots with `.[]{0}`/`p.*[]{0}`; current CA-R-2472 still says that a missing
  annotation remains undefined.
- `HAS_VALUE` has a clear instance binding rule, but its formal cardinality
  is supplied by the Property declaration; no separate value Node or
  Declaration should be introduced.

