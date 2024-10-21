# https://leetcode.com/problems/kth-missing-positive-number/description/

class Solution:
    '''
    APPROACH 1: BRUTE FORCE (Linear Scan)
    
    ALGORITHM
    1) Check if the kth missing number is less than the first element of the array. If that's the case, return k.
    2) Decrease k by the number of positive integers which are missing before the array starts: k -= arr[0] - 1.
    3) Iterate over the array elements:
        a) At each step, compute the number of missing positive integers in-between i + 1th and ith elements: currMissing = arr[i + 1] - arr[i] - 1.
        b) Compare k to the currMissing. If k <= currMissing then the number to return is in-between arr[i] and arr[i + 1], and we can return it: arr[i] + k
        c) Otherwise, decrease k by currMissing and proceed further.
    4) At the end if we did not return in loop that menas the element to return is greater than the last element of the array
       so we return it: arr[n - 1] + k.


    TC - O(N) | SC - O(1)
    '''
    def findKthPositive2(self, arr: List[int], k: int) -> int:
        if k <= arr[0] - 1: return k

        k = k - (arr[0] - 1)

        for i in range(len(arr) - 1):
            missing = arr[i + 1] - arr[i] - 1

            if k <= missing:
                return arr[i] + k
            
            k -= missing
        
        return arr[-1] + k

    '''
    APPROACH 2: Binary Search
    
    ALGORITHM
    1) Since the array is sorted we can use Binary Search on it but we would have to modify BS a bit here since we can't search stright forward here
    2) If we can figure out between which indexes our kth missing number should have been then our problem will be solved, so we have to
       figure out the 2 nearby indexes
    3) So basically at each index we will check how many numbers are missing, we can calculate that by subtracting the num that should have been at the
        index (if no numbers were missing) FROM the cur number at the index
        
        Proof:
        -----
        idx    0  1  2  3   4
        I/P - [2  3  4  7  11]
              [1  2  3  4   5]  (actual array if there were no missing)
        
        So to find how many numbers are missing at index 3 we do cur_num (7) - the num that should have been there (4) = 3 missing (1, 5, 6 are the missing)
    
    4) So thinking in terms of BS, we calculate the mid and find the numbers missing at the mid index
        - if the missing numbers < k then we will move our left boundary to mid + 1
        - else we move our right boundary to mid - 1
    5) At the end of the loop, our left pointer will have crossed the right pointer (left will be just ahead of right at index right + 1)
    6) So the answer will be arr[right] + how many more we need (k - missing numbers before arr[right])
        - we can't use arr[right] in our ans as this can go out of bounds if k is less than the 1st num
            i/p:       [4  7  9]  k = 3
                   |    |
                right  left
        - So lets convert ans = arr[right] + how many more we need (k - missing numbers before arr[right]) IN TERMS OF arr[left]
        -> missing numbers before arr[right] = arr[right] - (right + 1)
        -> ans = arr[right] + k - (arr[right] - right - 1)
               = arr[right] + k - arr[right] + right + 1
               = right + 1 + k (cancelling out arr[right])
               = left + k (right + 1 is actually left pointer)
        
    TC - O(logN)
    SC - O(1)
    
    Video - https://www.youtube.com/watch?v=uZ0N_hZpyps&t=909s&ab_channel=takeUforward
    '''
    def findKthPositive(self, arr: List[int], k: int) -> int:
        n = len(arr)
        left = 0
        right = n - 1

        while left <= right:
            mid = (left + right) // 2
            missing = arr[mid] - (mid + 1)
            if missing < k:
                left = mid + 1
            else:
                right = mid - 1
        return left + k # or right + 1  + k

    # TC - O(n + k)
    def findKthPositive1(self, arr: List[int], k: int) -> int:
        arr_set = set(arr)

        for i in range(1, k + len(arr) + 1):
            if i not in arr_set: k -= 1
            if k == 0: return i
    
    # TC - O(N) | SC - O(1) - NOT INUITIVE (STRIVER BRUTE FORCE)
    def findKthPositive3(self, arr: List[int], k: int) -> int:
        n = len(arr)
        for i in range(n):
            if arr[i] <= k:
                k += 1  # shifting k
            else:
                break
        return k