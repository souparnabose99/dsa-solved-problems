
"""
@TODO:
Sort a T[] one-dimensional array of integers in O(N) running time - and without any extra memory.
The array can contain only values: 0, 1 and 2 where 1 is the pivot element.
"""


def dutch_national_flag(nums, pivot=1):
    i = 0
    j = 0
    k = len(nums) - 1

    while j <= k:
        # when current element is 0
        if nums[j] < pivot:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j += 1
        # when current element is 2
        elif nums[j] > pivot:
            nums[j], nums[k] = nums[k], nums[j]
            k -= 1
        # when current element is 1
        else:
            j += 1
    print("Sorted nums : ", nums)
    return nums


n = [2, 1, 0, 1, 2, 1, 0, 2, 0, 1]
print(n)
dutch_national_flag(n)

# [2, 1, 0, 1, 2, 1, 0, 2, 0, 1]
# Sorted nums :  [0, 0, 0, 1, 1, 1, 1, 2, 2, 2]


