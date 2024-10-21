# https://leetcode.com/problems/subarray-sum-equals-k/

from collections import defaultdict
'''
CLARIFYING QUESTIONS:
- Does it contain only +ve integers? (IF YES, USE THE SOLUTION OF ALTERNATE QUESTION)
'''
class Solution:
    '''
    APPROACH: Brute Force
    - Consider every possible subarrays of the given nums aray using nested loops
    - Keep track of sum while we are making the subarrays and as soon as sum == k do count += 1

    TC - O(N^2)
    SC - O(1)
    '''
    def subarraySum1(self, nums, k):
        count = 0

        for i in range(len(nums)):
            total = 0
            for j in range(i, len(nums)):
                total += nums[j]

                if total == k: count += 1
        return count

    '''
    APPROACH 2: Prefix sum
    - Use prefix sum to get subarrays
    - If we have a prefix sum X and we are looking for sub arrays with sum K then we find out how many times preffix sum "X" - "K" occurs till now

                                   K
                           | ---------- 
            _______________||__________|
                           |          X (pref sum)
                           |
    - Ex [1, 2, 3, -3, 1, 1, 1, 4, 2, -3]
          0  1  2   3  4  5  6  7  8   9
        - if K = 3 consider window from 2nd idx to 6th idx it gives a sum of 3
        - But the pref sum till 6th idx is 6
        - So there exist pref sum (6) - k(3) = 3 sum sub array from 0th to 1st idx
    
    Video - https://www.youtube.com/watch?v=fFVZt-6sgyo&ab_channel=NeetCode
    Video - https://youtu.be/xvNwoz-ufXA?si=_GGMyEDtihmGgVzD&t=501

    TC - O(N)
    SC - O(N)
    '''
    def subarraySum(self, nums, k):
        preSum = count = 0
        hmap = defaultdict(int)
        
        '''
        * For the case [1, 1, ,1, 1,, 1] and k = 3
        * As we hit the first 3 elements the diff (3 - 3 = 0) will not be there in the map
        '''
        hmap[0] = 1

        for num in nums:
          preSum+=num
          if preSum - k in hmap: count+= hmap[preSum-k]
          hmap[preSum]+=1

        # for num in nums:
        #     preSum += num
            
        #     # if there exists old sum that can be subtracted from currsum to get k
        #     remove = preSum - k
        #     count += hmap[remove]
            
        #     hmap[preSum] += 1

        return count

'''
ALTERNATE QUESTIONS: Given list of non-negative integers and an integer target, return whether a continuous sequence of input integers sums up to target

https://leetcode.com/discuss/interview-question/4259535/META-or-Random-pick-index-and-Subarray-sum-K

WHY THIS CANNOT BE SOLVED WITH SLIDING WINDOW? (due to the presence of negative numbers)
https://leetcode.com/problems/subarray-sum-equals-k/solutions/2799591/the-reason-why-this-problem-can-t-be-solved-using-sliding-window/

https://leetcode.com/problems/subarray-sum-equals-k/solutions/2188200/hashmap-approach-sliding-window-approach-by-aditya-verma/

If only positive numbers are present in the array:

def subarraySum(self, nums, k: int) -> int:

    # to handle this edge case of k = 0
    if k == 0:
        return 0

    i = 0
    j = 0
    n = len(nums)
    s = 0
    subarrayCount = 0
    while j < n:
        s += nums[j]
        if s < k:
            j += 1
        elif s == k:
            subarrayCount += 1
            j += 1
        else:
            while i < len(nums) and s > k:
                s -= nums[i]
                i += 1
                if s == k:
                    subarrayCount += 1
                    break
            j += 1
    return subarrayCount
'''

'''
FOR META ANSWERS BELOW : Return TRUE/FALSE
'''

# ONLY +ve INTEGERS (SLIDING WINDOW)
# TC - O(N) | SC - O(1)
def subarraySumK1(arr, k):
    n = len(arr)
    start = cur_sum = end = 0

    for end in range(len(arr)):
        cur_sum += arr[end]

        #DOES NOT HANDLE CASE: arr = [1, 3] and target = 0 --> while start < n and cur_sum > k:
        while start < end and cur_sum > k:
            cur_sum -= arr[start] 
            start += 1
        
        if cur_sum == k:
            return True
    
    # ANOTHER WAY USING ONLY WHILE LOOPS
    # while end < n:
    #     cur_sum += arr[end]
    #     end += 1
        
    #     # to avoid cases when target is 0 we do start < end - 1
    #     while start < end - 1 and cur_sum > k:
    #         cur_sum -= arr[start]
    #         start += 1
        
    #     if cur_sum == k:
    #         return True

    return False

# ABOVE SOLUTION WITH PRINTING SUBSEQUENCE
import collections
def subarraySumKWithPrint(arr, k):
    n = len(arr)
    start = cur_sum = end = 0
    subsequence = collections.deque()

    for end in range(len(arr)):
        cur_sum += arr[end]
        subsequence.append(arr[end])  # Append the current element to the subsequence list

        while start < end and cur_sum > k:
            cur_sum -= arr[start]
            subsequence.popleft()  # Remove the first element from the subsequence
            start += 1
        
        if cur_sum == k:
            print("Subsequence with sum equal to", k, ":", subsequence)
            return True
    return False

# WORKS FOR -ve INTEGERS
# TC - O(N) | SC - O(N)
def subarraySumK2(nums, k):
    preSum = count = 0
    hmap = defaultdict(int)
    
    '''
    * For the case [1, 1, ,1, 1,, 1] and k = 3
    * As we hit the first 3 elements the diff (3 - 3 = 0) will not be there in the map
    '''
    hmap[0] = 1

    for num in nums:
        preSum += num
        
        # if there exists old sum that can be subtracted from currsum to get k
        remove = preSum - k
        if preSum - k in hmap:
            return True
        
        hmap[preSum] += 1

    return False

tests = [
    # empty sequence
    {
        'arr': [],
        'target': 1,
        'expected': False
    },
    {
        'arr': [],
        'target': 0,
        'expected': False
    },
    
    # 1 element sequences
    {
        'arr': [1],
        'target': 1,
        'expected': True
    },
    {
        'arr': [0],
        'target': 0,
        'expected': True
    },
    
    # general test cases with bein, middle and end
    {
        'arr': [1, 3, 5, 23],
        'target': 1,
        'expected': True
    },
    {
        'arr': [1, 3, 5, 23],
        'target': 3,
        'expected': True
    },
    {
        'arr': [1, 3, 5, 23],
        'target': 8,
        'expected': True
    },
    {
        'arr': [1, 3, 5, 23],
        'target': 23,
        'expected': True
    },
    {
        'arr': [1, 3, 5, 23],
        'target': 28,
        'expected': True
    },
    {
        'arr': [1, 3, 5, 23],
        'target': 4,
        'expected': True
    },
    {
        'arr': [1, 3, 5, 23],
        'target': 32,
        'expected': True
    },
    {
        'arr': [1, 3, 5, 23],
        'target': 70,
        'expected': False
    },
    {
        'arr': [1, 3, 5, 23],
        'target': 7,
        'expected': False
    },
    
    # tricky 0 cases
    {
        'arr': [1, 3],
        'target': 0,
        'expected': False
    },
    {
        'arr': [1, 3, 0],
        'target': 0,
        'expected': True
    },
    {
        'arr': [0, 1, 3],
        'target': 0,
        'expected': True
    },
    {
        'arr': [1, 0, 3],
        'target': 0,
        'expected': True
    },
]

# f = subarraySumK1
f = subarraySumKWithPrint
for test in tests:
    ans = f(test['arr'], test['target'])
    if ans != test['expected']:
        print("FAILED: f({0}, {1}) returned {2} expected {3}".format(test['arr'], test['target'], ans, test['expected']))
    else:
        print("PASSED")