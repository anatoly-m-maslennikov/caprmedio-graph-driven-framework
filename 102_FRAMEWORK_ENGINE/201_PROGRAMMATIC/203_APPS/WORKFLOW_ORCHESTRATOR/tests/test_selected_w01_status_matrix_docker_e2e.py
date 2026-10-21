"""Complete W01 selected status matrix; Docker reuses the current evidence harness."""

from __future__ import annotations

import os
from pathlib import Path
import sys
import unittest


TESTS = Path(__file__).resolve().parent
APP = TESTS.parent
PROGRAMMATIC = APP.parents[1]
for location in (TESTS, APP, PROGRAMMATIC / "201_TOOLS", PROGRAMMATIC / "204_MCP"):
    if str(location) not in sys.path:
        sys.path.insert(0, str(location))

import test_selected_workflows_docker_e2e as docker_evidence  # noqa: E402
from atom_operations import atom_from_path, frontmatter_scalar, require_current_atom  # noqa: E402
from authoritative_status_models import resolve_status_model  # noqa: E402
from selected_workflows_docker_fixture import STATUS_DOMAINS  # noqa: E402


@unittest.skipUnless(
    os.environ.get("CAPRMEDIO_DOCKER_E2E") == "1"
    and docker_evidence.E2E_CONTEXT is not None,
    "requires CAPRMEDIO_DOCKER_E2E=1 and an explicit built image/scratch context",
)
class SelectedW01StatusMatrixDockerEndToEnd(unittest.IsolatedAsyncioTestCase):
    def setUp(self) -> None:
        # Composition reuses helpers, not the opt-in Docker TestCase collection.
        self.evidence = docker_evidence.SelectedWorkflowsDockerEndToEnd("runTest")

    @staticmethod
    def _expected_observed_path(
        root: Path,
        carrier_path: str,
        role: str,
        status: str,
        directory: str,
    ) -> Path:
        expected_directory = root / ".caprmedio_caprmedio" / "PARENT" / directory
        if status.casefold() == "draft":
            expected_directory /= "draft"
        elif role == "Plan" and status == "Backlog":
            expected_directory /= "001_backlog"
        elif status.casefold() != "active":
            expected_directory /= status.casefold()
        return expected_directory / Path(carrier_path).name

    def _assert_atom_properties(
        self,
        atom,
        native: dict,
        carrier: dict,
        role: str,
        status: str,
        expected_id: str | None,
    ) -> None:
        self.assertEqual(role, frontmatter_scalar(atom.frontmatter, "content_role"))
        self.assertEqual(status, frontmatter_scalar(atom.frontmatter, "status"))
        self.assertEqual(expected_id, atom.atom_id)
        self.assertEqual(expected_id, native["observed"]["atom_id"])
        self.assertEqual(1, native["observed"]["version"])
        self.assertEqual("1", frontmatter_scalar(atom.frontmatter, "version"))
        self.assertEqual(
            frontmatter_scalar(carrier["frontmatter"], "type"),
            frontmatter_scalar(atom.frontmatter, "type"),
        )
        self.assertEqual(
            "high" if role == "Concern" else None,
            frontmatter_scalar(atom.frontmatter, "priority"),
        )

    def _assert_status_model(
        self,
        root: Path,
        atom,
        status: str,
        statuses: tuple[str, ...],
        role: str,
        source_id: str,
    ) -> None:
        model = resolve_status_model(root, atom, status)
        self.assertEqual(list(statuses), model["statuses"])
        expected_source_ids = (
            ("CA-R-1947", "CA-R-1608") if role == "Concern"
            else ("CA-R-1947", "CA-R-1539") if role == "Plan"
            else (source_id,)
        )
        self.assertEqual(
            expected_source_ids,
            tuple(row["atom_id"] for row in model["model_sources"]),
        )

    async def _create_and_assert(
        self,
        evidence,
        runtime,
        root: Path,
        fixture,
        role: str,
        letter: str,
        directory: str,
        source_id: str,
        status: str,
        statuses: tuple[str, ...],
        number: int,
    ) -> None:
        carrier = fixture.create_status_carrier(role, status, number=number)
        native, _graph, _selected = await evidence._execute_create_case(
            runtime, root, fixture, carrier,
            f"p2385-w01-{role.casefold()}-{status.casefold()}-{number}",
            reconnect=False,
        )
        self.assertEqual("applied", native.get("outcome"), native)
        observed = root / native["observed"]["path"]
        self.assertTrue(observed.is_file(), native)
        atom = atom_from_path(root, observed)
        require_current_atom(root, atom)
        self.assertEqual(
            self._expected_observed_path(root, carrier["path"], role, status, directory),
            observed,
        )
        self.assertEqual(carrier["path"], atom.relative)
        self.assertEqual(carrier["content"], atom.content)
        if status == "Archived":
            self.assertTrue(atom.filename.endswith("@1.md"), atom.filename)
        expected_id = None if status.casefold() == "draft" else f"CA-{letter}-{number}"
        self._assert_atom_properties(atom, native, carrier, role, status, expected_id)
        self._assert_status_model(root, atom, status, statuses, role, source_id)

    async def test_w01_creates_every_role_admitted_status_through_docker(self) -> None:
        """W01 applies each current source-admitted role/status pair through MCP."""
        evidence = self.evidence
        temporary, root, fixture = evidence._new_fixture(
            docker_evidence.GoldenCase("W01", "create_atom")
        )
        runtime = evidence._runtime(root)
        launched = False
        created = 0
        try:
            fixture.prepare()
            launched = True
            await evidence._start(runtime)
            for role, letter, directory, source_id, statuses in STATUS_DOMAINS:
                for status in statuses:
                    with self.subTest(role=role, status=status):
                        created += 1
                        number = 8100 + created
                        await self._create_and_assert(
                            evidence, runtime, root, fixture, role, letter, directory,
                            source_id, status, tuple(statuses), number,
                        )
            self.assertEqual(29, created)
        except docker_evidence.GoldenCorpusError as error:
            self.fail(str(error))
        finally:
            if launched:
                await evidence._stop(runtime)
            temporary.cleanup()


if __name__ == "__main__":
    unittest.main()
