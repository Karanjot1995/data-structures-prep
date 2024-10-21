from queue import deque

class MovingAverage:

  def __init__(self, size: int):
    self.size = size
    self.q = deque([])
    self.total = 0
      

  def next(self, val: int) -> float:
    popped = 0
    if len(self.q)==self.size: popped = self.q.popleft()
    self.total += (val - popped)
    self.q.append(val)

    return self.total/len(self.q)




# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)