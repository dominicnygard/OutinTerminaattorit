import unittest
from util import validate_field, UserInputError

class TestFieldValidation(unittest.TestCase):
    def setUp(self):
        pass

    def test_valid_length_does_not_raise_error(self):
        validate_field("juokse")
        validate_field("a" * 100)

    def test_too_short_or_long_raises_error(self):
        with self.assertRaises(UserInputError):
            validate_field("ole")

        with self.assertRaises(UserInputError):
            validate_field("koodaa" * 20)



# test creating??
# test input validation