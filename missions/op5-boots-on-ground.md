# OP 5: BOOTS ON GROUND

```text
                                    BOOTS ON GROUND
        ______                                                       ______
       |      |      ,-----------.                                  | HQ   |
       | TENT |     /  _______    \__                               | TENT |
       |______|    |  | LANTERN|     |===]    ---- 25 m ---->       |______|
                    \__|_______|_____/
                     (O)       (O)       real rover, real grass, real mud
       ...............................................................
       :  dry field exercise: tape "flood line", cardboard "debris",  :
       :  mannequins as "survivors", a stopwatch and a clipboard      :
       :..............................................................:
```

**Duration:** months 9–11 · **Rank on completion:** FIELD OPERATOR

## Situation

Simulations lie politely. Real wheels slip, real cameras get glare, real batteries die. This operation
moves from Gazebo to hardware, in a safe, dry, controlled field.

## Mission

Build the physical rover with the Jetson, run a scripted field exercise against the test plan, and record
honest results.

## Recon (training reps)

```text
  [ ] EU A1/A3 open-category drone certificate (LBA, online)  - for later drone work and credibility
  [ ] FEMA IS-230.d   Fundamentals of Emergency Management
  [ ] Read NFPA 1006 awareness-level duties for water rescue (what a non-swimmer helper may do)
  [ ] Battery + charging safety checklist for LiPo packs
```

## Build

```text
  STEP 1  Hardware       -> chassis, motors, Jetson, camera, lidar, e-stop button that cuts motor power
  STEP 2  Bring-up       -> same ROS 2 launch files as in sim, with real drivers
  STEP 3  Safety         -> pre-run checklist, speed limit, e-stop test before every run
  STEP 4  Scenario       -> a written exercise plan: 4 sectors, 3 "survivors", 1 blocked route
  STEP 5  Run it         -> 5 runs, everything logged, video recorded
  STEP 6  Compare        -> sim results vs field results, side by side
```

```text
       E-STOP  ____
              |STOP|   <- a physical red button. Tested before EVERY run.
              |____|      No button, no run. No exceptions.
```

## Gate: BOOTS ON GROUND

```text
  +--------------------------------------------------------------+
  |  [ ] E-stop test logged before every run                      |
  |  [ ] 5 field runs against the written scenario                |
  |  [ ] Detection recall and coverage measured in the field      |
  |  [ ] Sim-vs-field gap table with explanations                 |
  |  [ ] TRL 4 claim written up with evidence                     |
  +--------------------------------------------------------------+
```

## Defend it

1. What was the biggest difference between simulation and the field, and why?
2. Walk through your safety checklist. What would make you cancel a run?
3. What does TRL 4 mean, and why is your project not TRL 6?
4. Why does this project use a ground rover for real tests and keep drones in simulation?
