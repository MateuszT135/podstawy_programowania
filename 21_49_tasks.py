#First 21 exercises
#1. Write a Python function to find the maximum of three numbers.

def max_of_two(x, y):
    if x > y:
        return x
    return y

def max_of_three(x, y, z):
    return max_of_two(x, max_of_two(y, z))

print(max_of_three(5, -3, 1))

#2. Write a Python function to sum all the numbers in a list.

def sum(numbers):
    total = 0
    for x in numbers:
        total += x
    return total

print(sum((8, 2, 3, 0, 7)))

#3. Write a Python function to multiply all the numbers in a list.

def multiply(numbers):
    total = 1
    for x in numbers:
        total *= x
    return total

print(multiply((8, 2, 3, -1, 7)))

#4. Write a Python program to reverse a string.

def string_reverse(str1):
    rstr1 = ''
    index = len(str1)
    while index > 0:
        rstr1 += str1[index - 1]
        index = index - 1
    return rstr1

print(string_reverse('1234abcd'))

#5. Write a Python function to calculate the factorial of a number (a non-negative integer). The function accepts the number as an argument.

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

n = int(input("Input a number to compute the factorial: "))

print(factorial(n))

#6. Write a Python function to check whether a number falls within a given range.

def test_range(n):
    if n in range(3, 9):
        print("%s is in the range" % str(n))
    else:
        print("The number is outside the given range.")
test_range(n)

#7. Write a Python function that accepts a string and count the number of upper and lower case letters.

def string_test(s):
    d = {"UPPER_CASE": 0, "LOWER_CASE": 0}

    for c in s:
        if c.isupper():
            d["UPPER_CASE"] += 1
        elif c.islower():
            d["LOWER_CASE"] += 1
        else:
            pass

    print(f"Original String: {s}")
    print("No. of Upper case characters: ", d["UPPER_CASE"])
    print("No. of Lower case Characters: ", d["LOWER_CASE"])

word = input("Type a word: ")
string_test(word)

#8. Write a Python function that takes a list and returns a new list with distinct elements from the first list.

def unique_list(l):
    x = []
    for a in l:
        if a not in x:
            x.append(a)
    return x

print(unique_list([1, 2, 3, 3, 3, 3, 4, 5]))

#9. Write a Python function that takes a number as a parameter and checks whether the number is prime or not.

def test_prime(n):
    if (n == 1):
        return False
    elif (n == 2):
        return True
    else:
        for x in range(2, n):
            if (n % x == 0):
                return False
        return True

print(test_prime(9))

#10. Write a Python program to print the even numbers from a given list.

def is_even_num(l):
    enum = []

    for n in l:
        if n % 2 == 0:
            enum.append(n)
    return enum

print(is_even_num([1, 2, 3, 4, 5, 6, 7, 8, 9]))

#11. Write a Python function to check whether a number is “Perfect” or not.

def perfect_number(n):
    sum = 0
    for x in range(1, n):
        if n % x == 0:
            sum += x
    return sum == n

num = int(input("Type a number: "))
print(perfect_number(num))

#12. Write a Python function that checks whether a passed string is a palindrome or not.

def isPalindrome(string):
    left_pos = 0
    right_pos = len(string) - 1

    while right_pos >= left_pos:
        if not string[left_pos] == string[right_pos]:
            return False
        left_pos += 1
        right_pos -= 1
    return True

word = input("Type a word: ")
print(isPalindrome(word))

#13. Write a Python function that prints out the first n rows of Pascal’s triangle.

def pascal_triangle(n):
    trow = [1]
    y = [0]
    for x in range(max(n, 0)):
        print(trow)
        trow = [l + r for l, r in zip(trow + y, y + trow)]
    return n >= 1

pascal_triangle(6)

#14. Write a Python function to check whether a string is a pangram or not.

import string
import sys

def ispangram(str1, alphabet=string.ascii_lowercase):
    alphaset = set(alphabet)
    str_set = set(str1.lower())
    return alphaset <= str_set

print(ispangram('The quick brown fox jumps over the lazy dog'))

#15. Write a Python program that accepts a hyphen-separated sequence of words as input and prints the words in a hyphen-separated sequence after sorting them alphabetically.

items = [n for n in input().split('-')]
items.sort()

print('-'.join(items))

#16. Write a Python function to create and print a list where the calues are the squares of numbers between 1 and 30 (both included).

def printValues():
    l = list()
    for i in range(1, 21):
        l.append(i**2)
    print(l)

printValues()

#17. Write a Python program to create a chain of function decorators (bold, italic, underline etc.).


def make_bold(fn):
    def wrapped():
        return "<b>" + fn() + "</b>"
    return wrapped

def make_italic(fn):
    def wrapped():
        return "<i>" + fn() + "</i>"
    return wrapped

def make_underline(fn):
    def wrapped():
        return "<u>" + fn() + "</u>"
    return wrapped

@make_bold
@make_italic
@make_underline
def hello():
    return "hello world"

print(hello())

#18. Write a Python program to execute a string containing Python code.

mycode = 'print("hello world")'

code = """
def mutiply(x,y):
    return x*y
print('Multiply of 2 and 3 is: ',mutiply(2,3))
"""

exec(mycode)
exec(code)

#19. Write a Python program to access a function inside a function.

def test(a):
    def add(b):
        nonlocal a
        a += 1
        return a + b

    return add

func = test(4)

print(func(4))

#20. White a Python program to detect the number of local variables declared in a function.

def abc():
    x = 1
    y = 4
    str1 = "python_code"
    print("Hello World!")
print(abc.__code__.co_nlocals)

#21. Write a Python program that invokes a function after a specified period of time.

from time import sleep
import math

def delay(fn, ms, *args):
    sleep(ms / 1000)
    return fn(*args)

print("Square root after specific milliseconds:")
print(delay(lambda x: math.sqrt(x), 100, 16))
print(delay(lambda x: math.sqrt(x), 1000, 100))

print(delay(lambda x: math.sqrt(x), 2000, 25100))
