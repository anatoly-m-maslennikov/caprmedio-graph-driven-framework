"""Fail-closed descriptor-driven registration for installed MCP Tools.

The registry is an MCP transport projection.  Compilation discovers only
provider descriptions and canonical model symbols; it never invokes a Tool.
"""
from __future__ import annotations

from collections.abc import Callable, Mapping, Sequence
from dataclasses import dataclass
import hashlib
import importlib.util
import json
import os
from pathlib import Path, PurePosixPath
import re
import stat
import sys
from types import ModuleType
from typing import Any

from mcp.server.mcpserver.exceptions import ToolError
from mcp.types import ToolAnnotations
from pydantic import TypeAdapter


_ENTRYPOINT_PREFIX = PurePosixPath("102_FRAMEWORK_ENGINE/201_PROGRAMMATIC")
_PROGRAMMATIC_ROOT = Path(__file__).resolve().parents[1]
_DESCRIPTOR_FIELDS = frozenset({
    "schema_version", "identity", "binding", "models", "callable",
    "effect_hints", "permissions", "source_pins", "admission", "diagnostics",
    "failure_contract",
})
_IDENTITY_FIELDS = frozenset({"name", "tool_version", "title", "description", "purpose"})
_BINDING_FIELDS = frozenset({"delivery_atom_id", "action_ids", "implementation_entrypoint"})
_MODEL_FIELDS = frozenset({"input", "output"})
_SYMBOL_FIELDS = frozenset({"module", "symbol"})
_EFFECT_HINT_FIELDS = frozenset({
    "read_only_hint", "destructive_hint", "idempotent_hint", "open_world_hint",
})
_PERMISSION_FIELDS = frozenset({"execution", "enforcement", "metadata_grants_permission"})
_ADMISSION_FIELDS = frozenset({"module", "symbol", "refresh_after_success"})
_SHA256 = re.compile(r"[0-9a-f]{64}\Z")
_RESERVED_PUBLIC_NAMES = frozenset({
    "rmed_atoms_base_revise", "discover_tools", "discover_operations",
    "get_execution_context", "get_execution_status", "resume_execution_context",
    "watch_execution", "workflow_orchestrator", "reload_mcp_implementation",
    "get_mcp_reload_status",
})


class RegisteredToolError(ValueError):
    """A descriptor is not eligible for MCP projection."""


@dataclass(frozen=True)
class RegistrySnapshot:
    """A deterministic, non-executing Tool-registry projection."""

    tools: tuple[Mapping[str, object], ...]
    quarantined: tuple[Mapping[str, object], ...]
    digest: str

    @property
    def registered_names(self) -> frozenset[str]:
        return frozenset(str(item["mcp_name"]) for item in self.tools)

    def projection(self) -> dict[str, object]:
        return {
            "schema_version": 1,
            "tools": [dict(item) for item in self.tools],
            "quarantined": [dict(item) for item in self.quarantined],
            "digest": self.digest,
        }


# The cache is intentionally keyed by fresh, physically-read provider bytes.
_MODULE_CACHE: dict[Path, tuple[str, ModuleType]] = {}


def _canonical_json(value: object) -> bytes:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"), allow_nan=False).encode("utf-8")


def _diagnostic(field: str, code: str) -> dict[str, str]:
    return {"field": field, "code": code}


def _normalise_entrypoint(value: object) -> tuple[str, Path]:
    """Resolve one normalized Python member under this installed Engine only."""

    if not isinstance(value, str) or not value or "\\" in value:
        raise RegisteredToolError("entrypoint: invalid")
    raw = PurePosixPath(value)
    if (
        raw.is_absolute()
        or raw.as_posix() != value
        or any(part in {"", ".", ".."} for part in raw.parts)
        or any(part.lower().startswith(".env") or part.lower().endswith(".env") for part in raw.parts)
        or tuple(raw.parts[:len(_ENTRYPOINT_PREFIX.parts)]) != _ENTRYPOINT_PREFIX.parts
    ):
        raise RegisteredToolError("entrypoint: outside trusted programmatic root")
    relative = raw.relative_to(_ENTRYPOINT_PREFIX)
    if not relative.parts or relative.suffix != ".py":
        raise RegisteredToolError("entrypoint: not a Python module")
    candidate = _PROGRAMMATIC_ROOT.joinpath(*relative.parts)
    try:
        cursor = _PROGRAMMATIC_ROOT
        for part in relative.parts:
            cursor /= part
            if stat.S_ISLNK(os.lstat(cursor).st_mode):
                raise RegisteredToolError("entrypoint: symlink is not admitted")
        if not stat.S_ISREG(os.stat(candidate, follow_symlinks=False).st_mode):
            raise RegisteredToolError("entrypoint: not a regular file")
    except RegisteredToolError:
        raise
    except OSError as error:
        raise RegisteredToolError("entrypoint: unavailable") from error
    return raw.as_posix(), candidate


def _read_entrypoint(candidate: Path) -> tuple[str, bytes]:
    """Read exact module bytes without accepting aliases or replacement races."""

    flags = os.O_RDONLY | getattr(os, "O_CLOEXEC", 0) | getattr(os, "O_NOFOLLOW", 0)
    try:
        descriptor = os.open(candidate, flags)
    except OSError as error:
        raise RegisteredToolError("entrypoint: unavailable") from error
    try:
        before = os.fstat(descriptor)
        if not stat.S_ISREG(before.st_mode) or before.st_size > 8 * 1024 * 1024:
            raise RegisteredToolError("entrypoint: not a bounded regular file")
        payload = bytearray()
        while len(payload) <= 8 * 1024 * 1024:
            chunk = os.read(descriptor, min(65536, 8 * 1024 * 1024 + 1 - len(payload)))
            if not chunk:
                break
            payload.extend(chunk)
        after = os.fstat(descriptor)
        if (
            len(payload) > 8 * 1024 * 1024
            or before.st_dev != after.st_dev
            or before.st_ino != after.st_ino
            or before.st_size != after.st_size
            or len(payload) != before.st_size
        ):
            raise RegisteredToolError("entrypoint: changed while being read")
        return hashlib.sha256(payload).hexdigest(), bytes(payload)
    finally:
        os.close(descriptor)


def _load_provider(entrypoint: object) -> tuple[str, str, ModuleType]:
    canonical, candidate = _normalise_entrypoint(entrypoint)
    code_hash, payload = _read_entrypoint(candidate)
    cached = _MODULE_CACHE.get(candidate)
    if cached is not None and cached[0] == code_hash:
        return canonical, code_hash, cached[1]

    module_name = f"_caprmedio_registered_{code_hash}"
    spec = importlib.util.spec_from_file_location(module_name, candidate)
    if spec is None or spec.loader is None:
        raise RegisteredToolError("entrypoint: implementation is unavailable")
    module = importlib.util.module_from_spec(spec)
    previous = sys.modules.get(module_name)
    try:
        # Module-level annotations can need their own module while evaluating;
        # never leave the private import key installed afterwards.
        sys.modules[module_name] = module
        # Execute the same bytes that supplied ``code_hash``.  Delegating to
        # ``exec_module`` would reread the path and may select a stale pyc.
        exec(compile(payload, str(candidate), "exec", dont_inherit=True), module.__dict__)
    except Exception as error:
        raise RegisteredToolError("entrypoint: descriptor import failed") from error
    finally:
        if previous is None:
            sys.modules.pop(module_name, None)
        else:
            sys.modules[module_name] = previous
    _MODULE_CACHE[candidate] = (code_hash, module)
    return canonical, code_hash, module


def _mapping(value: object, field: str, expected: frozenset[str] | None = None) -> Mapping[str, object]:
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


def _validated_descriptor(binding: Mapping[str, object]) -> dict[str, object]:
    entrypoint, code_hash, module = _load_provider(binding.get("entrypoint"))
    if (
        not isinstance(binding.get("source_atom"), str)
        or not isinstance(binding.get("source_path"), str)
        or not isinstance(binding.get("sha256"), str)
        or _SHA256.fullmatch(binding["sha256"]) is None
    ):
        raise RegisteredToolError("source: missing or stale source pin")
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
        not isinstance(actions, list) or not actions
        or not all(isinstance(action, str) and action for action in actions)
        or len(actions) != len(set(actions))
        or tool_binding["delivery_atom_id"] != binding.get("source_atom")
        or actions != binding.get("action_ids")
        or tool_binding["implementation_entrypoint"] != entrypoint
        or identity["name"] != binding.get("name")
    ):
        raise RegisteredToolError("binding: conflicts with admitted catalog binding")
    mcp_name = _string(binding.get("mcp_name"), "catalog.mcp_name")

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
    if not _source_pins_match_binding(descriptor["source_pins"], binding):
        raise RegisteredToolError("source_pins: conflicts with admitted catalog binding")
    for field in ("diagnostics", "failure_contract"):
        if not _mapping(descriptor[field], field):
            raise RegisteredToolError(f"{field}: incomplete")
    admission = _mapping(descriptor["admission"], "admission", _ADMISSION_FIELDS)
    if admission["module"] != entrypoint:
        raise RegisteredToolError("admission.module: unresolved")
    admitted = getattr(module, _string(admission["symbol"], "admission.symbol"), None)
    if not callable(admitted) or type(admission["refresh_after_success"]) is not bool:
        raise RegisteredToolError("admission: invalid")
    if _mapping(descriptor["failure_contract"], "failure_contract").get("invokes_on_discovery") is not False:
        raise RegisteredToolError("failure_contract.invokes_on_discovery: invalid")
    try:
        is_admitted = admitted(binding)
    except Exception as error:
        raise RegisteredToolError("admission: unavailable") from error
    if is_admitted is not True:
        raise RegisteredToolError("admission: current binding is not admitted")

    return {
        "name": identity["name"],
        "mcp_name": mcp_name,
        "descriptor": descriptor,
        "source": {
            "source_atom": binding.get("source_atom"),
            "source_path": binding.get("source_path"),
            "sha256": binding.get("sha256"),
        },
        "catalog_binding": _catalog_binding(binding),
        "entrypoint": entrypoint,
        "code_sha256": code_hash,
        "input_schema": TypeAdapter(input_model).json_schema(),
        "output_schema": TypeAdapter(output_model).json_schema(),
    }


def _binding_identity(binding: Mapping[str, object]) -> dict[str, object]:
    return {key: binding.get(key) for key in ("name", "mcp_name", "source_atom", "source_path", "entrypoint")}


def _catalog_binding(binding: Mapping[str, object]) -> dict[str, object]:
    """The source pins that must still agree immediately before dispatch."""

    return {
        key: binding.get(key)
        for key in ("name", "mcp_name", "entrypoint", "action_ids", "source_atom", "source_path", "sha256")
    }


def _binding_is_fresh(root: str | Path, expected: Mapping[str, object]) -> bool:
    """Reopen discovery; startup admission alone never permits dispatch."""

    try:
        from capability_discovery.service import Service
        _atoms, current, _issues = Service(root).catalog()
    except (ImportError, OSError, TypeError, ValueError):
        return False
    return len([
        item for item in current
        if all(item.get(key) == value for key, value in expected.items())
    ]) == 1


def _snapshot(tools: Sequence[Mapping[str, object]], quarantined: Sequence[Mapping[str, object]]) -> RegistrySnapshot:
    valid = sorted((dict(item) for item in tools), key=lambda item: (
        str(item["mcp_name"]), str(item["name"]), _canonical_json(item["source"]),
    ))
    unavailable = sorted((dict(item) for item in quarantined), key=_canonical_json)
    semantic = {"schema_version": 1, "tools": valid, "quarantined": unavailable}
    return RegistrySnapshot(
        tuple(valid), tuple(unavailable), hashlib.sha256(_canonical_json(semantic)).hexdigest(),
    )


def compile_registry(root: str | Path, bindings: Sequence[Mapping[str, Any]]) -> RegistrySnapshot:
    """Compile an effect-free deterministic projection of one catalog snapshot."""

    del root  # Registry code must not inspect caller-controlled Project carriers.
    tools: list[dict[str, object]] = []
    quarantined: list[dict[str, object]] = []
    for binding in sorted((dict(item) for item in bindings), key=_canonical_json):
        try:
            tools.append(_validated_descriptor(binding))
        except RegisteredToolError as error:
            field, _, code = str(error).partition(": ")
            quarantined.append({"source": _binding_identity(binding), "diagnostics": [_diagnostic(field, code or "invalid")]})

    names: dict[str, int] = {}
    public_names: dict[str, int] = {}
    for item in tools:
        name, mcp_name = str(item["name"]), str(item["mcp_name"])
        names[name] = names.get(name, 0) + 1
        public_names[mcp_name] = public_names.get(mcp_name, 0) + 1
    valid: list[dict[str, object]] = []
    for item in tools:
        name, mcp_name = str(item["name"]), str(item["mcp_name"])
        if mcp_name in _RESERVED_PUBLIC_NAMES:
            quarantined.append({"source": dict(item["source"]), "diagnostics": [_diagnostic("identity.mcp_name", "reserved MCP helper name")]})
        elif names[name] != 1 or public_names[mcp_name] != 1:
            field = "identity.name" if names[name] != 1 else "catalog.mcp_name"
            quarantined.append({"source": dict(item["source"]), "diagnostics": [_diagnostic(field, "ambiguous catalog binding")]})
        else:
            valid.append(item)
    return _snapshot(valid, quarantined)


def _invoke_wrapper(
    *,
    adapter: object,
    input_model: object,
    output_model: object,
    mcp_name: str,
    root: str | Path,
    catalog_binding: Mapping[str, object],
) -> Callable[..., object]:
    """Make the SDK-visible wrapper with exactly one typed request parameter."""

    invoke = getattr(adapter, "invoke", None)
    if not callable(invoke):
        raise RegisteredToolError("callable.invoke: adapter is unresolved")
    output_adapter = TypeAdapter(output_model)

    def registered_tool(request: object) -> object:
        try:
            if not _binding_is_fresh(root, catalog_binding):
                raise ToolError(f"{mcp_name}: source binding is stale or unavailable")
            return output_adapter.validate_python(invoke(request))
        except ToolError:
            raise
        except Exception as error:
            raise ToolError(f"{mcp_name}: {error}") from error

    # Captured objects stay closures instead of optional default parameters,
    # avoiding accidental SDK request-schema fields.
    registered_tool.__name__ = mcp_name
    registered_tool.__annotations__ = {"request": input_model, "return": output_model}
    return registered_tool


def register_catalog_tools(server: Any, root: str | Path, tools: Sequence[Mapping[str, Any]]) -> RegistrySnapshot:
    """Compile and register every independently valid current descriptor."""

    snapshot = compile_registry(root, tools)
    registered: list[Mapping[str, object]] = []
    quarantined: list[Mapping[str, object]] = list(snapshot.quarantined)
    for record in snapshot.tools:
        try:
            entrypoint, code_hash, module = _load_provider(record["entrypoint"])
            if entrypoint != record["entrypoint"] or code_hash != record["code_sha256"]:
                raise RegisteredToolError("entrypoint: changed after compilation")
            descriptor = _mapping(record["descriptor"], "descriptor", _DESCRIPTOR_FIELDS)
            models = _mapping(descriptor["models"], "models", _MODEL_FIELDS)
            adapter = getattr(module, "create_adapter")(root)
            wrapper = _invoke_wrapper(
                adapter=adapter,
                input_model=_model_symbol(module, entrypoint, models["input"], "models.input"),
                output_model=_model_symbol(module, entrypoint, models["output"], "models.output"),
                mcp_name=str(record["mcp_name"]),
                root=root,
                catalog_binding=_mapping(record["catalog_binding"], "catalog_binding"),
            )
            identity = _mapping(descriptor["identity"], "identity", _IDENTITY_FIELDS)
            server.add_tool(
                wrapper,
                name=str(record["mcp_name"]),
                title=str(identity["title"]),
                description=str(identity["description"]),
                annotations=ToolAnnotations(**dict(_mapping(descriptor["effect_hints"], "effect_hints", _EFFECT_HINT_FIELDS))),
                structured_output=True,
            )
            registered.append(record)
        except Exception as error:
            if isinstance(error, RegisteredToolError):
                field, _, code = str(error).partition(": ")
            else:
                field, code = "registration", type(error).__name__
            quarantined.append({
                "source": dict(record["source"]),
                "diagnostics": [_diagnostic(field, code or "failed")],
            })
    return _snapshot(registered, quarantined)


__all__ = ["RegisteredToolError", "RegistrySnapshot", "compile_registry", "register_catalog_tools"]
