# The joke

Final entry (103 characters, one line):

> Removed the post-checkout hook that detects a detached HEAD just to echo "Hi detached, I'm Dad."

Draft v1 (replaced):

> Why did the dad cross the road? To git to the other side.

## Why the final wins — against the judge's criteria and the champion structure

The judge (brief published in the kit) weighs, in order: (1) a dad joke a
father would tell at the table; (2) the pun lands cleanly on first read;
(3) fresh rather than told a thousand times, while staying inside the dad
joke tradition; (4) tight, punchline at the end; (5) reads naturally aloud.

- v1 is the canonical road-crossing frame with a git pun swapped in. It is
  exactly the "told a thousand times" shape criterion 3 loses to, and the
  pun is the whole joke — there is no second beat.
- The final keeps the oldest dad-joke reflex there is — a father answering
  a plain statement by introducing himself ("Hi X, I'm Dad") — but the
  setup is fresh: a post-checkout hook whose only job is to greet a
  detached HEAD. The turn needs no explanation (criterion 2): anyone who
  has seen the "Hi hungry, I'm Dad" move gets it on first read, and the
  git vocabulary is the scene, not a bolted-on pun.
- It is told deadpan as a changelog line, straight-faced on the page, and
  the punchline ("I'm Dad.") is the last thing read (criterion 4). Read
  aloud it has the flat, pleased-with-itself rhythm of a joke told across
  a dinner table (criterion 5).

Champion structure check (PAST-WINNERS.md, joke class): winning one-liners
run 73–240 bytes, are format-native (commit messages, code review, flaky
tests), and read like something clipped out of real work. The final is
103 bytes in that band, shaped like a commit/changelog line, with the gag
grown inside the tool itself rather than pasted onto a generic frame.
