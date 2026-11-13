# Release Process

```text
   feature branches --> main (CI green) --> release branch --> tag vX.Y.Z --> GitHub Release
                                                 |                               |
                                           changelog, SBOM,               notes, SBOM, map-data
                                           traceability check             licences, checksums
```

## Versioning

[Semantic Versioning](https://semver.org/): `MAJOR.MINOR.PATCH`.
Before 1.0.0, each passed operation gate bumps MINOR (see `roadmap.md`).

## Steps

```text
  1. All gate items for the operation are checked in missions/aar/opN.md
  2. CI and security workflows green on main
  3. Move CHANGELOG "Unreleased" entries under the new version and date
  4. Bump version in pyproject.toml and CITATION.cff
  5. Update docs/traceability.md results with dates and commit
  6. Tag:  git tag -s vX.Y.Z -m "vX.Y.Z: <op name>"   (signed tag)
  7. Create the GitHub Release; attach SBOM, eval results, checksums
  8. Announce in the README status line and (optionally) LinkedIn
```

## Never in a release

- Secrets, `.env` files, keys
- Raw map data or datasets (they are built locally from sources with their own licences)
- Real personal data
