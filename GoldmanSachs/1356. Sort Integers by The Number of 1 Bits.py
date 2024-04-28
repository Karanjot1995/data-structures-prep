'''
APPROACH 1: Custom comparator built in

TC - O(nlogn)
SC - O(n) depending upon the sorting algorithm
'''
class Solution:
    def sortByBits(self, arr):
        #  sorting is done first based on the count of set bits and then, if there are ties, based on the original number (that is why the tuple (bit count, num))
        arr.sort(key = lambda num: (num.bit_count(), num))
        return arr

'''
APPROACH: Bit Manipulation

TC - O(nlogn)
SC - O(n) depending upon the sorting algorithm
'''
class Solution:
    def sortByBits(self, arr):
        def find_weight(num):
            mask = 1
            weight = 0
            
            while num:
                if num & mask:
                    weight += 1
                    num ^= mask
                
                mask <<= 1
            
            return weight
        
        arr.sort(key = lambda num: (find_weight(num), num))
        return arr