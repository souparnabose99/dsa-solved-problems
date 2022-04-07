"""
Problem Statement:
@TODO:
The problem is to reverse a T[] array in O(N) linear time complexity with the algorithm to be in-place.
No additional memory can be used

For example: input is [1,2,3,4,5,6,7,8] then the output is [8,7,6,5,4,3,2,1]
"""


# O(N) runtime complexity, O(1) space complexity
def rev_array(arr):
    i = 0
    j = len(arr) - 1
    while j >= i:
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1
    return arr


nums = [1, 2, 3, 4, 5, 6, 7, 8]
print("Nums before reversal : ", nums)
num_reversed = rev_array(nums)
print("Nums after reversal : ", num_reversed)


