# Standalone Project Settings reader checkpoint — 2026-10-13

Derived evidence for P2354–P2356 under P2300. The Tasks remain Active; this is not runtime or complete receiving admission.

## Accepted boundary

The Operator requested only the new reader, without migrating Settings or existing callers. The latest decision supersedes the earlier unknown-history design: read and validate the Settings file; Journal is for history. Ordinary Read does not query Journal, calculate logical Revision/currentness, or require history evidence. No Journal observation is registered by this work.

The closed Project schema is D366's string marker `2.0`, `project.name`, optional `project.obsolete_names`, `artifacts.identity.project_prefix`, and `paths.control_root`. Unknown fields, legacy sections, missing required values and invalid types are refused without repair. Prior-name absence differs from an explicit empty array. Parsing and I/O remain separate; there is no writer or new public route.

## Source and Plan review

Source author: `settings_review`; independent reviewer: `settings_rules`. All six prior versions were preserved byte-for-byte. Summary, Scope, Subjects and unrelated metadata were preserved. D365 and D392 were not changed. E459 retains the existing General and Standard constraints.

| Source | Version | SHA-256 |
| --- | --- | --- |
| D366 | 9 | `c784150f0606565346419b44ba38e2333870de6bcbd3bf90e16dae76dbdc8e33` |
| D375 | 10 | `d32280d1b04a033a9398745c8471e731bbca293ffcfe4260d9136c06951c950b` |
| D376 | 9 | `f03248c4d66a550d2c2ad6018b1a42a5cf2ac6aba0488e1d3c38c388ecedb321` |
| E459 | 19 | `c20f5a68f2d2299e44651f68348605447cad6095b06b898c3cb135994dfc2c38` |
| M284 | 14 | `511958b7bb1701039215209b3be552a4b25485c48d56d19fab10c5a95564ed98` |
| O206 | 5 | `2a084b05d42816c461019606973a55e7bbb5c71e1bb4a9f61c1c1bbe49ca4411` |

The initial source packet exposed M284's missing explicit header. The Operator separately approved its header-only normalization, completed in v13 with an exact v12 archive. Named-source inventory then passed. Ten remaining legacy carrier-format findings are outside that header-only change; full carrier conformance is not claimed.

Plan author `plan_closure` and independent reviewer `plan_checks` accepted P2300 v3 and its three bounded Active children P2354–P2356. P2300 v2 is archived exactly. These children cover source alignment, standalone implementation and independent tests; they do not close the parent Configuration Read work.

## Simplified reader verification

The Operator subsequently clarified that the earlier correction concerned the port and explicitly approved M284's header-only normalization. M284 v13 now carries its ID, Method role, PROGRAMMATIC owner and Active Status; its body and prior metadata are unchanged. The exact v12 archive has digest `c96e4f32db7684b56c0e09050ff10456ba36777828ec0a8d029a9e8c4ffbe921`. Current v13 digest is `413d071dd00e0ca8592015386daac6f8458864cf154c5b3e6008e7979727abe4`. Independent named inventory and final retained-currentness checks pass. Full carrier conformance is still not claimed: ten remaining legacy metadata/body-format findings are outside this header-only change.

M284 v14 and E459 v19 now separate ordinary Read from history queries. Independent reviewer `plan_checks` accepted both narrow changes and their exact predecessor archives. D365 remains unchanged. The earlier history-aware implementation and its test counts are superseded, not evidence for this simplified implementation.

The reader is 61 lines, down from 185. Six author tests and fourteen independent tests pass; `plan_checks` independently reproduced all twenty and found no concrete bugs in this scope. The checks include instrumented reads proving that malformed, inaccessible or symlinked Journal data is never read. The reader remains standalone; no existing public caller or route is changed. A new private Scope Query receiver consumes this reader only in bounded fixture checks. Root's connected regression run passed all 303 `test_connector*.py` tests after the simplification. These fixture results do not claim live admission.

| Implementation | SHA-256 |
| --- | --- |
| project_settings_reader.py | `24efe774f43f3c9c4a46b93104737a65abef24f6761fa2332be590c21cf507e6` |
| project_settings_schema.py | `2a700399527761e9272d245b2e1a06bb3efc875d68c1928e31c523617922227d` |
| test_project_settings_reader.py | `4c418a5335a7d0ad333a4ac59b0120fb86d9295e73635b68448d7825ed091007` |
| test_project_settings_reader_independent.py | `0304e690a4d33645380b7c2b1a30ca0c90bf0e45ccd54191f559d426709cfcb2` |

Mechanical checks retain complete schema validation, immutable values/provenance, exact Settings/schema pins and source drift refusal. Receipt classification, Journal enumeration, logical Revision and historical currentness are deliberately absent.

One separate schema conflict remains: concurrent D594 v4 defines `project_mcp.http_port`, but D366 v9's closed schema rejects it. This is a governed-current field, not legacy. A read-only review recommends narrowly admitting the optional section with strict integer port validation, required for launch/reuse rather than generic reading; alignment is not yet authorized or applied. Passing tests for the frozen schema do not resolve this conflict or admit the current live Settings file.

Concurrent MCP/runtime and live Project Settings changes already present in this checkout belong to other work. This packet neither includes nor reverts them. The Operator clarified that the current endpoint is `http://127.0.0.1:56317/mcp`; the earlier failure at port 63972 is obsolete. Root independently initialized the current endpoint, listed 33 tools and called the advertised read-only `get_mcp_reload_status` successfully at 2026-10-13 18:34 UTC. Its generation was serving and available with zero calls in flight; client refresh remained unconfirmed. No Workflow ran and no reload, configuration change or Journal observation was performed. These transport diagnostics do not establish admission of the new Settings reader.
