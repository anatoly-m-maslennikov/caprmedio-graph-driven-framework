# CFEL reference-migration handoff

Status: read-only mapping evidence, not a source migration or adoption result.

## Evidence pins

- Application plan: `adoption-plan.json`, SHA-256 `a917133ffee7a744e0ed203122e49a5aa11f8e763c68621c9811abf9bb6758d3`.
- Application receipt: `adoption-receipt.json`, SHA-256 `bda1136bd581f1782db99e3fae09d7785e022dbfca9fe244073e56acf0385def`; it is `APPLIED_VERIFIED`, with native workflow admission and journal append both false.
- Final cohort: `final-live-cohort.json`, SHA-256 `2a09b40f4428467c91823b3ff6da560a6684aa1f1ad9fe631438614105bb6681`; it is checked Draft cohort evidence, not adopted.

## Classification

| Reference kind | Action |
| --- | --- |
| Unversioned Current/native reference | Retain unless a checked source-level migration explicitly names it. Do not blanket-retarget. |
| Versioned `@N`, archive, receipt, plan, snapshot, or quoted literal | Historical evidence; retain verbatim. |
| Draft reference named by the plan’s `identity_replacements` | Retarget only at the exact reviewed source occurrence. |
| Split/collision/withdrawn mapping | Hold; do not infer one successor. |

## Language-rule mapping coverage

The plan has 29 old-source mapping rows to the 28-ID `CA-R-2794`–`CA-R-2821` allocation range. Twenty-seven final fresh allocation targets remain after the one withdrawn allocation. `CA-R-2810` is withdrawn, so its two old-source rows are explicit holds rather than live replacements:

- `CA-R-2592 -> CA-R-2810` — hold: withdrawn standalone allowed-value Rule.
- `CA-R-2777 -> CA-R-2810` — hold: same withdrawn target; no inferred split successor.

All other plan rows are direct old-to-fresh mappings: `2591->2794`, `2593->2795`, `2594->2796`, `2596->2797`, `2597->2798`, `2599->2799`, `2600->2800`, `2601->2801`, `2602->2802`, `2603->2803`, `2604->2804`, `2606->2805`, `2607->2806`, `2608->2807`, `2609->2808`, `2611->2809`, `2780->2811`, `2781->2812`, `2612->2813`, `2613->2814`, `2614->2815`, `2615->2816`, `2720->2817`, `2769->2818`, `2770->2819`, `2773->2820`, and `2774->2821`.

## Required special cases

- `CA-R-1245` Current is an unversioned live reference: retain it. The plan’s same-ID Draft `CA-R-1245@29` is separately withdrawn as redundant; do not turn that Draft withdrawal into a Current-ID retarget.
- `CA-R-2616`, `CA-R-2605`, and `CA-R-2610` have no final-cohort successor mapping. They remain explicit Current-native holds pending coordinated Operator-declaration retirement; do not substitute a neighboring syntax Rule.
- The final value-Relation identity repair is exact: `2822->2826` (`HAS_ALLOWED_VALUE`), `2823->2827` (`IS_ALLOWED_VALUE_OF`), `2824->2828` (`HAS_VALUE_CONSTRAINT`), and `2825->2829` (`IS_VALUE_CONSTRAINT_OF`).

## Native stale-reference check

Scoped native non-Draft/non-archive scan found zero references to old Relation IDs `CA-R-2822` through `CA-R-2825`; four final Draft headers `CA-R-2826` through `CA-R-2829` exist. This checks only stale native content, not analysis/history/receipt evidence.

## Handoff boundary

Apply only to exact unversioned live references selected for migration after source review. Keep every versioned/historical occurrence and every ambiguous or withdrawn mapping as above. No Current adoption, parser/runtime change, or workflow admission is established by these mappings.
