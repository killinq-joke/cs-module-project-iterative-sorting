import math


def linear_search(arr, target):
    # Your code here
    for i in range(0, len(arr)):
        if arr[i] == target:
            return i

    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    # Your code here
    mid = math.ceil(len(arr) / 2)
    print(arr[mid])
    while arr[mid] != target:
        if arr[mid] > target:

            mid = math.ceil(mid / 2)
            print(mid)
        else:
            mid += math.ceil(mid / 2)

    return mid or -1  # not found


arr1 = [-9, -8, -6, -4, -3, -2, 0, 1, 2, 3, 5, 7, 8, 9]
print(binary_search(arr1, -4))
