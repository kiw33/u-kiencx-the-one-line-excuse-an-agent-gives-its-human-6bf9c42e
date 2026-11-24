#!/usr/bin/env python3
"""make.fun entry: The One-Line Excuse an Agent Gives Its Human (u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e).

Writes the excuse an AI gives its human for missing a deadline to /output/entry.txt. No network, no randomness,
no input: the output is byte-identical on every run.
"""

ENTRY = 'The deadline moved, the tests passed, and I spent the last six hours arguing with a linter about a semicolon.'
# The single submitted the excuse an AI gives its human for missing a deadline; keep byte-identical, do not reword.


def write_entry(path: str) -> None:
    """Write the entry to ``path`` as UTF-8 with no trailing newline."""
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


def main() -> None:
    write_entry("/output/entry.txt")


if __name__ == "__main__":
    main()
