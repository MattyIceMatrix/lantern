# Data Protection Impact Assessment (GDPR Art. 35)

```text
     ____
    |    |   Survivor data is personal data, and in a disaster it can include
    | [] |   health data (special category, Art. 9). Treat it like gold.
    |____|
```

> **Status:** TEMPLATE. Complete before Op 4 gate.

## 1. Processing description

| Data | Example | Category | Where stored | How long |
| --- | --- | --- | --- | --- |
| Sightings | location, time, confidence | personal (location of a person) | device SQLite | [ ] |
| SITREPs | "2 people, 1 injured" | may contain health data | device + cloud (pseudonymised) | [ ] |
| Images | rover camera frames | personal (faces) | device only, [retention] | [ ] |
| Voice notes | team lead dictation | personal (voice of the rescuer) | device only, deleted after transcription | [ ] |

## 2. Necessity and proportionality

[Why each data item is needed for the rescue purpose; what is NOT collected.]

## 3. Risks to people

| Risk | Likelihood | Severity | Measure |
| --- | --- | --- | --- |
| Faces of survivors leaked | [ ] | high | No face storage; blur before any export |
| Location of empty homes leaked (looting) | [ ] | high | Coarse locations in cloud; access control |
| Health details over-shared | [ ] | high | Pseudonymise; minimum fields |

## 4. Measures

- Data minimisation in the schema (no free-text names by default).
- Pseudonymisation on the device before sync (REQ-011).
- Encryption at rest on the device and in the cloud.
- Retention limits enforced in code, with tests.
- During development: public or synthetic data only.
