
def findBuildings(self, heights):
  n = len(heights)
  maxi = -1
  views = []
  for i in range(n-1,-1,-1):
    if heights[i]>maxi: 
      views.append(i)
      maxi = heights[i]
  return views[::-1]

def findBuildings2(self, heights):
  stack = []
  for i in range(len(heights)):
      #if next value is bigger then empty stack till you find a bigger value  [4,2], 3 => [4,3]
      while stack and heights[stack[-1]] <= heights[i]: stack.pop()
      stack.append(i)
  return stack


heights = [4,2,3,1] #op [0,2,3]
print(findBuildings(heights))