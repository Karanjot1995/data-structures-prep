def findItinerary(tickets):
  start = "JFK"
  adj = {}
  res = []
  for ticket in tickets:
    adj[ticket[0]] = []
    adj[ticket[1]] = []

  for ticket in tickets:
    adj[ticket[0]].append(ticket[1])
    adj[ticket[0]].sort()
    # adj[ticket[0]].reverse() #for bfs
  print(adj)

  def dfs(node):
    while adj[node]:
      dfs(adj[node].pop(0))
    res.append(node)
  dfs("JFK")
  return res[::-1] 

  # print(adj)
  # q = [start]

  # while q:
  #   print(q,res)
  #   while adj[q[-1]]:
  #     q.append(adj[q[-1]].pop())
  #   res.append(q.pop())
  # return res[::-1]
  
tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
print(findItinerary(tickets))
#op = ["JFK","MUC","LHR","SFO","SJC"]

