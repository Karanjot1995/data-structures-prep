# Alien Dictionary
#dict = {"baa","abcd","abca","cab","cad"}
def findOrder(alien_dict, N, K):
  adj=[[] for _ in range(K)]
  # in_degree = [0]*K

  for i in range(N-1):
    s1,s2 = alien_dict[i], alien_dict[i+1]
    l = min(len(s1), len(s2))
    for j in range(l):
      if s1[j]!=s2[j]:
        n1,n2 = ord(s1[j]) - 97,ord(s2[j]) - 97 
        # print(n1,n2)
        adj[n1].append(n2)
        # in_degree[n2]+=1
        break
  print(adj)

  def topo_sort(graph):
    in_degree=[0]*K
    for i in range(K):
      for j in adj[i]:
        in_degree[j]+=1
    
    q=list()
    topo_sort = []
    for i in range(K):
      if in_degree[i]==0:
        q.append(i)

    while q:
      curr = q.pop(0)
      topo_sort.append(curr)
      for neighbor in graph[curr]:
        in_degree[neighbor]-=1
        if in_degree[neighbor]==0:
          q.append(neighbor)

    return topo_sort
  
  topo=topo_sort(adj)
  
  ans=list()
  for i in topo:
      ans.append(chr(97+i))
  return ans

print(findOrder(["baa","abcd","abca","cab","cad"],5,4))


def alienOrder(words):
  adj=[[] for _ in range(26)]
  indegree = {}
  for w in words:
    for c in w: indegree[ord(c) - ord("a")] = 0

  N = len(words)
  for i in range(N-1):
    s1,s2 = words[i], words[i+1]
    l = min(len(s1), len(s2))
    j=0
    while j < len(s1) and j < len(s2):
      if s1[j]!=s2[j]:
        n1,n2 = ord(s1[j]) - 97,ord(s2[j]) - 97 
        adj[n1].append(n2)
        indegree[n2]+=1
        break
      j+=1
    if j == len(s2) and j < len(s1): return ""

  #topo sort
  q = []
  for node in indegree:
    if indegree[node]==0:
      q.append(node)
  

  res = ''
  while q:
    curr = q.pop(0)
    char = chr(97+curr)
    res+=char
    for nb in adj[curr]:
      indegree[nb]-=1
      if indegree[nb]==0: q.append(nb)

  return res if sum(indegree.values()) == 0 else ""


print(alienOrder(["baa","abcd","abca","cab","cad"]))