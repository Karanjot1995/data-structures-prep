# https://leetcode.com/problems/interval-list-intersections/description/

class Solution:
    '''
    SPECIAL CASE: overlapping at 1 point ONLY
    a = [[1, 8], [12, 16]]
    b = [[8, 10]]

    Whill [[8, 8]] be an interval??

    There will be 3 cases where intersection can be possible
    1) CASE I: s1 <= e2 and s2 <= e1
            s2---------e2
      s1----------e1
    
    2) CASE II: s1 <= e2 and s2 <= e1
            s2---------e2
                s1----------e1
    
    3) CASE III: s1 <= e2 and s2 <= e1
                  s2---------e2
      s1----------e1
    
    So intersection = [max(s1, s2), min(e1, e2)]

    Video - https://www.youtube.com/watch?v=Qh8ZjL1RpLI&ab_channel=Techdose
    
    TC - O(N + M)
    SC - O(N + M)
    '''
    def intervalIntersection(self, firstList, secondList):
        i = j = 0
        ans = []

        while i < len(firstList) and j < len(secondList):
            i_start, i_end = firstList[i]
            j_start, j_end = secondList[j]

            # intersection will happen only for this condition
            if i_start <= j_end and j_start <= i_end:
                low = max(i_start, j_start)
                high = min(i_end, j_end)
                
                ans.append([low, high])
            # lo = max(i_start, j_start)
            # hi = min(i_end, j_end)
            # if lo<=hi: ans.append([lo,hi])
            
            # increment based on the end times of the interval
            if i_end <= j_end:
                i += 1
            else:
                j += 1
        
        return ans

