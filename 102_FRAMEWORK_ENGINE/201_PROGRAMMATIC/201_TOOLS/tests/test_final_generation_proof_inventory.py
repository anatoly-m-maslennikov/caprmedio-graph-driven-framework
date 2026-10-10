"""Physical closed-inventory checks for the D601 fragment plus D604 proof."""

from __future__ import annotations

import hashlib
from pathlib import Path
import sys
import tempfile
import unittest

TOOLS = Path(__file__).resolve().parents[1]
if str(TOOLS) not in sys.path:
    sys.path.insert(0, str(TOOLS))

from portable_runtime_materialization import (
    PortableRuntimeMaterializationError,
    _final_generation_carriers,
)


class FinalGenerationProofInventoryTests(unittest.TestCase):
    def setUp(self):
        self.root = Path(tempfile.mkdtemp(prefix="final-proof-inventory-"))
        self.generation = self.root / ".caprmedio_runtime/installation/generations/1"
        self.generation.mkdir(parents=True)
        for name, mode in (("command.toml", 0o600), ("environment.toml", 0o600),
                           ("wrapper", 0o700), ("stage-manifest.toml", 0o600)):
            path = self.generation / name
            path.write_bytes(name.encode())
            path.chmod(mode)
        self.proof = self.generation / "release-proof.toml"
        self.payload = b"schema_version = 2\n"
        self.digest = hashlib.sha256(self.payload).hexdigest()

    def write_proof(self):
        self.proof.write_bytes(self.payload)
        self.proof.chmod(0o600)

    def read(self, digest=None):
        return _final_generation_carriers(self.root, 1, release_proof_sha256=digest)

    def test_fragment_without_proof_remains_closed(self):
        self.assertEqual(4, len(self.read()))

    def test_exact_bound_native_proof_is_not_a_stage_manifest_member(self):
        self.write_proof()
        self.assertEqual(self.payload, self.read(self.digest)["release-proof.toml"])

    def test_unbound_proof_remains_an_extra_carrier(self):
        self.write_proof()
        with self.assertRaises(PortableRuntimeMaterializationError):
            self.read()

    def test_missing_or_changed_bound_proof_refuses(self):
        with self.assertRaises(PortableRuntimeMaterializationError):
            self.read(self.digest)
        self.write_proof()
        self.proof.write_bytes(self.payload + b"# drift\n")
        with self.assertRaises(PortableRuntimeMaterializationError):
            self.read(self.digest)

    def test_extra_carrier_is_not_allowed_with_bound_proof(self):
        self.write_proof()
        (self.generation / "unexpected.toml").write_bytes(b"extra")
        with self.assertRaises(PortableRuntimeMaterializationError):
            self.read(self.digest)

    def test_nonprivate_symlink_and_hardlink_proof_refuse(self):
        self.write_proof()
        self.proof.chmod(0o644)
        with self.assertRaises(PortableRuntimeMaterializationError):
            self.read(self.digest)
        self.proof.chmod(0o600)
        alias = self.root / "proof-alias"
        alias.hardlink_to(self.proof)
        with self.assertRaises(PortableRuntimeMaterializationError):
            self.read(self.digest)
        # Retain the hardlink fixture; use a new generation for symlink coverage.
        other = self.root / ".caprmedio_runtime/installation/generations/2"
        other.mkdir()
        for name in ("command.toml", "environment.toml", "wrapper", "stage-manifest.toml"):
            source = self.generation / name
            target = other / name
            target.write_bytes(source.read_bytes())
            target.chmod(source.stat().st_mode & 0o777)
        (other / "release-proof.toml").symlink_to(self.proof)
        with self.assertRaises(PortableRuntimeMaterializationError):
            _final_generation_carriers(self.root, 2, release_proof_sha256=self.digest)


if __name__ == "__main__":
    unittest.main()
