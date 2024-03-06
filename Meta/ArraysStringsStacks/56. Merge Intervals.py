
# O(NlogN)
class Solution:
  def merge(self, intervals):
    intervals.sort()
    arr = [intervals[0]]

    for interval in intervals[1:]:
      end = arr[-1][1]
      if interval[0]<=end:
        arr[-1][1]= max(end,interval[1])
      else: arr.append(interval)
      
    return arr

    # for interval in intervals[1:]:
    #   start,end = arr[-1][0], arr[-1][1]
    #   start2,end2 = interval[0], interval[1]
    #   if start<=end2 and start2<=end:
    #     lo = min(start,start2)
    #     hi = max(end,end2)
    #     arr[-1] = [lo,hi]
    #   else: arr.append(interval)

    # return arr
        

      
      
