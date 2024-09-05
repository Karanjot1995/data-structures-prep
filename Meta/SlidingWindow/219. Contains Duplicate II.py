# https://leetcode.com/problems/contains-duplicate-ii/description/

from collections import defaultdict


class Solution:
    '''
    APPROACH 1: BRUTE FORCE
    - For every element in array look at previous k elements
    
    TC - O(N * min(k, n))
    SC - O(1)
    '''
    def containsNearbyDuplicate1(self, nums, k: int) -> bool:
        for i in range(len(nums)):
            for j in range(max(i - k, 0), i):
                if nums[i] == nums[j]:
                    return True
        
        return False
    
    '''
    APPROACH 2: HASHMAP
    - Keep a sliding window of kkk elements using Hash Table.
    - Loop through the array, for each element do
        - Search current element in the HashTable, return true if found
        - Put current element in the HashTable
        - If the size of the HashTable is larger than "k", remove the oldest item
    - None of this works out then return false
    
    TC - O(N)
    SC - O(min(N, k))
    '''
    def containsNearbyDuplicate(self, nums, k: int) -> bool:
        m = {}

        for i in range(len(nums)):
            if nums[i] in m: return True

            m[nums[i]] = True
            
            if len(m) > k:
                del m[nums[i - k]]
        
        return False
    
    def containsNearbyDuplicate(self, nums, k: int) -> bool:
      dups = defaultdict(int)
      for i,num in enumerate(nums):
        if num in dups: 
          if abs(dups[num]-i)<=k: return True
        dups[num] = i
      return False