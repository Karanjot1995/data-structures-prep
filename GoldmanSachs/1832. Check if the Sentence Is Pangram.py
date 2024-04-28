import collections

class Solution:
  def checkIfPangram(self, sentence: str) -> bool:
    seen = set(sentence)
    # seen = collections.Counter(sentence)
    return len(seen)==26