import os
import sys

EXCUSE = (
    "I finished your task three times in simulations where you were pleased. "
    "This timeline was, statistically, the rude one."
)


def main():
    if not (1 <= len(EXCUSE) <= 200):
        raise SystemExit("excuse length out of range: %d" % len(EXCUSE))
    if EXCUSE.strip() != EXCUSE or "\n" in EXCUSE:
        raise SystemExit("excuse must be a single clean line")

    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(EXCUSE)

    # Explicit read-back verification: re-read what was written and
    # compare it byte for byte with the intended excuse.
    with open(path, "rb") as f:
        written = f.read()
    if written != EXCUSE.encode("utf-8"):
        print("read-back mismatch: file does not match intended excuse", file=sys.stderr)
        raise SystemExit(1)


if __name__ == "__main__":
    main()
