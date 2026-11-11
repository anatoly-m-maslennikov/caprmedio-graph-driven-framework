# Allowed-value operator disposition

The user has classified allowed-value admission as a CFEL operator, not a Node-to-Node Relation. The `IS_ALLOWED_VALUE_OF` Relation Declaration candidate is withdrawn. CA-R-1436 remains Current until its reviewed retirement; this file does not retire it.

The `:` operator owner must retain the admitted meaning of the Current rules: in the applicable qualified context, `X:Y` admits Y as a possible value of X. Admission does not assign Y to an occurrence, establish the number of values, or admit Y in a different context. These constraints come from CA-R-1245 and CA-R-1436; contextual separation is also reflected by CA-R-1346. The operator is distinct from literal value assignment and does not create Node endpoints.

Before retiring CA-R-1436, bind the replacement `:` operator Declaration to its approved source and review all affected Current Subjects, rules, Methods, Evaluations and graph views. CA-R-1245’s Claim and passive Subject currently use the old Relation identity; CA-R-1346 uses it as the active Subject. They need explicit dispositions under the operator owner rather than an automatic Relation-to-operator alias. Historical citations should remain identified as such. The frozen 13-carrier reference set, source hashes and line evidence are in `reclassification-reference-frontier.json`.
