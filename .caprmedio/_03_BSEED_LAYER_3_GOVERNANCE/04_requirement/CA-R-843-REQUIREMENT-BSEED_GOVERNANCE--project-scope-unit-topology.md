---
atom_id: CA-R-843
subject_scopes:
  - settings
version: 1
updated_at: 2026-08-21 01:38:53
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CA-R-842-REQUIREMENT-BSEED_METAMODEL--define-ordered-upstream-unit
    - CAPRMEDIO-GOV-REQU-626--encode-project-settings-as-a-generated-toml-projection
    - CAPRMEDIO-GOV-REQU-647--register-project-settings-projection-mechanics
---
# Project Scope Unit topology

Each Project Graph State Projection must expose the canonical direct Project-root Scope Unit carrier folders separately from the complete current Scope Unit topology. Every Scope Unit row identifies the Unit, carrier path, Structural kind, Structural level, Structural coordinate, and immediate `structural_parent`; an absent parent is explicit. An `ordered_unit` row also exposes its `local_order` and derived `upstream_unit`, with absence explicit for the first ordered peer. The Projection must not enumerate Content-role folders or their role-local organizational subfolders as Scope Units or root Scope Unit folders.
