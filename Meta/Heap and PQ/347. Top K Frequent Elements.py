# https://leetcode.com/problems/top-k-frequent-elements/description/

from collections import Counter
from heapq import heappop, heappush

class Solution:
    '''
    APPROACH 1: MIN HEAP solution
    
    TC - O(Nlogk)
    SC - O(N + k)
    '''
    def topKFrequent1(self, nums: List[int], k: int) -> List[int]:
        m = Counter(nums)
        minHeap = []

        if k > len(m):
            return []
        
        for key in m:
            heappush(minHeap, (m[key], key))

            if len(minHeap) > k:
                heappop(minHeap)
        
        ans = []
        while minHeap:
            item = heappop(minHeap)
            ans.append(item[1])
        
        return ans

    '''
    APPROACH 2: QUICKSELECT solution
    - This approach can further be optimized by bringing down to worst case TC(O(N^2)) to O(N) by using Medians of Median algorithm
    - But that has its drawback
        - It's outperformer. Yes, it works in a linear time alpha*N, but the constant alpha is so large that in practice it often works
          even slower than N^2
        - It doesn't work with duplicates
    
    TC - O(N) average and O(N ^ 2) worst case
    SC - O(N)
    '''
    def topKFrequent2(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        unique = list(count.keys())

        def partition(l, r, pivot_index):
            pivot_frequency = count[unique[pivot_index]]
            lesser_items_tail_index = l

            # move pivot to end
            unique[pivot_index], unique[r] = unique[r], unique[pivot_index]
            for i in range(l, r):
                if count[unique[i]] < pivot_frequency:
                    unique[lesser_items_tail_index], unique[i] = unique[i], unique[lesser_items_tail_index]
                    lesser_items_tail_index += 1
            
            unique[r], unique[lesser_items_tail_index] = unique[lesser_items_tail_index], unique[r]

            return lesser_items_tail_index
        
        def quickselect(l, r, k_smallest):
            """
            Sort a list within left..right till kth less frequent element
            takes its place. 
            """
            # base case: the list contains only one element
            if l == r: 
                return
            
            # select a random pivot_index
            pivot_index = random.randint(l, r)     
                            
            # find the pivot position in a sorted list   
            pivot_index = partition(l, r, pivot_index)
            
            # if the pivot is in its final sorted position
            if k_smallest == pivot_index:
                 return 
            # go left
            elif k_smallest < pivot_index:
                quickselect(l, pivot_index - 1, k_smallest)
            # go right
            else:
                quickselect(pivot_index + 1, r, k_smallest)

        n = len(unique)
        quickselect(0, n - 1, n - k)
        return unique[n - k:]
    
    '''
    APPROACH 3: BUCKET SORT solution (MOST OPTIMAL)
    - Since no frequencies can be more than N we can use O(N) space to get to O(N) TC
    
    TC - O(N)
    SC - O(N)
    Video - https://www.youtube.com/watch?v=YPTqKIgVk-k
    '''
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        bucket = [[] for _ in range(n + 1)]
        count = Counter(nums)

        for num, freq in count.items():
            bucket[freq].append(num)
        
        res = []
        for i in range(len(bucket) - 1, 0, -1):
            for n in bucket[i]:
                res.append(n)
                if len(res) == k:
                    return res