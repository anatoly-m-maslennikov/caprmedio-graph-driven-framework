---
atom_id: CA-P-2043
content_role: Plan
type: Plan
label: Task
work_sequence_number: 53
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
assignee: AI Agent
status: Active
subjects:
  governs: Entity
  depends_on: [Atom, Subject, Projection, Plan, Operator]
version: 1
updated_at: "2026-10-11 01:23:41 +0400"
relations:
  is_decomposition_of: [CA-P-1966]
  depends_on: ["CA-P-1972", "CA-P-1988", "CA-P-1989", "CA-P-1990", "CA-P-1992", "CA-P-1993", "CA-P-1994", "CA-P-1995", "CA-P-1996", "CA-P-1997", "CA-P-1998", "CA-P-1999", "CA-P-2000", "CA-P-2001", "CA-P-2002", "CA-P-2003", "CA-P-2004", "CA-P-2005", "CA-P-2006", "CA-P-2007", "CA-P-2008", "CA-P-2009", "CA-P-2010", "CA-P-2011", "CA-P-2012", "CA-P-2013", "CA-P-2014", "CA-P-2015", "CA-P-2016", "CA-P-2017", "CA-P-2018", "CA-P-2019", "CA-P-2020", "CA-P-2021", "CA-P-2022", "CA-P-2023", "CA-P-2024", "CA-P-2025", "CA-P-2026", "CA-P-2027", "CA-P-2028", "CA-P-2029", "CA-P-2030", "CA-P-2031", "CA-P-2032", "CA-P-2033", "CA-P-2034", "CA-P-2035", "CA-P-2036", "CA-P-2037", "CA-P-2038", "CA-P-2039", "CA-P-2040", "CA-P-2041", "CA-P-2042"]
  blocks: ["CA-P-1967", "CA-P-1909"]
---
# Summary

Integrate current Subject mapping ledger

## Objective

Produce one complete, source-pinned occurrence ledger with every unresolved finding visible.

## Details

Estimated own work: 15 minutes. Required prerequisites: CA-P-1972, CA-P-1988, CA-P-1989, CA-P-1990 and all 51 direct review Tasks Done. Read and pin `.caprmedio_caprmedio/_projection/core-entity-review/stage2/current-subjects.contract.md` SHA-256 `5eb0d90022b68a7d1d2cd27cf60a147deaf4161cb9b2e1c8bdf6c4ef8f2a10bf` and `.caprmedio_caprmedio/_projection/core-entity-review/stage2/current-subjects.review.contract.md` SHA-256 `b7c9c065f997d5bae1409f5c09b4223d08327a523decab6d26c2e4425fd2c28b`. Recheck the inventory SHA-256 `e284dbe4943568bc75b7f9ba63ebf583372a60813e62eee3d43b5b75b270220a`, all batch/source/input pins and each receipt. Verify every selected source/finding and occurrence exactly once, no overlap, unchanged/proposed/unresolved states, evidence spans and confidence. An incomplete review cannot count as Done.

Persist only the derived integrated ledger and verification receipt under stage2. Preserve the original candidate/captured review. Ask only about concrete unresolved design conflicts; missing evidence stays research work. Low-confidence mappings must remain null. If research remains, decompose it into bounded Tasks before completing this Plan. No Core write, grammar adoption, native fact admission or migration approval. CA-P-1909 retains accepted-graph ownership; CA-P-1910–1912 retain sealed approval, application and reproduction. Root owns shared integration and Git.

### Definition of Done

Not Done if any prerequisite is incomplete, a pin is stale, coverage or evidence verification fails, a selected source/finding is missing, unresolved mapping work is hidden, or own work exceeds 15 minutes without decomposition. This ledger alone does not finish or authorize migration.
