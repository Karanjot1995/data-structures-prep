#https://leetcode.com/problems/design-in-memory-file-system/description/

from collections import defaultdict

class FsNode:
  def __init__(self):
    self.children = defaultdict(FsNode)
    # Flag to indicate if the node represents a file
    self.isFile = False
    self.content = ""

class FileSystem:

  def __init__(self):
    self.root = FsNode()
      
  def ls(self, path: str):
    curr = self.root
    arr = path.split('/')

    for ch in arr:
      if not ch: continue
      curr = curr.children[ch]
    
    if curr.isFile:
      return [ch]

    return sorted(curr.children.keys())


  def mkdir(self, path: str) -> None:
    curr = self.root
    if path == "/": return []
    arr = path.split('/')
    for ch in arr:
      if ch:
        if curr.children[ch]==None:
          curr.children[ch] = FsNode()
        curr = curr.children[ch]
      

  def addContentToFile(self, filePath: str, content: str) -> None:
    curr = self.root
    arr = filePath.split('/')
    for ch in arr:
      if ch:
        if curr.children[ch]==None:
          curr.children[ch] = FsNode()
        curr = curr.children[ch]

    curr.content += content
    curr.isFile = True
      

  def readContentFromFile(self, filePath: str) -> str:
    curr = self.root
    arr = filePath.split('/')
    for ch in arr:
      if ch:
        if curr.children[ch]==None:
          return False
        curr = curr.children[ch]
    return curr.content
      


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)