
"""
@TODO:
Given an unsorted array A of size N that contains only non-negative integers,
find a continuous sub-array which adds to a given number S.
In case of multiple sub-arrays, return the subarray which comes first on moving from left to right.
For example : A = [1,2,3,4,5,6,7,8,9,10] , N = 10, S = 15
Output: A[:5]
"""


# O(N^2) runtime complexity
# Need further optimization to O(N)
def find_sub_array(arr, val):
    index_tracker = 1

    for i in range(len(arr)):
        sub_sum = arr[i]
        for j in range(index_tracker, len(arr)):
            sub_sum = sub_sum + arr[j]
            if sub_sum == val:
                print("Sub array is : ", arr[i:j+1])
                return arr[i:j+1]
            if sub_sum > val:
                break

        index_tracker += 1


if __name__ == "__main__":
    arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    arr2 = [1, 2, 3, 7, 12]
    find_sub_array(arr1, 15)
    find_sub_array(arr2, 12)

    # Sub array is :  [1, 2, 3, 4, 5]
    # Sub array is :  [2, 3, 7]

