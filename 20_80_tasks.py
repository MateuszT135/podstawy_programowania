#80 zadan

#first 20
#1. Write a Python program to calculate the length of a string.


def string_lenght(x):
  count = 0
  for char in x:
    count += 1
  return count
y = input("What word length u want to know: ")
print("That word length is: ")
print(string_lenght(y))

#2. Write a Python function that takes a list of words and return the longest word and the length of the longest one.

def find_longest_word(words_list):
    word_len = []

    for n in words_list:
        word_len.append((len(n), n))

    word_len.sort()

    return word_len[-1][0], word_len[-1][1]

first = input("What's the first word: ")
second = input("What's the second word: ")
third = input("What's the third word: ")
result = find_longest_word([first, second, third])

print(f"\nLongest word: {result[1]}")
print(f"Length of the longest word: {result[0]}")

#3. Write a Python program to swap cases in a given string.

def swap_case_string(word):
    result_str = ""

    for item in word:
        if item.isupper():
            result_str += item.lower()
        else:
            result_str += item.upper()

    return result_str

first = input("What word you want to swap cases in: ")
print(swap_case_string(first))

#4. Write a Python program to reverse a string.

def reverse_string(word):
    return ''.join(reversed(word))

print()

reword = input("What word u want to reverse? ")
print(reverse_string(reword))
print()

#5. Write a Python program to reverse words in a string.

def reverse_string_words(text):
  for line in text.split("\n"):
    return(" ".join(line.split()[::-1]))

    rewords = input("What words u want to reverse? ")
    print(reverse_string_words(rewords))

#6. Write a Python program to swap commas and dots in a string.

amount = "32.054,23"
maketrans = amount.maketrans
amount = amount.translate(maketrans(",.", ".,"))
print(amount)

#7. Write a Python program to convert a given strin into a list of words.

sen = input("Give me a sentence:")
print(sen.split(" "))
print(sen.split("-"))

#8. Write a Python program to count repeated characters in a string.

import collections
string = 'Konstantynopolitanczykowianeczka'
d = collections.defaultdict(int)
for c in string:
  d[c] += 1
for c in sorted(d, key=d.get, reverse=True):
  if d[c] > 1:
    print('%s %d' % (c, d[c]))

#9. Write a Python program to format a number with a percentage.

number = float(input("Type me a number: "))
percentage = number
print(f"{percentage:.2%}")

#10. Write a Python program to remove a newline in Python.

str1 = 'Hello World\n'
print(str1)
print(str1.rstrip())

#11. Write a Python script that takes input from the user and displays that input back in upper and lower cases.

user_input = input("What's your favorite fruit? ")
print(f"My favorite fruit is {user_input.upper()}")
print(f"My favorite fruit is {user_input.lower()}")

#12. Write a Python program to get a string made of the first 2 and last 2 characters of a given string. If the string lenght is less than 2, return the empty string instead.

def string_both_ends(str):
    if len(str) < 2:
        return ''
    return str[0:2] + str[-2:]

word = input("Give me a word: ")
word2 = input("Give me a word with less characters than 2: ")

print(string_both_ends(word))
print(string_both_ends(word2))

#13. Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing', add 'ly' instead. If the string length of the given string is less than 3, leave it unchanged.

def add_string(str1):
    length = len(str1)

    if length > 2:
        if str1[-3:] == 'ing':
            str1 += 'ly'
        else:
            str1 += 'ing'

    return str1

string = input("Give me a first word: ")
string2 = input("Give me a second word: ")
string3 = input("Give me a third word:  ")
print(add_string(string))
print(add_string(string2))
print(add_string(string3))

#14. Write a  Python function to insert a string in the middle of a string.

def insert_string_middle(str, word):
    return str[:2] + word + str[2:]

print(insert_string_middle('[[]]', 'Python'))
print(insert_string_middle('{{}}', 'Java'))
print(insert_string_middle('<<>>', 'c++'))

#15. Write a Python program to print the following positive and negative numbers with no decimal places.


x = 3.1415926

y = -12.9999

print()

print("Original Number: ", x)
print("Formatted Number with no decimal places: "+"{:.0f}".format(x))


print("Original Number: ", y)
print("Formatted Number with no decimal places: "+"{:.0f}".format(y))

print()

#16. Write a Python program to count the number of characters (character frequency) in a string.

def char_frequency(str1):
    dict = {}

    for n in str1:
        keys = dict.keys()

        if n in keys:
            dict[n] += 1
        else:
            dict[n] = 1
    return dict

word = input("Type a word: ")
print(char_frequency(word))

#17. Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself.

def change_char(str1):
    char = str1[0]

    str1 = str1.replace(char, '$')
    str1 = char + str1[1:]

    return str1

word = input("Type a word: ")
print(change_char(word))

#18. Write a Python program to find the first apperance of the substrings ‘not’ and ‘poor’ in a give string. If ‘not’ follows ‘poor’, replace the whole ‘not’...’poor’ substring with ‘good’. Return the resulting string.

def not_poor(str1):
    snot = str1.find('not')
    spoor = str1.find('poor')

    if spoor > snot and snot > 0 and spoor > 0:
        str1 = str1.replace(str1[snot:(spoor+4)], 'good')
        return str1
    else:
        return str1

print(not_poor("That guy is not that poor!"))
print(not_poor("That guy is poor!"))

#19. Write a Python program to change a given string to a newly string where the first and last chars have been exchanged.

def change_string(str1):
    return str1[-1:] + str1[1:-1] + str1[:1]

word = input("Type a first word: ")
word2 = input("Type a second word: ")
print(change_string(word))
print(change_string(word2))

#20. Write a Python program to remove spaces from a given string.

def remove_spaces(str1):
    str1 = str1.replace(' ', '')
    return str1

word = input("Type a word with a lot of spaces: ")
word2 = input("Type a second word with a lot of spaces: ")
print(remove_spaces(word))
print(remove_spaces(word2))
