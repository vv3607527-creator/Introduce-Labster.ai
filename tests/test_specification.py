import pathlib
import unittest


ROOT = pathlib.Path(__file__).resolve().parents[1]
SPEC = ROOT / "Labster ai"


class SpecificationIntegrityTests(unittest.TestCase):
    def test_specification_exists_and_is_nonempty(self):
        self.assertTrue(SPEC.is_file())
        self.assertGreater(SPEC.stat().st_size, 0)

    def test_specification_covers_required_product_areas(self):
        text = SPEC.read_text(encoding="utf-8")
        required_sections = (
            "Core Principles",
            "System Overview",
            "Recommended Tech Stack",
            "Chat Platform Integrations",
            "Voice Assistant",
            "Memory System",
            "Guided Setup",
            "Hardware Recommendations",
        )
        missing = [section for section in required_sections if section not in text]
        self.assertEqual([], missing, f"Missing specification sections: {missing}")

    def test_specification_identifies_local_self_hosting_goal(self):
        text = SPEC.read_text(encoding="utf-8").lower()
        for phrase in ("self-hosted", "local", "data never leaves"):
            self.assertIn(phrase, text)


if __name__ == "__main__":
    unittest.main()
