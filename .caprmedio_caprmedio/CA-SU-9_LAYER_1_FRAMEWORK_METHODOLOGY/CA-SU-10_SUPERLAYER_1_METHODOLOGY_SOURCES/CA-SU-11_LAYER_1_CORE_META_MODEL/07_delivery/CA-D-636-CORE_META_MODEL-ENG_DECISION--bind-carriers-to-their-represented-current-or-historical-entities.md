---
atom_id: CA-D-636
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CAPRMEDIO_MODEL <+ Carrier
  passive:
  - CAPRMEDIO_MODEL <+ Entity
  - CAPRMEDIO_MODEL <+ CFEL <+ Relation//CARRIES
  - CAPRMEDIO_MODEL <+ Entity/Object/Continuant/History
relations:
  child_of:
  - CA-R-1174
version: 16
updated_at: 2026-11-02 00:18:22 +0400
tier: 1
role: Delivery
form: Policy
---
## Summary

Bind Carriers to their represented current or historical Entities

## Claim

### Prose Claim


Carrier bindings of non-ephemeral Entities.


a Carrier binding **must** identify the Entity actually represented by that Carrier. a current Entity's Carrier binds that current Entity; a preserved historical version's Carrier binds that archived Atom version or the historical record actually represented, not a separate Revision entity. citing a current Entity's Version **must not** reclassify the current Entity as an archived version.

## Details

Use the separately defined CARRIES meaning. Its IS_CARRIED_BY inverse exposes the same binding with the endpoints reversed; neither direction substitutes an archived version for the Current Entity actually represented. The applicable Carrier policy determines the representation. General representation rules may carry dependent properties inside one File Carrier; this policy does not require a separately registered binding for each field or section. It creates no additional Carrier, snapshot, Journal record or history gate.
