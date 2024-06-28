#Python Unit Test
#1. Write a Python unit test program to check if a given number is prime or not.

import unittest

def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

class PrimeNumberTestCase(unittest.TestCase):
    def test_prime_numbers(self):
        prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
        print("Prime numbers:", prime_numbers)
        for number in prime_numbers:
            self.assertTrue(is_prime(number), f"{number} is not recognized as a prime number")

    def test_non_prime_numbers(self):
        non_prime_numbers = [4, 6, 8, 10, 12, 14, 16, 18, 20]
        print("Non-prime numbers:", non_prime_numbers)
        for number in non_prime_numbers:
            self.assertFalse(is_prime(number), f"{number} is incorrectly recognized as a prime number")

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(PrimeNumberTestCase)
    unittest.TextTestRunner().run(suite)

#2. Write a Python unit test program to check if a list is sorted in ascending order.

import unittest

def is_sorted_ascending(lst):
    return all(lst[i] <= lst[i+1] for i in range(len(lst)-1))

class TestSortedAscending(unittest.TestCase):
    def test_sorted_list(self):
        lst = [1, 2, 3, 4, 5, 6, 7]
        print("Sorted list: ", lst)
        # Assert that the list is sorted in ascending order.
        self.assertTrue(is_sorted_ascending(lst), "The list is not sorted in ascending order")

    def test_unsorted_list(self):
        lst = [5, 7, 2, 8, 1, 9]
        print("Unsorted list: ", lst)
        self.assertFalse(is_sorted_ascending(lst), "The list is sorted in ascending order")

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestSortedAscending)
    unittest.TextTestRunner().run(suite)

#3. Write a Python unit test program that checks if two lists are equal.

import unittest

def lists_are_equal(nums1, nums2):
    return nums1 == nums2

class TestListsEquality(unittest.TestCase):
    def test_equal_lists(self):
        nums1 = [10, 20, 30, 40]
        nums2 = [10, 20, 30, 40]
        print("\nTesting equal lists:\n", nums1, "\n", nums2)
        self.assertTrue(lists_are_equal(nums1, nums2), "The lists are not equal")

    def test_unequal_lists(self):
        nums1 = [10, 20, 30, 40]
        nums2 = [30, 20, 10, 40]
        print("\nTesting unequal lists:\n", nums1, "\n", nums2)
        self.assertFalse(lists_are_equal(nums1, nums2), "The lists are equal")

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestListsEquality)
    unittest.TextTestRunner().run(suite)

#4. Write a Python unit test program to check if a string is a palindrome.


import unittest

def is_palindrome(string):
    return string == string[::-1]

class TestPalindrome(unittest.TestCase):
    def test_palindrome_string(self):
        palindrome = "madam"
        print("Test palindrome string:", palindrome)
        self.assertTrue(is_palindrome(palindrome), f"The string '{palindrome}' is not recognized as a palindrome")

    def test_non_palindrome_string(self):
        non_palindrome = "hello"
        print("Test non-palindrome string:", non_palindrome)
        self.assertFalse(is_palindrome(non_palindrome), f"The string '{non_palindrome}' is incorrectly recognized as a palindrome")

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestPalindrome)
    unittest.TextTestRunner(verbosity=2).run(suite)

#5. Write a Python unit test program to check if a file exists in a specified directory.

import os
import unittest

def file_exists(directory, filename):
    file_path = os.path.join(directory, filename)
    return os.path.exists(file_path)

class TestFileExists(unittest.TestCase):
    def test_existing_file(self):
        directory = '/content'
        filename = 'test1.txt'
        print("Testing existing file:", os.path.join(directory, filename))
        self.assertTrue(file_exists(directory, filename), "The file does not exist in the specified directory")

    def test_nonexistent_file(self):
        directory = '/content'
        filename = 'test2.txt'
        print("Testing non-existent file:", os.path.join(directory, filename))
        self.assertFalse(file_exists(directory, filename), "The file exists in the specified directory")

with open('/content/test1.txt', 'w') as f:
    f.write('This is a test file.')

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestFileExists)
    unittest.TextTestRunner(verbosity=2).run(suite)

#6. Write a Python unit test that checks if a function handles floating-point calculations accurately.

import unittest

class TestFloatingPointCalculations(unittest.TestCase):
    def test_addition(self):
        result = 0.3 + 0.5
        self.assertAlmostEqual(result, 0.8, places=6, msg="Addition result is not as expected")

    def test_multiplication(self):
        result = 0.3 * 0.5
        self.assertAlmostEqual(result, 0.15, places=6, msg="Multiplication result is not as expected")

    def test_division(self):
        result = 0.7 / 0.3
        self.assertAlmostEqual(result, 2.333333, places=6, msg="Division result is not as expected")

def run_tests():
    suite = unittest.TestLoader().loadTestsFromTestCase(TestFloatingPointCalculations)
    unittest.TextTestRunner(verbosity=2).run(suite)

run_tests()

#7. Write a Python unit test program to check if a function handles multi_threading correctly.

import unittest
import threading

def perform_task():
    result = 0
    for i in range(1, 100000):
        result += i
    return result

class TestMultiThreading(unittest.TestCase):
    def test_multi_threading(self):
        num_threads = 10
        threads = []

        for _ in range(num_threads):
            t = threading.Thread(target=perform_task)
            threads.append(t)
            t.start()

        for t in threads:
            t.join()

        for t in threads:
            self.assertFalse(t.is_alive(), "Thread is still running")

def run_tests():
    suite = unittest.TestLoader().loadTestsFromTestCase(TestMultiThreading)
    unittest.TextTestRunner(verbosity=2).run(suite)

run_tests()

#8. Write a Python unit test program to check if a database connection is successful.

import unittest
import sqlite3

class TestDatabaseConnection(unittest.TestCase):
    def test_database_connection(self):
        conn = sqlite3.connect(':memory:')
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT 1")
            result = cursor.fetchone()
            self.assertEqual(result, (1,))
        finally:
            cursor.close()
            conn.close()

def run_tests():
    suite = unittest.TestLoader().loadTestsFromTestCase(TestDatabaseConnection)
    unittest.TextTestRunner(verbosity=2).run(suite)
run_tests()

#9. Write a Python unit test program to check if a database query returns the expected results.

import unittest
import sqlite3

class TestDatabaseQuery(unittest.TestCase):
    def setUp(self):
        self.conn = sqlite3.connect(':memory:')
        self.cursor = self.conn.cursor()
        self.cursor.execute("CREATE TABLE employees (id INTEGER PRIMARY KEY, name TEXT, salary REAL)")
        self.cursor.execute("INSERT INTO employees (name, salary) VALUES ('Ylva Guiomar', 1800.0)")
        self.cursor.execute("INSERT INTO employees (name, salary) VALUES ('Scott Gregorius', 2100.0)")
        self.conn.commit()

    def tearDown(self):
        self.cursor.close()
        self.conn.close()

    def test_database_query(self):
        self.cursor.execute("SELECT name, salary FROM employees ORDER BY name")
        results = self.cursor.fetchall()
        expected_results = [('Scott Gregorius', 2100.0), ('Ylva Guiomar', 1800.0)]
        self.assertEqual(results, expected_results)

def run_tests():
    suite = unittest.TestLoader().loadTestsFromTestCase(TestDatabaseQuery)
    unittest.TextTestRunner(verbosity=2).run(suite)

run_tests()

#10. Write a Python unit test program to check if a function correctly parses and validates input data.

import unittest

def parse_and_validate_input(data):
    if isinstance(data, str) and data.isnumeric():
        return int(data) > 0
    return False

class TestInputParsing(unittest.TestCase):
    def test_valid_input(self):
        data = "100"
        result = parse_and_validate_input(data)
        self.assertTrue(result)

    def test_invalid_input(self):
        data = "Hello"
        result = parse_and_validate_input(data)
        self.assertFalse(result)

def run_tests():
    suite = unittest.TestLoader().loadTestsFromTestCase(TestInputParsing)
    unittest.TextTestRunner(verbosity=2).run(suite)

run_tests()

