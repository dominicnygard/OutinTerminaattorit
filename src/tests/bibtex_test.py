import unittest

from util import to_bibtex


class TestBibtexUtilities(unittest.TestCase):

    def test_to_bibtex_includes_only_present_fields(self):
        reference = {
            "id": 42,
            "type": "article",
            "title": "BibTex testi",
            "author": "Testi Testinen",
            "year": "2024",
            "journal": "Testing",
            "notes": "",
        }

        result = to_bibtex(reference)

        self.assertIn("@article", result)
        self.assertIn("title = {BibTex testi}", result)
        self.assertNotIn("notes", result)

if __name__ == "__main__":
    unittest.main()
