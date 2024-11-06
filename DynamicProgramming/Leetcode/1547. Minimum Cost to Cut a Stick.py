def minCost(n, cuts):
  c = len(cuts)
  cuts.append(0)
  cuts.append(n)
  cuts.sort()
  def rec(i,j):
    if i > j: return 0
    min_cost = float("inf")
    # cost = cuts[j+1] - cuts[i-1] #cost/length
    for k in range(i,j+1):
      tot_cost = cuts[j+1] - cuts[i-1] + (rec(i,k-1) + rec(k+1,j))
      min_cost = min(min_cost, tot_cost)
    return min_cost

  return rec(1,c)
 #    0 ,1 ,3, 4, 5, 7
 #i = 0 |1  2  3  4| 5

n = 7
cuts = [1,3,4,5]
print(minCost(n, cuts))


'''
Let m be the length of the input array cuts.

Time complexity: O(m3)
The number of states in our DP is the number of possible combinations of (left, right), which is O(m2) subproblems. 
For each subproblem cost(left, right), we need to try all possible cutting positions between new_cuts[left] and new_cuts[right], 
resulting in an additional factor of m. Therefore, the overall time complexity is O(m3).

Space complexity: O(m2)

We need to store the solutions for all (m2) subproblems in memory.
'''

def minCostMemo(n, cuts):
  c = len(cuts)
  cuts.append(0)
  cuts.append(n)
  cuts.sort()
  dp = [[-1 for _ in range(c+1)] for _ in range(c+1)]
  def rec(i,j):
    if i > j: return 0
    if dp[i][j]!=-1: return dp[i][j]
    min_cost = float("inf")
    for k in range(i,j+1):
      tot_cost = cuts[j+1] - cuts[i-1] + (rec(i,k-1) + rec(k+1,j))
      min_cost = min(min_cost, tot_cost)
    dp[i][j] = min_cost
    return dp[i][j]

  return rec(1,c)


n = 7
cuts = [1,3,4,5]
print(minCostMemo(n, cuts))


def minCostTab(n, cuts):
  c = len(cuts)
  cuts.append(0)
  cuts.append(n)
  cuts.sort()
  dp = [[0 for _ in range(c+2)] for _ in range(c+2)]

  for i in range(c,0,-1): #n->1
    for j in range(1,c+1): #1->n
      if i>j: continue
      min_cost = float("inf")
      for k in range(i,j+1):
        tot_cost = cuts[j+1] - cuts[i-1] + dp[i][k-1] + dp[k+1][j]
        min_cost = min(min_cost, tot_cost)
      dp[i][j] = min_cost
  return dp[1][c]


n = 7
cuts = [1,3,4,5]
print(minCostTab(n, cuts))