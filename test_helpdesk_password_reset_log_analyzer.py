import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import unittest
from main import analyze

def row(d, a, u="user1"):
    return {"date": d, "agent": a, "user": u}

class TestResetLog(unittest.TestCase):
    def test_top_agent(self):
        _, _, _, top = analyze([row("2026-11-05", "ali"), row("2026-11-05", "ali"), row("2026-11-05", "sara")])
        self.assertEqual(top, ("ali", 2))
    def test_busiest_day(self):
        _, _, busiest, _ = analyze([row("2026-11-04", "ali"), row("2026-11-05", "ali"), row("2026-11-05", "sara")])
        self.assertEqual(busiest, ("2026-11-05", 2))
    def test_per_agent_counts(self):
        agents, _, _, _ = analyze([row("2026-11-05", "ali"), row("2026-11-05", "sara")])
        self.assertEqual(dict(agents), {"ali": 1, "sara": 1})
    def test_empty_input(self):
        agents, days, busiest, top = analyze([])
        self.assertEqual((agents, days, busiest, top), ([], [], None, None))
