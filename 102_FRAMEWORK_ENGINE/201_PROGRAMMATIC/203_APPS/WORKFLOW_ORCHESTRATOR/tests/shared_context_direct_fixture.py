# implementation of:
# Requirement: CA-R-2117
# Method: CA-M-431
"""Checked-in current O016 fixture with direct full R/M/E/D rows."""

from __future__ import annotations

import copy
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Mapping, cast

from shared_context_graph import build_graph
from shared_context_packets import _permission_fields, _plan_fields, _state_fields, _step_packets
from shared_context_support import CurrentFixtureError, checked_bytes, verify_identity


FIXTURE_ROOT = Path(__file__).with_name("fixtures") / "shared_context_direct"


# implementation of:
# Requirement: CA-R-2117
# Method: CA-M-431
def _inventory_rows(inventory: Mapping[str, Any]) -> tuple[Mapping[str, Any], ...]:
    groups = [inventory["required_authority"]]
    groups.extend(inventory["applicable_rde"][key] for key in ("requirements", "deliveries", "evaluations"))
    selected: dict[str, Mapping[str, Any]] = {}
    for group in groups:
        for row in group:
            selected[str(row["atom_id"])] = row
    return tuple(selected.values())


# implementation of:
# Requirement: CA-R-2117
# Method: CA-M-431
def _with_content(fixture: "DirectSharedContextFixture", row: Mapping[str, Any]) -> dict[str, Any]:
    result = {
        key: row[key]
        for key in ("atom_id", "version", "path", "sha256")
    }
    result["content"] = fixture._row_bytes(row).decode("utf-8")
    return result


# implementation of:
# Requirement: CA-R-2117
# Method: CA-M-431
@dataclass(frozen=True)
class DirectSharedContextFixture:
    """Frozen source closure for O016@18 and direct RMED validation."""

    root: Path = FIXTURE_ROOT

    @classmethod
    def load(cls) -> "DirectSharedContextFixture":
        try:
            manifest = json.loads((cls.root / "manifest.json").read_text(encoding="utf-8"))
        except (OSError, ValueError) as error:
            raise CurrentFixtureError("direct fixture manifest is unavailable") from error
        if manifest.get("kind") != "shared_context_direct_rmed_frozen_fixture":
            raise CurrentFixtureError("direct fixture kind is not admitted")
        return cls(cls.root)

    @property
    def manifest(self) -> dict[str, Any]:
        return cast(dict[str, Any], json.loads((self.root / "manifest.json").read_text(encoding="utf-8")))

    @property
    def support_inventory(self) -> dict[str, Any]:
        try:
            value = json.loads((self.root / "support_inventory.json").read_text(encoding="utf-8"))
        except (OSError, ValueError) as error:
            raise CurrentFixtureError("direct RMED inventory is unavailable") from error
        if value.get("kind") != "shared_context_direct_rmed_inventory" or value.get("not_implicit") is not True:
            raise CurrentFixtureError("direct RMED inventory is not an explicit selection")
        if "method_projection" in value:
            raise CurrentFixtureError("direct RMED inventory retains a legacy projection")
        return cast(dict[str, Any], value)

    def source_pins(self) -> tuple[Mapping[str, Any], ...]:
        pins = self.manifest.get("source_pins")
        if not isinstance(pins, list) or not pins:
            raise CurrentFixtureError("direct fixture has no source pins")
        return tuple(pin for pin in pins if isinstance(pin, Mapping))

    def source_bytes(self, atom_id: str) -> bytes:
        matches = [pin for pin in self.source_pins() if pin.get("atom_id") == atom_id]
        if len(matches) != 1:
            raise CurrentFixtureError(f"direct source pin is not unique: {atom_id}")
        pin = matches[0]
        return checked_bytes(self.root, str(pin["fixture_path"]), pin["sha256"], atom_id)

    def _support_rows(self) -> tuple[Mapping[str, Any], ...]:
        return _inventory_rows(self.support_inventory)

    def _method_rows(self) -> tuple[Mapping[str, Any], ...]:
        rows = self.support_inventory.get("methods")
        if not isinstance(rows, list) or not rows:
            raise CurrentFixtureError("direct Method inventory is unavailable")
        return tuple(row for row in rows if isinstance(row, Mapping))

    @property
    def trusted_methods(self) -> tuple[dict[str, Any], ...]:
        return tuple(_with_content(self, row) for row in self._method_rows())

    def _row_bytes(self, row: Mapping[str, Any]) -> bytes:
        return checked_bytes(self.root, str(row["fixture_path"]), row["sha256"], str(row["atom_id"]))

    def support_source_bytes(self, atom_id: str) -> bytes:
        matches = [row for row in self._support_rows() if row.get("atom_id") == atom_id]
        if len(matches) != 1:
            raise CurrentFixtureError(f"direct RMED source is not unique: {atom_id}")
        return self._row_bytes(matches[0])

    def method_source_pins(self) -> tuple[Mapping[str, Any], ...]:
        return self._method_rows()

    def method_source_bytes(self, atom_id: str) -> bytes:
        matches = [row for row in self._method_rows() if row.get("atom_id") == atom_id]
        if len(matches) != 1:
            raise CurrentFixtureError(f"direct Method source is not unique: {atom_id}")
        return self._row_bytes(matches[0])

    def verify(self) -> None:
        for pin in self.source_pins():
            verify_identity(self.source_bytes(str(pin["atom_id"])), pin)
        for row in self._support_rows():
            verify_identity(self._row_bytes(row), row)
        for row in self._method_rows():
            verify_identity(self._row_bytes(row), row)

    def materialize(self, destination: Path) -> Path:
        destination = Path(destination)
        destination.mkdir(parents=True, exist_ok=False)
        control = destination / ".caprmedio_caprmedio"
        (control / "_journal").mkdir(parents=True)
        (destination / ".caprmedio_runtime").mkdir()
        (destination / ".git").mkdir()
        settings = ('[project]\nkey = "shared-context-direct-fixture"\nname = "shared-context-direct-fixture"\n'
                    'repository_slug = "fixture"\n[artifacts.identity]\nproject_prefix = "CA"\n')
        (control / "caprmedio_project_settings.toml").write_text(settings, encoding="utf-8")
        for pin in self.source_pins():
            target = destination / str(pin["source_path"])
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(self.source_bytes(str(pin["atom_id"])))
        for row in (*self._support_rows(), *self._method_rows()):
            target = destination / str(row["path"])
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(self._row_bytes(row))
        return destination

    def graph(self) -> dict[str, Any]:
        graph = build_graph(self)
        graph["workflow"] = {"atom_id": "CA-O-016", "version": 18}
        return graph

    def native_implementation_parameters(self) -> dict[str, Any]:
        self.verify()
        inventory = self.support_inventory
        source_bindings = [dict(pin) for pin in self.source_pins()]
        direct_rows = {
            packet_key: [_with_content(self, row) for row in inventory["applicable_rde"][source_key]]
            for packet_key, source_key in (
                ("requirements", "requirements"), ("delivery", "deliveries"), ("evaluations", "evaluations")
            )
        }
        base: dict[str, Any] = {
            "context": "Integrated",
            "selected_project": {
                "kind": "selected_project",
                "source_root": ".caprmedio_caprmedio",
                "source_references": source_bindings,
            },
            "source_bindings": source_bindings,
            "methods": [dict(row) for row in self.trusted_methods],
            **direct_rows,
        }
        base.update(_permission_fields())
        base.update(_plan_fields())
        base.update(_state_fields(inventory["applicable_rde"]))
        return {
            "base_packet": base,
            "run_visit_limits": {"CA-O-231": 4, "CA-O-094": 2},
            "step_packets": _step_packets(source_bindings),
        }

    def packet_variant(self, **changes: object) -> dict[str, Any]:
        packet = copy.deepcopy(self.native_implementation_parameters())
        base = packet["base_packet"]
        if isinstance(changes.get("stale_atom"), str):
            binding = next(row for row in base["source_bindings"] if row["atom_id"] == changes["stale_atom"])
            binding["sha256"] = "0" * 64
        if isinstance(changes.get("candidate"), str):
            base["candidate"] = changes["candidate"]
        return packet


CurrentDirectSharedContextFixture = DirectSharedContextFixture

