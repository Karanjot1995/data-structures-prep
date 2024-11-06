def countPartitions(n: int, d: int, nums: List[int]) -> int:
    MOD = 10 ** 9 + 7

    # write your code here
    n = len(nums)
    # if sum(nums)/2
    if (sum(nums)-d)<0: return 0
    if (sum(nums)-d)%2==1: return 0
    k = (sum(nums)-d)//2


    dp = [[-1 for _ in range(k+1)] for _ in range(n)]
    def rec(i,rem):
        if i == 0:
            if rem == 0 and nums[0] == 0: return 2
            if rem == 0 or rem == nums[0]: return 1
            return 0

        if dp[i][rem]!=-1: return dp[i][rem]
        take = 0
        if rem>=nums[i]: take = rec(i-1,rem-nums[i])
        not_take = rec(i-1,rem)
        dp[i][rem] = (take + not_take)%MOD

        return dp[i][rem]

    res = rec(n-1,k)
    return res


d = 3
nums = [5,2,6,4]