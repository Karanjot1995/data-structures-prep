import math
#If the array is sorted or there are 2 pointers.
#I. Order Agnostic Search
#II. Find the range of occurrence of an element in a sorted array :
#III. Frequency of an element in a sorted array :
#IV. Find the number of times a sorted array is rotated :
#V. Find an element in a rotated sorted array :
#VI. Searching in a nearly sorted array :
#VII. Find floor of an element in a sorted array
#VIII. Find ceil of an element in a sorted array
#
#


#Template
# while left < right :
# 	if condition is true:
# 		right = mid 
# 	else:
# 		left = mid +1

def binarySearch(nums, target):
    start = 0
    end = len(nums)-1

    while start<=end:
      mid = int((start+end)/2)
      #mid = int(start + (end-start)/2)
      if target==nums[mid]:
        return mid
      elif target<nums[mid]:
        end = mid-1
      else:
         start = mid+1
    return -1
    # print(mid)

print(binarySearch([1,2,3,4,5,6,7,8,9],7))

def binarySearchReverse(nums, target):
    mid = int(len(nums)/2)

    start = 0
    end = len(nums)-1

    while start<=end:
      mid = int((start+end)/2)
      #mid = int(start + (end-start)/2)
      if target==nums[mid]:
        return mid
      elif target<nums[mid]:
        start = mid+1
      else:
         end = mid-1
    return -1
    # print(mid)

print(binarySearchReverse([9,8,7,6,5,4,3,2,1],1))

# def orderAgnosticSearch(nums):
#   if len(nums)==1:
#     return nums[0]
   
#   if nums[0]<nums[1]:
#     binarySearch(nums)
#   else:
#     binarySearchReverse(nums)

def firstOccurance(nums,target):
  start = 0
  end = len(nums)-1
  idx = -1
  while start<=end:
    mid = int((start+end)/2)
    #mid = int(start + (end-start)/2)
    if target==nums[mid]:
      idx=mid
      end = mid-1 #first occurance
    elif target<nums[mid]:
      end = mid-1
    else:
        start = mid+1
  return idx

def lastOccurance(nums,target):
  start = 0
  end = len(nums)-1
  idx = -1
  while start<=end:
    mid = int((start+end)/2)
    if target==nums[mid]:
      idx=mid
      start = mid+1 #last occurance
    elif target<nums[mid]:
      end = mid-1
    else:
        start = mid+1
  return idx


def countOccurances(nums,target):
  first = firstOccurance(nums,target)
  last = lastOccurance(nums,target)
  return last-first+1
    
print(countOccurances([2,4,10,10,10,10,18,20],10))




def findMin(nums):
  start = 0
  end = len(nums)-1
  while start<=end:
    mid = int((start+end)/2)
    if(nums[start] <= nums[end]): return nums[start]
    if nums[mid]>nums[end]:
      start = mid+1
    elif nums[mid]<nums[start]:
      end = mid
  return -1
  # return idx

print(findMin([11,12,15,18,19,20,2,5,6,8]))
# print(findMin([3,4,5,1,2]))
# print(findMin([11,13,15,17]))

# def checkMinIdx(nums):
#   start = 0
#   end = len(nums)-1
#   n = len(nums)
#   while start<=end:
#     mid = int((start+end)/2)
#     next = (mid+1)%n
#     prev = (mid+n-1)%n
#     pivot = 0
#     if nums[mid]<=nums[prev] and nums[mid]<=nums[next]:
#       pivot = mid
#       break
#     if nums[start]<=nums[mid]:
#       start = mid
#     elif nums[mid]<=nums[end]:
#       end = mid
#   return pivot

# print(checkMinIdx([11,13,15,17]))



def bs(nums,target):
    start = 0
    end = len(nums)-1
    while start<=end:
      mid = int((start+end)/2)
      if target==nums[mid]:
        return mid
      elif target<nums[mid]:
        end = mid-1
      else:
         start = mid+1
    return -1

def searchRotated(nums, target):
  start = 0
  end = len(nums)-1
  n = len(nums)
  pivot = 0
  while start<=end:
    mid = int((start+end)/2)
    if(nums[start] <= nums[end]): 
      pivot = start
      break
    if nums[mid]>nums[end]:
      start = mid+1
    elif nums[mid]<nums[start]:
      end = mid

  idx = -1
  idx1 = bs(nums[0:pivot],target)
  idx2 = bs(nums[pivot:len(nums)],target)
  if idx1!=-1:
    idx = idx1
  elif idx2!=-1:
    idx = pivot+idx2
  return 'idx of elem in rotated array:' ,idx

print(searchRotated([4,5,6,7,0,1,2], 4))

#  or
def searchRot(self, nums, target):
    start, end = 0, len(nums)-1
    while start <= end:
        mid = int((start+end)/2)
        if nums[mid] == target:
            return mid
        if nums[mid]>=nums[start]:
            if target>=nums[start] and target<=nums[mid]:
                end = mid-1
            else:
                start = mid+1
        else:
            if target>=nums[mid] and target<=nums[end]:
                start = mid+1
            else:
                end = mid-1

    return -1


def nearlySortedSearch(arr,target):
  start = 0
  end = len(arr)-1
  while start<=end:
    mid = int((start+end)/2)
    if target == arr[mid]:
       return mid
    elif mid-1>= start and target == arr[mid-1]:
       return mid-1
    elif mid+1<= end and target == arr[mid+1]:
       return mid+1
    elif target < arr[mid-1]:
       end = mid-2
    else:
       start = mid+2
    # else:
    #    return target
  return -1

print(nearlySortedSearch([1,2,3,4,7,5,12,15,19,22,21,23,24],5))


def floorOfElement(arr, target):
  start = 0
  end = len(arr)-1
  floor = arr[start]
  while start<=end:
    mid = int((start+end)/2)
    if target == arr[mid]:
      return target      
    if target < arr[mid]:
      end = mid-1
    elif target > arr[mid]:
      floor = max(floor, arr[mid])
      start = mid+1
  return floor
   
print(floorOfElement([1,2,3,4,7,12,15,19,21,22,23,25],6))


def ceilOfElement(arr, target):
  start = 0
  end = len(arr)-1
  ceil = arr[end]
  while start<=end:
    mid = int((start+end)/2)
    if target == arr[mid]:
      return target      
    if target < arr[mid]:
      ceil = min(ceil, arr[mid])
      end = mid-1
    elif target > arr[mid]:
      start = mid+1
  return ceil
   
print(ceilOfElement([1,2,3,4,7,12,15,19,21,22,23,25],24))



def nextAlphabeticalElement(arr, target):
  start = 0
  end = len(arr)-1
  res = arr[end]
  while start<=end:
    mid = int((start+end)/2)
    if target == arr[mid]:
      start = mid+1      
    if target < arr[mid]:
      res = arr[mid]
      end = mid-1
    elif target > arr[mid]:
      start = mid+1
  return res
   
print(nextAlphabeticalElement(['a','c','e','f','g','h'],'a'))



def bsInfinite(arr, target):
  start = 0
  end = 1
  while target>arr[end]:
     start = end
     end *= 2
  idx = binarySearch(arr[start:end], target)
  if idx>-1:
     return start+idx
  return -1
   
print(bsInfinite([1,2,3,4,5,6,7,8,9,10,11,12,13],8))


def indexOfOneInfiniteSorted(arr, target):
  start = 0
  end = 1
  while target>arr[end]:
     start = end
     end *= 2
  idx = firstOccurance(arr[start:end], 1)
  if idx>-1:
     return start+idx
  return -1
   
print(indexOfOneInfiniteSorted([0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1],1))


def minDiff(arr, target):
  start = 0
  end = len(arr)-1

  while start<=end:
    mid = int((start+end)/2)
    if arr[mid] == target:
       return arr[mid]
    elif target<arr[mid]:
      end = mid-1
    else:
      start = mid+1

  if abs(target-arr[start])>abs(target-arr[end]):
     return arr[end]
  else:
     return arr[start]
   
print(minDiff([1,2,3,4,8,9,10,11,12],6))




def searchMatrix(matrix, target):
    start = 0
    end = len(matrix)-1
    res = []
    while start<=end:
        mid = int((start+end)/2)
        #mid = int(start + (end-start)/2)
        if target >= matrix[mid][0] and target <= matrix[mid][-1]:
            res = matrix[mid]
            break
        if target<matrix[mid][0]:
            end = mid-1
        elif target>matrix[mid][-1]:
            start = mid+1
    first = 0
    last = len(res)-1
    while first<=last:
        mid = int((first+last)/2)
        if target == res[mid]:
            return True
        elif target<res[mid]:
            last = mid-1
        else:
            first = mid+1
            
    return False

print(searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13))


# koko eating bananas
def minEatingSpeed(piles, h):
    left = 1
    right = max(piles)

    while left<right:
        m = (left+right)//2
        total_hours = sum(math.ceil(pile/m) for pile in piles)

        if total_hours>h:
            left = m+1
        else:
            right = m
    return left

print(minEatingSpeed([3,6,7,11],8))
#output = 4



def findMedianSortedArrays(nums1, nums2):
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1
    
    m, n = len(nums1), len(nums2)
    low, high = 0, m
    
    while low <= high:
        partitionX = (low + high) // 2
        partitionY = (m + n + 1) // 2 - partitionX
        
        maxX = float('-inf') if partitionX == 0 else nums1[partitionX - 1]
        maxY = float('-inf') if partitionY == 0 else nums2[partitionY - 1]
        minX = float('inf') if partitionX == m else nums1[partitionX]
        minY = float('inf') if partitionY == n else nums2[partitionY]
        print(partitionX, partitionY, maxX, minX, maxY, minY)
        
        if maxX <= minY and maxY <= minX:
            if (m + n) % 2 == 0:
                return (max(maxX, maxY) + min(minX, minY)) / 2
            else:
                return max(maxX, maxY)
        elif maxX > minY:
            high = partitionX - 1
        else:
            low = partitionX + 1

# print(findMedianSortedArrays([1,2,3,4,5],[6,7,8,9,10]))


def findMedianSortedArrays (nums1, nums2):
    A, B = nums1, nums2
    total = len(nums1) + len (nums2)
    half = total // 2
    if len(B) < len(A):
        A, B = B, A
    l, r = 0, len(A) - 1
    while True:
        i = (l + r) // 2 # A
        j= half - i - 2 # B
        Aleft = A[i] if i >= 0 else float("-infinity")
        Aright = A[i + 1] if (i + 1) < len(A) else float ("infinity")
        Bleft = B[j] if j >= 0 else float("-infinity")
        Bright = B[j + 1] if (j + 1) < len(B) else float("infinity")
        # partition is correct
        if Aleft <= Bright and Bleft <= Aright:
            # odd
            if total % 2:
                return min(Aright, Bright)
            # even
            return (max(Aleft, Bleft) + min(Aright, Bright)) / 2 
        elif Aleft > Bright: 
            r = i - 1
        else:
            l = i + 1
print(findMedianSortedArrays([1,2,3,4,5],[6,7,8,9,10]))


def maxElemBitonicArray(nums):
  res = nums[0]
  start = 0
  end = len(nums)-1
  while start<=end:
    mid = int((start+end)/2)
    if mid>0 and mid<len(nums)-1:
      if nums[mid]> nums[mid-1] and nums[mid] > nums[mid+1]:
        return nums[mid]
      elif nums[mid-1] > nums[mid]:
        end = mid-1
      else:
         start = mid+1
    elif mid==0:
      if nums[0]>nums[1]:
         return nums[0]
      else:
         return nums[1]
    elif mid == len(nums)-1:
       if nums[-1] > nums[-2]:
          return nums[-1]
       else:
          return nums[-2]
  return -1


print(maxElemBitonicArray([1,2,3,4,5,4,3,2,1]))
