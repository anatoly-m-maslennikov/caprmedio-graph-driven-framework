# CA-D-673@15
# CA-D-697@2

"""Convert native result values without changing their positional structure."""

from __future__ import annotations

import base64
import datetime as dt
import json
import math
from collections.abc import Mapping
from decimal import Decimal
from typing import Any


_SAFE_INTEGER = 2**53 - 1
_UNREPRESENTABLE = object()


def _scalar(value: Any) -> Any:
    if value is None or isinstance(value, (str, bool)):
        return value
    if isinstance(value, int):
        return str(value) if abs(value) > _SAFE_INTEGER else value
    if isinstance(value, float):
        if not math.isfinite(value):
            raise ValueError("query result contains NaN or infinity")
        return value
    if isinstance(value, Decimal):
        return str(value)
    if isinstance(value, bytes):
        return "base64:" + base64.b64encode(value).decode("ascii")
    if isinstance(value, (dt.datetime, dt.date, dt.time)):
        return value.isoformat()
    return _UNREPRESENTABLE


def result_value(value: Any) -> Any:
    """Return one public JSON-compatible value or raise for an unsupported value."""

    scalar = _scalar(value)
    if scalar is not _UNREPRESENTABLE:
        return scalar
    if isinstance(value, (list, tuple)):
        return [result_value(item) for item in value]
    if isinstance(value, Mapping):
        if any(not isinstance(key, str) for key in value):
            raise ValueError("query result mapping keys must be strings")
        return {key: result_value(item) for key, item in value.items()}
    raise ValueError(f"unsupported query result value: {type(value).__name__}")


def group_key(value: Any) -> str:
    """Provide an equality key after conversion while keeping the original value public."""

    return json.dumps(value, ensure_ascii=False, separators=(",", ":"), sort_keys=True)
