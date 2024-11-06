# https://leetcode.com/problems/contiguous-array/

class Solution:
    '''
    APPROACH 1: BRUTE FORCE
    - Building all the contigous arrays -> O(N^2)

    APPROACH 2: HASHMAP
    1) We maintain a "count" variable that signifies the balance b/w the 1s and the 0s
    2) When we see a 1 we increment the count by 1 else we decrement by 1
    3) So now when we start from 0 and later on our "count" becomes zero again that means this window contains equal 0s and 1s
    4) Apart from this we would also keep track of the count in a hashmap because it is possible if for ex our count becomes -3
       and after a few values it becomes -3 again that means the portion in the middle cancelled out each other and became balance
       so we need to account for this window also
       
    
    TC - O(N)
    SC - O(N)

    Video - https://www.youtube.com/watch?v=Xkl4EknqW8Y&ab_channel=CrackingFAANG
    '''
    def findMaxLength(self, nums: List[int]) -> int:
        seen_at = {} # count: index
        seen_at[0] = -1 # for [0, 1]
        ans = count = 0 # count represents the balance between 0s and 1s

        for i, num in enumerate(nums):
            count += 1 if num == 1 else -1

            if count in seen_at:
                ans = max(ans, i - seen_at[count])
            else:
                seen_at[count] = i
        
        return ans
    

#TLE 

# public class Solution {

#     public int findMaxLength(int[] nums) {
#         int maxlen = 0;
#         for (int start = 0; start < nums.length; start++) {
#             int zeroes = 0, ones = 0;
#             for (int end = start; end < nums.length; end++) {
#                 if (nums[end] == 0) {
#                     zeroes++;
#                 } else {
#                     ones++;
#                 }
#                 if (zeroes == ones) {
#                     maxlen = Math.max(maxlen, end - start + 1);
#                 }
#             }
#         }
#         return maxlen;
#     }
# }
