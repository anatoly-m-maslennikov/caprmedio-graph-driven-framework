---
subject_scopes:
  - python-engineering
version: 2
updated_at: 2026-08-23 17:40:00 +0400
relations:
  derived_from:
    - CA-A-057
---
# Bind Tool effect results to the canonical operation

Apply this candidate only after the shared PROGRAMMATIC file-and-subprocess Method (`CA-M-161`) applies to a Tool operation. The Tool-specific adapter must bind every admitted effect request and returned receipt to that canonical operation's sealed target or explicit argument contract, preserve the operation identity through recovery, and return the Tool's declared structured outcome.

This candidate does not select the shared file-replacement or subprocess-safety procedure, a platform envelope, or an MCP protocol. It specializes only the Tool operation-to-effect-result boundary and leaves all effect policy to `CA-M-161` and the owning current Tool Requirement.

Candidate alignment: CA-R-004, CA-R-827, CA-R-846, CA-D-001, CA-R-861.

## Sources

- [Python documentation: subprocess security considerations](https://docs.python.org/3.14/library/subprocess.html#security-considerations)
- [Python documentation: tempfile](https://docs.python.org/3.14/library/tempfile.html)
- [Python documentation: os.replace](https://docs.python.org/3.14/library/os.html#os.replace)
