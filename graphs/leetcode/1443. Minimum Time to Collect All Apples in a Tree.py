from collections import defaultdict

class Solution:
  def minTime(self, n: int, edges, hasApple) -> int:
    if n==0 or not edges: return 0
    adj = defaultdict(list)
    for v1,v2 in edges:
      adj[v1].append(v2)
      adj[v2].append(v1)

    # print(adj)
    def dfs(node,parent):
      totalTime,childTime = 0,0

      for child in adj[node]:
        if child == parent: continue
        childTime = dfs(child, node)

        if childTime or hasApple[child]:
          totalTime+=childTime+2

      return totalTime

    return dfs(0,-1)

        