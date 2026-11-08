# CA-M-508@3
# CA-E-799@1
# CA-E-800@1
"""Real Workbench lifecycle workload for the opt-in resource guard."""

from __future__ import annotations

from pathlib import Path
import time
from typing import Any, Callable

from workbench_performance_fixture import PerformanceFixture, SOURCE_SCOPE, TARGET_SCOPE
from workbench_soak_metrics import settle
from APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND.errors import QueryExecutionError


MAX_OPERATION_SECONDS = 45.0


def wait_until(probe: Callable[[], bool], *, operation: str, timeout: float = MAX_OPERATION_SECONDS) -> None:
    deadline = time.monotonic() + timeout
    while time.monotonic() < deadline:
        if probe():
            return
        time.sleep(0.05)
    raise AssertionError(f"{operation} did not become visible within {timeout:.0f}s")


class Workload:
    """One same-owner cycle: source lifecycle plus View/result lifecycle."""

    def __init__(self, tools: Any, fixture: PerformanceFixture) -> None:
        self.tools, self.fixture = tools, fixture
        self.workspace_id = "resource-soak"
        self.anchor_view_id: str | None = None

    @property
    def owner(self) -> Any:
        return self.tools._owner()

    def call(self, name: str, arguments: dict[str, Any]) -> dict[str, Any]:
        return self.tools._call(name, arguments)

    def warm(self) -> None:
        self.call("query_run", {"sql": "SELECT count(*) FROM atoms", "page_size": 1})
        opened = self.call("workspace_open", {"session_id": self.workspace_id})
        self.anchor_view_id = opened["views"][0]["id"]
        self.call("view_update", {
            "workspace_id": self.workspace_id, "view_id": self.anchor_view_id,
            "sql": "SELECT * FROM atoms ORDER BY reference", "expected_revision": 0,
        })
        self.call("view_run", {"workspace_id": self.workspace_id, "view_id": self.anchor_view_id})
        self.call("view_fetch", {
            "workspace_id": self.workspace_id, "view_id": self.anchor_view_id,
            "offset": 0, "page_size": 1,
        })
        transient = self.call("query_run", {"sql": "SELECT count(*) FROM atoms", "page_size": 1})
        time.sleep(1.1)
        store = self.owner._store
        assert store is not None
        store.prune_results()
        if transient["query_id"] in store._results:
            raise AssertionError("unopened result survived its test TTL")
        anchor = self.call("view_get", {"workspace_id": self.workspace_id, "view_id": self.anchor_view_id})
        if anchor.get("result", {}).get("query_id") not in store._results:
            raise AssertionError("open View result expired despite its lease")
        self.schema_change(-1)
        self.declaration_refresh(1)
        self.call("view_run", {"workspace_id": self.workspace_id, "view_id": self.anchor_view_id})
        self.call("view_fetch", {
            "workspace_id": self.workspace_id, "view_id": self.anchor_view_id,
            "offset": 0, "page_size": 1,
        })
        result = self.call("query_run", {"sql": "SELECT count(*) FROM atoms", "page_size": 1})
        store.drop(result["query_id"])

    def tables(self) -> set[str]:
        store = self.owner._store
        with store._lock:
            return {row[0] for row in store._connection.execute(
                "SELECT table_name FROM information_schema.tables WHERE table_schema='workbench_results'"
            ).fetchall()}

    def _matches(self, reference: str, *, version: int, scope_id: str, path: Path) -> bool:
        store = self.owner._store
        assert store is not None
        with store._lock:
            rows = store._connection.execute(
                'SELECT "header.state.version", "header.context.container.scope_unit", filename, "relative path", '
                '"header.destination.file.path" FROM atoms WHERE reference = ?', [reference]
            ).fetchall()
        return rows == [(version, scope_id, path.name, self.fixture.relative(path.parent), self.fixture.relative(path.parent))]

    def _has_reference(self, reference: str) -> bool:
        store = self.owner._store
        assert store is not None
        with store._lock:
            return bool(store._connection.execute("SELECT 1 FROM atoms WHERE reference = ?", [reference]).fetchall())

    def _write_cycle_atom(self, index: int, *, version: int, changed: bool = False) -> tuple[str, Path]:
        reference = f"CA-R-{8_000_000 + index:07d}"
        path = self.fixture.source_directory / "soak" / f"{reference}-created.md"
        self.fixture.write_atom(
            path, reference, version=version, scope_id=self.fixture.source_scope_id,
            scope_name=SOURCE_SCOPE, changed=changed,
        )
        return reference, path

    def source_cycle(self, index: int) -> None:
        reference, path = self._write_cycle_atom(index, version=1)
        wait_until(lambda: self._matches(reference, version=1, scope_id=self.fixture.source_scope_id, path=path), operation="create", timeout=1.5)

        self.fixture.write_atom(path, reference, version=2, scope_id=self.fixture.source_scope_id,
                                scope_name=SOURCE_SCOPE, changed=True)
        wait_until(lambda: self._matches(reference, version=2, scope_id=self.fixture.source_scope_id, path=path), operation="update", timeout=1.5)

        renamed = path.with_name(f"{reference}-renamed.md")
        path.rename(renamed)
        self.fixture.write_atom(renamed, reference, version=3, scope_id=self.fixture.source_scope_id,
                                scope_name=SOURCE_SCOPE, destination=self.fixture.relative(renamed), changed=True)
        wait_until(lambda: self._matches(reference, version=3, scope_id=self.fixture.source_scope_id, path=renamed), operation="rename", timeout=1.5)

        target = self.fixture.target_directory / "soak" / renamed.name
        target.parent.mkdir(parents=True, exist_ok=True)
        renamed.rename(target)
        self.fixture.write_atom(target, reference, version=4, scope_id=self.fixture.target_scope_id,
                                scope_name=TARGET_SCOPE, destination=self.fixture.relative(target), changed=True)
        wait_until(lambda: self._matches(reference, version=4, scope_id=self.fixture.target_scope_id, path=target), operation="move", timeout=1.5)

        target.unlink()
        wait_until(lambda: not self._has_reference(reference), operation="delete", timeout=1.5)

    def schema_change(self, index: int) -> None:
        """Add/remove one Header key; Content declarations remain unchanged."""
        reference, path = self._write_cycle_atom(index + 100_000, version=1)
        text = path.read_text(encoding="utf-8").replace("relations: {", "soak_probe_key: true\nrelations: {", 1)
        path.write_text(text, encoding="utf-8")
        wait_until(lambda: self._has_column("header.soak_probe_key") and self._has_reference(reference), operation="schema add")
        path.write_text(text.replace("soak_probe_key: true\n", "", 1), encoding="utf-8")
        wait_until(lambda: not self._has_column("header.soak_probe_key"), operation="schema remove")
        path.unlink()
        wait_until(lambda: not self._has_reference(reference), operation="schema delete")

    def _has_column(self, name: str) -> bool:
        store = self.owner._store
        with store._lock:
            return bool(store._connection.execute(
                "SELECT 1 FROM information_schema.columns WHERE table_name='atoms' AND column_name=?", [name]
            ).fetchall())

    def view_cycle(self) -> None:
        created = self.call("view_create", {"workspace_id": self.workspace_id, "name": "Transient"})
        view_id = created["view_id"]
        self.call("view_update", {
            "workspace_id": self.workspace_id, "view_id": view_id,
            "sql": "SELECT * FROM atoms ORDER BY reference", "expected_revision": 0,
        })
        run = self.call("view_run", {"workspace_id": self.workspace_id, "view_id": view_id})
        if run["status"] != "success":
            raise AssertionError(run)
        self.call("view_fetch", {"workspace_id": self.workspace_id, "view_id": view_id, "offset": 0, "page_size": 2})
        duplicate = self.call("view_duplicate", {"workspace_id": self.workspace_id, "view_id": view_id})
        duplicate_id = duplicate["view_id"]
        if self.call("view_get", {"workspace_id": self.workspace_id, "view_id": duplicate_id}).get("result"):
            raise AssertionError("duplicate inherited a result lease")
        self.call("view_run", {"workspace_id": self.workspace_id, "view_id": duplicate_id})
        self.call("view_remove", {"workspace_id": self.workspace_id, "view_id": duplicate_id})
        rerun = self.call("view_run", {"workspace_id": self.workspace_id, "view_id": view_id})
        if rerun["status"] != "success" or f"query_{run['query_id']}" in self.tables():
            raise AssertionError("rerun failed to release its previous result table")
        self.call("view_remove", {"workspace_id": self.workspace_id, "view_id": view_id})
        store = self.owner._store
        with store._lock:
            if rerun["query_id"] in store._results and store._results[rerun["query_id"]].pinned:
                raise AssertionError("closed View retained its result pin")
        time.sleep(1.15)
        settle(self.owner)
        anchor = self.call("view_get", {"workspace_id": self.workspace_id, "view_id": self.anchor_view_id})
        if self.tables() != {f"query_{anchor['result']['query_id']}"}:
            raise AssertionError("closed View result tables survived TTL or anchor result disappeared")

    def error_cycle(self) -> None:
        store = self.owner._store
        assert store is not None
        before = self.tables()
        for sql in ("SELECT FROM", "SELECT CAST('x' AS INTEGER)"):
            try:
                self.call("query_run", {"sql": sql, "page_size": 1})
            except (QueryExecutionError, ValueError):
                pass
            else:
                raise AssertionError(f"invalid SQL succeeded: {sql}")
            if self.tables() != before:
                raise AssertionError("failed query retained a result table")
        healthy = self.call("query_run", {"sql": "SELECT 1", "page_size": 1})
        self.call("query_page", {"query_id": healthy["query_id"], "offset": 0, "page_size": 1})
        self.owner._store.drop(healthy["query_id"])

    def declaration_refresh(self, revision: int) -> None:
        """A valid declaration carrier edit observed through the real watcher."""
        declaration = Path(self.fixture.declarations[TARGET_SCOPE]["declaration_path"])
        text = declaration.read_text(encoding="utf-8")
        import re
        updated, count = re.subn(r'(?m)^version: .*$', f'version: {revision + 1}', text, count=1)
        if count != 1:
            raise AssertionError("fixture Declaration version not found")
        declaration.write_text(updated, encoding="utf-8")
        relative = self.fixture.relative(declaration)
        def visible() -> bool:
            store = self.owner._store
            with store._lock:
                return store._connection.execute(
                    'SELECT declaration_version FROM scope_units WHERE name = ?', [TARGET_SCOPE]
                ).fetchall() == [(revision + 1,)]
        wait_until(visible, operation=f"declaration update {relative}")

    def cycle(self, index: int, *, schema: bool = False) -> None:
        self.source_cycle(index)
        if schema:
            self.schema_change(index)
            self.declaration_refresh(index + 2)
        self.view_cycle()
        self.error_cycle()
