# Roadmap and KPIs

```text
  2026  Nov  Dec | 2027 Jan  Feb  Mar  Apr  May  Jun  Jul  Aug  Sep  Oct  Nov  Dec | 2028 Jan
        [OP0]    |      [=====OP1=====]
                 |                [====OP2====]
                 |                          [====OP3====]
                 |                                    [====OP4====]
                 |                                              [====OP5====]
                 |                                                        [===OP6===]
                 |                                                                  [OP7]
  milestone:  v0.1      v0.2 (sim)    v0.3 (detect)  v0.4 (offline)  v0.5 (safe)  v0.6 (field)  v1.0
```

Dates move if a gate is not passed. A slipped gate is recorded in the AAR, never skipped.

## Releases

| Version | Exit criteria |
| --- | --- |
| v0.1.0 | Op 0 gate passed |
| v0.2.0 | Op 1: simulated search with coverage measured |
| v0.3.0 | Op 2: detector on Jetson with honest metrics |
| v0.4.0 | Op 3: full airplane-mode demo |
| v0.5.0 | Op 4: Guardian passes red team |
| v0.6.0 | Op 5: dry field exercise, TRL 4 evidence |
| v0.9.0 | Op 6: chaos-tested sync and dashboard |
| v1.0.0 | Op 7: release, video, paper draft |

## Project KPIs (tracked monthly in the GitHub Projects board)

| KPI | Target |
| --- | --- |
| Weekly build hours | 8–10 |
| Requirements with a passing test | rises every op; 100% MUST by v1.0 |
| Open safety-relevant bugs at a gate | 0 |
| CI on `main` | green |
| FEMA courses completed | 5 of 5 by Op 5 |
| Budget spent vs plan (about €650–700) | within 10% |
