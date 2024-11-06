# https://leetcode.com/problems/random-pick-index/description/

from collections import defaultdict

'''
CLARIFYING QUESTIONS
- Will the given target always exist in the array?
- What if the array is empty?
- What if the array is null?
- Will the array always contain integers?
'''


'''
APPRACH 1: Brute Force (HASH MAP)
1) Precompute the positions of the elements in the nums array
2) In the hash map for store indices of each element {element: [idx1, idx2, idx3] }
3) Now for the target get the list of indices of target from hash map and randomly pick any index

TC - O(N) | SC - O(N)
'''
class Solution1:

    def __init__(self, nums: List[int]):
        self.hmap = defaultdict(list)

        for i, val in enumerate(nums):
            self.hmap[val].append(i)

    def pick(self, target: int) -> int:
        return random.choice(self.hmap[target])


'''
APPRACH 2: OPTIMAL (RESERVIOR SAMPLING)
1) In this we will keep a count which will represent the number of times we have seen the target
2) Also we will keep a variable called as picked_index which will represent the index that we have picked for the target
3) Then we iterate over the array from left to right and increment the "count" when we see the target
4) Then in each iteration we pick a number from 1, count and if that number equals count we pick that index -- this is the way how we acheive randomness

Explanation of Reservior Sampling
- If we have a box and we have 1 marble then probability of picking that marble is 1 (100%)
- If we add a 2nd marble then now probability of picking the marble is 1/2
- If we add a 3rd marble then now probability of picking the marble is 1/3
- If we notice the denominators, every time we add a marble we increase the denominator
- To acheive randomness we pick a number from 1 to "count" and if that number == count we say that index is the pick

TC - O(N) | SC - O(1)

Video - https://www.youtube.com/watch?v=HXRN8ZfAQOI&ab_channel=CrackingFAANG
'''
class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def pick(self, target: int) -> int:
        count = picked_index = 0

        for i, num in enumerate(self.nums):
            if num == target:
                count += 1
                if random.randint(1, count) == count:
                    picked_index = i
        return picked_index
        

'''
FOLLOW UP / ALTERNATE QUESTION

Q. Given stream of integers which can have duplicates. return random index of LARGEST NUMBER
eg: 1, 1, 9, 2, 3, 9, 9 probabilty of 9 to return is 1/3

Solution: use reservoir sampling
TC - O(N)
SC- O(1)


import random
def random1(arr):

    target = max(arr)
    
    count = 0
    pick_index = 0

    for i in range(len(arr)):
        # count the number of times target variable has come in array
        if arr[i] == target:
            count += 1

            # if we encounter target num we will check if the random number generated from 1-> count == count, if yes then we update the pick index as i
            if random.randint(1, count) == count:
                pick_index = i

    return pick_index

ans = random1([1, 10, 9, 11, 3, 11, 9])
print(ans)
'''