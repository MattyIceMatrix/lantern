# Governance

```text
              +----------------------+
              |   MAINTAINER         |   final say on scope, merges, releases
              |   (Matthew Moore)    |
              +----------+-----------+
                         |
          +--------------+---------------+
          |                              |
 +--------+---------+          +---------+---------+
 | REVIEWERS        |          | DOMAIN ADVISORS   |
 | code + design    |          | rescue, GIS, law  |
 +------------------+          +-------------------+
                         |
              +----------+-----------+
              |  CONTRIBUTORS        |
              +----------------------+
```

## Roles

| Role | Who | Can |
| --- | --- | --- |
| Maintainer | @MattyIceMatrix | merge, release, set roadmap, accept ADRs |
| Reviewer | invited after 3 merged PRs | approve PRs in their area (see CODEOWNERS) |
| Domain advisor | rescue professionals, GIS and legal experts who volunteer | review doctrine, safety case, DPIA |
| Contributor | anyone | open issues and PRs |

## Decisions

- **Day-to-day:** the PR review process.
- **Architecture:** an ADR, open for comment at least 5 days, accepted by the maintainer.
- **Safety-relevant** (Guardian rules, safety case, anything that touches the rover's motion): needs the
  maintainer **and** one reviewer, plus a recorded check against `docs/safety-case.md`.

## Phase gates

Each operation in `missions/` ends with a gate review: a written record in `missions/aar/` stating which
gate items passed, with links to evidence. A gate is passed only when every item is checked.
