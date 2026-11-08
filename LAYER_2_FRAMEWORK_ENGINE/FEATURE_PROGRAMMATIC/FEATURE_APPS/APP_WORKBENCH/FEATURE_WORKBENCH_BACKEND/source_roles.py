# CA-R-3009@1

"""Admitted Workbench source-role directory and filename markers."""

from __future__ import annotations

import re


ROLES = {
    "01_concern",
    "02_analysis",
    "03_plan",
    "04_requirement",
    "05_method",
    "06_evaluation",
    "07_delivery",
    "08_implementation",
    "09_operations",
}
ARCHIVE_PARTS = {"archive", "archived", "_projection"}
FILENAME_MARKER = re.compile(
    rb"^(?:[0-9]+-)?[A-Za-z0-9-]+-(?P<role>[A-Za-z][A-Za-z0-9]*)-"
    rb"(?:[0-9]+|[Dd][Rr][Aa][Ff][Tt])(?:[-.@]|$)"
)
HEADER_MARKER = re.compile(
    rb"^[ \t]*(?:['\"]?)(?:atom_id|role|content_role)(?:['\"]?):", re.MULTILINE
)
ROLE_MARKERS = {
    "01_concern": {"C", "CONC", "CONCERN"},
    "02_analysis": {"A", "ANAL", "ANALYSIS", "ANRP"},
    "03_plan": {"P", "PLAN", "EPIC", "TASK"},
    "04_requirement": {"R", "REQ", "REQU", "REQUIREMENT"},
    "05_method": {"M", "METH", "METHOD"},
    "06_evaluation": {"E", "EVAL", "EVALUATION"},
    "07_delivery": {"D", "DEL", "DELIVERY"},
    "08_implementation": {"I", "IMPL", "IMPLEMENTATION"},
    "09_operations": {"O", "OPER", "OPERATION", "OPERATIONS", "ACTION", "WORKFLOW", "STEP"},
}
