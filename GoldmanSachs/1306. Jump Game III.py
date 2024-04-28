class Solution:
  '''
    TC - O(N)
    SC - O(N)
  '''
  def canReach(self, arr, start: int) -> bool:
    q = [start]
    while q:
      idx = q.pop(0)
      if arr[idx] == 0: return True
      if arr[idx]<0: continue

      if idx+arr[idx]<len(arr): q.append(idx+arr[idx])
      if idx-arr[idx]>0: q.append(idx-arr[idx])

      # mark it as visited
      arr[idx] = -arr[idx]

    return False


  def canReach(self, arr, start: int) -> bool:
    def jump(i):
      if i>=0 and i<len(arr) and arr[i]>=0:
        if arr[i] == 0: return True
        arr[i] = -arr[i]
        return jump(i-arr[i]) or jump(i+arr[i])
      return False
    return jump(start)


  def canReach(self, arr, start: int) -> bool:
    vis = set()
    def jump(i):
      if i<0 or i>=len(arr): return False
      if i in vis: return False

      if arr[i] == 0: return True
      vis.add(i)
      return jump(i-arr[i]) or jump(i+arr[i])

    return jump(start)
        