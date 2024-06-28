#FOURTH 20
#1. Write a Python program to find those numbers which are divisible by 7 and multiples of 5, between 1500 and 2700 (both included).  1


emlist = []

for x in range(1500, 2701):
    if (x % 7 == 0) and (x % 5 == 0):
        emlist.append(str(x))

print(','.join(emlist))

#2. Write a Python program to convert temperatures to and from Celsius and Fahrenheit. 2

temp = input("Input the temperature you like to convert? (e.g., 45F, 102C etc.) : ")

degree = int(temp[:-1])
i_convention = temp[-1]

if i_convention.upper() == "C":
    result = int(round((9 * degree) / 5 + 32))
    o_convention = "Fahrenheit"
elif i_convention.upper() == "F":
    result = int(round((degree - 32) * 5 / 9))
    o_convention = "Celsius"
else:
    print("Input proper convention.")
    quit()

print("The temperature in", o_convention, "is", result, "degrees.")

#3. Write a Python program that accepts a word from the user and reverses it.

word = input("Input a word to reverse: ")

for char in range(len(word) - 1, -1, -1):
    print(word[char], end="")

print("\n")

#4. Write a Python program that prints all the numbers from 0 to 6 except 3 and 6.

for x in range(6):
    if (x == 3 or x == 6):
        continue
    print(x, end=' ')

print("\n")

#5. Write a Python program to get the Fibonacci series between 0 and 50.

x, y = 0, 1

while y < 50:
    print(y)

    x, y = y, x + y

#6. Write a Python program that iterates through integers from 1 to 50. For each multiple of three, print “Fizz” instead of the number; for each multiple of five, print “Buzz”. For numbers that are multiples of both three and five, print “FizzBuzz”.

for fizzbuzz in range(51):
    if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
        print("fizzbuzz")
        continue
    elif fizzbuzz % 3 == 0:
        print("fizz")
        continue
    elif fizzbuzz % 5 == 0:
        print("buzz")
        continue
    print(fizzbuzz)

#7. Write a Python program that accepts a sequence of lines (blank line to terminate) as input and prints the lines as output (all characters in lower case).

lines = []

while True:
    l = input()

    if l:
        lines.append(l.upper())
    else:
        break;

for l in lines:
    print(l)

#8. Write a Python program that accepts a string and calculates the number of digits and letters.

s = input("Input a string")

d = l = 0

for c in s:
    if c.isdigit():
        d = d + 1
    elif c.isalpha():
        l = l + 1
    else:
        pass

print("Letters", l)
print("Digits", d)

#9. Write a Python program to print the alphabet pattern ‘G’.

result_str = ""

for row in range(0, 7):
    for column in range(0, 7):
        if ((column == 1 and row != 0 and row != 6) or ((row == 0 or row == 6) and column > 1 and column < 5) or (row == 3 and column > 2 and column < 6) or (column == 5 and row != 0 and row != 2 and row != 6)):
            result_str = result_str + "*"
        else:
            result_str = result_str + " "

    result_str = result_str + "\n"

print(result_str)

#10. Write a Python program to calculate a dog’s age in dog years.

h_age = int(input("Input a dog's age in human years: "))

if h_age < 0:
    print("Age must be a positive number.")
    exit()
elif h_age <= 2:
    d_age = h_age * 10.5
else:
    d_age = 21 + (h_age - 2) * 4

print("The dog's age in dog's years is", d_age)

#11. Write a Python program to check whether an alphabet is a vowel or consonant.

l = input("Input a letter of the alphabet: ")

if l in ('a', 'e', 'i', 'o', 'u'):
    print("%s is a vowel." % l)
elif l == 'y':
    print("Sometimes the letter y stands for a vowel, sometimes for a consonant.")
else:
    print("%s is a consonant." % l)

#12. Write a Python program that checks whether a string represents an integer or not.

text = input("Input a string: ")
text = text.strip()

if len(text) < 1:
    print("Input a valid text")
else:
    if all(text[i] in "0123456789" for i in range(len(text))):
        print("The string is an integer.")
    elif (text[0] in "+-") and all(text[i] in "0123456789" for i in range(1, len(text))):
        print("The string is an integer.")
    else:
        print("The string is not an integer.")

#13. Write a Python program that reads two integers representing a month and day and prints the season for that month and day.

month = input("Input the month (e.g. January, February etc.): ")
day = int(input("Input the day: "))

if month in ('January', 'February', 'March'):
    season = 'winter'
elif month in ('April', 'May', 'June'):
    season = 'spring'
elif month in ('July', 'August', 'September'):
    season = 'summer'
else:
    season = 'autumn'

if (month == 'March') and (day > 19):
    season = 'spring'
elif (month == 'June') and (day > 20):
    season = 'summer'
elif (month == 'September') and (day > 21):
    season = 'autumn'
elif (month == 'December') and (day > 20):
    season = 'winter'

print("Season is", season)

#14. Write a Python program to display the astrological sign for a given date of birth.

day = int(input("Input day of birthday: "))

month = input("Input month of birth (e.g. march, july etc): ")

if month == 'december':
    astro_sign = 'Sagittarius' if (day < 22) else 'Capricorn'
elif month == 'january':
    astro_sign = 'Capricorn' if (day < 20) else 'Aquarius'
elif month == 'february':
    astro_sign = 'Aquarius' if (day < 19) else 'Pisces'
elif month == 'march':
    astro_sign = 'Pisces' if (day < 21) else 'Aries'
elif month == 'april':
    astro_sign = 'Aries' if (day < 20) else 'Taurus'
elif month == 'may':
    astro_sign = 'Taurus' if (day < 21) else 'Gemini'
elif month == 'june':
    astro_sign = 'Gemini' if (day < 21) else 'Cancer'
elif month == 'july':
    astro_sign = 'Cancer' if (day < 23) else 'Leo'
elif month == 'august':
    astro_sign = 'Leo' if (day < 23) else 'Virgo'
elif month == 'september':
    astro_sign = 'Virgo' if (day < 23) else 'Libra'
elif month == 'october':
    astro_sign = 'Libra' if (day < 23) else 'Scorpio'
elif month == 'november':
    astro_sign = 'Scorpio' if (day < 22) else 'Sagittarius'

print("Your Astrological sign is :", astro_sign)

#15. Write a Python program to find the median of three values.

a = float(input("Input first number: "))
b = float(input("Input second number: "))
c = float(input("Input third number: "))

if a > b:
    if a < c:
        median = a
    elif b > c:
        median = b
    else:
        median = c
else:
    if a > c:
        median = a
    elif b < c:
        median = b
    else:
        median = c

print("The median is", median)

#16. Write a Python program to create the multiplication table (from 1 to 10) of  a number.

n = int(input("Input a number: "))

for i in range(1, 11):
    print(n, 'x', i, '=', n * i)

#17. Write a Python program to construct the following pattern, using a nested loop number.

for i in range(10):
    print(str(i) * i)

#18. Write a Python program to get the next day of a given date.

year = int(input("Input a year: "))

if (year % 400 == 0):
    leap_year = True
elif (year % 100 == 0):
    leap_year = False
elif (year % 4 == 0):
    leap_year = True
else:
    leap_year = False

month = int(input("Input a month [1-12]: "))

if month in (1, 3, 5, 7, 8, 10, 12):
    month_length = 31
elif month == 2:
    if leap_year:
        month_length = 29
    else:
        month_length = 28
else:
    month_length = 30

day = int(input("Input a day [1-31]: "))

if day < month_length:
    day += 1
else:
    day = 1
    if month == 12:
        month = 1
        year += 1
    else:
        month += 1

print("The next date is [yyyy-mm-dd] %d-%d-%d." % (year, month, day))

#19. Write a Python program to check if a triangle is equilateral, isosceles or scalene.

print("Input lengths of the triangle sides: ")

x = int(input("x: "))
y = int(input("y: "))
z = int(input("z: "))

if x == y == z:
    print("Equilateral triangle")
elif x == y or y == z or z == x:
    print("Isosceles triangle")
else:
    print("Scalene triangle")

#20. Write a Python program to convert a month name to a number of days.

print("List of months: January, February, March, April, May, June, July, August, September, October, November, December")
month_name = input("Input the name of Month: ")

if month_name == "February":
    print("No. of days: 28/29 days")
elif month_name in ("April", "June", "September", "November"):
    print("No. of days: 30 days")
elif month_name in ("January", "March", "May", "July", "August", "October", "December"):
    print("No. of days: 31 days")
else:
    print("Wrong month name")
