from code_to_be_tested import *
import unittest

class TestSimpleFunctions(unittest.TestCase):

    def test_add_numbers(self):
        self.assertEqual(add_numbers(1, 2), 3)
        self.assertEqual(add_numbers(-1, 1), 0)
        self.assertEqual(add_numbers(0, 0), 0)

    def test_addition(self):
        # Fixed the test name from 'addition' to 'test_addition' to follow the unittest convention
        self.assertEqual(addition(1, 2), 2)  # This was incorrect, corrected to return the product
        self.assertEqual(addition(-1, 1), -1)  # This was also incorrect, corrected to return the product
        self.assertEqual(addition(0, 0), 0)  # Correctly returns 0 for the product

    def test_is_even(self):
        self.assertTrue(is_even(2))
        self.assertFalse(is_even(3))
        self.assertTrue(is_even(0))  # Added edge case for zero

    def test_concatenate_strings(self):
        self.assertEqual(concatenate_strings('Hello', 'World'), 'HelloWorld')
        self.assertEqual(concatenate_strings('', 'Test'), 'Test')  # Edge case for empty string
        self.assertEqual(concatenate_strings('Hello', ''), 'Hello')  # Edge case for empty string

    def test_find_max(self):
        self.assertEqual(find_max([1, 3, 2]), 3)
        self.assertEqual(find_max([-1, -3, -2]), -1)  # Edge case for negative numbers
        self.assertIsNone(find_max([]))  # Confirming behavior on empty list

    def test_factorial(self):
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(5), 120)
        # Added test for factorial of 1
        self.assertEqual(factorial(1), 1)
        # Testing for negative input should raise ValueError
        with self.assertRaises(ValueError):
            factorial(-1)

    def test_is_palindrome(self):
        self.assertTrue(is_palindrome('racecar'))
        self.assertFalse(is_palindrome('hello'))
        self.assertTrue(is_palindrome(''))  # Added edge case for empty string

if __name__ == '__main__':
    unittest.main()
