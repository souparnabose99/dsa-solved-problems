

"""
@TODO:
Given n non-negative integers representing an elevation map where the width of each bar is 1.
Compute how much water it can trap after raining.

eg:- If the elevation map is [4,1,3,1,5], then the output is 7
"""


def trapping_rain_water(heights_arr):
    if len(heights_arr) < 3:
        return 0
    # create 2 lists storing left and right max values
    left_max = [0 for _ in range(len(heights_arr))]
    right_max = [0 for _ in range(len(heights_arr))]

    for i in range(1, len(heights_arr) - 1):
        left_max[i] = max(left_max[i-1], heights_arr[i-1])

    for i in range(len(heights_arr) - 2, -1, -1):
        right_max[i] = max(left_max[i+1], heights_arr[i+1])

    # Consider all the items in O(N) and calculate sum of trapped rain water units
    trapped_units = 0
    for i in range(1, len(heights_arr) - 1):
        if min(left_max[i], right_max[i]) > heights_arr[i]:
            trapped_units += min(left_max[i], right_max[i]) - heights_arr[i]

    print("Trapped rain water : ", trapped_units)
    return trapped_units


arr = [4, 0, 1, 5, 3]
trapping_rain_water(arr)
trapping_rain_water([1, 0, 2, 1, 3, 1, 0, 0, 3])


