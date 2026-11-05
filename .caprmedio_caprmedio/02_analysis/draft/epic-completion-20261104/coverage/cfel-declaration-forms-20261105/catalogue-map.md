# Proposed CFEL item owners

User approved individual CFEL Subjects. Semantic labels below remain proposed unless otherwise noted; no Category carrier is introduced.

| Item | Form | Active Subject |
|---|---|---|
| `+` | Operator Declaration | `CAPRMEDIO_MODEL/CFEL/Operator//Addition` |
| `==` | Operator Declaration | `CAPRMEDIO_MODEL/CFEL/Operator//Required Value` |
| `=` | Operator Declaration | `CAPRMEDIO_MODEL/CFEL/Operator//Equality` |
| `>=` | Operator Declaration | `CAPRMEDIO_MODEL/CFEL/Operator//Greater Than or Equal` |
| `>` | Operator Declaration | `CAPRMEDIO_MODEL/CFEL/Operator//Greater Than` |
| `<=` | Operator Declaration | `CAPRMEDIO_MODEL/CFEL/Operator//Less Than or Equal` |
| `<` | Operator Declaration | `CAPRMEDIO_MODEL/CFEL/Operator//Less Than` |
| `!=` | Operator Declaration | `CAPRMEDIO_MODEL/CFEL/Operator//Inequality` |
| `()` | Operator Declaration | `CAPRMEDIO_MODEL/CFEL/Operator//Grouping` |
| `*` | Operator Declaration | `CAPRMEDIO_MODEL/CFEL/Operator//Immediate Property Selection` |
| `**` | Operator Declaration | `CAPRMEDIO_MODEL/CFEL/Operator//Recursive Property Selection` |
| `$ participant selection` | Operator Declaration | `CAPRMEDIO_MODEL/CFEL/Operator//Participant Binding` |
| `[] Format` | Operator Declaration | `CAPRMEDIO_MODEL/CFEL/Operator//Format` |
| `<> Model reference` | Operator Declaration | `CAPRMEDIO_MODEL/CFEL/Operator//Model Reference` |
| `in` | Operator Declaration | `CAPRMEDIO_MODEL/CFEL/Operator//Membership` |
| `not in` | Operator Declaration | `CAPRMEDIO_MODEL/CFEL/Operator//Membership` |
| `!() delivery exclusion` | Operator Declaration | `CAPRMEDIO_MODEL/CFEL/Operator//Delivery Exclusion` |
| `>> delivery` | Operator Declaration | `CAPRMEDIO_MODEL/CFEL/Operator//Delivery` |
| `?== default` | Operator Declaration | `CAPRMEDIO_MODEL/CFEL/Operator//Default` |
| `AND` | Operator Declaration | `CAPRMEDIO_MODEL/CFEL/Operator//Conjunction` |
| `OR` | Operator Declaration | `CAPRMEDIO_MODEL/CFEL/Operator//Disjunction` |
| `FOR EACH` | Construct Declaration | `CAPRMEDIO_MODEL/CFEL/Construct//Universal Quantification` |
| `IF / THEN` | Construct Declaration | `CAPRMEDIO_MODEL/CFEL/Construct//Conditional` |
| `IF / THEN / ELSE` | Construct Declaration | `CAPRMEDIO_MODEL/CFEL/Construct//Conditional` |
| `((Relation))` | Operator Declaration | `CAPRMEDIO_MODEL/CFEL/Operator//Relation Direction` |
| `<((Relation))` | Operator Declaration | `CAPRMEDIO_MODEL/CFEL/Operator//Relation Direction` |
| `HAS_ALLOWED_VALUE :=` | Relation Declaration | `CAPRMEDIO_MODEL/CFEL/Relation//HAS_ALLOWED_VALUE` |
| `HAS_VALUE_CONSTRAINT ::` | Relation Declaration | `CAPRMEDIO_MODEL/CFEL/Relation//HAS_VALUE_CONSTRAINT` |
| `IS_PROPERTY_OF .` | Relation Declaration | `CAPRMEDIO_MODEL/CFEL/Relation//IS_PROPERTY_OF` |
| `HAS_NARROWER //` | Relation Declaration | `CAPRMEDIO_MODEL/CFEL/Relation//HAS_NARROWER` |
| `CONTAINS /` | Relation Declaration | `CAPRMEDIO_MODEL/CFEL/Relation//CONTAINS` |
| `IS_CONTAINED_BY +>` | Relation Declaration | `CAPRMEDIO_MODEL/CFEL/Relation//IS_CONTAINED_BY` |
| `HAS_CLASSIFICATION >| and |<` | Relation Declaration | `CAPRMEDIO_MODEL/CFEL/Relation//HAS_CLASSIFICATION` |
| `HAS_INVERSE <-->` | Relation Declaration | `CAPRMEDIO_MODEL/CFEL/Relation//HAS_INVERSE` |
| `qualified Subject :=` | Relation Declaration | `CAPRMEDIO_MODEL/CFEL/Relation//HAS_ALLOWED_VALUE` |
| `VALUES` | Function Declaration | `CAPRMEDIO_MODEL/CFEL/Function//VALUES` |
| `COUNT` | Function Declaration | `CAPRMEDIO_MODEL/CFEL/Function//COUNT` |
| `MAX` | Function Declaration | `CAPRMEDIO_MODEL/CFEL/Function//MAX` |
| `LOOKUP` | Function Declaration | `CAPRMEDIO_MODEL/CFEL/Function//LOOKUP` |
| `FENCED_LABELS` | Function Declaration | `CAPRMEDIO_MODEL/CFEL/Function//FENCED_LABELS` |
| `alias` | Function Declaration | `CAPRMEDIO_MODEL/CFEL/Function//alias` |
| `UNIQUE` | Function Declaration | `CAPRMEDIO_MODEL/CFEL/Function//UNIQUE` |
| `DETERMINES` | Function Declaration | `CAPRMEDIO_MODEL/CFEL/Function//DETERMINES` |
| `DISTINCT` | Function Declaration | `CAPRMEDIO_MODEL/CFEL/Function//COUNT` |
| `;` | Operator Declaration | `CAPRMEDIO_MODEL/CFEL/Operator//Expression Separator` |
| `# model / # instances` | retained generic CFEL language Declaration | `CAPRMEDIO_MODEL/CFEL` |
| `: FOR EACH delimiter` | Construct Declaration | `CAPRMEDIO_MODEL/CFEL/Construct//Universal Quantification` |
| `| HAV alternatives` | Relation Declaration | `CAPRMEDIO_MODEL/CFEL/Relation//HAS_ALLOWED_VALUE` |
| `, in list` | Operator Declaration | `CAPRMEDIO_MODEL/CFEL/Operator//Membership` |

FOR EACH and Conditional are multi-expression Constructs. ELSE behavior and scope remain pending. DISTINCT and punctuation are mapped to their owning item; comments use the retained whole-language Declaration.
