# https://leetcode.com/problems/product-of-two-run-length-encoded-arrays/description/

'''
APPROACH 1: BRUTE FORCE
- Spread out both the encoded arrays using 2 new arrays and then multiply them (2 iterations)
- Calculate the run length encoding (compress) for the resulting array and return (2 iterations)
'''

class Solution:
    '''
    APPROACH 2: MOST OPTIMAL

    ALGORITHM
    1) Take 2 pointers "i" for encoded1 and "j" for encoded2
    2) We iterate over them --- and extract the val and freq from both the arrays
    3) If the freq matches we simply multiply the values and store that product with the freq to the solution
        - in this case we can move both "i" and "j" by one
    4) If the freq do not match we multiply the values and we take the min(freq1, freq2) and add that to our solution
        - We also have to keep in mind that the product that we got if that matches the prev product we increase prev 
          products freq instead of adding it to the solution
    5) In the case that freq does not match we want to move the pointer that has fully exhausted the freq and decrement
       the other pointer's freq by min(freq1, freq2)
    6) We do this till we finish analysing all the arrays

    TC - O(N + M) we have to traverse both encoded1 and encoded2
    SC - O(N + M) worst case will be we have all the elements from encoded1 and encoded2
    
    Video - https://www.youtube.com/watch?v=_YBijp-C63A&ab_channel=CrackingFAANG
    '''
    def findRLEArray(self, encoded1, encoded2):
        i = j = 0
        ans = []

        while i < len(encoded1) and j < len(encoded2):
            val1, freq1 = encoded1[i]
            val2, freq2 = encoded2[j]

            product = val1 * val2
            freq = min(freq1, freq2)

            # check if product is equal to the prev product
            if not ans or product != ans[-1][0]:
                ans.append([product, freq])
            else:
                ans[-1][1] += freq
            
            encoded1[i][1] -= freq
            encoded2[j][1] -= freq

            if freq1 == freq:
                i += 1
            
            if freq2 == freq:
                j += 1
        return ans


class Solution:
  def findRLEArray(self, encoded1, encoded2):
    m,n = len(encoded1), len(encoded2)
    i,j=0,0
    res = []
    while i<m and j<n:
      val = encoded1[i][0]*encoded2[j][0]
      if encoded1[i][1]==encoded2[j][1]:
        res.append([val, encoded1[i][1]])
        i+=1
        j+=1
      elif encoded1[i][1] > encoded2[j][1]:
        res.append([val, encoded2[j][1]])
        encoded1[i][1]-=encoded2[j][1]
        j+=1
      else:
        res.append([val, encoded1[i][1]])
        encoded2[j][1]-=encoded1[i][1]
        i+=1
      if len(res)>1 and res[-2][0]==res[-1][0]:
        res[-2][1]+=res[-1][1]
        res.pop()
    return res