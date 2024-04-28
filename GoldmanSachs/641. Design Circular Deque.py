class MyCircularDeque:

  def __init__(self, k: int):
    self.dq = [0]*k 
    self.front = -1
    self.rear = -1
    self.capacity = k

  def insertFront(self, value: int) -> bool:
    if self.isFull(): return False
    if self.front == self.rear == -1:
      self.front = self.rear = 0
    else:
      self.front = (self.front-1)%self.capacity
    self.dq[self.front] = value
    return True

  def insertLast(self, value: int) -> bool:
    if self.isFull(): return False
    if self.front == self.rear == -1:
      self.front = self.rear = 0
    else:
      self.rear = (self.rear+1)%self.capacity
    self.dq[self.rear] = value
    return True

  def deleteFront(self) -> bool:
    if self.isEmpty(): return False
    value = self.dq[self.front]
    if self.front == self.rear:
      self.front = self.rear = -1
    else:
      self.front = (self.front+1)%self.capacity
    return True
        
  def deleteLast(self) -> bool:
    if self.isEmpty(): return False
    value = self.dq[self.rear]
    if self.front == self.rear:
      self.front = self.rear = -1
    else:
      self.rear = (self.rear-1)%self.capacity
    return True

  def getFront(self) -> int:
    if self.isEmpty(): return -1
    return self.dq[self.front]

  def getRear(self) -> int:
    if self.isEmpty(): return -1
    return self.dq[self.rear]

  def isEmpty(self) -> bool:
    return self.front == self.rear == -1

  def isFull(self) -> bool:
    return (self.front == 0 and self.rear == self.capacity - 1) or (self.front == self.rear + 1)
      

d = MyCircularDeque(5)
print(d.insertLast(1))
print(d.insertLast(2))
print(d.insertLast(3))
print(d.insertLast(4))
print(d.deleteFront())
print(d.deleteFront())
print(d.insertFront(433))
print(d.insertFront(53))
print(d.insertFront(7))
print(d.getFront())
print(d.insertLast(13))
print(d.insertLast(14))
print(d.insertLast(15))
print(d.getRear())

# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
