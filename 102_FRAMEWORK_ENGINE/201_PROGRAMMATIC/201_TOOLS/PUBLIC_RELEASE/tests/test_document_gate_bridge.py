from __future__ import annotations
import json
import sys, unittest
from dataclasses import replace
from pathlib import Path

TOOLS = Path(__file__).resolve().parents[2]
for item in (TOOLS, TOOLS / "PUBLIC_RELEASE", TOOLS / "RELEASE_VERSION"):
    if str(item) not in sys.path: sys.path.insert(0, str(item))

from document_gate_bridge import DocumentGateBridgeError, canonical_bytes, derive_bridge
from public_release import SourceProof
from release_full_gate import NativeFullGateEvidence
from release_public_gate import PublicFreshGateInputs
from release_package_evidence import PackageEvidenceView
from release_retained_package import RetainedNativePackageEvidence
from release_test_phases import ReleaseTestPhaseMap

S = "a" * 64

class DocumentGateBridgeTests(unittest.TestCase):
    def source(self):
        return SourceProof(S, "0.4.1", "b"*64, "README.md", "c"*64, "docs/pr.md", "d"*64, "VERSION_HISTORY.md", "e"*64, "Summary", None, None)
    def inputs(self, source, phase="initial"):
        # Pure non-authoritative encoding fixture: no session, packet, or
        # physical gate is implied by these unopened identity carriers.
        view = PackageEvidenceView("portable-1", S, "8"*64, "a"*64, "run-1",
                                   "b"*64, source.framework_version,
                                   source.version_toml_sha256, Path("unopened-package"),
                                   (), ReleaseTestPhaseMap((), "2"*64, (), ()))
        retained = RetainedNativePackageEvidence(view, "9"*64, Path("unopened-proof.json"))
        return PublicFreshGateInputs(Path("."), None, phase, "action-1", "CA-O-194",
                                    source, source.public_document_closure_sha256,
                                    None, retained, None, Path("unopened-attempt"))
    def evidence(self, source):
        return NativeFullGateEvidence(S, "sha256:"+"1"*64, "2"*64, "3"*64, "4"*64, "5"*64, "6"*64, "passed", "passed", ".caprmedio_runtime/gate", "7"*64, 1, "portable-1", "8"*64, "9"*64, "proof.json", "a"*64, "run-1", "b"*64, source.framework_version, source.version_toml_sha256)
    def test_closed_canonical_encoder_uses_reopened_phase_and_source(self):
        source=self.source(); bridge=derive_bridge(inputs=self.inputs(source), evidence=self.evidence(source), producer_result_ref="runtime/result.json")
        self.assertEqual("initial", bridge.phase); self.assertEqual(source.public_document_closure_sha256, bridge.public_document_closure_sha256)
        payload = canonical_bytes(bridge)
        self.assertEqual(payload, json.dumps(json.loads(payload), ensure_ascii=False, sort_keys=True, separators=(",", ":"), allow_nan=False).encode())
        self.assertEqual(11, len(bridge.__dict__))
    def test_refuses_forged_inputs_and_unsafe_reference(self):
        source=self.source(); evidence=self.evidence(source)
        with self.assertRaises(DocumentGateBridgeError): derive_bridge(inputs=object(), evidence=evidence, producer_result_ref="x.json")
        with self.assertRaises(DocumentGateBridgeError): derive_bridge(inputs=self.inputs(source), evidence=evidence, producer_result_ref="../x.json")
        bad=self.inputs(source); object.__setattr__(bad, "public_document_closure_sha256", "0"*64)
        with self.assertRaises(DocumentGateBridgeError): derive_bridge(inputs=bad, evidence=evidence, producer_result_ref="x.json")

    def test_other_identity_or_failed_receipt_refuses(self):
        source = self.source()
        changes = ({"candidate_snapshot_manifest_sha256": "0"*64},
                   {"framework_version": "0.4.3"}, {"version_toml_sha256": "0"*64},
                   {"package_manifest_sha256": "0"*64}, {"candidate_run_id": "other"},
                   {"package_schema": "legacy-2"}, {"outcome": "failed"},
                   {"receipt_sha256": None})
        for change in changes:
            with self.subTest(change=change), self.assertRaises(DocumentGateBridgeError):
                derive_bridge(inputs=self.inputs(source), evidence=replace(self.evidence(source), **change), producer_result_ref="result.json")

    def test_untyped_evidence_refuses_without_attribute_error(self):
        with self.assertRaises(DocumentGateBridgeError):
            derive_bridge(inputs=self.inputs(self.source()), evidence=object(), producer_result_ref="result.json")

    def test_unsafe_refs_refuse_without_reading(self):
        source = self.source()
        for reference in ("../result.json", "/result.json", ".env", "result.env", "x\n.json", "x\\y.json"):
            with self.subTest(reference=reference), self.assertRaises(DocumentGateBridgeError):
                derive_bridge(inputs=self.inputs(source), evidence=self.evidence(source), producer_result_ref=reference)
        with self.assertRaises(DocumentGateBridgeError):
            derive_bridge(inputs=self.inputs(source), evidence=replace(self.evidence(source), evidence_root="../gate"), producer_result_ref="result.json")

    def test_history_bridge_changes_closure_not_package(self):
        source = self.source()
        linked = replace(source, version_history_sha256="0"*64,
                         version_history_pr_url="https://github.com/owner/repo/pull/1", version_history_pr_number=1)
        initial = derive_bridge(inputs=self.inputs(source), evidence=self.evidence(source), producer_result_ref="initial.json")
        final = derive_bridge(inputs=self.inputs(linked, "history_link"), evidence=self.evidence(linked), producer_result_ref="history.json")
        self.assertEqual(initial.package_manifest_sha256, final.package_manifest_sha256)
        self.assertNotEqual(initial.public_document_closure_sha256, final.public_document_closure_sha256)

if __name__ == "__main__": unittest.main()
