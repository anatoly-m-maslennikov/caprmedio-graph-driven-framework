# CA-R-1108@21
# CA-M-506@2
# CA-D-704@1

"""Fail-closed descriptor-driven MCP registration for installed Tools."""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from dataclasses import dataclass
import hashlib
import json
from pathlib import Path
from types import ModuleType
from typing import Any

from pydantic import TypeAdapter
from registered_tool_providers import RegisteredToolError, load_provider


_PACKAGE_ROOT = Path(__file__).resolve().parents[3]
_DESCRIPTOR_FIELDS = frozenset(
    {
        "schema_version",
        "identity",
        "binding",
        "models",
        "callable",
        "effect_hints",
        "permissions",
        "source_pins",
        "admission",
        "diagnostics",
        "failure_contract",
    }
)
_IDENTITY_FIELDS = frozenset({"name", "tool_version", "title", "description", "purpose"})
_BINDING_FIELDS = frozenset({"delivery_atom_id", "action_ids", "implementation_entrypoint"})
_MODEL_FIELDS = frozenset({"input", "output"})
_SYMBOL_FIELDS = frozenset({"module", "symbol"})
_EFFECT_HINT_FIELDS = frozenset(
    {
        "read_only_hint",
        "destructive_hint",
        "idempotent_hint",
        "open_world_hint",
    }
)
_PERMISSION_FIELDS = frozenset({"execution", "enforcement", "metadata_grants_permission"})
_ADMISSION_FIELDS = frozenset({"module", "symbol", "refresh_after_success"})
_RESERVED_PUBLIC_NAMES = frozenset(
    {
        "workflow_orchestrator",
        "reload_mcp_implementation",
        "get_mcp_reload_status",
    }
)


class ToolRegistryAssetError(ValueError):
    """The generated MCP registration asset is unavailable or unsafe."""


@dataclass(frozen=True)
class RegistrySnapshot:
    """A deterministic, non-executing Tool-registry projection."""

    tools: tuple[Mapping[str, object], ...]
    quarantined: tuple[Mapping[str, object], ...]
    digest: str
    registered: tuple[Mapping[str, object], ...] | None = None
    withheld: tuple[Mapping[str, object], ...] = ()

    @property
    def registered_names(self) -> frozenset[str]:
        source = self.tools if self.registered is None else self.registered
        return frozenset(
            name for item in source if isinstance((name := item.get("mcp_name")), str) and name
        )

    def projection(self) -> dict[str, object]:
        return {
            "schema_version": 1,
            "tools": [dict(item) for item in self.tools],
            "quarantined": [dict(item) for item in self.quarantined],
            "withheld": [dict(item) for item in self.withheld],
            "public_mcp_names": sorted(self.registered_names),
            "digest": self.digest,
        }


def _canonical_json(value: object) -> bytes:
    return json.dumps(
        value, ensure_ascii=False, sort_keys=True, separators=(",", ":"), allow_nan=False
    ).encode("utf-8")


def _diagnostic(field: str, code: str) -> dict[str, str]:
    return {"field": field, "code": code}


def _load_provider(
    entrypoint: object, package_root: str | Path = _PACKAGE_ROOT
) -> tuple[str, str, ModuleType]:
    """Compatibility loader; compilation always passes an explicit package root."""

    return load_provider(package_root, entrypoint)


def _mapping(
    value: object, field: str, expected: frozenset[str] | None = None
) -> Mapping[str, object]:
    if not isinstance(value, Mapping):
        raise RegisteredToolError(f"{field}: missing or invalid")
    result = dict(value)
    if expected is not None and set(result) != expected:
        raise RegisteredToolError(f"{field}: incomplete or conflicting")
    return result


def _string(value: object, field: str) -> str:
    if not isinstance(value, str) or not value:
        raise RegisteredToolError(f"{field}: missing or invalid")
    return value


def _model_symbol(module: ModuleType, entrypoint: str, value: object, field: str) -> object:
    reference = _mapping(value, field, _SYMBOL_FIELDS)
    # ``module`` is deliberately an installed Engine-relative entrypoint, not
    # the private, content-hashed module name used by the isolated loader.
    # That keeps descriptors portable while resolving only the module whose
    # bytes were sealed and executed above.
    if reference["module"] != entrypoint:
        raise RegisteredToolError(f"{field}.module: unresolved canonical model")
    try:
        model = getattr(module, _string(reference["symbol"], f"{field}.symbol"))
        # No provider JSON schema is accepted: derive it from this symbol.
        TypeAdapter(model).json_schema()
    except (AttributeError, TypeError, ValueError) as error:
        raise RegisteredToolError(f"{field}: unresolved canonical model") from error
    return model


def _source_pins_match_binding(value: object, binding: Mapping[str, object]) -> bool:
    """Require source-pin identity to agree with the verified catalog row.

    The catalog has the verified Delivery carrier path and digest.  It does
    not expose a separately sealed Action-carrier record, so source pins carry
    only the catalog-comparable Delivery and Action identities.  Version/hash
    enforcement remains at the canonical Action boundary rather than being
    re-declared here without a trustworthy resolver.
    """

    pins = _mapping(value, "source_pins", frozenset({"delivery_atom_id", "action_ids"}))
    action_ids = pins["action_ids"]
    return (
        pins["delivery_atom_id"] == binding.get("source_atom")
        and isinstance(action_ids, list)
        and action_ids == binding.get("action_ids")
        and bool(action_ids)
        and all(isinstance(action_id, str) and action_id for action_id in action_ids)
        and len(action_ids) == len(set(action_ids))
    )


def _validated_descriptor(  # noqa: C901
    package_root: str | Path, binding: Mapping[str, object]
) -> dict[str, object]:
    entrypoint, code_hash, module = _load_provider(binding.get("entrypoint"), package_root)
    describe = getattr(module, "describe_tool", None)
    if not callable(describe):
        raise RegisteredToolError("provider: required descriptor API is absent")
    try:
        descriptor = _mapping(describe(), "descriptor", _DESCRIPTOR_FIELDS)
    except RegisteredToolError:
        raise
    except Exception as error:
        raise RegisteredToolError("descriptor: unavailable") from error
    if type(descriptor["schema_version"]) is not int or descriptor["schema_version"] != 1:
        raise RegisteredToolError("schema_version: unsupported")

    identity = _mapping(descriptor["identity"], "identity", _IDENTITY_FIELDS)
    for field in ("name", "title", "description", "purpose"):
        _string(identity[field], f"identity.{field}")
    if type(identity["tool_version"]) is not int or identity["tool_version"] < 1:
        raise RegisteredToolError("identity.tool_version: invalid")

    tool_binding = _mapping(descriptor["binding"], "binding", _BINDING_FIELDS)
    actions = tool_binding["action_ids"]
    if (
        not isinstance(actions, list)
        or not actions
        or not all(isinstance(action, str) and action for action in actions)
        or len(actions) != len(set(actions))
        or tool_binding["implementation_entrypoint"] != entrypoint
    ):
        raise RegisteredToolError("binding: conflicts with installed provider")
    raw_mcp_name = binding.get("mcp_name")
    if raw_mcp_name is not None and not isinstance(raw_mcp_name, str):
        raise RegisteredToolError("provider.mcp_name: invalid")
    mcp_name = raw_mcp_name or None
    code_binding = {
        "name": identity["name"],
        "mcp_name": raw_mcp_name,
        "entrypoint": entrypoint,
        "source_atom": tool_binding["delivery_atom_id"],
        "action_ids": actions,
    }
    for field in ("name", "source_atom", "action_ids"):
        if field in binding and binding[field] != code_binding[field]:
            raise RegisteredToolError(f"binding.{field}: conflicts with installed provider")

    models = _mapping(descriptor["models"], "models", _MODEL_FIELDS)
    input_model = _model_symbol(module, entrypoint, models["input"], "models.input")
    output_model = _model_symbol(module, entrypoint, models["output"], "models.output")
    callable_ref = _mapping(descriptor["callable"], "callable", _SYMBOL_FIELDS)
    if callable_ref["module"] != entrypoint or callable_ref["symbol"] != "create_adapter":
        raise RegisteredToolError("callable: unresolved adapter factory")
    if not callable(getattr(module, "create_adapter", None)):
        raise RegisteredToolError("callable: unresolved adapter factory")

    hints = _mapping(descriptor["effect_hints"], "effect_hints", _EFFECT_HINT_FIELDS)
    if not all(type(hints[field]) is bool for field in _EFFECT_HINT_FIELDS):
        raise RegisteredToolError("effect_hints: invalid")
    permissions = _mapping(descriptor["permissions"], "permissions", _PERMISSION_FIELDS)
    if (
        permissions["execution"] != "operator_authorized"
        or permissions["enforcement"] != "canonical_action_boundary"
        or permissions["metadata_grants_permission"] is not False
    ):
        raise RegisteredToolError("permissions: invalid")
    if not _source_pins_match_binding(descriptor["source_pins"], code_binding):
        raise RegisteredToolError("source_pins: conflicts with installed provider")
    for field in ("diagnostics", "failure_contract"):
        if not _mapping(descriptor[field], field):
            raise RegisteredToolError(f"{field}: incomplete")
    admission = _mapping(descriptor["admission"], "admission", _ADMISSION_FIELDS)
    if admission["module"] != entrypoint:
        raise RegisteredToolError("admission.module: unresolved")
    admitted = getattr(module, _string(admission["symbol"], "admission.symbol"), None)
    if not callable(admitted) or type(admission["refresh_after_success"]) is not bool:
        raise RegisteredToolError("admission: invalid")
    if (
        _mapping(descriptor["failure_contract"], "failure_contract").get("invokes_on_discovery")
        is not False
    ):
        raise RegisteredToolError("failure_contract.invokes_on_discovery: invalid")
    try:
        is_admitted = admitted(code_binding)
    except Exception as error:
        raise RegisteredToolError("admission: unavailable") from error
    if is_admitted is not True:
        raise RegisteredToolError("admission: current binding is not admitted")

    return {
        "name": identity["name"],
        "mcp_name": mcp_name,
        "descriptor": descriptor,
        "source": {
            **code_binding,
            "code_sha256": code_hash,
        },
        "entrypoint": entrypoint,
        "code_sha256": code_hash,
        "input_schema": TypeAdapter(input_model).json_schema(),
        "output_schema": TypeAdapter(output_model).json_schema(),
    }


def _binding_identity(binding: Mapping[str, object]) -> dict[str, object]:
    return {
        key: binding.get(key)
        for key in ("name", "mcp_name", "source_atom", "source_path", "entrypoint")
    }


def _snapshot(
    tools: Sequence[Mapping[str, object]],
    quarantined: Sequence[Mapping[str, object]],
    *,
    registered: Sequence[Mapping[str, object]] | None = None,
    withheld: Sequence[Mapping[str, object]] = (),
) -> RegistrySnapshot:
    valid = sorted(
        (dict(item) for item in tools),
        key=lambda item: (
            str(item.get("mcp_name") or ""),
            str(item["name"]),
            _canonical_json(item["source"]),
        ),
    )
    unavailable = sorted((dict(item) for item in quarantined), key=_canonical_json)
    deferred = sorted((dict(item) for item in withheld), key=_canonical_json)
    actual = (
        None
        if registered is None
        else sorted((dict(item) for item in registered), key=_canonical_json)
    )
    semantic = {
        "schema_version": 1,
        "tools": valid,
        "quarantined": unavailable,
        "registered": actual,
        "withheld": deferred,
    }
    return RegistrySnapshot(
        tuple(valid),
        tuple(unavailable),
        hashlib.sha256(_canonical_json(semantic)).hexdigest(),
        None if actual is None else tuple(actual),
        tuple(deferred),
    )


def compile_registry(root: str | Path, bindings: Sequence[Mapping[str, Any]]) -> RegistrySnapshot:
    """Compile an effect-free deterministic projection of explicit providers."""

    tools: list[dict[str, object]] = []
    quarantined: list[dict[str, object]] = []
    for binding in sorted((dict(item) for item in bindings), key=_canonical_json):
        try:
            tools.append(_validated_descriptor(root, binding))
        except RegisteredToolError as error:
            field, _, code = str(error).partition(": ")
            quarantined.append(
                {
                    "source": _binding_identity(binding),
                    "diagnostics": [_diagnostic(field, code or "invalid")],
                }
            )

    names: dict[str, int] = {}
    public_names: dict[str, int] = {}
    for item in tools:
        name = str(item["name"])
        mcp_name = item["mcp_name"]
        names[name] = names.get(name, 0) + 1
        if isinstance(mcp_name, str) and mcp_name:
            public_names[mcp_name] = public_names.get(mcp_name, 0) + 1
    valid: list[dict[str, object]] = []
    for item in tools:
        name = str(item["name"])
        mcp_name = item["mcp_name"]
        if mcp_name and mcp_name in _RESERVED_PUBLIC_NAMES:
            quarantined.append(
                {
                    "source": dict(item["source"]),
                    "diagnostics": [_diagnostic("identity.mcp_name", "reserved MCP helper name")],
                }
            )
        elif names[name] != 1 or (mcp_name and public_names[mcp_name] != 1):
            field = "identity.name" if names[name] != 1 else "catalog.mcp_name"
            quarantined.append(
                {
                    "source": dict(item["source"]),
                    "diagnostics": [_diagnostic(field, "ambiguous catalog binding")],
                }
            )
        else:
            valid.append(item)
    return _snapshot(valid, quarantined)


__all__ = [
    "RegisteredToolError",
    "RegistrySnapshot",
    "ToolRegistryAssetError",
    "compile_registry",
]
