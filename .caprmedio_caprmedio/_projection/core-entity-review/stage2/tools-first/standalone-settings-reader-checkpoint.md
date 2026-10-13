# Standalone Project Settings reader checkpoint — 2026-10-13

Derived evidence for P2354–P2356 under P2300. The Tasks remain Active; this is not runtime or complete receiving admission.

## Accepted boundary

The Operator requested only the new reader, without migrating Settings or existing callers. A schema-valid inspection may return unknown logical Revision and currentness with explicit diagnostics. It must not satisfy an operation that requires verified history. No Journal observation is registered by this work.

The closed Project schema is D366's string marker `2.0`, `project.name`, optional `project.obsolete_names`, `artifacts.identity.project_prefix`, and `paths.control_root`. Unknown fields, legacy sections, missing required values and invalid types are refused without repair. Prior-name absence differs from an explicit empty array. Parsing and I/O remain separate; there is no writer or new public route.

## Source and Plan review

Source author: `settings_review`; independent reviewer: `settings_rules`. All six prior versions were preserved byte-for-byte. Summary, Scope, Subjects and unrelated metadata were preserved. D365 and D392 were not changed. E459 retains the existing General and Standard constraints.

| Source | Version | SHA-256 |
| --- | --- | --- |
| D366 | 9 | `c784150f0606565346419b44ba38e2333870de6bcbd3bf90e16dae76dbdc8e33` |
| D375 | 10 | `d32280d1b04a033a9398745c8471e731bbca293ffcfe4260d9136c06951c950b` |
| D376 | 9 | `f03248c4d66a550d2c2ad6018b1a42a5cf2ac6aba0488e1d3c38c388ecedb321` |
| E459 | 18 | `38dd54df00e4ceb0ba169311d5f1b91ef8465d2e80af04345b816ec6a63bc03d` |
| M284 | 12 | `c96e4f32db7684b56c0e09050ff10456ba36777828ec0a8d029a9e8c4ffbe921` |
| O206 | 5 | `2a084b05d42816c461019606973a55e7bbb5c71e1bb4a9f61c1c1bbe49ca4411` |

Finite exact-file PRMEDO diagnostics pass for five sources with zero findings or gaps. M284 retains its predecessor's 12 findings and two gaps: its old header lacks explicit identity, Status, Content Role and owner metadata. Named-source inventory therefore refuses M284. Text/history review does not waive this limitation. A narrow header-normalization question has been submitted to the Operator; no permission is inferred from an unrelated MCP status update.

Plan author `plan_closure` and independent reviewer `plan_checks` accepted P2300 v3 and its three bounded Active children P2354–P2356. P2300 v2 is archived exactly. These children cover source alignment, standalone implementation and independent tests; they do not close the parent Configuration Read work.

## Work still open

The reader and independent tests are being implemented. Positive source-bound acceptance must not be fabricated to bypass M284. Pure-schema checks and actual refusal checks are distinct from complete-reader acceptance. History checks must reject old matching receipts superseded by later updates, removals or moves.

Concurrent MCP/runtime and live Project Settings changes already present in this checkout belong to other work. This packet neither includes nor reverts them. The Operator clarified that the current endpoint is `http://127.0.0.1:56317/mcp`; the earlier failure at port 63972 is obsolete. Root independently initialized the current endpoint, listed 33 tools and called the advertised read-only `get_mcp_reload_status` successfully at 2026-10-13 18:34 UTC. Its generation was serving and available with zero calls in flight; client refresh remained unconfirmed. No Workflow ran and no reload, configuration change or Journal observation was performed. These transport diagnostics do not establish admission of the new Settings reader.
