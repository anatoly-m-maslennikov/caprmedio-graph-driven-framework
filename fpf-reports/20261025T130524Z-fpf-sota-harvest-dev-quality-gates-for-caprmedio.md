## Task, scope, and boundaries

**Yes. The strongest opportunity is to enforce checks we already have, then add narrowly scoped document/config checks.**

| Format | Useful adoption | Existing coverage / limit |
|---|---|---|
| **Python** | Connect pinned Ruff/mypy to the intended developer/release or PR route. | Already configured; no automatic switch to ty. |
| **Markdown** | Pilot read-only `rumdl check` on ordinary docs. | Style checks supplement Atom/CCE validation. |
| **YAML, TOML, JSON** | `check-jsonschema` for a specific uncovered config with an owned schema. | Existing Atom/frontmatter validators stay authoritative. |
| **All formats** | Same pinned commands locally/CI; prove each gate rejects a known violation. | Reuse uv/project tooling; no new hook/tool-manager stack needed. |

This approved source harvest supports Anatoly’s adoption decision. It compared the pinned catalogue, primary tool docs and current CAPRMEDIO configuration/code on **25 October 2026**. No installation, implementation, configuration change, gate execution or autofix occurred. **1/1 COMPLETE**; profile none, no composition/suffix. Recommendations are proposals, not adoption decisions.

Saved report: `fpf-reports/20261025T130524Z-fpf-sota-harvest-dev-quality-gates-for-caprmedio.md` ([open report](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/fpf-reports/20261025T130524Z-fpf-sota-harvest-dev-quality-gates-for-caprmedio.md)).

## Issues, weak points, and improvements

### Native result

**Contract DQ-CA-1:** find useful, nonduplicative checks for Python, documents and config. Admit primary docs/config/code; distinguish configured, invoked and successfully executed. Exclude exhaustive audits, global reformatting and semantic-pass claims.

**The main local finding:** [pyproject.toml](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/pyproject.toml:27) already pins Ruff **0.16.8** and mypy **2.3.1**, with selected Ruff rules and a strict bounded mypy file list. No Ruff/mypy invocation was found in the inspected tracked release/CI paths. The [release phase](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/PROJECT_TOOLS/RELEASE_VERSION/local_release.py:528) already runs comprehensive tests; the [PR workflow](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.github/workflows/dev-to-main-policy.yml:22) enforces branch/owner policy. This establishes a wiring opportunity, not whether either checker currently passes.

**MD/YAML validation is already substantial.** [VALIDATE_ATOMS](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/VALIDATE_ATOMS/validate_atoms_workers/parsing.py:26) rejects aliases, merge/duplicate keys, bounds YAML resources and requires a mapping. Its [schema checks](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/VALIDATE_ATOMS/validate_atoms_workers/check_schema_extended.py:150) enforce authority-backed properties. [Project Structure](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/project_structure.toml:86) separates strict sources, delivered carriers and projections. Generic formatters must not redefine those contracts or rewrite Claims/identities indiscriminately.

**CorpusLedger CL-DQ-1** — all rows included for these bounded purposes; mutable tool docs were observed on the harvest date, not release-pinned.

| ID | Edition and evidence | Used for |
|---|---|---|
| A | Catalogue [75b8b400c2bb7c363522923740ecfc5eb719c5a8](https://github.com/mokevnin/dev-quality-gates/tree/75b8b400c2bb7c363522923740ecfc5eb719c5a8): registry/README, [adoption](https://github.com/mokevnin/dev-quality-gates/blob/75b8b400c2bb7c363522923740ecfc5eb719c5a8/docs/adopt.md), [patterns](https://github.com/mokevnin/dev-quality-gates/blob/75b8b400c2bb7c363522923740ecfc5eb719c5a8/docs/patterns.md) | Actual coverage, process and limits. |
| B | [Ruff](https://docs.astral.sh/ruff/linter/), [formatter](https://docs.astral.sh/ruff/formatter/), [ty policy](https://github.com/astral-sh/ty/blob/main/README.md), [deptry](https://deptry.com/rules-violations/), [import-linter](https://import-linter.readthedocs.io/en/stable/contract_types/) | Python roles and limits. |
| C | [rumdl CLI](https://rumdl.dev/usage/cli/), [schema usage](https://check-jsonschema.readthedocs.io/en/latest/usage.html), [TOML support](https://check-jsonschema.readthedocs.io/en/latest/optional_parsers.html#toml), [yamllint](https://yamllint.readthedocs.io/en/stable/) | Style/schema distinctions. |
| D | Local files above; [runner](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/PROJECT_TOOLS/run_full_test_suite.py:17), [manual WSL workflow](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.github/workflows/wsl-proof.yml:3) | Receiving baseline; cleanliness/live status unverified. |

**FR-DQ-1:** catalogue → recommendation/research/adoption material → promising primary docs → receiving code/config. Parked unrelated languages and broad security/coverage migrations. No tracked quality Git hook was found; external/untracked hooks were outside scope. Codex’s context hook protects a different boundary.

**ClaimSheets:** CS-L = language/static diagnostics (A/B/D, implementation code); CS-T = document-surface checks (A/C/D, Markdown representation); CS-S = schema validation (A/C/D, parsed config). Their comparison basis is diagnostic coverage for adoption planning. Tool capabilities are source claims; local fit is reviewer interpretation; acceptance remains the Project’s decision.

**HP-DQ-1 / CJ-DQ-1:** count inspected methods by their principal checking contract, merging repeated tools/versions/citations within language-aware analysis, document linting, or schema validation. Process orchestration adds no checker family. Count **3**, floor **k=3**, met for this bounded purpose; three materially distinct claim regions and multiple lineages are retained. **SET-DQ-1 / PAL-DQ-1** comprise CS-L/T/S, sources, limits and examples. No exhaustive coverage, distance gate, scalar rank, atlas, fusion or substitution is asserted.

**Important limits:** keep mypy; ty remains beta and the catalogue’s research notes disagree with its preferred checker. Deptry/import-linter are conditional leads for a demonstrated dependency/import-boundary problem, not established gaps; dynamic/plugin imports limit static coverage. Ruff formatting needs its own explicit command/policy. [Python primary docs, B](https://docs.astral.sh/ruff/formatter/)

Use `rumdl check` for gating: `fmt` can succeed with unfixable violations remaining. Check-jsonschema validates instances against JSON Schema, not TOML formatting or Claim meaning; remote schemas need controlled inputs. **Yamllint remains under review in the catalogue**, despite research notes suggesting it for style. [rumdl](https://rumdl.dev/usage/cli/), [schema docs](https://check-jsonschema.readthedocs.io/en/latest/usage.html), [catalogue](https://github.com/mokevnin/dev-quality-gates/blob/75b8b400c2bb7c363522923740ecfc5eb719c5a8/README.md)

The portable process is explicit file scope, shared pinned commands, useful diagnostics and a controlled failing fixture. Separate quick offline checks from expensive/network checks; preserve same-job tools before adding dependencies. [Adoption/patterns, A](https://github.com/mokevnin/dev-quality-gates/blob/75b8b400c2bb7c363522923740ecfc5eb719c5a8/docs/adopt.md)

**INV-DQ-1:** diagnostic/schema/source-scope objects and lint/validate/invoke operations are **stubs; typing/integration TBD**. No public IDs/thresholds minted. **ME-DQ-1** gives illustrative future checks, assurance tag **none**; no achieved TA/VA/LA:

| Family / evidence | Two substrates |
|---|---|
| CS-L, B/D | Undefined Python name fails; CI YAML wrapper propagates that failure. |
| CS-T, C/D | Disposable README violation fails; frozen Atom retains identity/Claim and existing-parser validity after a separately authorized formatting proposal. |
| CS-S, C/D | Schema-forbidden YAML key fails; equivalent invalid TOML instance fails. |

Branches: selected/unselected file; clean/violation/tool-error; valid/invalid/unknown-schema. Existing definitions govern acceptance. **HO-DQ-1** supplies CS/INV/ME to possible evaluation/design/registry work; none started. Refresh causes: `RSCRTriggerKindId.EditionPinChange`, `EvidenceSurfaceEdit`, `PolicyPinChange`, `BaselineBindingEdit` (same prefix).

### Issue registry

- **I1:** configured Ruff/mypy may not be enforced. Evidence: config versus inspected release/CI calls; target: tracked execution routes. Consequence: rules without a demonstrated gate. Confidence **high**, bounded source finding; live/untracked routes unknown. **OPEN → F1**.
- **I2:** generic validity could be mistaken for authoritative-content correctness. Evidence: existing contracts versus C’s narrower checks; target: MD/config/derived carriers. Consequence: duplicate rules, unintended edits or false acceptance. Confidence **high** in this boundary; no offending adoption observed. **OPEN → F2/F3**.
- **I3:** replacements could add cost/noise without value. Evidence: A’s research conflicts, B/C limits and existing tools; target: checker/tool-manager additions. Confidence **high** in risk basis, local burden unmeasured. Consequence: maintenance/migration/false positives. **OPEN → F1–F3**.

### Fix and improvement register

All **PROPOSED**, owner **Anatoly**; trials/configuration changes require separate authorization.

- **F1**, I1/I3, **required prerequisite**, **preferred**: first select the fast-check boundary and connect existing pinned Ruff/mypy through current tooling. Expected enforcement; cost: findings/check time. Independent confidence **high**, A/B/D. Verify clean/failure/tool-error cases, file coverage and exit propagation; preserve comprehensive release tests.
- **F2**, I2/I3, **complementary**, **preferred**: after scope selection, pilot check-only rumdl on ordinary docs; extend to Atoms only with explicit dialect/rules/exclusions and existing-validator comparison. Expected Markdown consistency; cost: style noise/rule upkeep. Confidence **medium-high**, C/D. Verify violations fail, exclusions hold and Claim/identity content is unchanged.
- **F3**, I2/I3, **complementary**, **acceptable**: first identify one uncovered config and governing schema, then consider check-jsonschema. Deptry/import-linter are alternatives only for a separately demonstrated gap. Expected targeted coverage; cost: schemas/exceptions/dependencies. Confidence **medium**, A–D capabilities, need unproved. Verify valid/invalid fixtures, deterministic schema inputs and exact coverage before blocking adoption.

## Unresolved evidence gaps

- **G1 → I1/F1:** wiring inspected, live outcomes/hooks/history unchecked. No pass/fail claim; next evidence is an authorized scoped run plus controlled failure.
- **G2 → I2/I3, F2/F3:** local noise, dialect compatibility and uncovered config need unknown. Next: representative frozen fixtures compared with existing validators.
- **G3 → I3/F3:** dynamic imports/schema ownership not exhaustively audited. Next: name a concrete unwanted case and demonstrate current coverage before a specialized trial.

## Skills used

1. `$fpf sota harvest` — approved source harvest only.

### FPF sources consulted (2 read; 2 used)

Edition `fb3b6a4ad1d51d732a365f75f7d68337c7a751e2`, generated 25 October 2026; IDs verified through its index.

- **Used:** `FPF-Knowledge-Graph/G_Discipline SoTA Patterns Kit/03_02_Harvest and Synthesize SoTA for a CG-Frame/00_G.02 - Harvest and Synthesize SoTA for a CG-Frame.md` — Problem frame/Problem/Forces, Solution §§4.1–4.4/4.6–4.7, coverage example, conformance, Consequences; extensions unused.
- **Used:** `FPF-Knowledge-Graph/G_Discipline SoTA Patterns Kit/00_Core_Discipline SoTA Kit Invariants, Defaults and Refresh Triggers (Part G)/00_G.Core - Discipline SoTA Kit Invariants, Defaults and Refresh Triggers (Part G).md` — Problem frame/Problem/Forces, relevant linkage/profile/pin/trigger/ID/non-goal sections, Consequences; bounded inspection.

No quality tools, tests, gates or fixers ran; analyzed files were unchanged. Compatibility, runtime behavior and false-positive rates remain unverified.

<oai-mem-citation>
<citation_entries>
MEMORY.md:2-2|note=[Kept source authority and observed implementation distinct]
</citation_entries>
<rollout_ids>
</rollout_ids>
</oai-mem-citation>
