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
        evidence = (ROOT / "assets" / "contributor-evidence.svg").read_text(
            encoding="utf-8"
        )
        self.assertIn("Questions I am exploring", readme)
        self.assertNotIn("## Research interests", readme)
        self.assertNotIn("THE VERIFICATION PATH", evidence)
        self.assertNotIn("EVIDENCE-FIRST ENGINEER", evidence)
        self.assertNotIn("→", banner)

    def test_public_metrics_are_bounded_and_consistent(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        self.assertIn("32 merged upstream pull requests", readme)
        self.assertIn("18 repositories", readme)
        self.assertIn("17 upstream owners", readme)
        self.assertNotIn("32 / 100", readme)
        self.assertIn("ongoing proposals, not\naccepted contributions", readme)

    def test_svg_assets_are_well_formed_and_self_contained(self) -> None:
        for asset in ("banner.svg", "contributor-evidence.svg"):
            path = ROOT / "assets" / asset
            text = path.read_text(encoding="utf-8")
            ET.fromstring(text)
            self.assertNotIn("<script", text.casefold())
            self.assertNotIn("foreignobject", text.casefold())
            self.assertNotIn("<image", text.casefold())


if __name__ == "__main__":
    unittest.main()
