# CA-R-2729@10
# CA-M-516@2
# CA-D-673@18
"""Deliver a cached result inline or as a temporary Project file."""
from __future__ import annotations

from typing import Any

from .result_files import write_result_file


def validate_delivery(delivery: str, result_format: str) -> None:
    if delivery not in {"inline", "file"}:
        raise ValueError("result_delivery must be inline or file")
    if result_format not in {"json_matrix", "csv", "toon"}:
        raise ValueError("unsupported result format")


def deliver(store: Any, root: Any, page: dict[str, Any], delivery: str, result_format: str, *, full: bool = False) -> dict[str, Any]:
    validate_delivery(delivery, result_format)
    page.pop("sql", None)
    if delivery == "inline":
        return page
    try:
        if full:
            def rows():
                offset = 0
                while offset < page["row_count"]:
                    chunk = store.page(page["query_id"], offset, page_size=1000)
                    yield from chunk["rows"]
                    offset += len(chunk["rows"])
                    if not chunk["rows"]:
                        break
            with store._lock:
                artifact = write_result_file(root, [column["name"] for column in page["columns"]], rows(), result_format=result_format, offset=0, has_more=False)
        else:
            artifact = write_result_file(root, [column["name"] for column in page["columns"]], page["rows"], result_format=result_format, offset=page["offset"], has_more=page["has_more"])
        page.pop("rows", None)
        page["result_file"] = artifact
    except Exception as error:
        page.pop("rows", None)
        page.update(outcome="partial", export_error=str(error))
    return page


def result_metadata(result: dict[str, Any]) -> dict[str, Any]:
    return {"status": "success", "error": None, "query_id": result["query_id"],
            "row_count": result["row_count"], "column_count": result["column_count"]}


def failed_metadata(error: Exception) -> dict[str, Any]:
    return {"status": "failed", "error": str(error), "query_id": None, "row_count": None, "column_count": None}

