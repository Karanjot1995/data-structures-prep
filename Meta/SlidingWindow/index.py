# identification terms - substring, sub array, largest max or min, window size

def maxProfit(prices):
  min = prices[0]
  max_profit = 0
  i = 0
  while i < len(prices):
      if prices[i]<min:
          min = prices[i]
      else:
          max_profit = max(max_profit, prices[i]-min)
      i+=1
  return max_profit

print(maxProfit([7,1,5,3,6,4]))
#o/p = 6-1 = 5


def maxSumSubarray(arr, k):
    sum=0
    for i in range(k):
        sum+=arr[i]
    max_sum = sum
    for i in range(k,len(arr)):
        sum+=arr[i]-arr[i-k]
        max_sum = max(max_sum, sum)
    return max_sum
#or
def maxSumSubarray(arr, k):
  i=0
  j=0
  sum=0
  res=float("-infinity")
  for j in range(len(arr)):
    sum=sum+arr[j]
    if j-i+1>=k:
      res=max(res,sum)
      sum=sum-arr[i]
      i+=1
    # j+=1
  return res
    
print(maxSumSubarray([2,5,1,8,2,9,1],3))

def lengthOfLongestSubstring(s):
    seen = {}
    i = 0
    # sub_str = ''
    count = 0
    for j in range(len(s)):
        char = s[j]
        if char in seen and seen[char]>=i:
            i = seen[char]+1
        else:
            count = max(count, j-i+1)
        seen[char] = j
    return count


print(lengthOfLongestSubstring('abcdaecd'))
#5


def firstNegative(arr,k):
  i = 0
  stack = []
  res = []
  for j in range(len(arr)):
    if arr[j]<0:
        stack.append(arr[j])

    if j-i+1==k:
      if len(stack)==0:
          res.append(0)
      else:
          res.append(stack[0])
          if arr[i]==stack[0]:
            stack.pop(0)
      i+=1
    
  return res

print(firstNegative([12,-1,-7,8,-15,30,16,28],3))


def maxSlidingWindow(nums, k):
  stack = []
  res = []
  for i in range(len(nums)):
    if stack and stack[0]==i-k:
      stack.pop(0)
    while stack and nums[stack[-1]]<nums[i]:
      stack.pop()
    stack.append(i)
    if i>=k-1:
      res.append(nums[stack[0]])
  return res


# def maxSlidingWindow(nums, k):
#   stack = []
#   res = []
#   i=0
#   for j in range(len(nums)):
#     if stack and stack[0]==j-k #or i:
#       stack.pop(0)
#     while stack and nums[stack[-1]]<nums[j]:
#       stack.pop()
#     stack.append(j)
#     if j-i+1==k:
#       res.append(nums[stack[0]])
#       i+=1
#   return res
# def maxSlidingWindow(nums, k):
#   stack = []
#   res = []
#   for i in range(len(nums)):
#     if stack and stack[0]==nums[i-k]:
#       stack.pop(0)
#     while stack and stack[-1]<nums[i]:
#       stack.pop()
#     stack.append(nums[i])
#     # print(stack)
#     if i>=k-1:
#       res.append(stack[0])
#   return res


print(maxSlidingWindow([1,3,3,-1,-3,5,3,6,7],3))
#o/p = [3,3,5,5,6,7]


def occurancesOfAnagram(str, substr):
  dict = {}
  k = len(substr)
  for char in substr:
    dict[char] = dict.get(char, 0) + 1
    
  i = 0
  n=0
  count = len(dict)
  idxs = []
  for j in range(len(str)):
    if str[j] in dict:
      dict[str[j]]-=1
      if dict[str[j]] ==0:
        count-=1
    if j-i+1==k:
      if count ==0:
        n+=1
        idxs.append(i)
      if str[i] in dict:
        dict[str[i]]+=1
        if dict[str[i]] == 1:
          count+=1
      i+=1

  return idxs

#or

# def occurancesOfAnagram(str, substr):
#   dict = {}
#   count = 0
#   k = len(substr)
#   for char in substr:
#     if char in dict:
#       dict[char]+=1
#     else:
#       dict[char]=1
#   i = 0
#   for j in range(len(str)):
#     if str[j] in dict:
#       dict[str[j]]-=1
#     print(i,j, dict)
#     anagram = True
#     for char in dict:
#       if dict[char]>0:
#         anagram = False
#     if anagram:
#        count+=1
#     # if j-i+1<k:
#     if j-i+1==k:
#       if str[i] in dict:
#         dict[str[i]]+=1
#       i+=1
#   return count

print(occurancesOfAnagram('aabaabaa', 'aaba'))



def checkInclusion(s1, s2):
    dict = {}
    k = len(s1)
    for char in s1:
        dict[char] = dict.get(char, 0) + 1
    i = 0
    n=0
    count = len(dict)
    for j in range(len(s2)):
        if s2[j] in dict:
            dict[s2[j]]-=1
            if dict[s2[j]] ==0:
                count-=1
        if j-i+1==k:
            if count ==0:
                return True
            if s2[i] in dict:
                dict[s2[i]]+=1
                if dict[s2[i]] == 1:
                    count+=1
            i+=1
    return False

print(checkInclusion('aaba', 'aabaabaa'))
