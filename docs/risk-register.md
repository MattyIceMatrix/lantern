# Project Risk Register

Project risks (schedule, money, people, technology). System hazards live in `safety-case.md`.

```text
   IMPACT
     5 |            R-03        R-01
     4 |      R-06        R-02
     3 |  R-08       R-04  R-05
     2 |       R-07
     1 |
       +---------------------------
         1    2    3    4    5    LIKELIHOOD
```

| ID | Risk | L | I | Owner | Response | Trigger to watch |
| --- | --- | --- | --- | --- | --- | --- |
| R-01 | Weekly hours drop (work, study load) and ops slip | 4 | 5 | Matthew | Fixed weekly build slot; smaller gates | 2 weeks under 6 h |
| R-02 | 3B LLM too slow on 8 GB Jetson | 4 | 4 | Matthew | Smaller model, 4-bit quantisation, shorter outputs | Op 3 latency bench |
| R-03 | Rover hardware damaged in field test | 2 | 5 | Matthew | Spare parts budget, speed limit, dry field only | any crash |
| R-04 | Dataset licences block publishing results | 3 | 3 | Matthew | Check licence before training; data cards | new dataset |
| R-05 | Map data services change or go offline | 3 | 3 | Matthew | Cache raw downloads; record versions in MANIFEST | failed download |
| R-06 | Scope creep (new features before gates) | 3 | 4 | Matthew | Post-v1 label; ADR for scope changes | issue count without REQ |
| R-07 | Cloud costs exceed free tier | 2 | 2 | Matthew | Budget alarm at €5 | alarm fires |
| R-08 | Feedback from rescue professionals is hard to get | 3 | 3 | Matthew | Ask THW local chapter after Op 3 demo | no reply in 4 weeks |

Review this register at every gate. Close risks that no longer apply; add new ones from the AAR.
