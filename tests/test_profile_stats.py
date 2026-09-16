from __future__ import annotations

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from update_profile_stats import END, START, update_readme


class ProfileStatsTests(unittest.TestCase):
    def test_refresh_preserves_content_outside_markers_and_is_idempotent(self):
        source = f"My introduction\n{START}\nold totals\n{END}\nMy projects"
        live = {("astropy/astropy", 1), ("astropy/astropy", 2), ("rclone/rclone", 3)}
        result = update_readme(source, live, "16 September 2026")
        self.assertTrue(result.startswith("My introduction\n" + START))
        self.assertTrue(result.endswith(END + "\nMy projects"))
        self.assertIn("3 merged pull requests · 2 upstream repositories", result)
        self.assertEqual(result, update_readme(result, live, "17 September 2026"))

    def test_empty_results_and_ambiguous_markers_fail_without_replacement(self):
        valid = f"{START}\n{END}"
        with self.assertRaises(ValueError):
            update_readme(valid, set(), "today")
        for invalid in ("", valid + START, valid + END, END + START):
            with self.assertRaises(ValueError):
                update_readme(invalid, {("astropy/astropy", 1)}, "today")
