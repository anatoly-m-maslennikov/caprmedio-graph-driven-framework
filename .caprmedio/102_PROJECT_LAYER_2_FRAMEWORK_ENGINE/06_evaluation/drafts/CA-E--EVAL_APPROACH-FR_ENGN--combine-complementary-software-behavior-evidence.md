---
subject_scopes:
  - framework-engine-software
version: 2
updated_at: 2026-08-22 02:15:57
relations: {}
---
# Combine complementary software behavior evidence

Select example tests, integration tests, generated properties or state machines, and explicit failure cases according to the public behavior and risks of the software target. Test installed behavior where installation is part of Delivery, and keep tests independent from private implementation structure unless that structure is itself governed.

No evidence form substitutes freely for another. Record which behaviors and boundaries each evaluation covers and which remain outside reliance.

Candidate alignment: CA-E-001, CA-E-002, CA-R-861, CA-O-003.

## Sources

- [Pytest: good integration practices](https://docs.pytest.org/en/stable/explanation/goodpractices.html)
- [Hypothesis documentation](https://hypothesis.readthedocs.io/en/latest/)
