---
atom_id: CA-P-1968@12
content_role: Plan
type: Plan
label: Epic
work_sequence_number: 10
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
author: Anatoly Maslennikov
status: Archived
subjects:
  governs: Subject
  depends_on:
  - Subject/Domain/Node/Continuant/Atom
  - Subject/Domain/Node/Continuant/Term
  - Subject/Domain/Node/Continuant/Term//Property
  - Subject/Engineering/Carrier
  - Subject/Domain/Node/Continuant/Scope Unit
  - Subject/Domain/Node/Continuant/Projection
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Plan'
  - 'Subject/Domain/Node/Continuant/Actor/Type: Operator'
version: 12
updated_at: 2026-10-25 01:20:04 +0400
relations:
  is_decomposition_of:
  - CA-P-1959
  depends_on:
  - CA-P-1966
  - CA-P-2045
  blocks:
  - CA-P-1969
tier: 3
---
# Summary

Apply approved Subject migration batches

## Objective

Organize and verify approved Candidate #7 methodology source increments before ordinary content updates, preserving predecessor history and truthful applied effects.

## Details

### Latest Epic boundary — 2026-10-25

Finish Methodology first in CA-P-1959 and its retained work. All Engine RMED
migration belongs to the separate Backlog Epic CA-P-2637, including PROGRAMMATIC,
APPS, TOOLS and other Engine descendants. Do not execute that migration here.
The later Engine Epic starts with Subject-system and Scope Unit review.

No code/runtime implementation is included in either migration. Preserve
Engine work already applied or proposed; do not undo it or promote more Engine
proposals ahead of the Methodology gate. Earlier combined-pass wording and
all-pass completion gates below are superseded by this boundary.

Methodology keeps the approved order: Subjects → missing Atoms → archive
obsolete Atoms → properties → Content. General Content work stays under
CA-P-1970. Terms, instance naming, conflict-workflow updates and protected
owners retain their explicit deferrals.


### Latest Operator order — 2026-10-25

Run these stages in order:

1. Migrate Subjects.
2. Add missing Atoms.
3. Archive obsolete Atoms.
4. Fix properties.
5. Update Atom content last, under CA-P-1970.

Complete the Methodology pass first. Then repeat the sequence for PROGRAMMATIC
RMED Atoms only. No PROGRAMMATIC code or runtime implementation is authorized.
Do not interleave new PROGRAMMATIC corrections ahead of Methodology's pass.
Preserve work already applied or staged; this order is not a rollback.

Create new proposed revisions as Drafts and refine them in iterations. Keep
Current originals unchanged until a proposal is ready and applied. Preserve
existing Drafts, Archives, protected owners and explicit deferrals. Stage a
concrete uncertain proposal without claiming it is approved; ask the Operator
only where refinement still requires a real decision.

Stage 1 changes Subjects, not ordinary Content, properties or lifecycle state.
Later-stage gaps may be inventoried now, but are not permission to execute them
early. Normal maintenance of these execution Plans records the new order; it
does not count as migration of a model Atom's Content.

Mapping, application and verification are per-pass milestones. Methodology
completion opens Methodology content work; it must not wait on the later
PROGRAMMATIC pass. Verify each pass separately before its content stage.
Keep CA-P-1959 Active while its retained work remains unproved. Earlier mixed
increment schedules and global all-pass wording below are historical where
they conflict with this order.


### Latest Operator decisions — 2026-10-24

Use candidate-7.current-prmedo-subject-worklist.json and its reading note,
then re-read the actual source before accepting or applying a row. The older
remaining-subject-worklist excludes Plans and is historical, not the current
ownership frontier. Current worklist groups route review; they do not impose
a fixed worker count or admit a target. Bounded parallel workers are now
authorized, with root integrating source and shared planning changes.

Terms and instance naming in Subjects are explicitly deferred. This
supersedes the earlier Summary-based Operation-name approval. Preserve
existing names and whole-owner holds, keep limitations visible, and do not
make either deferred activity a completion gate or invent a naming solution.

If confidence is below95%, check Candidate #7, the application plan, this
chat's last two days of human input and active principles. Latest human
words win. If still uncertain, ask the Operator one question at a time;
do not use the superseded best-choice/90% policy as permission to guess.

Summary or Content Role changes create a new Atom identity. Type, other
properties or content changes alone retain the base ID when Summary and
Content Role stay unchanged, with the usual Version/time/history update.
This is the current general rule, not a migration-only Type exception.
Ordinary content migration remains separate; approved defining-rule and
execution-Plan alignment does not authorize general content rewrites.

Candidate #7 application includes Current P/R/M/E/D/O sources and Governing Configurations. P is explicitly re-added; existing C/A, Drafts and Archives stay excluded, except new predecessor archives for Current updates and new bounded C/Questions. No PROGRAMMATIC implementation. The methodology changes are: Subjects, defining Requirements/Deliveries, property rules, Type classifications and identity/ID rules. Re-read live source files before any effect and record actual current paths, old/new IDs, Versions, Statuses, timestamps, predecessor archives and changed fields. A Type correction alone retains the ID; Summary or Content Role changes create a successor identity. Preserve unrelated body content and ordinary content migration under CA-P-1970.

Mapping research remains separate from source application. Use the fresh worklist and the integrated ledger from CA-P-2043/CA-P-2045; do not resurrect the old Candidate #3/#4 packet, fixed counts, CA-P-2188–CA-P-2193, the CA-P-2167 Tool gate or the CA-P-1909–CA-P-1912 sealed pipeline as current prerequisites. CA-P-1973 was canceled; its predecessor and cancellation path are history, not a current child-completion requirement.

Each applied update must preserve its Summary and Content Role unless a separately defined R/D source change requires a new identity; archive the predecessor with qualified ID@oldVersion and Archived Status, leaving archived numeric Version, Updated At and unrelated content unchanged. Stop on a failed effect and leave completed effects plus untouched remainder visible. Below 95% confidence, recheck Candidate #7, the Epic, the latest two days of exact human input and principles. If still uncertain after those checks, ask the Operator one question at a time; preserve existing explicit deferrals. Do not invent a Domain entity/property. No automatic replay or rollback.

Maintain a separate Current P mapping and metadata ledger. Apply supported Subject, Type, ID, required-property and numeric Tier corrections to Current Plans, including the implicit Project root. Preserve existing lifecycle statuses and unrelated content. Report legacy carriers and containment mismatches explicitly; do not infer a new parent from folder nesting alone. Existing Draft-ID/lineage migration is excluded and must not block this pass.

No code, implementation schemas, MCP, tests, Settings values, runtime activation, Journal fabrication, release or deployment is included. This Plan does not claim a complete Subject migration or a rebuilt graph.

### Definition of Done

Not Done if an effect lacks a current approved mapping and source readback, a predecessor archive is malformed, an identity change violates the Summary-or-Content-Role rule, ordinary content changes, a canceled child is treated as required, or actual effects are confused with a plan, scratch record or runtime receipt.
