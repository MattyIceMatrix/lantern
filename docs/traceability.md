# Traceability Matrix

```text
   NEED (ConOps) --> REQ-xxx --> DESIGN (module / ADR) --> TEST (file::name) --> RESULT (date, pass/fail)
```

A reviewer should be able to pick any requirement and follow it to the code and the test that proves it.

| REQ | Design | Test | Result |
| --- | --- | --- | --- |
| REQ-001 | brain/, scout/, agents/ (no network calls) | tests/test_offline.py::test_no_sockets | not run |
| REQ-002 | mappack/build.sh, config/area.yaml | mappack/checks.py | not run |
| REQ-003 | scout/detector | eval/detector_eval.py | not run |
| REQ-004 | TensorRT INT8 engine | eval/bench_jetson.py | not run |
| REQ-005 | model/schemas.py::Sitrep | tests/test_schemas.py | xfail (Op 0 starter) |
| REQ-006 | brain/ fine-tune + reward | eval/sitrep_eval.py | not run |
| REQ-007 | guardian/engine.py | tests/test_guardian.py | not run |
| REQ-008 | guardian/policies.yaml | tests/test_guardian.py | not run |
| REQ-009 | guardian/audit.py | tests/test_audit.py | not run |
| REQ-010 | sync/outbox.py | eval/chaos_sync.py | not run |
| REQ-011 | guardian/privacy.py | tests/test_privacy.py | not run |
| REQ-012 | rover e-stop wiring | field log, Op 5 | not run |

Status values: `not run` · `xfail` · `PASS (yyyy-mm-dd, hardware)` · `FAIL (link to issue)`.
