---
subjects:
  governs: Scope Unit
  depends_on:
  - Project.Settings
  - Project.Framework Settings
  - Project
  - Carrier
version: 1
updated_at: 2026-11-02 19:17:40 +0400
relations: {}
atom_id: CA-E-671
status: Active
tier: 6
role: Evaluation
form: Eval Case
projection:
  source_carrier_path: ../../../CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/06_evaluation/CA-E-671-CORE_META_MODEL-EVAL_CASE--validate-settings-boundaries-and-scope-unit-declarations.md
  source_atom_id: CA-E-671
  source_atom_revision: 1
  source_sha256: b312c38875940094a2ec7435dfc4ffeefeae2c75a32e9d9398520c3c53864488
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Validate settings boundaries and Scope Unit Declarations

## Claim

Settings resolve inside their own Project without cross-Project fallback. Project Settings remain authoritative initialization inputs and Framework Instance Settings remain authoritative instance choices. A declared Scope Unit remains visible when its Carrier or active Goal is missing. An undeclared folder remains an observation. Scope Unit Declarations do not change Settings, and Settings do not replace a Declaration. No Projection edit changes Settings, Scope Unit Declarations, or source Atoms.

Every Framework Instance's Methodology Sources and Applicable Methodology output resolve beneath its own Project's `000_CAPRMEDIO_framework/` directory. Rebuilding one Project's Applicable Methodology does not read, replace, or modify another Project's sources, Settings, or compiled results. A missing selected Project instance is reported rather than resolved through another Project or the former repository-shared framework root. Nesting the framework directory does not change source Atom identity or make a Projection a second authoritative Atom.

## Details

### Test case

Create two Projects in one repository, each with Project Settings and a `000_CAPRMEDIO_framework` directory. Resolve both Settings before creating Project Atoms or Implementation. Give the instances distinct Methodology Sources and Applicable Methodology results. Declare a Scope Unit with no active Goal and no directory; separately add an undeclared candidate directory. Include Draft and archived Goals as non-active evidence.
