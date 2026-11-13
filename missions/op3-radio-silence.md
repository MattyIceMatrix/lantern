# OP 3: RADIO SILENCE

```text
        ((( )))                                         ___________________
       ((( o )))   "two people on the roof at          | SITREP 0217      |
        ((( )))     Bruckstrasse 12, water rising,     | LOC: Sector D-4  |
          |||       one injured, need a boat"   ---->  | PAX: 2 (1 inj.)  |
         /|||\                                         | NEED: boat       |
        /_____\     [ no signal ]  x---x---x           | PRIO: IMMEDIATE  |
                                                       |__________________|
                  RADIO SILENCE: everything runs ON the device
```

**Duration:** months 5–7 · **Rank on completion:** SIGNALLER

## Situation

Rescuers are wet, cold and shouting over noise. Their notes are messy. Commanders need short, standard
situation reports (SITREPs) to make decisions. There is no internet to call a big cloud model.

## Mission

Build Field Brain: offline speech-to-text, a small LLM fine-tuned to turn messy notes into structured
SITREPs, a RAG search over procedures, and translation for multilingual residents.

## Recon (training reps)

```text
  [ ] FEMA IS-200.c   ICS for single resources and initial action incidents
  [ ] Udacity LLM / RAG projects in the cluster map - done solo
  [ ] Read about the ICS-209 situation report and the ICS-214 activity log (structure only)
  [ ] Whisper (small/base) and llama.cpp quick-starts
```

## Build

```text
  STEP 1  Schema         -> model/: a Sitrep Pydantic model; the LLM must output valid JSON for it
  STEP 2  ASR            -> brain/asr.py: offline speech-to-text on the Jetson
  STEP 3  Dataset        -> synthetic messy-notes -> SITREP pairs (written by you, reviewed, no real people)
  STEP 4  Fine-tune      -> LoRA on a ~3B model; then GRPO with a reward = "schema-valid + facts kept"
  STEP 5  RAG            -> brain/rag.py over the doctrine/ folder; every answer cites its source
  STEP 6  Translate      -> offline translation for the 3 most-needed languages in the area
  STEP 7  Eval           -> a held-out test set; measure schema validity and fact recall
```

```text
     reward for GRPO (sketch, YOU implement it):

        reward = 1.0 * schema_valid
               + 0.5 * fraction_of_facts_kept
               - 1.0 * any_invented_fact          <- hallucination is the worst failure
```

## Gate: RADIO SILENCE

```text
  +--------------------------------------------------------------+
  |  [ ] Airplane-mode demo: voice note -> SITREP, no network      |
  |  [ ] Schema validity >= target in docs/test-plan.md           |
  |  [ ] Invented-fact rate measured and reported                 |
  |  [ ] RAG answers cite a doctrine file every time              |
  |  [ ] End-to-end latency on the Jetson measured                |
  +--------------------------------------------------------------+
```

## Defend it

1. Why is an invented fact in a SITREP worse than a missing fact?
2. What does LoRA change in the model, and what does it leave alone?
3. Why does the RAG system have to cite its source?
4. How do you know your synthetic data does not just teach the model your own writing habits?
