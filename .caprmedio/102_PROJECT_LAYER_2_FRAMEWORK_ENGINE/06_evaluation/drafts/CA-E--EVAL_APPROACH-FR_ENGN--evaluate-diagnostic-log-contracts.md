---
subject_scopes:
  - framework-engine-software
  - observability
version: 2
updated_at: 2026-08-22 02:15:57
relations: {}
---
# Evaluate diagnostic log contracts

For each logging surface, verify the required schema fields, severity selection, component and operation context, canonical action or event correlation, deterministic serialization where required, and exclusion of secrets and unnecessary governed content.

Exercise normal, warning, failed, and critical-stop paths separately. Confirm that logs diagnose execution without becoming a second owner of Work Journal meaning.

Candidate alignment: CA-E-001, CA-E-002, CA-M-002, CA-D-002.

## Sources

- [Python Logging HOWTO](https://docs.python.org/3.14/howto/logging.html)
- [Python Logging Cookbook: contextual information](https://docs.python.org/3.14/howto/logging-cookbook.html#adding-contextual-information-to-your-logging-output)
- [OpenTelemetry Logs data model](https://opentelemetry.io/docs/specs/otel/logs/data-model/)
