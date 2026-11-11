# Named endpoint kinds in Relation Declarations

Current Active native Requirement/Declaration subjects were examined across the pinned role-file scope in `permission-occurrences.json`; draft, archived, staging, analysis and plan directories were excluded. `endpoint-kind-pins.json` pins key declarations and Rules. A Current Declaration is model authority for a kind; a Rule mentioning that kind or a prose name is not. This does not evaluate runtime populations, inheritance closure, endpoint permissions, or parser binding.

| Named endpoint | Current model Declaration | Assessment |
|---|---|---|
| Atom | CA-R-2508 | Declared; specific role/form selections retain their own applicable constraints. |
| Carrier | CA-R-1958 | Declared, distinct branch; do not assume Node. |
| Relation | CA-R-2247 | Declared CFEL descriptor, not an executed predicate or glyph. |
| Plan | CA-R-2511 | Declares `Atom/(.Header.Role := Plan)`; whether bare `Plan//` in R1580 resolves to that selection still requires declared binding evidence. |
| Scope Unit | CA-R-2523 | Declared. |
| Workflow | CA-R-2464 | Declared. |
| Event Record | CA-R-2557 | Declared. |
| Actor | CA-R-2542 | Declared. |
| Step | CA-R-2465 | Declared. |
| Substep | CA-R-2466 | Declared. |
| Action | CA-R-2467 | Declared. |
| Workflow Run | No Current Declaration found in native MODEL source scope | Definite declaration gap in this scanned scope. R2245, R2246 and R2255 name it in prose; R1520/R1525 are Rules on an older path, not Declarations. Their existence does not establish the kind or its runtime instances. |
| Runtime | No Current Declaration found in native MODEL source scope | Definite declaration gap in this scanned scope. R2255 names it in prose; `$runtime` is untyped, not a declared Runtime kind or evidence that any exist. |
| Execution | No Current Declaration found in native MODEL source scope | Definite declaration gap in this scanned scope. R1528 is a Rule on an older Execution path, not a Declaration; R2245/R2246 use execution semantically. Do not infer a specific missing kind for every use of the ordinary word. |
| Event | No Current Declaration found in native MODEL source scope | R2246 describes an actual Event or execution as a possible RECORDS target, but its target is `$occurrence`. The missing declaration is distinct from an empty population; whether Event must be a distinct model kind needs a decision. |

R1639, R1654, R1660, R2473, R2475, R2476 and similar declarations use untyped endpoint variables with semantic prose. Their unresolved selected populations remain diagnostics: neither their variable names nor ordinary words such as Artifact, Property, kind, represented-content version or occurrence create kinds, prove kind absence, or prove a link. Inverse declarations inherit the direct counterpart's domain, but that does not supply a missing kind or a permission.

No new definitions, retirement proposals or runtime-instance assertions are made here. Workflow execution and Workflow Purpose changes are owned separately; resolve their source decisions before changing these endpoints.
