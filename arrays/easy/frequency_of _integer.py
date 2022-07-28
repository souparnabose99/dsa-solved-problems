
"""
@TODO :
Given a vector of N positive integers and an integer X. The task is to find the frequency of X in vector.

For example:
N = 5, vector = [1, 1, 1, 1, 1], X = 1
Output: 5
"""


def frequency_count(arr, num):
    count = 0
    for i in range(len(arr)):
        if arr[i] == num:
            count += 1
    print("Frequency of Num :", num, " in ", arr, " is : ", count)
    return count


if __name__ == "__main__":
    arr_1 = [1, 29, 3, -4, 3, 7, -1, 11, 3, 12, 5, 3, 3]
    frequency_count(arr_1, 3)

# Frequency of Num : 3  in  [1, 29, 3, -4, 3, 7, -1, 11, 3, 12, 5, 3, 3]  is :  5


