from collections import defaultdict, deque


class Solution:
  def alienOrder(self, words) -> str:
    adj = defaultdict(set)
    indegree = {}
    for w in words:
      for c in w: indegree[c] = 0

    for i in range(len(words)-1):
      w1, w2 = words[i], words[i+1]
      j = 0
      while j<len(w1) and j<len(w2):
        c1,c2 = w1[j], w2[j]
        if c1!=c2:
          adj[c1].add(c2)
          indegree[c2]+=1
          break
        j+=1
      if j==len(w2) and j<len(w1): return ""

    res = ''
    q = deque()
    for node in indegree:
      if indegree[node] == 0:
        q.append(node)

    while len(q):
      node = q.popleft()
      res+=node
      for nb in adj[node]:
        indegree[nb]-=1
        if indegree[nb]==0:
          q.append(nb)
    
    return res if sum(indegree.values()) == 0 else ""

    

      












    # adj=[[] for _ in range(26)]
    # indegree = {}
    # for w in words:
    #   for c in w: indegree[ord(c) - ord("a")] = 0
    
    # print(indegree)
    # N = len(words)
    # for i in range(N-1):
    #   s1,s2 = words[i], words[i+1]
    #   l = min(len(s1), len(s2))
    #   j=0
    #   while j < len(s1) and j < len(s2):
    #     if s1[j]!=s2[j]:
    #       n1,n2 = ord(s1[j]) - 97,ord(s2[j]) - 97 
    #       adj[n1].append(n2)
    #       indegree[n2]+=1
    #       break
    #     j+=1
    #   if j == len(s2) and j < len(s1): return ""

    # print(indegree)
    # #topo sort
    # q = []
    # for node in indegree:
    #   if indegree[node]==0:
    #     q.append(node)
    

    # res = ''
    # while q:
    #   curr = q.pop(0)
    #   char = chr(97+curr)
    #   res+=char
    #   for nb in adj[curr]:
    #     indegree[nb]-=1
    #     if indegree[nb]==0: q.append(nb)

    # return res if sum(indegree.values()) == 0 else ""






        