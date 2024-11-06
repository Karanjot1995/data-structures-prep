class Solution:
    '''
    APPROACH 1: Brute Force
    - Take a new array and merge the 2 sorted arrays into this 3rd array
    - Get the median

    TC - O(N + M)
    SC - O(N + M)

    APPROACH 2: Better (optimized above approach)
    - Just get the median elements and no need to store the merged array
    - If n is even find elements at index n/2 and n/2 - 1 and calculate median
    - If n is odd find element at index n/2 and that is the median
    - Video: https://www.youtube.com/watch?v=C2rRzz-JDk8&ab_channel=takeUforward

    TC - O(N + M)
    SC - O(1)
    '''
    def findMedianSortedArrays1(self, nums1: List[int], nums2: List[int]) -> float:
        n1, n2 = len(nums1), len(nums2)
        i = j = 0
        n = n1 + n2
        idx1 = n // 2 - 1
        idx2 = n // 2

        cur_idx = 0
        idx1_element = idx2_element = -1

        while i < n1 and j < n2:
            if nums1[i] < nums2[j]:
                if cur_idx == idx1: idx1_element = nums1[i]
                if cur_idx == idx2: idx2_element = nums1[i]

                cur_idx += 1
                i += 1
            else:
                if cur_idx == idx1: idx1_element = nums2[j]
                if cur_idx == idx2: idx2_element = nums2[j]

                cur_idx += 1
                j += 1
        
        while i < n1:
            if cur_idx == idx1: idx1_element = nums1[i]
            if cur_idx == idx2: idx2_element = nums1[i]

            cur_idx += 1
            i += 1
        
        while j < n2:
            if cur_idx == idx1: idx1_element = nums2[j]
            if cur_idx == idx2: idx2_element = nums2[j]

            cur_idx += 1
            j += 1
        
        if n % 2 != 0: return idx2_element

        return (idx1_element + idx2_element) / 2
    
    '''
    APPROACH 3: Binary Search (most optimal)
    - Video: https://www.youtube.com/watch?v=q6IEA26hvXc&t=101s&ab_channel=NeetCode
    - Video: https://www.youtube.com/watch?v=F9c7LpRZWVQ&ab_channel=takeUforward

    TC - O(log(min(m, n)))
    SC - O(1)
    '''
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total // 2

        if len(B) < len(A):
            A, B = B, A
        
        # run BS on smaller array (A)
        l, r = 0, len(A) - 1
        while True:
            i = (l + r) // 2 # A
            j = half - i - 2 # B

            Aleft = A[i] if i >= 0 else -math.inf
            Aright = A[i + 1] if (i + 1) < len(A) else math.inf
            Bleft = B[j] if j >= 0 else -math.inf
            Bright = B[j + 1] if (j + 1) < len(B) else math.inf

            # partition is correct
            if Aleft <= Bright and Bleft <= Aright:
                # odd
                if total % 2 != 0:
                    return min(Aright, Bright)
                
                # even
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright:
                # A partition has too many elements in A and reduce the size of the left partition
                r = i - 1
            else:
                # inclrease the size of the left partition from A
                l = i + 1
