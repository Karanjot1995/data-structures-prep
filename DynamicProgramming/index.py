# when the problem statement will say count all ways, count/try all possible ways, count distinct ways,
# what gives you the minimum or max output then we apply recursion
# shortcut
# try to represent the problem in terms of an index
# do all possible stuffs on that index according to the problem statement
# if the question says count all ways -> sum up all the stuffs
# eg ->  ques says find min/max => take min/max of all stuffs



def fib(num):
  if num <=1: return num
  return fib(num-1)+fib(num-2)
print(fib(7))


# def fibDP(num):
#   hmap = {}

#   def fib(num):
#     if num in hmap: return hmap[num]
#     if num <=1: 
#       return num
#     op = fib(num-1)+fib(num-2)
#     hmap[num] = op
#     return op
  
#   return fib(num)


#memoization (TOP DOWN)
def fibDP(n):
  dp = [-1]*(n+1)

  def fib(num):
    if num <=1: return num
    if dp[num]!=-1: return dp[num]
    op = fib(num-1)+fib(num-2)
    dp[num] = op
    return op
  
  return fib(n)

print('solved by Memoization: ',fibDP(7))



#Tabulation (Bottom Up)
def fibDP2(n):
  dp = [-1]*(n+1)
  dp[0] = 0
  dp[1] = 1

  for i in range(2,n+1):
    dp[i] = dp[i-1]+dp[i-2]

  print(dp)
  return dp[n]
  
print('solved by Tabulation: ',fibDP2(7))



#Tabulation (Bottom Up) constant space
def fibDP3(n):
  prev2 = 0 
  prev = 1
  for i in range(2,n+1):
    curr = prev+prev2
    prev2 = prev
    prev = curr
  return prev
  
print('solved by Space Optimized DP: ',fibDP3(7))