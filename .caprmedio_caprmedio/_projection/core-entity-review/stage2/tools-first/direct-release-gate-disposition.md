# Direct-release gate disposition — 2026-10-13

Derived audit of P2270; no release executed.

The Operator-approved P1848 v12 scope explicitly replaces old release sealing, snapshots and admission prerequisites with the direct happy path. Current M332 v6 and O164 v14 define that path. selected_routes.register_selected_routes registers release_version and directly invokes PROJECT_TOOLS/RELEASE_VERSION/local_release.py. D572 remains deliberately Archived, with no current successor; its absence is not a current direct-release blocker.

Actual intended direct-release regression suite: 18/18 PASS in 1.875 seconds (7 local, 5 public, 6 MCP route). Route tests explicitly make legacy admission loading fail and do not inject a historical D572 golden source. Temporary file copy/configuration preservation and Git checkpoints are exercised. Compiler, Docker, external commands and route runners remain simulated, so these tests prove no live release or installed runtime result.

Keep historical admission code/receipts fail-closed. Active R1847/D521/R1882/D589 references to legacy release behavior remain separate reconciliation debt; this audit does not silently repair their authority or revive the retired gate. P2270 stays Active for its actual current consumer obligations. PROJECT_TOOLS relocation remains separate and unexecuted.
