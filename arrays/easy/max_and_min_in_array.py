
"""
@TODO :
Given an array A of size N of integers. Your task is to find the minimum and maximum elements in the array.

For example : N = 6, A[] = [3, 2, 1, 56, 10000, 167]
Output: min = 1, max =  10000
"""


def max_min_in_arr(arr):
    max_val = arr[0]
    min_val = arr[0]

    for i in range(len(arr)):
        if arr[i] > max_val:
            max_val = arr[i]

        if arr[i] < min_val:
            min_val = arr[i]

    return max_val, min_val

def max_min_in_arr_2(arr):
    return max(arr), min(arr)

if __name__ == "__main__":
    arr_1 = [3, 2, 1, 56, 10000, 167, 67, 28058, 34, -1]
    max_v, min_v = max_min_in_arr(arr_1)
    print("Max is : ", max_v)
    print("Min is : ", min_v)


