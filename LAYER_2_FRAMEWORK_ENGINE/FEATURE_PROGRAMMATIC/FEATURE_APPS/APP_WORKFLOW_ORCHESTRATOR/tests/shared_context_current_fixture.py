from __future__ import annotations
from dataclasses import dataclass
import json
from pathlib import Path
from typing import Any, Mapping, cast
from shared_context_support import (
    CurrentFixtureError,
    checked_bytes,
    method_projection_content as read_method_projection,
    method_source_bytes as read_method_source,
    support_rows,
    support_source_bytes as read_support_source,
    verify_identity,
)
from shared_context_packets import (
    build_native_parameters,
    packet_bindings_are_current as packet_bindings_current,
    packet_variant as build_packet_variant,
)
from shared_context_graph import build_graph

FIXTURE_ROOT = Path(__file__).with_name("fixtures") / "shared_context_current"


@dataclass(frozen=True)
class CurrentSharedContextFixture:
    root: Path = FIXTURE_ROOT

    @classmethod
    def load(cls) -> "CurrentSharedContextFixture":
        try:
            manifest = json.loads((cls.root / "manifest.json").read_text(encoding="utf-8"))
        except (OSError, ValueError) as error:
            raise CurrentFixtureError("current fixture manifest is unavailable") from error
        if manifest.get("kind") != "shared_context_current_frozen_fixture":
            raise CurrentFixtureError("current fixture kind is not admitted")
        return cls(cls.root)

    @property
    def manifest(self) -> dict[str, Any]:
        return cast(
            dict[str, Any],
            json.loads((self.root / "manifest.json").read_text(encoding="utf-8")),
        )

    @property
    def support_inventory(self) -> dict[str, Any]:
        try:
            value = json.loads((self.root / "support_inventory.json").read_text(encoding="utf-8"))
        except (OSError, ValueError) as error:
            raise CurrentFixtureError("current support inventory is unavailable") from error
        if (
            value.get("kind") != "shared_context_support_inventory"
            or value.get("not_implicit") is not True
        ):
            raise CurrentFixtureError("current support inventory is not an explicit selection")
        return cast(dict[str, Any], value)

    def source_pins(self) -> tuple[Mapping[str, Any], ...]:
        pins = self.manifest.get("source_pins")
        if not isinstance(pins, list) or not pins:
            raise CurrentFixtureError("current fixture has no source pins")
        return tuple(pin for pin in pins if isinstance(pin, Mapping))

    def source_bytes(self, atom_id: str) -> bytes:
        matches = [pin for pin in self.source_pins() if pin.get("atom_id") == atom_id]
        if len(matches) != 1:
            raise CurrentFixtureError(f"source pin is not unique: {atom_id}")
        pin = matches[0]
        return checked_bytes(self.root, str(pin["fixture_path"]), pin["sha256"], atom_id)

    def _support_rows(self) -> tuple[Mapping[str, Any], ...]:
        return support_rows(self.support_inventory)

    def support_source_bytes(self, atom_id: str) -> bytes:
        return read_support_source(self.root, self.support_inventory, atom_id)

    def method_projection_content(self) -> str:
        return read_method_projection(self.root, self.support_inventory)

    def method_source_pins(self) -> tuple[Mapping[str, Any], ...]:
        return tuple(self.support_inventory["method_projection"]["sources"])

    def method_source_bytes(self, atom_id: str) -> bytes:
        return read_method_source(self.root, self.support_inventory, atom_id)

    def verify(self) -> None:
        for pin in self.source_pins():
            verify_identity(self.source_bytes(str(pin["atom_id"])), pin)
        for pin in self._support_rows():
            verify_identity(self.support_source_bytes(str(pin["atom_id"])), pin)
        for pin in self.method_source_pins():
            verify_identity(self.method_source_bytes(str(pin["atom_id"])), pin)
        self.method_projection_content()

    def materialize(self, destination: Path) -> Path:
        destination = Path(destination)
        destination.mkdir(parents=True, exist_ok=False)
        control = destination / ".caprmedio_caprmedio"
        (control / "_journal").mkdir(parents=True)
        (destination / ".caprmedio_runtime").mkdir()
        (destination / ".git").mkdir()
        settings = (
            '[project]\nkey = "shared-context-current-fixture"\n'
            'name = "shared-context-current-fixture"\nrepository_slug = "fixture"\n'
            '[artifacts.identity]\nproject_prefix = "CA"\n'
        )
        (control / "caprmedio_project_settings.toml").write_text(settings, encoding="utf-8")
        for pin in self.source_pins():
            target = destination / str(pin["source_path"])
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(self.source_bytes(str(pin["atom_id"])))
        for pin in self.method_source_pins():
            target = destination / str(pin["path"])
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(self.method_source_bytes(str(pin["atom_id"])))
        return destination

    def native_implementation_parameters(self) -> dict[str, Any]:
        return build_native_parameters(self)

    def packet_variant(self, **changes: object) -> dict[str, Any]:
        return build_packet_variant(self, **changes)

    def packet_bindings_are_current(self, packet: Mapping[str, Any]) -> bool:
        return packet_bindings_current(self, packet)

    def graph(self) -> dict[str, Any]:
        return build_graph(self)
