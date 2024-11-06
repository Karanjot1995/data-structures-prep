# https://www.naukri.com/code360/problems/unbounded-knapsack_1215029?

def unboundedKnapsack(n: int, w: int, profit: List[int], weight: List[int]) -> int:
    dp = [[-1 for _ in range(w+1)] for _ in range(len(weight))]

    def rec(i, rem):
        # if rem<0: return 0
        if i == len(weight)-1:
            if weight[i]<=rem: return rem//weight[i] * profit[i]
            return 0
        if dp[i][rem] != -1: return dp[i][rem]
        take = float("-inf")
        if weight[i]<=rem:
            take = profit[i] + rec(i, rem-weight[i])
        not_take = 0+rec(i+1,rem)
        dp[i][rem] = max(take, not_take)
        return max(take, not_take)
        
    return rec(0, w)