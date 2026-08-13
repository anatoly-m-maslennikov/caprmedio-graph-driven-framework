# Methodology hub

## Purpose

This is the helicopter-view entry point for the DSET Spec Loops methodology. It routes readers through the delivery stages and cross-cutting standards without making the repository root README an exhaustive methodology index.

## Boundaries

This area owns the reusable DSET delivery method. Reusable framework source
lives in `10_project/` and the ordered `11_layer_meta/` through
`16_layer_ops/` source layers. An adopter installs the accepted methodology
under `.caprmadio/000_caprmadio_framework/` and keeps project and scoped
artifacts in repeated ordered Content-role folders. Earlier family and special
project/version containers remain compatibility or migration inputs only.

## Start here

1. `00_Tool Development Playbook.md` — pipeline, stage routing, and document responsibilities.
2. `01_Spec Authoring Patterns — Service Spec Conventions.md` — domain and behavioral specification.
3. `02_Test and Evaluation Case Patterns — Proof Artifact Conventions.md` — deterministic tests and qualitative/probabilistic evals as separate proof contracts.
4. `03_Implementation Plan Patterns — Service Build Conventions.md` — dependency-ordered build and rollout planning.
5. `04_General Build Rules — Tool Code Conventions.md` — runtime risk, durability topology, safety, and supportability patterns.
6. `05_Layered Build Standard — DDD, TDD, Small Functions, Typed Gates.md` — language-neutral code gates and applied implementation-language profiles.
7. `06_External Grounding — LLM Power-User Practice.md` — external provenance and candidate practices.

## Cross-cutting navigation

- Artifact governance — artifact profiles, types, authoring, hubs, and maintenance.
- Installed methodology — the edition currently resolved by this repository's skills.
- Applied project artifacts — this repository's current project truth and records.
- `methodology-todos` — retired planning context, not current methodology.

The numbered documents remain stable responsibility owners. The documentation architecture is cross-cutting and is not pipeline stage 7.
