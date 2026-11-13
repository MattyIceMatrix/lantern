# Map Pack (Track A)

```text
     OSM .pbf ----osmium extract----> area.osm.pbf ----> Valhalla routing tiles
         |                                 |
         |                                 +----------> pmtiles (vector basemap)
     DGM1 terrain ----gdalbuildvrt / gdalwarp----> area_dgm1.tif ---> hillshade, slope
     HQ10/HQ100/HQextrem (WMS/WFS) ----ogr2ogr----> flood_zones.gpkg
     EMSR517 delineation ----ogr2ogr----> ground_truth_2021.gpkg

                     everything above ===> mappack/out/<area>/   (copied to the Jetson)
```

One command builds an offline map pack for the area in `config/area.yaml`.
After that, the kit never needs the internet for maps.

## Layers

| Layer | Source | Licence | Tool |
| --- | --- | --- | --- |
| Roads, buildings, waterways | OpenStreetMap via Geofabrik | ODbL | osmium |
| Basemap tiles | Protomaps (`pmtiles extract`) | ODbL (OSM data) | pmtiles CLI |
| Terrain 1 m | LVermGeo RLP DGM1 | dl-de/by-2-0 | GDAL |
| Flood hazard zones | RLP Hochwassergefahrenkarten | see provider terms | GDAL/OGR |
| 2021 flood extent | Copernicus EMS EMSR517 | Copernicus licence | GDAL/OGR |
| Routing graph | built from OSM | ODbL | Valhalla |

## Your tasks (Op 1)

```text
  [ ] build.sh: implement each TODO step; it must be safe to re-run
  [ ] checks.py: write tests that the pack covers the bbox and every layer is present
  [ ] record the download date of every source in out/<area>/MANIFEST.json
  [ ] keep attribution text for every layer (it ships with the pack)
```

Large downloads go in `mappack/cache/` (git-ignored). Never commit raw data.
