"""Shared plain-append fixture, not a collected TestCase."""

from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))
import test_append_change_records as native_tests  # noqa: E402
import append_change_records as appender  # noqa: E402
import work_journal  # noqa: E402


class AppendMcpFixture:
    def setUp(self) -> None:
        self.fixture = native_tests.AppendChangeRecordsTest("test_dry_run_is_mutation_free")
        self.fixture.setUp()
        self.addCleanup(self.fixture.tearDown)
        self.root = self.fixture.root.resolve()
        self.adapter = appender.create_adapter(self.root)

    def _context(self, records=None) -> dict:
        return self.fixture.context(records=records)

    def _events(self) -> list:
        return work_journal.read_records(self.root)

    def _apply(self, context: dict) -> dict:
        return self.adapter.invoke({"context": context, "apply": True})
