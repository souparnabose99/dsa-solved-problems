

"""
@TODO:
Given an array a[] of size N which contains elements from 0 to N-1,
you need to find all the elements occurring more than once in the given array.

For example:
N = 5, A = [2, 3, 1, 2, 3], Output: 2, 3
"""


def find_duplicates(arr):
    dup_arr = list()
    for i in range(len(arr)):
        if arr.count(i) > 1:
            dup_arr.append(i)
    if len(dup_arr) > 1:
        return dup_arr
    else:
        return -1


if __name__ == "__main__":
    arr_1 = [1, 2, 3]
    print("Original array : ", arr_1)
    arr_2 = find_duplicates(arr_1)
    print("Array with duplicates : ", arr_2)


# Original array :  [2, 3, 1, 2, 3]
# Array with duplicates :  [2, 3]
# Original array :  [1, 2, 3]
# Array with duplicates :  -1


