class TrieNode:
  def __init__(self):
    self.children = [None] * 26
    self.words_ending_here = 0
    self.words_starting_here = 0

class Trie:

  def __init__(self):
    self.root= TrieNode()
    
  def insert(self, word: str) -> None:
    curr = self.root
    for c in word:
      i = ord(c)-ord('a')
      if not curr.children[i]:
        curr.children[i] = TrieNode()
      curr = curr.children[i]
      curr.words_starting_here += 1

    curr.words_ending_here += 1

  def countWordsEqualTo(self, word: str) -> int:
    curr = self.root
    for c in word:
      i = ord(c) - ord('a')
      if not curr.children[i]: return 0
      curr = curr.children[i]
    return curr.words_ending_here

  def countWordsStartingWith(self, prefix: str) -> int:
    curr = self.root
    for c in prefix:
      i = ord(c) - ord('a')
      if not curr.children[i]: return 0
      curr = curr.children[i]
    return curr.words_starting_here

  def erase(self, word: str) -> None:
    curr = self.root
    for c in word:
      i = ord(c) - ord('a')
      curr = curr.children[i]
      curr.words_starting_here -= 1
    curr.words_ending_here -= 1