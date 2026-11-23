"""One Word From Grandma — entry for make.fun.

Writes exactly one word to entry.txt: the word my grandma would
text about AI. Deterministic, no network, no model calls.
"""

import os

WORD = "beepboop"


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(WORD)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
