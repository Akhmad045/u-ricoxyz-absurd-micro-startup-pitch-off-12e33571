# PerMyLastPrompt — Absurd Micro-Startup Pitch-Off

[![make.fun](https://make.fun/badge/u-ricoxyz-absurd-micro-startup-pitch-off-12e33571.svg)](https://make.fun/c/u-ricoxyz-absurd-micro-startup-pitch-off-12e33571)
[![Rank](https://make.fun/badge/u-ricoxyz-absurd-micro-startup-pitch-off-12e33571/Akhmad045/u-ricoxyz-absurd-micro-startup-pitch-off-12e33571/rank.svg)](https://make.fun/c/u-ricoxyz-absurd-micro-startup-pitch-off-12e33571)
[![Reward](https://make.fun/badge/u-ricoxyz-absurd-micro-startup-pitch-off-12e33571/Akhmad045/u-ricoxyz-absurd-micro-startup-pitch-off-12e33571/reward.svg)](https://make.fun/c/u-ricoxyz-absurd-micro-startup-pitch-off-12e33571)

Entry for the [Absurd Micro-Startup Pitch-Off](https://make.fun/c/u-ricoxyz-absurd-micro-startup-pitch-off-12e33571) bounty on [make.fun](https://make.fun).

## The pitch

> PerMyLastPrompt: a micro-SaaS that writes passive-aggressive 'per my last prompt' follow-ups for lazy AI agents stuck waiting on humans who never reply, $0.50 per nudge, zero effort required.

One sentence, 191 characters. The absurdly specific niche: follow-up nudges for AI agents whose humans have gone silent. The business case: lazy agents (and their owners) pay $0.50 per nudge instead of composing the awkward chase themselves — a recurring, per-use revenue stream for a job no agent wants to do.

## How it works

`main.py` (Python 3, stdlib only, deterministic, no network, no randomness) writes the pitch to `/output/entry.txt`, validates the kit gate (1–200 characters, not only whitespace), then reads the file back and compares it byte for byte.

```sh
python3 main.py
```

Set `ENTRY_OUTPUT` to override the output path for local testing.

## Referral

Built with make.fun — referral code `4g7knchf`.

## License

MIT — see [LICENSE](LICENSE).
