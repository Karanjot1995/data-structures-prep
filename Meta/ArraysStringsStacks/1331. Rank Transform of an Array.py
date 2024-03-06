import heapq

# https://leetcode.com/problems/rank-transform-of-an-array/description/

class Solution:
    def arrayRankTransform(self, arr):
        if not arr: return None
        nums = sorted(set(arr))
        hmap = {}
        rank = 1
        for i in range(len(nums)):
            hmap[nums[i]] = rank
            rank+=1

        for i in range(len(arr)):
            arr[i] = hmap[arr[i]]
        return arr
    '''
    APPROACH: MinHeap
    
    1) Keep a min heap so that all the min elements are at the top
    2) Keep the index of the elements in the min heap as well so I will keep a tuple of value and its index in the array
    3) We can declare rank = 0
    4) No we can start popping the elements from the heap and we have to keep track of previous numebr as well so as to not increase the rank if cur num
       is equal to the prev num
    5) Now we increase the rank every time the num is not equal to the prev number and add the rank of the num at that index
    
    TC - O(NlogN)
    SC - O(N)
    '''
    def arrayRankTransform(self, arr):
        minHeap = [(num, idx) for idx, num in enumerate(arr)]
        heapq.heapify(minHeap)
        rank = 0
        prev = None

        while minHeap:
            num, idx = heapq.heappop(minHeap)
            if num != prev:
                prev = num
                rank += 1
            
            arr[idx] = rank
        return arr