#!/usr/bin/env bash
# =====================================================================
#   _ __ ___   __ _ _ __    _ __   __ _  ___| | __
#  | '_ ` _ \ / _` | '_ \  | '_ \ / _` |/ __| |/ /
#  | | | | | | (_| | |_) | | |_) | (_| | (__|   <
#  |_| |_| |_|\__,_| .__/  | .__/ \__,_|\___|_|\_\
#                  |_|     |_|          LANTERN Track A
# =====================================================================
# Builds the offline map pack for the area in config/area.yaml.
# STARTER SCRIPT: each step is a TODO for Op 1. Fill them in one at a time
# and make every step safe to run twice.

set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
CACHE="$ROOT/mappack/cache"
mkdir -p "$CACHE"

say() { printf '\n  [*] %s\n' "$1"; }

say "Step 0: read the bounding box from config/area.yaml"
# TODO: read area.bbox into WEST SOUTH EAST NORTH (hint: python -c with yaml, or yq)

say "Step 1: OSM extract"
# TODO: download rheinland-pfalz-latest.osm.pbf from Geofabrik into $CACHE (skip if present)
# TODO: osmium extract -b "$WEST,$SOUTH,$EAST,$NORTH" ... -o "$OUT/area.osm.pbf"

say "Step 2: vector basemap"
# TODO: pmtiles extract <protomaps build url> "$OUT/ahr.pmtiles" --bbox=...

say "Step 3: terrain (DGM1)"
# TODO: download the DGM1 tiles that intersect the bbox
# TODO: gdalbuildvrt + gdalwarp -t_srs EPSG:25832 -> "$OUT/dgm1.tif"
# TODO: gdaldem hillshade and slope

say "Step 4: flood hazard zones"
# TODO: ogr2ogr from the RLP flood hazard service, one layer per scenario: HQ10, HQ100, HQextrem

say "Step 5: 2021 ground truth"
# TODO: ogr2ogr the EMSR517 flood delineation for the Ahr AOIs -> ground_truth_2021.gpkg

say "Step 6: routing"
# TODO: valhalla_build_config + valhalla_build_tiles from area.osm.pbf

say "Step 7: manifest"
# TODO: write MANIFEST.json: every file, its source URL, download date, licence, sha256

echo
echo "  The lantern needs fuel: finish the TODOs above, then run mappack/checks.py"
