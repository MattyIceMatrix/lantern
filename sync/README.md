# Sync

```text
   device                                                    cloud
   +-----------+     x x x  (no link)  x x x                 +-----------+
   |  OUTBOX   |                                             | LAKEHOUSE |
   | [#][#][#] | ====== link returns: resumable upload =====>| raw       |
   | [#][#][#] |        signed, batched, idempotent          | cleaned   |
   +-----------+                                             | mission   |
                                                             +-----+-----+
                                                                   |
                                                             [ dashboard ]
```

| File (to create) | Op | What it does |
| --- | --- | --- |
| `outbox.py` | 6 | SQLite queue; every record has a UUID and a signature |
| `uploader.py` | 6 | batches, retries with backoff, resumes after a cut |
| `server/` | 6 | API that rejects bad signatures and ignores duplicates |
| `dashboard/` | 6 | sector status map for the coordination centre |
| `chaos.py` | 6 | cuts the link 20 times and counts lost/duplicate records |
