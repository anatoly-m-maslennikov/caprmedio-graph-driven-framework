"""Bound lifecycle effects read through Workbench and publish index changes."""
import hashlib
import os
import sys
import tempfile
from pathlib import Path
from unittest.mock import patch

import pytest

TOOLS = Path(__file__).resolve().parents[1]
ROOT = TOOLS.parents[2]
sys.path.insert(0, str(TOOLS))
from ATOM_LIFECYCLE import directory_effect, effects, source  # noqa: E402


class Reader:
    def __init__(self):
        self.events = []
        self.fail_sync = False

    def lifecycle_read(self, path, *, descriptor=None):
        self.events.append(("read", path))
        return path.read_bytes() if descriptor is None else os.pread(descriptor, os.fstat(descriptor).st_size, 0)

    def lifecycle_changed(self, old, new):
        self.events.append(("changed", old, new))
        if self.fail_sync:
            raise RuntimeError("unavailable")


@pytest.fixture
def carrier_dir():
    base = ROOT / ".caprmedio_tmp/CA-P-2791/CA-P-2934/carrier-effects"
    base.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(dir=base) as directory:
        yield Path(directory)


def test_bound_create_update_and_remove_use_workbench(carrier_dir):
    path = carrier_dir / "CA-R-100-TEST.md"
    reader = Reader()
    with source.bind_query_reader(reader), patch.object(
            effects, "_read", side_effect=AssertionError("direct Atom read")):
        assert not effects.create(ROOT, path, b"one").errors
        assert reader.events == [("changed", None, path), ("read", path)]
        reader.events.clear()
        assert not effects.replace(ROOT, path, hashlib.sha256(b"one").hexdigest(), b"two").errors
        assert reader.events == [("read", path), ("read", path), ("changed", path, path), ("read", path)]
        reader.events.clear()
        assert not effects.remove(ROOT, path, hashlib.sha256(b"two").hexdigest()).errors
        assert reader.events == [("read", path), ("changed", path, None)]


def test_failed_sync_reports_committed_effect(carrier_dir):
    path = carrier_dir / "CA-R-100-TEST.md"
    reader = Reader()
    reader.fail_sync = True
    with patch.object(effects, "_reader", return_value=reader):
        result = effects.create(ROOT, path, b"one")
    assert path.read_bytes() == b"one"
    assert result.effects[0]["operation"] == "create"
    assert result.effects[0]["state"] == "unknown"
    assert result.errors[0]["code"] == "effect_uncertain"
    assert result.errors[0]["message"] == "Workbench synchronization failed"


def test_readback_allows_metadata_change_after_verified_content(carrier_dir):
    path = carrier_dir / "CA-R-100-TEST.md"
    reader = Reader()
    read = reader.lifecycle_read

    def read_then_change_mode(target, *, descriptor=None):
        raw = read(target, descriptor=descriptor)
        target.chmod(0o640)
        return raw

    with source.bind_query_reader(reader), patch.object(reader, "lifecycle_read", read_then_change_mode):
        result = effects.create(ROOT, path, b"one")
    assert not result.errors
    assert result.effects[0]["state"] == "known"


def test_readback_rejects_carrier_replacement_after_verified_content(carrier_dir):
    path = carrier_dir / "CA-R-100-TEST.md"
    replacement = carrier_dir / "replacement.md"
    replacement.write_bytes(b"concurrent edit")
    reader = Reader()
    read = reader.lifecycle_read

    def read_then_replace(target, *, descriptor=None):
        raw = read(target, descriptor=descriptor)
        replacement.replace(target)
        return raw

    with source.bind_query_reader(reader), patch.object(reader, "lifecycle_read", read_then_replace):
        result = effects.create(ROOT, path, b"one")

    assert path.read_bytes() == b"concurrent edit"
    assert result.effects[0]["state"] == "unknown"
    assert result.errors[0]["code"] == "effect_uncertain"


def test_bound_reader_rejects_symlink_without_reading_it(carrier_dir):
    target = carrier_dir / "target"
    target.write_bytes(b"one")
    path = carrier_dir / "CA-R-100-TEST.md"
    path.symlink_to(target)
    reader = Reader()
    with source.bind_query_reader(reader):
        result = effects.remove(ROOT, path, hashlib.sha256(b"one").hexdigest())
    assert result.errors
    assert not reader.events
    assert target.read_bytes() == b"one"


def test_directory_move_reads_atoms_through_workbench(carrier_dir):
    source = carrier_dir / "source"
    source.mkdir()
    atom = source / "CA-R-100-TEST.md"
    atom.write_bytes(b"atom")
    (source / "asset.bin").write_bytes(b"asset")
    destination = carrier_dir / "destination"
    reader = Reader()
    with patch.object(effects, "_reader", side_effect=lambda path: reader if path.name == atom.name else None), \
            patch.object(effects, "_read", wraps=effects._read) as direct:
        result = directory_effect.move_directory(ROOT, source, destination)
    assert not result.errors
    assert (destination / atom.name).read_bytes() == b"atom"
    assert (destination / "asset.bin").read_bytes() == b"asset"
    assert any(event == ("changed", None, destination / atom.name) for event in reader.events)
    assert any(event == ("changed", atom, None) for event in reader.events)
    assert all(call.args[1] != atom.name for call in direct.call_args_list)
