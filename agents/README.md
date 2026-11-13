# Mission Agents

```text
     [ sector planner ]   [ survivor tracker ]   [ handover writer ]
             \                    |                    /
              \___________________|___________________/
                                  |
                           every tool call
                                  v
                          [  G U A R D I A N  ]
```

| Agent | Op | Tools it may call |
| --- | --- | --- |
| Sector planner | 4 | `propose_sectors`, `assign_sector` |
| Survivor tracker | 4 | `log_sighting`, `merge_sightings` |
| Handover writer | 4 | `draft_handover` |

## Design rules

- Agents only **propose**. Tools that change the world go through the Guardian.
- Tools are small and typed (inputs and outputs are `lantern_model` objects).
- No agent can call another agent's tools.
