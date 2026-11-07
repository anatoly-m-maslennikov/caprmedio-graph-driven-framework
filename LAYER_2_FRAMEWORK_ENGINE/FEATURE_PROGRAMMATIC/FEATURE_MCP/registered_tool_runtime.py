# CA-R-1108@21
# CA-M-506@2
# CA-D-704@1

"""Project canonical Tool adapters into the MCP transport."""

from __future__ import annotations

from collections.abc import Callable, Collection, Mapping, Sequence
from dataclasses import replace
import inspect
from pathlib import Path
from typing import Any

from mcp.server.mcpserver.exceptions import ToolError
from mcp.types import ToolAnnotations
from pydantic import TypeAdapter

from operation_error_boundary import (
    FailureRecord,
    classify_failure,
    emit_failure_diagnostic,
    operation_error_boundary,
)
from project_selection import active_selection
from registered_tool_registry import (
    _DESCRIPTOR_FIELDS,
    _EFFECT_HINT_FIELDS,
    _IDENTITY_FIELDS,
    _MODEL_FIELDS,
    _PACKAGE_ROOT,
    _load_provider,
    _mapping,
    _model_symbol,
    _snapshot,
    compile_registry,
    RegisteredToolError,
    RegistrySnapshot,
    ToolRegistryAssetError,
)
from technical_diagnostics import make_technical_logger


def _classify_public_failure(error: Exception) -> FailureRecord | None:
    """Keep known public refusals attributable without exposing exception text."""

    if isinstance(error, RegisteredToolError):
        return FailureRecord("WARNING", "source_binding_invalid", "source binding is invalid")
    if isinstance(error, ToolError):
        return FailureRecord(
            "WARNING", "request_rejected", "request or source binding was rejected"
        )
    return None


def _invoke_wrapper(
    *,
    adapter: object,
    input_model: object,
    output_model: object,
    mcp_name: str,
    root: str | Path,
    catalog_binding: Mapping[str, object] | None = None,
) -> Callable[..., object]:
    """Make the SDK-visible wrapper with exactly one typed request parameter."""

    del catalog_binding
    invoke = getattr(adapter, "invoke", None)
    if not callable(invoke):
        raise RegisteredToolError("callable.invoke: adapter is unresolved")
    output_adapter = TypeAdapter(output_model)

    def logger():
        try:
            selection = active_selection(root)
            value, _error = make_technical_logger(selection.settings, Path(root))
            return replace(value, component="MCP_REGISTRY") if value is not None else None
        except Exception:
            return None

    def on_error(error: Exception) -> object:
        failure = classify_failure(error, classifier=_classify_public_failure)
        diagnostic_error = emit_failure_diagnostic(logger(), failure, operation=mcp_name)
        message = f"{failure.code}: {failure.message}"
        if diagnostic_error:
            message += "; technical diagnostic unavailable"
        raise ToolError(f"{mcp_name}: {message}") from error

    @operation_error_boundary(on_error=on_error)
    async def guarded_invoke(request: object) -> object:
        result = invoke(request)
        if inspect.isawaitable(result):
            result = await result
        return output_adapter.validate_python(result)

    async def registered_tool(request: object) -> object:
        return await guarded_invoke(request)

    registered_tool.__name__ = mcp_name
    registered_tool.__annotations__ = {"request": input_model, "return": output_model}
    return registered_tool


def register_catalog_tools(
    server: Any,
    root: str | Path,
    tools: Sequence[Mapping[str, Any]],
    *,
    occupied_public_names: Sequence[str] = (),
    registered_public_names: Sequence[str] = (),
    tool_blacklist: Collection[str] = (),
    package_root: str | Path | None = None,
) -> RegistrySnapshot:
    """Compile explicit providers and register only unoccupied public names."""

    code_root = _PACKAGE_ROOT if package_root is None else package_root
    snapshot = compile_registry(code_root, tools)
    return _register_snapshot(
        server,
        root,
        snapshot,
        occupied_public_names=occupied_public_names,
        registered_public_names=registered_public_names,
        tool_blacklist=tool_blacklist,
        package_root=code_root,
    )


def register_generated_tools(
    server: Any,
    root: str | Path,
    generated: RegistrySnapshot,
    *,
    occupied_public_names: Sequence[str] = (),
    registered_public_names: Sequence[str] = (),
    tool_blacklist: Collection[str] = (),
    package_root: str | Path | None = None,
) -> RegistrySnapshot:
    """Register only providers whose installed code still matches the asset."""

    providers: list[dict[str, object]] = []
    for record in generated.tools:
        source = record.get("source")
        if not isinstance(source, Mapping):
            raise ToolRegistryAssetError("generated MCP registry has an invalid provider binding")
        providers.append(
            {"entrypoint": record.get("entrypoint"), "mcp_name": source.get("mcp_name")}
        )
    code_root = _PACKAGE_ROOT if package_root is None else package_root
    current = compile_registry(code_root, providers)
    if current.projection() != generated.projection():
        raise ToolRegistryAssetError(
            "generated MCP registry does not match installed provider code"
        )
    return _register_snapshot(
        server,
        root,
        current,
        occupied_public_names=occupied_public_names,
        registered_public_names=registered_public_names,
        tool_blacklist=tool_blacklist,
        package_root=code_root,
    )


def _register_snapshot(
    server: Any,
    root: str | Path,
    snapshot: RegistrySnapshot,
    *,
    occupied_public_names: Sequence[str],
    registered_public_names: Sequence[str],
    tool_blacklist: Collection[str],
    package_root: str | Path,
) -> RegistrySnapshot:
    registered: list[Mapping[str, object]] = []
    quarantined: list[Mapping[str, object]] = list(snapshot.quarantined)
    withheld: list[Mapping[str, object]] = []
    frontier_binders: list[Callable[..., None]] = []
    occupied = frozenset(name for name in occupied_public_names if isinstance(name, str) and name)
    excluded = frozenset(tool_blacklist)
    for record in snapshot.tools:
        mcp_name = record.get("mcp_name")
        if not isinstance(mcp_name, str) or not mcp_name:
            withheld.append(
                {
                    "source": {**dict(record["source"]), "name": record["name"], "mcp_name": None},
                    "reason": "source_only",
                }
            )
            continue
        if mcp_name in excluded:
            withheld.append(
                {
                    "source": {
                        **dict(record["source"]),
                        "name": record["name"],
                        "mcp_name": mcp_name,
                    },
                    "reason": "tool_blacklisted",
                }
            )
            continue
        if mcp_name in occupied:
            withheld.append(
                {
                    "source": {
                        **dict(record["source"]),
                        "name": record["name"],
                        "mcp_name": mcp_name,
                    },
                    "reason": "public_name_owned_by_route",
                }
            )
            continue
        try:
            entrypoint, code_hash, module = _load_provider(record["entrypoint"], package_root)
            if entrypoint != record["entrypoint"] or code_hash != record["code_sha256"]:
                raise RegisteredToolError("entrypoint: changed after compilation")
            descriptor = _mapping(record["descriptor"], "descriptor", _DESCRIPTOR_FIELDS)
            models = _mapping(descriptor["models"], "models", _MODEL_FIELDS)
            adapter = getattr(module, "create_adapter")(root)
            wrapper = _invoke_wrapper(
                adapter=adapter,
                input_model=_model_symbol(module, entrypoint, models["input"], "models.input"),
                output_model=_model_symbol(module, entrypoint, models["output"], "models.output"),
                mcp_name=mcp_name,
                root=root,
            )
            identity = _mapping(descriptor["identity"], "identity", _IDENTITY_FIELDS)
            server.add_tool(
                wrapper,
                name=mcp_name,
                title=str(identity["title"]),
                description=str(identity["description"]),
                annotations=ToolAnnotations(
                    **dict(
                        _mapping(descriptor["effect_hints"], "effect_hints", _EFFECT_HINT_FIELDS)
                    )
                ),
                structured_output=True,
            )
            registered.append(record)
            bind_frontier = getattr(adapter, "bind_server_frontier", None)
            if callable(bind_frontier):
                frontier_binders.append(bind_frontier)
        except Exception as error:
            field, _, code = (
                str(error).partition(": ")
                if isinstance(error, RegisteredToolError)
                else ("registration", "", type(error).__name__)
            )
            quarantined.append(
                {
                    "source": dict(record["source"]),
                    "diagnostics": [{"field": field, "code": code or "failed"}],
                }
            )
    result = _snapshot(snapshot.tools, quarantined, registered=registered, withheld=withheld)
    names = (frozenset(registered_public_names) | result.registered_names) - excluded
    for bind_frontier in frontier_binders:
        bind_frontier(
            registered_names=names, quarantined=result.quarantined, withheld=result.withheld
        )
    return result
