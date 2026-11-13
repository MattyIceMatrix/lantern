# Architecture

Described with the [C4 model](https://c4model.com/): context, containers, then quality attributes.

## Level 1: System context

```text
                         +--------------------+
                         |  Search team lead  |
                         +---------+----------+
                                   | voice notes, approvals
                                   v
  +---------------+      +--------------------+      +------------------------+
  | Flood area    | ---> |      LANTERN       | ---> | Coordination centre    |
  | (sensed by    |      |   field kit        |      | (via cloud, only when  |
  |  rover)       |      | (fully offline)    |      |  a link exists)        |
  +---------------+      +---------+----------+      +------------------------+
                                   ^
                                   | map pack + doctrine, loaded BEFORE deployment
                         +---------+----------+
                         | Open geodata,      |
                         | rescue doctrine    |
                         +--------------------+
```

## Level 2: Containers (on the Jetson unless marked)

```text
  +---------------------------------------------------------------------------------+
  | Jetson Orin Nano                                                                |
  |                                                                                 |
  |  [ Scout ROS 2 nodes ]   [ Field Brain svc ]   [ Agents svc ]   [ Guardian svc ]|
  |   nav2, slam, detector    asr, llm, rag         planner, tracker  policy, audit |
  |          \                     |                     |               /          |
  |           \____________________|_____________________|______________/           |
  |                                |                                                |
  |                     [ Mission store: SQLite ]  <-- lantern_model schemas         |
  |                                |                                                |
  |                         [ Sync outbox ]                                         |
  +--------------------------------+------------------------------------------------+
                                   :  HTTPS, signed batches, when a link exists
  +--------------------------------v------------------------------------------------+
  | Cloud:  [ Ingest API ] -> [ Lakehouse raw/clean/mission ] -> [ Dashboard ]       |
  +---------------------------------------------------------------------------------+
```

## Key interfaces

| From | To | How | Contract |
| --- | --- | --- | --- |
| Scout | Mission store | ROS 2 topic -> bridge node | `Sighting`, `Sector` |
| Field Brain | Mission store | local function call | `Sitrep` (schema-validated) |
| Agents | Guardian | in-process call, **mandatory** | tool call -> ALLOW / DENY / ASK_HUMAN |
| Sync | Cloud | HTTPS, resumable | signed, idempotent record batches |

## Quality attributes and targets

| Attribute | Target | How we know |
| --- | --- | --- |
| Availability (offline) | 100% of mission functions without network | REQ-001 airplane-mode test |
| Battery runtime | >= [N] h per kit | field log, Op 5 |
| Latency: voice note to SITREP | <= [N] s on Jetson | eval, Op 3 |
| Detection throughput | >= [N] fps INT8 | bench, Op 2 |
| Integrity | every change in the audit log is tamper-evident | REQ-009 |
| Privacy | no image or name leaves the device | REQ-011 |
| Recoverability | power loss mid-mission loses <= 1 record | Op 5 test |

## Deployment views

```text
  DEV:    laptop -> Docker dev container -> Gazebo sim
  FIELD:  Jetson (JetPack 6) -> systemd services -> rover hardware
  CLOUD:  container on AWS or Azure free tier -> managed storage -> dashboard
```
