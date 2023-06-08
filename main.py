# fruits = ["apple", "banana", "cherry", "orange"]
#
# print(fruits)
#
# fruits.append("grape")
#
# print(fruits)
#
# fruits.insert(2, "kiwi")
#
# print(fruits)
#
# print(fruits.pop())
# print(fruits.pop(1))
#
# print(fruits)
#
# fruits.append("cherry")
# print(fruits)
#
# print(fruits.index("cherry"))
# print(fruits.remove("cherry"))
# print(fruits.index("cherry"))
# print(fruits.remove("cherry"))
# # print(fruits.index("cherry"))
#
# fruits.reverse()
#
# print(fruits)

fruits = ["apple", "banana", "cherry", "orange"]
vegetables = ["carrot", "cucumber"]

grocery = fruits + vegetables
print(grocery)

numbers = [10, 5, 8, 1, 7]
numbers.sort()

print(numbers)

slice_numbers = numbers[1:4]

print(slice_numbers)

numbers_copy = numbers.copy()

print(numbers_copy)

numbers_clone = numbers[:]

print(numbers_clone)