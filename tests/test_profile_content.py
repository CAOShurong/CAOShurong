from __future__ import annotations

import unittest
import xml.etree.ElementTree as ET
from pathlib import Path
from urllib.parse import parse_qs, urlsplit
import re


ROOT = Path(__file__).resolve().parents[1]


class ProfileContentTests(unittest.TestCase):
    def test_academic_identity_and_collaboration_details_are_explicit(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        self.assertIn("Electronic Engineering", readme)
        self.assertIn("The Chinese University of Hong Kong", readme)
        self.assertIn("Nanjing University", readme)
        self.assertIn("internships", readme)
        self.assertIn("Hong Kong or Shenzhen", readme)
        self.assertIn("North America, Europe", readme)

    def test_profile_keeps_research_exploratory_and_secondary(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        banner = (ROOT / "assets" / "banner.svg").read_text(encoding="utf-8")
        self.assertIn("I am exploring", readme)
        self.assertLess(readme.index("## Selected work"), readme.index("## Research background"))
        self.assertLess(readme.index("## Open-source contributions"), readme.index("## Research background"))
        self.assertNotIn("## Research interests", readme)
        self.assertNotIn("not its boundary", readme.casefold())
        self.assertNotIn("rather than permanent labels", readme.casefold())
        self.assertNotIn("claim boundaries", readme.casefold())
        self.assertNotIn("does not imply maintainership", readme.casefold())
        self.assertNotIn("→", banner)

    def test_public_metrics_are_bounded_and_consistent(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        normalized = " ".join(readme.split())
        searches = re.findall(r"https://github.com/search\?[^)\s]+", readme)
        queries = [parse_qs(urlsplit(url).query)["q"][0].split() for url in searches]
        self.assertEqual(len(queries), 2)
        for query in queries:
            self.assertIn("author:CAOShurong", query)
            self.assertIn("-user:CAOShurong", query)
            self.assertIn("is:pr", query)
        self.assertEqual(sum("is:merged" in q for q in queries), 1)
        self.assertEqual(sum("is:open" in q for q in queries), 1)
        self.assertNotIn("35 / 100", normalized)
        self.assertNotRegex(normalized, r"\d+\+? merged upstream")
        self.assertNotIn("contributor-evidence.svg", normalized)

    def test_banner_is_well_formed_and_self_contained(self) -> None:
        path = ROOT / "assets" / "banner.svg"
        text = path.read_text(encoding="utf-8")
        ET.fromstring(text)
        self.assertNotIn("<script", text.casefold())
        self.assertNotIn("foreignobject", text.casefold())
        self.assertNotIn("<image", text.casefold())
        self.assertFalse((ROOT / "assets" / "contributor-evidence.svg").exists())


if __name__ == "__main__":
    unittest.main()
