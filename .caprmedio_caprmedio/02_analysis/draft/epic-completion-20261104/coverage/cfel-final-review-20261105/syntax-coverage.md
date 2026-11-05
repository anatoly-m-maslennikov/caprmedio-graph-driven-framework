# CFEL source syntax coverage

Status: **not yet coherent for cutover**. The 49 sources are Drafts. All 49 recorded hashes match their actual bytes and each has exactly one nonempty active Subject field; this checks metadata shape, not semantic correctness.

The JSON report lists all 30 Current Operator-subject source rows and their proposed disposition, the complete reviewed syntax inventory, source pins and all 49 Draft pins. It also includes named CFEL constructs that are not Operator subjects.

The user has approved `$container[<Workflow Run> OR <Step Run>]` as one participant over a union domain. Update R2804 and R2248, and check R2778; an endpoint `{::1}` applies to the union overall. R2821 already defines OR.

Concrete cutover blockers:

- R2816 still gives `Workflow/(.Purpose := Runtime)`, where `/` is the newly proposed containment syntax rather than narrowing. Its repair is separately owned.
- R2247 and R2462 still contain `{:...}` bounds and old `Kind//$variable` bindings. Preserve their graph constraints while migrating their expressions.
- Current R2243, R2563, R2566 and R2585 define cardinality, fenced labels, MAX/filter, and COUNT/DISTINCT using old syntax. Their retained semantics need contextual migration too; final 49 alone are not a complete language cutover.
- Current relation aliases still assign `/` to narrowing, `//` to instance-of, and `<+` to contains. Their staged relation declarations must be applied coherently with the new grammar. The other existing aliases are inventoried, not assumed retired.

The same `:=` has separate qualified-selection and allowed-value contexts. `::` denotes value constraints; all allowed-value alternatives combine by OR and all constraints by AND, including inherited ones; an absent allowed-value group imposes no enumeration restriction. This does not establish a duplicate authority conflict.

This report does not establish a complete consumer migration, semantic validity of each active Subject, runtime behavior or parser conformance.
