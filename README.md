```text
                                   )
                                  ( )
                                 .-^-.
                                /_____\
                                |  |  |        _      ___   _  _  _____  ___  ___  _  _
                                | (*) |       | |    / _ \ | \| ||_   _|| __|| _ \| \| |
                                |  |  |       | |__ / /_\ \| .` |  | |  | _| |   /| .` |
                                |_____|       |____/_/   \_\_|\_|  |_|  |___||_|_\|_|\_|
                                \_____/
                                  | |         Local AI for Navigation, Triage and
                       ~~~~~~~~~~~| |~~~~~~~~ Emergency Reporting with No network
                     ~~~~~~~~~~~~~| |~~~~~~~~~~~~~~
                   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~   "When the towers go dark,
                                                             the lantern stays lit."
```

# LANTERN

**An offline edge-AI kit that helps flood rescue teams find people, map damage and file reports when the phone network is gone.**

> On the night of 14–15 July 2021 the Ahr river in Rhineland-Palatinate flooded. 134 people died, and the mobile
> network collapsed as exchanges were destroyed, so many residents could not call for help.
> Cloud AI is useless in that moment. Only AI that runs **on the device** works.
> LANTERN is built for that moment.

This repo is the full buildout of LANTERN: the plan, the mission briefings, the engineering documents,
the doctrine data, the map-pack pipeline, and the starter code for every part of the system.

**Status:** Phase 0, Op Groundwork. Prototype and portfolio project. **Not** for use in real emergencies.

---

## The kit at a glance

```text
 +----------------------------------------------------------------------------------+
 |  ON THE DEVICE  (works with NO network)          Jetson Orin Nano, 8 GB, 67 TOPS |
 |                                                                                  |
 |   +----------------+       +------------------+       +------------------+       |
 |   |     SCOUT      | <---> |  MISSION AGENTS  | <---> |   FIELD BRAIN    |       |
 |   | camera + lidar |       | assign sectors   |       | offline voice    |       |
 |   | detect, fuse,  |       | track survivors  |       | local LLM report |       |
 |   | map, search    |       | draft handovers  |       | RAG + translate  |       |
 |   +-------+--------+       +--------+---------+       +---------+--------+       |
 |           |                         |                           |                |
 |           v                         v                           v                |
 |   +------------------------------------------------------------------------+     |
 |   |  GUARDIAN  -  policy check on every action, survivor-data protection,  |     |
 |   |               audit log, red-teamed                                    |     |
 |   +-----------------------------------+------------------------------------+     |
 |                                       ^                                          |
 |                                       v                                          |
 |                          +------------------------+                              |
 |                          |   RESCUE TEAM LEAD     |   approves risky moves       |
 |                          +------------------------+                              |
 +---------------------------------------+------------------------------------------+
                                         :
                                         :  store-and-forward, ONLY when a link returns
                                         v
                          +------------------------------+
                          |  CLOUD (AWS or Azure)        |
                          |  lakehouse, dashboards,      |
                          |  retraining loop             |
                          +------------------------------+
```

| Part | Folder | What it does |
| --- | --- | --- |
| Scout | [`scout/`](scout/) | Ground robot (drone in simulation only): perception, sensor fusion, SLAM, search patterns |
| Field Brain | [`brain/`](brain/) | Offline speech, a small LLM fine-tuned to write situation reports, RAG over procedures, translation |
| Mission agents | [`agents/`](agents/) | Sector planning, survivor tracking, handover reports, with human approval gates |
| Guardian | [`guardian/`](guardian/) | Policy engine, GDPR data protection, audit log, red-team suite |
| Sync | [`sync/`](sync/) | Store-and-forward to the cloud lakehouse and dashboards |
| Mission data model | [`lantern_model/`](lantern_model/) | The shared typed objects every part reads and writes |
| Map pack | [`mappack/`](mappack/) | Offline maps of one area: OSM, tiles, terrain, flood zones, routing, 2021 ground truth |
| Doctrine | [`doctrine/`](doctrine/) | ICS/NIMS roles, NFPA levels, marking systems and THW terms, as data |

---

## The campaign

```text
   OP 0          OP 1           OP 2            OP 3            OP 4           OP 5            OP 6         OP 7
 GROUNDWORK -> PATHFINDER -> NIGHT VISION -> RADIO SILENCE -> GATEKEEPER -> BOOTS ON GROUND -> RELAY ---> DEBRIEF
  wk 1-3       mo 1-3         mo 3-5          mo 5-7          mo 7-9         mo 9-11          mo 11-13     mo 13-14
    |            |              |               |               |              |                |            |
  repo,       Scout in       detector,       offline        agents +      real rover,      sync +       ship it:
  ROS 2,      Gazebo,        INT8 on         voice + LLM    Guardian +    dry field        cloud        video,
  ConOps      SLAM map       Jetson          reports        red team      test             dashboard    paper, talk
    <>           <>             <>              <>              <>             <>               <>           <>
   GATE         GATE           GATE            GATE            GATE           GATE             GATE        GATE
```

Every phase is an **operation** with a briefing, a build, a gate you must pass, and an after-action review.
Start here: [`missions/README.md`](missions/README.md).

---

## How this project is built

```text
   +----------------------+        +----------------------+        +----------------------+
   |  MATTHEW             |        |  CLAUDE              |        |  OUTSIDE REVIEWER    |
   |  writes every line   |        |  coach, reviewer,    |        |  from Op Night       |
   |  of code             |        |  "interviewer"       |        |  Vision onward       |
   +----------+-----------+        +----------+-----------+        +----------+-----------+
              |                               |                               |
              +---------------+---------------+---------------+---------------+
                              |                               |
                        defend-it check                 formal gate review
                        at every gate                   against requirements
```

- **Matthew writes the code.** The starter files contain TODOs and failing tests, like a course starter kit.
  Claude briefs, explains, reviews and debugs alongside, and does not hand over finished modules.
- **Udacity first, LANTERN second.** Each matching Udacity project is done solo as the training rep,
  then the skill is carried into LANTERN.
- **Honest numbers.** Every result is measured on real hardware and reported with its failures.

---

## Repo map

```text
lantern/
|-- README.md                 <- you are here
|-- missions/                 <- 8 operation briefings + campaign map + AAR template
|-- docs/
|   |-- PLAN.md               <- the full project plan
|   |-- training-layers.md    <- the 7-layer training stack
|   |-- conops.md             <- Concept of Operations (template)
|   |-- requirements.md       <- numbered requirements (template + first examples)
|   |-- traceability.md       <- requirement -> design -> test -> result
|   |-- safety-case.md        <- FMEA hazard analysis
|   |-- test-plan.md          <- datasets, metrics, thresholds
|   |-- dpia.md               <- GDPR data protection impact assessment
|   |-- threat-model.md       <- STRIDE threat model
|   |-- glossary.md           <- EN/DE terms: ICS, NIMS, THW, HQ100 ...
|   |-- adr/                  <- architecture decision records
|   `-- cards/                <- model card + data card templates
|-- config/area.yaml          <- which area the map pack covers
|-- mappack/                  <- Track A: offline map build pipeline
|-- doctrine/                 <- Track B: rescue doctrine as data
|-- lantern_model/            <- mission data model (schemas)
|-- tests/                    <- starter tests (xfail until you implement)
|-- scout/  brain/  agents/  guardian/  sync/
|-- scripts/lantern_status.py <- prints the banner + campaign progress
|-- art/                      <- the ASCII art collection
`-- .github/workflows/ci.yml  <- tests on every push
```

---

## Quick start

```bash
python scripts/lantern_status.py      # banner + where the campaign stands
pip install -e ".[dev]"
pytest                                # mission tests start as expected failures (xfail)
```

---

## Safety and ethics

```text
   /!\  PROTOTYPE ONLY  /!\
   - Never used in a real emergency unless a rescue organisation (THW, fire service) adopts and tests it.
   - Drones stay in simulation; the real hardware is a ground rover.
   - Survivor data is personal data under GDPR: public or synthetic datasets only, no stored faces.
   - Human in the loop: the robot proposes, a person approves anything risky.
   - Civilian purpose only. No targeting or weaponisation features, ever.
```

## Licence

Code: [Apache-2.0](LICENSE). Map data keeps its own licences: OpenStreetMap (ODbL),
Rhineland-Palatinate geodata (Datenlizenz Deutschland, Namensnennung 2.0, "©GeoBasis-DE / LVermGeoRP"),
Copernicus EMS (Copernicus licence).
