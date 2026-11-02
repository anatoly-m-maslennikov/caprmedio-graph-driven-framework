---
atom_id: CA-A-1239@1-draft
content_role: Analysis
type: Specification Proposal
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
subjects:
  governs: Model
tier: 3
status: Draft
author: Anatoly Maslennikov
version: 1
updated_at: 2026-10-29 05:35:13 +0400
relations: {}
---
# Summary

Model draft: primary kinds and properties

## Status and scope

Review Draft extending Candidate #12 (CA-A-1238). The latest Operator naming decision is Model, replacing the earlier name Formal Model. Prepared selectors use Model::...; Current sources are not migrated by this proposal. Its five base branches are Continuant, Occurrent, Aspect, Carrier and Graph Syntax. Relation and value Format are grouped under Graph Syntax. Structural constraints belong to model Definition Claims, not a separate Graph Rule branch or instance population. Project Model is only an optional organizational view, not a base classification.

This Draft contains the primary tree, then one flat property block for every selected primary kind with known direct or inherited properties, in the same declaration order as the tree. It includes no named instances. It does not promote Drafts, migrate Current Atoms, rename YAML fields or change code. Terms Graph work and the function proposals in CA-A-1237 remain deferred.

Each property block shows its proposed full `subjects.governs` selector. These describe the proposed governing targets; they are not claims that existing source Atom headers already use the new paths. Inline cardinality/format annotations belong to Claims, not to these selectors.

## Reading the annotations

- `/` specializes; `::` groups; `>` contains, and each contained part belongs to exactly one whole; `@(...)` refers to an existing declaration. `((RELATION_TYPE))` names a defined Relation without a short operator. Only actual specialization carries inherited properties.
- `[int]`, `[string]`, `[bool]`, `[datetime]`, `[decimal]` and `[float]` name proposed value formats. Format is for value types only. List and map are carrier structures, not value Formats; child paths define nesting under CA-A-1283 and CA-A-1286. Carrier.Format continues to describe representation formats; Markdown/YAML/TOML/JSON are not placed under this new Format branch.
- General formula and function-style expressions are deferred to CA-A-1282. Existing-kind `@(...)` references remain; general property-value interpolation and executable composition do not enter this syntax increment. A1291 remains a separate bracketed-condition proposal, excluded from this review under A1297.
- Cardinalities under CA-A-1280: `{n}` means exactly n; `{n+}` means at least n without an upper bound; `{n..m}` is an inclusive range. Bounds are non-negative integers with n <= m. Common forms are `{0}`, `{1}`, `{0+}`, `{1+}` and `{0..1}`. A property suffix counts only its own direct values, never nested keys or child values; explicit `{0}` permits a grouping path with independently counted children; `>{1+}` and `>{0+}` count immediate parts per whole. Omitted counts remain unspecified; explicit `{0}` is used for grouping properties. No parser implementation is claimed.
- `[inherited]` marks actual specialization inheritance. Grouping and containment do not supply it. A local additive Status declaration retains inherited values.
- Omitted format or cardinality is undefined in this declaration. In particular, subjects without a suffix is not subjects{0}, subjects{1} or subjects{0+}. Explicit counts remain distinct; independently applicable rules still apply. CA-A-1284 records this distinction. Definition and rule references use Atom IDs only; no definition text is copied into the tree.
- Format annotations are proposed readable constraints unless a cited rule explicitly specifies the datatype. CA-A-1287 removes ref as a value Format. Reference-valued identifiers use string; their definitions preserve target meanings such as Actor, Scope Unit, Operator and Project. Existing-kind @ references are separate syntax and remain admitted.
- Base counts describe the complete-Atom contract, with the Claim structure in CA-A-1243 and the R-only formalization scope in CA-A-1244. Every complete RMED Atom has content.claim{1}. Only R admits an optional content.claim.formal_claim{0..1} child, alongside its mandatory direct prose. The formal child cannot satisfy the prose count. M/E/D keep prose Claims. The Role/Type defines what forms one complete Claim. No separate atom.claim/formal_claim or content.claim.prose field is used. Drafts may be incomplete. Project Goal ownership remains exceptional. Effective Label is required, but its stored explicit value is optional and falls back to Type.

## Primary kinds

```text
Model [Definition Draft]
	::CAPRMEDIO [CA-R-2206]
		::Continuant [CA-R-1967]
			/Actor [CA-R-2218]
				/AI Agent [CA-R-1959]
				/Operator [CA-R-1422]
			/Governing Objects [Definition Draft]
				/Atom [CA-R-655]
					/Content Role: Analysis [CA-R-1337]
						/Type: Analysis Report [CA-R-1232; successor Draft]
						/Type: Rationale [CA-R-1705]
						/Type: Spec Proposal [CA-R-2219; successor Draft]
					/Content Role: Concern [CA-R-1336]
						/Type: Problem [CA-R-1231; successor Draft]
						/Type: Bug [CA-R-1231; successor Draft]
						/Type: Risk [CA-R-1231; successor Draft]
						/Type: Opportunity [CA-R-1231; successor Draft]
					/Content Role: Delivery [CA-R-1342]
					/Content Role: Evaluation [CA-R-1341]
						/Type: Eval Policy [CA-R-2115; successor Draft]
						/Type: Eval Case [CA-R-2116]
					/Content Role: Method [CA-R-1340]
						/Type: Eng Policy [CA-R-2119]
						/Type: Eng Decision [CA-R-2120]
					/Content Role: Operations [CA-R-1530]
						/Type: Action [CA-R-1452]
						/Type: Workflow [CA-R-1508]
							>{1+}Step [CA-R-1509; successor Draft]
								>{0+}Substep [new Definition Draft; ID pending]
					/Content Role: Plan [CA-R-1338]
						>@(Model::CAPRMEDIO::Continuant/Governing Objects/Atom/Content Role: Plan)
					/Content Role: Requirement [CA-R-1339]
						/Type: Requirement [Definition Draft]
						/Type: Demand [CA-R-932]
						/Type: Definition [CA-R-2110; successor Draft]
						/Type: Project Goal [CA-R-2152]
				/Governing Configuration [CA-R-1962]
			/History [CA-R-1961]
				/Journal [CA-R-1745]
					>Event Record [Definition Draft; numeric ID pending]
				/Release [CA-R-2171]
			/Package [CA-R-2178; successor Draft]
				/Project Implementation [Definition Draft]
					>@(Package)
				/Runtime Package [Definition Draft]
				/Eval Package [Definition Draft]
					>@(Module)
					>@(Prompt)
				>@(Package)
				>Module [CA-R-2177; successor Draft]
					>Code Unit [Definition Draft]
						/Class [CA-R-2176]
						/Function [CA-R-2175]
				>Prompt [CA-R-2179; successor Draft]
				>Asset [Definition Draft]
					/Configuration [CA-R-2190; successor Draft]
					/Schema [CA-R-2191; successor Draft]
					/Template [CA-R-2192; successor Draft]
					/Test Fixture [CA-R-2193; successor Draft]
				>Documentation [CA-R-2180]
					/Code Block [CA-R-2187]
					/Diagram [CA-R-2188]
					/Document [CA-R-2181]
						>Section [CA-R-2182]
							>@(Section)
					/List [CA-R-2185]
					/Paragraph [CA-R-2183]
					/@(Section)
					/Sentence [CA-R-2184]
					/Table [CA-R-2186]
			/Structural Unit [Definition Draft]
				/Scope Unit [CA-R-1757]
					>@(Atom)
					>@(Projection)
					>@(Scope Unit)
					/Project [CA-R-2220]
						>@(Scope Unit)
			/Projection [CA-R-1746]
				/Terms Projection [Definition Draft]
			/Selection [CA-R-1966]
			/Term [CA-R-1318]
		::Occurrent [CA-R-1972]
			/Event [CA-R-1968]
			/Execution [CA-R-1970]
				/Action Run [CA-R-1969]
				/Container Run [CA-R-2195]
				/Process Run [CA-R-2196]
				/Step Run [CA-R-1511]
				/Workflow Run [CA-R-1510]
			/Runtime [CA-R-2194]
			/Session [CA-R-1971]
		::Aspect [CA-R-2210]
			::Design [CA-R-2216]
			::Documentation Aspect [CA-R-2217]
				::@(Traceability)
			::Domain [CA-R-2213]
			::Engineering [CA-R-2214]
				::Architecture
					::Communication
						::API [Definition Draft]
							::Result Contract [Definition Draft]
							::Self Documentation [Definition Draft]
					::Component Structure
				::Authoring
					::Code Authoring
						::Python Code Authoring
					::Controlled English
					::Prompt Authoring
				::Data Handling
					::Data Transformation
					::Data Validation
					::Output Publication
					::Parsing
					::Serialization
					::Source Retrieval
					::Source Selection
				::Delivery
					::Extension Lifecycle
					::Git Commits
				::Execution Control
					::Decision Confidence
					::Effect Authorization
					::Failure Handling
					::Recovery
				::Observability
					::Logging
					::Monitoring
				::Storage
					::Directory Layout
				::Traceability
				::Verification
					::Coverage
					::Dynamic Testing
					::Static Analysis
						::Python Static Analysis
					::Test Data
						::Golden Corpora
					::Test Design
			::Product [CA-R-2211]
			::Project Aspect [CA-R-2212]
			::UX [CA-R-2215]
				::Discovery and Navigation
				::Entry
				::Guidance
				::Interaction
					::Accessibility
					::Decision
				::Result and Status Presentation
		::Carrier [CA-R-1958]
			/Database [CA-R-1955]
			/Directory [CA-R-1956]
			/Docker Image [CA-R-2198]
			/File [CA-R-1957]
			/Git Branch [CA-R-2200]
			/Git Commit [CA-R-2199]
			/Git Index [CA-R-2202]
			/Git Repository [CA-R-2203]
				>@(Git Branch)
			/Pull Request [CA-R-2201]
		::Graph Syntax [Definition Draft]
			::Relation [Definition Draft; replaces CA-R-1963]
			::Format [Definition Draft]
				/bool [value-type definition pending]
				/datetime [value-type definition pending]
				/decimal [value-type definition pending]
				/float [value-type definition pending]
				/int [value-type definition pending]
				/string [value-type definition pending]
	::caprmedio [CA-R-2207; project namespace, no instances expanded]
```

## Retired umbrella

Resources is removed under CA-A-1278. Its useful non-executable runtime/evaluation Configuration, Schema, Template and Test Fixture kinds specialize Asset. Executable LLM instructions are Prompts; explanatory/reference content is Documentation. Governing Configuration remains separate. R2189 is a retirement candidate; Current sources are unchanged.

## Properties by primary kind

Only kinds with at least one supported direct or inherited property appear below. The selected qualified Types expose important exceptions; this is not an assertion that the complete Type catalog has been shown.

### Actor

```yaml
subjects:
  governs: 'Model::CAPRMEDIO::Continuant/Actor'
```

```text
Actor
	.Name[string]{0..1} [CA-R-1944]
```

### AI Agent

```yaml
subjects:
  governs: 'Model::CAPRMEDIO::Continuant/Actor/AI Agent'
```

```text
AI Agent
	.Name[string]{0..1} [CA-R-1944] [inherited]
	.Permissions [CA-R-1552]
```

### Operator

```yaml
subjects:
  governs: 'Model::CAPRMEDIO::Continuant/Actor/Operator'
```

```text
Operator
	.Name[string]{0..1} [CA-R-1944] [inherited]
```

### Atom

```yaml
subjects:
  governs: 'Model::CAPRMEDIO::Continuant/Governing Objects/Atom'
```

```text
Atom
	.Author[string]{1} [CA-R-2102]
	.content{0} [CA-R-1359]
		.details[string]{0..1} [CA-R-2102; CA-R-1624]
		.scope[string]{0..1} [CA-R-2102; CA-R-2160]
		.semantics[string]{0..1} [CA-R-2102; CA-R-1946]
		.summary[string]{1} [CA-R-2102; CA-R-1465]
	.Content Role[string]{1} [CA-R-1283; CA-R-2102]
		:Analysis
		:Concern
		:Delivery
		:Evaluation
		:Method
		:Operations
		:Plan
		:Requirement
	.Enabled Relations{0}
		.Contains[bool] [CA-R-1945] [kind-level capability]
			:False
			:True
	.id[string]{1} [CA-R-728; CA-R-2102]
	.Label[string]{0..1} [CA-R-1594; CA-R-2102]
	.Local Scope Unit[string]{1} [CA-R-920; CA-R-2102]
	.Relations{0} [CA-R-2102]
	.Status[string]{1} [CA-R-1412; CA-R-1947; CA-R-2102]
		:Active
		:Archived
		:Draft
	.Subjects{0} [CA-R-1198; CA-R-2102]
		.Depends On[string]{0+} [CA-R-1198]
		.Governs[string]{1} [CA-R-1363]
	.Target Scope Unit[string]{0..1} [CA-R-1595; CA-R-2102]
	.Tier[int]{1} [CA-R-2124; CA-R-2125; CA-R-2102]
	.Type[string]{1} [CA-R-2102]
	.Updated At[datetime]{1} [CA-R-1416; CA-R-2102]
	.version_number[int]{1} [CA-R-1415; CA-R-2102]
```

### Atom/Content Role: Analysis

```yaml
subjects:
  governs: 'Model::CAPRMEDIO::Continuant/Governing Objects/Atom/Content Role: Analysis'
```

```text
Atom/Content Role: Analysis
	.Author[string]{1} [CA-R-2102] [inherited]
	.content{0} [CA-R-1359] [inherited]
		.analysis[string] [CA-R-2102]
		.details[string]{0..1} [CA-R-2102; CA-R-1624] [inherited]
		.question[string] [CA-R-2102]
		.scope[string]{0..1} [CA-R-2102; CA-R-2160] [inherited]
		.semantics[string]{0..1} [CA-R-2102; CA-R-1946] [inherited]
		.summary[string]{1} [CA-R-2102; CA-R-1465] [inherited]
	.Content Role[string]{1} [CA-R-1283; CA-R-2102] [inherited]
		:Analysis [inherited]
	.Enabled Relations{0} [inherited]
		.Contains[bool] [CA-R-1945] [inherited] [kind-level capability]
			:False [inherited]
			:True [inherited]
	.id[string]{1} [CA-R-728; CA-R-2102] [inherited]
	.Label[string]{0..1} [CA-R-1594; CA-R-2102] [inherited]
	.Local Scope Unit[string]{1} [CA-R-920; CA-R-2102] [inherited]
	.Relations{0} [CA-R-2102] [inherited]
	.Status[string]{1} [CA-R-1412; CA-R-1947; CA-R-2102] [inherited]
		:Active [inherited]
		:Archived [inherited]
		:Draft [inherited]
	.Subjects{0} [CA-R-1198; CA-R-2102] [inherited]
		.Depends On[string]{0+} [CA-R-1198] [inherited]
		.Governs[string]{1} [CA-R-1363] [inherited]
	.Target Scope Unit[string]{0..1} [CA-R-1595; CA-R-2102] [inherited]
	.Tier[int]{1} [CA-R-2124; CA-R-2125; CA-R-2102] [inherited]
	.Type[string]{1} [CA-R-2102] [inherited]
	.Updated At[datetime]{1} [CA-R-1416; CA-R-2102] [inherited]
	.version_number[int]{1} [CA-R-1415; CA-R-2102] [inherited]
```

### Atom/Content Role: Analysis/Type: Analysis Report

```yaml
subjects:
  governs: 'Model::CAPRMEDIO::Continuant/Governing Objects/Atom/Content Role: Analysis/Type: Analysis Report'
```

```text
Atom/Content Role: Analysis/Type: Analysis Report
	.Author[string]{1} [CA-R-2102] [inherited]
	.content{0} [CA-R-1359] [inherited]
		.analysis[string] [CA-R-2102] [inherited]
		.details[string]{0..1} [CA-R-2102; CA-R-1624] [inherited]
		.question[string] [CA-R-2102] [inherited]
		.scope[string]{0..1} [CA-R-2102; CA-R-2160] [inherited]
		.semantics[string]{0..1} [CA-R-2102; CA-R-1946] [inherited]
		.summary[string]{1} [CA-R-2102; CA-R-1465] [inherited]
	.Content Role[string]{1} [CA-R-1283; CA-R-2102] [inherited]
		:Analysis [inherited]
	.Enabled Relations{0} [inherited]
		.Contains[bool] [CA-R-1945] [inherited] [kind-level capability]
			:False [inherited]
			:True [inherited]
	.id[string]{1} [CA-R-728; CA-R-2102] [inherited]
	.Label[string]{0..1} [CA-R-1594; CA-R-2102] [inherited]
	.Local Scope Unit[string]{1} [CA-R-920; CA-R-2102] [inherited]
	.Relations{0} [CA-R-2102] [inherited]
	.Status[string]{1} [CA-R-1412; CA-R-1947; CA-R-2102] [inherited]
		:Active [inherited]
		:Archived [inherited]
		:Draft [inherited]
	.Subjects{0} [CA-R-1198; CA-R-2102] [inherited]
		.Depends On[string]{0+} [CA-R-1198] [inherited]
		.Governs[string]{1} [CA-R-1363] [inherited]
	.Target Scope Unit[string]{0..1} [CA-R-1595; CA-R-2102] [inherited]
	.Tier[int]{1} [CA-R-2124; CA-R-2125; CA-R-2102] [inherited]
	.Type[string]{1} [CA-R-2102] [inherited]
		:Analysis Report
	.Updated At[datetime]{1} [CA-R-1416; CA-R-2102] [inherited]
	.version_number[int]{1} [CA-R-1415; CA-R-2102] [inherited]
```

### Atom/Content Role: Analysis/Type: Rationale

```yaml
subjects:
  governs: 'Model::CAPRMEDIO::Continuant/Governing Objects/Atom/Content Role: Analysis/Type: Rationale'
```

```text
Atom/Content Role: Analysis/Type: Rationale
	.Author[string]{1} [CA-R-2102] [inherited]
	.content{0} [CA-R-1359] [inherited]
		.analysis[string] [CA-R-2102] [inherited]
		.details[string]{0..1} [CA-R-2102; CA-R-1624] [inherited]
		.question[string] [CA-R-2102] [inherited]
		.scope[string]{0..1} [CA-R-2102; CA-R-2160] [inherited]
		.semantics[string]{0..1} [CA-R-2102; CA-R-1946] [inherited]
		.summary[string]{1} [CA-R-2102; CA-R-1465] [inherited]
	.Content Role[string]{1} [CA-R-1283; CA-R-2102] [inherited]
		:Analysis [inherited]
	.Enabled Relations{0} [inherited]
		.Contains[bool] [CA-R-1945] [inherited] [kind-level capability]
			:False [inherited]
			:True [inherited]
	.id[string]{1} [CA-R-728; CA-R-2102] [inherited]
	.Label[string]{0..1} [CA-R-1594; CA-R-2102] [inherited]
	.Local Scope Unit[string]{1} [CA-R-920; CA-R-2102] [inherited]
	.Relations{0} [CA-R-2102] [inherited]
	.Status[string]{1} [CA-R-1412; CA-R-1947; CA-R-2102] [inherited]
		:Active [inherited]
		:Archived [inherited]
		:Draft [inherited]
	.Subjects{0} [CA-R-1198; CA-R-2102] [inherited]
		.Depends On[string]{0+} [CA-R-1198] [inherited]
		.Governs[string]{1} [CA-R-1363] [inherited]
	.Target Scope Unit[string]{0..1} [CA-R-1595; CA-R-2102] [inherited]
	.Tier[int]{1} [CA-R-2124; CA-R-2125; CA-R-2102] [inherited]
	.Type[string]{1} [CA-R-2102] [inherited]
		:Rationale
	.Updated At[datetime]{1} [CA-R-1416; CA-R-2102] [inherited]
	.version_number[int]{1} [CA-R-1415; CA-R-2102] [inherited]
```

### Atom/Content Role: Analysis/Type: Spec Proposal

```yaml
subjects:
  governs: 'Model::CAPRMEDIO::Continuant/Governing Objects/Atom/Content Role: Analysis/Type: Spec Proposal'
```

```text
Atom/Content Role: Analysis/Type: Spec Proposal
	.Author[string]{1} [CA-R-2102] [inherited]
	.content{0} [CA-R-1359] [inherited]
		.analysis[string] [CA-R-2102] [inherited]
		.details[string]{0..1} [CA-R-2102; CA-R-1624] [inherited]
		.question[string] [CA-R-2102] [inherited]
		.scope[string]{0..1} [CA-R-2102; CA-R-2160] [inherited]
		.semantics[string]{0..1} [CA-R-2102; CA-R-1946] [inherited]
		.summary[string]{1} [CA-R-2102; CA-R-1465] [inherited]
	.Content Role[string]{1} [CA-R-1283; CA-R-2102] [inherited]
		:Analysis [inherited]
	.Enabled Relations{0} [inherited]
		.Contains[bool] [CA-R-1945] [inherited] [kind-level capability]
			:False [inherited]
			:True [inherited]
	.id[string]{1} [CA-R-728; CA-R-2102] [inherited]
	.Label[string]{0..1} [CA-R-1594; CA-R-2102] [inherited]
	.Local Scope Unit[string]{1} [CA-R-920; CA-R-2102] [inherited]
	.Relations{0} [CA-R-2102] [inherited]
	.Status[string]{1} [CA-R-1412; CA-R-1947; CA-R-2102] [inherited]
		:Active [inherited]
		:Archived [inherited]
		:Draft [inherited]
	.Subjects{0} [CA-R-1198; CA-R-2102] [inherited]
		.Depends On[string]{0+} [CA-R-1198] [inherited]
		.Governs[string]{1} [CA-R-1363] [inherited]
	.Target Scope Unit[string]{0..1} [CA-R-1595; CA-R-2102] [inherited]
	.Tier[int]{1} [CA-R-2124; CA-R-2125; CA-R-2102] [inherited]
	.Type[string]{1} [CA-R-2102] [inherited]
		:Spec Proposal
	.Updated At[datetime]{1} [CA-R-1416; CA-R-2102] [inherited]
	.version_number[int]{1} [CA-R-1415; CA-R-2102] [inherited]
```

### Atom/Content Role: Concern

```yaml
subjects:
  governs: 'Model::CAPRMEDIO::Continuant/Governing Objects/Atom/Content Role: Concern'
```

```text
Atom/Content Role: Concern
	.Author[string]{1} [CA-R-2102] [inherited]
	.content{0} [CA-R-1359] [inherited]
		.concern[string]{1} [CA-R-2102]
		.details[string]{0..1} [CA-R-2102; CA-R-1624] [inherited]
		.scope[string]{0..1} [CA-R-2102; CA-R-2160] [inherited]
		.semantics[string]{0..1} [CA-R-2102; CA-R-1946] [inherited]
		.summary[string]{1} [CA-R-2102; CA-R-1465] [inherited]
	.Content Role[string]{1} [CA-R-1283; CA-R-2102] [inherited]
		:Concern [inherited]
	.Enabled Relations{0} [inherited]
		.Contains[bool] [CA-R-1945] [inherited] [kind-level capability]
			:False [inherited]
			:True [inherited]
	.id[string]{1} [CA-R-728; CA-R-2102] [inherited]
	.Label[string]{0..1} [CA-R-1594; CA-R-2102] [inherited]
	.Local Scope Unit[string]{1} [CA-R-920; CA-R-2102] [inherited]
	.Priority
	.Relations{0} [CA-R-2102] [inherited]
	.Status[string]{1} [CA-R-1412; CA-R-1608; CA-R-1947; CA-R-2102] [inherited]
		:Active [inherited]
		:Archived [inherited]
		:Canceled
		:Draft [inherited]
		:Resolved
	.Subjects{0} [CA-R-1198; CA-R-2102] [inherited]
		.Depends On[string]{0+} [CA-R-1198] [inherited]
		.Governs[string]{1} [CA-R-1363] [inherited]
	.Target Scope Unit[string]{0..1} [CA-R-1595; CA-R-2102] [inherited]
	.Tier[int]{1} [CA-R-2124; CA-R-2125; CA-R-2102] [inherited]
	.Type[string]{1} [CA-R-2102] [inherited]
	.Updated At[datetime]{1} [CA-R-1416; CA-R-2102] [inherited]
	.version_number[int]{1} [CA-R-1415; CA-R-2102] [inherited]
```

### Atom/Content Role: Concern/Type: Problem

```yaml
subjects:
  governs: 'Model::CAPRMEDIO::Continuant/Governing Objects/Atom/Content Role: Concern/Type: Problem'
```

```text
Atom/Content Role: Concern/Type: Problem
	.Author[string]{1} [CA-R-2102] [inherited]
	.content{0} [CA-R-1359] [inherited]
		.concern[string]{1} [CA-R-2102] [inherited]
		.details[string]{0..1} [CA-R-2102; CA-R-1624] [inherited]
		.scope[string]{0..1} [CA-R-2102; CA-R-2160] [inherited]
		.semantics[string]{0..1} [CA-R-2102; CA-R-1946] [inherited]
		.summary[string]{1} [CA-R-2102; CA-R-1465] [inherited]
	.Content Role[string]{1} [CA-R-1283; CA-R-2102] [inherited]
		:Concern [inherited]
	.Enabled Relations{0} [inherited]
		.Contains[bool] [CA-R-1945] [inherited] [kind-level capability]
			:False [inherited]
			:True [inherited]
	.id[string]{1} [CA-R-728; CA-R-2102] [inherited]
	.Label[string]{0..1} [CA-R-1594; CA-R-2102] [inherited]
	.Local Scope Unit[string]{1} [CA-R-920; CA-R-2102] [inherited]
	.Priority [inherited]
	.Relations{0} [CA-R-2102] [inherited]
	.Status[string]{1} [CA-R-1412; CA-R-1608; CA-R-1947; CA-R-2102] [inherited]
		:Active [inherited]
		:Archived [inherited]
		:Canceled [inherited]
		:Draft [inherited]
		:Resolved [inherited]
	.Subjects{0} [CA-R-1198; CA-R-2102] [inherited]
		.Depends On[string]{0+} [CA-R-1198] [inherited]
		.Governs[string]{1} [CA-R-1363] [inherited]
	.Target Scope Unit[string]{0..1} [CA-R-1595; CA-R-2102] [inherited]
	.Tier[int]{1} [CA-R-2124; CA-R-2125; CA-R-2102] [inherited]
	.Type[string]{1} [CA-R-2102] [inherited]
		:Problem
	.Updated At[datetime]{1} [CA-R-1416; CA-R-2102] [inherited]
	.version_number[int]{1} [CA-R-1415; CA-R-2102] [inherited]
```

### Atom/Content Role: Concern/Type: Bug

```yaml
subjects:
  governs: 'Model::CAPRMEDIO::Continuant/Governing Objects/Atom/Content Role: Concern/Type: Bug'
```

```text
Atom/Content Role: Concern/Type: Bug
	.Author[string]{1} [CA-R-2102] [inherited]
	.content{0} [CA-R-1359] [inherited]
		.concern[string]{1} [CA-R-2102] [inherited]
		.details[string]{0..1} [CA-R-2102; CA-R-1624] [inherited]
		.scope[string]{0..1} [CA-R-2102; CA-R-2160] [inherited]
		.semantics[string]{0..1} [CA-R-2102; CA-R-1946] [inherited]
		.summary[string]{1} [CA-R-2102; CA-R-1465] [inherited]
	.Content Role[string]{1} [CA-R-1283; CA-R-2102] [inherited]
		:Concern [inherited]
	.Enabled Relations{0} [inherited]
		.Contains[bool] [CA-R-1945] [inherited] [kind-level capability]
			:False [inherited]
			:True [inherited]
	.id[string]{1} [CA-R-728; CA-R-2102] [inherited]
	.Label[string]{0..1} [CA-R-1594; CA-R-2102] [inherited]
	.Local Scope Unit[string]{1} [CA-R-920; CA-R-2102] [inherited]
	.Priority [inherited]
	.Relations{0} [CA-R-2102] [inherited]
	.Status[string]{1} [CA-R-1412; CA-R-1608; CA-R-1947; CA-R-2102] [inherited]
		:Active [inherited]
		:Archived [inherited]
		:Canceled [inherited]
		:Draft [inherited]
		:Resolved [inherited]
	.Subjects{0} [CA-R-1198; CA-R-2102] [inherited]
		.Depends On[string]{0+} [CA-R-1198] [inherited]
		.Governs[string]{1} [CA-R-1363] [inherited]
	.Target Scope Unit[string]{0..1} [CA-R-1595; CA-R-2102] [inherited]
	.Tier[int]{1} [CA-R-2124; CA-R-2125; CA-R-2102] [inherited]
	.Type[string]{1} [CA-R-2102] [inherited]
		:Bug
	.Updated At[datetime]{1} [CA-R-1416; CA-R-2102] [inherited]
	.version_number[int]{1} [CA-R-1415; CA-R-2102] [inherited]
```

### Atom/Content Role: Concern/Type: Risk

```yaml
subjects:
  governs: 'Model::CAPRMEDIO::Continuant/Governing Objects/Atom/Content Role: Concern/Type: Risk'
```

```text
Atom/Content Role: Concern/Type: Risk
	.Author[string]{1} [CA-R-2102] [inherited]
	.content{0} [CA-R-1359] [inherited]
		.concern[string]{1} [CA-R-2102] [inherited]
		.details[string]{0..1} [CA-R-2102; CA-R-1624] [inherited]
		.scope[string]{0..1} [CA-R-2102; CA-R-2160] [inherited]
		.semantics[string]{0..1} [CA-R-2102; CA-R-1946] [inherited]
		.summary[string]{1} [CA-R-2102; CA-R-1465] [inherited]
	.Content Role[string]{1} [CA-R-1283; CA-R-2102] [inherited]
		:Concern [inherited]
	.Enabled Relations{0} [inherited]
		.Contains[bool] [CA-R-1945] [inherited] [kind-level capability]
			:False [inherited]
			:True [inherited]
	.id[string]{1} [CA-R-728; CA-R-2102] [inherited]
	.Label[string]{0..1} [CA-R-1594; CA-R-2102] [inherited]
	.Local Scope Unit[string]{1} [CA-R-920; CA-R-2102] [inherited]
	.Priority [inherited]
	.Relations{0} [CA-R-2102] [inherited]
	.Status[string]{1} [CA-R-1412; CA-R-1608; CA-R-1947; CA-R-2102] [inherited]
		:Active [inherited]
		:Archived [inherited]
		:Canceled [inherited]
		:Draft [inherited]
		:Resolved [inherited]
	.Subjects{0} [CA-R-1198; CA-R-2102] [inherited]
		.Depends On[string]{0+} [CA-R-1198] [inherited]
		.Governs[string]{1} [CA-R-1363] [inherited]
	.Target Scope Unit[string]{0..1} [CA-R-1595; CA-R-2102] [inherited]
	.Tier[int]{1} [CA-R-2124; CA-R-2125; CA-R-2102] [inherited]
	.Type[string]{1} [CA-R-2102] [inherited]
		:Risk
	.Updated At[datetime]{1} [CA-R-1416; CA-R-2102] [inherited]
	.version_number[int]{1} [CA-R-1415; CA-R-2102] [inherited]
```

### Atom/Content Role: Concern/Type: Opportunity

```yaml
subjects:
  governs: 'Model::CAPRMEDIO::Continuant/Governing Objects/Atom/Content Role: Concern/Type: Opportunity'
```

```text
Atom/Content Role: Concern/Type: Opportunity
	.Author[string]{1} [CA-R-2102] [inherited]
	.content{0} [CA-R-1359] [inherited]
		.concern[string]{1} [CA-R-2102] [inherited]
		.details[string]{0..1} [CA-R-2102; CA-R-1624] [inherited]
		.scope[string]{0..1} [CA-R-2102; CA-R-2160] [inherited]
		.semantics[string]{0..1} [CA-R-2102; CA-R-1946] [inherited]
		.summary[string]{1} [CA-R-2102; CA-R-1465] [inherited]
	.Content Role[string]{1} [CA-R-1283; CA-R-2102] [inherited]
		:Concern [inherited]
	.Enabled Relations{0} [inherited]
		.Contains[bool] [CA-R-1945] [inherited] [kind-level capability]
			:False [inherited]
			:True [inherited]
	.id[string]{1} [CA-R-728; CA-R-2102] [inherited]
	.Label[string]{0..1} [CA-R-1594; CA-R-2102] [inherited]
	.Local Scope Unit[string]{1} [CA-R-920; CA-R-2102] [inherited]
	.Priority [inherited]
	.Relations{0} [CA-R-2102] [inherited]
	.Status[string]{1} [CA-R-1412; CA-R-1608; CA-R-1947; CA-R-2102] [inherited]
		:Active [inherited]
		:Archived [inherited]
		:Canceled [inherited]
		:Draft [inherited]
		:Resolved [inherited]
	.Subjects{0} [CA-R-1198; CA-R-2102] [inherited]
		.Depends On[string]{0+} [CA-R-1198] [inherited]
		.Governs[string]{1} [CA-R-1363] [inherited]
	.Target Scope Unit[string]{0..1} [CA-R-1595; CA-R-2102] [inherited]
	.Tier[int]{1} [CA-R-2124; CA-R-2125; CA-R-2102] [inherited]
	.Type[string]{1} [CA-R-2102] [inherited]
		:Opportunity
	.Updated At[datetime]{1} [CA-R-1416; CA-R-2102] [inherited]
	.version_number[int]{1} [CA-R-1415; CA-R-2102] [inherited]
```

### Atom/Content Role: Delivery

```yaml
subjects:
  governs: 'Model::CAPRMEDIO::Continuant/Governing Objects/Atom/Content Role: Delivery'
```

```text
Atom/Content Role: Delivery
	.Author[string]{1} [CA-R-2102] [inherited]
	.content{0} [CA-R-1359] [inherited]
		.claim[string]{1} [CA-R-1269; CA-R-2102]
		.claim_scope[string]{0..1} [CA-R-2160; CA-R-2102]
		.details[string]{0..1} [CA-R-2102; CA-R-1624] [inherited]
		.semantics[string]{0..1} [CA-R-2102; CA-R-1946] [inherited]
		.summary[string]{1} [CA-R-2102; CA-R-1465] [inherited]
	.Content Role[string]{1} [CA-R-1283; CA-R-2102] [inherited]
		:Delivery [inherited]
	.Enabled Relations{0} [inherited]
		.Contains[bool] [CA-R-1945] [inherited] [kind-level capability]
			:False [inherited]
			:True [inherited]
	.id[string]{1} [CA-R-728; CA-R-2102] [inherited]
	.Label[string]{0..1} [CA-R-1594; CA-R-2102] [inherited]
	.Local Scope Unit[string]{1} [CA-R-920; CA-R-2102] [inherited]
	.Relations{0} [CA-R-2102] [inherited]
	.Status[string]{1} [CA-R-1412; CA-R-1947; CA-R-2102] [inherited]
		:Active [inherited]
		:Archived [inherited]
		:Draft [inherited]
	.Subjects{0} [CA-R-1198; CA-R-2102] [inherited]
		.Depends On[string]{0+} [CA-R-1198] [inherited]
		.Governs[string]{1} [CA-R-1363] [inherited]
	.Target Scope Unit[string]{0..1} [CA-R-1595; CA-R-2102] [inherited]
	.Tier[int]{1} [CA-R-2124; CA-R-2125; CA-R-2102] [inherited]
	.Type[string]{1} [CA-R-2102] [inherited]
	.Updated At[datetime]{1} [CA-R-1416; CA-R-2102] [inherited]
	.version_number[int]{1} [CA-R-1415; CA-R-2102] [inherited]
```

### Atom/Content Role: Evaluation

```yaml
subjects:
  governs: 'Model::CAPRMEDIO::Continuant/Governing Objects/Atom/Content Role: Evaluation'
```

```text
Atom/Content Role: Evaluation
	.Author[string]{1} [CA-R-2102] [inherited]
	.content{0} [CA-R-1359] [inherited]
		.claim[string]{1} [CA-R-1269; CA-R-2102]
		.claim_scope[string]{0..1} [CA-R-2160; CA-R-2102]
		.details[string]{0..1} [CA-R-2102; CA-R-1624] [inherited]
		.semantics[string]{0..1} [CA-R-2102; CA-R-1946] [inherited]
		.summary[string]{1} [CA-R-2102; CA-R-1465] [inherited]
	.Content Role[string]{1} [CA-R-1283; CA-R-2102] [inherited]
		:Evaluation [inherited]
	.Enabled Relations{0} [inherited]
		.Contains[bool] [CA-R-1945] [inherited] [kind-level capability]
			:False [inherited]
			:True [inherited]
	.id[string]{1} [CA-R-728; CA-R-2102] [inherited]
	.Label[string]{0..1} [CA-R-1594; CA-R-2102] [inherited]
	.Local Scope Unit[string]{1} [CA-R-920; CA-R-2102] [inherited]
	.Relations{0} [CA-R-2102] [inherited]
	.Status[string]{1} [CA-R-1412; CA-R-1947; CA-R-2102] [inherited]
		:Active [inherited]
		:Archived [inherited]
		:Draft [inherited]
	.Subjects{0} [CA-R-1198; CA-R-2102] [inherited]
		.Depends On[string]{0+} [CA-R-1198] [inherited]
		.Governs[string]{1} [CA-R-1363] [inherited]
	.Target Scope Unit[string]{0..1} [CA-R-1595; CA-R-2102] [inherited]
	.Tier[int]{1} [CA-R-2124; CA-R-2125; CA-R-2102] [inherited]
	.Type[string]{1} [CA-R-2102] [inherited]
	.Updated At[datetime]{1} [CA-R-1416; CA-R-2102] [inherited]
	.version_number[int]{1} [CA-R-1415; CA-R-2102] [inherited]
```

### Atom/Content Role: Evaluation/Type: Eval Policy

```yaml
subjects:
  governs: 'Model::CAPRMEDIO::Continuant/Governing Objects/Atom/Content Role: Evaluation/Type: Eval Policy'
```

```text
Atom/Content Role: Evaluation/Type: Eval Policy
	.Author[string]{1} [CA-R-2102] [inherited]
	.content{0} [CA-R-1359] [inherited]
		.claim[string]{1} [CA-R-1269; CA-R-2102] [inherited]
		.claim_scope[string]{0..1} [CA-R-2160; CA-R-2102] [inherited]
		.details[string]{0..1} [CA-R-2102; CA-R-1624] [inherited]
		.semantics[string]{0..1} [CA-R-2102; CA-R-1946] [inherited]
		.summary[string]{1} [CA-R-2102; CA-R-1465] [inherited]
	.Content Role[string]{1} [CA-R-1283; CA-R-2102] [inherited]
		:Evaluation [inherited]
	.Enabled Relations{0} [inherited]
		.Contains[bool] [CA-R-1945] [inherited] [kind-level capability]
			:False [inherited]
			:True [inherited]
	.id[string]{1} [CA-R-728; CA-R-2102] [inherited]
	.Label[string]{0..1} [CA-R-1594; CA-R-2102] [inherited]
	.Local Scope Unit[string]{1} [CA-R-920; CA-R-2102] [inherited]
	.Relations{0} [CA-R-2102] [inherited]
	.Status[string]{1} [CA-R-1412; CA-R-1947; CA-R-2102] [inherited]
		:Active [inherited]
		:Archived [inherited]
		:Draft [inherited]
	.Subjects{0} [CA-R-1198; CA-R-2102] [inherited]
		.Depends On[string]{0+} [CA-R-1198] [inherited]
		.Governs[string]{1} [CA-R-1363] [inherited]
	.Target Scope Unit[string]{0..1} [CA-R-1595; CA-R-2102] [inherited]
	.Tier[int]{1} [CA-R-2124; CA-R-2125; CA-R-2102] [inherited]
	.Type[string]{1} [CA-R-2102] [inherited]
		:Eval Policy
	.Updated At[datetime]{1} [CA-R-1416; CA-R-2102] [inherited]
	.version_number[int]{1} [CA-R-1415; CA-R-2102] [inherited]
```

### Atom/Content Role: Evaluation/Type: Eval Case

```yaml
subjects:
  governs: 'Model::CAPRMEDIO::Continuant/Governing Objects/Atom/Content Role: Evaluation/Type: Eval Case'
```

```text
Atom/Content Role: Evaluation/Type: Eval Case
	.Author[string]{1} [CA-R-2102] [inherited]
	.content{0} [CA-R-1359] [inherited]
		.claim[string]{1} [CA-R-1269; CA-R-2102] [inherited]
		.claim_scope[string]{0..1} [CA-R-2160; CA-R-2102] [inherited]
		.details[string]{0..1} [CA-R-2102; CA-R-1624] [inherited]
		.semantics[string]{0..1} [CA-R-2102; CA-R-1946] [inherited]
		.summary[string]{1} [CA-R-2102; CA-R-1465] [inherited]
	.Content Role[string]{1} [CA-R-1283; CA-R-2102] [inherited]
		:Evaluation [inherited]
	.Enabled Relations{0} [inherited]
		.Contains[bool] [CA-R-1945] [inherited] [kind-level capability]
			:False [inherited]
			:True [inherited]
	.id[string]{1} [CA-R-728; CA-R-2102] [inherited]
	.Label[string]{0..1} [CA-R-1594; CA-R-2102] [inherited]
	.Local Scope Unit[string]{1} [CA-R-920; CA-R-2102] [inherited]
	.Relations{0} [CA-R-2102] [inherited]
	.Status[string]{1} [CA-R-1412; CA-R-1947; CA-R-2102] [inherited]
		:Active [inherited]
		:Archived [inherited]
		:Draft [inherited]
	.Subjects{0} [CA-R-1198; CA-R-2102] [inherited]
		.Depends On[string]{0+} [CA-R-1198] [inherited]
		.Governs[string]{1} [CA-R-1363] [inherited]
	.Target Scope Unit[string]{0..1} [CA-R-1595; CA-R-2102] [inherited]
	.Tier[int]{1} [CA-R-2124; CA-R-2125; CA-R-2102] [inherited]
	.Type[string]{1} [CA-R-2102] [inherited]
		:Eval Case
	.Updated At[datetime]{1} [CA-R-1416; CA-R-2102] [inherited]
	.version_number[int]{1} [CA-R-1415; CA-R-2102] [inherited]
```

### Atom/Content Role: Method

```yaml
subjects:
  governs: 'Model::CAPRMEDIO::Continuant/Governing Objects/Atom/Content Role: Method'
```

```text
Atom/Content Role: Method
	.Author[string]{1} [CA-R-2102] [inherited]
	.content{0} [CA-R-1359] [inherited]
		.claim[string]{1} [CA-R-1269; CA-R-2102]
		.claim_scope[string]{0..1} [CA-R-2160; CA-R-2102]
		.details[string]{0..1} [CA-R-2102; CA-R-1624] [inherited]
		.semantics[string]{0..1} [CA-R-2102; CA-R-1946] [inherited]
		.summary[string]{1} [CA-R-2102; CA-R-1465] [inherited]
	.Content Role[string]{1} [CA-R-1283; CA-R-2102] [inherited]
		:Method [inherited]
	.Enabled Relations{0} [inherited]
		.Contains[bool] [CA-R-1945] [inherited] [kind-level capability]
			:False [inherited]
			:True [inherited]
	.id[string]{1} [CA-R-728; CA-R-2102] [inherited]
	.Label[string]{0..1} [CA-R-1594; CA-R-2102] [inherited]
	.Local Scope Unit[string]{1} [CA-R-920; CA-R-2102] [inherited]
	.Relations{0} [CA-R-2102] [inherited]
	.Status[string]{1} [CA-R-1412; CA-R-1947; CA-R-2102] [inherited]
		:Active [inherited]
		:Archived [inherited]
		:Draft [inherited]
	.Subjects{0} [CA-R-1198; CA-R-2102] [inherited]
		.Depends On[string]{0+} [CA-R-1198] [inherited]
		.Governs[string]{1} [CA-R-1363] [inherited]
	.Target Scope Unit[string]{0..1} [CA-R-1595; CA-R-2102] [inherited]
	.Tier[int]{1} [CA-R-2124; CA-R-2125; CA-R-2102] [inherited]
	.Type[string]{1} [CA-R-2102] [inherited]
	.Updated At[datetime]{1} [CA-R-1416; CA-R-2102] [inherited]
	.version_number[int]{1} [CA-R-1415; CA-R-2102] [inherited]
```

### Atom/Content Role: Method/Type: Eng Policy

```yaml
subjects:
  governs: 'Model::CAPRMEDIO::Continuant/Governing Objects/Atom/Content Role: Method/Type: Eng Policy'
```

```text
Atom/Content Role: Method/Type: Eng Policy
	.Author[string]{1} [CA-R-2102] [inherited]
	.content{0} [CA-R-1359] [inherited]
		.claim[string]{1} [CA-R-1269; CA-R-2102] [inherited]
		.claim_scope[string]{0..1} [CA-R-2160; CA-R-2102] [inherited]
		.details[string]{0..1} [CA-R-2102; CA-R-1624] [inherited]
		.semantics[string]{0..1} [CA-R-2102; CA-R-1946] [inherited]
		.summary[string]{1} [CA-R-2102; CA-R-1465] [inherited]
	.Content Role[string]{1} [CA-R-1283; CA-R-2102] [inherited]
		:Method [inherited]
	.Enabled Relations{0} [inherited]
		.Contains[bool] [CA-R-1945] [inherited] [kind-level capability]
			:False [inherited]
			:True [inherited]
	.id[string]{1} [CA-R-728; CA-R-2102] [inherited]
	.Label[string]{0..1} [CA-R-1594; CA-R-2102] [inherited]
	.Local Scope Unit[string]{1} [CA-R-920; CA-R-2102] [inherited]
	.Relations{0} [CA-R-2102] [inherited]
	.Status[string]{1} [CA-R-1412; CA-R-1947; CA-R-2102] [inherited]
		:Active [inherited]
		:Archived [inherited]
		:Draft [inherited]
	.Subjects{0} [CA-R-1198; CA-R-2102] [inherited]
		.Depends On[string]{0+} [CA-R-1198] [inherited]
		.Governs[string]{1} [CA-R-1363] [inherited]
	.Target Scope Unit[string]{0..1} [CA-R-1595; CA-R-2102] [inherited]
	.Tier[int]{1} [CA-R-2124; CA-R-2125; CA-R-2102] [inherited]
	.Type[string]{1} [CA-R-2102] [inherited]
		:Eng Policy
	.Updated At[datetime]{1} [CA-R-1416; CA-R-2102] [inherited]
	.version_number[int]{1} [CA-R-1415; CA-R-2102] [inherited]
```

### Atom/Content Role: Method/Type: Eng Decision

```yaml
subjects:
  governs: 'Model::CAPRMEDIO::Continuant/Governing Objects/Atom/Content Role: Method/Type: Eng Decision'
```

```text
Atom/Content Role: Method/Type: Eng Decision
	.Author[string]{1} [CA-R-2102] [inherited]
	.content{0} [CA-R-1359] [inherited]
		.claim[string]{1} [CA-R-1269; CA-R-2102] [inherited]
		.claim_scope[string]{0..1} [CA-R-2160; CA-R-2102] [inherited]
		.details[string]{0..1} [CA-R-2102; CA-R-1624] [inherited]
		.semantics[string]{0..1} [CA-R-2102; CA-R-1946] [inherited]
		.summary[string]{1} [CA-R-2102; CA-R-1465] [inherited]
	.Content Role[string]{1} [CA-R-1283; CA-R-2102] [inherited]
		:Method [inherited]
	.Enabled Relations{0} [inherited]
		.Contains[bool] [CA-R-1945] [inherited] [kind-level capability]
			:False [inherited]
			:True [inherited]
	.id[string]{1} [CA-R-728; CA-R-2102] [inherited]
	.Label[string]{0..1} [CA-R-1594; CA-R-2102] [inherited]
	.Local Scope Unit[string]{1} [CA-R-920; CA-R-2102] [inherited]
	.Relations{0} [CA-R-2102] [inherited]
	.Status[string]{1} [CA-R-1412; CA-R-1947; CA-R-2102] [inherited]
		:Active [inherited]
		:Archived [inherited]
		:Draft [inherited]
	.Subjects{0} [CA-R-1198; CA-R-2102] [inherited]
		.Depends On[string]{0+} [CA-R-1198] [inherited]
		.Governs[string]{1} [CA-R-1363] [inherited]
	.Target Scope Unit[string]{0..1} [CA-R-1595; CA-R-2102] [inherited]
	.Tier[int]{1} [CA-R-2124; CA-R-2125; CA-R-2102] [inherited]
	.Type[string]{1} [CA-R-2102] [inherited]
		:Eng Decision
	.Updated At[datetime]{1} [CA-R-1416; CA-R-2102] [inherited]
	.version_number[int]{1} [CA-R-1415; CA-R-2102] [inherited]
```

### Atom/Content Role: Operations

```yaml
subjects:
  governs: 'Model::CAPRMEDIO::Continuant/Governing Objects/Atom/Content Role: Operations'
```

```text
Atom/Content Role: Operations
	.Author[string]{1} [CA-R-2102] [inherited]
	.content{0} [CA-R-1359] [inherited]
		.details[string]{0..1} [CA-R-2102; CA-R-1624] [inherited]
		.operation[string]{1} [CA-R-2102]
		.scope[string]{0..1} [CA-R-2102; CA-R-2160] [inherited]
		.semantics[string]{0..1} [CA-R-2102; CA-R-1946] [inherited]
		.summary[string]{1} [CA-R-2102; CA-R-1465] [inherited]
	.Content Role[string]{1} [CA-R-1283; CA-R-2102] [inherited]
		:Operations [inherited]
	.Enabled Relations{0} [inherited]
		.Contains[bool] [CA-R-1945] [inherited] [kind-level capability]
			:False [inherited]
			:True [inherited]
	.id[string]{1} [CA-R-728; CA-R-2102] [inherited]
	.Label[string]{0..1} [CA-R-1594; CA-R-2102] [inherited]
	.Local Scope Unit[string]{1} [CA-R-920; CA-R-2102] [inherited]
	.Relations{0} [CA-R-2102] [inherited]
	.Status[string]{1} [CA-R-1412; CA-R-1947; CA-R-2102] [inherited]
		:Active [inherited]
		:Archived [inherited]
		:Draft [inherited]
	.Subjects{0} [CA-R-1198; CA-R-2102] [inherited]
		.Depends On[string]{0+} [CA-R-1198] [inherited]
		.Governs[string]{1} [CA-R-1363] [inherited]
	.Target Scope Unit[string]{0..1} [CA-R-1595; CA-R-2102] [inherited]
	.Tier[int]{1} [CA-R-2124; CA-R-2125; CA-R-2102] [inherited]
	.Type[string]{1} [CA-R-2102] [inherited]
	.Updated At[datetime]{1} [CA-R-1416; CA-R-2102] [inherited]
	.version_number[int]{1} [CA-R-1415; CA-R-2102] [inherited]
```

### Atom/Content Role: Operations/Type: Action

```yaml
subjects:
  governs: 'Model::CAPRMEDIO::Continuant/Governing Objects/Atom/Content Role: Operations/Type: Action'
```

```text
Atom/Content Role: Operations/Type: Action
	.Author[string]{1} [CA-R-2102] [inherited]
	.content{0} [CA-R-1359] [inherited]
		.details[string]{0..1} [CA-R-2102; CA-R-1624] [inherited]
		.operation[string]{1} [CA-R-2102] [inherited]
		.scope[string]{0..1} [CA-R-2102; CA-R-2160] [inherited]
		.semantics[string]{0..1} [CA-R-2102; CA-R-1946] [inherited]
		.summary[string]{1} [CA-R-2102; CA-R-1465] [inherited]
	.Content Role[string]{1} [CA-R-1283; CA-R-2102] [inherited]
		:Operations [inherited]
	.Enabled Relations{0} [inherited]
		.Contains[bool] [CA-R-1945] [inherited] [kind-level capability]
			:False [inherited]
			:True [inherited]
	.Execution Kind[string] [CA-R-1526]
		:Agentic
		:Programmatic
	.id[string]{1} [CA-R-728; CA-R-2102] [inherited]
	.Label[string]{0..1} [CA-R-1594; CA-R-2102] [inherited]
	.Local Scope Unit[string]{1} [CA-R-920; CA-R-2102] [inherited]
	.Relations{0} [CA-R-2102] [inherited]
	.Status[string]{1} [CA-R-1412; CA-R-1947; CA-R-2102] [inherited]
		:Active [inherited]
		:Archived [inherited]
		:Draft [inherited]
	.Subjects{0} [CA-R-1198; CA-R-2102] [inherited]
		.Depends On[string]{0+} [CA-R-1198] [inherited]
		.Governs[string]{1} [CA-R-1363] [inherited]
	.Target Scope Unit[string]{0..1} [CA-R-1595; CA-R-2102] [inherited]
	.Tier[int]{1} [CA-R-2124; CA-R-2125; CA-R-2102] [inherited]
	.Type[string]{1} [CA-R-2102] [inherited]
		:Action
	.Updated At[datetime]{1} [CA-R-1416; CA-R-2102] [inherited]
	.version_number[int]{1} [CA-R-1415; CA-R-2102] [inherited]
```

### Atom/Content Role: Operations/Type: Workflow

```yaml
subjects:
  governs: 'Model::CAPRMEDIO::Continuant/Governing Objects/Atom/Content Role: Operations/Type: Workflow'
```

```text
Atom/Content Role: Operations/Type: Workflow
	.Author[string]{1} [CA-R-2102] [inherited]
	.content{0} [CA-R-1359] [inherited]
		.details[string]{0..1} [CA-R-2102; CA-R-1624] [inherited]
		.operation[string]{1} [CA-R-2102] [inherited]
		.scope[string]{0..1} [CA-R-2102; CA-R-2160] [inherited]
		.semantics[string]{0..1} [CA-R-2102; CA-R-1946] [inherited]
		.summary[string]{1} [CA-R-2102; CA-R-1465] [inherited]
	.Content Role[string]{1} [CA-R-1283; CA-R-2102] [inherited]
		:Operations [inherited]
	.Enabled Relations{0} [inherited]
		.Contains[bool] [CA-R-1945; CA-R-1991] [inherited] [kind-level capability]
			:True [inherited]
	.id[string]{1} [CA-R-728; CA-R-2102] [inherited]
	.Label[string]{0..1} [CA-R-1594; CA-R-2102] [inherited]
	.Local Scope Unit[string]{1} [CA-R-920; CA-R-2102] [inherited]
	.Relations{0} [CA-R-2102] [inherited]
	.Status[string]{1} [CA-R-1412; CA-R-1947; CA-R-2102] [inherited]
		:Active [inherited]
		:Archived [inherited]
		:Draft [inherited]
	.Subjects{0} [CA-R-1198; CA-R-2102] [inherited]
		.Depends On[string]{0+} [CA-R-1198] [inherited]
		.Governs[string]{1} [CA-R-1363] [inherited]
	.Target Scope Unit[string]{0..1} [CA-R-1595; CA-R-2102] [inherited]
	.Tier[int]{1} [CA-R-2124; CA-R-2125; CA-R-2102] [inherited]
	.Type[string]{1} [CA-R-2102] [inherited]
		:Workflow
	.Updated At[datetime]{1} [CA-R-1416; CA-R-2102] [inherited]
	.version_number[int]{1} [CA-R-1415; CA-R-2102] [inherited]
```

### Step

```yaml
subjects:
  governs: 'Model::CAPRMEDIO::Continuant/Governing Objects/Atom/Content Role: Operations/Type: Workflow>Step'
```

```text
Step
	.Agentic Execution Context [CA-R-1527]
	.Enabled Relations
		.Contains[bool] [CA-R-1992] [kind-level capability]
			:True
	.Type[string]{1} [CA-R-1509]
		:Step
```

### Atom/Content Role: Plan

```yaml
subjects:
  governs: 'Model::CAPRMEDIO::Continuant/Governing Objects/Atom/Content Role: Plan'
```

```text
Atom/Content Role: Plan
	.Assignee
	.Author[string]{1} [CA-R-2102] [inherited]
	.Autonomous Confidence Threshold
	.content{0} [CA-R-1359] [inherited]
		.details[string]{0..1} [CA-R-2102; CA-R-1624] [inherited]
		.objective[string]{1} [CA-R-2102]
		.scope[string]{0..1} [CA-R-2102; CA-R-2160] [inherited]
		.semantics[string]{0..1} [CA-R-2102; CA-R-1946] [inherited]
		.summary[string]{1} [CA-R-2102; CA-R-1465] [inherited]
	.Content Role[string]{1} [CA-R-1283; CA-R-2102] [inherited]
		:Plan [inherited]
	.Definition of Done{1} [CA-R-1581]
	.Enabled Relations{0} [inherited]
		.Contains[bool] [CA-R-1945; CA-R-1990] [inherited] [kind-level capability]
			:True [inherited]
	.id[string]{1} [CA-R-728; CA-R-2102] [inherited]
	.Label[string]{0..1} [CA-R-1594; CA-R-2102] [inherited]
	.Local Scope Unit[string]{1} [CA-R-920; CA-R-2102] [inherited]
	.Relations{0} [CA-R-2102] [inherited]
	.Status[string]{1} [CA-R-1412; CA-R-1539; CA-R-1947; CA-R-2102] [inherited]
		:Active [inherited]
		:Archived [inherited]
		:Backlog
		:Canceled
		:Done
		:Draft [inherited]
	.Subjects{0} [CA-R-1198; CA-R-2102] [inherited]
		.Depends On[string]{0+} [CA-R-1198] [inherited]
		.Governs[string]{1} [CA-R-1363] [inherited]
	.Target Scope Unit[string]{0..1} [CA-R-1595; CA-R-2102] [inherited]
	.Tier[int]{1} [CA-R-2124; CA-R-2125; CA-R-2102] [inherited]
	.Type[string]{1} [CA-R-2102] [inherited]
	.Updated At[datetime]{1} [CA-R-1416; CA-R-2102] [inherited]
	.version_number[int]{1} [CA-R-1415; CA-R-2102] [inherited]
	.Work Sequence Number [CA-R-991]
```

### Atom/Content Role: Requirement

```yaml
subjects:
  governs: 'Model::CAPRMEDIO::Continuant/Governing Objects/Atom/Content Role: Requirement'
```

```text
Atom/Content Role: Requirement
	.Author[string]{1} [CA-R-2102] [inherited]
	.content{0} [CA-R-1359] [inherited]
		.claim[string]{1} [CA-R-1269; CA-R-2102]
			.formal_claim[string]{0..1} [CA-R-1269]
		.claim_scope[string]{0..1} [CA-R-2160; CA-R-2102]
		.details[string]{0..1} [CA-R-2102; CA-R-1624] [inherited]
		.semantics[string]{0..1} [CA-R-2102; CA-R-1946] [inherited]
		.summary[string]{1} [CA-R-2102; CA-R-1465] [inherited]
	.Content Role[string]{1} [CA-R-1283; CA-R-2102] [inherited]
		:Requirement [inherited]
	.Enabled Relations{0} [inherited]
		.Contains[bool] [CA-R-1945] [inherited] [kind-level capability]
			:False [inherited]
			:True [inherited]
	.id[string]{1} [CA-R-728; CA-R-2102] [inherited]
	.Label[string]{0..1} [CA-R-1594; CA-R-2102] [inherited]
	.Local Scope Unit[string]{1} [CA-R-920; CA-R-2102] [inherited]
	.Relations{0} [CA-R-2102] [inherited]
	.Status[string]{1} [CA-R-1412; CA-R-1947; CA-R-2102] [inherited]
		:Active [inherited]
		:Archived [inherited]
		:Draft [inherited]
	.Subjects{0} [CA-R-1198; CA-R-2102] [inherited]
		.Depends On[string]{0+} [CA-R-1198] [inherited]
		.Governs[string]{1} [CA-R-1363] [inherited]
	.Target Scope Unit[string]{0..1} [CA-R-1595; CA-R-2102] [inherited]
	.Tier[int]{1} [CA-R-2124; CA-R-2125; CA-R-2102] [inherited]
	.Type[string]{1} [CA-R-2102] [inherited]
	.Updated At[datetime]{1} [CA-R-1416; CA-R-2102] [inherited]
	.version_number[int]{1} [CA-R-1415; CA-R-2102] [inherited]
```

### Atom/Content Role: Requirement/Type: Requirement

```yaml
subjects:
  governs: 'Model::CAPRMEDIO::Continuant/Governing Objects/Atom/Content Role: Requirement/Type: Requirement'
```

```text
Atom/Content Role: Requirement/Type: Requirement
	.Author[string]{1} [CA-R-2102] [inherited]
	.content{0} [CA-R-1359] [inherited]
		.claim[string]{1} [CA-R-1269; CA-R-2102] [inherited]
			.formal_claim[string]{0..1} [CA-R-1269] [inherited]
		.claim_scope[string]{0..1} [CA-R-2160; CA-R-2102] [inherited]
		.details[string]{0..1} [CA-R-2102; CA-R-1624] [inherited]
		.semantics[string]{0..1} [CA-R-2102; CA-R-1946] [inherited]
		.summary[string]{1} [CA-R-2102; CA-R-1465] [inherited]
	.Content Role[string]{1} [CA-R-1283; CA-R-2102] [inherited]
		:Requirement [inherited]
	.Enabled Relations{0} [inherited]
		.Contains[bool] [CA-R-1945] [inherited] [kind-level capability]
			:False [inherited]
			:True [inherited]
	.id[string]{1} [CA-R-728; CA-R-2102] [inherited]
	.Label[string]{0..1} [CA-R-1594; CA-R-2102] [inherited]
	.Local Scope Unit[string]{1} [CA-R-920; CA-R-2102] [inherited]
	.Relations{0} [CA-R-2102] [inherited]
	.Status[string]{1} [CA-R-1412; CA-R-1947; CA-R-2102] [inherited]
		:Active [inherited]
		:Archived [inherited]
		:Draft [inherited]
	.Subjects{0} [CA-R-1198; CA-R-2102] [inherited]
		.Depends On[string]{0+} [CA-R-1198] [inherited]
		.Governs[string]{1} [CA-R-1363] [inherited]
	.Target Scope Unit[string]{0..1} [CA-R-1595; CA-R-2102] [inherited]
	.Tier[int]{1} [CA-R-2124; CA-R-2125; CA-R-2102] [inherited]
	.Type[string]{1} [CA-R-2102] [inherited]
		:Requirement
	.Updated At[datetime]{1} [CA-R-1416; CA-R-2102] [inherited]
	.version_number[int]{1} [CA-R-1415; CA-R-2102] [inherited]
```

### Atom/Content Role: Requirement/Type: Demand

```yaml
subjects:
  governs: 'Model::CAPRMEDIO::Continuant/Governing Objects/Atom/Content Role: Requirement/Type: Demand'
```

```text
Atom/Content Role: Requirement/Type: Demand
	.Author[string]{1} [CA-R-2102] [inherited]
	.content{0} [CA-R-1359] [inherited]
		.claim[string]{1} [CA-R-1269; CA-R-2102] [inherited]
			.formal_claim[string]{0..1} [CA-R-1269] [inherited]
		.claim_scope[string]{0..1} [CA-R-2160; CA-R-2102] [inherited]
		.details[string]{0..1} [CA-R-2102; CA-R-1624] [inherited]
		.semantics[string]{0..1} [CA-R-2102; CA-R-1946] [inherited]
		.summary[string]{1} [CA-R-2102; CA-R-1465] [inherited]
	.Content Role[string]{1} [CA-R-1283; CA-R-2102] [inherited]
		:Requirement [inherited]
	.Enabled Relations{0} [inherited]
		.Contains[bool] [CA-R-1945] [inherited] [kind-level capability]
			:False [inherited]
			:True [inherited]
	.id[string]{1} [CA-R-728; CA-R-2102] [inherited]
	.Label[string]{0..1} [CA-R-1594; CA-R-2102] [inherited]
	.Local Scope Unit[string]{1} [CA-R-920; CA-R-2102] [inherited]
	.Relations{0} [CA-R-2102] [inherited]
	.Status[string]{1} [CA-R-1412; CA-R-1947; CA-R-2102] [inherited]
		:Active [inherited]
		:Archived [inherited]
		:Draft [inherited]
	.Subjects{0} [CA-R-1198; CA-R-2102] [inherited]
		.Depends On[string]{0+} [CA-R-1198] [inherited]
		.Governs[string]{1} [CA-R-1363] [inherited]
	.Target Scope Unit[string]{0..1} [CA-R-1595; CA-R-2102; CA-R-944] [inherited]
	.Tier[int]{1} [CA-R-2124; CA-R-2125; CA-R-2102] [inherited]
	.Type[string]{1} [CA-R-2102] [inherited]
		:Demand
	.Updated At[datetime]{1} [CA-R-1416; CA-R-2102] [inherited]
	.version_number[int]{1} [CA-R-1415; CA-R-2102] [inherited]
```

### Atom/Content Role: Requirement/Type: Definition

```yaml
subjects:
  governs: 'Model::CAPRMEDIO::Continuant/Governing Objects/Atom/Content Role: Requirement/Type: Definition'
```

```text
Atom/Content Role: Requirement/Type: Definition
	.Author[string]{1} [CA-R-2102] [inherited]
	.content{0} [CA-R-1359] [inherited]
		.claim[string]{1} [CA-R-1269; CA-R-2102; CA-R-2110] [inherited]
			.formal_claim[string]{0..1} [CA-R-1269] [inherited]
		.claim_scope[string]{0..1} [CA-R-2160; CA-R-2102] [inherited]
		.details[string]{0..1} [CA-R-2102; CA-R-1624] [inherited]
		.semantics[string]{0..1} [CA-R-2102; CA-R-1946] [inherited]
		.summary[string]{1} [CA-R-2102; CA-R-1465] [inherited]
	.Content Role[string]{1} [CA-R-1283; CA-R-2102] [inherited]
		:Requirement [inherited]
	.Enabled Relations{0} [inherited]
		.Contains[bool] [CA-R-1945] [inherited] [kind-level capability]
			:False [inherited]
			:True [inherited]
	.id[string]{1} [CA-R-728; CA-R-2102] [inherited]
	.Label[string]{0..1} [CA-R-1594; CA-R-2102] [inherited]
	.Local Scope Unit[string]{1} [CA-R-920; CA-R-2102] [inherited]
	.Relations{0} [CA-R-2102] [inherited]
	.Status[string]{1} [CA-R-1412; CA-R-1947; CA-R-2102] [inherited]
		:Active [inherited]
		:Archived [inherited]
		:Draft [inherited]
	.Subjects{0} [CA-R-1198; CA-R-2102] [inherited]
		.Depends On[string]{0+} [CA-R-1198] [inherited]
		.Governs[string]{1} [CA-R-1363] [inherited]
	.Target Scope Unit[string]{0..1} [CA-R-1595; CA-R-2102] [inherited]
	.Tier[int]{1} [CA-R-2124; CA-R-2125; CA-R-2102] [inherited]
	.Type[string]{1} [CA-R-2102] [inherited]
		:Definition
	.Updated At[datetime]{1} [CA-R-1416; CA-R-2102] [inherited]
	.version_number[int]{1} [CA-R-1415; CA-R-2102] [inherited]
```

### Atom/Content Role: Requirement/Type: Project Goal

```yaml
subjects:
  governs: 'Model::CAPRMEDIO::Continuant/Governing Objects/Atom/Content Role: Requirement/Type: Project Goal'
```

```text
Atom/Content Role: Requirement/Type: Project Goal
	.Author[string]{1} [CA-R-2102] [inherited]
	.content{0} [CA-R-1359] [inherited]
		.claim[string]{1} [CA-R-1269; CA-R-2102] [inherited]
			.formal_claim[string]{0..1} [CA-R-1269] [inherited]
		.claim_scope[string]{0..1} [CA-R-2160; CA-R-2102] [inherited]
		.details[string]{0..1} [CA-R-2102; CA-R-1624] [inherited]
		.semantics[string]{0..1} [CA-R-2102; CA-R-1946] [inherited]
		.summary[string]{1} [CA-R-2102; CA-R-1465] [inherited]
	.Content Role[string]{1} [CA-R-1283; CA-R-2102] [inherited]
		:Requirement [inherited]
	.Enabled Relations{0} [inherited]
		.Contains[bool] [CA-R-1945] [inherited] [kind-level capability]
			:False [inherited]
			:True [inherited]
	.id[string]{1} [CA-R-728; CA-R-2102] [inherited]
	.Label[string]{0..1} [CA-R-1594; CA-R-2102] [inherited]
	.Local Scope Unit[string]{0} [CA-R-2102; CA-R-2132; CA-R-2152; CA-R-920] [inherited]
	.Owner[string]{1} [CA-R-2152]
	.Relations{0} [CA-R-2102] [inherited]
	.Status[string]{1} [CA-R-1412; CA-R-1947; CA-R-2102] [inherited]
		:Active [inherited]
		:Archived [inherited]
		:Draft [inherited]
	.Subjects{0} [CA-R-1198; CA-R-2102] [inherited]
		.Depends On[string]{0+} [CA-R-1198] [inherited]
		.Governs[string]{1} [CA-R-1363] [inherited]
	.Target Scope Unit[string]{1} [CA-R-1595; CA-R-2102; CA-R-2152] [inherited]
	.Tier[int]{1} [CA-R-2102; CA-R-2124; CA-R-2125; CA-R-2132] [inherited]
		:-1
	.Type[string]{1} [CA-R-2102] [inherited]
		:Project Goal
	.Updated At[datetime]{1} [CA-R-1416; CA-R-2102] [inherited]
	.version_number[int]{1} [CA-R-1415; CA-R-2102] [inherited]
```

### Release

```yaml
subjects:
  governs: 'Model::CAPRMEDIO::Continuant/History/Release'
```

```text
Release
	.ID [CA-R-2172]
```

### Scope Unit

```yaml
subjects:
  governs: 'Model::CAPRMEDIO::Continuant/Structural Unit/Scope Unit'
```

```text
Scope Unit
	.Children
	.Expansion Boundary
	.ID [CA-R-1988]
	.Label [CA-R-972]
	.Local Order [CA-R-1763]
	.Name[string, unique(Scope Units in the Project)] [CA-R-970]
	.Navigational Order Number [CA-R-978]
	.Parent
	.Path [CA-R-1764; CA-R-2133; CA-R-2134]
	.Project Boundary Position [CA-R-961]
	.Scope
```

### Project

```yaml
subjects:
  governs: 'Model::CAPRMEDIO::Continuant/Structural Unit/Scope Unit/Project'
```

```text
Project
	.Children [inherited]
	.Expansion Boundary [inherited]
	.Framework Settings [CA-R-1402]
		.Artifact Timestamp Timezone [CA-R-1977]
		.Authority Modes
		.Code-Root Locators [CA-R-1978]
		.Confidence [CA-R-1979]
			.Necessary Information Threshold
			.Semantic Resolution Threshold
		.Extension Selections
		.Framework Control-Root Locator [CA-R-1980]
		.Identifier
		.implementation
			.retry_limit
		.Interaction [CA-R-1982]
			.Reporting Mode
				.Effects
				.Mandatory Information
		.Parameter Resolution [CA-R-1983]
		.Parameter Resolution Validation
		.Tool Selections
	.Graph Dimensions
	.ID [CA-R-1988] [inherited]
	.Label [CA-R-972] [inherited]
	.Local Order [CA-R-1763] [inherited]
	.Minimum Model
	.Name[string, unique(Scope Units in the Project)] [CA-R-970] [inherited]
	.Navigational Order Number [CA-R-978] [inherited]
	.Operator Registry [CA-R-1984]
	.Parent{0} [CA-R-2220] [inherited] [proposed]
	.Path [CA-R-1764; CA-R-2133; CA-R-2134] [inherited]
	.Principle Universe
	.Project Boundary Position [CA-R-961] [inherited]
	.Scope [inherited]
	.Settings [CA-R-1738]
		.Atom Prefix
		.Identifier
		.Obsolete Names
		.Project Name
		.Temporary State
	.Structure [CA-R-1483]
```

### Projection

```yaml
subjects:
  governs: 'Model::CAPRMEDIO::Continuant/Projection'
```

```text
Projection
	.Authority
	.ID
	.Updated At
```

### Terms Projection

```yaml
subjects:
  governs: 'Model::CAPRMEDIO::Continuant/Projection/Terms Projection'
```

```text
Terms Projection
	.Authority [inherited]
	.ID [inherited]
	.Updated At [inherited]
```

### Term

```yaml
subjects:
  governs: 'Model::CAPRMEDIO::Continuant/Term'
```

```text
Term
	.Name
	.Type
```

### Execution

```yaml
subjects:
  governs: 'Model::CAPRMEDIO::Occurrent/Execution'
```

```text
Execution
	.Execution ID [CA-R-1973]
	.Result [proposed]
```

### Action Run

```yaml
subjects:
  governs: 'Model::CAPRMEDIO::Occurrent/Execution/Action Run'
```

```text
Action Run
	.Execution ID [CA-R-1973] [inherited]
	.Result [inherited] [proposed]
```

### Container Run

```yaml
subjects:
  governs: 'Model::CAPRMEDIO::Occurrent/Execution/Container Run'
```

```text
Container Run
	.Execution ID [CA-R-1973] [inherited]
	.Result [inherited] [proposed]
```

### Process Run

```yaml
subjects:
  governs: 'Model::CAPRMEDIO::Occurrent/Execution/Process Run'
```

```text
Process Run
	.Execution ID [CA-R-1973] [inherited]
	.Result [inherited] [proposed]
```

### Step Run

```yaml
subjects:
  governs: 'Model::CAPRMEDIO::Occurrent/Execution/Step Run'
```

```text
Step Run
	.Agentic Step Execution Context [CA-R-1527]
	.Execution Context
	.Execution ID [CA-R-1973] [inherited]
	.Invocation Context
	.Result [inherited] [proposed]
```

### Workflow Run

```yaml
subjects:
  governs: 'Model::CAPRMEDIO::Occurrent/Execution/Workflow Run'
```

```text
Workflow Run
	.Coverage
	.Execution ID [CA-R-1973] [inherited]
	.Implementation Retry Limit
	.Provenance
	.Result [inherited] [proposed]
	.Retry
	.Retry and Repair Results
	.Source Admission
```

### Carrier

```yaml
subjects:
  governs: 'Model::CAPRMEDIO::Carrier'
```

```text
Carrier
	.Canonical Address [CA-R-1949]
		.Segment [CA-R-1948]
	.Format [CA-R-1950]
	.ID
```

### Database

```yaml
subjects:
  governs: 'Model::CAPRMEDIO::Carrier/Database'
```

```text
Database
	.Canonical Address [CA-R-1949] [inherited]
		.Segment [CA-R-1948] [inherited]
	.Format [CA-R-1950] [inherited]
	.ID [inherited]
```

### Directory

```yaml
subjects:
  governs: 'Model::CAPRMEDIO::Carrier/Directory'
```

```text
Directory
	.Canonical Address [CA-R-1949] [inherited]
		.Segment [CA-R-1948] [inherited]
	.Format [CA-R-1950] [inherited]
	.ID [inherited]
	.Name [CA-R-1952]
	.Numeric Prefix [CA-R-1953]
	.Path [CA-R-1954]
```

### Docker Image

```yaml
subjects:
  governs: 'Model::CAPRMEDIO::Carrier/Docker Image'
```

```text
Docker Image
	.Canonical Address [CA-R-1949] [inherited]
		.Segment [CA-R-1948] [inherited]
	.Format [CA-R-1950] [inherited]
	.ID [inherited]
```

### File

```yaml
subjects:
  governs: 'Model::CAPRMEDIO::Carrier/File'
```

```text
File
	.Canonical Address [CA-R-1949] [inherited]
		.Segment [CA-R-1948] [inherited]
	.Extension [CA-R-1974]
	.Filename [CA-R-1975]
		.Scope Unit Token
	.Format [CA-R-1950] [inherited]
	.ID [inherited]
	.Main Content
		.CCE Operator
		.Paragraph
	.Path [CA-R-1976]
	.YAML Frontmatter
		.Scalar
```

### Git Branch

```yaml
subjects:
  governs: 'Model::CAPRMEDIO::Carrier/Git Branch'
```

```text
Git Branch
	.Canonical Address [CA-R-1949] [inherited]
		.Segment [CA-R-1948] [inherited]
	.Format [CA-R-1950] [inherited]
	.ID [inherited]
```

### Git Commit

```yaml
subjects:
  governs: 'Model::CAPRMEDIO::Carrier/Git Commit'
```

```text
Git Commit
	.Canonical Address [CA-R-1949] [inherited]
		.Segment [CA-R-1948] [inherited]
	.Format [CA-R-1950] [inherited]
	.ID [inherited]
```

### Git Index

```yaml
subjects:
  governs: 'Model::CAPRMEDIO::Carrier/Git Index'
```

```text
Git Index
	.Canonical Address [CA-R-1949] [inherited]
		.Segment [CA-R-1948] [inherited]
	.Format [CA-R-1950] [inherited]
	.ID [inherited]
```

### Git Repository

```yaml
subjects:
  governs: 'Model::CAPRMEDIO::Carrier/Git Repository'
```

```text
Git Repository
	.Canonical Address [CA-R-1949] [inherited]
		.Segment [CA-R-1948] [inherited]
	.Format [CA-R-1950] [inherited]
	.ID [inherited]
```

### Pull Request

```yaml
subjects:
  governs: 'Model::CAPRMEDIO::Carrier/Pull Request'
```

```text
Pull Request
	.Canonical Address [CA-R-1949] [inherited]
		.Segment [CA-R-1948] [inherited]
	.Format [CA-R-1950] [inherited]
	.ID [inherited]
```

### Graph Syntax

```yaml
subjects:
  governs: 'Model::CAPRMEDIO::Graph Syntax'
```

```text
Graph Syntax
	.Cardinality Notation [proposed]
	.Format Notation [proposed]
	.Reference Notation [proposed]
	.Relation Notation [proposed]
```

### Relation

```yaml
subjects:
  governs: 'Model::CAPRMEDIO::Graph Syntax::Relation'
```

```text
Relation
	.Authority
	.Declared Direction[string] [CA-R-806]
	.Derived Inverse[string] [CA-R-806]
	.Meaning[string]{1} [CA-R-806]
	.Name[string]{1} [CA-R-806]
	.Transitivity [CA-R-806]
```

### Format

```yaml
subjects:
  governs: 'Model::CAPRMEDIO::Graph Syntax::Format'
```

```text
Format
	.Data Type[string]{1} [proposed]
	.Uniqueness Selection[string]{0..1} [proposed]
```

### bool

```yaml
subjects:
  governs: 'Model::CAPRMEDIO::Graph Syntax::Format/bool'
```

```text
bool
	.Data Type[string]{1} [inherited] [proposed]
	.Uniqueness Selection[string]{0..1} [inherited] [proposed]
```

### datetime

```yaml
subjects:
  governs: 'Model::CAPRMEDIO::Graph Syntax::Format/datetime'
```

```text
datetime
	.Data Type[string]{1} [inherited] [proposed]
	.Uniqueness Selection[string]{0..1} [inherited] [proposed]
```

### decimal

```yaml
subjects:
  governs: 'Model::CAPRMEDIO::Graph Syntax::Format/decimal'
```

```text
decimal
	.Data Type[string]{1} [inherited] [proposed]
	.Uniqueness Selection[string]{0..1} [inherited] [proposed]
```

### float

```yaml
subjects:
  governs: 'Model::CAPRMEDIO::Graph Syntax::Format/float'
```

```text
float
	.Data Type[string]{1} [inherited] [proposed]
	.Uniqueness Selection[string]{0..1} [inherited] [proposed]
```

### int

```yaml
subjects:
  governs: 'Model::CAPRMEDIO::Graph Syntax::Format/int'
```

```text
int
	.Data Type[string]{1} [inherited] [proposed]
	.Uniqueness Selection[string]{0..1} [inherited] [proposed]
```

### string

```yaml
subjects:
  governs: 'Model::CAPRMEDIO::Graph Syntax::Format/string'
```

```text
string
	.Data Type[string]{1} [inherited] [proposed]
	.Uniqueness Selection[string]{0..1} [inherited] [proposed]
```

## Cardinality notation

| Notation | Meaning | Example |
| --- | --- | --- |
| `{n}` | Exactly n | `{1}`: exactly one |
| `{n+}` | At least n, no upper bound | `{2+}`: two or more |
| `{n..m}` | From n to m, inclusive | `{2..5}`: two through five |
| `{0}` | No direct values or no contained parts | A group can still have declared child properties |
| `{0+}` | Zero or more direct values or parts | An optional multi-value property |
| `{1+}` | One or more | At least one part or value |
| `{0..1}` | Zero or one | An optional single value |
| `{0..m}` | At most m | `{0..3}`: zero through three |

The suffix counts only direct values at that path, or immediate parts per whole after >. It never counts nested keys. Grouping subjects{0} permits governs{1} and dependency{0+} as independently counted children. YAML sequences carry multiple values under one unique property key; list is not a value Format. The exactly-one immediate whole rule is unchanged. CA-A-1283 records this decision.

## Deferred formula proposal

General formula expressions are preserved separately in [CA-A-1282](../CA-A-1282-SPECIFICATION_PROPOSAL--defer-general-formula-expressions.md), rather than admitted in this Model Draft. This includes composed ID values, property-value interpolation, formula grouping, function-style uniqueness expressions and calculated counts. Existing scalar IDs and their governing prose rules remain unchanged. Bracketed conditions and implicit value materialization remain separate proposals under A1291, outside the current review. The explicit execution function remains deferred. Cardinalities, formats, literal allowed values, relationship operators and existing-kind references stay in scope.

## Property and rule qualifications

Under A1296, YAML null and an empty string each count as one direct value; an omitted property has zero. YAML interpretation determines the value. Its Format and applicable prose conditions decide admissibility; the count alone does not. There is no universal null or empty-string prohibition.

Subject values use string under CA-A-1285. The basic format check validates the string and its admitted Model notation without requiring the target to pre-exist its defining Atom. A Definition may introduce its entity and governed path together. Syntax alone does not define the entity or grant authority.

- `id` and `version_number` use the Operator's latest example spellings. They do not rename `atom_id` or `version` in YAML. Use atom.version_number for the YAML part and atom.content.claim for the Markdown part. No atom.property, property/text subgroup or colon-based lookup layer is introduced.
- Version Number is positive and increases for updates. Tier uses [int] in this review packet. Its lower bound is -1; the numeric and more-specific conditions stay in prose under A1297: Project ordinary >=0, other ordinary >=1, Project Goal -1 with Operator ownership. No case-specific lookup function or conditional expression is needed. Numbers are graph ordering, not a second Global Tier.
- RMED content.claim_scope can be omitted only when the Claim covers the whole governed thing/topic and whole owning context. Conditional requirements still apply to a property shown as 0..1. Other Content Roles retain their registered scope contract.
- Analysis Question/Analysis counts depend on its applicable Type. Analysis Done is admitted by the applicable Analysis Report/Rationale rules, not asserted as a new universal Status on every Analysis Type.
- Every complete RMED Atom carries exactly one content.claim. Its own direct text is one required prose value. Only R admits optional content.claim.formal_claim with one fenced formal expression for now; M/E/D stay prose, including their syntax/format/relation policies and decisions. Illustrative code does not create an operative formal child. A Definition may combine required prose and optional complementary formal structure as one Type-defined unit, not separate Atoms for each representation or condition. Semantics is outside Claim and adds no operative constraints.
- The RMED section order is ## Summary, optional ## Claim scope, required ## Claim, optional ## Semantics, optional ## Details. R alone may add optional ### Formal claim under Claim. The Summary value is below ## Summary, not substituted into the heading. Optional sections are omitted when absent. A formal child needs a defined syntax/schema. All top-level RMED sections are siblings at ##; Summary never contains Claim. Heading hierarchy maps Claim → Formal claim to content.claim.formal_claim; normalized components are lowercase with spaces replaced by underscores and characters other than letters, numbers, underscore and hyphen stripped.
- Enabled Relations.Contains is a kind-level capability, with base default False and Plan/Workflow/Step enabling True. It is not a mandatory Boolean field to add to every Atom instance. The existing Step rule CA-R-1992 still describes nested Steps; this Draft retains its enabling value but follows the Operator's newer distinct-Substep decision for the contained kind.
- The Project Goal Owner targets Operator, Target Scope Unit targets Project, and its single Tier is exactly -1. Its absence of Local Scope Unit is the explicit exception, not permission to omit that field on ordinary Atoms.
- Governing Objects classifies Atom and Governing Configuration without granting additional authority to any Content Role. Structural Unit classifies Scope Unit; Project specializes Scope Unit and is its single parentless root. Scope Units recursively contain Scope Units and may contain Atom/Projection parts. No numeric structural rank or ownership-field rename is introduced by these groups.
- Event Record is declared only under History/Journal. Project Implementation specializes Package and is the root Package. Implementation is only a section heading. Package contains nested Packages, Modules, Prompts, runtime/evaluation Assets and Documentation; Code Units belong inside Modules, with Class and Function specializations. There is no separate Code kind in this proposed model. Prompt is executable instructions for an LLM AI Agent engine; Module is executable on its language engine; both runtime code and evaluation code, including tests, are Modules. Asset is non-executable Implementation content needed by runtime or evaluations. Documentation provides descriptive/reference information separately from those required inputs. Neither definition automatically captures every non-executable repository file. Module's one File Carrier and Package's proposed Directory representation remain distinct Delivery concerns. Documentation is a Package part separate from Asset. Resources is retired in this proposal under CA-A-1278; its non-executable implementation inputs specialize Asset. Containment does not confer property inheritance.
- Projection remains a direct Continuant and Terms Projection specializes it. Term remains separate as in the Operator's tree. This classification does not create a Terms Projection artifact or start Terms Graph implementation.
- Carrier, Actor, Execution, Project, History, Projection and their descendants do not inherit Scope Unit fields through the former Project Model grouping. The old projection's spurious Scope Unit subtree is excluded.
- Current source rules and operative formal graph-rule paths still use older Subject paths. This review Draft does not claim those paths were migrated to Model.

## Deferred or unresolved details

- Format has a new Definition Draft; individual primitive-format definitions remain to be completed before adoption. This Draft does not assert a closed primitive vocabulary, specific numeric precision, float special-value policy or reference encoding.
- Formula design and property-value bindings remain outside this adoption increment under CA-A-1282. A1295 permits future functions only when recurring patterns establish reusable operations that reduce overall complexity; no per-case or per-instance function proliferation is admitted. No new ID component field or contextual named Selection is created.
- Substep is a leaf: it calls one Action with parameters, cannot call a Workflow and cannot contain further Substeps. A leaf Step can call one Action or one Workflow with parameters; a Step containing Substeps has no own call. A1262–A1264 record these decisions. Catalog reconciliation and Substep numeric identity remain preparation work, not an open choice about the settled container hierarchy. Containment supplies no inheritance.
- Code Unit is declared under Module, with Class and Function as specializations. Modules belong to Packages; the former Code-versus-Package question is closed. Package is a declared kind; Project Implementation is its root specialization, not a containing Implementation kind. Tool is not a separate primary kind under CA-A-1273: use Scope Unit instances and existing Package implementation structure. R2197 is a retirement candidate; R2205 meaning is preserved in Engineering API Self Documentation. R2204 Effect Result meaning is mapped to Execution.Result under CA-A-1276; its API result contract stays in Engineering/API. Current retirement is pending. Current source definitions are not deleted by these candidate placements.
- The Operator confirms Workflow >{1+} Step >{0+} Substep. CA-A-1279 reconfirms this settled hierarchy with the latest cardinality spelling. It is prepared in Definition Drafts; Current source adoption is still pending.
- Complete Type inventories and property formats/counts absent from sources remain deferred. Useful legacy graph constraints need incorporation into the appropriate Definition Claims before retiring their Current sources. No Graph Rule instance registry or substitute Rule population is introduced.
- The read-only property inventory retains older direct labels for evidence. Retired Substance, Atom.Entity, duplicate Governed Subject vs Subjects.Governs, and accidental inherited Scope Unit fields are not copied into the Draft. No extra Scope Unit Status or Global Tier is introduced.

## Drafts and basis

- CA-A-1238: Candidate #12 primary-kind proposal, refined here without editing it.
- CA-A-1236: accepted notation decisions and existing successor Drafts.
- [Value Format Definition Draft](../../101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/draft/CA-R-draft-CORE_META_MODEL-DEFINITION--define-value-format.md).
- [CA-A-1241: unified RMED Claim and section-layout Draft packet](../CA-A-1241-SPECIFICATION_PROPOSAL--use-one-content-claim-and-stable-rmed-headings.md). This latest decision supersedes the earlier frontmatter-Claim exception; these property blocks describe the successor proposal, not an already completed source migration.
- [CA-A-1242: model constraints in Definitions and Graph Syntax](../CA-A-1242-SPECIFICATION_PROPOSAL--define-model-constraints-with-one-formal-claim.md). This later decision removes the Graph Rule branch and special Atom Type; marked legacy packet Drafts are not promotion candidates.
- [CA-A-1243: Type-defined Claim and optional formal child](../CA-A-1243-SPECIFICATION_PROPOSAL--define-type-specific-claim-and-formal-child.md). This latest refinement permits prose plus a formal child within the same Claim and registers the chosen heading-to-property spelling.
- [CA-A-1244: operative formal Claims are R-only for now](../CA-A-1244-SPECIFICATION_PROPOSAL--limit-operative-formal-claims-to-requirements.md). M/E/D retain prose Claims while participating in the shared layout migration.
- [CA-A-1245: Event Record exists only in Journal](../CA-A-1245-SPECIFICATION_PROPOSAL--require-journal-containment-for-event-records.md).
- [Event Record Definition Draft](../../101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/draft/CA-R-draft-CORE_META_MODEL-DEFINITION--define-event-record.md).
- [CA-A-1246: historical Code wrapper proposal, superseded by CA-A-1254 and CA-A-1259](../CA-A-1246-SPECIFICATION_PROPOSAL--require-implementation-containment-for-code.md).
- [CA-A-1247: Asset scope resolved](../CA-A-1247-SPECIFICATION_PROPOSAL--scope-assets-to-non-executable-implementation-content.md).
- [CA-A-1248: Continuant groups and structural parts](../CA-A-1248-SPECIFICATION_PROPOSAL--group-continuants-as-governing-and-structural-objects.md).
- [CA-A-1249: Projection and Terms Projection](../CA-A-1249-SPECIFICATION_PROPOSAL--classify-terms-projection-under-projection.md).
- [CA-A-1250: Code Units, Packages and file-level Modules](../CA-A-1250-SPECIFICATION_PROPOSAL--refine-code-units-packages-and-file-level-modules.md).
- CA-A-1258 makes Project the root Scope Unit. CA-A-1259 makes Project Implementation the root Package and removes Implementation as a kind. Their latest decisions supersede older wrapper paths.
- [Package Definition Draft](../../101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/draft/CA-R-2178@3-draft-CORE_META_MODEL-DEFINITION--define-package.md).
- [Module Definition Draft](../../101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/draft/CA-R-2177@3-draft-CORE_META_MODEL-DEFINITION--define-module.md).
- [Prompt Definition Draft](../../101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/draft/CA-R-2179@4-draft-CORE_META_MODEL-DEFINITION--define-prompts.md).
- [Project Implementation Definition Draft](../../101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/draft/CA-R-draft-CORE_META_MODEL-DEFINITION--define-project-implementation.md).
- [CA-A-1268: root Model](../CA-A-1268-SPECIFICATION_PROPOSAL--name-the-root-model.md).
- [CA-A-1269: historical Runtime/Test Package decision, refined by CA-A-1272](../CA-A-1269-SPECIFICATION_PROPOSAL--specialize-packages-for-runtime-and-tests.md).
- [CA-A-1276: actual Execution Result versus API contract](../CA-A-1276-SPECIFICATION_PROPOSAL--separate-execution-result-from-api-result-contract.md).
- [Execution Result Definition Draft](../../101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/draft/CA-R-draft-CORE_META_MODEL-DEFINITION--define-execution-result.md).
- [API Result Contract Definition Draft](../../101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/draft/CA-R-draft-CORE_META_MODEL-DEFINITION--define-api-result-contract.md).
- [CA-A-1273: no Tool primary kind](../CA-A-1273-SPECIFICATION_PROPOSAL--use-scope-units-and-packages-without-a-tool-kind.md).
- [CA-A-1274: API umbrella](../CA-A-1274-SPECIFICATION_PROPOSAL--use-api-as-the-interface-umbrella.md).
- [CA-A-1275: Engineering API Self Documentation](../CA-A-1275-SPECIFICATION_PROPOSAL--place-package-api-self-documentation-in-engineering.md).
- [Package API Definition Draft](../../101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/draft/CA-R-draft-CORE_META_MODEL-DEFINITION--define-package-api.md).
- [API Self Documentation Definition Draft](../../101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/draft/CA-R-draft-CORE_META_MODEL-DEFINITION--define-api-self-documentation.md).
- [CA-A-1272: Eval Package includes Modules and Prompts](../CA-A-1272-SPECIFICATION_PROPOSAL--rename-test-package-to-eval-package.md).
- [CA-A-1278: retire Resources and classify content by purpose](../CA-A-1278-SPECIFICATION_PROPOSAL--retire-resources-and-classify-content-by-purpose.md).
- [CA-A-1271: logical Asset versus File Carrier](../CA-A-1271-SPECIFICATION_PROPOSAL--keep-asset-distinct-from-file-carrier.md).
- [CA-A-1270: historical Asset File naming, superseded by CA-A-1271](../CA-A-1270-SPECIFICATION_PROPOSAL--name-the-non-executable-item-asset-file.md).
- [Model Definition Draft](../../101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/draft/CA-R-draft-CORE_META_MODEL-DEFINITION--define-model.md).
- [Runtime Package Definition Draft](../../101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/draft/CA-R-draft-CORE_META_MODEL-DEFINITION--define-runtime-package.md).
- [Eval Package Definition Draft](../../101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/draft/CA-R-draft-CORE_META_MODEL-DEFINITION--define-eval-package.md).
- [CA-A-1267: runtime/test usage for Modules and Assets](../CA-A-1267-SPECIFICATION_PROPOSAL--allow-modules-and-assets-for-runtime-or-tests.md).
- [CA-A-1266: runtime Assets versus Documentation](../CA-A-1266-SPECIFICATION_PROPOSAL--distinguish-runtime-assets-from-documentation.md).
- [Documentation Definition Draft](../../101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/draft/CA-R-2180@4-draft-CORE_META_MODEL-DEFINITION--define-documentation.md).
- [CA-A-1282: general formula expressions deferred](../CA-A-1282-SPECIFICATION_PROPOSAL--defer-general-formula-expressions.md). Earlier formula discussions remain proposals, not admitted syntax here.
- CA-A-1257 adds missing Content Role Types; Plan Labels remain properties, not primary kinds.
- CA-A-1256 removes duplicate classification references and confirms Workflow/Step/Substep containment counts.
- Decisions CA-A-1251–CA-A-1253 place Format under Graph Syntax, Code Unit inside Module, and record exactly-one whole per contained part. CA-A-1254 removes Code and organizes Modules and Assets under Package; CA-A-1255 adds Prompt under Package and distinguishes Prompt and Module execution.
- [Governing Objects Definition Draft](../../101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/draft/CA-R-draft-CORE_META_MODEL-DEFINITION--define-governing-objects.md).
- [Structural Unit Definition Draft](../../101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/draft/CA-R-draft-CORE_META_MODEL-DEFINITION--define-structural-unit.md).
- [Asset Definition Draft](../../101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/draft/CA-R-draft-CORE_META_MODEL-DEFINITION--define-implementation-asset.md).
- [Code Unit Definition Draft](../../101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/draft/CA-R-draft-CORE_META_MODEL-DEFINITION--define-code-unit.md).
- [Terms Projection Definition Draft](../../101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/draft/CA-R-draft-CORE_META_MODEL-DEFINITION--define-terms-projection.md).
- [Graph Syntax Definition Draft](../../101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/draft/CA-R-draft-CORE_META_MODEL-DEFINITION--define-graph-syntax.md).
- Current property rules include CA-R-2102, CA-R-1269, CA-R-1947, CA-R-1539, CA-R-1608, CA-R-1875, CA-R-1945, CA-R-1990, CA-R-1991 and CA-R-1995 through CA-R-1999. Carrier and other property references appear inline.
- CA-PROJ-011 was used only as a direct-property inventory. Its inherited marks were not trusted. Governing source definitions and the Operator's latest input determine this Draft.

## General named relations

`Source ((RELATION_TYPE)) Target` expresses the named directed Relation from Source to Target. Use this general form where no short operator exists; it may also spell a defined Relation explicitly without changing its meaning. The name between `((` and `))` identifies one declared Relation Type, not a new kind, arbitrary prose label or automatically registered Relation. Endpoint restrictions and counts come from the Relation definition and constraints in the relevant Model Definition Claim.

There is no separate backward notation. To navigate or display the opposite direction, use the defined derived inverse Relation name in the same form with the endpoints exchanged. Persist the direct fact only, not a second independent inverse fact. No inverse name or inverse meaning is guessed from spelling.

The matching unescaped `((` and `))` delimit the Relation Type name. Existing backslash escaping handles literal delimiter characters. Existing `/`, `//`, `.`, `:`, `::`, `>`, `@(...)` and format/cardinality annotations keep their meanings. The double parentheses are relation syntax, not a function invocation. This decision defines a binary relation expression; it does not silently choose precedence for arbitrary mixed chains or turn a whole relation statement into a node selector for subjects.governs.

The Operator supplied these schema-level examples:

```text
Workflow Run ((IS_EXECUTION_OF)) Workflow
Event Record ((RECORDS)) Workflow Run
Runtime ((EXECUTES)) Workflow Run
```

These expressions connect modeled kinds and do not create actual Runs or records. Their Relation Type definitions and derived-inverse declarations must be authored before source admission; notation alone does not establish that they are already registered. The Runtime in the last expression is the live executor, not the Engineering topic or stored engine Code.

Decision record: [CA-A-1240](../CA-A-1240-SPECIFICATION_PROPOSAL--use-named-relation-notation.md).

## Definition, execution and record connections

```text
Workflow Run ((IS_EXECUTION_OF)) Workflow
Event Record ((RECORDS)) Workflow Run
```

Every Workflow Run executes exactly one Workflow; this binding is stated in prose rather than an undefined suffix on a named relation. Workflow is the reusable definition; Workflow Run is an actual Occurrent; Event Record is its persistent description in Journal. The displayed RECORDS target is one supported case, not a closed range restricting every record to Workflow Run. The inverse views HAS_EXECUTION and IS_RECORDED_BY are proposed in the two Definition Drafts; direct facts are stored once. No actual Run or record is created here.

- [IS_EXECUTION_OF Definition Draft](../../101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/draft/CA-R-draft-CORE_META_MODEL-DEFINITION--define-is-execution-of-relation.md).
- [RECORDS Definition Draft](../../101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/draft/CA-R-draft-CORE_META_MODEL-DEFINITION--define-records-relation.md).
- [Workflow Run Definition Draft](../../101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/draft/CA-R-1510@17-draft-CORE_META_MODEL-DEFINITION--define-workflow-run.md).
- [CA-A-1260: the two-link increment](../CA-A-1260-SPECIFICATION_PROPOSAL--connect-workflow-definitions-runs-and-event-records.md).

These Relation Definitions are prepared, not promoted or registered. The earlier Runtime EXECUTES example remains separately undefined in this increment.

## Step and Substep call boundaries

A leaf Step calls one Action or one Workflow with parameters. A Step containing Substeps makes no call of its own. A Substep is a leaf that calls one Action with parameters: no Workflow calls and no nested Substeps.

```text
Workflow >{1+} Step
Step >{0+} Substep
Substep >{0} @(Substep)
```

Containment connects a Workflow to its Steps and a Step to its Substeps. It does not mean the caller contains the called Workflow or Action definition. No wrapper Action or new execution kind is introduced for Workflow calls.

- [A1262: leaf Substeps](../CA-A-1262-SPECIFICATION_PROPOSAL--keep-substeps-as-leaves.md).
- [A1263: Steps may call Workflows; Update Atom example](../CA-A-1263-SPECIFICATION_PROPOSAL--allow-steps-to-call-workflows.md).
- [A1264: Workflow calls only in Steps](../CA-A-1264-SPECIFICATION_PROPOSAL--limit-workflow-calls-to-steps.md).
- [A1277: recursive Workflow calls](../CA-A-1277-SPECIFICATION_PROPOSAL--allow-recursive-workflow-calls.md).
- [A1279: settled Workflow container hierarchy](../CA-A-1279-SPECIFICATION_PROPOSAL--retain-settled-workflow-container-hierarchy.md).
- [A1280: compact cardinality variants](../CA-A-1280-SPECIFICATION_PROPOSAL--use-compact-cardinality-notation.md).
- [A1283: independent direct-value counts and grouping {0}](../CA-A-1283-SPECIFICATION_PROPOSAL--count-direct-values-independently-at-each-property-path.md).
- [A1284: omitted cardinality stays undefined](../CA-A-1284-SPECIFICATION_PROPOSAL--leave-omitted-cardinality-undefined.md).
- [A1285: string format for Subject paths](../CA-A-1285-SPECIFICATION_PROPOSAL--use-string-format-for-model-subject-paths.md).
- [A1286: nested properties instead of map Format](../CA-A-1286-SPECIFICATION_PROPOSAL--represent-nesting-with-properties-instead-of-map-format.md).
- [A1287: strings instead of ref Format](../CA-A-1287-SPECIFICATION_PROPOSAL--use-strings-instead-of-ref-format.md).
- [A1297: plain Model review scope](../CA-A-1297-SPECIFICATION_PROPOSAL--separate-advanced-expressions-from-the-plain-model-review.md).
- [A1299: sibling Summary and Claim headings](../CA-A-1299-SPECIFICATION_PROPOSAL--use-sibling-summary-and-claim-headings.md).
- [A1300: plain Model review repairs](../CA-A-1300-SPECIFICATION_PROPOSAL--repair-the-plain-model-packet-with-settled-decisions.md).
- [Relation Definition replacement Draft](../../101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/draft/CA-R-draft-CORE_META_MODEL-DEFINITION--define-relation.md).
- [A1294: simple Tier bound and prose conditions](../CA-A-1294-SPECIFICATION_PROPOSAL--keep-tier-minimum-formal-and-owner-specific-rules-in-prose.md).
- [A1295: reusable functions only when they reduce complexity](../CA-A-1295-SPECIFICATION_PROPOSAL--introduce-functions-only-for-reusable-patterns-that-reduce-complexity.md).
- [A1296: YAML null and empty strings count as values](../CA-A-1296-SPECIFICATION_PROPOSAL--count-yaml-null-and-empty-strings-as-values.md).
- [Numeric Tier Definition Draft](../../101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/draft/CA-R-2124@9-draft-CORE_META_MODEL-DEFINITION--define-numeric-tier-as-an-atom-property.md).

- [Cardinality Notation Definition Draft](../../101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/draft/CA-R-draft-CORE_META_MODEL-DEFINITION--define-cardinality-notation.md).
- [Step Definition Draft](../../101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/draft/CA-R-1509@22-draft-CORE_META_MODEL-DEFINITION--define-step.md).
- [Substep Definition Draft](../../101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/draft/CA-R-draft-CORE_META_MODEL-DEFINITION--define-substep.md).
- [Step Run Definition Draft](../../101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/draft/CA-R-1511@20-draft-CORE_META_MODEL--define-step-run.md).

These are prepared Definition changes, not Current adoption or Engine implementation. CA-A-1277 permits direct and indirect Workflow recursion: the call graph need not be acyclic. No mandatory recursion-depth limit or termination proof is added.

## Latest root and Type supersession

A1302 supersedes this root/classification and bare Definition-Type naming. Use CA-A-1302@1-draft-SPECIFICATION_PROPOSAL--entity-graph-candidate-with-four-root-branches.md for the latest top-level Entity candidate. Retain this detailed inventory as remapping input, not as the latest root authority.
