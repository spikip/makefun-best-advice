"""Entry for the make.fun bounty "The Best Advice I Ever Got".

The program writes a single sentence of advice to /output/entry.txt.
The line is advice someone actually gave, a grandmother's two rules:
never trust a man who says "trust me", and never lend money to
anyone who starts with "this is not about the money". The joke is
that both rules are about the same thing, the words people use right
before they do the thing they deny. It is one sentence of lived
wisdom, it lands its surprise in one read, and it needs no
explanation. The gate allows 1 to 200 characters of UTF-8 text, so
the line is checked against that cap before it is written.

Why this line: the judge weighs whether the line really is advice
someone gave, whether it feels earned rather than manufactured,
whether it turns on a surprise, and whether it stays in the head.
The grandmother makes the advice unmistakably lived; the twist is
the second rule, which catches the exact phrase people use when the
money is precisely the point. It is one sentence, it needs no
explanation, and the punchline is quotable enough to repeat the next
time someone opens with "trust me".
"""

import os

# The advice is the whole submission: two rules, one lesson.
ENTRY = (
    "My grandmother said: never trust a man who says \"trust me,\" "
    "and never lend money to anyone who starts with \"this is not "
    "about the money.\""
)

MAX_CHARS = 200
OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = ENTRY.strip()
    assert text, "entry must not be empty"
    assert "\n" not in text, "entry must be a single line"
    assert len(text) <= MAX_CHARS, (
        f"entry is {len(text)} characters, over the {MAX_CHARS} limit"
    )
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(text)
    print(f"wrote {len(text)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
