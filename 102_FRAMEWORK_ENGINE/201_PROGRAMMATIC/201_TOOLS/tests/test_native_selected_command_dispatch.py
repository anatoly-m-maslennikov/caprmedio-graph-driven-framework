"""Narrow D604 command dispatch through physical package/start authority."""

from __future__ import annotations

import hashlib
import sys
import tempfile
import unittest
from pathlib import Path


TOOLS = Path(__file__).resolve().parents[1]
RELEASE = TOOLS / "RELEASE_VERSION"
for path in (TOOLS, RELEASE, RELEASE / "tests"):
    if str(path) not in sys.path:
        sys.path.insert(0, str(path))

from framework_installation_command import (  # noqa: E402
    run_framework_installation_command,
)
import test_framework_installation_command as command_fixture  # noqa: E402
from native_selected_installation import (  # noqa: E402
    NativeSelectedInstallationError,
    _reopen_installation_command,
)


class NativeSelectedCommandDispatchTests(unittest.TestCase):
    def setUp(self) -> None:
        # Reuse the physical admitted-package and registered-Operator fixture,
        # retaining this lane's isolated files as requested by the user.
        self.fixture = command_fixture.FrameworkInstallationCommandTests("runTest")
        self.fixture.base = Path(tempfile.mkdtemp(
            prefix="native-command-dispatch-", dir=command_fixture.TEST_TEMP_ROOT,
        )).resolve()
        self.fixture.package = self.fixture._package()
        self.fixture.root, self.fixture.control = self.fixture._project("alpha")
        self.registry_ref = (
            self.fixture.control / "operators_registry.toml"
        ).relative_to(self.fixture.root)

    def test_reopens_closed_direct_o200_receipt(self) -> None:
        command = run_framework_installation_command(self.fixture._request())
        self.addCleanup(command.action_session.close)
        payload = command.command_receipt_path.read_bytes()
        receipt = _reopen_installation_command(
            self.fixture.root,
            payload,
            hashlib.sha256(payload).hexdigest(),
            action_package=self.fixture.package,
            operators_registry_ref=self.registry_ref,
        )
        self.assertEqual(command.command_receipt, receipt)
        self.assertEqual("fixture-install-command", receipt.command_id)

    def test_refuses_undesignated_operation(self) -> None:
        with self.assertRaises(NativeSelectedInstallationError) as raised:
            _reopen_installation_command(
                self.fixture.root,
                b'{"operation":"other"}',
                "a" * 64,
                action_package=self.fixture.package,
                operators_registry_ref=self.registry_ref,
            )
        self.assertEqual("native-selected-installation-command-invalid", raised.exception.code)


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
