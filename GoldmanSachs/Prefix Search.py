'''
Question:
1) Provide the implementation of find_all method in MyPrefixSearch
2) Describe any trade-offs arising from your implementation? (how to store the index efficiently while maintaining fast look up)
3) Try to improve the implementation
'''

'''
CLARIFYING QUESTIONS TO ASK
- What if document is empty?
- Will document contain only alphabets? Do we consider numbers or special characters?
'''

class MyTrie:
    def __init__(self, char):
      self.data = [] # indexes
      self.char = char
      self.nodes = {} # children
    
    def add(self, word, idx):
      if self.char is not None:
        self.data.append(idx)
      if len(word) > 0:
        c = word[0]
          
        if c not in self.nodes:
          self.nodes[c] = MyTrie(c)
        node = self.nodes[c]
        node.add(word[1:], idx)
    
    def get(self, prefix):
        if len(prefix) == 0:
            res = self.data
        else:
            c = prefix[0]
            if c in self.nodes:
                res = self.nodes[c].get(prefix[1:])
            else:
                res = []
        return res
    
    def pprint(self, level = 0):
        print('-' * level + str(self.char), self.data)
        for c, node in self.nodes.items():
            node.pprint(level + 1)

class MyPrefixSearch:
    document = ""
    
    def __init__(self, document):
      self.document = document
      self.root = MyTrie(None)
      self.store_document(document)
    
    def store_document(self, document):
      words = document.lower().split()
      index = 0
      for word in words:
        # CLEAN if told to take only alpha numeric
        new_word = ""
        for char in word:
          if char.isalnum():
            new_word += char
        
        self.root.add(new_word, index)
        # print('root: ', self.root.char)
        index += len(word) + 1
      # self.root.pprint()
    
    '''
    find_all: return a list of all locations in a document where the (case insensitive) word begins with the given prefix
    Example: given the document - "a aa Aaa abca bca"
    find_all("a") -> [0, 2, 5, 9]
    find_all("bc") -> [14]
    find_all("aA") -> [2, 5]
    find_all("abc") -> [9]
    '''
    def find_all(self, prefix):
      # implement here
        
      return self.root.get(prefix.lower())


search = MyPrefixSearch("a aa Aaa abca bca")
print(search.root.pprint())
# print(search.find_all("a"))
# print(search.find_all("bc"))
# print(search.find_all("aA"))
# print(search.find_all("abc"))

doc = "In publishing and graphic design, loren ipsum is a filler text commonly used to demonstrate the graphic elements of a document or visual presentation. Replacing meaningful content that could be distracting with placeholder text may allow viewers to focus on graphic aspects such as font, typography, and page layout. It also reduces the need for the designer to come up with meaningful text, as they con insteed use hastily generated lorem ipsum text. The lorem Ipsum text is typically a scrambled section of De finibus bonorum et malorum, a 1st-century BC Latin text by Cicero, with words altered, added, and renoved to make it nonsensical, improper Latin. A variation of the ordinary lorem ipsum text has been used in typesetting since the 1960s or earlier, when it was popularized by advertisements for Letraset transfer Sheets. It was introduced to the Information Age in the mid-1980s by Aldus Corporation, which employed it in graphics and word processing templates for its desktop publishing program, PegeMaker, for the Apple Macintosh. A common form of lorem ipsum reads: Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do clusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ed minim venian, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute frure doloc in reprehenderit in voluptate velit esse cillun dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatet non proident, sunt in  culpa qui officia deserunt mollit anim id est laborum."
# doc = "In publishing and graphic design, loren ipsum is a filler text commonly used to demonstrate the graphic elements of a document or visual presentation. Replacing meaningful content that could be distracting with placeholder text may allow viewers to focus on graphic aspects such as font, typography, and page layout. It also reduces the need for the designer to come up with meaningful text, as they con insteed use hastily generated lorem ipsum text. The lorem Ipsum text is typically a scrambled section of De finibus bonorum et malorum, a century BC Latin text by Cicero, with words altered, added, and renoved to make it nonsensical, improper Latin. A variation of the ordinary lorem ipsum text has been used in typesetting since the or earlier, when it was popularized by advertisements for Letraset transfer Sheets. It was introduced to the Information Age in the by Aldus Corporation, which employed it in graphics and word processing templates for its desktop publishing program, PegeMaker, for the Apple Macintosh. A common form of lorem ipsum reads: Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do clusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ed minim venian, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute frure doloc in reprehenderit in voluptate velit esse cillun dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatet non proident, sunt in  culpa qui officia deserunt mollit anim id est laborum."

search = MyPrefixSearch(doc)
print(search.find_all("demonstrate")) # [80]
print(search.find_all("pub")) # [3, 988]
print(search.find_all("publishing")) # [3, 988]
print(search.find_all("lab")) # [1173, 1263, 1517]
print(search.find_all("laborum")) # [1517]
print(search.find_all("in")) # [0, 404, 717, 839, 857, 873, 930, 1159, 1334, 1351, 1468]
print(search.find_all("lor")) # [34, 434, 456, 686, 1061, 1080]
print(search.find_all("l")) # [34, 309, 434, 456, 557, 651, 686, 806, 1061, 1080, 1173, 1263, 1517]
print(search.find_all("hamburger")) # []
print(search.find_all("")) # []








class TrieNode:
  def __init__(self,char):
    # Array to store links to child nodes
    self.children = {}
    self.char = char
    self.indexes = []

class Trie:
  def __init__(self, doc):
    self.root= TrieNode("")
    self.store_document(doc)

  def insert(self, word, index):
    curr = self.root
    # print(word,index)
    for c in word:
      i = ord(c) - ord('a')
      curr.char = c
      if i not in curr.children or not curr.children[i]:
        curr.children[i] = TrieNode('')
      curr.indexes.append(index)
      curr = curr.children[i]
    curr.indexes.append(index)
  
  def store_document(self, document):
    words = document.lower().split()
    index = 0
    for word in words:
      # CLEAN if told to take only alpha numeric
      new_word = ""
      for char in word:
        if char.isalnum():
          new_word += char
      
      self.insert(new_word, index)
      index += len(word) + 1

      
  def startsWith(self, prefix: str) -> bool:
    curr = self.root
    for c in prefix:
      i = ord(c) - ord('a')
      if i not in curr.children or not curr.children[i]:
        return []
      curr = curr.children[i]
    return curr.indexes
  


# Your Trie object will be instantiated and called as such:
doc = "In publishing and graphic design, loren ipsum is a filler text commonly used to demonstrate the graphic elements of a document or visual presentation. Replacing meaningful content that could be distracting with placeholder text may allow viewers to focus on graphic aspects such as font, typography, and page layout. It also reduces the need for the designer to come up with meaningful text, as they con insteed use hastily generated lorem ipsum text. The lorem Ipsum text is typically a scrambled section of De finibus bonorum et malorum, a 1st-century BC Latin text by Cicero, with words altered, added, and renoved to make it nonsensical, improper Latin. A variation of the ordinary lorem ipsum text has been used in typesetting since the 1960s or earlier, when it was popularized by advertisements for Letraset transfer Sheets. It was introduced to the Information Age in the mid-1980s by Aldus Corporation, which employed it in graphics and word processing templates for its desktop publishing program, PegeMaker, for the Apple Macintosh. A common form of lorem ipsum reads: Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do clusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ed minim venian, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute frure doloc in reprehenderit in voluptate velit esse cillun dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatet non proident, sunt in  culpa qui officia deserunt mollit anim id est laborum."
obj = Trie(doc)
print('----------------------------------------')
print(obj.startsWith("demonstrate")) # [80]
print(obj.startsWith("pub")) # [3, 988]
print(obj.startsWith("publishing")) # [3, 988]
print(obj.startsWith("lab")) # [1173, 1263, 1517]
print(obj.startsWith("laborum")) # [1517]
print(obj.startsWith("in")) # [0, 404, 717, 839, 857, 873, 930, 1159, 1334, 1351, 1468]
print(obj.startsWith("lor")) # [34, 434, 456, 686, 1061, 1080]
print(obj.startsWith("l")) # [34, 309, 434, 456, 557, 651, 686, 806, 1061, 1080, 1173, 1263, 1517]
print(obj.startsWith("hamburger")) # []







# class TrieNode:
#   def __init__(self,char):
#     # Array to store links to child nodes
#     self.nodes = {}
#     self.char = char
#     self.indexes = []

# class Trie:

#   def __init__(self, doc):
#     self.root= TrieNode("")
#     self.store_document(doc)

#   def insert(self, word, index) -> None:
#     curr = self.root
#     # print(word,index)
#     for c in word:
#       if c not in curr.nodes:
#          curr.nodes[c] = TrieNode(c)
#       curr.indexes.append(index)
#       curr = curr.nodes[c]
#     curr.indexes.append(index)