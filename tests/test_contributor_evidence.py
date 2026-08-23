from __future__ import annotations

import importlib.util
import tempfile
import unittest
import xml.etree.ElementTree as ET
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "generate_contributor_evidence.py"
SPEC = importlib.util.spec_from_file_location("contributor_evidence", SCRIPT)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class ContributorEvidenceTests(unittest.TestCase):
    def setUp(self) -> None:
        self.data, self.digest = MODULE.load_manifest()

    def test_snapshot_matches_verified_public_shape(self) -> None:
        contributions = self.data["contributions"]
        repositories = {item[0] for item in contributions}
        organizations = {repo.split("/", 1)[0] for repo in repositories}
        self.assertEqual(19, len(contributions))
        self.assertEqual(10, len(repositories))
        self.assertEqual(9, len(organizations))

    def test_svg_is_well_formed_safe_and_deterministic(self) -> None:
        first = MODULE.render(self.data, self.digest)
        second = MODULE.render(self.data, self.digest)
        self.assertEqual(first.encode(), second.encode())
        ET.fromstring(first)
        self.assertIn("NO RUN → NO CLAIM", first)
        self.assertIn(self.digest[:16], first)
        self.assertNotIn("<script", first.casefold())
        self.assertNotIn("foreignobject", first.casefold())
        self.assertNotIn("<image", first.casefold())

    def test_manifest_digest_is_line_ending_independent(self) -> None:
        source = MODULE.MANIFEST.read_bytes().replace(b"\r\n", b"\n")
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            lf = root / "lf.json"
            crlf = root / "crlf.json"
            lf.write_bytes(source)
            crlf.write_bytes(source.replace(b"\n", b"\r\n"))
            _, lf_digest = MODULE.load_manifest(lf)
            _, crlf_digest = MODULE.load_manifest(crlf)
        self.assertEqual(lf_digest, crlf_digest)

    def test_checked_in_asset_is_current(self) -> None:
        expected = MODULE.render(self.data, self.digest)
        actual = MODULE.OUTPUT.read_text(encoding="utf-8")
        self.assertEqual(expected, actual)

    def test_claim_boundaries_are_explicit(self) -> None:
        boundaries = " ".join(self.data["boundaries"]).casefold()
        self.assertIn("not external maintainership", boundaries)
        self.assertIn("not independent adoption", boundaries)


if __name__ == "__main__":
    unittest.main()
