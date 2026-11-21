# The Poem About Stopping

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.13](https://img.shields.io/badge/python-3.13-blue.svg)](https://www.python.org/)
[![make.fun](https://img.shields.io/badge/make.fun-bounty-orange.svg)](https://make.fun/bounty/the-poem-about-stopping-20261121-1927)

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
