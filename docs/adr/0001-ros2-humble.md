# ADR-0001: Use ROS 2 Humble on Ubuntu 22.04

```text
   [ PROPOSED ] --> [ ACCEPTED ] --> [ SUPERSEDED by ADR-xxxx ]
        ^ you are here until Matthew defends it at the Op 0 gate
```

- **Status:** Proposed
- **Date:** [fill in]
- **Deciders:** Matthew (owner), Claude (reviewer)

## Context

Scout needs a robotics middleware for sensors, navigation (Nav2) and SLAM (slam_toolbox) that runs the same
way in Gazebo and on the Jetson Orin Nano. NVIDIA's JetPack 6 is based on Ubuntu 22.04.

## Decision

Use ROS 2 Humble Hawksbill (LTS, supported until May 2027) on Ubuntu 22.04, in a Docker dev container.

## Consequences

- Good: long-term support during the whole project; large Nav2 / slam_toolbox community; matches JetPack 6.
- Good: same launch files in simulation and on hardware.
- Bad: Humble ends support in 2027, so a migration ADR will be needed after the project.
- Bad: Docker on the Jetson needs NVIDIA container runtime setup.

## Alternatives considered

| Option | Why not (for now) |
| --- | --- |
| ROS 2 Jazzy (Ubuntu 24.04) | Does not match JetPack 6's Ubuntu 22.04 without extra work |
| ROS 1 Noetic | End of life (May 2025) |
| No middleware, plain Python | Would rebuild navigation and SLAM from scratch |
