class Solution:
  # Time - O(m + n), Space - O(1)
  def mergeBest(self, nums1, m: int, nums2, n: int) -> None:
   # Set i and j to point to the end of their respective arrays.
    i = m - 1
    j = n - 1

    # And move p backward through the array, each time writing
    # the smallest value pointed at by p1 or p2.
    for p in range(n + m - 1, -1, -1):
      if j < 0:
        break
      if i>=0 and nums1[i]>nums2[j]:
        nums1[p]=nums1[i]
        i-=1
      else:
        nums1[p]=nums2[j]
        j-=1


  #TC - O(O(n+m))
  def mergeBetter(self, nums1, m: int, nums2, n: int) -> None:
    i,j=0,0
    n1 = nums1[:m]
    p=0
    for p in range(n+m):
      #if either second one has reached its end or the normal condition exists
      if j>=n or (i<m and n1[i]<=nums2[j]):
        nums1[p] = n1[i]
        i+=1
      else:
        nums1[p] =nums2[j]
        j+=1
    return nums1
  

  # Time - O(m + n), Space - O(m + n)
  def merge(nums1, m, nums2, n):
    i,j=0,0
    ans = []
    while i<m and j<n:
      if nums1[i]<=nums2[j]: 
        ans.append(nums1[i])
        i+=1
      else:
        ans.append(nums2[j])
        j+=1

    while i<m: 
      ans.append(nums1[i])
      i+=1
    while j<n: 
      ans.append(nums2[j])
      j+=1

    for i in range(len(nums1)):
      nums1[i] = ans[i]
    

'''
ALTERNATE QUESTION - https://leetcode.com/discuss/interview-question/4595295/Meta-Technical-Phone-Screen
Merge 3 sorted arrays wihout extra space

TC - O(max(N, M, K))
SC - O(1) if we don't consider ouput array
'''

import math
def merge(list1, list2, list3):
    i = j = k = 0
    ans = []
    
    while i < len(list1) or j < len(list2) or k < len(list3):
        mini = math.inf
        if i < len(list1):
            mini = min(mini, list1[i])
        
        if j < len(list2):
            mini = min(mini, list2[j])
        
        if k < len(list3):
            mini = min(mini, list3[k])
        
        ans.append(mini)
        
        while i < len(list1) and list1[i] == mini:
            i += 1
        
        while j < len(list2) and list2[j] == mini:
            j += 1
        
        while k < len(list3) and list3[k] == mini:
            k += 1
    return ans

# Example usage:
# arr1 = [1, 3, 5, 7]
# arr2 = [2, 4, 6, 8]
# arr3 = [0, 9, 10, 11]

arr1 = [-100, -10, -1, -1, 0, 0, 0, 1, 1, 5]
arr2 = [-90, -2, 0, 0, 0, 3, 5, 5]
arr3 = [-20, -1, 0, 0, 1, 4, 4]

merged = merge(arr1, arr2, arr3)
print("Merged array:", merged)

        


        