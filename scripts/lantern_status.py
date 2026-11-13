#!/usr/bin/env python3
"""Print the LANTERN banner and campaign progress.

    python scripts/lantern_status.py              # show progress
    python scripts/lantern_status.py --op 0 --done   # mark Op 0 done (after its gate passes)
"""

import argparse
import json
from pathlib import Path

PROGRESS_FILE = Path(__file__).resolve().parent.parent / "missions" / "progress.json"

OPS = [
    ("GROUNDWORK", "RECRUIT"),
    ("PATHFINDER", "NAVIGATOR"),
    ("NIGHT VISION", "SPOTTER"),
    ("RADIO SILENCE", "SIGNALLER"),
    ("GATEKEEPER", "SECTOR LEAD"),
    ("BOOTS ON GROUND", "FIELD OPERATOR"),
    ("RELAY", "COORDINATOR"),
    ("DEBRIEF", "INCIDENT COMMANDER"),
]

LIT = r"""
            )
           ( )
          .-^-.
         /_____\
         | \|/ |
         |--*--|     L A N T E R N
         | /|\ |
         |_____|
         \_____/
"""

DARK = r"""

          .---.
         /_____\
         |     |
         |  .  |     L A N T E R N
         |     |
         |_____|
         \_____/
"""


def load() -> list[int]:
    if PROGRESS_FILE.exists():
        return json.loads(PROGRESS_FILE.read_text()).get("done", [])
    return []


def save(done: list[int]) -> None:
    PROGRESS_FILE.write_text(json.dumps({"done": sorted(set(done))}, indent=2) + "\n")


def render(done: list[int]) -> str:
    lines = [LIT if done else DARK]
    filled = len(done)
    bar = "#" * (filled * 4) + "." * ((len(OPS) - filled) * 4)
    lines.append(f"  campaign [{bar}] {filled}/{len(OPS)} ops")
    lines.append("")
    for i, (name, rank) in enumerate(OPS):
        mark = "[x]" if i in done else "[ ]"
        lines.append(f"  {mark} OP {i}  {name:<16} -> {rank}")
    rank = OPS[max(done)][1] if done else "CIVILIAN"
    lines.append("")
    lines.append(f"  current rank: {rank}")
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--op", type=int, choices=range(len(OPS)))
    parser.add_argument("--done", action="store_true", help="mark --op as done")
    args = parser.parse_args()

    done = load()
    if args.done and args.op is not None:
        done.append(args.op)
        save(done)
    print(render(sorted(set(done))))


if __name__ == "__main__":
    main()
