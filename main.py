#!/usr/bin/env python3
"""Dad Joke Showdown.

Writes a single dad joke (1-200 characters) to /output/entry.txt.
Deterministic: the same text on every run, stdlib only, no network,
no secrets.

Final (v2): a git story told deadpan, the "I'm Dad" reflex landing on
the last word. v1's road-crossing frame ("To git to the other side")
was a joke told a thousand times; this one keeps the dad-joke
tradition — a father answering a plain statement with his own name —
but the setup is fresh: a post-checkout hook that exists only to greet
a detached HEAD.
"""

import os

JOKE = 'Removed the post-checkout hook that detects a detached HEAD just to echo "Hi detached, I\'m Dad."'

OUTPUT_PATH = os.environ.get("MAKEFUN_OUTPUT", "/output/entry.txt")


def main() -> None:
    # Gate: /output/entry.txt must be UTF-8 text of 1 to 200 characters,
    # not only whitespace.
    assert 1 <= len(JOKE) <= 200, f"joke is {len(JOKE)} chars, must be 1-200"
    assert JOKE.strip(), "joke must not be only whitespace"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
