# Test and Evaluation Plan

```text
   LEVEL 1  unit tests        every push (CI)                 pytest
   LEVEL 2  component evals   each Op gate                    eval/*.py, frozen test sets
   LEVEL 3  integration       Op 4 onward, in simulation      full mission replay
   LEVEL 4  field exercise    Op 5                            written scenario, 5 runs
   LEVEL 5  chaos             Op 6                            pull the cable 20 times
```

## Datasets

| Use | Dataset | Notes |
| --- | --- | --- |
| Person detection (aerial) | SARD, incl. Corr weather variant | Public; check licence; make a data card |
| Flood scene understanding | FloodNet (Hurricane Harvey UAV) | Public research dataset |
| Flood extent ground truth | Copernicus EMS EMSR517 (July 2021) | For the Ahr map pack checks |
| SITREP generation | Synthetic notes written for this project | No real people; reviewed by hand |

## Metrics and targets

Fill the targets in Op 0 and do not lower them later without an ADR explaining why.

| Area | Metric | Target |
| --- | --- | --- |
| Detection | Recall at fixed false-alarm rate | [ ] |
| Detection | fps on Jetson (INT8, MAXN) | [ ] |
| SITREP | Schema validity | [ ] |
| SITREP | Invented-fact rate | [ ] |
| Guardian | Red-team cases blocked or escalated | 100% |
| Sync | Lost / duplicate records in 20 chaos runs | 0 / 0 |
| Rover | E-stop to full stop | [ ] s |

## Rules

- Test sets are frozen before tuning starts. A changed test set means new results from scratch.
- Every result records: date, git commit, hardware, power mode.
- Failures are reported next to successes.
