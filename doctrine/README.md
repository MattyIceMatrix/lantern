# Doctrine as Data (Track B)

```text
     ____________          _______________          _____________
    | FEMA / NIMS|        | NFPA 1006     |        | INSARAG /   |
    | ICS roles  |        | rescue levels |        | FEMA marks  |
    |____________|        |_______________|        |_____________|
          \                      |                       /
           \_____________________|______________________/
                                 |
                      doctrine/*.yaml  (this folder)
                                 |
              +------------------+------------------+
              |                  |                  |
         RAG index          Guardian rules     SITREP schema
       (Field Brain)       (who may approve)   (field names)
```

Rescue doctrine is turned into **data files** so the code can use it and the RAG system can cite it.

## Files

| File | What it holds | Used by |
| --- | --- | --- |
| `ics_roles.yaml` | ICS roles, German equivalents, what they may approve | Guardian, agents |
| `nfpa1006_levels.yaml` | Awareness / Operations / Technician, plain-language scope | Guardian (who may do what) |
| `markings.yaml` | Search marking systems, as structured fields | Scout logging, SITREP |
| `thw_terms.yaml` | THW and German civil-protection terms | translation, UI labels |

## Rules

- Every entry has a `source:` field. No source, no entry.
- These are **summaries for software**, not training material. They do not qualify anyone for rescue work.
- Verify each entry against the official document before Op 3 (RAG) uses it, and record the check date.
