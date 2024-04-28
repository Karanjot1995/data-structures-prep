class Solution:
  def longestMountain(self, arr) -> int:
    i, ans = 0,0
    n = len(arr)
    while i < len(arr):
      base = i
      while i+1 < n and arr[i] < arr[i+1]:
        i+=1
      if i == base:
        i+=1
        continue
      peak = i

      while i+1<n and arr[i]>arr[i+1]:
        i+=1
      if i == peak:
        i+=1
        continue

      ans = max(ans, i-base+1)

    return ans



    
  # def longestMountain(self, arr: List[int]) -> int:
  #   if len(arr)<3: return 0
  #   i,j=0,1
  #   n = len(arr)
  #   max_cnt = 1
  #   while i<n and j<n:
  #     base = i
  #     if arr[i]>=arr[j]:
  #       i+=1
  #     cnt = 1
  #     while j< n-1 and arr[j+1]>arr[j]:
  #       cnt+=1
  #       j+=1
  #     if cnt>1:
  #       while j<n-1 and arr[j+1]<arr[j]:
  #         cnt+=1
  #         j+=1
  #     max_cnt = max(max_cnt,cnt)
  #     i+=1

  #   return max_cnt if max_cnt>1 else 0


        