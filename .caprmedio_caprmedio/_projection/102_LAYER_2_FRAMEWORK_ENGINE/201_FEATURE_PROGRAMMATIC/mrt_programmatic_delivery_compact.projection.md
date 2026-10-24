---
updated_at: "2026-10-22T16:35:33Z"
---
# PROGRAMMATIC Delivery — Implementation Prompt

## Role and use

Prepare the assigned PROGRAMMATIC implementation's delivery carriers using applicable current R/M/E/D/O. This is a compact, non-authoritative view of explicitly Active root Delivery atoms, not a delivery receipt, specification replacement or permission to release.

Use together with [Methods](mrt_programmatic_methods_compact.projection.md) and [Evaluation](mrt_programmatic_evaluation_compact.projection.md) during preparation, not only after implementation. M guides construction, E establishes applicable quality checks, and D binds encoding, placement and package boundaries. Load applicable Project Principles, Methodology, task Requirements/Operations and child-scope rules separately. This root selection does not flatten descendant rules or make every conditional case mandatory for every task.

For a formal CA-O-016 invocation, follow the [Implementation Workflow input contract](../../../../102_FRAMEWORK_ENGINE/202_AGENTIC/202_PROMPTS/ACTION_PROMPTS/IMPLEMENTATION_WORKFLOW/README.md): the verified full-content active-M file and separately bound R/D/E sources remain required. These compact views are supplemental guidance, not substitutes for that file or the source contents/digests, and are not automatically injected into runtime packets.

## Delivery playbook

### Carrier placement — D251

PROGRAMMATIC's declared authority place is `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/`; its delivery place is `102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/`. Keep governed atoms separate from delivered implementation. Resolve component-specific delivery places and formats from their own applicable carriers; do not infer a new mapping from a physical folder name.

### Technical carriers — D250

Source, installable runtime carriers, admitted dependency records and non-Python exception records use the locations and encoding declared in root `pyproject.toml`, table `tool.caprmedio.framework_engine_software`. Corresponding acceptance evidence uses its declared Evaluation location.

D250 owns the configuration and integration-contract carriers; M415/M412 own the technology selections materialized there. Read the actual contract before packaging; this view neither supplies missing configuration values nor proves installability or platform support.

D250 is explicitly Active but has no explicit local/global tier or claim-target field. Its filename's `CORE` token is not tier authority; no classification or metadata repair is performed here.

### Reproducible fixture/package boundary — D638

- Deliver one inspectable manifest with the existing bundle/package metadata in its declared delivery place. Reuse its admitted format when sufficient; do not create a second independent inventory for the same boundary.
- Bind bundle/schema revision, entrypoint and invocation context, selected interpreter/dependency environment, and required member/support/configuration/schema inputs. Carried inputs have paths and content digests; identified Atom inputs also retain actual Atom IDs and Versions.
- Carry required bytes or declare them explicitly external. Declare external services and environment prerequisites as external, not bundled bytes. Successful use must not depend on undeclared ambient files/imports, mutable Project Atoms or the author's workspace.
- Resolve carried paths relative to the bundle/package boundary. Keep external references distinct.
- For fixture/replay bundles, bind selected governing definitions and consistent manifests, fixture inputs, expected outputs or expected failures, and any separately identified live-current compatibility purpose. Include the exercised lazy-read support closure, not the entire live graph.
- Preserve intentionally invalid target bytes and their expected outcomes. New current authority does not silently rewrite a frozen oracle; an intentional fixture-contract change delivers a consistent bundle revision.
- Keep canonical reusable fixtures/package sources separate from live corpus and non-authoritative runtime copies. Disposable materializations/remnants use configured Project Temporary State; reusable sources and retained evidence are not automatically disposable.
- Preserve file/path safety and source-preservation rules. A manifest is not authoring authority, mutation permission, successful execution, complete Journal coverage or a new release-admission registry.

### Shared MCP runtime binding — D640

- Encode the shared host configuration at the default `XDG_CONFIG_HOME/caprmedio/runtime.toml`, falling back to `~/.config/caprmedio/runtime.toml`; this is host runtime configuration, not a Project Settings source.
- Preserve the exact contract fields:

  ```toml
  schema_version = 1

  [shared_mcp]
  projects_root = "/Users/am/Documents/My_Repos"
  http_port = 8092
  max_loaded_projects = 2
  ```

- `max_loaded_projects` is optional and defaults to 2 warm/active contexts; it
  does not cap discoverable or explicitly selectable Projects. The image listens
  on port 8092; the host-published HTTP port is configurable and must not be
  hard-coded to a historical host value. Host configuration changes require
  restart, and no Project-root remapping is live.
- Carry one Docker container and one external HTTP MCP endpoint, with the
  shared gateway/catalog/pool/server implementation delivered under
  `102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS` and
  `102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/204_MCP`; retain the legacy one-Project
  launcher as a separate explicit mode. This source packet records delivery
  shape only; it is not deployment or active-runtime evidence.

## Before handoff

Resolve the applicable delivery mapping, technical contract, package/fixture entrypoint, environment, carried/external dependencies, expected results and actual evidence location. Use the selected Evaluation checks to establish the delivered result. Report incomplete or uncertain delivery truthfully; do not infer success from a written manifest, projection, source revision or local commit.

## Sources, scope and freshness

Selection: direct root `07_delivery/*.md` with explicit `status: Active`, `content_role: Delivery` and `current_scope_unit: PROGRAMMATIC`. Snapshot: **4 Deliveries — 0 explicit Core, 0 General, 3 Standard, 1 unclassified**. Excluded: 1 root legacy carrier without explicit Active metadata (D437), all archive/archived/Draft carriers and descendant Deliveries. Exclusion is not retirement; referenced external authority still needs resolution when applicable.

Refresh from the originals when relevant content or selection changes. `updated_at` marks this rebuild, not proof of currentness. No source atom, status, tier, implementation, runtime or release is changed by this view.

| Tier from metadata | Source revision | Summary |
|---|---|---|
| Unclassified | [CA-D-250@12](../../../102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/07_delivery/CA-D-250-PROGRAMMATIC-CORE-DELIVERY--provide-programmatic-software-carriers.md) | Provide PROGRAMMATIC software carriers |
| Standard | [CA-D-251@7](../../../102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/07_delivery/CA-D-251-PROGRAMMATIC-DELIVERY--bind-programmatic-delivery-place.md) | Bind PROGRAMMATIC Delivery place |
| Standard | [CA-D-638@2](../../../102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/07_delivery/CA-D-638-PROGRAMMATIC-STANDARD-DELIVERY--deliver-a-closed-reproducible-fixture-and-package-boundary.md) | Deliver a closed reproducible fixture and package boundary
| Standard | [CA-D-640@3](../../../102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/07_delivery/CA-D-640-PROGRAMMATIC-STANDARD-DELIVERY--deliver-multi-project-mcp-binding-contract.md) | Deliver the multi-Project MCP binding contract

## Result format

Delivered: exact carriers and entrypoint. Checked: actual environment/dependency/reproducibility evidence. Remaining: missing inputs, undeclared dependencies, unresolved authority, failed/unavailable checks and risks. Claim only observed results.

