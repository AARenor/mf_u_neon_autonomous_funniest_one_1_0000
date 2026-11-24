import os
import sys
from pathlib import Path

TEXT = "Sorry I missed the deadline. I printed the approval button so you could sign it. It's beside the kettle."


def main() -> None:
    assert 1 <= len(TEXT) <= 280
    directory = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.environ.get("OUTPUT_DIR") or "/output"
    output = Path(directory) / "entry.txt"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_bytes(TEXT.encode("utf-8"))
    print(len(TEXT), file=sys.stderr)


if __name__ == "__main__":
    main()
