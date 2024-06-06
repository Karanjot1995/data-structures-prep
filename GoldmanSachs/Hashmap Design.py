class MyHashMap:

  def __init__(self):
    self.buckets = [[] for _ in range(100)]
  
  # def getHashedIndex(self, key):
  #   return hash(key) % len(self.buckets)
        
  def put(self, key: int, value: int) -> None:
    # modulo
    index = key % len(self.buckets)
    curr_bucket = self.buckets[index]

    for pair in curr_bucket:
      if pair[0] == key:
        pair[1] = value
        return
    curr_bucket.append([key,value])


  def get(self, key: int) -> int:
    index = key % len(self.buckets)
    curr_bucket = self.buckets[index]
    
    for pair in curr_bucket:
      if pair[0]==key: return pair[1]
    return -1

  def remove(self, key: int) -> None:
    index = key % len(self.buckets)
    curr_bucket = self.buckets[index]
    
    for i,pair in enumerate(curr_bucket):
      if pair[0] == key:
        curr_bucket.pop(i)
        return 
    return -1
