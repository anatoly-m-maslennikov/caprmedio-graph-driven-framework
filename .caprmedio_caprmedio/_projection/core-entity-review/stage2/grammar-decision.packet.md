# CA-P-1976 — Subject grammar decision packet

Status: decision pending. Prerequisite CA-P-1960 is recorded Done at source-commit prefix `83dc6b866`. This is a derived, source-pinned packet only. It does not change Core authoring Atoms, create the successor Atom, approve native relation admission, or migrate any Subjects.

Prepared 2026-10-11 from the Core authoring root:
`.caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL`

## Minimum five-change candidate

The current conflict is concrete: CA-R-1204@14 says `/` is bearer qualification, while the requested Subject profile needs `/` broader→narrower and `.` bearer→dependent. CA-R-1204's Summary is its identity-bearing meaning and must not be rewritten in place. Preserve it as the predecessor and allocate a new Operator-assigned successor only after approval; no successor ID or Atom is created by this packet.

1. **Replacement candidate for CA-R-1204 (new ID pending allocation, proposed version 1).** Proposed Summary: `Use Subject Path Separators for Broader-to-Narrower and Bearer-to-Dependent`. Proposed Claim: in the proposed Subject Path profile, `/` separates a broader component from its following narrower component; `.` separates a bearer component from its following dependent component; `:` separates a Property component from its following allowed-value component; and `@` is not Subject syntax. Subject Paths still resolve one canonical target and do not create target identities. The mechanical native fact for `.` is `Dependent IS_BORNE_BY Bearer`; for `:` it is `AllowedValue IS_ALLOWED_VALUE_OF Property`. A native edge for `/` is **not admitted by this packet**: if later bound to existing Terms-Graph `NARROWER_THAN`, its native direction would be `Narrower NARROWER_THAN Broader`, but CA-R-1435 does not authorize a new Subject/Entity relation.
2. **CA-R-1321@12 → proposed v13.** Add `.` to the registered Subject syntax and to the “not a Term” list. State that `@` is outside Subject syntax, while every named component still resolves to a Term and the expression identifies one target.
3. **CA-R-1324@10 → proposed v11.** Reserve `/`, `.`, and `:` in Subject-expression Term names. Do not turn `@` into a separator or silently impose a new Term-character rule beyond the explicit parser boundary.
4. **CA-M-228@14 → proposed v15.** Author Subject Expressions with `/` in broader→narrower order, `.` in bearer→dependent order, and `:` in Property→allowed-value order. Resolve all named components; retain the no-copy/no-new-target rule and existing GOVERNS/DEPENDS_ON incidence boundary.
5. **CA-E-383@13 → proposed v14.** Validate the proposed profile: dot bearer order, colon allowed-value order, slash broader→narrower syntax profile, reserved `/ . :`, and rejection of `@` as a Subject token. Replace its `evaluation_for` binding to CA-R-1204 with the allocated successor after approval. Its literal example must pass only if the approved profile resolves it; no native slash relation is inferred.

This is an actual Subject-parser/validator profile, not merely a tree-rendering preference. It changes how approved Subject expressions are interpreted, but it deliberately does not itself admit a new native graph Relation or perform source migration. That remaining boundary is the point of the Operator question.

## Stable authorities — no body change in this packet

- CA-R-1194@14 defines a Subject Path as a full canonical Subject Expression resolving one Entity; it does not define separator direction.
- CA-R-1198@13, CA-R-1199@13, and CA-R-1200@16 retain flat direct GOVERNS/DEPENDS_ON source references and their Atom-to-target directions.
- CA-R-1245@13 and CA-R-1436@8 retain colon as `IS_ALLOWED_VALUE_OF`; display order is Property→AllowedValue, native order is value→Property.
- CA-R-1260@13 retains `IS_BORNE_BY` as Dependent→Bearer; display order is Bearer→Dependent.
- CA-R-1435@8 remains Terms-Graph-only `NARROWER_THAN`; it does not admit `/` as an Entity/Subject edge.
- CA-M-232@12 continues to reproduce exact direct Subject targets and relation kinds without creating another authority.
- CA-E-246@25 keeps its Atom-Subjects coverage Claim. Its literal `Atom/Content Role: Requirement/Type: Demand` fixture requires isolated revalidation under the approved profile, not an inferred authority rewrite.
- CA-D-269@12 keeps flat `subjects.governs` and `subjects.depends_on` serialization.
- CA-D-289@12 (and contextual CA-D-301@15) keep `@<version>` as archive-carrier filename syntax, not Subject syntax.
- CA-R-1688@24's broader-parent→narrower-child Scope-path ordering is a separate Scope-path rule, not authority for Subject grammar.

## Exact Operator question

> May Step 1 admit exactly this Subject-grammar exception: `/` is a Subject separator ordered broader→narrower, `.` is a Subject separator ordered bearer→dependent, `:` remains Property→allowed-value, and `@` is not a Subject token and remains display/carrier-only; may the body-only revisions to CA-R-1321, CA-R-1324, CA-M-228 and CA-E-383 be made together with a new Operator-assigned successor to CA-R-1204 (preserving CA-R-1204 as predecessor/history), while preserving native `Dependent IS_BORNE_BY Bearer`, native `AllowedValue IS_ALLOWED_VALUE_OF Property`, and the existing Terms-Graph-only scope of `NARROWER_THAN`, with no unapproved native slash relation or Subject migration?

Approval must be tied to this packet and its exact hash. Refusal or deferral leaves grammar cutover and Subject migration blocked. Existing source Atoms, captured reviews, candidate JSON, and Operator decisions remain untouched.

## Source and packet pins

`CA-P-1976@2` packet plan: `03_plan/18-CA-P-1959-EPIC--improve-entity-model-stage-2/06-CA-P-1964-TASK--resolve-the-subject-grammar-cutover-boundary/01-CA-P-1976-TASK--prepare-the-subject-grammar-decision-packet.md`; SHA-256 `ce549add3a1eddc5a5d915857d9f83f53da5aec61d4c2da327b9f5697d07f1fa`.

Candidate display input: `_projection/core-entity-review/presentation/operator.entity-graph.candidate.json`; SHA-256 `99e7710f5ef83df2b1f3ec1ef4142547655e63bef7415266c5521380da7fa99b`.

Operator direction record: `_projection/core-entity-review/design/operator.decisions.md`; SHA-256 `53eeb7a3fdaa002cd05170fe185cfb5baeea72814a1f32567d8eea6f56ac65cb`.

Minimal-change source pins (all under the Core authoring root):

| Atom | Current version | Relative path | SHA-256 |
|---|---:|---|---|
| CA-R-1204 | 14 | `04_requirement/CA-R-1204-CORE_META_MODEL--use-subject-path-slash-only-for-bearer-qualification.md` | `f57d56dab2cff12ea38a94900a1f146e40ead39f0af9e26e3130e9867f290dda` |
| CA-R-1321 | 12 | `04_requirement/CA-R-1321-CORE_META_MODEL-CORE--define-subject-expression.md` | `6baf3f4179591dcc89c458dcb6503a55f24b70f9f1bd93203f4b748a9bcb1b8c` |
| CA-R-1324 | 10 | `04_requirement/CA-R-1324-CORE_META_MODEL-REQUIREMENT--reserve-subject-expression-separators.md` | `f38d4cc446b04cde6958f1fe011679ff95048bdfe30f360d11a7366a572bc0b1` |
| CA-M-228 | 14 | `05_method/CA-M-228-CORE_META_MODEL-METHOD--write-subject-expressions-with-bearer-and-value-qualification.md` | `f5a2152648b95c04af56c49118f43ac64ee46dd8183b23913cb64f335d6f26df` |
| CA-E-383 | 13 | `06_evaluation/CA-E-383-CORE_META_MODEL-EVALUATION_APPROACH--reject-invalid-subject-expressions.md` | `00c3e901fbd18cdb584387386f6b04cd43905f651c4369e16a97d20b469b3274` |

Stable authority pins:

| Atom | Version | Relative path | SHA-256 |
|---|---:|---|---|
| CA-R-1194 | 14 | `04_requirement/CA-R-1194-CORE_META_MODEL-CORE-REQUIREMENT--define-subject-path.md` | `159ff72818c390f6d126c543587ebb8de49d5d5ae53cfc0e437df25d25e3c30e` |
| CA-R-1198 | 13 | `04_requirement/CA-R-1198-CORE_META_MODEL-CORE-REQUIREMENT--define-atom-subjects.md` | `6eb2f68642b09eb05e1c6ece6b2dd92d309b92445fcea3e0b37f4b485576365b` |
| CA-R-1199 | 13 | `04_requirement/CA-R-1199-CORE_META_MODEL-CORE-REQUIREMENT--define-governs-subject-relation-kind.md` | `1eb27ffbeb24d9ba35e39bfb6e6207214260867b6fb0687b1952ba70a7defd30` |
| CA-R-1200 | 16 | `04_requirement/CA-R-1200-CORE_META_MODEL-CORE-REQUIREMENT--define-depends-on-subject-relation-kind.md` | `baa339768dcb5ef82ea6ce07c2020b934f787e552fc3e08a37dbc85c0021aa1f` |
| CA-R-1245 | 13 | `04_requirement/CA-R-1245-CORE_META_MODEL-REQUIREMENT--qualify-allowed-values-with-colon.md` | `fbfb35fcfff4feadfe7ec62e599e502a65eb0007108fe7947ca555d71abb0e54` |
| CA-R-1260 | 13 | `04_requirement/CA-R-1260-CORE_META_MODEL-CORE-REQUIREMENT--define-is-borne-by.md` | `ea7911f8d3bc88bcba954332193354c80df63005dbf94812960dda162615f54d` |
| CA-R-1435 | 8 | `04_requirement/CA-R-1435-CORE_META_MODEL-CORE--define-narrower-than.md` | `15fa6d3511be9f2d4ad76eea38373f13bcbb37522a2f7c5b985e0a4b836f54cb` |
| CA-R-1436 | 8 | `04_requirement/CA-R-1436-CORE_META_MODEL-CORE--define-is-allowed-value-of.md` | `a33bdc582beb140647e6012022730abf531f6311923edf80ed7d1fe1614dabad` |
| CA-M-232 | 12 | `05_method/CA-M-232-CORE_META_MODEL-CORE--derive-atom-subjects-graph-from-current-atom-subjects.md` | `01e1f3355f52762beabcc19fe30746a536c12f79015f581d00b6ff765a202cd7` |
| CA-E-246 | 25 | `06_evaluation/CA-E-246-CORE_META_MODEL-QA_CASE--validate-atom-subjects.md` | `6d5e65915b857be8e399aee9b32364dde2caa56ec6757bd8e69282b4ffee0098` |
| CA-D-269 | 12 | `07_delivery/CA-D-269-CORE_META_MODEL-DELIVERY--serialize-atom-subjects-in-frontmatter.md` | `eea15e5b1c2411acdd552c8701da98ac34bab89a107ee05f28760eb1ce8eeac3` |
| CA-D-289 | 12 | `07_delivery/CA-D-289-CORE_META_MODEL--serialize-archive-revision-version-suffixes.md` | `8489ccfb75f951effff4b61a1abe97e4d52001524c6d1ce87192e290e5cb0efb` |
| CA-R-1688 | 24 | `04_requirement/CA-R-1688-CORE_META_MODEL-REQUIREMENT--scope-path-does-not-change-semantic-coordinates.md` | `7b5cf238bd6f1d4f928c6016300c2727440aff2ff5761d4684693a6b8d44deb1` |
| CA-D-301 | 15 | `07_delivery/CA-D-301-CORE_META_MODEL--require-portable-safe-carrier-addresses.md` | `40fa41c8ff9abdd81a39689a3b95284a2240cf567113bbf794fa874b8e61a691` |

No source Atom, Plan Atom, code, MCP, FPF, Git, captured review, or production Subject was edited by preparing this packet.
