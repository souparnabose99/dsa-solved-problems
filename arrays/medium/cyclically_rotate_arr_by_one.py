
"""
@TODO:
Given an array, rotate the array by one position in clock-wise direction.

For example:
A = [1, 2, 3, 4, 5]
Output : [5, 1, 2, 3, 4]
"""


def cyclic_arr_rotation(arr):
    i = 0
    j = len(arr) - 1
    while j != 0:
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1
    return arr


if __name__ == "__main__":
    arr_1 = [9, 8, 7, 6, 4, 2, 1, 3]
    print("Original Array : ", arr_1)
    arr_final = cyclic_arr_rotation(arr_1)
    print("Array after cyclic rotation : ", arr_final)

    # Original Array :  [9, 8, 7, 6, 4, 2, 1, 3]
    # Array after cyclic rotation :  [3, 8, 7, 6, 4, 2, 1, 9]


