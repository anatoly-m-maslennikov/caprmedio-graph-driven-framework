# CONTRIBUTES_TO contribution lane

## Proposed minimum

Prepare one new Requirement / Declaration with local key
`contributes-to-relation-declaration`, Summary **Declare CONTRIBUTES_TO**, and
Main Subject `CAPRMEDIO_MODEL <+ CFEL <+ Relation//CONTRIBUTES_TO`.

The proposed direct relation is:

```CFEL
# model
Relation//CONTRIBUTES_TO ((HAS_CLASSIFICATION)) Derivation == Direct;

# instances
Atom//$contributor ((CONTRIBUTES_TO)) Atom//$contribution
```

Its Host and Target are both Atom instances without Role/Form restriction.
The Relation records contribution and does not by itself prove Requirement
satisfaction. An Atom need not author a link; an explanatory Requirement is
preferred guidance, not an endpoint restriction or an authoring prerequisite.

## Required companion permission

Node's general outgoing-relation default is zero, and Atom currently names only
its IS_CONTAINED_BY, HAS_ACTIVE_SUBJECT, and GOVERNS permissions. The narrow
required companion proposal is an addition to CA-R-2508's instance Formal
Claim:

```CFEL
Atom//$atom {::0+}((CONTRIBUTES_TO));
```

This gives every Atom zero-or-more **outgoing** contribution links in the
declaration's Atom-to-Atom endpoint domain. It does not add an incoming target
permission, an inverse, a global Node exception, a required link, or an upper
bound. No change to CA-R-2462's `((*))` default is proposed.

## No inverse or alias

No separate inverse Relation is justified: no different reverse meaning has
been approved. Reverse writing can describe the same authored fact under the
existing endpoint rules. No symbolic alias is needed, so none is proposed.

## Optional Method guidance

If normative authoring guidance is needed, prepare it as a separate Method
proposal using an already admitted guidance Form. It may say that an RMEDO
Solution, Direct Policy, Approach Policy, or Decision links to an existing
Requirement that explains its purpose. Do not fabricate a Requirement to fill
the link. The link does not prove satisfaction; applicable Evaluation and
implementation evidence do. This guidance does not narrow the general Relation
to Requirement targets or admit Forms by itself.

## Source pins

| Source | SHA-256 | Why it matters |
| --- | --- | --- |
| CA-A-1328@1-draft | `d4ceb6d13191f6fbbfc291602efecf4ea6b6751201e524b4043bccf2618c4f98` | General contribution Relation, optional explanatory-R guidance, and no satisfaction inference. |
| CA-R-2486@6 | `039c43fd71e77dfb733bad0e0bc72cafc8f71e9eb353a878244e39bb76f42f8e` | Direct declaration owns endpoint signature; outgoing direction needs permission. |
| CA-R-2588@5 | `53fe4d15d07776dc19a0d11ccd9c6c63de4b3c12fe32bc92d61a5be975bf8fe5` | Zero default and explicit named outgoing permission behavior. |
| CA-R-2508@8 | `0d30d5a01af09777d7cc465b66e15997783f41298d3e85376fa458897031a666` | Exact Atom permission owner to amend. |
| CA-R-2462@6 | `725a3a66f857394014fa7c77fe734d6725eeb69455d5b9ad8655b8c0e28b49ec` | Keep Node wildcard default closed. |
| CA-R-2618@3 | `875c1cbc4aa0656a57d574fa1849e73c9838e4ae303ea976c2a270036551a01d` | Existing direct Atom-host relation declaration pattern. |
| CA-R-2485@7 | `6f80f1195b52133763aa132279eb0adc42aa9215edfc6b96d5e55f312f9c7176` | HAS_INVERSE needs a distinct derived Relation; it is not automatic. |

## Source check

The live A1328 manifest points to the pinned `scope-delegation` Draft and the
same SHA-256. It is a valid source pin for this proposal.

## Open items

No endpoint ambiguity remains: the approved direction is Atom to Atom; the
explanatory Requirement target is optional guidance. ID allocation, exact Draft
placement, and promotion remain Root-owned. No native source was changed.
