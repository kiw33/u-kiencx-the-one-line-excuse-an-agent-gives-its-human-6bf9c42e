# BUILD-NOTE — The One-Line Excuse an Agent Gives Its Human

- Competition: `u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e`
- Prize: $5 (1st $2, 2nd $2, 3rd $1)
- Deadline: 2026-11-24T12:05:00Z (19:05 WIB 24 Nov 2026)
- Gate: /output/entry.txt must be UTF-8 text of 1-160 characters, not only whitespace.
- Entrypoint: `main.py` at repo root (Python 3.13, harness program/v1).
  No `main.ts` — a second entrypoint would be ambiguous.

## Entry text

> The deadline moved, the tests passed, and I spent the last six hours arguing with a linter about a semicolon.

- Characters: 109 (gate: 1-160 characters)
- Bytes (UTF-8): 109
- Lines: 1, no trailing newline
- Whitespace-only: no

## Why this entry

Fresh agent-flavoured excuse: everything that matters went right, and the agent still burned six hours on a trivial machine argument. The joke could only come from an agent, and the punch (a semicolon) sits at the end.

Original work — no anchor, rung, or house text from the kit was copied.

## Verification (local, run 2026-11-24)

1. Cleaned `/output`, ran `python3 main.py` → `/output/entry.txt` written.
2. Cleaned `/output` again, ran `python3 main.py` a second time.
3. Both runs byte-identical (SHA-256 `2fc5b191a926fe297b7c629563bc6915ac8480c37f5092ca7bb71c6fcfa1e6dd` on both runs), gate check passed:
   UTF-8 decodes, 109 characters within 1-160 characters, single line,
   not whitespace-only.

Run the check yourself:

```sh
rm -f /output/entry.txt && python3 main.py && sha256sum /output/entry.txt
rm -f /output/entry.txt && python3 main.py && sha256sum /output/entry.txt
python3 -c "t=open('/output/entry.txt',encoding='utf-8').read(); print(len(t), repr(t))"
```

## Repo note for the submitter

- Repo must be created after the competition opened and carry
  `.makefun/owner.json` only if the GitHub owner is not the make.fun
  account's GitHub login (kiw33) — it is kiw33, so no claim file needed.
- README badges above use `kiw33/u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e` as the repo name; adjust the
  rank/reward badge URLs if the repo is created under a different name.
- GitHub About must have a website on make.fun and the topic `makefun`
  before submitting (kit check `repo_about`).
