---
subject_scopes:
  - framework-engine-software
  - observability
version: 2
updated_at: 2026-08-22 01:50:50
relations: {}
---
# Emit structured contextual levelled logs

Emit diagnostic records from Tools, Apps, and MCP components through one project-owned logging abstraction and schema. Include timestamp, severity, component, operation, outcome, and the canonical action or event identifier when one exists. Use DEBUG for diagnostic detail, INFO for expected progress, WARNING for recoverable abnormal conditions, ERROR for failed operations, and CRITICAL only when continued operation is unsafe.

Keep concise human diagnostics at the CLI boundary. Logs diagnose execution; they reference rather than redefine governed Work Journal events. Exclude credentials, tokens, and unnecessary content from all levels.

Candidate alignment: CA-M-002, CA-M-003, CA-D-002, CA-O-003.

## Sources

- [Python Logging HOWTO](https://docs.python.org/3.14/howto/logging.html)
- [Python Logging Cookbook](https://docs.python.org/3.14/howto/logging-cookbook.html)
- [OpenTelemetry: logs](https://opentelemetry.io/docs/concepts/signals/logs/)
