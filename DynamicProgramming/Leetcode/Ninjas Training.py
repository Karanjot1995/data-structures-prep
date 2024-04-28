
#memoization from right to left
def ninjasTraining(n,points) -> int:
  m = 3
  dp = [[-1 for j in range(4)] for i in range(n)]

  def rec(day,last):
    if dp[day][last] != -1: return dp[day][last]

    # Base case: When we reach day 0, return the maximum point for the last day.
    if day == 0:
        maxi = 0
        for i in range(3):
            if i != last: maxi = max(maxi, points[0][i])
        dp[day][last] = maxi
        return dp[day][last]

    maxi = 0
    # Iterate through all activities for the current day.
    for i in range(3):
      if i != last:
        # Calculate the total points for the current day's activity and recursively call for the previous day.
        activity = points[day][i] + rec(day - 1, i)
        maxi = max(maxi, activity)

    # Store the maximum points in the DP table and return it.
    dp[day][last] = maxi
    return dp[day][last]

  return rec(n-1,m)


points = [[1,2,5], [3 ,1 ,1] ,[3,3,3], [0,3,6] ]
# points = [[10,30,20],[10,20,30],[10,30,20]]
print(ninjasTraining(4,points))






#tabulation
def ninjasTraining2(n,points) -> int:
  m = 3

  dp = [[0 for j in range(4)] for i in range(n)]

  dp[0][0] = max(points[0][1], points[0][2])
  dp[0][1] = max(points[0][0], points[0][2])
  dp[0][2] = max(points[0][0], points[0][1])
  dp[0][3] = max(points[0][0], max(points[0][1], points[0][2]))

  for day in range(1,n):
    for last in range(m+1):
      # dp[day][last] = 0
      maxi = 0
      for task in range(m):
        if task != last:
          pts = points[day][task] + dp[day-1][task]
          maxi = max(maxi,pts)
      dp[day][last] = maxi

  print(dp)
  return dp[n-1][3]


points = [[1,2,5], [3 ,1 ,1] ,[3,3,3], [0,3,6] ]
# points = [[10,30,20],[10,20,30],[10,30,20]]
print(ninjasTraining2(4,points))