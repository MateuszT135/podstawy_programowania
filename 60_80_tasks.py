#THIRD 20
#1. Write a Python script to sort (ascending and descending)   1

import operator

d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}

print('Original dictionary : ',d)

sorted_d = sorted(d.items(), key=operator.itemgetter(1))
print('Dictionary in ascending order by value : ',sorted_d)


sorted_d = dict( sorted(d.items(), key=operator.itemgetter(1), reverse=True))
print('Dictionary in descending order by value : ',sorted_d)

#2. Write a Python program to iterate over dictionaries using for loops.   5

d = {'x': 10, 'y': 20, 'z': 30}

for dict_key, dict_value in d.items():
    print(dict_key, '->', dict_value)

#3. Write a Python program to sum all the items in a dictionary.  10

my_dict = {'data1': 100, 'data2': -54, 'data3': 247}
result = sum(my_dict.values())
print(result)

#4. Write a Python program to print a dictionary in table format.  25

my_dict = {'C1': [1, 2, 3], 'C2': [5, 6, 7], 'C3': [9, 10, 11]}

for row in zip(*([key] + (value) for key, value in sorted(my_dict.items()))):
    print(*row)

#5. Write a Python program to convert a list into a nested dictionary of keys.   27

num_list = [1, 2, 3, 4]

new_dict = current = {}

for name in num_list:
    current[name] = {}
    current = current[name]

print(new_dict)

#6. Write a Python programto print a dictionary line by line.  32

students = {'Aex': {'class': 'V', 'roll_id': 2}, 'Puja': {'class': 'V', 'roll_id': 3}}

for a in students:
    print(a)
    for b in students[a]:
        print(b, ':', students[a][b])

#7. Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are the square of the keys. 7

d = dict()

for x in range(1, 16):
    d[x] = x ** 2

print(d)

#8. Write a Python script to check whether a given key already exists in a dictionary. 4

d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

def is_key_present(x):
    if x in d:
        print('Key is present in the dictionary')
    else:
        print('Key is not present in the dictionary')

is_key_present(5)
is_key_present(9)

#9. Write a Python script to concatenate the following dictionaries to create a new one.

dict1 = {1: 10, 2: 20}
dict2 = {3: 30, 4: 40}
dict3 = {5: 50, 6: 60}

dict4 = {}

for d in (dict1, dict2, dict3):
    dict4.update(d)

print(dict4)

#10. Write a Python program to sort a given dictionary by key.  14

color_dict = {'red': '#FF0000', 'green': '#008000', 'black': '#000000', 'white': '#FFFFFF'}

for key in sorted(color_dict):
    print("%s: %s" % (key, color_dict[key]))

#11. Write a Python program to add a key to a dictionary. 2

d = {0: 10, 1: 20}
print(d)

d.update({2: 30})
print(d)

#12. Write a Python program to sort a list alphabetically in a dictionary.  28

num = {'n1': [2, 3, 1], 'n2': [5, 1, 2], 'n3': [3, 2, 4]}

sorted_dict = {x: sorted(y) for x, y in num.items()}
print(sorted_dict)

#13. Write a Python program to sort Counter by value.

from collections import Counter

x = Counter({'Tomato': 12, 'Beetroot': 21, 'Potato': 37})

print(x.most_common())

#14. Write a Python program to filter a dictionary based on values.

price = {'Deus Ex': 45, 'Infamous': 50, 'Company of Heroes': 55, 'Command & Conquer': 90}

print("Original Dictionary:")
print(price)

print("Game price greater than 90:")

result = {key: value for (key, value) in price.items() if value >= 90}

print(result)

#15. Write a Python program to find the key of the maximum calue in a disctionary. 80

def test(d):
    return max(d, key=d.get), min(d, key=d.get)

games = {'Max Payne': 19,  "Assassin'S Creed": 22, 'Killzone': 21, 'Bioshock': 20}

print("\nOriginal dictionary elements:")
print(games)

print("\nFinds the key of the maximum and minimum value of the said dictionary:")
print(test(games))

#16. Write a Python program to create a flat list of all the values in a flat dictionary. 79

def test(flat_dict):
    return list(flat_dict.values())

games = {'Mario': 12, 'Zelda': 43, 'Batman': 21, 'Sekiro': 19}

print("\nOriginal dictionary elements:")
print(games)

print("\nFlat list of all the values of the said flat dictionary:")
print(test(games))

#17. Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).  6

n = int(input("Input a number "))
d = dict()

for x in range(1, n + 1):
    d[x] = x * x

print(d)

#18. Write a Python script to merge two Python dictionaries. 8

d1 = {'a': 100, 'b': 200}
d2 = {'x': 300, 'y': 200}

d = d1.copy()
d.update(d2)

print(d)

#19. Write a Python program to create and display all combinations of letters, selecting each letter from a different key in a dictionary. 21

import itertools

d = {'1': ['a', 'b'], '2': ['c', 'd']}

for combo in itertools.product(*[d[k] for k in sorted(d.keys())]):
    print(''.join(combo))

#20. Write a Python program to count the values associated with a key in a dictionary.

games = [{'id': 1, 'accomplished': True, 'title': 'Terraria'},
 {'id': 2, 'accomplished': False, 'title': 'Minecraft'},
 {'id': 3, 'accomplished': True, 'title': 'Hurtworld'}]

print(sum(d['id'] for d in games))
print(sum(d['accomplished'] for d in games))
