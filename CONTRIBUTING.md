# Contributing to LANTERN

```text
     ___________________________________________
    |  issue  -->  branch  -->  PR  -->  review |
    |    |                        |        |    |
    |  REQ-xxx                  CI green  merge |
    |___________________________________________|
```

Thanks for helping. LANTERN is a learning project with engineering discipline: every change traces to a
requirement, passes CI, and is reviewed.

## Ground rules

1. **Open an issue first** for anything bigger than a typo. Use the templates.
2. **Link a requirement.** PRs that change behaviour reference a `REQ-xxx` from `docs/requirements.md`,
   or add a new one.
3. **Tests come with code.** New behaviour needs a test; bug fixes need a test that failed before the fix.
4. **No real personal data.** Public or synthetic data only. Never commit images of real people from a real incident.
5. **No secrets.** No API keys, tokens or `.env` files. CI scans for them.
6. **Civilian use only.** Contributions adding targeting, surveillance or weaponisation features will be closed.

## Workflow

```bash
make setup        # create venv, install dev deps, install pre-commit hooks
make check        # lint + type check + tests: what CI runs
```

Branch names: `op<N>/<short-topic>`, for example `op1/search-patterns`.

Commit messages follow [Conventional Commits](https://www.conventionalcommits.org/):

```text
feat(scout): add parallel-track search pattern (REQ-0xx)
fix(guardian): deny unknown tools by default (REQ-007)
docs(conops): add team lead user story
```

## Definition of done

```text
  [ ] linked issue and REQ-xxx
  [ ] tests added or updated; `make check` passes
  [ ] docs/traceability.md updated if a requirement's status changed
  [ ] safety-case.md / threat-model.md updated if a new hazard or threat appears
  [ ] CHANGELOG.md entry under "Unreleased"
```

## Architecture decisions

Significant choices (a new framework, a changed metric target, a new data source) need an ADR in
`docs/adr/` using `docs/adr/template.md`.
