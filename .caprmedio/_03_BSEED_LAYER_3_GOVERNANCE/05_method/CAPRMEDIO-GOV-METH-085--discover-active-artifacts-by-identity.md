---
subject_scopes:
  - artifact-catalog
tier: core
version: 2
updated_at: 2026-08-20 18:32:49
relations:
  child_of:
    - CAPRMEDIO-META-REQU-085--separate-active-authority-from-preserved-history
---
# Discover active artifacts by identity

CAPRMEDIO discovery resolves requested `atom_id` property values within the
selected project's active control-root frontier, excludes drafts and every
role-local archive, follows only expressly governed native locators, validates
that each identified filename mirrors the property, and stops on zero or
multiple active matches.
