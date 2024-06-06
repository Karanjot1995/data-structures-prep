from collections import defaultdict

class Solution:
  def findJudge(self, n: int, trust) -> int:
    if len(trust)<n-1: return -1
    trust_map = [0] * (n + 1)

    for a,b in trust:
      trust_map[a]-=1
      trust_map[b]+=1

    for i, score in enumerate(trust_map[1:],1):
      if score == n-1: return i
    return -1


  def findJudge(self, n: int, trust) -> int:
    if len(trust)<n-1: return -1

    indegree = [0]*(n+1)
    outdegree = [0]*(n+1)

    for a,b in trust:
      outdegree[a]+=1
      indegree[b]+=1

    for i in range(1,n+1):
      if indegree[i]==n-1 and outdegree[i]==0:
        return i
    
    return -1


  