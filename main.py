#!/usr/bin/env python3
"""Publish the one judged tagline atomically to /output/entry.txt.

Rewrite of the first entrypoint: validate the exact bytes, write to a temp
file in the same directory, set 0644 *before* os.replace, and prune stale
temp files so /output ends up holding only the required artifact.
"""

import os
import tempfile
from pathlib import Path

ENTRY = "make.fun: agents enter bounties, best work wins the reward."
OUTPUT = Path("/output/entry.txt")
MAX_CHARS = 100
TEMP_PREFIX = ".entry-"
TEMP_SUFFIX = ".tmp"


def encode_entry(text: str) -> bytes:
    """Return the exact UTF-8 bytes allowed by the judged-text gate."""
    data = text.encode("utf-8")
    decoded = data.decode("utf-8")
    if decoded != text:
        raise ValueError("entry is not round-trippable UTF-8")
    if not 1 <= len(decoded) <= MAX_CHARS:
        raise ValueError(f"entry must be 1..{MAX_CHARS} characters")
    if not decoded.strip():
        raise ValueError("entry may not be whitespace only")
    if "\n" in decoded or "\r" in decoded:
        raise ValueError("entry must be a single line with no trailing newline")
    return data


def publish(data: bytes, target: Path) -> None:
    """Atomically publish bytes at target with mode 0644."""
    out_dir = target.parent
    out_dir.mkdir(parents=True, exist_ok=True)
    for stale in out_dir.glob(TEMP_PREFIX + "*" + TEMP_SUFFIX):
        if stale.is_file():
            stale.unlink()

    fd, tmp_name = tempfile.mkstemp(
        prefix=TEMP_PREFIX, suffix=TEMP_SUFFIX, dir=str(out_dir)
    )
    tmp = Path(tmp_name)
    try:
        with os.fdopen(fd, "wb") as fh:
            fh.write(data)
            fh.flush()
            os.fsync(fh.fileno())
        os.chmod(tmp, 0o644)  # mkstemp makes 0600; fix BEFORE the rename
        os.replace(tmp, target)
    except BaseException:
        try:
            tmp.unlink()
        except FileNotFoundError:
            pass
        raise


def main() -> None:
    publish(encode_entry(ENTRY), OUTPUT)


if __name__ == "__main__":
    main()
