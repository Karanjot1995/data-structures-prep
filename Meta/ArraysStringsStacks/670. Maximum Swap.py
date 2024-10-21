# https://leetcode.com/problems/maximum-swap/description/

from collections import defaultdict

# Video - https://www.youtube.com/watch?v=IiAd7twX0xU&ab_channel=Pepcoding
class Solution:
    def maximumSwap(self, num: int) -> int:
        '''
        APPROACH 1: BRUTE FORCE
        Starting from left for each index "i" find the FURTHEST MAX to right for each digit, if you found one swap and break

        Ex - 1993 (THIS SHOWS THE OBSERVATION OF FURTHEST MAXIMUM TO RIGHT)
        For 1 we find the max digit which is furthest at index 2. So we swap index 0 and index 2 to get 9913
        
        TC - O(N^2) | SC - O(N)
        '''
        def bruteForce():
            arr = [d for d in str(num)]

            for i in range(len(arr)):
                max_index = i
                for j in range(i + 1, len(arr)):
                    if arr[j] >= arr[max_index]:
                        max_index = j
                    
                if arr[max_index] > arr[i]:
                    arr[max_index], arr[i] = arr[i], arr[max_index]
                    break
            
            return int("".join(arr))
        
        '''
        APPROACH 2: BETTER
        Optimizing above approach, instead of finding furthest max to right for each index (2 loops), we store for each index which is the furthset number greater than itself
        
        TC - O(N) | SC - O(N)
        '''
        def betterApproach():
            arr = [d for d in str(num)]
            hmap = defaultdict(int) # { cur_index: furthest_max_idx }
            

            # traverse from back and find the max furthest idx for each index
            cur_max_index = None
            for i in range(len(arr) - 1, -1, -1):
                if not cur_max_index or arr[i] > arr[cur_max_index]:
                    cur_max_index = i
                
                hmap[i] = cur_max_index
            
            for i in range(len(arr)):
                max_idx_to_right = hmap[i]

                if arr[i] < arr[max_idx_to_right]:
                    arr[i], arr[max_idx_to_right] = arr[max_idx_to_right], arr[i]
                    break
            
            return int("".join(arr))

        '''
        APPROACH 3: MOST OPTIMAL
        - Optimizing above approach, instead of storing for each index which is the furthset number greater than itself, we will store
          the furthest index of digits 0 - 9 in the hash map/array of size 10
        - Now when we consider the current digit, we check if all the digits from that are greater than itslef and if they come after the cur index if so then swap

        
        TC - O(N) | SC - O(k) wher k is a constant as we are only storing 10 digits in a hashmap
        '''
        def optimal():
            arr = [d for d in str(num)]
            hmap = defaultdict(int)
            
            # for each digit in num calculate its last index
            for idx, digit in enumerate(arr):
                hmap[digit] = idx
            
            for i, digit in enumerate(arr):
                swapped = False

                for d in range(9, int(digit), -1):
                    d_index = hmap[str(d)]
                    
                    if d_index > i:
                        arr[i], arr[d_index] = arr[d_index], arr[i]
                        return int("".join(arr))

            # didn't need to swap anything return the num as it is
            return num

        # return bruteForce()
        # return betterApproach()
        return optimal()

# https://leetcode.com/problems/maximum-swap/solutions/1623820/python-3-o-n-time-o-1-space-without-using-strings-with-comments/