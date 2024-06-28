#Second 20

#1. Write a Python program to sum all the items in a list.]


def sum_list(items):
    sum_numbers = 0
    for x in items:
        sum_numbers += x
    return sum_numbers

print(sum_list([3, -4, 4]))

#2. Write a Python program to multiply all the items in a list.

def multiply_list(items):
    tot = 1
    for x in items:
        tot *= x
    return tot

print(multiply_list([6, 9, -7]))

#3. Write a Python program to clone or copy a list.

original_list = [5, 21, 42, 76, 1]

new_list = list(original_list)

print(original_list)

print(new_list)

#4. Write a Python program to calculate the difference between the two lists.

list1 = [1, 3, 5, 7, 9]

list2 = [1, 2, 4, 6, 7, 8]

diff_list1_list2 = list(set(list1) - set(list2))
diff_list2_list1 = list(set(list2) - set(list1))

total_diff = diff_list1_list2 + diff_list2_list1

print(total_diff)

#5. Write a Python program to check if a list is empty or not.

list = []

if not list:
    print("List is empty")
elif list:
    print("List is not empty")

#6. Write a Python program to clone or copy a list.

original = [12, 21, 37, 23, 4]

new = list(original)

print(original)

print(new)

#7. Write a Python program to print the numbers of a specified list after removing even numbers from it.

num = [7, 8, 120, 25, 44, 20, 27]

num = [x for x in num if x % 2 != 0]

print(num)

#8. Write a Python programto access the index of a list.

nums = [3, 21, 37, 4, 67]
for num_index, num_val in enumerate(nums):
    print(num_index, num_val)

#9. Write a Python program to get the frequency of elements in a list.

import collections

my_list = [10, 10, 10, 10, 20, 20, 20, 20, 40, 40, 50, 50, 30]

print("Original List : ", my_list)

ctr = collections.Counter(my_list)

print(f"Frequency of the elements in the List : {ctr}")

#10. Write a Python program to find common items in two lists.

list1 = "Potato", "Tomato", "Onion", "Garlic"

list2 = "Garlic", "Cucumber", "Potato", "Beetroot"

print(set(list1) & set(list2))

#11. Write a Python program to iterate over two lists simultaneously.

num = [1, 2, 3, 4]
veg = ['potato', 'beetroot', 'onion', 'tomato']

for (a, b) in zip(num, veg):
    print(a, b)

#12. Write a Python program to extract common index elements from more than one given list.

def extract_index_ele(l1, l2, l3):
    result = []
    for m, n, o in zip(l1, l2, l3):
        if (m == n == o):
            result.append(m)
    return result

nums1 = [1, 1, 3, 4, 5, 6, 7]
nums2 = [0, 1, 2, 3, 4, 5, 7]
nums3 = [0, 1, 2, 3, 4, 5, 7]

print("Original lists:")
print(nums1)
print(nums2)
print(nums3)

print("\nCommon index elements of the said lists:")

print(extract_index_ele(nums1, nums2, nums3))

#13. Write a Python program to count integers in a given mixed list.

def count_integer(list1):
    ctr = 0
    for i in list1:
        if isinstance(i, int):
            ctr = ctr + 1
    return ctr

list1 = [1, 'krem', 3, 1.2, 4, 'kanapka', 5, 'sosiwo', 7, -5, -23.21]

print("Original list:")
print(list1)

print("\nNumber of integers in the said mixed list:")

print(count_integer(list1))

#14. Write a Python program to convert a list of characters into a string.


s = ['a', 'b', 'c', 'd']

str1 = ''.join(s)

print(str1)

#15. Write a Python program to select an item randomly from a list.

import random
veg = ['Potato', 'Tomato', 'Onion', 'Garlic', 'Beetroot']

print(random.choice(veg))

#16. Write a Python program to find the second smallest number in a list.

def second_smallest(numbers):
    if len(numbers) < 2:
        return
    if len(numbers) == 2 and numbers[0] == numbers[1]:
        return

    dup_items = set()
    uniq_items = []

    for x in numbers:
        if x not in dup_items:
            uniq_items.append(x)
            dup_items.add(x)
    uniq_items.sort()
    return uniq_items[1]

print(second_smallest([1, 2, -8, -2, 0, -2]))
print(second_smallest([1, 1, 0, 0, 2, -2, -2]))
print(second_smallest([1, 1, 1, 0, 0, 0, 2, -2, -2]))
print(second_smallest([2, 2]))
print(second_smallest([2]))

#17. Write a Python function that takes two lists and returns True if they have at least one common member.

def common_data(list1, list2):
    result = False

    for x in list1:
        for y in list2:
            if x == y:
                result = True
                return result

print(common_data([1, 2, 3, 4, 5], [5, 6, 7, 8, 9]))
print(common_data([1, 2, 3, 4, 5], [6, 7, 8, 9]))

#18. Write a Python program to check whether two lists are circularly identical.

list1 = [10, 10, 0, 0, 10]
list2 = [10, 10, 10, 0, 0]
list3 = [1, 10, 10, 0, 0]

print('Compare list1 and list2')
print(' '.join(map(str, list2)) in ' '.join(map(str, list1 * 2)))
print('Compare list1 and list3')
print(' '.join(map(str, list3)) in ' '.join(map(str, list1 * 2)))

#19. Write a Python program to get a variable with an identification number of a string.

x = 100
print(format(id(x), 'x'))

s = 'mortalkombat'
print(format(id(s), 'x'))

#20. Write a Python program to convert a pair of values into a sorted unique array.

L = [(1, 2), (3, 4), (1, 2), (5, 6), (7, 8), (1, 2), (3, 4), (3, 4), (7, 8), (9, 10)]

print("Original List: ", L)
print("Sorted Unique Data:", sorted(set().union(*L)))
