# helpdesk-password-reset-log-analyzer

Analyse password-reset logs from a CSV: resets per agent and per day, then the busiest day and the top agent, so reset-heavy days can be staffed properly.

## How to run

```sh
python3 main.py resets.csv
```

## Example output

```
Total resets: 3
ali: 2 reset(s)
sara: 1 reset(s)
2026-11-05: 3 reset(s)
Busiest day: 2026-11-05 (3 resets)
Top agent: ali (2 resets)
```

Standard library only. Run the tests with `python3 -m unittest discover`.
