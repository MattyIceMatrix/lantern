# Compliance Overview

```text
     ___________
    |  _______  |     EU AI Act . GDPR . data licences . drone rules . export
    | |  ___  | |     A map of what applies, what we do about it, and what is still open.
    | | |   | | |
    | | |___| | |     Not legal advice. Before any real deployment, get a lawyer's review.
    |_|_______|_|
```

| Area | What applies | Status | Where |
| --- | --- | --- | --- |
| EU AI Act (Reg. 2024/1689) | Research and pre-market testing are largely excluded from scope (Art. 2). A deployed system that helps prioritise emergency first response could fall under the high-risk use cases in Annex III. | Assessment to complete before any deployment talks | this file, section 1 |
| GDPR | Survivor locations, images and health details are personal (some special-category) data | DPIA template ready | `dpia.md` |
| Data licences | ODbL (OSM), dl-de/by-2-0 (RLP geodata), Copernicus licence, dataset licences | Attribution file in place | `NOTICE`, `docs/cards/` |
| Drones (EU 2019/947) | Open category A1/A3 for any real flight; this project keeps drones in simulation | Certificate planned in Op 5 | `training-layers.md` |
| Radio equipment | Only CE-marked radios and modules are used | Rule | hardware list |
| Open-source licences | Apache-2.0 outbound; dependency licences checked through the SBOM | CI produces SBOM | `.github/workflows/security.yml` |
| Accessibility | Field UI usable with gloves, in rain, at night | Design constraint | `conops.md` |

## 1. EU AI Act: working assessment

```text
   Is it placed on the market or put into service?
        |
        +-- NO (research prototype)  -->  largely out of scope; keep good practice anyway
        |
        +-- YES (adopted by an organisation)
                 |
                 +-- Does it evaluate or prioritise emergency calls or dispatch of first response?
                          |
                          +-- likely HIGH-RISK  -->  risk management system, data governance,
                                                    technical documentation, logging, human oversight,
                                                    accuracy and robustness, conformity assessment
```

LANTERN already builds several high-risk-style controls in on purpose: human oversight (Guardian ASK_HUMAN),
logging (hash-chained audit), technical documentation (this `docs/` tree), data governance (data cards, DPIA)
and accuracy reporting (model cards, test plan). That keeps the door open for a real adoption later.

## 2. Open items

- [ ] Confirm the AI Act classification with a qualified adviser before any partner pilot.
- [ ] Confirm the RLP flood-hazard data terms for redistribution inside a map pack.
- [ ] Check each training dataset's licence for publishing model weights.
