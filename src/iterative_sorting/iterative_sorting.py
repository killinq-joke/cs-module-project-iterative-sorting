# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for base in range(0, len(arr) - 1):
        for i in range(0, len(arr) - base):
            cur_index = i + base
            smallest_index = arr[base]
            # TO-DO: find next smallest element
            # (hint, can do in 3 loc)
            # Your code here
            if arr[cur_index] < smallest_index:
                smallest_index = arr[cur_index]
                arr[cur_index] = arr[base]
                arr[base] = smallest_index
        base += 1

        # TO-DO: swap
        # Your code here
    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # Your code here
    for base in range(0, len(arr) - 1):
        for i in range(1, len(arr) - base):
            if arr[i] < arr[i - 1]:
                smallest = arr[i]
                arr[i] = arr[i - 1]
                arr[i - 1] = smallest

        base += 1

    return arr


'''
STRETCH: implement the Counting Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''


def counting_sort(arr, maximum=None):
    # Your code here

    count = [0 for i in range(0, maximum + 1)]
    result = [0 for i in range(0, len(arr))]

    for i in range(0, len(arr)):
        count[arr[i]] += 1

    for i in range(0, len(count) - 1):
        count[i + 1] = count[i] + count[i + 1]

    for o in range(0, len(arr)):
        result[count[arr[o]] - 1] = arr[o]
        count[arr[o]] -= 1

    return result


arr1 = [1, 5, 8, 9, 2, 9, 6, 0, 3, 7]
print(counting_sort(arr1, 9))
