# Some simple functions to demo the usage

#def add_numbers(a, b):
#    return a + b

def addition(a, b):
    return a*b

def is_even(number):
    return number % 2 == 0

def concatenate_strings(s1, s2):
    return s1 + s2

def find_max(numbers):
    if not numbers:
        return None
    return max(numbers)

def factorial(n):
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def is_palindrome(s):
    return s == s[::-1]
