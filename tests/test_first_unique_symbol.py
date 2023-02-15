import unittest
from first_unique_symbol import get_one_unique_letter


class TestUniqueLetter(unittest.TestCase):

    def test_regular_text(self):
        text = """The Tao gave birth to machine language.  Machine language gave birth to the assembler."""
        expected_result = "First unique letter is - 'm'"
        actual_result = get_one_unique_letter(text)

        self.assertEqual(expected_result, actual_result)

    def test_empty_text(self):
        with self.assertRaises(ValueError):
            get_one_unique_letter('')

    def test_no_unique(self):
        expected_result = "There is no unique letter. Try other text."
        actual_result = get_one_unique_letter('lololo, kokoko')
        self.assertEqual(expected_result, actual_result)


