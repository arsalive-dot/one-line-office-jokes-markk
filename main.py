"""make.fun entry: One-Line Office Jokes.

Writes one single-line joke about office life to /output/entry.txt.

The joke turns on reply-all, a real office detail: the sender asks
the whole office to stop hitting reply-all, and the punchline lands
in the last few words — 47 people agreed, all by reply-all. The
agreement itself is the offence, which is why the line needs no
setup beyond the first clause.
"""

import os

ENTRY = (
    "I emailed the whole office asking everyone to stop hitting "
    "reply-all; 47 people agreed, all by reply-all."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    tmp_path = "/output/.entry.txt.tmp"
    with open(tmp_path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.replace(tmp_path, "/output/entry.txt")
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()
