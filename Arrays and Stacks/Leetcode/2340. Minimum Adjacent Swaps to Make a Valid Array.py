def minimumSwaps(nums) -> int:
  mini = min(nums)
  idx1 = nums.index(mini)  
  #swap that min num
  nums = [nums[idx1]] + nums[:idx1] + nums[idx1+1:]

  maxi = max(nums)
  idx2 = nums[::-1].index(maxi)  

  return idx1+idx2



def minimumSwaps2(nums) -> int:
  n = len(nums)
  min_swaps = 0
  mini = float('inf')
  for i in range(n-1,-1,-1):
    if nums[i]<=mini:
      mini = nums[i]
      min_swaps = 0
    else: min_swaps+=1
  #swap the elem
  nums = [nums[min_swaps]] + nums[:min_swaps] + nums[min_swaps+1:]

  max_swaps = 0
  maxi = -float('inf')
  for i in range(n):
    if nums[i]>=maxi:
      maxi = nums[i]
      max_swaps = 0
    else: max_swaps+=1

  return min_swaps+max_swaps