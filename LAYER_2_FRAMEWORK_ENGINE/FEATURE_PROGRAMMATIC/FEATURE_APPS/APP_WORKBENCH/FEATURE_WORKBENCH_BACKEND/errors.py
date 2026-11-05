# CA-M-462@10
# CA-M-463@6

"""Typed Workbench failures with stable public messages."""


class QueryExecutionError(RuntimeError):
    """A submitted read query failed while the Workbench remains usable."""


class WorkbenchUnavailableError(RuntimeError):
    """The Workbench owner cannot safely continue until restart."""
