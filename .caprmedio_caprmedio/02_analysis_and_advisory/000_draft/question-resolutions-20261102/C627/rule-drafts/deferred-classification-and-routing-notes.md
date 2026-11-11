# Deferred Linear and Conditional classification and routing notes

These notes are preserved verbatim from the pinned Current sources. They are not staged Atom content and do not constrain actual Workflow instances.

## CA-R-1569@25

> - a Linear Step model definition has ordered nonconditional Substep definitions only.
> - a Conditional Step model definition chooses exactly **`1`** branch in its own definition from its declared result condition and **may** use Actor input; result-based routing belongs to that definition.

## CA-R-1570@24

> a Workflow Atom **must** own **only** its graph scheme: Step references, declared order and structural Relations, entry points, **and** terminal outcomes. a Conditional Step definition owns its result-based routing; the Workflow graph does not use a separate result-transition Relation.

The sources are pinned in [manifest.json](../manifest.json). Review these notes only with the deferred actual-Workflow review.
