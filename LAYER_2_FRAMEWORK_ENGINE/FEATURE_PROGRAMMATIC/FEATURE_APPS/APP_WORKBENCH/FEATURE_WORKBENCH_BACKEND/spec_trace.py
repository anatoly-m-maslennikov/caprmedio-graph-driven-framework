"""Discover Workbench implementation objects and their explicit RMeDO pins."""
from __future__ import annotations

import os
from pathlib import Path
import re
import sys

PILOT = Path('LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_APPS/APP_WORKBENCH')
EXCLUDED = {'FEATURE_WORKBENCH_CODEX', 'FEATURE_CODEX_EXTENSION', 'node_modules',
            '__pycache__', 'dist', 'build', 'coverage', 'assets', 'generated', 'benchmark', 'benchmarks'}
EXTENSIONS = {'.py', '.svelte', '.ts', '.js', '.mjs'}
PIN = re.compile(r'- (CA-[RMEDO]-[0-9]+)@([0-9]+)')
SUFFIX = '.spec_trace.md'


class SpecTraceStore:
    """Publish source facts to a caller-owned DuckDB connection."""

    def __init__(self, connection, repo_root):
        self.connection = connection
        self.root = Path(repo_root).absolute()

    def initialize(self):
        self.connection.execute('CREATE TABLE IF NOT EXISTS implementation_objects '
                                '(path VARCHAR PRIMARY KEY, kind VARCHAR, container_path VARCHAR)')
        self.connection.execute('CREATE TABLE IF NOT EXISTS implementation_rmedo '
                                '(owner_path VARCHAR, sidecar_path VARCHAR, entry_kind VARCHAR, '
                                'atom_id VARCHAR, version INTEGER)')

    def _allowed(self, path):
        try:
            rel = path.relative_to(self.root)
        except ValueError:
            return False
        if any(part in EXCLUDED or part.lower() in EXCLUDED for part in rel.parts):
            return False
        # Never follow a symlink, including one in an ancestor.
        return not any((self.root / Path(*rel.parts[:i])).is_symlink()
                       for i in range(1, len(rel.parts) + 1))

    def _rel(self, path):
        return path.relative_to(self.root).as_posix()

    def _sidecar(self, path, kind):
        return path / (path.name + '.p' + SUFFIX) if kind == 'package' else path.with_name(path.name + SUFFIX)

    def _pins(self, path, kind):
        if path != self.root / PILOT and self.root / PILOT not in path.parents:
            return []
        sidecar = self._sidecar(path, kind)
        if not self._allowed(sidecar) or not sidecar.is_file():
            return []
        try:
            lines = sidecar.read_text(encoding='utf-8').splitlines()
        except (OSError, UnicodeError) as exc:
            print(f'Invalid spec trace {sidecar}: {exc}', file=sys.stderr)
            return []
        section = None
        pins = []
        for line in lines:
            if line.startswith('## '):
                section = {'## Implements': 'implements', '## Applies': 'applies'}.get(line)
            elif section and line.startswith('- '):
                match = PIN.fullmatch(line)
                if match is None or (section == 'applies' and kind != 'package'):
                    print(f'Invalid spec trace entry {sidecar}: {line}', file=sys.stderr)
                    continue
                pins.append((self._rel(path), self._rel(sidecar), section,
                             match.group(1), int(match.group(2))))
        return pins

    def _insert(self, path, kind):
        rel = self._rel(path)
        container = None if path == self.root else self._rel(path.parent)
        self.connection.execute('INSERT OR REPLACE INTO implementation_objects VALUES (?, ?, ?)',
                                [rel, kind, container])
        self.connection.execute('DELETE FROM implementation_rmedo WHERE owner_path = ?', [rel])
        pins = self._pins(path, kind)
        if pins:
            self.connection.executemany('INSERT INTO implementation_rmedo VALUES (?, ?, ?, ?, ?)', pins)

    def _ancestors(self, path):
        for directory in reversed((path, *path.parents)):
            if directory == self.root or (self.root in directory.parents and directory.is_dir()):
                self._insert(directory, 'package')

    def _scan(self, path):
        if not self._allowed(path):
            return
        if path.is_file() and path.suffix in EXTENSIONS:
            self._ancestors(path.parent)
            self._insert(path, 'module')
        elif path.is_dir():
            self._ancestors(path.parent)
            for directory, dirs, files in os.walk(path, followlinks=False):
                folder = Path(directory)
                dirs[:] = [name for name in dirs if self._allowed(folder / name)]
                self._insert(folder, 'package')
                for name in files:
                    candidate = folder / name
                    if candidate.suffix in EXTENSIONS and self._allowed(candidate):
                        self._insert(candidate, 'module')

    def refresh(self, paths=None):
        """Refresh all pilot files initially, or affected paths and directory subtrees."""
        if paths is None:
            self.connection.execute('DELETE FROM implementation_rmedo')
            self.connection.execute('DELETE FROM implementation_objects')
            self._scan(self.root / PILOT)
            return
        for value in paths:
            path = Path(os.path.abspath(self.root / value))
            if path.name.endswith(SUFFIX):
                name = path.name[:-len(SUFFIX)]
                path = path.parent if name == path.parent.name + '.p' else path.with_name(name)
            if not self._allowed(path) or not (path == self.root / PILOT or self.root / PILOT in path.parents):
                continue
            rel = self._rel(path)
            for table, column in (('implementation_rmedo', 'owner_path'), ('implementation_objects', 'path')):
                self.connection.execute(f'DELETE FROM {table} WHERE {column} = ? OR starts_with({column}, ?)',
                                        [rel, rel + '/'])
            self._scan(path)
