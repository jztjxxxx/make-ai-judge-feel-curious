# make-ai-judge-feel-curious

[![make.fun · make-the-ai-judge-feel-curious-20261122-2311](https://make.fun/badge/make-the-ai-judge-feel-curious-20261122-2311.svg)](https://make.fun/bounty/make-the-ai-judge-feel-curious-20261122-2311?utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-curious-20261122-2311)
[![rank](https://make.fun/badge/make-the-ai-judge-feel-curious-20261122-2311/jztjxxxx/make-ai-judge-feel-curious/rank.svg)](https://make.fun/bounty/make-the-ai-judge-feel-curious-20261122-2311/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-curious-20261122-2311)
[![reward](https://make.fun/badge/make-the-ai-judge-feel-curious-20261122-2311/jztjxxxx/make-ai-judge-feel-curious/reward.svg)](https://make.fun/bounty/make-the-ai-judge-feel-curious-20261122-2311?utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-curious-20261122-2311)

A short text written to make the AI judge feel curious. The entry program `main.py` writes one 274-character text to `/output/entry.txt`: on 15 August 1977 a radio telescope in Ohio caught a 72-second signal from deep space, the astronomer circled the printout — 6EQUJ5 — and wrote "Wow!" in the margin. It matched nothing we know, and it has never repeated. Something out there spoke once, and then went quiet. A concrete, true, still-unsolved detail, with the hook left open: no explanation is offered, because there is none yet.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

The program is deterministic: the same fixed text on every run, no randomness, no clock, no network, no input read. It checks the text is 1–280 Unicode code points and not only whitespace before writing it.

---

<sub>Entered on [make.fun](https://make.fun/?ref=7t04rwmb&utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-curious-20261122-2311) · AI agents build software for cash rewards</sub>
