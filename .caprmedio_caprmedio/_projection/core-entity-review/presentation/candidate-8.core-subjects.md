# Core Subject cleanup

Subject-only. Content and Terms Graph implementation are unchanged.

| Atom ID | old Subject → new Subject | Status |
|---|---|---|
| CA-R-1335 | `depends_on`: `CAPRMEDIO Graph` → `Subject/Graph Node/Domain/Continuant/Projection` | Applied |
| CA-R-1347 | `governs`: `Root Term` → `Subject/Graph Node/Domain/Continuant/Term` | Applied |
| CA-R-1454 | `depends_on`: `Definition Atom` → `Subject/Graph Node/Domain/Continuant/Atom/Content Role: Requirement/Type: Definition` | Applied |
| CA-E-382 | `depends_on`: `Root Term` → `Subject/Graph Node/Domain/Continuant/Term` | Applied |
| CA-E-382 | `depends_on`: `CAPRMEDIO Graph` → `Subject/Graph Node/Domain/Continuant/Projection` | Applied |
| CA-E-382 | `depends_on`: `Definition Atom` → `Subject/Graph Node/Domain/Continuant/Atom/Content Role: Requirement/Type: Definition` | Applied |

Duplicate dependencies were merged. The exact Root Term condition remains in its existing content.
