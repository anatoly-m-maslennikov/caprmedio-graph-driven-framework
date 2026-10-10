"""Binding mechanics only; the physical producer reader is mocked here."""
from __future__ import annotations

import sys
import unittest
from dataclasses import replace
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch

TOOLS = Path(__file__).resolve().parents[2]
for entry in (TOOLS, TOOLS / "PUBLIC_RELEASE", TOOLS / "RELEASE_VERSION"):
    if str(entry) not in sys.path:
        sys.path.insert(0, str(entry))

from public_release import (FreshPublicNativeFullGateBinding, GateResult,
                            PublicReleaseError, SourceProof, ToolCallEvidence,
                            _full_gate_receipt_ref, _gate)
from release_public_gate import PublicFreshGateInputs
from release_public_producer import PublicNativeFullGateResult


class FreshGateBindingTests(unittest.TestCase):
    def setUp(self):
        self.root = Path(__file__).resolve().parents[6]
        self.source = SourceProof("a" * 64, "0.4.2", "b" * 64,
                                  "README.md", "c" * 64, "pr.md", "d" * 64,
                                  "VERSION_HISTORY.md", "e" * 64, "Summary", None, None)
        inputs = PublicFreshGateInputs(
            self.root, None, "initial", "action", "CA-O-194", self.source,
            self.source.public_document_closure_sha256, None, None, None,
            self.root / ".caprmedio_tmp" / "unopened",
        )
        # Typed producer carrier without physical proof: every positive binding
        # case below explicitly replaces the reader, not release admission.
        self.evidence = SimpleNamespace(
            passed=True, evidence_root=".caprmedio_runtime/fresh-gate",
            candidate_snapshot_manifest_sha256=self.source.candidate_snapshot_manifest_sha256,
            framework_version=self.source.framework_version,
            version_toml_sha256=self.source.version_toml_sha256,
        )
        self.result = PublicNativeFullGateResult(
            inputs, None, None, self.evidence, "passed", "result.json", "f" * 64,
            "bridge.json", "1" * 64,
        )

    def gate(self, result=None, label="freeze_and_gate", source=None):
        return _gate(GateResult(ToolCallEvidence("input.json", "result.json"),
                                FreshPublicNativeFullGateBinding(result or self.result)),
                     label, source or self.source, project_root=self.root, selected_version="0.4.2")

    def test_positive_binding_calls_physical_reader(self):
        with patch("release_public_producer.verify_public_native_full_gate_result",
                   return_value=self.evidence) as reader:
            self.gate()
            reader.assert_called_once_with(self.result)

    def test_physical_reader_refusal_stops_binding(self):
        with patch("release_public_producer.verify_public_native_full_gate_result",
                   side_effect=ValueError("changed physical result")):
            with self.assertRaises(PublicReleaseError) as caught:
                self.gate()
            self.assertEqual("full-gate-unproven", caught.exception.code)

    def test_other_phase_source_or_project_refuses(self):
        for changes in ({"phase": "history_link"},
                        {"project_root": self.root / "other"},
                        {"public_document_closure_sha256": "0" * 64},
                        {"source": replace(self.source, version_history_sha256="0" * 64)}):
            with self.subTest(changes=changes), patch(
                "release_public_producer.verify_public_native_full_gate_result", return_value=self.evidence
            ), self.assertRaises(PublicReleaseError) as caught:
                self.gate(replace(self.result, inputs=replace(self.result.inputs, **changes)))
            self.assertEqual("stale-full-gate", caught.exception.code)

    def test_renewed_gate_requires_history_phase(self):
        with patch("release_public_producer.verify_public_native_full_gate_result", return_value=self.evidence):
            with self.assertRaises(PublicReleaseError):
                self.gate(label="renewed full gate")
            self.gate(replace(self.result, inputs=replace(self.result.inputs, phase="history_link")),
                      label="renewed full gate")

    def test_receipt_ref_reopens_not_just_attribute_lookup(self):
        with patch("release_public_producer.verify_public_native_full_gate_result",
                   return_value=self.evidence) as reader:
            self.assertEqual(".caprmedio_runtime/fresh-gate/receipt.json",
                             _full_gate_receipt_ref(FreshPublicNativeFullGateBinding(self.result)))
            reader.assert_called_once_with(self.result)

    def test_untyped_result_refuses(self):
        with self.assertRaises(PublicReleaseError) as caught:
            self.gate(object())
        self.assertEqual("invalid-full-gate", caught.exception.code)


if __name__ == "__main__":
    unittest.main()
