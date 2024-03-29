
"""
@TODO:
Given an array of size N-1 such that it only contains distinct integers in the range of 1 to N.
Find the missing element.

For example : A = [6,1,2,8,3,4,7,10,5]
Output: 9
"""


# O(N) runtime complexity
def find_missing_num(arr):
    for i in range(1, len(arr) +1):
        if i in arr:
            continue
        else:
            print("The missing number is : ", i)
            return i


if __name__ == "__main__":
    arr_1 = [6, 1, 2, 8, 3, 4, 7, 10, 5]
    arr_2 = [1, 2, 3, 5]
    num = find_missing_num(arr_1)
    num_2 = find_missing_num(arr_2)

    # The missing number is :  9
    # The missing number is :  4


