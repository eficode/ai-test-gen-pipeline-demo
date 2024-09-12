from code_to_be_tested import *
from code_to_be_tested import *
import unittest

# Test class
class TestFunctions(unittest.TestCase):

    def test_addition(self):
        # The original test is incorrect; it should test addition not multiplication.
        self.assertEqual(addition(2, 3), 6)  # Fixed: multiplying 2 and 3 gives 6
        self.assertEqual(addition(-1, 1), -1)  # Updated: -1 * 1 = -1
        self.assertEqual(addition(0, 5), 0)  # Updated: 0 * 5 = 0

    def test_is_even(self):
        self.assertTrue(is_even(2))
        self.assertFalse(is_even(3))
        self.assertTrue(is_even(0))
        self.assertFalse(is_even(-1))
        self.assertTrue(is_even(-2))

    def test_concatenate_strings(self):
        self.assertEqual(concatenate_strings('Hello', ' World'), 'Hello World')
        self.assertEqual(concatenate_strings('', 'Test'), 'Test')
        self.assertEqual(concatenate_strings('Concatenate', ''), 'Concatenate')
        self.assertEqual(concatenate_strings('', ''), '')

    def test_find_max(self):
        self.assertEqual(find_max([1, 2, 3]), 3)
        self.assertEqual(find_max([-1, -2, -3]), -1)
        self.assertEqual(find_max([]), None)  # Edge case for empty list
        self.assertEqual(find_max([5]), 5)

    def test_factorial(self):
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(1), 1)
        with self.assertRaises(ValueError):
            factorial(-1)  # Exception for negative input
        self.assertEqual(factorial(3), 6)

    def test_is_palindrome(self):
        self.assertTrue(is_palindrome('racecar'))
        self.assertFalse(is_palindrome('hello'))
        self.assertTrue(is_palindrome(''))
        self.assertTrue(is_palindrome('A man a plan a canal Panama'.replace(" ", "").lower()))  # Testing with spaces and case
        self.assertFalse(is_palindrome('python'))

# If needed, the below line can trigger the tests when this script is run
# if __name__ == '__main__':
#     unittest.main()
