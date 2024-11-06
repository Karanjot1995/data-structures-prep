def maxSumAfterPartitioning(arr, k: int):
  n = len(arr)
  def rec(i):
    if i == n: return 0
    maxi = float("-inf")
    max_sum = float("-inf")
    length = 0
    for j in range(i,min(i+k,n)):
      length+=1
      maxi = max(maxi, arr[j]) #eg 15,7,9 max is 15 so it becomes 15, 15, 15 and sum is 3*15 + rec()
      sum = length*maxi + rec(j+1)
      max_sum = max(max_sum, sum)
    return max_sum

  return rec(0)

arr = [1,15,7,9,2,5,10]
k = 3
print(maxSumAfterPartitioning(arr,k))



def maxSumAfterPartitioningMemo(arr, k):
  n = len(arr)
  dp = [-1]*(n)
  def rec(i):
    if i == n: return 0
    if dp[i]!=-1: return dp[i]
    maxi = float("-inf")
    max_sum = float("-inf")
    length = 0
    for j in range(i,min(i+k,n)):
      length+=1
      maxi = max(maxi, arr[j]) #eg 15,7,9 max is 15 so it becomes 15, 15, 15 and sum is 3*15 + rec()
      sum = length*maxi + rec(j+1)
      max_sum = max(max_sum, sum)
    dp[i] = max_sum
    return dp[i]

  return rec(0)

arr = [1,15,7,9,2,5,10]
k = 3
print(maxSumAfterPartitioningMemo(arr,k))




def maxSumAfterPartitioningTab(arr, k):
  n = len(arr)
  dp = [0]*(n+1)
  for i in range(n-1,-1,-1):
    maxi = float("-inf")
    max_sum = float("-inf")
    length = 0
    for j in range(i,min(i+k,n)):
      length+=1
      maxi = max(maxi, arr[j]) #eg 15,7,9 max is 15 so it becomes 15, 15, 15 and sum is 3*15 + rec()
      sum = length*maxi + dp[j+1]
      max_sum = max(max_sum, sum)
    dp[i] = max_sum
      
  return dp[0]

arr = [1,15,7,9,2,5,10]
k = 3
print(maxSumAfterPartitioningTab(arr,k))