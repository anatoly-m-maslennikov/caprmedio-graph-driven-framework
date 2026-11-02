# Definition polishing result

Selected sources: Current Methodology and direct project-local RMED. Engine/code/runtime, Terms Graph implementation, subtype hierarchy and advanced formulas were not migrated.

## Actual result

- Re-read 1,256 Current source Atoms with zero metadata/hash discrepancies.
- The original 337 parsed kind/property paths represent 336 logical entities: the two Notation for subject spellings are one property. All 336 now have exactly one canonical R/Entity Definition. Zero missing or competing owners remain.
- All 33 named Relation Types have one exact R/Relation Definition. The specialized template qualifies without a subtype hierarchy. Main meaning is defined once; counterparts are short references. IS_DEFINED_BY is derived from qualified defining GOVERNS links.
- Published 75 Current successors with 75 predecessor archives, 136 new Entity Definitions, one ownership Rule and eight Relation Definitions (IS_DEFINED_BY and seven existing catalog counterparts). New Atom count: 145.
- Eleven newly governed targets are reported separately from the immutable original cohort; the baseline was not replaced with the newer audit boundary.
- Rebuilt CA-PROJ-014, CA-PROJ-015 and CA-PROJ-016 from the exact 1,256-source version/hash vector and governing-config hashes. IDs remain stable. Definition markers use exact governing Definitions, not supporting Rule/formal mentions.

## Inheritance

`/` specialization reuses the broader Definition and states only differences. `//` instances follow their kind Definition and state instance facts. A Method Atom is an Atom with Content Role Method; it does not repeat the whole Atom Definition. Common properties and constraints are inherited. `>` containment adds no inheritance.

The Entity Definition template (R2227), ownership Rule (R2278), seven Content Role Definitions (R1336–R1342) and proposal A1312 record this. Relation Definition R2228 has one canonical Notation for subject declaration, not two aliases.

## Review and corrections

Reviewed the original 180 unique candidates (124 kinds and 56 properties), the 24 competing groups, all 133 shared/formal raw cases, all 136 new Definitions, seven role successors and the relation counterparts. Bounded Terra semantic reviews and Luna source/ownership checks were followed by actual-source readback.

| Finding | Applied correction |
| --- | --- |
| Rules, references and lexical constraints competing with actual Definitions | Retained their meaning as supporting Rules; exact canonical ownership is explicit. |
| R1359 / Atom.Content and R2149 / Atom.Relations | Kept their constraints separate; supplied actual grouping-property Definitions. |
| R944 / Demand.Target Scope Unit | Preserved the direction rule separately; defined the inherited target property with its authoring/resolved distinction. |
| R1360, R1356 and R1637 governed topics but defined concrete mechanisms | Preserved supporting requirements; supplied concise source-backed Data Transformation, Effect Authorization and UX Entry Definitions. |
| R1569 contradicted the approved Step call model | A leaf Step calls one Action or Workflow; Sub-step calls Action only; composite Step has no own call. |
| Six Rule successors lost Claim conditions | Restored the source conditions without restoring the obsolete Artifact partition. |
| R1947 outdated status-inheritance note | Removed the stale note; Plan/Analysis allowed values remain additive. |
| R2150 called Subject Graph Entity Graph | Corrected the Claim/scope terminology without changing the projection boundary. |
| Four new property Drafts lost source nuance | Preserved parentless Project, stable Projection ID tuple, admitted Projection Types and resolved Plan target semantics. |
| Missing resolved-target headers | Completed the selected Draft headers before promotion. |

## Where dedicated Definitions fit less well

- Inherited role-qualified properties need little or no new meaning. Their short Definitions reuse the base instead of repeating the Atom schema, but separate files still add overhead under this trial.
- Aspect Definitions split concise taxonomy declarations into many small documents. Scoped constraints remain additional Rs, rather than competing Definitions. No additional entities were invented for nuances.
- Map and Hub are admitted nominal Projection Type labels without a declared behavioral distinction. Their Definitions deliberately invent no layout or behavior. A meaningful distinction would need a later Operator decision.
- Some old lexical definitions are useful interpretation Rules rather than model entities. They were preserved as such; this work does not claim to have reviewed every legacy Rule's policy.
- R1368 historically governs derived CONTAINS while documenting the full containment pair. The short IS_CONTAINED_BY Definition points to it and explicitly retains IS_CONTAINED_BY as the stored direct direction. The pair's semantics are not copied into two full Definitions.

## Verification limits

Ownership/metadata/hash readback, selected native target resolution, basic property format/cardinality coverage, prose/formal review, scratch-renderer regressions and projection/source-vector readback passed. The 1,036 native relation references resolve without missing or ambiguous Current IDs. This is not a full runtime test suite or a review of every legacy Rule, Engine Atom or executable consumer. Governing TOML parsed and needed no new values.

The Epic remains Active at the Operator's request.
