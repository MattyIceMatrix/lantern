# LANTERN: The Full Plan

```text
   =====================================================================
     MISSION: an offline edge-AI kit that helps flood rescue teams find
     people, map damage and report, with no network at all.
   =====================================================================
```

The living version of this plan is the LANTERN Docs page in Claude. This file is the copy kept in the repo.

## 1. Why this project

- **Real problem:** July 2021, Ahr valley, Rhineland-Palatinate. 134 dead; the mobile network failed when it
  mattered most.
- **Real gap:** most AI tools need the cloud. LANTERN runs on a Jetson Orin Nano and needs nothing outside the kit.
- **Real skill spread:** it pulls together robotics, computer vision, LLMs, agents, security and cloud data:
  the clusters that show up again and again in the 142 Udacity projects.

## 2. The four parts

```text
   SCOUT ........ rover: perception, SLAM, search patterns          scout/
   FIELD BRAIN .. offline voice, small LLM SITREPs, RAG, translate  brain/
   GUARDIAN ..... policy engine, privacy, audit, red team           guardian/
   SYNC ......... store-and-forward to the cloud + dashboard        sync/
   (+ mission agents in agents/, shared data model in lantern_model/)
```

## 3. Two knowledge tracks

```text
   TRACK A: MAPS                            TRACK B: DOCTRINE
   ---------------------------------        ---------------------------------
   Geofabrik OSM -> osmium                  FEMA IS-100/200/700/800/230
   Protomaps pmtiles                        NIMS resource typing
   LVermGeo DGM1 terrain -> GDAL            NFPA 1006 rescue levels
   RLP HQ10 / HQ100 / HQextrem zones        INSARAG + FEMA marking systems
   Valhalla offline routing                 THW / BBK structure (Germany)
   Copernicus EMSR517 ground truth          -> doctrine/*.yaml, cited by RAG
   -> mappack/build.sh
```

## 4. The campaign (about 14 months at 8–10 h/week)

| Op | Codename | Months | Gate in one line |
| --- | --- | --- | --- |
| 0 | Groundwork | wk 1–3 | repo + CI + ConOps + 10 requirements |
| 1 | Pathfinder | 1–3 | sim rover maps and searches a flooded street |
| 2 | Night Vision | 3–5 | person detector, honest metrics, INT8 on Jetson |
| 3 | Radio Silence | 5–7 | voice note -> valid SITREP in airplane mode |
| 4 | Gatekeeper | 7–9 | agents + Guardian survive the red team |
| 5 | Boots on Ground | 9–11 | real rover, dry field exercise, TRL 4 |
| 6 | Relay | 11–13 | zero lost / duplicate records in chaos test |
| 7 | Debrief | 13–14 | v1.0.0, video, paper draft, talk |

Briefings: [`missions/`](../missions/README.md).

## 5. Engineering rigour

```text
   conops.md -> requirements.md -> traceability.md <- test-plan.md
                      |                    ^
                      v                    |
             safety-case.md (FMEA)    threat-model.md (STRIDE)    dpia.md (GDPR)
                      |
                 adr/  +  cards/ (model + data cards)  +  SBOM at release
```

Targets: TRL 4 (lab and dry-field validation) by Op 5, with a TRL 5 stretch goal.

## 6. Hardware and budget (about €650–700)

| Item | Approx. cost |
| --- | --- |
| Jetson Orin Nano Super developer kit (67 TOPS) | $249 |
| Rover chassis, motors, driver | ~€150 |
| 2D lidar + camera | ~€150 |
| Battery, charger, LiPo bag, e-stop, wiring | ~€80 |
| A1/A3 drone certificate (LBA) | ~€25 |
| Cloud (free tier + budget alarm) | ~€0–10/month |

## 7. How we build together

- Matthew writes every line of LANTERN code. Claude briefs, reviews, debugs alongside and runs defend-it checks.
- Udacity projects are done solo first (Honor Code); LANTERN carries the skill further.
- Every number is measured, dated and tied to a git commit.

## 8. Safety and legal

Prototype only. Drones stay in simulation. Public or synthetic data only. Human in the loop. Civilian use only.
Map data keeps its own licences (ODbL, dl-de/by-2-0, Copernicus).

## 9. First two weeks

```text
  WEEK 1                                   WEEK 2
  [ ] clone repo, run lantern_status.py    [ ] write conops.md user stories
  [ ] FEMA SID + start IS-100.c            [ ] write REQ-001..010 targets
  [ ] dev container with ROS 2 Humble      [ ] finish IS-100.c + IS-700.b
  [ ] make test_sector_id_pattern pass     [ ] defend ADR-0001, mark it Accepted
```
