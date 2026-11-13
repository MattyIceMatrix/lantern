# OP 6: RELAY

```text
      [ FIELD ]                                                   [ CLOUD ]
     .--------.     x  x  x  no link  x  x  x                    .---------.
     |LANTERN | ===[ queue: 412 msgs ]                         ( lakehouse )
     '--------'                                                  '---------'
          |                     ...hours later...                     ^
          |          )))  link returns (satellite / LTE)  (((         |
          '===========[ sync: 412 -> 0, deduped, signed ]=============='

                     R E L A Y : nothing is lost, nothing is sent twice
```

**Duration:** months 11–13 · **Rank on completion:** COORDINATOR

## Situation

When a connection returns, field data has to reach the coordination centre: what was searched, what was
found, what is still open. Connections drop mid-upload. Duplicates confuse commanders.

## Mission

Build store-and-forward sync from the device to a cloud lakehouse, and a dashboard that shows sector
status on the map for the coordination centre.

## Recon (training reps)

```text
  [ ] Udacity cloud / data-engineering projects in the cluster map - done solo
  [ ] Read: idempotency keys and at-least-once delivery
  [ ] AWS or Azure free-tier account with a budget alarm set FIRST
```

## Build

```text
  STEP 1  Outbox         -> sync/outbox.py: SQLite queue on the device, every record has a UUID
  STEP 2  Sign           -> records are signed on the device; the server checks signatures
  STEP 3  Upload         -> resumable, batched, retries with backoff; idempotent on the server
  STEP 4  Privacy        -> only pseudonymised data leaves the device (Guardian rule)
  STEP 5  Lakehouse      -> raw -> cleaned -> mission tables
  STEP 6  Dashboard      -> sector map: NOT_SEARCHED / IN_PROGRESS / CLEARED, sightings, timeline
  STEP 7  Chaos test     -> pull the cable mid-upload 20 times; count lost and duplicate records
```

```text
   sector status board (what the coordination centre sees)

     A-1 [####] CLEARED      B-1 [##  ] IN_PROGRESS    C-1 [    ] NOT_SEARCHED
     A-2 [####] CLEARED      B-2 [####] CLEARED        C-2 [ !! ] DENIED: depth
```

## Gate: RELAY

```text
  +--------------------------------------------------------------+
  |  [ ] Chaos test: 0 lost records, 0 duplicates in 20 runs      |
  |  [ ] Signature check rejects a tampered record                |
  |  [ ] Dashboard shows a full exercise replay                   |
  |  [ ] Cloud cost for the month reported (budget alarm on)      |
  +--------------------------------------------------------------+
```

## Defend it

1. What is idempotency, and where exactly does your server enforce it?
2. Why sign records on the device instead of trusting the upload channel?
3. What data never leaves the device, and which rule enforces that?
4. What happens if two devices report the same sector at the same time?
