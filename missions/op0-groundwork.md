# OP 0: GROUNDWORK

```text
          _____                              _                      _
         / ____|                            | |                    | |
        | |  __ _ __ ___  _   _ _ __   __| |_      _____  _ __| | __
        | | |_ | '__/ _ \| | | | '_ \ / _` \ \ /\ / / _ \| '__| |/ /
        | |__| | | | (_) | |_| | | | | (_| |\ V  V / (_) | |  |   <
         \_____|_|  \___/ \__,_|_| |_|\__,_| \_/\_/ \___/|_|  |_|\_\

     ______________________________________________________________
    |  ######  |  ######  |  ######  |  ######  |  ######  |      |   lay the foundation
    |__________|__________|__________|__________|__________|______|   before the water comes
```

**Duration:** weeks 1–3 · **Rank on completion:** RECRUIT

## Situation

Every rescue organisation starts with paperwork: who does what, what the mission is, how you know it worked.
Projects that skip this stage end up as a folder of demos. This operation turns LANTERN into a
project that a reviewer can take seriously from day one.

## Mission

Stand up the repo, the toolchain and the three founding documents: the ConOps, the first ten requirements
and the first architecture decision.

## Recon (training reps)

```text
  [ ] FEMA IS-100.c   Intro to the Incident Command System        (free, online)
  [ ] FEMA IS-700.b   Intro to NIMS                               (free, online)
  [ ] Read the July 2021 Ahr flood timeline (see docs/PLAN.md sources)
  [ ] ROS 2 Humble "Beginner: CLI tools" tutorials
```

## Build

```text
  STEP 1  Repo hygiene        -> branch protection, CI green on an empty test, issue templates
  STEP 2  Dev container       -> Ubuntu 22.04 + ROS 2 Humble in Docker, one command to start
  STEP 3  ConOps              -> fill docs/conops.md: who, where, when the network dies, what they need
  STEP 4  Requirements        -> write REQ-001..REQ-010 in docs/requirements.md (each testable!)
  STEP 5  ADR-0001            -> record why ROS 2 Humble (already drafted, you defend it)
  STEP 6  Area config         -> choose the bounding box in config/area.yaml, commit it
  STEP 7  Board               -> GitHub Projects board with every Op as a milestone
```

## Gate: GROUNDWORK

```text
  +--------------------------------------------------------------+
  |  [ ] `pytest` and CI run green on main                       |
  |  [ ] `docker compose run dev ros2 doctor` passes             |
  |  [ ] ConOps has 3 user stories with a named role each        |
  |  [ ] 10 requirements, each with a verification method        |
  |  [ ] ADR-0001 accepted                                        |
  |  [ ] FEMA IS-100.c and IS-700.b certificates in docs/certs/   |
  +--------------------------------------------------------------+
```

## Defend it

1. What does a "shall" requirement need so that someone else can test it?
2. Who is the Incident Commander in a flood response, and why does LANTERN report to them instead of acting on its own?
3. Why ROS 2 Humble and not the newest ROS 2 release?
4. What happens to LANTERN's users at the exact moment the mobile network fails?

## Easter egg

When the gate passes, run `python scripts/lantern_status.py --op 0 --done` and watch the lantern light up.
