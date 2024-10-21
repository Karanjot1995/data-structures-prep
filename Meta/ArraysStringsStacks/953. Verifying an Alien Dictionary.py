# https://leetcode.com/problems/verifying-an-alien-dictionary/description/

class Solution:
    '''
    APPROACH: Compare char by char
    
    1) We first create an order_map which for each char in order will let us know its index which tells us which chars comes first
    2) We compare 2 words char by char at a time
    3) If the chars differ we check the order of the chars in the 2 words and which comes first, if the order is valid we move on else we return False
    4) One case that we have to keep track of is if w2 is a prefix of w1 for ex: w1 = hello and w2 = he => then w2 should come first
    
    SPECIAL CASE - w2 is prefix of w1; Ex: w1 = hello, w2 = he
    
    TC - O(M)
    SC - O(k) where k is constant as order string will have at most 26 chars
    '''
    def isAlienSorted(self, words, order: str) -> bool:
        order_map = { val: idx for idx, val in enumerate(order) }
        
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]

            for j in range(len(w1)):
                # reached the end of w2 first so w2 might be the prefix of w1
                # w1 = hello, w2 = he
                if j >= len(w2):
                    return False
                
                if w1[j] != w2[j]:
                    if order_map[w2[j]] < order_map[w1[j]]:
                        return False
                    break
        return True
    
