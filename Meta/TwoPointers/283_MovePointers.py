# https://leetcode.com/problems/move-zeroes/description/

'''
APPROACH 1: Brute Force
1) Create extra space of the same size as the input
2) Iterate over the input and put non zeroes at the beginning of the ans array
3) After the iteration fill the remaining spots as zeroes

TC - O(N)
SC - O(N)

APPROACH 2: Optimal (constant extra space)
1) Keep a pointer "i" at the beginning of the array which points to the last seen zero in the array
2) Iterate over the array and as we see non zeroes we copy the non zero number to "i" and increment "i"
3) This way all the non zeroes will move to the beginning of the array
4) After the iteration "i" will be pointing to the place from where zeroes should start
5) So in a loop from "i" till the length of the array we put 0s

TC - O(N)
SC - O(1)
'''
class Solution:
    def moveZeroes(self, nums) -> None:
        idx_last_zero = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[idx_last_zero] = nums[i]
                idx_last_zero += 1
        
        while idx_last_zero < len(nums):
            nums[idx_last_zero] = 0
            idx_last_zero += 1


'''
FOLLOW UP - https://leetcode.com/discuss/interview-question/4476189/Meta-Interview-question
Given an integer array nums, modify the array by moving all 0's to the end of it while maintaining the relative order of the non-zero elements.
Additionally, ensure that between any two non-zero elements in the array, there are at least k zeroes, if possible.
For the input [0,1,0,3,12] with k = 1, the output is [1,0,3,0,12], for another input like [0,1,0,3,0,12] with k = 1, the output is [1,0,3,0,0,12]
'''
def moveZeroes(nums, k):
    # first move all zeroes to end
    w = 0
    for r in range(len(nums)):
        if nums[r]:
            nums[w] = nums[r]
            w +=1
    
    nonZeroPos = w-1
    
    # assign zeroes at the end
    for i in range(w, len(nums)):
        nums[i] = 0
    
    if nonZeroPos < 0: # all zeroes
        return nums
    
    # shift all non-zeroes by curPos * k positions expect the first one
    for i in range(nonZeroPos, 0, -1):
        tgt = min(i+(i*k), len(nums)-1)
        if nums[tgt]: # non zero, can't assign
            continue
        nums[i], nums[tgt] = nums[tgt], nums[i]
    return nums

print (moveZeroes([0,1,0,3,12], 1))
print (moveZeroes([0,1,0,3,0,12], 1))
print (moveZeroes([0,1,0,3,0,12], 2))
print (moveZeroes([2,0,0,7,0,9, 8, 0, 0], 1))
print (moveZeroes([2,0,0,7,0,9, 8, 0, 0, 0], 2))
print (moveZeroes([1,2,3,4,5], 1))