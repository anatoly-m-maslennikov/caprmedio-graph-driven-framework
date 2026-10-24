---
atom_id: CA-E-draft
content_role: Evaluation
type: Evaluation Approach
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
tier: 2
status: Draft
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-23 18:58:14 +0400"
subjects:
  governs: Subject/Engineering/Source Unit Responsibility
  depends_on:
    - Subject/Engineering/Source Check Adoption
relations:
  relates_to:
    - CA-E-539
    - CA-M-419
    - CA-M-411
---
# Summary

Evaluate source size, cohesion and package organization

## Scope

New or materially changed hand-authored PROGRAMMATIC source and its directly
owned tests and non-code assets. Do not implicitly migrate all legacy source,
vendor code, generated output or frozen fixtures into this Evaluation.

## Claim

Accept the applicable source-boundary result only when the measured source
passes the thresholds, measurement profile, cohesion review and organization
criteria below. A soft-limit crossing requires review and a written
justification. A hard-limit violation fails with no exception. Unknown or
unavailable measurements are unresolved; they must not be silently replaced by
another counting profile.

## Details

- Count every standalone function, method, async function, nested function and
  classmethod independently. Logical executable function LOC excludes
  comments, docstrings and blank lines. A function or classmethod has a soft
  limit of 25 lines and a hard limit of 40 lines. Exactly 25 and exactly 40
  are allowed. Crossing the soft limit requires a cohesion review and written
  justification; above 40 is FAIL with no exception. Never count a whole
  class as one function or use class size to excuse a method.
- Use an explicit pinned measurement profile retaining CA-E-539's logical
  function and physical module counting convention. A module has a soft limit
  of 200 physical lines and a hard limit of 300
  lines. Exactly 200 and exactly 300 are allowed. Crossing 200 requires
  review and written justification; above 300 is FAIL regardless of any
  accepted legacy exception. Comments and docstrings remain part of physical
  module LOC under that profile.
- Use this isolated boundary matrix for focused checks: function/method cases
  at 24, 25, 26, 39, 40 and 41 lines; module cases at 199, 200, 201, 299,
  300 and 301 lines; comment/docstring variants; standalone, method, async
  and nested forms; and a class over 40 lines whose individual methods remain
  small. The large class alone does not fail; a method over 40 does.
- Review whether each class and source unit has a cohesive responsibility.
  Extract a helper only when it expresses a meaningful reusable
  responsibility or boundary; do not add meaningless helpers, wrappers,
  indirection or line compression to bypass a threshold.
- When a module grows, prefer coherent packages or subfolders with visible
  ownership over a sprawling flat file set. Avoid meaningless nesting and use
  descriptive, sufficiently verbose filenames. Review responsibility and
  naming qualitatively; there is no arbitrary folder-count or file-count cap.
- Place JSON, YAML, TOML and other non-code source assets in the owning
  module's local `assets/` folder unless a platform genuinely requires another
  name or location. Keep governed Atom carriers, Journals and Runtime outputs
  under their own authorities.
- Apply the profile only to new or materially changed hand-authored source.
  Do not infer a full legacy, vendor, generated-output or frozen-fixture
  migration from this Evaluation. Preserve existing complexity, Ruff and
  ratchet requirements; this Evaluation adds size/cohesion evidence and does
  not weaken them.

These are Evaluation acceptance criteria, not a duplicate Method policy. The
measurement profile and result must identify the exact changed source and
return pass, fail or unresolved with the relevant evidence.

## Adoption notes

This is a Draft with the numeric draft schema and no stable Atom identity. It
is not current authority and does not change CA-E-539. On coordinated
promotion, this Evaluation may supersede the CA-E-539 oversize exception only
through the normal identity, predecessor and consumer-rebinding process. Until
then, CA-E-539, existing complexity checks, Ruff configuration and ratchets
remain untouched and authoritative.

Companion Draft: [cohesive source organization](../../05_method/draft/CA-M-draft-PROGRAMMATIC-CORE-ENG_POLICY--organize-cohesive-modules-packages-and-assets.md).
