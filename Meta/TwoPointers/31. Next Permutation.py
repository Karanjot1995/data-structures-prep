'''
APPROACH 1: Brute force
1) Generate all the permutations (in sorted order)
2) Get the next permutation after the current nums

TC - AT min O(N!)

APPROACH 2: Trick

Ex - 2 1 5 4 3 0 0
1) We see we can't change 54300 as it is max but we can change 1 -> find the item right before the decreasing sequence (5 -> 4 -> 3 -> 0 -> 0) starts
2) Now whom do we swap 1 with ? 5, 4, 3?? => We swap with 3 as we want the next greatest not greatest permutation
Thus, we have to find the item just greater than pivot (1) from right to left
3) Now we have taken 2 3 _ _ _ _ _ (what should be the next numbers)?
We have to make this part as small as possible so we reverse so that they are in ASCENDING order - 2 3 0 0 1 4 5

TC - O(N) | SC - O(1)

EDGE CASES
- What is there is no next permutation like 321 should I return the smallest or -1?

STEPS (to tell interviewer)
1) We iterate from right to left and find the element right before the decreasing sequence which will be the pivot element
2) If we find the index which is greater than 0 we then iterate again from right to left till we find the first element greater than the pivot
3) We swap the number found with the pivot
4) Now we reverse the decreasing sequence to get the final next permutation
'''
class Solution:
    # TC - O(N) | SC - O(1)
    def nextPermutation(self, nums) -> None:
        def reverse(start):
            left = start
            right = len(nums) - 1

            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        '''
        * Walk backwards. Keep walking until we reach the point right before the
        * decreasing sequence begins. When this while loop ends that is where i will
        * stand
        '''
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        
        '''
        * If i is not the first element we have more work to do
        * 
        * If i IS the first element we just skip down to reverse the whole array since
        * the WHOLE array would be decreasing meaning we are on our last permutation
        '''
        if i >= 0:

            '''
            * Start a pointer at the end of the array, we want to search for the smallest item THAT IS GREATER THAN THE ELEMENT AT i
            '''
            j = len(nums) - 1
            while j >= 0 and nums[i] >= nums[j]:
                j -= 1
            
            # swap the elements
            nums[i], nums[j] = nums[j], nums[i]
        
        """
        * Perform the reversal on the decreasing section now. We pass in i + 1 since i
        * sits RIGHT BEFORE the decreasing section that is on its final permutation
        * if i<0 it will automatically reverse the whole array
        """
        reverse(i + 1)