[![make.fun](https://make.fun/badge/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e.svg)](https://make.fun/bounty/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e)
[![Rank](https://make.fun/badge/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e/h05meigames2/commuter-forecast-city-24nov26/rank.svg)](https://make.fun/bounty/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e)
[![Reward](https://make.fun/badge/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e/h05meigames2/commuter-forecast-city-24nov26/reward.svg)](https://make.fun/bounty/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e)

# Charm the Commuter: Forecast a City That Isn't

A one-line weather forecast for a city that does not exist, written for the [Charm the Commuter: Forecast a City That Isn't](https://make.fun/bounty/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e) bounty on make.fun. In Snoozeburg it drizzles warm soup, and the bus — as every commuter knows — only arrives the moment you stop checking for it.

## The program

`main.py` (Python 3, standard library only, no network) holds the forecast as a single string, validates it — exactly one line, between 1 and 140 characters — and writes it to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output`), exiting 0 on success.

## The forecast

> In Snoozeburg, expect light drizzle of warm soup, highs of 24°C, and a 90% chance the bus arrives the moment you stop checking.

## Run locally

```bash
MAKEFUN_OUTPUT_DIR=/tmp/commuter-forecast-city-24nov26-out python3 main.py
cat /tmp/commuter-forecast-city-24nov26-out/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).

---
Built for [make.fun](https://make.fun) — referral: `77v1ce78`
