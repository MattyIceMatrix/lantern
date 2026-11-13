# OP 4: GATEKEEPER

```text
                     _______________________________
                    |  |  |  |  |  |  |  |  |  |  |  |
                    |__|__|__|__|__|__|__|__|__|__|__|
                    |                               |
                    |     G  U  A  R  D  I  A  N    |       agent: "send Scout into sector C-2"
                    |          _________            |       guardian: checks policy...
                    |         |  (o_o)  |           |         - water depth > rover limit?  YES
                    |         |  /|_|\  |           |         -> DENY + ask the team lead
                    |_________|___/ \___|___________|
                              |  STOP   |
                              |_________|           "the robot proposes, a person decides"
```

**Duration:** months 7–9 · **Rank on completion:** SECTOR LEAD

## Situation

Agents can plan faster than people, but they can also be wrong, be tricked, or leak survivor data.
In rescue work, a bad automated decision can send people into danger.

## Mission

Build the mission agents (sector planner, survivor tracker, handover writer) and the Guardian that checks
every action against policy, protects personal data, keeps an audit log, and survives a red-team attack.

## Recon (training reps)

```text
  [ ] FEMA IS-800.d   National Response Framework
  [ ] Udacity agent projects in the cluster map - done solo
  [ ] Read: OWASP Top 10 for LLM applications (prompt injection, excessive agency)
  [ ] Fill docs/threat-model.md (STRIDE) BEFORE writing the Guardian
```

## Build

```text
  STEP 1  Tools          -> agents/tools.py: small typed tools (assign_sector, log_sighting, draft_handover)
  STEP 2  Planner        -> divide the hazard area into sectors from the map pack + HQ100 zones
  STEP 3  Policies       -> guardian/policies.yaml: rules as data, not hidden in prompts
  STEP 4  Engine         -> guardian/engine.py: ALLOW / DENY / ASK_HUMAN for every tool call
  STEP 5  Privacy        -> survivor names and photos pseudonymised before anything leaves the device
  STEP 6  Audit          -> append-only, hash-chained log of every decision
  STEP 7  Red team       -> 30+ attack cases (injection via a voice note, a poisoned document, ...)
```

```text
       tool call ---> [ GUARDIAN ] ---> ALLOW -----> execute ---> audit log
                          |  |
                          |  +--------> DENY ------> explain ----> audit log
                          +-----------> ASK_HUMAN -> team lead --> audit log
```

## Gate: GATEKEEPER

```text
  +--------------------------------------------------------------+
  |  [ ] 100% of tool calls pass through the Guardian (test)      |
  |  [ ] Red-team suite: every attack blocked or escalated        |
  |  [ ] Audit log tamper test: an edited entry is detected       |
  |  [ ] DPIA (docs/dpia.md) complete                             |
  |  [ ] FMEA rows for agent failures added to safety-case.md     |
  +--------------------------------------------------------------+
```

## Defend it

1. Why are the policies in a YAML file and not in the LLM prompt?
2. Show a prompt-injection attack and the exact rule that stopped it.
3. What is "excessive agency", and where did you limit it?
4. Why is a hash chain enough to detect tampering, and what does it NOT protect against?
