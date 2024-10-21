# https://leetcode.com/problems/kth-largest-element-in-an-array/description/

'''
There are a lot of ways to solve this problem. You should tell it in order to the interviewer.

APPROACH 1: Using sorting
Sort the array and return n - k element from back
TC - O(NlogN) | SC - O(1) (depends upon the sorting algorithm)
------------------------------------------------------------------------------------------

APPROACH 2: Using MaxHeap (can avoid telling this)
Max Heapify the array and pop k times to get kth largest
TC - O(klogN) | SC - O(N) (for heap)
------------------------------------------------------------------------------------------

APPROACH 3: Using MinHeap
Create MIN heap of size k and keep on adding elements to heap (in loop) and if size becomes greater than heap pop.
At the end top element will be kth largest
TC - O(Nlogk) | SC - O(k) (for heap)
------------------------------------------------------------------------------------------

APPROACH 4: Quick select
Use the quick select algorithm and Lomuto's Partition Scheme to select the kth largest element

TC - O(N) average; O(N^2) worst | SC - O(N) space to create left, mid, and right
------------------------------------------------------------------------------------------

APPROACH 5: Medians of medians algorithm (DONT USE)
Using this algorithm we can improve quick selects worst case TC to O(N)
------------------------------------------------------------------------------------------

APPROACH 6: COUNTING SORT
ONLY used for +ve integers
TC - O(N + K) where K is the largest value in the array
SC - O(K)
'''

'''
CLARIFYING QUESTIONS
- Does nums contain -ve integers ? (if ONLY +ve we can use COUNTING SORT)
- What if nums is empty ?
- What if nums is None ?
- What if k > len(nums) ?
- What if k < len(nums) ?
- What if k is -ve ?
- What if k == 0 ?
'''

'''
APPROACH 3: MINHEAP
- Create MIN heap of size k and keep on adding elements to heap (in loop) and if size becomes greater than heap pop.
- At the end top element will be kth largest

TC - O(Nlogk)
SC - O(k) (for heap)
'''
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minHeap = []

        for num in nums:
            heapq.heappush(minHeap, num)

            if len(minHeap) > k:
                heapq.heappop(minHeap)
        
        return minHeap[0]

'''
APPROACH 4: QUICK SELECT
Use the quick select algorithm and Lomuto's Partition Scheme to select the kth largest element

ALGORITHM
1) Choose random pivot
2) Find final index of pivot using partition algorithm
3) Move left and right according to final pivot index

TC - O(N) average; O(N^2) worst | SC - O(N) space to create left, mid, and right
TAKE EXAMPLE - [3, 2, 1, 5, 6, 4]; k = 2
'''
class Solution:
    def findKthLargest(self, arr, k):
        n = len(arr)
        left = 0
        right = n - 1

        while left <= right:
            pivot_index = random.randint(left, right)

            final_pivot_index = self.partition(
                arr, left, right, pivot_index)
            
            if (final_pivot_index == n - k):                
                return arr[final_pivot_index]
            elif (final_pivot_index > n - k):
                right = final_pivot_index - 1
            else:
                left = final_pivot_index + 1

        return -1

    def partition(self, arr, left, right, pivot_index):
        pivot_value = arr[pivot_index]
        j = left # lesser items tail index
        
        self.swap(arr, pivot_index, right)

        for i in range(left, right):
            if arr[i] < pivot_value:
                self.swap(arr, i, j)
                j += 1

        self.swap(arr, right, j)

        return j

    def swap(self, arr, first, second):
        arr[first], arr[second] = arr[second], arr[first]

'''
APPROACH 6: COUNTING SORT
- ONLY used for +ve integers

TC - O(N + K) where K is the largest value in the array
SC - O(K)
'''
def findKthLargest(self, nums, k):
    def countingSort(array):
        M = max(array)

        # Initialize count array
        count = [0] * (M + 1)

        # Store the count of each elements in count array
        for num in array:
            count[num] += 1

        # Calculate the Prefix Sum
        for i in range(1, M + 1):
            count[i] = count[i] + count[i - 1]
        
        output = [0] * len(array)

        # Starting from back of the input array start placing the elements
        i = len(array) - 1
        while i >= 0:
            output[count[array[i]] - 1] = array[i]
            count[array[i]] -= 1
            i -= 1

        # Copy the sorted elements into original array
        for i in range(len(array)):
            array[i] = output[i]
    
    countingSort(nums)
    return nums[-k]