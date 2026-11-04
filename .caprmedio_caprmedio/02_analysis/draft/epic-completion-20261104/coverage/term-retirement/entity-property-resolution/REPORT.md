# Entity and Property Term resolution

**Source-only previews; no Current carrier changed.**

## Prepared artifacts

- M453 preview: `.caprmedio_caprmedio/02_analysis/draft/epic-completion-20261104/coverage/term-retirement/entity-property-resolution/CA-M-453.preview.txt` (base CA-M-453@3; intended next version 4). Summary remains `Define Property`.
- Exact M451 retirement preimage: `.caprmedio_caprmedio/02_analysis/draft/epic-completion-20261104/coverage/term-retirement/entity-property-resolution/CA-M-451.retirement-preimage.txt` (byte-exact SHA-256 `eb7a86a6a60e74c43f0f1f9a1cb990c3e3e0b8eed7c27701067596ec3ad4c253`).
- Current authority pins and full incoming-reference rows are in `manifest.json`.

## M453 preview meaning

The lexical `Property` Term describes a `Node.**` Property with exactly one immediate bearer through `IS_PROPERTY_OF`; `Bearer.Property` is the qualified Subject and `HAS_PROPERTY` is derived. The preview removes the `Entity/Property` Subject and all stale Draft/adoption text. It preserves the Term Definition role and active `Term//Property` target.

## Atomic repair refs

- `Term//Entity` Subjects: CA-E-444, CA-M-451, CA-R-1318. M451 retirement therefore needs coordinated updates to CA-R-1318 and CA-E-444; M451 itself is the retiring source.
- `Entity/Property` Subjects: CA-E-246, CA-E-449, CA-M-125, CA-M-451, CA-M-453, CA-R-1247, CA-R-1259, CA-R-1284, CA-R-1318, CA-R-1931, CA-R-2003. Current R1247 and R2003 are among the sources to repair under Node Property classification.
- Literal Atom-ID mentions of CA-M-451 elsewhere: none found.
- Literal Atom-ID mentions of CA-M-453 elsewhere: none found.
- `Term//Property` Subject refs remain in 30 Current carriers; these are not global registry removals.

Reference lines, paths and hashes are pinned in `manifest.json`. The source selectors distinguish typed Subjects from ordinary English “Entity” mentions.

## Approved inbound repairs and naming scope

- Added R1247/R2003 previews with active Subject `Node.**`, preserving complete-path identity, exactly-one immediate bearer, and missing-edge behavior for all Node Properties.
- R1318 removes its typed `Term//Entity` and old `Entity/Property` Subjects; E444 removes the `Term//Entity` selector and obsolete root-Entity exception fixture. The global Term registry and Property Term remain.
- R2276 applies from `CAPRMEDIO_MODEL`, keeps one-to-one naming and reusable Terms, and permits a short complete name only when the exact expression is source-admitted and unambiguous. Its Summary is unchanged.
- `Package <+ Module <+ Code Unit` is three connected endpoint entities. Check declaration coverage for Package, Module, and Code Unit separately; do not classify the entire chain as one missing entity or add a fourth kind.

Exact preview and inbound-reference hashes are in `manifest.json`. All remaining typed legacy `Entity/Property` Subject refs are covered by versioned previews to `Node.**`; M451 is retired. Literal English “Entity” remains unchanged.

The additional typed-reference previews cover CA-E-246, CA-E-449, CA-M-125, CA-R-1259, CA-R-1284, and CA-R-1931.
