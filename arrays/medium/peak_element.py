
"""
@TODO:
An element is called a peak element if its value is not smaller than the value of its adjacent elements(if they exists).
Given an array arr[] of size N, Return the index of any one of its peak elements.
eg : N = 3
arr[] = {1,2,3}
Possible Answer: 2
Explanation: index 2 is 3.
It is the peak element as it is greater than its neighbour 2.
"""

def peakElement(self,arr, n):
  # Code here
  peak_element = 0
  for i in range(n):
    if i==0:
      peak_element = 0
    else:
      if i<n-1 and (arr[i] > arr[i-1] and arr[i] > arr[i+1]):
        peak_element = i
  return peak_element


