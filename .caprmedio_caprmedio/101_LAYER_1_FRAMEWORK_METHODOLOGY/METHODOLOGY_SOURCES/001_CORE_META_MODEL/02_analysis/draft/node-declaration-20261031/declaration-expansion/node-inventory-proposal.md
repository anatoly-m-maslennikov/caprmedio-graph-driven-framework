# Smaller Node inventory — selected

Status: selected by the Operator. Declaration Draft coverage is being checked.

## Primary Nodes

```text
Node
/ Actor
/ Atom
  /(.Role: Concern)
  /(.Role: Analysis)
  /(.Role: Plan)
  /(.Role: Requirement)
    /(.Form: Declaration)
    /(.Form: Relation Definition)
  /(.Role: Method)
  /(.Role: Evaluation)
  /(.Role: Delivery)
  /(.Role: Operations)
    / Workflow
    / Step
    / Substep
    / Action
/ Scope Unit
  / Project
/ Aspect
/ Package
  / Implementation
/ Projection
/ Journal
```

This is an inventory view of the selected model. Current sources have not moved.

## Why these Nodes

- Actor: identity and authority.
- Atom: governed content.
- Scope Unit: formal Scope boundaries.
- Project: the root Scope Unit.
- Aspect: Project aspect instances.
- Package: implementation structure.
- Implementation: the root Package kind.
- Projection: derived views.
- Journal: recorded events.

## Properties

- Keep each Property under its bearer.
- Declare its direct-value Format.
- Declare its direct-value cardinality.
- Declare its dependent-entity Format.
- Declare its dependent-entity cardinality.
- Use `p.*[]{0}` when neither local nor inherited rules declare dependents.
- Preserve declared nested Properties, such as Tier.Label.
- Resolve inherited Properties to their original Declaration.

## Boundaries

- Primary Node is an Independence case.
- Property is an Independence case.
- Neither is a new subtype branch here.
- CFEL is a separate model component.
- Carrier is a separate model component.
- Terms are vocabulary.
- Legacy Object, Continuant, Occurrent are not imported automatically.
- Actual Workflow instances remain deferred.

## Coverage

The selected inventory has 24 Primary Nodes. Each now has a Declaration Draft. Property contracts remain under review.

Scope Unit.structural_level and Package.structural_level derive from containment. Roots have level 0; a child has its parent level plus 1.
