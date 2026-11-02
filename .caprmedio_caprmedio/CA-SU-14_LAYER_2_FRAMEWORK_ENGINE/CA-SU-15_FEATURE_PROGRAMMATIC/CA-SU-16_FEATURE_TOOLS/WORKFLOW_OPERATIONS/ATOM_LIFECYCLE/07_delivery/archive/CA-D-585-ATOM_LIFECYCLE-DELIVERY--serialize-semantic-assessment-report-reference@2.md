---
atom_id: CA-D-585
content_role: Delivery
current_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
author: Anatoly Maslennikov
status: Active
subjects:
  governs: "Workflow Operations/Atom Lifecycle/Semantic Assessment Report Reference"
  depends_on: ["CA-R-1892", "CA-D-531", "CA-D-532"]
version: 2
updated_at: "2026-10-12 04:20:25 +0400"
relations:
  delivery_for: [CA-R-1892]
---
# Summary

Serialize semantic assessment report reference

## Scope

The optional external evidence field of one lifecycle Update request and its retained O145/O129 result evidence.

## Claim

The request representation of external semantic evidence **must** be `semantic_assessment_report: {path, digest}`, with `path` a canonical Project-relative path and `digest` its lowercase SHA-256, bound to the report representation below.

## Details

The referenced report stores exactly one canonical JSON object at `## Results` / `### Update assessment evidence`, with no aliases. The object contains exact target and proposal pins, CA-R-1432 and CA-R-1464 authority pins, the admitted class, `primaryClaimIdentityPreserved: true`, a nonempty declared delta and nonempty lineage-evidence pins. Every pin is `{path, digest}` except the Atom target, which additionally contains `atom_id`.

For CA-D-531's Subject-only variant, the report's `proposal` pins bind the exact UTF-8 frontmatter and body of the complete intended Carrier produced by CA-M-371: only declared Subject spans change, while old Version and Updated At remain. Compare the report's existing `frontmatter_digest` and `content_digest` to CA-D-425's corresponding intended-proposal pins. The separately bound `subject_intent_sha256` seals the fixed `N+1`/actual-effect-time materialization rule and exact predecessor history; illustrative preview metadata and future actual timestamps/hashes are not report proposal pins. O145 and O129 reopen the same current report, authority, lineage and intended-proposal evidence. Materializing the admitted Version/time rule at the actual effect does not silently replace that assessed Subject delta; any other proposal or intent change requires fresh assessment/preview/authorization. A value change still requires the admitted `semantic_revision` and preserved primary-Claim identity; this variant grants no assessment exception.

The request reference accepts no identifier alias, inline assessment, caller-supplied class, Status, authority pin or approval field. O145 returns normalized verified report observations; O129 returns the verified evidence with the actual lifecycle outcome. The shared Run result retains those Action facts under its existing Journal contract; this Delivery adds no Event schema or authorization grant.
