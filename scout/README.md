# Scout

```text
          ,-----------.
         /  _______    \__         SCOUT: the rover
        |  | LANTERN|     |===]    eyes: RGB camera + 2D lidar
         \__|_______|_____/        brain: Jetson Orin Nano
          (O)        (O)           job: map, search, spot
```

| Folder (to create) | Op | What goes in it |
| --- | --- | --- |
| `sim/` | 1 | Gazebo world of a flooded street, rover URDF, launch files |
| `nav/` | 1 | Nav2 and slam_toolbox configs |
| `search_patterns.py` | 1 | parallel-track and expanding-square waypoint generators |
| `detector/` | 2 | training config, export scripts, TensorRT engine builder |
| `bringup/` | 5 | real-hardware launch files, e-stop monitor |

## Starter task (Op 1)

Write `search_patterns.py` with one function:

```python
def parallel_track(boundary: dict, spacing_m: float) -> list[tuple[float, float]]:
    """Return waypoints that sweep the polygon in parallel lanes spacing_m apart."""
```

Write its tests first: the waypoints must stay inside the polygon and cover at least 95% of it.
