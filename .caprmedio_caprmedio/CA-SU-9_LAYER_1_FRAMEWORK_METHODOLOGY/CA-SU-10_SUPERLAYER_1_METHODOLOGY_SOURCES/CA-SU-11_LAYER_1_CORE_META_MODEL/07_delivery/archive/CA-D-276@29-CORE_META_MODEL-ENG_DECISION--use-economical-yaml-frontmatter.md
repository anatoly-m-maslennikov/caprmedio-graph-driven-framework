---
subjects:
  governs: Subject/Graph Node/Engineering/Continuant/Carrier/File Carrier.YAML Frontmatter
  depends_on:
  - Subject/Graph Node/Domain/Continuant/Atom.Author
  - 'Subject/Graph Node/Domain/Continuant/Actor/Type: Operator'
  - Subject/Graph Node/Domain/Continuant/Scope Unit
  - Subject/Graph Node/Domain/Continuant/Actor
version: 29
updated_at: 2026-10-25 17:32:27 +0400
relations: {}
atom_id: CA-D-276@29
content_role: Delivery
type: Eng Decision
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 3
---
# Summary

Use Economical YAML Frontmatter

## Scope

YAML Frontmatter of Markdown Atom Carriers.

## Claim

the YAML Frontmatter of a Markdown Atom Carrier **must** use the least syntax **and** nesting that preserves unambiguous deterministic parsing, validation, extensibility, **and** human readability.

## Details

### Common field encoding

use the following field encodings for the applicable Atom Properties. presence follows the cited Property authority, **not** observed filename tokens. a String is a nonempty YAML string; an Integer excludes Booleans. a null value does **not** satisfy a required Property.

| Property | Top-level field | Encoding **and** applicable presence |
|---|---|---|
| Atom Identity | `atom_id` | String under CA-D-446; exactly one for every Current, Draft, **or** Archived Atom; Draft marker forms follow CA-D-378; carry Version separately |
| Content Role | `content_role` | **=1** String selecting its canonical Content Role; resolve the admitted domain from applicable authority |
| Type | `type` | **=1** String selecting the Atom's admitted Type under its applicable Type authority; a present field **must not** be null, empty, **or** a collection; filename Type tokens are **not** a second value |
| Local Scope Unit | `current_scope_unit` | **=1** String naming the registered Local Scope Unit that owns an ordinary Atom. For Type Project Goal only, carry its Operator Actor owner through the existing Author fallback under CA-D-482; do not register that Actor as a Scope Unit or infer the value from filename |
| Target Scope Unit | `claim_target_scope_unit` | use CA-D-482 |
| Numeric Tier | `tier` | exactly one integer for every Current Atom under CA-R-2102; ordinary Project Atoms use **>=0** under CA-R-2130, non-Project Atoms use **>=1** under CA-R-2131, and a verified Project Goal carries exactly `-1` under CA-R-2132 |
| Version **and** Updated At | `version`, `updated_at` | use CA-D-270 |
| Author | `author` | use CA-D-274 |
| Status | `status` | use CA-D-483 |
| Label | `label` | **<=1** nonempty String for an explicit Label value; when absent, the effective Label is derived from the Atom Type name under CA-R-1594, without requiring a stored copy of that fallback |
| Summary | no frontmatter copy | exactly one body Property under CA-D-479; its effective value is the nonempty Summary content |
| Substance | no frontmatter copy | exactly one body Property for ordinary Atoms under CA-D-479; formal Graph Rule Atoms use CA-D-637 instead |
| Subjects | `subjects` | use CA-D-269; **only** the governed Subject keys **and** their admitted encodings |
| authored Atom Relations | `relations` | use CA-D-268; omission **or** an empty mapping represents no authored Relations; **every** present Relation Kind carries its nonempty target collection |

- `current_scope_unit` **must not** be null, a list, a joined set of names, **or** replaced by an `operators` field. it names the owning Local Scope Unit, except that Type Project Goal carries its Operator Actor owner under CA-D-482. This exception does not apply to ordinary Goals. Never infer the value from its filename.
- the Atom ID and Version identify a Current or Archived Atom version under CA-D-446; do **not** duplicate them **in** an `identifier` field. Current, Draft, **and** Archived Atoms carry exactly one Atom ID; a Draft may remain incomplete in other required Properties until promotion. Draft marker forms follow CA-D-378.
- Every Current Atom satisfies the required and optional base Property cardinalities in CA-R-2102. A Draft may be incomplete, but retains its mandatory Atom ID and reports missing required Properties; it must satisfy the full Current contract before promotion. Formal Graph Rule content follows CA-D-637 and its Substance exception.
- Summary **and** Claim use their body sections under CA-D-479, **not** `summary` **or** `claim` frontmatter copies. other body Properties use their own registered section authority.

### Conditional fields and expansion

- a Plan's explicit `assignee` uses **<=1** String identifying an admitted Actor under CA-D-473. `autonomous_confidence_threshold` **and** `implementation_retry_limit` use their integer encodings under CA-D-472 **and** CA-D-447. inherited values remain omitted unless explicitly selected; self-sufficiency does **not** copy them.
- `priority` follows CA-R-386 for Concern Atoms **only**. additional Plan, Operations, proof, **or** other Type-specific fields require their applicable Delivery declarations; their occurrence **in** old Carriers does **not** admit them.
- the generated `projection` block is admitted **only** **in** a projected representation under CA-D-305, with **only** its defined `source_carrier_path` String. it is **not** an authored source Atom Property.
- a new field **or** nested key requires applicable authority that settles its canonical location, value type, cardinality, admission condition, **and** permitted values **or** reference resolution. unadmitted fields are invalid; an admitted Property with an unsettled encoding is a schema gap, **not** permission **to** guess **or** report full conformance.
- apply explicitly governed migration exceptions **only** within their declared boundary. legacy presence alone is **not** an exception; retired fields under CA-D-478 remain rejected.

### Subjects-only edit-draft exception

CA-D-446's explicit source-pinned Subjects-only edit draft is a derived proposed next Revision of an existing Atom, not a new Atom Draft or another canonical original. It may carry `atom_id: <canonical-ID>@<proposed-version>-draft` (preferred) or the compatible `atom_id: <canonical-ID>@draft`, `status: Draft`, and a matching Draft-marker filename in the owning role's `draft/` folder while the exact canonical source remains untouched. The reviewed packet retains the canonical target/source pin and exact draft path/digest for that specific proposed edit. Approval restores the canonical ID and original Status, independently validates normalized Subjects-only materialization, and uses the existing exact predecessor archive plus N+1/actual-time update. Staging and publication require no retained Draft-history entry, `revision_lineage`, unique Draft head, origin chain or consuming successor. New-Atom Drafts and ordinary lifecycle Drafts carry exactly one Atom ID; marker and filename rules remain governed by CA-D-378 and CA-D-650. Canonical ID grammar and the normal source, schema, identity/collision, permission and exact actual-history safeguards are unchanged.
