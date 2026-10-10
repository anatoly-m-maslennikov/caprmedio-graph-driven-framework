# CAPRMEDIO

**The Graph-Driven Development Framework**

## Contents

- [The Goal](#the-goal)
- [What CAPRMEDIO is](#what-caprmedio-is)
- [Why CAPRMEDIO works this way (chains-of-thoughts)](#why-caprmedio-works-this-way-chains-of-thoughts)
- [Main framework architecture](#main-framework-architecture)
- [First usable cut](#first-usable-cut)
- [Current boundaries](#current-boundaries)
- [Status](#status)
- [Version History](#version-history)
- [Thanks](#thanks)

## The Goal

If it can be built, CAPRMEDIO should help anyone build it if they are willing to invest the time and effort.

In practice, it should make AI-assisted development reliable from the first idea to production without losing meaning, traceability, or learning.

Even a fully AI-generated project should be understandable, controllable and **not slop**.

## What CAPRMEDIO is

CAPRMEDIO stores project knowledge as small artifacts connected by typed links. Humans and AI use this graph to understand the project, make changes, check consistency, and generate useful views.

## Why CAPRMEDIO works this way (chains-of-thoughts)

Prompts/Skills, MCP, Apps and execution Tools form the harness →\
the project's meaning must not depend on them →\
an explicit ontology/base model defines the core: concepts, relations and constraints.

### Ontology (methodology)

The project is made of implemented decisions—yours and AI Agents' →\
But sessions are ephemeral →\
We need a **stable source of truth** →\
It's the specification.

Spec grows →\
we need smaller units →\
no single file structure is optimal for every use case →\
a graph with typed nodes and typed relations.

Each unit should be the smallest meaningful part of the spec →\
one scope + one Claim = one Atom →\
splitting further adds no useful distinction.

Nodes represent different things →\
Atoms state Claims; Entities are the things those Claims describe →\
Subjects link Atoms to Entities through `GOVERNS` and `DEPENDS_ON`.

Different tasks need different views →\
derive them from one authoritative source →\
**load only the context needed without duplicating authority.**

Natural-language phrases can be ambiguous →\
shared vocabulary + CAPRMEDIO Controlled English (CCE), a constrained way to write Claims →\
**explicit, checkable Claims.**

The spec is about different things →\
Requirements — required outcomes →\
Methods — how code should be written →\
Evaluations — QA rules and test-case specifications →\
Delivery — where and how to deliver results →\
together, RMED.

Describing an outcome does not prove it was achieved →\
Evaluations define checks →\
actual runs provide evidence.

We need more than spec →\
Concerns, Analysis and Plans for understanding and planning →\
Implementation for code, tests and configuration →\
Operations for repeatable actions and workflows.

Repeatable sequences of actions →\
Operations define Workflows, their steps and control flow.

Implementation, tests and views rely on Claims →\
record the exact source Claim identities and revisions →\
**trace results back to the specification.**

A typical iteration starts with a Concern →\
Analysis →\
Plan →\
RMED →\
Implementation →\
checked outcomes →\
next Concern.

Journals record changes and execution. Not every change needs every stage.

Using the same system for projects and methodology is simpler →\
both use Atoms, content roles and relations →\
the same Tools and Prompts can work with both →\
**the framework is built with the framework.**

The framework must describe itself →\
the [meta-model](.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL) uses Atoms to describe Atoms and other framework concepts →\
this creates recursion and needs a starting point →\
bootstrap seeds provided the first definitions; those seeds are now retired.

Different projects need different rules →\
Extensions and local configuration are also sets of Atoms →\
they add only Core-permitted capabilities and configuration, without replacing or weakening Core authority →\
**expand and configure the framework using the same system.**

### Harness (engine)

Ontology is big and complex →\
operating a project with the framework should be simple →\
harness, Tools and Prompts should show this complexity only when needed →\
ontology and engine are the "backend"; Skills and Prompts are the "frontend".

Skills vary a lot →\
different people prefer different Skills →\
the framework harness should support third-party Skills as a **replaceable frontend/interface**.

Repeated model reasoning costs time and tokens →\
every repeatable task that can be done deterministically should run programmatically →\
**Tools save time and tokens.**

Work that cannot be done deterministically →\
LLM reasoning →\
repeatable actions need reusable Prompts/Skills.

Workflows are defined in Operations →\
the harness implements and runs them using Tools and Prompts/Skills.

We cannot put everything into one prompt →\
the built-in entry Skill, [ca](102_FRAMEWORK_ENGINE/202_AGENTIC/205_SKILLS/ca/SKILL.md), connects agents to MCP →\
Tools retrieve the needed context and assemble Prompts/Skills →\
MCP delivers them and exposes Tool and Workflow execution.

Wide-context reasoning →\
main session.

Narrow, repeatable work →\
bounded execution contexts and structured results.

Long actions should not block sessions →\
Workflow Orchestrator coordinates the steps in the background →\
durable state, reconnectable runs, approvals and recovery.

Files in folders are clear and inspectable →\
they currently hold authority →\
rescanning can become expensive →\
a derived graph database index supports queries and views. Database authority could be a future migration.

## Main framework architecture

### Node types

- **Scope Unit:** one area of project responsibility, declared in the project structure.
- **Atom:** one Claim in one scope, with a content role. Atoms belong to Scope Units; project-wide goals are the exception.
- **Journal:** records of changes, execution and observed outcomes.
- **Projection:** a derived, non-authoritative view of existing sources.

### Content roles

- **C — Concern:** problems, bugs, questions and opportunities.
- **A — Analysis:** analysis reports and rationale.
- **P — Plan:** backlog, tasks, epics and version plans.
- **R — Requirement:** specification of required outcomes.
- **M — Method:** how code should be written.
- **E — Evaluation:** quality assurance policies and test-case specifications.
- **D — Delivery:** target environments, CI/CD and release policies.
- **I — Implementation:** code, tests, configuration and CI/CD pipelines implementing all RMED.
- **O — Operations:** actions and workflows with steps to operate the project.

Each Atom content role has **Types**. Each Type has its own structure, properties, authoring rules and checks. For example, O has Action, Step, Workflow and Actor.

Content roles describe purpose. Atom, Journal and Projection describe form.

- **MECE:** cover the defined scope without overlap.
- **DRY:** keep one source of meaning, not independent copies.

**One coherent source of truth:** Atoms record Claims; actual Implementation shows what is built.

### Scope units

A Scope Unit groups Atoms for one part of the project, such as an app, feature or tool. Inside it, Atoms are organized by content role: Concerns, Plans, Requirements, Methods, and so on.

[project_structure.toml](.caprmedio_caprmedio/project_structure.toml) defines Scope Units, their parents and their authority/Delivery paths. Folders follow this file.

**Scope Unit levels** show nesting depth. The Project is level `0`. Each child is one level deeper: `1`, `2`, `3`, and so on.

**Scope Units can be ordered or unordered:**

- **Ordered:** has a `local_order` among ordered Scope Units with the same parent.
- **Unordered:** has no `local_order`. The Project itself is Unordered.

Order does not create dependencies. State dependencies separately. Folder numbers are for navigation; they do not set `local_order`.

### Fractal structure

Scope Units can fold one inside another. P Atoms can split into smaller P Atoms: epics, sub-epics, tasks and subtasks.

**As many layers as needed. The same framework rules at every layer.** The structure must not contain cycles.

### Atom tiers

**Local tiers** show an Atom's authority inside its Scope Unit:

- **Principle:** project principles.
- **Core:** basic definitions and boundaries.
- **General:** reusable rules.
- **Standard:** work and implementation details.

From higher to lower authority:

- Project: Principle, Core, Standard.
- Other Scope Units: Core, General, Standard.

**Global tiers** give Atoms one authority number across the project. The number comes from the scope and Local Tier. Within the scope where a Claim applies, a lower number means higher authority.

Project goals have Global Tier `-1` and no Local Tier. **Tiers are not work priority or folder depth.**

Agents act within delegated authority →\
they can analyze conflicts and propose resolutions →\
only the Operator can resolve conflicts between active Project Principles.

### Ownership and claim scope

- **Internal:** the project defines the meaning.
- **External:** an outside source defines or imposes the meaning. The project records the source and how it applies.
- **Relational:** a Claim targets another Scope Unit, or the Atom is not inside a Scope Unit.

Internal/external say **who defines the meaning**. Relational says **where the Claim applies**.

### Relations

**Direct relations** link artifacts. Examples:

- `child_of`: a parent Requirement.
- `method_for`, `evaluation_for`, `delivery_for`: RMED support for a Requirement.
- `derived_from`: the sources used.

**Subjects** link Atoms to Entities:

- `GOVERNS`: what the Claim governs.
- `DEPENDS_ON`: what the Claim needs but does not govern.

Subjects are links, not nodes.

Scope Units + typed relations + Subjects →\
**fetch the right part of the spec or other CAPRMEDIO content mechanically, or almost mechanically.**

### Main projections

There can be a lot of Atoms →\
they can be compiled into one Projection →\
**it is still a derived artifact, not a source of truth** →\
for example: one prompt for how to write code, built from all M Atoms that apply to the Scope Unit.

- **Atom Subjects Graph:** Atoms linked to Entities through `GOVERNS` and `DEPENDS_ON`.
- **Entities Graph:** Entities linked to other Entities through allowed relations.
- **Terms Graph:** terms and their allowed typed relations.
- **Project Scope Unit Graph and Sources view:** Scope Units, their parents and authority/Delivery paths.
- **Applicable Methodology:** the rules that apply to the selected scope.
- **Requirement Lineage Map:** Requirements traced back to their Principles.

**Different views, one source.** Rebuild Projections from their sources.

Each Project has a `.caprmedio_<project_name>/` folder. Store persistent Journals in `_journal/` and general Projections in `_projection/`. Project-declared Methodology source remains authoritative; the package/root `methodology/` export and Applicable Methodology delivery output below `000_CAPRMEDIO_framework/` are derived deliveries that preserve provenance. They, graph views, and derived Journal views are non-authoritative Projections: none replaces source or grants Action authority.

With an explicit Project root, Journal writes and queries use that Project's settings and Journal, not those of a parent or sibling Project. Ambiguous control folders and symlinked settings are rejected.

### Extension and configuration

**The framework is expandable and configurable.** You can add Types, Workflows, Tools and authoring rules. Put reusable additions in Extensions. Settings choose what to use and with which parameters. Framework rules still apply.

## First usable cut

The implementation contains a deliberately small, source-bound first cut with
six route definitions: Create Atom, Update Atom, Replace Atom, Change Status
Atom, Implementation Workflow, and Build Applicable Methodology. Discovery and
execution admission are available only when the selected-route manifest reopens
with current source pins. An admitted Run preserves its identity,
source/currentness checks, authorized permissions, terminal outcome, and
shared-Journal evidence. Status reports matching canonical Workflow terminal
evidence rather than a scheduler or child-Action outcome.

The MCP remains available over local stdio. The Docker `project-mcp` command
documented below is a development source launcher: it requires an explicit
Framework source root and can build a compatible image. It is distinct from
activation of a selected installed package. Neither transport starts work or
grants authorization by itself; see the [development and installed activation
routes](102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/203_APPS/WORKFLOW_ORCHESTRATOR/docker/README.md#launch-a-selected-project-mcp-endpoint).

A reusable Framework package is selected from
`.caprmedio_install/releases/<package-manifest-sha256>` by
`.caprmedio_install/current.toml`; Project-owned runtime state remains in
`.caprmedio_runtime/`. Installation creates `.caprmedio_runtime/config.toml` from the
package-admitted default only when it is absent, and otherwise preserves its
existing bytes or refuses a configuration migration. The legacy Tool-version
replacement erases only its managed `.caprmedio_runtime/tools` surface, never
Project controls, Journal, or other runtime state.

The native full-package installation path uses
`.caprmedio_runtime/installation/current.toml` for Project execution, after
publishing the matching `.caprmedio_install/current.toml` package selection.
Replacement requires the exact sealed package, complete release evidence and
verified quiescence of the selected predecessor. It stages the replacement
before removing only the old selected package; existing configuration and
Project-owned history remain outside that deletion boundary. An unavailable
process query is not proof of quiescence and stops replacement before removal.
The legacy Framework selector is only a pre-transition binding, not a second
native execution authority.

Under the installation lock, the runtime command stage writes only
`command.toml`, `environment.toml`, `wrapper`, and `stage-manifest.toml`; their
reopened final copies live below
`.caprmedio_runtime/installation/generations/<positive-N>/`. Those carriers
bind the selected package's locked `uv run --locked --no-sync --no-env-file`
command and deterministic environment, but are prospective data only. Actual
invocation additionally requires an installation-specific Operator command
binding the exact command digest and target context.

A package carries its active Methodology export, non-authoritative
`methodology/bindings/` projections, and `SKILLS/ca` payload. Only exact
admitted, selected Methodology active/support rows participate; presence does
not activate an Extension or Configuration. Publication follows the gated
installation/promotion path: Methodology output is limited to its declared
delivery root and never overwrites authoritative source, and Skill publication
is not automatic host registration. A package-owned CLI is implementation
capability, not an installation or Workflow-start authority.

This cut has golden mock-Agent evidence for the Implementation Workflow (W09),
not a live-LLM claim. It is not a formal Release or promotion, does not claim
full sixteen-route coverage, and leaves Scope mutations, Revert, graph builders,
and standalone advanced Artifact/Journal queries deferred. This README makes
no claim that a Project has passed native installation, Full Gate, package
selection, release promotion, public gate, or publication. `RELEASE_VERSION`
and `PUBLIC_RELEASE` code provides implementation and test capability, not a
completed public-release receipt.

## Current boundaries

- More than one person can use CAPRMEDIO on a project, but the framework does not yet provide native support for team workflows.
- CAPRMEDIO is not only local-first; it is currently local-only.

## Status

The current framework version is declared in [version.toml](version.toml). The framework foundation is under active development; this is not yet a complete production toolchain.

License: [Apache 2.0](LICENSE).

## Version History

See [Version History](VERSION_HISTORY.md) for project origins and version milestones.

## Thanks

- **[Andrej Karpathy](https://en.wikipedia.org/wiki/Andrej_Karpathy)**, for his fresh ideas—especially about graphs. His [LLM Wiki](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) says it vividly: “Obsidian is the IDE; the LLM is the programmer; the wiki is the codebase.” His [Software 3.0 talk](https://www.youtube.com/watch?v=XdbpCM4yGyE) develops the graph perspective further.
- **[Daniel Kravtsov](https://improvado.io/blog-authors/daniel-kravtsov)**, CEO and co-founder of [Improvado](https://improvado.io/company/about), for giving me the challenge of building a knowledge graph for my team. It showed me what graphs can achieve in practice. At Improvado, I also tried for the first time to build an internal product both with AI and by AI.
- **[Anatoly Levenchuk](https://t.me/ailev_blog)**, creator of the [First Principles Framework](https://github.com/ailev/FPF). I could never have built this project without FPF. I also maintain an [LLM-friendly FPF knowledge-graph toolkit](https://github.com/anatoly-m-maslennikov/levenchuk-fpf-knowledge-graph-toolkit).
