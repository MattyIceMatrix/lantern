# Concept of Operations (ConOps)

```text
   +-----------------------------------------------------------+
   |  WHO uses it  |  WHERE  |  WHEN the network is gone  | WHY |
   +-----------------------------------------------------------+
```

> **Status:** TEMPLATE. Matthew fills this in during Op 0. The bracketed prompts say what goes where.

## 1. Purpose

LANTERN helps a flood rescue team search an area, track what has been searched, and send clear reports
**while the mobile network is down**. It supports human decisions; it does not replace them.

## 2. Current situation (the problem)

[Describe the July 2021 Ahr flood: what failed (power, mobile network, roads), what rescuers had to do
without information, and why a cloud-based tool would not have helped.]

## 3. Users and roles

| Role (ICS term) | Who in Germany | What they need from LANTERN |
| --- | --- | --- |
| Incident Commander | Einsatzleiter | [one-line need] |
| Operations Section Chief | Leiter Einsatzabschnitt | [one-line need] |
| Search team lead | Gruppenführer / Truppführer | [one-line need] |
| Rover operator | (team member) | [one-line need] |
| Coordination centre | Führungsstab / Lagezentrum | [one-line need] |

## 4. Operational scenario

```text
 T+0h    heavy rain, river rising          LANTERN: map pack already loaded, batteries charged
 T+2h    mobile network fails              LANTERN: switches to offline mode (it never needed it)
 T+3h    team arrives at staging area      LANTERN: planner proposes sectors from HQ100/HQextrem zones
 T+4h    search begins                     LANTERN: Scout sweeps, detects, logs sightings
 T+6h    team lead dictates notes          LANTERN: Field Brain writes SITREPs offline
 T+12h   satellite link at command post    LANTERN: Sync uploads, coordination centre sees sectors
```

## 5. User stories

- As a **search team lead**, I want [goal] so that [reason].
- As an **Incident Commander**, I want [goal] so that [reason].
- As a **coordination centre officer**, I want [goal] so that [reason].

## 6. Constraints

- No network for up to [N] hours.
- One Jetson Orin Nano (8 GB) per kit; battery runtime at least [N] hours.
- Operators are wet, cold, wearing gloves: [UI constraints].
- Survivor data is personal data under GDPR.

## 7. Out of scope

- Autonomous entry into moving water.
- Any real deployment without adoption and testing by a rescue organisation.
- Military or law-enforcement use.
