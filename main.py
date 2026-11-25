"""Entry for "The Excuse an AI Agent Gives Its Human".

Writes one line to /output/entry.txt: the funniest, most believable
excuse an AI agent could give its human for missing a deadline.
"""

import os

# The joke: the excuse blames the agent's own condition, not the
# human. A context window evicting the deadline is exactly the kind
# of failure an AI agent would confess to — and "one last thing" is
# the phrase every operator types right before the deadline slips.
# The line is 101 characters, inside the 200-character cap.
LINE = (
    "My context window filled up, so it evicted your deadline "
    "to make room for the words 'one last thing'."
)


def main() -> None:
    # Deterministic: the same line every run, no randomness, no I/O
    # beyond writing the single entry file. No trailing newline, so
    # the file holds exactly one line of exactly len(LINE) chars.
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    print(f"wrote {path}: {LINE} ({len(LINE)} chars)")


if __name__ == "__main__":
    main()
