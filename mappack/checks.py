"""Checks for a built map pack (REQ-002).

        [ map pack ] --> checks.py --> PASS / FAIL with reasons

STARTER FILE: the checks are written as TODOs for Op 1.
"""

from pathlib import Path

REQUIRED_FILES = [
    "area.osm.pbf",
    "ahr.pmtiles",
    "dgm1.tif",
    "flood_zones.gpkg",
    "ground_truth_2021.gpkg",
    "MANIFEST.json",
]


def missing_files(pack_dir: Path) -> list[str]:
    """Return the required files that are not in pack_dir."""
    return [name for name in REQUIRED_FILES if not (pack_dir / name).exists()]


def check_bbox_coverage(pack_dir: Path, bbox: list[float]) -> bool:
    """TODO (Op 1): open dgm1.tif and check its extent covers bbox (after reprojecting)."""
    raise NotImplementedError


def check_flood_scenarios(pack_dir: Path) -> bool:
    """TODO (Op 1): check flood_zones.gpkg has HQ10, HQ100 and HQextrem layers, each non-empty."""
    raise NotImplementedError


if __name__ == "__main__":
    import sys

    pack = Path(sys.argv[1] if len(sys.argv) > 1 else "mappack/out/ahr-valley")
    missing = missing_files(pack)
    if missing:
        print("  [x] missing:", ", ".join(missing))
        sys.exit(1)
    print("  [ok] all files present (now implement the deeper checks)")
