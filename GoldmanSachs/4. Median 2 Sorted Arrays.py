def findMedianSortedArrays(nums1, nums2) -> float:
  A, B = nums1, nums2
  if len(A)> len(B):
      A,B = B,A
  n1,n2 = len(A),len(B)

  n = n1 + n2  # total length
  left = (n1 + n2 + 1) // 2  # length of left half
  # apply binary search:
  low, high = 0, n1
  while low <= high:
    mid1 = (low + high) // 2
    mid2 = left - mid1
    # calculate l1, l2, r1, and r2;
    l1, l2, r1, r2 = float('-inf'), float('-inf'), float('inf'), float('inf')
    if mid1 < n1: r1 = A[mid1]
    if mid2 < n2: r2 = B[mid2]
    if mid1 - 1 >= 0: l1 = A[mid1 - 1]
    if mid2 - 1 >= 0: l2 = B[mid2 - 1]

    if l1 <= r2 and l2 <= r1:
      if n % 2 == 1: return max(l1, l2)
      else:
        return (float(max(l1, l2)) + float(min(r1, r2))) / 2.0
    elif l1 > r2:
      high = mid1 - 1
    else:
      low = mid1 + 1
  return 0
    

# def findMedianSortedArrays(nums1, nums2) -> float:
#   merged = []
#   m, n = len(nums1), len(nums2)
#   i, j = 0, 0

#   while i<m and j<n:
#     if nums1[i]<nums2[j]:
#       merged.append(nums1[i])
#       i+=1
#     else:
#       merged.append(nums2[j])
#       j+=1

#   while i<m:
#     merged.append(nums1[i])
#     i+=1
#   while j<n:
#     merged.append(nums2[j])
#     j+=1 
  
#   mid = len(merged)//2
#   if len(merged)%2 == 0: return (merged[mid-1]+merged[mid])/2
#   return merged[mid]


      