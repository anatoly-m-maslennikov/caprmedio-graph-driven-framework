# Captured Core review context

The Operator chose: **Finish against the captured snapshot only**.

This review uses the original 951 Core source pins in `../baseline.inventory.json`, not the currently edited Core. The immutable Git source is commit `a971d0e00c33c779f485fc8cad63194894d440fb`. Every recovered source must match its original SHA-256 and revision exactly. A missing or mismatched Git source stops verification; there is no automatic rebind.

CA-D-494 revision 2 is the captured source. Its newer revision 3 remains untouched. The original Step 1 graph, inventory, relation ledger and candidate design stay unchanged. Carrier paths in old evidence are captured locators, not assertions that those paths still contain the captured bytes.

`support/snapshot_sources.py` reads the captured bytes from Git history. It does not copy sources, overwrite Core, admit facts or migrate Subjects. Review receipts must say **captured snapshot**, not **current Core**. The later Substance and Substance Scope Operator directions remain candidate inputs; they are not retroactively inserted into Core.
