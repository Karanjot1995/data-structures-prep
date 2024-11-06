
####################  Rain water Trapping  ######################

#most optimal SC- O(1)
def RWH(arr):
  left_max = right_max = 0
  left,right = 0, len(arr)-1
  ans = 0

  while left<=right:
    if arr[left]<=arr[right]:
      if arr[left]>=left_max: left_max = arr[left]
      else: ans+= left_max - arr[left]
      left+=1
    else:
      if arr[right]>=right_max: right_max = arr[right]
      else: ans+= right_max - arr[right]
      right-=1

  return ans

arr = [3,0,0,2,0,4,1,2]
print('rwh1: ',RWH(arr))



def RWH2(arr):
  # height = 0
  # for i in range(0,len(arr)):
  #   left = max(arr[0:i+1])
  #   right = max(arr[i:len(arr)])
  #   h = min(left,right)-arr[i]
  #   height += min(left,right)-arr[i]
  #   print(h)
  # return height
  max_l = []
  max_r = []
  mxl = arr[0]
  mxr = arr[-1]
  heights = []

  for i in range(0,len(arr)):
    mxl = max(mxl, arr[i])
    max_l.append(mxl)

  for i in range(len(arr)-1,-1,-1):
    mxr = max(mxr, arr[i])
    max_r.append(mxr)
  max_r.reverse()

  print(max_l, max_r)
  print('rwh: ', mxl,mxr)
  max_h = 0
  for i in range(0,len(arr)):
    heights.append(min(max_l[i],max_r[i])-arr[i])
    max_h += min(max_l[i],max_r[i])-arr[i]
  # print(heights)
  return max_h

print('rwh2: ',RWH2([3,0,0,2,0,4,1,2]))


def RWH3(arr):
  mxl = arr[0]
  mxr = arr[-1]
  max_l = []
  max_r = []

  ht = 0
  for i in range(0,len(arr)):
    mxl = max(mxl, arr[i])
    max_l.append(mxl)
    mxr= max(mxr, arr[len(arr)-1-i])
    max_r.append(mxr)
  max_r.reverse()
  ht = 0
  for i in range(0,len(arr)):
    ht += min(max_l[i],max_r[i])-arr[i]  
  return ht

print('rwh3: ',RWH3([3,0,0,2,0,4,1,2]))

def RWH4(arr):
  max_l = [arr[0]]
  max_r = [arr[-1]]

  ht = 0
  for i in range(1,len(arr)):
    max_l.append(max(max_l[i-1],arr[i]))

  for i in range(len(arr)-2,-1,-1):
    max_r.append(max(max_r[len(max_r)-1], arr[i]))
  max_r.reverse()
  
  ht = 0
  for i in range(0,len(arr)):
    ht += min(max_l[i],max_r[i])-arr[i]  
  return ht


print('rwh4: ',RWH4([3,0,0,2,0,4,1,2]))


# n2

class Solution:
    def trap(self, height):
        ans = 0
        size = len(height)
        for i in range(1, size - 1):
            left_max = 0
            right_max = 0
            # Search the left part for max bar size
            for j in range(i, -1, -1):
                left_max = max(left_max, height[j])
            # Search the right part for max bar size
            for j in range(i, size):
                right_max = max(right_max, height[j])
            ans += min(left_max, right_max) - height[i]
        return ans
