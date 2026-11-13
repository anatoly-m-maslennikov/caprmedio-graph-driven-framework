from pathlib import Path

import duckdb

from FEATURE_WORKBENCH_BACKEND.spec_trace import PILOT, SpecTraceStore


def test_incremental_trace_and_directory_changes(tmp_path):
    pilot = tmp_path / PILOT
    package = pilot / 'FEATURE_WORKBENCH_BACKEND' / 'sub'
    package.mkdir(parents=True)
    module = package / 'unit.py'
    module.write_text('pass')
    (package / 'unit.py.spec_trace.md').write_text('## Implements\n- CA-R-123@4\n- CA-M-9@2\n')
    (package / 'sub.p.spec_trace.md').write_text('## Applies\n- CA-E-8@3\n')
    excluded = pilot / 'FEATURE_WORKBENCH_CODEX'
    excluded.mkdir()
    (excluded / 'ignored.py').write_text('pass')
    (tmp_path / (tmp_path.name + '.p.spec_trace.md')).write_text('## Applies\n- CA-R-999@1\n')
    conn = duckdb.connect(':memory:')
    store = SpecTraceStore(conn, tmp_path)
    store.initialize()
    store.refresh()
    rel = lambda p: p.relative_to(tmp_path).as_posix()
    assert conn.execute('SELECT atom_id, version FROM implementation_rmedo ORDER BY atom_id').fetchall() == [
        ('CA-E-8', 3), ('CA-M-9', 2), ('CA-R-123', 4)]
    assert conn.execute('SELECT path FROM implementation_objects WHERE path = ?', [rel(excluded)]).fetchall() == []
    assert conn.execute('SELECT container_path FROM implementation_objects WHERE path = ?', [rel(module)]).fetchone() == (rel(package),)
    assert conn.execute("SELECT kind, container_path FROM implementation_objects WHERE path = '.'").fetchone() == ('package', None)

    (package / 'unit.py.spec_trace.md').write_text('## Implements\n- CA-R-123@5\n')
    store.refresh([package / 'unit.py.spec_trace.md'])
    assert conn.execute('SELECT version FROM implementation_rmedo WHERE owner_path = ?', [rel(module)]).fetchall() == [(5,)]
    (package / 'unit.py.spec_trace.md').unlink()
    store.refresh([package / 'unit.py.spec_trace.md'])
    assert conn.execute('SELECT * FROM implementation_rmedo WHERE owner_path = ?', [rel(module)]).fetchall() == []
    assert conn.execute('SELECT kind FROM implementation_objects WHERE path = ?', [rel(module)]).fetchone() == ('module',)

    renamed = package.with_name('moved')
    package.rename(renamed)
    store.refresh([package, renamed])
    assert conn.execute('SELECT path FROM implementation_objects WHERE starts_with(path, ?)', [rel(package)]).fetchall() == []
    assert conn.execute('SELECT kind FROM implementation_objects WHERE path = ?', [rel(renamed / 'unit.py')]).fetchone() == ('module',)
    # A directory-named sidecar no longer owns the renamed directory.
    assert conn.execute('SELECT * FROM implementation_rmedo').fetchall() == []
