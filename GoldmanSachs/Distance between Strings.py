import math
import re
'''
== Instructions ==
Debug why the included test cases aren't succeeding and account for them in the code

A description of the expected behaviour is given below

Missing enhancements:
1) Support case insensitivity (comparing word to word1 or word2)
2) Account for punctuation (allow multiple separators in the split)
3) Account for the split char in the total length between words (i.e. index += word.length() + 1)
4) Allow for words in either order (math.fabs(wordiloc - word2Loc))
5) Handle case where either word is not present
'''

def shortestDistance(document, word1, word2):
    '''
    Given two words returns the shortest distance between their two midpoints in number of characters
    Words can appear multiple times in any order and should be case insensitive.
    
    E.g. for the document "This is a sample document we just made up"
    shortestDistance(document, "we", "just) == 4
    shortestDistance(document, "is", "a") == 2.5
    shortestDistance(document, "is", "not) == -1
    '''
    
    # todo: determine why tests are failing
    # words = re.split("[,. ]", document) # fix 2
    words = document.split()
    print(words)
    index = 0
    shortest = len(document)
    word1Loc = 0
    word2Loc = 0
    
    for word in words:
        if word.lower() == word1.lower(): # fix 1
            word1Loc = index + (len(word) / 2.0)
        elif word.lower() == word2.lower(): # fix 1
            word2Loc = index + (len(word) / 2.0)
        # print(word1Loc,word2Loc)
        
        if word1Loc > 0 and word2Loc > 0:
            current = math.fabs(word1Loc - word2Loc) # fix 4
            if current < shortest:
                shortest = current
        
        index += len(word) + 1 # fix 3
    
    # fix 5
    if word1Loc == 0 or word2Loc == 0:
        return -1

    return shortest

document  = "This is a sample document we just made up"
print(shortestDistance(document, "we", "just"))
print(shortestDistance(document, "is", "a"))
print(shortestDistance(document, "is", "not"))