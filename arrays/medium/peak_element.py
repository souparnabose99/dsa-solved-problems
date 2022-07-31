
"""
@TODO:
An element is called a peak element if its value is not smaller than the value of its adjacent elements(if they exists).
Given an array arr[] of size N, Return the index of any one of its peak elements.

For example : N = 4
arr = [5, 10, 20, 15]
Output : 20
"""


def find_peak_element(arr):
    for i in range(len(arr)):
        if i == 0 and arr[i] > arr[i+1]:
            return arr[i]
        elif i == 1 and (arr[i] > arr[i-1] and arr[i] > arr[i+1]):
            return arr[i]
        elif i == (len(arr)-2) and (arr[i] > arr[i-1] and arr[i] > arr[i+1]):
            return arr[i]
        elif i == (len(arr)-1) and arr[i] > arr[i-1]:
            return arr[i]
        elif arr[i] > arr[i-1] and arr[i] > arr[i+1]:
            return arr[i]


if __name__ == "__main__":
    # arr_1 = [5, 10, 20, 15]
    # arr_1 = [10, 5, 20, 15]
    arr_1 = [3, 17, 1, 0, 5, 6]
    peak_element = find_peak_element(arr_1)
    print("Peak Element is : ", peak_element)

# Peak Element is :  20
# Peak Element is :  10
# Peak Element is :  17

