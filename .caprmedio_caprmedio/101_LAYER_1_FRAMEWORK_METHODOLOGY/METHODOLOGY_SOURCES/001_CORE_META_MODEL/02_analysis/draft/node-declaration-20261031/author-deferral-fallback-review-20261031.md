# Author deferral and omission fallback — 2026-10-31

Author is deferred and removed from the selected proposed artifacts. The Operator registry is preserved. Existing inheritance needs no extra operator or value-resolution stage.

## Draft changes

- Withdraw the unpublished Atom.Author Declaration. Its snapshot remains in review evidence, not in the target Node inventory.
- Remove author frontmatter from 100 existing selected carriers: the surviving registered Drafts, the proposal and Epic successor Draft. The new fallback Rule is also authorless.
- Omit author in the proposed Atom Carrier contracts.
- Add [CFEL omission fallback](../../../04_requirement/draft/node-declaration-20261031/CA-R-draft-CORE_META_MODEL-CFEL--fallback-when-omitted.md) and use it in [Atom.Label](../../../04_requirement/draft/node-declaration-20261031/property-expansion/CA-R-draft-CORE_META_MODEL-DECLARATION--declare-atom-label.md).
- Update the proposal, Epic Draft, Draft register and selected Node inventory.

```CFEL
Atom.Label{0..1}: [string]{1};
Atom.Label.*[]{0};
Atom.Label ?= Atom.Form
```

## Fallback meaning

- Trigger only when the selected bearer has zero authored occurrences of the Property.
- A supplied Property does not trigger fallback. Null, an empty string, zero and false are values, not omission.
- Existing declarations and inherited constraints apply normally. There is no inherited instance-value lookup stage.
- Bind both Property paths to the same bearer. Resolve a Property value or literal on the right.
- Validate the resolved value against the left Property's Format and value count.
- Do not write a Carrier or change authored presence. A fallback cannot satisfy a required authored occurrence.
- Report missing right-side values, cycles and multiple applicable fallbacks as errors.

## Contract examples

These are semantic review cases, not executable parser tests.

| Authored input | Result |
|---|---|
| Form = Declaration; Label omitted | Resolve Label to Declaration; do not store Label |
| Form = Declaration; Label = Custom | Resolve Label to Custom; ignore fallback |
| Form = Declaration; Label is an empty string | Keep the supplied empty string if its Format permits it; do not use fallback |
| Label = null under the string Format | Invalid supplied value; do not replace it with fallback |
| Label omitted; Form unresolved | Error resolving the fallback |
| Required authored Property omitted, with a fallback | Presence error remains; fallback does not fabricate the field |

No literal defaults or source paths were invented for confidence threshold or retry limit. Their applicable policies remain as declared.

## Verification

- Independent Terra review passed after removing an implied inherited-value lookup stage and clarifying authored presence and same-bearer binding.
- All 99 registered Drafts have no author metadata. The proposal and Epic successor Draft are also authorless.
- The packet has 23 Primary and 45 Property Declarations; the removed Property is Author.
- Formal-only Claims increased from 40 to 41, and from 37 at the start of the formalization work.
- Register hashes, local links and bounded Draft structure checks pass.
- The Operator registry and all 11 specifically pinned Current sources match their pre-change hashes.
- All 750 snapshotted Current Core Requirement sources and Current Epic version 37 remain unchanged.

See [result evidence](declaration-expansion/author-deferral-result.json), [pre-change inventory](declaration-expansion/author-deferral-inventory.json) and [withdrawn Draft snapshot](declaration-expansion/withdrawn-author-property.json).

## Current adoption boundary

Current CA-R-655@42, CA-R-1078@31, CA-R-1080@29, CA-R-2102@13, CA-R-2356@1, CA-D-274@30 and CA-D-463@25 still require or carry Author. These sources were not promoted, retired or rewritten. The authorless Draft packet follows the Operator's latest target-format instruction; bounded structural checks do not prove conformance with those legacy Author-required rules. Reconcile them and their consumers before Current adoption.

No parser, runtime, storage migration or Current carrier changes were performed.
