

"""
@TODO:
Given an array Arr[] of N integers.
Find the contiguous sub-array(containing at least one number) which has the maximum sum and return its sum.
For example:
Arr[] = [1,2,3,-2,5], Output:9
"""


def find_contiguous_sub_arr(arr):
    max_sum = 0
    temp_sum = 0
    for i in range(len(arr)):
        temp_sum = max_sum + arr[i]

        if temp_sum > max_sum:
            max_sum = temp_sum
    pass


if __name__ == "__main__":
    arr1 = [1, 2, 3, -2, 15, -7, 1]
    find_contiguous_sub_arr(arr1)


