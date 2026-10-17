---
atom_id: CA-P-2401
content_role: Plan
type: Plan
label: Epic
work_sequence_number: 5
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
local_tier: Standard
global_tier: 8
author: Anatoly Maslennikov
status: Active
subjects:
  governs: Tool
  depends_on: [Atom, Scope Unit, Property, Relation, Artifact/Carrier, Project Structure, Tool, Workflow]
relations: {}
version: 2
updated_at: "2026-10-18 01:26:07 +0400"
---
# Summary

Make Atom and Scope Unit Actions Good

## Objective

Make the PROGRAMMATIC Atom and Scope Unit actions complete, coherent and usable through the existing connectors, Workflows and MCP. This Epic records the Operator's decisions from this session; it is not evidence that the implementation already provides them.

## Details

### Agreed PROGRAMMATIC structure

The target structure is:

```text
PROGRAMMATIC
├── TOOLS
│   ├── CONNECTORS
│   └── CAPRMEDIO_TOOLS
├── PROJECT_TOOLS
└── APPS
    ├── WORKFLOW_ORCHESTRATOR
    └── MCP
```

All shown Scope Units are unordered; individual Tool Scope Units belong under the appropriate Tool group.

- TOOLS contains reusable capabilities delivered with the framework, rather than maintenance specific to this repository.
- CONNECTORS contains logical storage access and file/folder mechanics. Backend-specific implementations are adapters within CONNECTORS, not another peer feature group. Connectors do not choose Atom identity, lifecycle or Workflow sequencing.
- CAPRMEDIO_TOOLS contains reusable CAPRMEDIO domain actions, including the Atom and Scope Unit actions in this Epic, usable in any CAPRMEDIO-managed project.
- PROJECT_TOOLS contains only the build, test, release and maintenance operations specific to developing the caprmedio framework repository itself. It is a sibling of TOOLS, not a child of CAPRMEDIO_TOOLS.
- APPS contains WORKFLOW_ORCHESTRATOR and MCP as peers. The orchestrator owns Workflow execution and coordination using Tools. MCP owns discovery and transport for Tools and Workflows; it does not own orchestration or duplicate domain behavior. Preserve other existing Apps; this tree highlights the agreed boundary.

The implementation tasks must reconcile existing TOOLS, CONNECTOR_TOOLS, TOOL_WORKFLOWS, PROJECT_TOOLS, APPS and MCP declarations and contents with this target, reusing capabilities rather than creating duplicate owners. Align applicable RMEDO, project_structure.toml and both governing/delivery bindings during that migration. This Epic update records the target only; it does not itself rename or move folders, change scope declarations, or implement Tools.

### Atom actions

- Find Atoms using filters on any supported Atom property, including nested properties and relations; do not restrict Find to Subjects or a fixed small property whitelist. Validate typed filters and report invalid sources or incomplete coverage rather than silently ignoring them.
- Create any Content Role and applicable Type directly in any status admitted by that Role/Type model, filling and validating all mandatory fields. Do not require intermediate statuses, complete Journal history or retained Draft lineage.
- Update by publishing the next revision file and archiving the exact predecessor. Preserve same identity where current change-classification rules allow it; identity-changing replacement remains distinct. An actual edit advances revision metadata; a no-op does not create a revision or archive.
- Promote ID-free Drafts to Active with a fresh unused identity; no restoration of a previous ID or history/Journal admission gate.
- Cover ordinary file Atoms and folder-backed Plan and Operations containers, including Plan/Epic, Workflow and Step. Preserve exact prior bundles and current container semantics; compose explicitly selected per-Atom operations for bulk work rather than promising a cross-Atom transaction.

### Scope Unit actions

Create, rename, move and delete Scope Units coherently across authoritative project_structure.toml and both declared governing and delivery folder bindings. Preserve references and admitted relative/path semantics, distinguish declaration from intentional non-materialization, and never infer that root delivery and governing places are identical.

Delete must refuse a Scope Unit containing any Atoms or child Scope Units. It must also refuse when either affected folder contains code, other non-Atom files or any other content that would need deletion or preservation. No recursive deletion or removal of a declaration while abandoning nonempty delivery content is authorized. This is the Operator's explicit resolution of the deletion question.

### Validation and reconciliation

Validate YAML syntax, applicable Role/Type keys, mandatory properties and typed values; exact Markdown heading set and order; and coherence among carried properties, filename and actual placement. Validate Project Structure declarations and actual governing/delivery places together, recognizing declared unmaterialized places separately from drift.

Validate registered relation/placement invariants. For example, the current task membership of an Epic's folder must equal its declared direct decomposition membership, applying reserved status-directory and current-revision rules. Use the registered direct relation and derive inverses; do not add a second independent child list, infer Workflow control flow from containment, or count archived predecessor files as extra current members.

Separate mismatch detection from repair. Support three explicitly selected reconciliation policies: files/folders canonical (repair properties and applicable relations), properties canonical (repair filenames and folder placement), or manual (report differences and make no repair). Canonical means the selected repair direction for this mismatch, not permission to bypass validation, invent identity/semantics, overwrite collisions or discard content. Ambiguous or unsafe repairs remain visible without effects.

### Shared design

Reuse the current coherent connector interface and existing storage owners. Keep domain rules in one owner and file/folder mechanics in adapters. Provide one logical property-update entry point whose mapping resolves whether a property is carried in YAML or in its named Markdown section; do not duplicate values or bypass lifecycle/revision rules.

Represent extensible Content Role and Type schemas in external JSON rather than hard-coded property/heading rules. JSON carries the applicable governed schema representation and is easy to modify and extend; it must not silently become an independent conflicting source of business authority. Cover property location, mandatory/allowed keys, values and body layout.

### Delivery plan and execution rules

Align affected project-local, methodology-source and PROGRAMMATIC/connector/Workflow RMEDO before implementing newly decided behavior. Reuse existing capabilities and keep changes bounded; do not reopen settled fresh-ID, optional-history or deletion decisions.

Decompose into separate Task files under this Epic's matching directory, each with an estimated own-work budget of at most 15 minutes and an observable acceptance condition. Split any larger task before execution. After completing each task, review and update dependent next tasks before starting them. Record actual results; a plan or local fixture pass is not implementation or release acceptance.

Use functional/integration/golden-corpus checks as the primary proof, with only narrowly useful unit tests. Test data must be independent from mutable live project Atoms. Include valid Role/Type/status cases, negative validation, predecessor preservation, no-op, P/O containers, arbitrary property filters, relation/folder mismatches, all three repair policies and nonempty deletion refusal.

Creation of this Epic and its task records does not start implementation, a full suite, deployment or a release.

### Definition of Done

False if any scoped Atom or Scope Unit operation, validation invariant or reconciliation policy lacks aligned current contracts and implemented, independently checked functional evidence; or if container/ordinary Atom behavior diverges, predecessor content is lost, empty-only deletion is violated, or required relation/filename/folder/property coherence remains unreported; or the agreed framework/project Tool separation and App hierarchy are not reflected coherently in governing declarations and delivery carriers.
