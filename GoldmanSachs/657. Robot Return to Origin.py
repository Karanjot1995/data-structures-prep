class Solution:
  def judgeCircle(self, moves: str) -> bool:
    r,c=0,0

    for move in moves:
      if move == 'U': r-=1
      elif move == 'D': r+=1
      elif move == 'L': c-=1
      else: c+=1

    return r==0 and c==0
        