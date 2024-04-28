# class Node:
#   def __init__(self):
#     self.node = [0]*26
#     self.flag = False
class TrieNode:
  def __init__(self):
    # Array to store links to child nodes
    self.children = [None] * 26
    # Flag to indicate if the node represents the end of a word
    self.flag = False

class Trie:

  def __init__(self):
    self.root= TrieNode()

  def insert(self, word: str) -> None:
    curr = self.root
    for c in word:
      i = ord(c) - ord('a')

      if curr.children[i]==None:
        curr.children[i] = TrieNode()
      # print(c,curr.flag)
      curr = curr.children[i]
    curr.flag = True
      

  def search(self, word: str) -> bool:
    curr = self.root

    for c in word:
      i = ord(c) - ord('a')
      if curr.children[i] == None:
        return False
      curr = curr.children[i]
    # Return True if the last node represents the end of a word
    return curr.flag

      
  def startsWith(self, prefix: str) -> bool:
    curr = self.root
    for c in prefix:
      i = ord(c) - ord('a')
      if curr.children[i] == None:
        return False
      curr = curr.children[i]
    return True
        


# Your Trie object will be instantiated and called as such:
obj = Trie()
obj.insert('apple')
obj.insert('app')
obj.insert('bat')
obj.insert('bar')
print(obj.search('app'))
print(obj.search('apx'))
print(obj.startsWith('appl'))
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)







class Trie:

    def __init__(self):
        self.root = {}

    def insert(self, word: str) -> None:
        node = self.root
        for w in word:
            if w not in node:
                node[w] = {}
            node = node[w]
        node["."] = {}

    def search(self, word: str) -> bool:
        traversed = Trie.traverse(word, self.root)
        return traversed and "." in traversed

    def startsWith(self, prefix: str) -> bool:
        traversed = Trie.traverse(prefix, self.root)
        return traversed
    
    def traverse(word: str, node):
        for w in word:
            if w in node:
                node = node[w]
            else:
                return None
        return node
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)