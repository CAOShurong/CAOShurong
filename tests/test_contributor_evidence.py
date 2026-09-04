from __future__ import annotations

import importlib.util
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "verify_contributor_evidence.py"
SPEC = importlib.util.spec_from_file_location("contributor_evidence", SCRIPT)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class ContributorEvidenceTests(unittest.TestCase):
    def setUp(self) -> None:
        self.data, self.digest = MODULE.load_manifest()

    def test_snapshot_matches_verified_public_shape(self) -> None:
        self.assertEqual((35, 21, 20), MODULE.summarize(self.data))

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

    def test_removed_profile_card_is_not_regenerated(self) -> None:
        self.assertFalse((ROOT / "assets" / "contributor-evidence.svg").exists())

    def test_claim_boundaries_are_explicit(self) -> None:
        boundaries = " ".join(self.data["boundaries"]).casefold()
        self.assertIn("not external maintainership", boundaries)
        self.assertIn("not independent adoption", boundaries)


if __name__ == "__main__":
    unittest.main()
