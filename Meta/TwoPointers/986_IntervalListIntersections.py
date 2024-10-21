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
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        if not firstList or not secondList: return []

        n = max(len(firstList), len(secondList))
        i = j = 0

        ans = []
        while i<len(firstList) and j <len(secondList):
            lo = max(firstList[i][0], secondList[j][0])
            hi = min(firstList[i][1], secondList[j][1])
            if lo<=hi: ans.append([lo,hi])

            if firstList[i][1]<secondList[j][1]: i+=1
            else: j+=1

        return ans

