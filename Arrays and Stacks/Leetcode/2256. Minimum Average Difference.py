# TC -> O(N), SC -> O(N)
def minimumAverageDifference(nums) -> int:
  if not nums or len(nums)==0: return 0
  n = len(nums)
  avg = float('inf')
  ans = -1
  # Generate prefix and suffix sum arrays.
  prefix_sum = [0] * (n + 1)
  suffix_sum = [0] * (n + 1)
  
  for i in range(n):
    prefix_sum[i + 1] = prefix_sum[i] + nums[i]
    suffix_sum[n-1-i] = suffix_sum[n-1-i+ 1] + nums[n-1-i]
  
  # for i in range(n - 1, -1, -1):
  #   suffix_sum[i] = suffix_sum[i + 1] + nums[i]

  for i in range(n):
    left = prefix_sum[i+1]
    left_avg = left//(i+1)

    right = suffix_sum[i+1]
    right_avg = right
    if i != n - 1: right_avg = right//(n-i-1)

    curr_avg = abs(left_avg - right_avg)
    
    if curr_avg < avg:
      avg = curr_avg
      ans = i
  return ans
      
#space optimised O(1)
def minimumAverageDifference(nums) -> int:
  n = len(nums)
  ans = -1
  min_avg_diff = float('inf')
  curr_prefix_sum = 0
  total_sum = 0
  for index in range(n):
    total_sum += nums[index]
  
  for index in range(n):
    curr_prefix_sum += nums[index]
    
    left_part_average = curr_prefix_sum
    left_part_average //= (index + 1)
      
    right_part_average = total_sum - curr_prefix_sum
    if index != n - 1:
      right_part_average //= (n - index - 1)
    
    curr_difference = abs(left_part_average - right_part_average)
    if curr_difference < min_avg_diff:
      min_avg_diff = curr_difference
      ans = index
          
  return ans
    
  