import unittest
from src import input_validation


class TestTitleValidation(unittest.TestCase):
    def test_valid_title_length_does_not_raise_error(self):
        self.assertIsNone(input_validation.validate_title("This title is valid"))

    def test_too_short_title_raises_error(self):
        self.assertIsNotNone(input_validation.validate_title("n"))

    def test_too_long_title_raises_error(self):
        long_title = 'n'*251
        self.assertIsNotNone(input_validation.validate_title(long_title))

class TestAuthorValidation(unittest.TestCase):
    def test_valid_author_does_not_raise_error(self):
        self.assertIsNone(input_validation.validate_author("Arttu Artikkeli"))

    def test_author_with_invalid_characters_raises_error(self):
        self.assertIsNotNone(input_validation.validate_author("Arttu Artikkeli1"))

    def test_too_short_author_raises_error(self):
        self.assertIsNotNone(input_validation.validate_author("A"))

    def test_too_long_text_raises_error(self):
        long_author = 'n'*251
        self.assertIsNotNone(input_validation.validate_author(long_author))


class TestTextValidation(unittest.TestCase):
    def test_valid_text_length_does_not_raise_error(self):
        self.assertIsNone(input_validation.validate_text("This is the third article I needed for my writing work."))

    def test_too_short_text_raises_error(self):
        self.assertIsNotNone(input_validation.validate_text("T"))

    def test_too_long_text_raises_error(self):
        long_text = 'n'*251
        self.assertIsNotNone(input_validation.validate_text(long_text))


class TestYearValidation(unittest.TestCase):
    def test_valid_year_does_not_raise_error(self):
        self.assertIsNone(input_validation.validate_year("2000"))

    def test_too_short_year_raises_error(self):
        self.assertIsNotNone(input_validation.validate_year("200"))

    def test_too_long_year_raises_error(self):
        self.assertIsNotNone(input_validation.validate_year("20000"))
    
    def test_less_than_range_year_raises_error(self):
        self.assertIsNotNone(input_validation.validate_year("1800"))

    def test_more_than_range_year_raises_error(self):
        self.assertIsNotNone(input_validation.validate_year("3000"))


class TestMonthValidation(unittest.TestCase):
    def test_valid_month_does_not_raise_error(self):
        self.assertIsNone(input_validation.validate_month("jan"))

    def test_invalid_month_raises_error(self):
        self.assertIsNotNone(input_validation.validate_month("january"))

    def test_numeric_month_raises_error(self):
        self.assertIsNotNone(input_validation.validate_month("11"))


class TestPagesValidation(unittest.TestCase):
    def test_valid_one_page_does_not_raise_error(self):
        self.assertIsNone(input_validation.validate_pages("22"))
    
    def test_valid_page_range_does_not_raise_error(self):
        self.assertIsNone(input_validation.validate_pages("22--24"))

    def test_valid_many_page_ranges_does_not_raise_error(self):
        self.assertIsNone(input_validation.validate_pages("22--24,26--28"))

    def test_invalid_page_range_raises_error(self):
        self.assertIsNotNone(input_validation.validate_pages("22-24"))

    def test_letter_range_raises_error(self):
        self.assertIsNotNone(input_validation.validate_pages("ab-cd"))


class TestIntegerValidation(unittest.TestCase):
    def test_valid_integer_does_not_raise_error(self):
        self.assertIsNone(input_validation.validate_integer(20))

    def test_non_integer_raises_error(self):
        self.assertIsNotNone(input_validation.validate_integer("kaksi"))


if __name__ == "__main__":
    unittest.main()
