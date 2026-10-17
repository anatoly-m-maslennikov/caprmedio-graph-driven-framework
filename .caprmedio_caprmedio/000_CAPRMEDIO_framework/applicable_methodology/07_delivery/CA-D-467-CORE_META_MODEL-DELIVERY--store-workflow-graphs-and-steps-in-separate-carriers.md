---
subjects:
  governs: "Entity/Continuant/Object/Atom/Content Role: Operations/Type: Workflow"
  depends_on:
    ["Entity/Carrier/Directory Carrier", "Entity/Carrier", "Entity/Continuant/Object/Atom/Content Role: Operations/Type: Workflow", "Entity/Continuant/Object/Atom/Content Role: Operations/Type: Step"]
version: 9
updated_at: "2026-10-16 12:09:33 +0000"
relations: {"delivery_for": ["CA-R-1570", "CA-R-1569"], "relates_to": ["CA-D-457", "CA-D-285"]}
atom_id: "CA-D-467"
content_role: "Delivery"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/07_delivery/CA-D-467-CORE_META_MODEL-DELIVERY--store-workflow-graphs-and-steps-in-separate-carriers.md
  source_atom_id: CA-D-467
  source_atom_revision: 9
  source_sha256: 01a3ebd2514af6a4c4599b914aad723263c8577fa967932783e529222acd68f6
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Store Workflow graphs **and** Steps in separate carriers

## Scope

folder-backed Workflows **and** their nested Step Carriers.

## Claim

a folder-backed Workflow **must** use **`=1`** Workflow Atom Markdown Carrier **and** **`<=1`** optional sibling Directory Carrier with the same filename stem. the Directory Carrier contains separate Markdown Carriers for its Step Atoms; it **must not** contain a second Workflow definition.

## Details

- the Workflow Atom's main content carries the graph scheme; a Step Atom's main content carries that Step's Action reference **and** parameter/input bindings.
- a Step Markdown Carrier **may** have **`<=1`** optional sibling Directory Carrier with the same filename stem containing subordinate Step Markdown Carriers. this placement rule applies recursively at **every** nested Step level; **every** folder-backed Step retains its own Markdown Carrier.
- Action Atom Carriers **must** remain separately outside the entire Workflow **and** nested Step directory tree. Steps reference reusable Actions **without** copying their behavior.
- folder nesting organizes Carriers; it **must not** establish a Step Relation, execution inheritance, **or** execution order. the Workflow graph defines control flow, **and** **every** Step retains its own invocation of **`=1`** referenced Action.
- the Atom files retain the existing Atom filename, frontmatter, **and** main-content rules; the folder is a grouping Carrier, **not** another Workflow definition **or** owning Scope Unit.
- grouping is optional: separately placed Workflow **and** Step Carriers remain permitted **when** their references resolve unambiguously. a carrier-only move does **not** redefine the graph **or** change carried Status.
- **every** admitted Workflow **or** Step parent Status change requires the containment cascade under CA-R-1521: compose independent single-Atom Actions for the latest Revision of **every** recursively contained Step, requesting the same Status under each Atom's own model. separately placed referenced Steps **and** Actions outside the Carrier tree are **not** cascade targets; older archived Revisions retain their exact bytes, Version **and** Status.
- apply CA-D-466's Status placement inside each local Workflow **or** Step container. descendants remain inside the parent Carrier tree for **every** Status, including Archived; apply CA-D-289's Version suffixes **to** Archive Carrier basenames. this rule does **not** migrate noncanonical legacy `archive/` trees.
- read each Step's Status from its own Markdown Carrier under CA-D-483; containing Status directories **or** parents **must not** override it. the cascade writes the changed latest Revisions; it **does not** infer execution order **or** execution inheritance.
