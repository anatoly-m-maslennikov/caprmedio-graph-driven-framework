# Test plan — Bootstrap the DSET project structure

## Deterministic checks

| Test ID | Requirement | Proof |
|---|---|---|
| **CARMADIO-TEST-CASE-GOV-001** | CARMADIO-REQUIREMENT-GOV-001 | Assert `dset/{README.md,dset.toml,specs,changes,templates,schemas}` exists and no competing project-truth root is introduced |
| **CARMADIO-TEST-CASE-GOV-002** | CARMADIO-REQUIREMENT-GOV-002 | Parse `dset/dset.toml`; assert one package named `methodology`, its path exists, mode is `single-package`, and global root is null |
| **CARMADIO-TEST-CASE-META-001** | CARMADIO-REQUIREMENT-META-001 | Assert this change contains the eight named Markdown documents plus `specs/` and `proofs/` |
| **CARMADIO-TEST-CASE-OPS-001** | CARMADIO-REQUIREMENT-OPS-001 | Assert PR is non-pending before archive; assert archive path/date and fresh verification after the last content change |
| **CARMADIO-TEST-CASE-GOV-003** | CARMADIO-REQUIREMENT-GOV-003 | Assert manifest values remain `documentation-v1-pending` and `canonical_command: pending` until executable assets land |
| **CARMADIO-TEST-CASE-GOV-004** | All | Resolve local Markdown links, parse YAML, check balanced fences/details, and run `git diff --check` |

## Regression rule

A future structural defect adds a failing fixture to the canonical validator once that validator exists. Until then, verification records the exact read-only commands and exit status used for this bootstrap.
