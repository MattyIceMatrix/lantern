# Guardian

```text
                 _______________
                |  G U A R D    |
                |    _____      |       ALLOW      -> run it, log it
                |   ( o_o )     |       DENY       -> explain why, log it
                |   /|___|\     |       ASK_HUMAN  -> wait for a named role to approve, log it
                |____/   \______|
```

| File (to create) | Op | What it does |
| --- | --- | --- |
| `policies.yaml` | 4 | the rules, as data (starter version included) |
| `engine.py` | 4 | evaluate a tool call against the rules -> ALLOW / DENY / ASK_HUMAN |
| `privacy.py` | 4 | pseudonymise personal data before it leaves the device |
| `audit.py` | 4 | append-only, hash-chained decision log |
| `redteam/` | 4 | 30+ attack cases with expected outcomes |

Write the threat model (`docs/threat-model.md`) **before** the engine.
