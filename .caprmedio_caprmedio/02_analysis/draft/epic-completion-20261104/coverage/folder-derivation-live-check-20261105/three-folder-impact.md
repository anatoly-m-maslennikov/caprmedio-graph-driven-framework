# Impact of the three Delivery folder names

Pinned mapping rule: CA-D-667@2 requires the Delivery form to omit the Scope Unit ID. The exact tracked path list is in [`tracked-paths.txt`](./tracked-paths.txt); the machine-readable summary and per-folder tree hashes are in [`three-folder-impact.json`](./three-folder-impact.json).

| Scope Unit | Old folder | Tracked contents | Same bytes as native Current Atoms | Expected destination | Collision | Exact full-path refs |
| --- | --- | --- | ---: | --- | --- | ---: |
| CA-SU-11 | `CA-SU-11_LAYER_1_CORE_META_MODEL` | 894 Markdown Atoms; 1 TOML | 894/894 | `LAYER_1_CORE_META_MODEL` | No | 0 |
| CA-SU-12 | `CA-SU-12_LAYER_2_INSTALLED_EXTENSIONS` | 1 `.gitkeep` | 0/0 | `LAYER_2_INSTALLED_EXTENSIONS` | No | 0 |
| CA-SU-13 | `CA-SU-13_LAYER_3_PROJECT_CONFIGURATION` | 173 Markdown Atoms, including 33 Action, 10 Step, 3 Workflow definitions | 173/173 | `LAYER_3_PROJECT_CONFIGURATION` | No | 0 |

The tracked directories contain duplicated RMED/Atom source copies, not code; CA-SU-13's Operations files are duplicate definitions, not unique Workflow instances. No tracked file contains the exact old full Delivery path outside historical/Draft/projection/package trees. Destination folders do not exist. A path-only directory rename is mechanically bounded by the inspected tracked content and literal references; it relocates the Workflow/Step/Action definition copies in CA-SU-13. No moves or tests were performed. Dynamic path construction was not tested.
