"""Project-bound MCP recording adapter; the native appender owns serialization."""

from __future__ import annotations

from pathlib import Path
from types import ModuleType
from typing import TYPE_CHECKING, Any, Mapping

if TYPE_CHECKING:
    from append_change_records import AppendChangeRecordsRequest


class AppendChangeRecordsAdapter:
    def __init__(self, root: Path, native: ModuleType) -> None:
        self.root = root
        self.native = native

    def invoke(self, request: AppendChangeRecordsRequest | Mapping[str, Any]) -> dict[str, Any]:
        native = self.native
        self.root = self.root.resolve()
        if not isinstance(request, native.AppendChangeRecordsRequest):
            request = native.AppendChangeRecordsRequest.model_validate(request)
        context, events = native.validate_context(
            native._normalise_context({"context": request.root.context})
        )
        if Path(context["trigger"]["repository"]["root"]).resolve() != self.root:
            raise native.ToolError(
                "descriptor-root-mismatch", "The sealed context belongs to another Project"
            )
        partition = {name: context[name] for name in ("author", "local_date", "timezone")}
        predictions = native.predict_sealed_event_receipts(self.root, events, **partition)
        result = {
            "resolved_targets": {
                "repository": str(self.root),
                "action_id": context["action_id"],
                "event_ids": [event["event_id"] for event in events],
            },
            "planned_effects": {"journal_records": events, "receipts": predictions},
            "validation_results": [
                {"name": "sealed-context", "ok": True},
                {"name": "sealed-events", "ok": True},
                {"name": "bound-project", "ok": True},
            ],
        }
        retained = self._read_retained(events, partition)
        if not request.root.apply:
            return native._json_result(
                ok=True, mode="dry-run", result={**result, "receipts": predictions}, diagnostics=[]
            )
        return self._append_events(events, partition, retained, result)

    def _read_retained(self, events: list[dict], partition: dict) -> dict:
        native = self.native
        retained = {}
        for event in events:
            try:
                pending, sealed, append_context, _ = native._read_pending_event(
                    self.root, event["event_id"]
                )
            except native.WorkJournalError as error:
                if error.code != "pending-not-found":
                    raise
                continue
            if native.canonical_json_bytes(sealed) != native.canonical_json_bytes(event) or any(
                append_context[name] != partition[name] for name in partition
            ):
                raise native.WorkJournalError(
                    "identity-collision",
                    "Retained pending evidence differs from the supplied sealed observation",
                )
            retained[event["event_id"]] = pending
        return retained

    def _append_events(
        self, events: list[dict], partition: dict, retained: dict, result: dict
    ) -> dict:
        native = self.native
        receipts = []
        index = 0
        try:
            for index, event in enumerate(events):
                if event["event_id"] not in retained:
                    retained[event["event_id"]] = native.store_pending_event(
                        self.root,
                        event,
                        native.seal_append_context(self.root, event, **partition),
                        result_ref=None,
                        effect_refs=[],
                        diagnostic="Journal recording pending",
                    )
                receipts.append(native.recover_pending_event(self.root, event["event_id"]))
                retained.pop(event["event_id"], None)
        except (native.ToolError, native.WorkJournalError, OSError, RuntimeError) as error:
            return self._record_failure(events, partition, retained, result, receipts, index, error)
        return native._json_result(
            ok=True,
            mode="apply",
            result={**result, "state": "complete", "receipts": receipts},
            diagnostics=[],
        )

    def _record_failure(
        self,
        events: list[dict],
        partition: dict,
        retained: dict,
        result: dict,
        receipts: list[dict],
        index: int,
        error: Exception,
    ) -> dict:
        native = self.native
        pending_errors = []
        try:
            predictions = native.predict_sealed_event_receipts(
                self.root, events[index:], **partition
            )
            receipts.extend(
                {key: value for key, value in receipt.items() if key != "disposition"}
                for receipt in predictions
                if receipt.get("disposition") == "reused"
            )
        except (native.WorkJournalError, OSError, RuntimeError) as prediction_error:
            predictions = []
            pending_errors.append(str(prediction_error))
        for offset, event in enumerate(events[index:]):
            if event["event_id"] in retained:
                continue
            try:
                append_context = native.seal_append_context(self.root, event, **partition)
                if predictions:
                    append_context["partition_ref"] = predictions[offset]["carrier"]
                    append_context.pop("append_context_digest")
                    append_context["append_context_digest"] = native.canonical_json_digest(
                        append_context
                    )
                retained[event["event_id"]] = native.store_pending_event(
                    self.root,
                    event,
                    append_context,
                    result_ref=None,
                    effect_refs=[],
                    diagnostic=str(error),
                )
            except (native.WorkJournalError, OSError, RuntimeError) as pending_error:
                pending_errors.append(str(pending_error))
        return native._json_result(
            ok=False,
            mode="apply",
            result={
                **result,
                "state": "recording_pending",
                "receipts": receipts,
                "pending_events": list(retained.values()),
                "unattempted_event_ids": [event["event_id"] for event in events[index + 1 :]],
                "inspection_required": bool(pending_errors),
                "pending_errors": pending_errors,
            },
            diagnostics=[
                {"code": getattr(error, "code", "journal-write-failed"), "message": str(error)}
            ],
        )
