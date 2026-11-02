# Scope Unit Declaration source fields

The 44 retained instance Drafts state existing facts in prose; the separate APPLICABLE_METHODOLOGY Scope Unit Draft is withdrawn after the Operator confirmed it is a special Projection. This map does not introduce new YAML keys, GFEL operators or Scope Unit properties.

| Existing source | Declaration treatment | Existing defining sources |
| --- | --- | --- |
| Settings project name | Root Scope Unit identity; no invented Project Structure row | R1484, R1738 |
| scope_unit_name | Exact Name; the active Subject identifies this Scope Unit instance | R1484 |
| scope_unit_type | Preserve Ordered or Unordered | R1484, D442 |
| scope_unit_label | Preserve the existing Label | R1484, D442 |
| parent | Immediate containing Scope Unit; PROJECT resolves to the named Project root | R2402, R1757 |
| local_order | Preserve the nine retained explicit values; the tenth belongs to the withdrawn hosting Scope Unit; do not add values to Unordered units | R1484, D442 |
| navigational_order_number | Omit from Scope Unit Drafts, following the latest Operator decision | Supersedes the relevant parts of R1484, D442 and D297 |
| authority_path | Preserve the authority Carrier place; this is not logical Scope Unit.Path | D312, D442, D445, R2133 |
| delivery_path | Preserve the Delivery/Implementation Carrier place | D312, R862, D442, D445 |
| authority_mode | Preserve five retained explicit strict overrides; the sixth belongs to the withdrawn hosting Scope Unit; do not copy inherited defaults | R1430, R1402, R2404, D391, D442 |

Scope Unit.Path describes logical ancestry. A Carrier path describes a storage place. Moving one does not silently redefine the other.

The source TOML has no Scope Unit ID registry. No IDs are inferred from the generated Scope Unit graph. Separate Goals and local Tier-0 Contracts are inventoried in [Goal coverage](goal-coverage.md), not copied into Declaration Claims.

The root Declaration uses the Project Settings name, `caprmedio`, and the existing external Operator ownership. Its final discovery/location remains part of adoption; central Draft staging is not that decision.

Navigation Number remains only for Steps and Plan Atoms. Existing explicitly declared Carrier paths stay unchanged during preparation. No file or folder is renamed to implement a new convention here.
