# Requirements Specification

```text
   REQ-xxx  "The system SHALL ..."   ->  verified by  ->  TEST / DEMO / INSPECTION / ANALYSIS
```

Every requirement must be **testable**: someone else can check it and get the same answer.
IDs never change once written; deleted requirements are marked `WITHDRAWN`, not removed.

## Starter set (examples to keep, edit or replace in Op 0)

| ID | Requirement | Priority | Verify by | Op |
| --- | --- | --- | --- | --- |
| REQ-001 | The system SHALL perform all mission functions with no network connection. | MUST | DEMO (airplane mode) | 3 |
| REQ-002 | The map pack SHALL cover the area in `config/area.yaml` with roads, buildings, terrain and flood zones HQ10/HQ100/HQextrem. | MUST | INSPECTION | 1 |
| REQ-003 | The person detector SHALL reach recall >= [target] at <= [N] false alarms per image on the frozen test set. | MUST | TEST | 2 |
| REQ-004 | Detection SHALL run at >= [N] frames per second on the Jetson Orin Nano. | SHOULD | TEST | 2 |
| REQ-005 | Every SITREP SHALL be valid against the `Sitrep` schema. | MUST | TEST | 3 |
| REQ-006 | A SITREP SHALL NOT contain facts absent from the source note (invented-fact rate <= [target]). | MUST | TEST | 3 |
| REQ-007 | Every agent tool call SHALL be checked by the Guardian before execution. | MUST | TEST | 4 |
| REQ-008 | Actions marked high-risk in `guardian/policies.yaml` SHALL require human approval. | MUST | TEST | 4 |
| REQ-009 | The audit log SHALL detect any modified or deleted entry. | MUST | TEST | 4 |
| REQ-010 | Sync SHALL deliver every record exactly once in effect (no loss, no duplicates) across interrupted uploads. | MUST | TEST (chaos) | 6 |
| REQ-011 | Personal data SHALL be pseudonymised before leaving the device. | MUST | TEST + INSPECTION | 4, 6 |
| REQ-012 | The rover SHALL stop within [N] s of the physical e-stop being pressed. | MUST | TEST | 5 |

## Writing rules

```text
  GOOD: "Detection SHALL run at >= 15 fps on the Jetson Orin Nano in MAXN power mode."
  BAD:  "Detection should be fast."                  <- not testable
  BAD:  "Use YOLO for detection."                    <- a design choice, put it in an ADR
```
