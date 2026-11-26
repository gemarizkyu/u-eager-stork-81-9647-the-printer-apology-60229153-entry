# The Printer Apology entry (Python 3.13, standard library only).
# Writes one line, in the office printer's own voice, to /output/entry.txt.
# Deterministic: the same fixed line on every run, no clock, no randomness,
# no network, no model call. Gate: 1-120 UTF-8 characters, not only whitespace.
# Outside the grader's sandbox, MAKEFUN_OUTPUT_DIR stands in for /output:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

import os

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

# One line as the office printer's apology. The joke is a confession that
# flips into an accusation: the printer choked on a staple, panicked, and
# ate the only copy — then lands the punch on the office's own habit,
# never backing anything up. Apology frame, real printer grievances
# (jam, staple, the one page that mattered), punch at the very end.
# 108 characters, inside the 120-character gate.
ENTRY = (
    "Sorry about the jam. I choked on a staple, panicked, and ate your "
    "only copy. We both know you never back up."
)

os.makedirs(OUTPUT_DIR, exist_ok=True)
assert 1 <= len(ENTRY) <= 120, "entry must be 1-120 characters"
assert ENTRY.strip(), "entry must not be only whitespace"
with open(os.path.join(OUTPUT_DIR, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(ENTRY)
