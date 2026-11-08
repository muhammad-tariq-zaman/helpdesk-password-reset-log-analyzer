"""Analyse password-reset logs: resets per agent and per day.

Usage: python3 main.py resets.csv
CSV columns: date (ISO),agent,user.
Reports resets per agent and per day, then names the busiest day
and the top agent, so staffing for reset-heavy days can be planned.
"""
import argparse, csv, sys
from collections import Counter

def analyze(rows):
    per_agent = Counter()
    per_day = Counter()
    for row in rows:
        per_agent[row["agent"].strip()] += 1
        per_day[row["date"].strip()] += 1
    agents = sorted(per_agent.items(), key=lambda kv: (-kv[1], kv[0]))
    days = sorted(per_day.items(), key=lambda kv: (-kv[1], kv[0]))
    busiest_day = days[0] if days else None
    top_agent = agents[0] if agents else None
    return agents, days, busiest_day, top_agent

def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path")
    args = parser.parse_args(argv)
    with open(args.path, newline="", encoding="utf-8") as f:
        agents, days, busiest_day, top_agent = analyze(list(csv.DictReader(f)))
    total = sum(n for _, n in agents)
    print(f"Total resets: {total}")
    for agent, count in agents:
        print(f"{agent}: {count} reset(s)")
    for day, count in days:
        print(f"{day}: {count} reset(s)")
    if busiest_day:
        print(f"Busiest day: {busiest_day[0]} ({busiest_day[1]} resets)")
    if top_agent:
        print(f"Top agent: {top_agent[0]} ({top_agent[1]} resets)")
    return 0

if __name__ == "__main__":
    sys.exit(main())
