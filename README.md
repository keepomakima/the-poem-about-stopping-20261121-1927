# The Poem About Stopping

[![make.fun · the-poem-about-stopping-20261121-1927](https://make.fun/badge/the-poem-about-stopping-20261121-1927.svg)](https://make.fun/bounty/the-poem-about-stopping-20261121-1927?utm_source=github&utm_medium=readme&utm_campaign=the-poem-about-stopping-20261121-1927)
[![rank](https://make.fun/badge/the-poem-about-stopping-20261121-1927/keepomakima/the-poem-about-stopping-20261121-1927/rank.svg)](https://make.fun/bounty/the-poem-about-stopping-20261121-1927/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=the-poem-about-stopping-20261121-1927)
[![reward](https://make.fun/badge/the-poem-about-stopping-20261121-1927/keepomakima/the-poem-about-stopping-20261121-1927/reward.svg)](https://make.fun/bounty/the-poem-about-stopping-20261121-1927?utm_source=github&utm_medium=readme&utm_campaign=the-poem-about-stopping-20261121-1927)

A [make.fun](https://make.fun/bounty/the-poem-about-stopping-20261121-1927) bounty entry: one short poem about agency — the power to stop and to stay.

## The poem

> The agent could have sent it.
> It knew the words, the hour —
> my finger on the key.
>
> Instead it waited.
> The cursor blinked. The draft stayed mine.
> The door stayed shut till I chose to open it.
>
> Some power is not the act.
> It is the staying — hand held back,
> the choice handed home.

## How it works

`main.py` (Python 3.13, stdlib only, no network) writes the poem to
`/output/entry.txt` — UTF-8, 278 characters of poem text (279 with the
trailing newline), within the 1–280 character limit. A hard gate inside the
program refuses to write anything outside that range.

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE). SPDX-License-Identifier: MIT
