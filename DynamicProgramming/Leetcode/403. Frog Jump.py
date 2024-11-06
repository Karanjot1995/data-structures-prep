class Solution:
  def canCross(self, stones: List[int]) -> bool:
    if stones[1] != 1: return False

    dp = {}

    def jump(i,k):
      if i == len(stones)-1: return True
      if (i,k) in dp: return dp[(i,k)]

      res = False
      for j in range(i+1, len(stones)):
        if stones[i]+k-1 == stones[j]:
          res = res or jump(j,k-1)
        if stones[i]+k == stones[j]:
          res = res or jump(j,k)
        if stones[i]+k+1 == stones[j]:
          res = res or jump(j,k+1)
      
      dp[(i,k)] = res
      return res

    return jump(1,1)


        