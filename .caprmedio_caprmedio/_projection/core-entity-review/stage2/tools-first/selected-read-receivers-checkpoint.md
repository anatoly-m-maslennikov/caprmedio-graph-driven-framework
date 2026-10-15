# Selected read receivers — 2026-10-13

Derived implementation checkpoint for P2340/P2341 and P2300. These Tasks remain Active. This is not a production Settings-schema acceptance or runnable-route registration.

## Implemented and checked

The shared private `admission_for_started_action` derives the logical connector request from an existing sealed RunExecutionSession. It requires an actual recorded, nonterminal Action, exact Project/definition pins and native authorization. It reopens the real Action-start receipt and repeats currentness checks on later binds. It creates no Run or Journal record.

The private O212 Scope Read receiver binds retained Settings and Structure provenance, current Action/schema sources and the existing complete declaration reader. The private O218 Configuration Read receiver implements the current Project Structure branch and returns the existing complete TOML text/document/state result. Both reject requested effects and require an explicitly supplied complete Settings validator; neither substitutes the identity-only Settings parser for complete validation.

The Settings validators in tests are source-backed complete disposable fixture schemas, not the production Settings policy. Production admission still requires the actual accepted Settings schema. O218's Project Settings branch and historical views are not implemented by this packet. There is no public route, implicit Query, new authorization envelope, runtime registration or live source effect.

## Evidence

- Author checks: shared helper 13 genuine-Session checks; O212 six checks; O218 ten checks. The existing binding suite also passed.
- Different reviewer `/root/nested_ops`: 12 real receiving checks passed using actual LazyRunTracker admission, canonical Action starts and current O212/O218/D625/D527/D441/D442 source copies. Source and Journal bytes remain unchanged during receivers; the test caller separately records the actual result through its existing Session.
- Root integration: all 264 `test_connector*.py` tests passed in 21.728 seconds. These include the author and independent checks; counts overlap and must not be added.

Checks include wrong Action/root, terminal or unstarted Action, stale source/authorization, missing start receipt, actual context mismatch, complete Structure values, missing/ambiguous targets, Boolean validation substitutes, validator repairs and attempted mutation requests.

| Carrier | SHA-256 |
| --- | --- |
| connector_bindings.py | `48c49ffd76934896f117f98c9533cceed372fc316df48f7b8e9e14ca99899bfd` |
| connector_scope_receiver.py | `a8ba497e828e738b6303d68c8b5a7fa33e759e778dea75e3352d42ddeb5b6fdc` |
| connector_configuration_receiver.py | `4b7c6ccba03864054e004b1065a6dd841ff46572b5bb66896ae03e6dac3678b0` |
| test_connector_session_admission.py | `8186537a6f503f728b95d2f3ba6834737f499adc1ead1439efff062ea91336ac` |
| test_connector_scope_receiver.py | `bf016ead06d4b7d4c4e87fe500b679c9216f40e601ffdb1bb161d6b2352fa2d8` |
| test_connector_configuration_receiver.py | `fcf6b8e454571332a953bb5b382edaa61dc019911fd06a6d4e1f1a05433e4f65` |
| test_connector_receiving_independent.py | `45812b5a2f795c4cc84c62001d17b8b84d5e95548d44df556acbcfedc6a257b7` |

## Remaining work and latest decision

The Operator rejected preserving legacy compatibility in the new Settings reader: “we don't need legacy.” No legacy data was deleted. Inventory current governing fields and remaining live consumers before proposing the exact Settings/source migration. The prior open-content preservation proposal is not accepted.

Current selected lifecycle execution has a separate stale canonical-manifest blocker: the read-only review found 95 unavailable and 15 digest-stale paths among 162 unique source pins. A lifecycle-only repin cannot establish the full registry's readiness. Another one-off historical-repair registration is not approved. Draft promotion also needs source alignment between explicit Operator assignment, the receiving request and governed metadata changes; automatic allocation is not accepted as completion.

Keep the Epic, receiving Tasks and live Subject migration gates open. Live Settings observation registration remains separately blocked on the unavailable MCP route or explicit direct-writer permission.
