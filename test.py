import unittest
from chatbot_core import search_function, build_db, generate_answer

class TestSearchPhase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.db,cls.chunks=build_db("sample.pdf")

    def test_search_exact_match(self):
        results =search_function("Industry 4.0", self.db)
        self.assertTrue(any("industry" in r.lower() for r in results))

    def test_search_empty_query(self):
        results =search_function("", self.db)
        self.assertEqual(results, [])

    def test_generate_contains_keywords(self):
        question ="What is Industry 4.0?"
        related_keywords ={"industry", "manufacturing", "automation", "smart", "iot"}
        answer = generate_answer(question, self.db)
        self.assertTrue(
            any(k in answer.lower() for k in related_keywords),
            f"Answer did not contain any related keywords for question: {question}"
        )

    def test_generate_formatting(self):
        answer =generate_answer("Explain AI", self.db)
        self.assertTrue(len(answer) > 0 and answer[0].isupper())
        self.assertTrue(answer.endswith(".") or answer.endswith("!"))

if __name__ =="__main__":
    unittest.main(verbosity=2)