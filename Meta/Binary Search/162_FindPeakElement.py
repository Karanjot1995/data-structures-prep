#TC - logN , SC - O(1)
def findPeakElement(nums):
  n = len(nums)
  if n==1: return 0
  if nums[0]>nums[1]: return 0
  if nums[n-1]>nums[n-2]: return n-1

  l = 1
  r = n-1

  while l<=r:
    mid = (l+r)//2
    if nums[mid]>nums[mid+1]: r = mid-1
    else: l = mid+1

  # while l<=r:
  #   mid = (l+r)//2
  #   if nums[mid-1]<nums[mid]>nums[mid+1]:
  #     return mid
  #   elif nums[mid-1]>nums[mid]: r = mid-1
  #   else: l=mid+1

  return l


# TC -> O(N)
def findPeakElement2(nums):
  for i in range(0,len(nums)-1):
    if nums[i]>nums[i+1]:
      return i
  return len(nums)-1


# my approach
def findPeakElement3(nums):
  maxi = 0
  for i in range(1,len(nums)-1):
    if nums[i-1]<nums[i]>nums[i+1]:
      return i
  return len(nums)-1 if nums[-1]>nums[0] else 0
                  
nums = [1,2,1,3,5,6,4]
print(findPeakElement(nums))
#op = idx 5 (el = 6)



'''
ALTERNATE QUESTION TO THIS - FIND LOCAL MINIMA (https://www.geeksforgeeks.org/find-local-minima-array/)
'''

'''
APPROACH - Brute Force

TC - O(N)
SC - O(1)
'''
def findLocalMinima(nums):
    n = len(nums)

    for i in range(n):
        if (i == 0 or nums[i] < nums[i - 1]) and (i == n - 1 or nums[i] < nums[i + 1]):
            return i
    return -1

def findLocalMinima1(nums):
    for i in range(len(nums) - 1):
        if nums[i] <= nums[i + 1]:
            return i
    return len(nums) - 1

'''
APPROACH - Binary Search

TC - O(logN)
SC - O(1)
'''
def findLocalMinimaBinarySearch(nums):
    N = len(nums)

    if N == 1: return 0
    if nums[0] < nums[1]: return 0
    if nums[N - 1] < nums[N - 2]: return N - 1
    
    start = 1
    end = N - 2
    
    while start <= end:
        mid = (end + start) // 2
        if nums[mid] < nums[mid + 1] and nums[mid] < nums[mid - 1]:
            return mid
        elif nums[mid - 1] > nums[mid]:
            start = mid + 1
        else:
            end = mid - 1
    return -1

# print(findLocalMinima([4, 3, 1, 14, 16, 40]))
print(findLocalMinima([3, 2, 1, 4, 5, 2, 6]))