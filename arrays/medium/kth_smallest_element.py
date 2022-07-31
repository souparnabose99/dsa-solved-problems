
"""
@TODO:
Given an array arr[] and an integer K where K is smaller than size of array,
the task is to find the Kth smallest element in the given array.
It is given that all array elements are distinct.

For example : N = 6, arr[] = [7, 10, 4, 3, 20, 15], K = 3
Output : 7
"""


def find_kth_smallest_element(arr, k):
    arr.sort()
    print("arr : ", arr)
    print("K'th smallest element is  : ", str(arr[k-1]))
    return arr[k-1]


if __name__ == "__main__":
    arr_1 = [7, 10, 4, 3, 20, 15]
    find_kth_smallest_element(arr_1, 3)
    
    # arr :  [3, 4, 7, 10, 15, 20]
    # K'th smallest element is  :  7

