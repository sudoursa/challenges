# Merge Sorted Arrays
#
# Write a program that reads two sorted arrays from the user input, merges them into the third array and
# outputs the result. Arrays are sorted in ascending order. For example, the result of
# merging [1, 5, 8, 9] and [2, 3, 3, 14] is [1, 2, 3, 3, 5, 8, 9, 14].
#
# For example:
# Input:
# 1, 2, 3, 4
# 1, 1, 1, 42
# Output:
# 1, 1, 1, 1, 2, 3, 4, 42
#
# Input:
# 25, 55
# 1, 3, 94
# Output:
# 1, 3, 25, 55, 94
#
# bonus: Modify the program to sort arrays before merging.


def get_user_input():
    user_entry = input("Enter a sorted list of numbers separated by commas: ")
    int_mapping = map(int, user_entry.split(','))
    return list(int_mapping)


def merge_arrays(func1, func2):
    array1 = func1
    array2 = func2
    combined_array = sorted(array1 + array2)
    return combined_array


if __name__ == '__main__':
    array = merge_arrays(get_user_input(), get_user_input())
    print(array)
