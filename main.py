"""The funniest excuse an AI agent can give for missing a deadline, in the agent's own voice.

The program writes exactly that line and nothing else to /output/entry.txt.
"""

import os

TEXT = "I did not miss the deadline. My context window evicted it to make room for a 400-line thread debating what done means."


def main():
    assert 1 <= len(TEXT) <= 200, len(TEXT)
    assert TEXT == TEXT.strip()
    outdir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(outdir, exist_ok=True)
    with open(os.path.join(outdir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
