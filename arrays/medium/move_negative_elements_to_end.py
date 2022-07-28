
"""
@TODO :
Given an unsorted array arr[] of size N having both negative and positive integers,
the task is place all negative element at the end of array without changing the order of positive element and negative element.

For example:
arr[] = [1, -1, 3, 2, -7, -5, 11, 6 ]
Output : [1, 3, 2, 11, 6, -1, -7, -5]
"""


def move_all_negatives_to_end(arr):
    print("Original Array : ", arr)
    positive = list()
    negative = list()
    for i in range(len(arr)):
        if arr[i] < 1:
            negative.append(arr[i])
        else:
            positive.append(arr[i])
    arr = arr.clear()
    arr = positive + negative
    del positive, negative
    print("New Array : ", arr)
    return arr


if __name__ == "__main__":
    arr_1 = [-5, 7, -3, -4, 9, 10, -1, 11]
    move_all_negatives_to_end(arr_1)

# Original Array :  [-5, 7, -3, -4, 9, 10, -1, 11]
# New Array :  [7, 9, 10, 11, -5, -3, -4, -1]

