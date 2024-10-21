# https://leetcode.com/problems/3sum/description/

'''
APPROACH 1: Brute Force
Using 3 for loop to make each and every pair and putting it in a set

TC - O(N^3)
SC - O(1)
'''

class Solution:
    '''
    APPROACH 2: Better - No-Sorting (Hashing)
    1) Find first and second number using 2 for loops and third will be -(first + second)
    2) While we are traversing the array in the second loop we will add the elements in hashmap
    3) If we find a number that is -(first + second) then we have a triplet
    4) Store the triplet in a set
    
    Because in the question it is given first + second + third = 0

    TC - O(N^2)
    SC - O(N)

    Video - https://youtu.be/DhFh8Kw7ymk?si=wQGEKMTBH7J6GQ48&t=628
    '''
    def threeSum1(self, nums: List[int]) -> List[List[int]]:
        ans = set()

        for i in range(len(nums)):
            # making sure the third element is not same as the first and second chosen
            # Ex: [-1, 0, 1, 2, -1, -4] and first and second numbers are 2 and -4 so third will be -(2 - 4) = 2 so we cant choose 3rd simply from the hashmap
            # to over come this we will add elements only between i and j
            hmap = {}
            for j in range(i + 1, len(nums)):
                third = -(nums[i] + nums[j])

                if third in hmap:
                    temp = [nums[i], nums[j], third]
                    temp.sort()
                    ans.add(tuple(temp))

                hmap[nums[j]] = True
        
        return list(ans)
    
    '''
    APPROACH 3: OPTIMAL - Two Pointer (Lohia)
    1) Sort the array (so that all the dupilicates are together and we can pick only one of those for one position)
    2) We fix the first number using a for loop
    3) Inside the for loop we use a while loop to find out the rest 2 elements by using the 2 pointer technique
    4) If we fix the ith element then we can place a left pointer at i + 1 and the right pointer at the end of the list
    5) If the sum of ith element and the elements at the 2 pointers is 0 we add it to the result set -- we keep a set to avoid duplicates
    6) If the threesum is < 0 we move the left pointer else the right pointer
    7) At the end we return the result
    
    TC - O(NlogN) + O(N^2) = O(N^2)
    SC - O(1)
    '''
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if not nums or len(nums) < 3: return []

        nums.sort()
        ans = set()

        # fix the first element and find the other two elements
        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1

            while left < right:
                threesum = nums[i] + nums[left] + nums[right]

                if threesum == 0:
                    ans.add((nums[i], nums[left], nums[right]))
                    left += 1
                    right -= 1
                elif threesum < 0:
                    left += 1
                else:
                    right -= 1

        return list(ans)
    
    '''
    APPROACH 3: Optimal - Two pointer (STRIVER)
    1) Sort the array (so that all the dupilicates are together and we can pick only one of those for one position)
    2) Iterate the sorted array and pick first element
    3) Use Two Pointer on the sorted right part of the array to find its pairing

    TC - O(NlogN) + O(N^2) = O(N^2)
    SC - O(1)
    '''
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()

        # fix the first number and apply logic for TwoSum II for finding out rest of the elements
        for i, first in enumerate(nums):
            if i > 0 and first == nums[i - 1]:
                continue
            
            start, end = i + 1, len(nums) - 1
            while start < end:
                second, third = nums[start], nums[end]
                threesum = first + second + third

                if threesum > 0:
                    end -= 1
                elif threesum < 0:
                    start += 1
                else:
                    # condition: threesum == 0:

                    ans.append([first, second, third])
                    start += 1
                    # keep on incrementing the start pointer till the next item is not same as the current
                    # the end pointer will automatically updated by the main while loop
                    # [-2, -2, 0, 0, 2, 2] if start is at 0th and end is at 5th idx then move the start till it is not -2 i.e. to index 2
                    # don't need to increment end pointer as that will be incremented by the above conditions
                    while nums[start] == nums[start - 1] and start < end:
                        start += 1

        return ans