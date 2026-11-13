# OP 1: PATHFINDER

```text
                                 PATHFINDER
                     ___________________________________
                    |  .   .   .   .   .   .   .   .   |      sim world: flooded street
                    |    ____        ~~~~~~~      __   |
                    |   |    |  ~~~~~~~~~~~~~~~  |  |  |
                    |   |____|  ~~~~ [@>] ~~~~~  |__|  |      [@>] = Scout rover
                    |           ~~~~~~~~~~~~~~~        |
                    |   .   .   .  ~~~~~~~  .   .   .  |
                    |___________________________________|

           ,-------.
          /  ___    \       lidar sweep:   \ | /
         |  [___]    |                   -- @ --
          \_________/                      / | \
           O       O
```

**Duration:** months 1–3 · **Rank on completion:** NAVIGATOR

## Situation

After a flash flood, streets are blocked by debris, cars and collapsed walls. GPS maps are out of date by the
hour. A rescue team needs a fresh map of what is passable **now**.

## Mission

Put Scout in a Gazebo simulation of a flooded street, make it build a map with SLAM, plan a route around
obstacles, and run a systematic search pattern over a sector.

## Recon (training reps)

```text
  [ ] Udacity robotics projects in the cluster map (localisation, SLAM, path planning) - done solo
  [ ] ROS 2 Nav2 "Getting started" tutorial
  [ ] slam_toolbox online async demo
  [ ] Read: IAMSAR search patterns (expanding square, parallel track) - concept only
```

## Build

```text
  STEP 1  World           -> a Gazebo world with water planes, debris boxes, a few buildings
  STEP 2  Robot           -> a diff-drive rover URDF with lidar + RGB camera
  STEP 3  Map             -> slam_toolbox builds an occupancy grid while you teleop
  STEP 4  Navigate        -> Nav2 goes from A to B around debris
  STEP 5  Search          -> scout/search_patterns.py: generate parallel-track waypoints for a sector polygon
  STEP 6  Model link      -> each finished sweep sets Sector.state = CLEARED in the mission model
```

```text
   parallel-track search over a sector              expanding square from a last-known point
   +--------------------------------+                    +---------+
   | >>>>>>>>>>>>>>>>>>>>>>>>>>>>v  |                    | +-----+ |
   | v<<<<<<<<<<<<<<<<<<<<<<<<<<<   |                    | | +-+ | |
   | >>>>>>>>>>>>>>>>>>>>>>>>>>>>v  |                    | | |X| | |
   | v<<<<<<<<<<<<<<<<<<<<<<<<<<<   |                    | | +-+ | |
   | >>>>>>>>>>>>>>>>>>>>>>>>>>>>   |                    | +-----+ |
   +--------------------------------+                    +---------+
```

## Gate: PATHFINDER

```text
  +--------------------------------------------------------------+
  |  [ ] Map of the sim world saved and reloaded                  |
  |  [ ] 10 Nav2 runs A->B, success rate measured and logged      |
  |  [ ] Search pattern covers >= 95% of a test sector (measured) |
  |  [ ] Unit tests for search_patterns.py pass in CI             |
  |  [ ] REQ links updated in docs/traceability.md                |
  +--------------------------------------------------------------+
```

## Defend it

1. What is the difference between localisation and mapping, and why does SLAM need both at once?
2. Why does track spacing in a search pattern depend on the sensor's detection range?
3. What does your rover do when the planner cannot find a path? Is that safe?
4. Show one failed run and explain what caused it.
