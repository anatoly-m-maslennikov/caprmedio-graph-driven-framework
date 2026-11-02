# Direct current shared-context fixture

This is a distinct checked-in frozen corpus for the direct-RMED `CA-O-016@18` graph. It snapshots the explicit current graph and support selection from the legacy 17 fixture, adds `CA-R-2117`, `CA-M-431`, and `CA-E-653`, and carries full `requirements`, `methods`, `evaluations`, and `delivery` source rows. It intentionally has no `method_projection`; the trusted Method rows are independent of any packet under test.

All bytes are checked in and verified by digest. The fixture never refreshes from live authority during tests and is not execution or release evidence.
