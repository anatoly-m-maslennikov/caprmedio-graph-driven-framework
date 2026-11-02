# Fixed graph test inputs

These forty byte-exact carriers are test inputs, not authoritative Atoms or
published Projections. They cover only the fixed profiles and relation examples
used by the executable graph tests. `pins.json` binds their exact SHA-256 bytes.

Tests read these committed inputs and create disposable repository fixtures;
they never fall back to current repository authority. Update a fixture only
alongside an intentional change to its tested executable profile.
