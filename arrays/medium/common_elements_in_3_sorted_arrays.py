
"""
@TODO:
Given three arrays sorted in increasing order. Find the elements that are common in all three arrays.
For example:
n1 = 6; A = [1, 5, 10, 20, 40, 80]
n2 = 5; B = [6, 7, 20, 80, 100]
n3 = 8; C = [3, 4, 15, 20, 30, 70, 80, 120]
Output: 20, 80
Explanation: 20 and 80 are the only common elements in A, B and C.

Expected Time Complexity: O(n1 + n2 + n3)
Expected Auxiliary Space: O(n1 + n2 + n3)
"""


# O(n1 + n2 + n3) runtime complexity
def find_common_elements(arr1, arr2, arr3):
    common_ele = list()
    for i in range(len(arr1)):
        if (arr1[i] in arr2 and arr1[i] in arr3) and (arr1[i] not in common_ele):
            common_ele.append(arr1[i])
        else:
            continue

    for i in range(len(arr2)):
        if (arr2[i] in arr3 and arr2[i] in arr1) and (arr2[i] not in common_ele):
            common_ele.append(arr2[i])
        else:
            continue

    for i in range(len(arr3)):
        if (arr3[i] in arr1 and arr3[i] in arr2) and (arr3[i] not in common_ele):
            common_ele.append(arr3[i])
        else:
            continue

    print("Common elements : ", common_ele)
    return common_ele


if __name__ == "__main__":
    arr_1 = [1, 5, 10, 20, 40, 80]
    arr_2 = [6, 7, 20, 80, 100]
    arr_3 = [3, 4, 15, 20, 30, 70, 80, 120]
    find_common_elements(arr_1, arr_2, arr_3)

    # Common elements :  [20, 80]
