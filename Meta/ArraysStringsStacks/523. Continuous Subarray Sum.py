# https://leetcode.com/problems/continuous-subarray-sum/

'''
APPROACH 1: BRUTE FORCE
- Find every single subarrays and check if it is good subarray

TC - O(N^2)
SC - O(1)
'''

'''
APPROACH 2: OPTIMAL using PREFIX SUM

INTUITION: https://youtu.be/20v8zSo2v18?si=YZ9ipxuejfunap5u&t=20
s1 = kn + x
s2 = km + x

s2 - s1 = k(n + m) therefore divisible by k

WHY store intital {0: -1} in hash map?
Ex : [23, 2, 4, 6, 6] and k = 7 ...
- sub-array [23, 2, 4, 6] will have sum 35 so remainder will be 0, but in order to return 
this answer we need a condition i.e. element should already be present in the map
- IF THE FIRST VALUE IS ITSELF divisible by k then we need to have the 0 remainder in the hashmap so that we don't return it as it is a single
  element

WHY -1?
Ex - [2, 4, 3]. k = 6
If we don't set -1 (and do {0: 0}), then this will give False as window size will be 1 <= 2

ALGORITHM
1) Keep a hashmap with keys as the remainder and values as the index
2) We iterate over the array and in each iteration
    - we get the current running sum
    - we take the element and mod (%) it by k to get the remainder and add it to the hashmap
    - this signifies that we have a prefix sum with remainder x that ends at index i
    - things get interesting when we find a remainder that is already stored in the hashmap
        - if we have already seen the reaminder then how come we are seeing the exact same remainder again (since we are doing prefix sum)
        - this is possible because the value that we added from when first we got remainder x and now, will total up to a multiple of "K"
    - So now we just check the window size from 1st index of "x" to the second index of "x" and if the window size is >= 2 we return True
    - This will be done in our loop
3) When we come out of the loop if we haven't returned already then we return False as we couldn't find the required solution

TC - O(N)
SC - O(N)

Video - https://www.youtube.com/watch?v=OKcrLfR-8mE
'''
class Solution:
    def checkSubarraySum(self, nums, k: int) -> bool:
        hmap = { 0: -1 }
        total = 0

        for idx, num in enumerate(nums):
            total += num
            remainder = total % k

            if remainder not in hmap:
                hmap[remainder] = idx
            elif idx - hmap[remainder] >= 2: # getting widow size (need at least 2)
                return True
        return False

'''
WHY storing remainder and index gives the answer?

comment by - @markdanskin (editorial section)
Here is how the logic makes sense to me. Remainders are essentially the distance above a multiple of a number. For example 8 % 7 = 1, as 8 is 1 above 7. 15 % 7 is also 1, because 15 is 1 above another multiple of 7.

So keeping that in mind when you are taking a running sum and checking the remainder, the only way to get two of the same remainder is if the numbers between those two values add up to a multiple of what you are getting the remainder of.

Using the first example: [23, 2, 4, 6, 7] k = 6
The running tally would be: 23, 25, 29, 35, 42
And the remainder would be: 5, 1, 5, 5, 0

When we start (23) we are 5 above a multiple of 6, and by the 3rd digit we are back to 5 above a multiple of 6. The only way for this to be possible is if the numbers in between add up to a multiple of 6. Because how could you be the same distance above the multiple without that being true?

If it still doesn't make sense take a look at the running tally. The first number is 23, and the 3rd number (Which is the solution) is 29. Subtract and you get a multiple 29 - 23 = 6 because the numbers between add up to 6. The next number 35 also results in a multiple, and 35 - 23 = 12, because the numbers between add up to 12, which is also a multiple.

ALSO CHECK - https://leetcode.com/problems/continuous-subarray-sum/solutions/485589/c-python-easy-and-concise/
'''