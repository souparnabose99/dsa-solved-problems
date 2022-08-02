
"""
@TODO:
Given two arrays a[] and b[] of size n and m respectively. The task is to find union between these two arrays.
Union of the two arrays can be defined as the set containing distinct elements from both the arrays.
If there are repetitions, then only one occurrence of element should be printed in the union.

For example:
Input: 6, 2; [85, 25, 1, 32, 54, 6], [85, 2]
Output:
7 (Count of no of elements)
"""


def union_of_2_arrays(arr1, arr2):

    if len(arr1) > len(arr2):
        for i in range(len(arr1)):
            if arr1[i] not in arr2:
                arr2.append(arr1[i])
        arr2 = set(arr2)
        return len(arr2)
    else:
        for i in range(len(arr2)):
            if arr2[i] not in arr1:
                arr1.append(arr2[i])
        arr2 = set(arr1)
        return len(arr1)


if __name__ == "__main__":
    arr_1 = [85, 25, 1, 32, 54, 6, 44]
    arr_2 = [85, 2, 3]
    count = union_of_2_arrays(arr_1, arr_2)
    print("Count of elements after union : ", count)



