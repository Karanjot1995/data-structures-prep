class Solution:
  def isPathCrossing(self, path: str) -> bool:
    coordinates = [0,0]
    seen = [[0,0]]

    for d in path:
      if d == 'N': coordinates[1]+=1
      elif d == 'S': coordinates[1]-=1
      elif d == 'E': coordinates[0]+=1
      elif d == 'W': coordinates[0]-=1
      if coordinates in seen: return True
      seen.append(coordinates.copy())

    return False