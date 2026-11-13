# CA-R-3132@1
# CA-M-464@18

"""Prepublication reference lookup for parsed carriers."""
from __future__ import annotations

from pathlib import Path

from .source_rows import _path_rank, _reference


class ReferenceCatalog:
    def __init__(self, connection, lock, root):
        self.connection, self.lock, self.root = connection, lock, root
        with lock:
            connection.execute("CREATE TEMP TABLE workbench_reference_carriers (path VARCHAR PRIMARY KEY, reference VARCHAR, accepted BOOLEAN)")

    def _relative(self, path):
        return path.relative_to(self.root).as_posix()

    def paths_for(self, reference):
        return {path for _, path in self._peers([reference])}

    def paths_by_reference(self, references):
        grouped = {reference: set() for reference in references}
        for reference, path in self._peers(grouped):
            grouped[reference].add(path)
        return grouped

    def _peers(self, references):
        if not references:
            return []
        with self.lock:
            rows = self.connection.execute(
                "SELECT reference, path FROM temp.main.workbench_reference_carriers "
                "WHERE reference IN (SELECT unnest(?::VARCHAR[]))", [list(references)],
            ).fetchall()
        return [(reference, self.root / path) for reference, path in rows]

    def accepted_paths(self, paths=None):
        if paths is not None and not paths:
            return set()
        where = "accepted"
        params = []
        if paths is not None:
            where += " AND path IN (SELECT unnest(?::VARCHAR[]))"
            params.append([self._relative(path) for path in paths])
        with self.lock:
            rows = self.connection.execute(
                "SELECT path FROM temp.main.workbench_reference_carriers WHERE " + where, params
            ).fetchall()
        return {self.root / row[0] for row in rows}

    def rebuild(self, rows):
        winners = {}
        for path, row in rows.items():
            reference = _reference(row)
            if reference is not None and (reference not in winners or _path_rank(path) < _path_rank(winners[reference])):
                winners[reference] = path
        values = [(self._relative(path), reference, reference is None or winners[reference] == path)
                  for path, row in rows.items() for reference in (_reference(row),)]
        with self.lock:
            self.connection.execute("DELETE FROM temp.main.workbench_reference_carriers")
            if values:
                self.connection.execute(
                    "INSERT INTO temp.main.workbench_reference_carriers SELECT unnest(?::VARCHAR[]), unnest(?::VARCHAR[]), unnest(?::BOOLEAN[])",
                    [list(column) for column in zip(*values)],
                )

    def update(self, before, after, affected):
        if not affected:
            return set()
        references = {reference for lookup in (before.get, after) for path in affected
                      if (reference := _reference(lookup(path))) is not None}
        changed = {path for path in affected if (
            (before.get(path) is None) != (after(path) is None)
            or _reference(before.get(path)) != _reference(after(path))
        )}
        with self.lock:
            old = self._peers(references)
            if not changed:
                return affected | {path for _, path in old}
            self.connection.execute(
                "DELETE FROM temp.main.workbench_reference_carriers WHERE path IN (SELECT unnest(?::VARCHAR[]))",
                [[self._relative(path) for path in changed]],
            )
            values = [(self._relative(path), _reference(row), _reference(row) is None)
                      for path in changed if (row := after(path)) is not None]
            if values:
                self.connection.execute(
                    "INSERT INTO temp.main.workbench_reference_carriers SELECT unnest(?::VARCHAR[]), unnest(?::VARCHAR[]), unnest(?::BOOLEAN[])",
                    [list(column) for column in zip(*values)],
                )
            peers = [(reference, path) for reference, path in old if path not in changed]
            peers.extend((reference, path) for path in changed if (reference := _reference(after(path))) is not None)
            winners = {}
            for reference, path in peers:
                if reference not in winners or _path_rank(path) < _path_rank(winners[reference]):
                    winners[reference] = path
            if winners:
                self.connection.execute(
                    "UPDATE temp.main.workbench_reference_carriers AS carrier SET accepted = (carrier.path = winner.path) "
                    "FROM (SELECT unnest(?::VARCHAR[]) AS reference, unnest(?::VARCHAR[]) AS path) AS winner "
                    "WHERE carrier.reference = winner.reference",
                    [list(winners), [self._relative(path) for path in winners.values()]],
                )
        return affected | {path for _, path in old}
