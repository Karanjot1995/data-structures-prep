class Solution:
  def findMissingRanges(self, nums, lower: int, upper: int):
    if not nums: return [[lower,upper]]

    n = len(nums)
    arr = []

    if nums[0]>lower:
      arr.append([lower,nums[0]-1])
   
    for i in range(n-1):
      if nums[i+1] - nums[i] != 1:
        arr.append([nums[i]+1, nums[i+1]-1])
    
    if nums[-1]<upper:
      arr.append([nums[-1]+1,upper])

    '''
    ONLY DO THIS FOR FOLLOW UP QUESTION
    result = []
    for i in range(len(ans)):
        start, end = ans[i]

        if start == end:
            result.append(str(start))
        elif end - start >= 2:
            result.append(str(start) + "-" + str(end))
        else:
            result.append(str(start))
            result.append(str(end))
    return result
    '''
      
    return arr
  
'''
FOLLOW UP:

Variation of Missing Ranges where missing elements are less than or equal to 2, add them individually. Otherwise add a hyphen for the missing range

So for array = [2, 3, 6, 11, 13, 18, 75], lower = 0, upper = 99, we should return [0,1,4,5,7-10,12,14-17,19-74,76-99]

https://leetcode.com/discuss/interview-question/4694803/Meta-Interview-On-site
'''
def missingRanges(input, low, high):
	res= []

	for n in input:
		if n - low > 2:
			res.append(str(low)+'-'+str(n-1))
		else:
			while low < n:
				res.append(str(low))
				low += 1

		low = n+1

	if low <= high:
		if high - low > 2:
			res.append(str(low)+'-'+str(high))
		else:
			while low <= high:
				res.append(str(low))
				low += 1

	return res

print(missingRanges([2, 3, 6, 11, 13, 18, 75], 0, 99))



        


