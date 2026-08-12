---
artifact_type: requirement
artifact_id: CARMADIO-REQUIREMENT-GOV-147
scope_path: layer:gov
subject_scopes:
  - methodology-sync
priority: high
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  - type: child_of
    targets:
      - CARMADIO-REQUIREMENT-GOV-052
---

# Requirement — Provide an explicit root-to-installed-methodology sync script

The repository provides one directly executable script that synchronizes reusable root methodology into `.carmadio/000_CARMADIO_METHODOLOGY` through the canonical synchronization engine.

Preview is the default. Mutation requires an explicit apply flag. Synchronization is one-way from root source to installed methodology; the script never copies installed carriers back to root source.

An applied run verifies that no methodology drift remains and fails nonzero if the repository is invalid, synchronization fails, or residual drift remains. Output identifies every affected carrier concisely and deterministically.

## Primary claim

Maintainers can preview, apply, and verify complete root-to-installed-methodology synchronization through one deterministic script without remembering an internal CLI command chain.
