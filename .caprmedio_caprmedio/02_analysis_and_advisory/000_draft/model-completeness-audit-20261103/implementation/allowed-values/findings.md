# Model allowed-value list audit

## Result

The pinned frontier contains 1,148 sources, and every source hash matches. The scan found 56 lines with likely parenthesized enumerations; after classifying lists, nested field names, syntax examples, contextual filters, and conditions, the only high-confidence duplicate of individually declared values was the Atom Header Role enumeration in CA-R-1283. That enumeration is already removed in version 33; the current Rule delegates admission to the applicable Role Declaration. The eight individual Role Declarations cover Concern, Analysis & Advisory, Plan, Requirement, Method, Evaluation, Delivery, and Operations.

No further source repair is indicated by this audit. The remaining lists either lack per-value Declarations, state a contextual subset/minimum, describe a format or process sequence, or define structural child names. Preserve them pending any separate authority decision.

## Exact comparisons

- **Resolved duplicate — CA-R-1283 v33**, `Atom.Header.Role`: prior values were Concern, Analysis & Advisory, Plan, Requirement, Method, Evaluation, Delivery, Operations. Current claim no longer lists them; it says each value must be admitted by its applicable Role Declaration. Exact declarations: CA-R-2509 (Concern), CA-R-2637 (Analysis & Advisory), CA-R-2511 (Plan), CA-R-2512 (Requirement), CA-R-2513 (Method), CA-R-2514 (Evaluation), CA-R-2515 (Delivery), CA-R-2463 (Operations).
- **Status domains** — CA-R-1947, 1309, 1397–1399, 1874, 1539, 1608, 1875: the base/admitted and additive values have no individual Status-value Declarations in the frontier. Preserve pending a distinct user decision.
- **Other unbacked domains** — CA-R-2156 Actor Type (Operator, AI Agent); CA-R-1405 Artifact Type (Atom, Journal, Projection, Project Settings, Framework Instance Settings, Default Settings); CA-R-1628 reporting mode (silent, verbose); CA-R-1630 strictness (medium, high); CA-R-1632 impact disposition (compatible, update_required, replacement_required, uncertain); CA-R-1643 observation category (Started, Progressed, Completed, Failed, Interrupted, Abandoned, Recovered); CA-R-1430 and CA-R-2633/2634 Authority Mode (strict, casual). No exact per-value Declarations were found; preserve.
- **Not duplicate domains** — CA-R-1276 is a use-specific Relation Kind whitelist (GOVERNS, DEPENDS_ON); CA-R-924 is a qualified type selection list. CA-R-1565 says Operations Forms must *include* Action, Workflow, Step, and corresponding Type Declarations exist (CA-R-2467, CA-R-2464, CA-R-2465); this is a minimum-set requirement, not an exhaustive allowed-value list.
- **Format/semantics** — CA-R-2248's provisional scalar vocabulary (bool, datetime, decimal, float, int, string) has corresponding Format subtype Declarations CA-R-2249–2254, not exact Data Type value Declarations, and is expressly provisional. CA-R-2249 true/false describes Boolean semantics. Preserve.
- **Role subsets** — CA-R-1548, 1676, 1315, 1707, 1702, 1648 and CA-M-455 overlap individual Role Declarations, but each names a contextual subset, obligation boundary, or process sequence rather than the full allowed Role domain. R-1702 also includes “Implementation,” which is not a Role. Preserve their contextual meaning.

The machine-readable report records source IDs, paths, pinned versions and hashes, available source line/excerpt, values, matching Declaration IDs, coverage, and disposition. It also records excluded structural/nested-property name lists and generic syntax examples.
