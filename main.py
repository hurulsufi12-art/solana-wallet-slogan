"""One-Line Slogan for a Solana Wallet Agent.

Writes a single slogan (<=20 words, 1-140 chars, one line) to
/output/entry.txt. Stdlib only, deterministic, no network, no model calls.
"""
import os
from pathlib import Path

SLOGAN = (
    "Your Solana wallet, finally awake \u2014 it handles the paying "
    "and swapping, you handle the living."
)

DEFAULT_OUTPUT = Path("/output/entry.txt")


def validate(text: str) -> None:
    """Enforce the RULES.txt gate before writing: 1-140 chars, <=20 words,
    a single line, not only whitespace. Fail loudly instead of shipping
    an invalid entry."""
    if not (1 <= len(text) <= 140):
        raise ValueError(f"slogan is {len(text)} chars, gate requires 1-140")
    if not text.strip():
        raise ValueError("slogan is only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("slogan must be a single line")
    if len(text.split()) > 20:
        raise ValueError(f"slogan is {len(text.split())} words, max 20")


def main() -> None:
    validate(SLOGAN)
    out = Path(os.environ.get("ENTRY_OUTPUT", str(DEFAULT_OUTPUT)))
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(SLOGAN, encoding="utf-8")


if __name__ == "__main__":
    main()
