# Field Kit Runbook

```text
   BEFORE  ---->  DEPLOY  ---->  OPERATE  ---->  RECOVER  ---->  AFTER
   charge,        power on,      search,         stop, save,     sync,
   load pack,     self-test,     log, report     pack up         debrief
   check e-stop   e-stop test
```

For exercises only. LANTERN is a prototype and is not used in real emergencies.

## 1. Before (the day before)

```text
  [ ] Batteries charged in a LiPo bag, never unattended
  [ ] Map pack version matches config/area.yaml (check MANIFEST.json date)
  [ ] `make check` passes on the deployed commit; commit hash written in the exercise log
  [ ] Guardian policies.yaml version written in the exercise log
  [ ] Spare fuses, tape, cable ties, microfibre cloth for the camera
```

## 2. Deploy (on site)

```text
  [ ] Power on Jetson; wait for the status banner
  [ ] Self-test: camera, lidar, motors, storage free space
  [ ] E-STOP TEST: press, confirm motors stop within the REQ-012 limit, log it
  [ ] Set the speed limit for the site
  [ ] Confirm "offline" indicator: no network needed
```

## 3. Operate

| Situation | Action |
| --- | --- |
| Guardian returns ASK_HUMAN | Team lead reviews on screen, approves or denies; it is logged automatically |
| Detector confidence low in fog or rain | Slow down; human checks the camera feed |
| Rover stuck | E-stop, recover by hand, log the location |
| Battery under 20% | Return to staging area |

## 4. Recover (something went wrong)

| Symptom | First check | Then |
| --- | --- | --- |
| No camera image | cable, `ros2 topic list` | restart camera node |
| Rover drifts on map | lidar lens dirty, wheel slip | relocalise from a known point |
| Field Brain slow | thermal throttling (`tegrastats`) | shade the unit, reduce model size |
| Audit check fails | do **not** edit the log | stop, copy the store, open a security issue |

## 5. After

```text
  [ ] Sync when a link is available; confirm outbox is empty
  [ ] Export exercise log and video
  [ ] Write the AAR (missions/README.md template) within 48 hours
  [ ] File issues for every failure, labelled with the component
```
