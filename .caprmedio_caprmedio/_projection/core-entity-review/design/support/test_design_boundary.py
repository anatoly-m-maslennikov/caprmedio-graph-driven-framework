"""Regression checks for the review boundary, without touching source or output files."""
import copy
import hashlib
import importlib.util
import json
import pathlib
import tempfile
import unittest
from unittest.mock import patch
HERE=pathlib.Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location("review_validator",HERE/"verify_design_batches.py")
v=importlib.util.module_from_spec(spec);spec.loader.exec_module(v)
class EvidenceBoundaryTests(unittest.TestCase):
    def setUp(self):
        self.raw="---\natom_id: TEST\n---\n# Summary\n\nOnly a title\n\n## Scope\n\nx\n\n## Claim\n\nThe example Property is borne by its bearer.\n"
        self.pin={"atom_id":"TEST","atom_revision":1,"carrier_path":"example.md","carrier_sha256":hashlib.sha256(self.raw.encode()).hexdigest()}
        self.e={**self.pin,"start_line":14,"end_line":14,"quote":"The example Property is borne by its bearer."}
        self.e["text_sha256"]=hashlib.sha256(self.e["quote"].encode()).hexdigest()
    def test_main_claim_span_accepts(self):
        with patch.object(pathlib.Path,"read_text",return_value=self.raw):
            v.verify_evidence(self.e,{"TEST":self.pin})
    def test_summary_is_not_semantic_evidence(self):
        bad={**self.e,"start_line":4,"end_line":6,"quote":"# Summary\n\nOnly a title"}
        bad["text_sha256"]=hashlib.sha256(bad["quote"].encode()).hexdigest()
        with patch.object(pathlib.Path,"read_text",return_value=self.raw),self.assertRaises(AssertionError):
            v.verify_evidence(bad,{"TEST":self.pin})
    def test_metadata_is_not_semantic_evidence(self):
        bad={**self.e,"start_line":2,"end_line":2,"quote":"atom_id: TEST"}
        bad["text_sha256"]=hashlib.sha256(bad["quote"].encode()).hexdigest()
        with patch.object(pathlib.Path,"read_text",return_value=self.raw),self.assertRaises(AssertionError):
            v.verify_evidence(bad,{"TEST":self.pin})
    def test_forged_quote_rejected(self):
        bad={**self.e,"quote":"A forged claim","text_sha256":hashlib.sha256(b"A forged claim").hexdigest()}
        with patch.object(pathlib.Path,"read_text",return_value=self.raw),self.assertRaises(AssertionError):
            v.verify_evidence(bad,{"TEST":self.pin})
    def test_stale_reference_rejected(self):
        bad={**self.e,"carrier_sha256":"0"*64}
        with patch.object(pathlib.Path,"read_text",return_value=self.raw),self.assertRaises(AssertionError):
            v.verify_evidence(bad,{"TEST":self.pin})
    def test_bad_quote_hash_rejected(self):
        bad={**self.e,"text_sha256":"0"*64}
        with patch.object(pathlib.Path,"read_text",return_value=self.raw),self.assertRaises(AssertionError):
            v.verify_evidence(bad,{"TEST":self.pin})
if __name__=="__main__":
    unittest.main()
