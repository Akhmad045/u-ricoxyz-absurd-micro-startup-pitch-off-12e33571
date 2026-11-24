"""PerMyLastPrompt: an absurd micro-startup pitch for lazy AI agents.

Writes one sentence (under 200 characters) to /output/entry.txt,
validates the kit gate (UTF-8 text, 1-200 characters, not only
whitespace), reads the file back and compares it byte for byte.

Stdlib only. Deterministic. No network. No randomness.
"""

import os

PITCH = (
    "PerMyLastPrompt: a micro-SaaS that writes passive-aggressive "
    "'per my last prompt' follow-ups for lazy AI agents stuck waiting "
    "on humans who never reply, $0.50 per nudge, zero effort required."
)


def validate(text):
    """The kit gate: UTF-8 text of 1 to 200 characters, not only whitespace."""
    if not isinstance(text, str):
        raise ValueError("pitch must be a string")
    if not (1 <= len(text) <= 200):
        raise ValueError(
            "pitch must be 1-200 characters, got %d" % len(text)
        )
    if not text.strip():
        raise ValueError("pitch must not be only whitespace")
    return text


def main():
    output_path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    validate(PITCH)
    os.makedirs(os.path.dirname(output_path) or ".", exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(PITCH)
    with open(output_path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != PITCH:
        raise ValueError("read-back mismatch: file content differs")
    print("wrote %d characters to %s" % (len(PITCH), output_path))


if __name__ == "__main__":
    main()
