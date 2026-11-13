# Safety Case (FMEA)

```text
        /\
       /  \      Failure Mode and Effects Analysis
      / !! \     RPN = Severity x Occurrence x Detection   (each 1-10, higher = worse)
     /______\    Anything with Severity >= 9 gets a mitigation, whatever its RPN.
```

## Hazard log

| ID | Part | Failure mode | Effect | S | O | D | RPN | Mitigation | Verified by |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| H-01 | Detector | Misses a person (false negative) | Sector marked clear while someone is there | 10 | [ ] | [ ] | | Never auto-clear on detector alone; team lead confirms | REQ-008 test |
| H-02 | Detector | False alarm | Team time wasted | 4 | [ ] | [ ] | | Show confidence; batch review | Op 2 eval |
| H-03 | Field Brain | Invented fact in SITREP | Wrong resources sent | 9 | [ ] | [ ] | | GRPO penalty; source note attached to every SITREP | REQ-006 |
| H-04 | Agents | Prompt injection via voice note | Unsafe action proposed | 8 | [ ] | [ ] | | Guardian policy check; red-team suite | REQ-007 |
| H-05 | Rover | Drives into deep or moving water | Rover lost; rescuer follows it | 9 | [ ] | [ ] | | Depth/geofence rule from HQ zones; speed limit; e-stop | REQ-012 |
| H-06 | Map pack | Out-of-date roads | Bad route | 6 | [ ] | [ ] | | Show data date; SLAM map overrides | Op 1 |
| H-07 | Sync | Duplicate or lost report | Coordination centre confused | 7 | [ ] | [ ] | | Idempotent outbox | REQ-010 |
| H-08 | Battery | LiPo fire during charging | Injury, equipment loss | 9 | [ ] | [ ] | | Charging bag, never unattended, checklist | Op 5 checklist |

## Safety principles

1. **Human in the loop.** LANTERN proposes; a trained person decides.
2. **Fail visible.** Any uncertainty is shown, never hidden.
3. **Fail safe.** On error, the rover stops and the system says why.
4. **Prototype only.** No real-incident use without adoption by a rescue organisation.
