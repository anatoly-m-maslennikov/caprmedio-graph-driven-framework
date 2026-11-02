---
atom_id: CA-R-2277
current_scope_unit: PROJECT_CONFIGURATION
status: Active
tier: 1
subjects:
  active: Named Selection//Extension Sources
relations: {}
version: 4
updated_at: 2026-11-02 07:49:21 +0400
role: Requirement
form: Rule
---
## Summary

Define Extension Sources Selection

## Claim

Extension Sources is the named Selection of immutable installed Extension source Atoms available as candidate inputs to methodology compilation. Membership establishes availability, not activation. Framework Settings separately selects activation and the installed source version for an Extension; Applicable Methodology separately includes only sources applicable under those settings.

```CFEL
Named Selection//Extension Sources
```

## Details

CA-R-1175 requires preservation of installed source versions as candidate inputs. CA-R-1228 governs the applicable Methodology subset, and CA-R-1724 separates installed availability from activation and version selection. This definition identifies their shared candidate population; it adds no activation procedure, new Scope Unit, or automatic conflict resolution.
