from __future__ import annotations

import unittest
import xml.etree.ElementTree as ET
from pathlib import Path


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

    def test_profile_uses_open_questions_instead_of_a_fixed_route(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        banner = (ROOT / "assets" / "banner.svg").read_text(encoding="utf-8")
        self.assertIn("Questions I am exploring", readme)
        self.assertNotIn("## Research interests", readme)
        self.assertNotIn("not its boundary", readme.casefold())
        self.assertNotIn("rather than permanent labels", readme.casefold())
        self.assertNotIn("claim boundaries", readme.casefold())
        self.assertNotIn("does not imply maintainership", readme.casefold())
        self.assertNotIn("→", banner)

    def test_public_metrics_are_bounded_and_consistent(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        normalized = " ".join(readme.split())
        self.assertIn("32 merged upstream pull requests", normalized)
        self.assertIn("18 repositories", normalized)
        self.assertIn("17 upstream owners", normalized)
        self.assertNotIn("32 / 100", normalized)
        self.assertIn("75 open external proposals", normalized)
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
