#memoization, O(N) Space
def frogJump(n, heights) -> int:

    # Write your code here.
    dp = [-1]*(n)
    def jump(i):
        if i == 0: return 0
        if dp[i] != -1: return dp[i]

        jump1 = jump(i-1) + abs(heights[i]-heights[i-1])
        jump2 = float('inf')
        if i>1:
            jump2 = jump(i-2)+abs(heights[i]-heights[i-2])
        
        dp[i] = min(jump1,jump2)
        
        return min(jump1,jump2)
    ans = jump(n-1)
    print(dp)
    return ans

    # dp = [-1]*(n+1)
    # def jump(i):
    #     if i >= n-1: return 0
    #     if dp[i] != -1: return dp[i]
    #     jump1 = jump2 = float('inf')
    #     if i<n-1: jump1 = jump(i+1) + abs(heights[i]-heights[i+1])
    #     if i<n-2: jump2 = jump(i+2)+abs(heights[i]-heights[i+2])
    #     dp[i] = min(jump1,jump2)
        
    #     return min(jump1,jump2)

    # return jump(0)

print(frogJump(4, [10,20,30,10]))


#tabulation , O(N) Space
def frogJump2(n, heights) -> int:
    dp = [-1]*(n)
    dp[0] = 0

    for i in range(1,n):
      jump1 = dp[i-1] + abs(heights[i]-heights[i-1])
      jump2 = float('inf')
      if i > 1:
        jump2 = dp[i-2] + abs(heights[i]-heights[i-2])
      dp[i] = min(jump1,jump2)

    print(dp)
    return dp[n-1]


print(frogJump2(4, [10,20,30,10]))



#tabulation , O(1) Space
def frogJump3(n, heights) -> int:
    prev2 = 0
    prev1 = 0

    for i in range(1,n):
      jump1 = prev1 + abs(heights[i]-heights[i-1])
      jump2 = float('inf')
      if i > 1:
        jump2 = prev2 + abs(heights[i]-heights[i-2])

      prev2 = prev1
      prev1 =  min(jump1,jump2)

    return prev1


print(frogJump3(4, [10,20,30,10]))




# memoization K jumps
def frogJumpK(n, heights,k) -> int:

    # Write your code here.
    dp = [-1]*(n+1)
    def jump(i):
        # nonlocal k
        if i == 0: return 0
        if dp[i] != -1: return dp[i]

        min_jmp = float('inf')
        for j in range(1,k+1):
          if i-j>=0:
            jmp = jump(i-j)+abs(heights[i]-heights[i-j])
          min_jmp = min(min_jmp, jmp)
        dp[i] = min_jmp
        return min_jmp

    return jump(n-1)

print('K Jumps: ', frogJumpK(4, [10,20,30,10],2))


#tabulation , O(N) Space
def frogJumpK2(n, heights,k) -> int:
    dp = [-1]*(n)
    dp[0] = 0

    for i in range(1,n):
      min_jmp = float('inf')
      for j in range(1,k+1):
         if i-j>=0:
          jmp = dp[i-j] + abs(heights[i]-heights[i-j])
          min_jmp = min(jmp,min_jmp)
      dp[i] = min_jmp

    return dp[n-1]


print(frogJumpK2(4, [10,20,30,10],2))