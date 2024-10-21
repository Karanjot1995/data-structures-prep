from collections import defaultdict
from queue import deque
from Templates.directedGraph import Graph

class Graph(Graph):
  def ladderLength(self, beginWord: str, endWord: str, wordList):
    words=set(wordList)
    if endWord not in wordList:
      return 0
    q = deque()
    q.append((beginWord,1))
    while q:
      word,level=q.popleft()
      if word == endWord:
        return level
      
      for i in range(len(word)):
        for j in range(26):
          new_word=word[:i]+chr(97+j)+word[i+1:]
          # char = chr(97+j)
          # string_list = list(word)
          # string_list[i] = char
          # new_word = "".join(string_list)
          if new_word == endWord:
            return level+1
          if new_word in words:
            words.remove(new_word)
            q.append((new_word,level+1))
    return 0
  
  def findLadders(self, beginWord: str, endWord: str, wordList):
    if endWord not in wordList:
      return 0
    
    st=[beginWord]
    for word in wordList:
      st.append(word)

    q = [[beginWord]]
    used = [beginWord]

    level = 0
    ans = []

    while q:
      words = q.pop(0)
      print(words)
      if len(words)>level:
        level+=1
        for w in used:
          if w in st:
            st.remove(w)

      word = words[-1]
      if word == endWord:
        if len(ans)==0:
          ans.append(words)
        elif len(ans[0])==len(words):
          ans.append(words)

      for i in range(len(word)):
        for j in range(26):
          new_word=word[:i]+chr(97+j)+word[i+1:]
          if new_word in st:
            words.append(new_word)
            q.append(list(words))
            used.append(new_word)
            words.pop()
    return ans
  

graph = Graph(6)

beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
print(graph.ladderLength(beginWord, endWord, wordList))
print(graph.findLadders(beginWord, endWord, wordList))

  # def ladderLength(beginWord, endWord, wordList):
  #   q = []
  #   wordList=set(wordList)
  #   if endWord not in wordList:
  #     return 0
  #   q = []
  #   q.append([beginWord,1])

  #   while q:
  #     curr = q.pop(0)
  #     currWord = curr[0]
  #     level = curr[1]
  #     if currWord == endWord:
  #       return level
      
  #     for i in range(len(currWord)):
  #       for j in range(26):
  #         char = chr(97+j)
  #         string_list = list(currWord)
  #         string_list[i] = char
  #         new_string = "".join(string_list)
  #         if new_string in wordList:
  #           wordList.remove(new_string)
  #           q.append([new_string,level+1])
  #   return 0
  
  
  # def ladderLength(beginWord, endWord, wordList):
  #   vis = []
  #   q = []
  #   words = wordList
  #   q.append([beginWord,1])
  #   vis.append(beginWord)
  #   res = []
  #   ans= 0
  #   while q:
  #     curr = q.pop(0)
  #     currWord = curr[0]
  #     level = curr[1]
  #     res.append(curr)
  #     if currWord == endWord:
  #       return level
  #     for word in words:
  #       cnt = 0
  #       if word not in vis:
  #         for i in range(len(currWord)):
  #           if word[i]!=currWord[i]:
  #             cnt+=1
  #         if cnt==1:
  #           q.append([word,level+1])
  #           vis.append(word)

  #   return 0


  # curr = res[-1]
  # currWord = 
  # def dfs(word, words):


def findLadders(beginWord: str, endWord: str, wordList):    
  if endWord not in wordList:
    return []
  
  st=set(wordList)
  st.discard(beginWord)
  dict = {}
  dict[beginWord] = 1
  q = [beginWord]
  while q:
    word=q.pop(0)
    level = dict[word]
    if word==endWord:
      break
    for i in range(len(word)):
      for j in range(26):
        new_word=word[:i]+chr(97+j)+word[i+1:]
        if new_word in st:
          st.remove(new_word)
          q.append(new_word)
          dict[new_word] = level+1

  def dfs(word, words):
    if word == beginWord:
      # print(words)
      ans.append(words[::-1])
      return
    steps = dict[word]
    for i in range(len(word)):
      for j in range(26):
        new_word=word[:i]+chr(97+j)+word[i+1:]
        if new_word in dict and dict[new_word]+1==steps:
          words.append(new_word)
          dfs(new_word, words)
          words.pop()
    return ans
    

  ans = []
  words = [endWord]
  if endWord in dict:
    dfs(endWord, words)

  return ans



# return res
#     # edge case
#     if endWord not in wordList:
#         return []
    
#     # 1) build neighbor list for first bfs
#     if beginWord not in wordList:
#         wordList.append(beginWord)
#     unseen = set(wordList)
#     word_size = len(beginWord)
#     neighbors = defaultdict(list)
#     for word in wordList:
#         for i in range(word_size):
#             neighbors[f'{word[:i]}*{word[i+1:]}'].append(word)
#     print(neighbors)
#     # 2) do first bfs and build neighbors list for second bfs
#     reverse_neighbors = defaultdict(list)
#     n_t_h = [endWord]
#     unseen.remove(endWord)
#     while n_t_h:
#         new_seen = set()
#         for word in n_t_h:
#             for i in range(word_size):
#                 for neighbor in neighbors[f'{word[:i]}*{word[i+1:]}']:
#                     if neighbor in unseen:
#                         reverse_neighbors[neighbor].append(word)
#                         new_seen.add(neighbor)
#         n_t_h = list(new_seen)
#         unseen -= new_seen
#         if reverse_neighbors[beginWord]:
#             break
    
#     # if beginWord does not have reversed neigbors it is not reachable so return empty list
#     if not reverse_neighbors[beginWord]:
#         return []
    
#     # 3) do second bfs
#     paths = [[beginWord]]
#     while True:
#         new_paths = []
#         for path in paths:
#             last_node = path[-1]
#             for reverse_neighbor in reverse_neighbors[last_node]:
#                 new_paths.append(path + [reverse_neighbor])
#         paths = new_paths
#         if paths[0][-1] == endWord:
#             break
    
#     return paths

beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
print(findLadders(beginWord, endWord, wordList))


