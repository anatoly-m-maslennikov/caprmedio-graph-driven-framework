---
content_role: Requirement
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
local_tier: Standard
global_tier: 8
author: Anatoly Maslennikov
status: Draft
subjects:
  governs: PROGRAMMATIC
  depends_on: []
version: 1
updated_at: "2026-10-20 02:48:37 +0400"
relations: {}
---
# Summary

Compose expandable and overridable model declarations

## Scope

PROGRAMMATIC consumption of the entity model, Atom Types, Relation Types and Graph Rules from the base meta-model, activated installed Extensions and Project Configuration.

## Claim

PROGRAMMATIC shall support additions and explicit overrides of configurable Type, Relation Type and Graph Rule definitions while preserving the protected base: Atom identity/meaning, Content Role meanings, and the applicable internal/external distinctions. An override shall change the selected effective definition only within a declared overridable extension point; it shall not mutate its provider's source bytes, reidentify an existing Atom or reinterpret a protected basic meaning. Installed availability alone shall not activate an Extension.

## Details

Only the selected Project’s declared and admitted configuration carrier may contribute an override; a schema-valid unrelated file is not a provider. Each effective declaration shall retain its governing source, provider/revision, version or digest and applied override/configuration provenance. Resolution shall state the qualified target, allowed change surface, compatibility conditions and explicit precedence/conflict rule. General/Standard Local Tier is not permission to shadow Core. Current R1375 remains binding: any required new Core permission is a future governed dependency before activation, not a bypass supplied by this Draft. The exact protected internal/external definitions must be source-bound before adoption; an external Type-value example is not their general definition. Supported declaration/configuration changes shall be achievable through versioned files without editing engine code; avoiding an image rebuild is the target for supported data changes, with the supported language/capability boundary stated. Format, composition site, refresh trigger and detailed override policy remain open choices. Model declarations remain separate from actual Atom-ID relation tuples; this does not prevent rules from later validating such data under their own contract.
