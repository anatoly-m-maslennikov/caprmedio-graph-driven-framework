# CA-M-284@32
# CA-E-454@23
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from settings_carrier import read_settings_carrier, write_settings_carrier
from project_settings_schema import _parse_settings


class SettingsCarrierTest(unittest.TestCase):
    def test_readback_and_invalid_write_preserves_bytes(self):
        def validate(document):
            if set(document) != {"value"} or type(document["value"]) is not int:
                raise ValueError("invalid carrier")

        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "settings.toml"
            path.write_bytes(b"value = 1\n")
            write_settings_carrier(path, "value = 2\n", validate=validate)
            self.assertEqual(read_settings_carrier(path), {"value": 2})
            before = path.read_bytes()
            for text in ('value = "wrong"\n', 'value = [\n'):
                with self.assertRaises(ValueError):
                    write_settings_carrier(path, text, validate=validate)
                self.assertEqual(path.read_bytes(), before)

    def test_project_schema_write_rejects_unsupported_fields(self):
        valid = ('schema_version = "2.0"\n[project]\nname = "demo"\n'
                 '[artifacts.identity]\nproject_prefix = "DEMO"\n'
                 '[paths]\ncontrol_root = ".caprmedio_demo"\n')
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "settings.toml"
            write_settings_carrier(path, valid, validate=_parse_settings)
            self.assertEqual(_parse_settings(read_settings_carrier(path))[:3],
                             ("demo", "DEMO", ".caprmedio_demo"))
            before = path.read_bytes()
            with self.assertRaises(ValueError):
                write_settings_carrier(path, valid + '[historical]\nvalue = 1\n', validate=_parse_settings)
            self.assertEqual(path.read_bytes(), before)


if __name__ == "__main__":
    unittest.main()
