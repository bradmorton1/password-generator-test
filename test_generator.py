import unittest
import generator

class TestGenerator(unittest.TestCase):

    def test_is_repeating_with_repeated_characters(self):
        repeated_password = "abccdefgh"
        self.assertEqual(generator.is_repeating(repeated_password), True)

    def test_is_repeating_with_unique_characters(self):
        unique_password = "abcdefghi"
        self.assertEqual(generator.is_repeating(unique_password), False)

    def test_generate_random_number_for_each_sequence(self):
        #TODO

    def test_generate_random_password(self):
        #TODO

if __name__ == '__main__':
    unittest.main()
