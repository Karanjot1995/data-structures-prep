# https://leetcode.com/problems/custom-sort-string/description/

class Solution:
    '''
    APPROACH: HASHMAP
    
    TC - O(S + O)
    SC - O(S) where S and O are the len of strings "s" and "order"
    '''
    def customSortString(self, order: str, s: str) -> str:
        c = collections.Counter(s)
        res = ""

        for char in order:
            if char in c:
                res += char * c[char]
        
        for char in s:
            if char not in order:
                res += char
        
        return res