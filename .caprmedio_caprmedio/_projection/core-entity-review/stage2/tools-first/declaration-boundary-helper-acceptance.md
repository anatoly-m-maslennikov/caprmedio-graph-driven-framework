# Declaration boundary helper acceptance

Derived private-helper evidence, 2026-10-13. Not current caller or runtime acceptance.

P2321 implements a private shared check in project_selection.py. It captures the owning Project's exact Settings and a finite set of Settings markers along declared authority_path and delivery_path ancestors. Identity comes from Settings and the exact Project/control-root pair, not a directory prefix. Proven foreign roots, including same-name instances, refuse. Ordinary lookalikes and absent ordinary paths remain allowed.

The proof retains original marker hashes and absence observations. Revalidation compares those fixed observations rather than recapturing them. Marker introduction, removal and changes refuse. Reads are bounded and no-follow. No logical Settings revision or Journal event is invented.

Author epic_atom_read: ten focused tests passed. Independent verifier whitelist_tests: eight helper tests passed without mocks or skips, including actual unreadability, both path fields, same-name/no-Structure foreign roots, malformed/contradictory/symlink Settings, ordinary paths and drift. Independent reviewer whitelist_impl found no bounded-helper defect.

Accepted helper project_selection.py hash: `f2b4a327191baa80b9683edeb278e662347b79cc403f7b68a7bbdd887df1c199`.
Author test_project_declaration_boundary.py hash: `3ac0262cd6ecaef207632483c2d5fa82b59e86c910c434b8a78b1ec483a04cb3`.
Independent test_project_authority_boundary_independent.py checkpoint hash: `792c12a30d4ebae1eb2243ba4e9fd44ebd34779059cb4524800340c2a151f45e`.

The independent file also contains five actual Selection controls that were red before P2322 wiring; those are not accepted by this helper receipt. P2322 must retain the proof at selection time and recheck it in actual consumers. Integration also must use the current operation's bounded reader when revalidating long-lived proof, rather than reuse an expired reader clock; original pins must never be resealed. Final integrated hashes and checks require separate acceptance. Settings revision evidence, graph readiness and public activation remain outside this result.
