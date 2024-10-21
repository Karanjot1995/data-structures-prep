# https://leetcode.com/problems/dot-product-of-two-sparse-vectors/

'''
What is a SPARSE VECTOR? - A sparse vector is a vector having a relatively small number of nonzero elements
'''

'''
APPROACH 1: Non-efficient array approach.

Store the original sparse vector as an array reference.
TC - 
    Vector construction - O(N)
    dotProduct() calculation - O(N)
SC - 
    Vector construction - O(1) we simply save a reference to the input array
    dotProduct() calculation - O(1)
'''

'''
APPROACH 2: Hashtable

Store the non-zero values and their corresponding index in a dictionary, with the index being the key. If the index is not present that means values is 0.

TC - 
    Vector construction - O(N) hashmap creation
    dotProduct() calculation - O(L); where L is number of non zero elements
SC - 
    Vector construction - O(L) for creating the hash map of non zero elements
    dotProduct() calculation - O(1)

WHAT IF THE HASH FUNCTION IS BAD? Lookups in the hash table for large sparse vectors will be inefficient.
'''
class SparseVector:
    def __init__(self, nums: List[int]):
        self.nonzeros = {}
        for i, n in enumerate(nums):
            if n != 0:
                self.nonzeros[i] = n              

    def dotProduct(self, vec: 'SparseVector') -> int:
        result = 0
        # iterate through each non-zero element in this sparse vector
        # update the dot product if the corresponding index has a non-zero value in the other vector
        for key, val in self.nonzeros.items():
            if key in vec.nonzeros:
                result += val * vec.nonzeros[key]
        return result

'''
APPROACH 3: Two Pointer [USE THIS APPROACH TO CODE IN INTERVIEW AND DISCUSS ABOUT APPROACH 2]

TC - 
    Vector construction - O(N)
    Dot Product calculation - O(L1 + L2) where L1, L2 represents non zero elements in each vector
SC - 
    Vector construction - O(L) for creating <index, value> pairs for non zero values
    Dot Product calculation - O(1)

Algorithm
1) Store the sparse vector's non zero elements in a list of tuple having [(idx, element)]
2) Take two pointers i (for vec 1), j (for vec 2)
3) If both i'th and j'th item idx is same then compute the dot product else move the smaller index forward
'''

class SparseVector:
    def __init__(self, nums: List[int]):
        self.pairs = []

        for i, num in enumerate(nums):
            if num != 0:
                self.pairs.append((i, num))

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        ans = 0
        i = j = 0

        while i < len(self.pairs) and j < len(vec.pairs):
            i_idx, i_num = self.pairs[i]
            j_idx, j_num = vec.pairs[j]

            # if both idx same then multiply else move the smaller index forward
            if i_idx == j_idx:
                ans += (i_num * j_num)
                i += 1
                j += 1
            elif i_idx > j_idx:
                j += 1
            else:
                i += 1
        return ans


'''
APPROACH 4: Binary Search (ASKED AS A FOLLOW UP)
TC - O(min(m, n) * log(max(m, n))

@krinitsa [editorial comments]
Update from recent FB onsite, interviewer didn't accept the HASHMAP solution and wanted to see the 2 pointers solution, in addition he also came up with a follow up question, what would you do if one of the vectors werent fully "sparse" -> hint use binary search

Code [discuss]
https://leetcode.com/problems/dot-product-of-two-sparse-vectors/solutions/1927043/binary-search-facebook-approved-o-min-m-n-log-max-m-n/

Algorithm [@aastha_21 (editorial comments)]
Following is my solution for both situations when only one is sparse and when both are sparse.
1. Idea behind this solution is to store vectors as list of integer array which contains index and value at that index if it is non zero.
2. Now we will find out which vector is sparse(or we can say more sparse if both are sparse) or having less number of non zero values.
3. Then we start iterating list with less non zero values and check if the other list have a non zero value at same index i or not.In order to check this we will use binary search and check whether that index i exist in the bigger list or not.
4. If that index exists in bigger list as well we will do the product or else skip it.
'''    

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)