#Python Exception Handling
#1. Write a Python program to handle a ZeroDivision Error exception when dividing a number by zero.

def divide_numbers(x, y):
    try:
        result = x / y
        # Print the result of the division.
        print("Result:", result)
    except ZeroDivisionError:
        print("The division by zero operation is not allowed.")


numerator = 100
denominator = 0
divide_numbers(numerator, denominator)

#2. Write a Python program that prompts the user to input an integer and raises a ValueError exception if the input is not a valid integer.

def get_integer_input(prompt):
    try:
        value = int(input(prompt))
        return value
    except ValueError:
        print("Error: Invalid input, input a valid integer.")

n = get_integer_input("Input an integer: ")
print("Input value:", n)

#3. Write a Python program that opens a file and handles a FileNotFoundError exception if the file does not exist.

def open_file(filename):
    try:
        file = open(filename, 'r')
        contents = file.read()
        print("File contents:")
        print(contents)
        file.close()
    except FileNotFoundError:
        print("Error: File not found.")

file_name = input("Input a file name: ")
open_file(file_name)

#4. Write a Python program that prompts the user to input two numbers and raises a TypeError exception if the inputs are not numerical.

def get_numeric_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Error: Invalid input. Please Input a valid number.")

n1 = get_numeric_input("Input the first number: ")
n2 = get_numeric_input("Input the second number: ")
result = n1 * n2
print("Product of the said two numbers:", result)

#5. Write a Python program that opens a file and handles a PermissionError exception if there is a permission issue.

def open_file(file_name):
    try:
        with open(file_name, 'w') as file:
            contents = file.read()
            print("File contents:")
            print(contents)
    except PermissionError:
      print("Error: Permission denied to open the file.")

file_name = input("Input a file name: ")
open_file(file_name)

#6. Write a Python program that executes an operation on a list and handles an IndexError exception if the index is out of range.

def test_index(data, index):
    try:
        result = data[index]
        print("Result:", result)
    except IndexError:
        print("Error: Index out of range.")

nums = [1, 2, 3, 4, 5, 6, 7]
index = int(input("Input the index: "))
test_index(nums, index)

#7. Write a Python program that prompts the user to input a number and handles a KeyboardInterrupt exception if the user cancels the input.

#8. Write a Python program that executes division and handles an Arithmetic Error exception if there is an arithmetic error.

def division(dividend, divisor):
    try:
        result = dividend / divisor
        print("Result:", result)
    except ArithmeticError:
        print("Error: Arithmetic error occurred!")

dividend = float(input("Input the dividend: "))
divisor = float(input("Input the divisor: "))
division(dividend, divisor)

#9. Write a Python program that opens a file and handles a UnicodeDecodeError exception if there is an encoding issue.

def open_file(filename):
    encoding = input("Input the encoding (ASCII, UTF-16, UTF-8) for the file: ")
    try:
        with open(filename, 'r', encoding=encoding) as file:
            contents = file.read()
            print("File contents:")
            print(contents)
    except UnicodeDecodeError:
        print("Error: Encoding issue occurred while reading the file.")


file_name = input("Input the file name: ")
open_file(file_name)

#10. Write a Python program that executes a list operation and handles and AttributeError exception if the attribiute does not exist.
