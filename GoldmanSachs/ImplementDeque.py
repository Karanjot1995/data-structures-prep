'''
APPROACH: Circular Array

TC - O(1) all operations
SC - O(N) where N is the size of the queue
'''

class MyDeque:
    def __init__(self, k):
        self.dq = [0] * k
        self.front = -1
        self.rear = -1
        self.capacity = k

    def enQueueFront(self, value):
        if self.isFull():
            return False
        
        # dq is empty
        if self.front == -1 and self.rear == -1:
            self.front = 0
            self.rear = 0
        else:
            self.front =  (self.front - 1) % self.capacity # (0 - 1) % 5 == 4; so modulo of -ve is +ve
        
        self.dq[self.front] = value
        return True
    
    def enQueueRear(self, value):
        if self.isFull():
            return False
        
        # dq is empty
        if self.front == -1 and self.rear == -1:
            self.front = 0
            self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.capacity
        
        self.dq[self.rear] = value
        return True
        
    def deQueueFront(self):
        if self.isEmpty():
            return -1
        
        if self.front == self.rear:
            value = self.dq[self.front]
            self.front = -1
            self.rear = -1
        else:
            value = self.dq[self.front]
            self.front = (self.front + 1) % self.capacity

        return value

    def deQueueRear(self):
        if self.isEmpty():
            return -1

        if self.front == self.rear:
            value = self.dq[self.rear]
            self.front = -1
            self.rear = -1
        else:
            value = self.dq[self.rear]
            self.rear = (self.rear - 1) % self.capacity

        return value
        
    def getFront(self):
        if self.isEmpty():
            return -1
        return self.dq[self.front]

    def getRear(self):
        if self.isEmpty():
            return -1
        return self.dq[self.rear]

    def isEmpty(self):
        return self.front == -1 and self.rear == -1

    def isFull(self):
        return (self.front == 0 and self.rear == self.capacity - 1) or \
            (self.front == self.rear + 1)
    
    def printDeque(self):
        i = self.front
        
        while i != self.rear:
            print(self.dq[i])
            i = (i + 1) % self.capacity
        
        print(self.dq[self.rear])


d = MyDeque(5)
print(d.enQueueRear(1))
print(d.enQueueRear(2))
print(d.enQueueRear(3))
print(d.enQueueRear(4))
print(d.deQueueFront())
print(d.deQueueFront())
print(d.enQueueFront(433))
print(d.enQueueFront(53))
print(d.enQueueFront(7))
print(d.getFront())
print(d.enQueueRear(13))
print(d.enQueueRear(14))
print(d.enQueueRear(15))
print(d.getRear())