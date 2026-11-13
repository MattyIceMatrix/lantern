# Field Brain

```text
      (( voice ))        +------------+      +-----------+      +-----------+
     ((  note  ))  --->  |  ASR       | ---> |  LLM 3B   | ---> |  SITREP   |
                         |  offline   |      |  LoRA +   |      |  (valid   |
                         +------------+      |  GRPO     |      |   JSON)   |
                                             +-----+-----+      +-----------+
                                                   ^
                                       +-----------+-----------+
                                       |  RAG over doctrine/   |
                                       |  (always cites source)|
                                       +-----------------------+
```

| File (to create) | Op | What it does |
| --- | --- | --- |
| `asr.py` | 3 | offline speech-to-text |
| `sitrep.py` | 3 | prompt + constrained JSON output validated by `Sitrep` |
| `finetune/` | 3 | LoRA config, synthetic dataset builder, GRPO reward |
| `rag.py` | 3 | index doctrine/ files, retrieve, answer with citations |
| `translate.py` | 3 | offline translation for the area's most common languages |

## Hard rule

No network calls anywhere in this folder. A test (REQ-001) blocks sockets and runs the whole pipeline.
