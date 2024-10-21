# https://leetcode.com/problems/valid-word-abbreviation/

class Solution:
    # TC - O(min(N, M)) | SC - O(1)
    # Clarifying questions
    # 1) does the string have only lowercase chars? will "A" == "a"?
    # 2) can word also contain digits?
    # 3) can abbr contain "0" do we have to account for that?
    def validWordAbbreviation(self, word, abbr):
        if not word or not abbr: return False

        i = j = 0
        while i < len(word) and j < len(abbr):
          if abbr[j].isdigit():
            if abbr[j] == "0": return False
            total = 0
            while j < len(abbr) and abbr[j].isdigit():
              total = total * 10 + int(abbr[j])
              j += 1
            i += total
          else:
            if word[i] != abbr[j]: return False
            i += 1
            j += 1
        
        return i == len(word) and j == len(abbr)

s = Solution()
print(s.validWordAbbreviation("internationalization", "i18n")) # true
print(s.validWordAbbreviation("interpolation", "i18n")) # false
print(s.validWordAbbreviation("facebook", "f6k")) # true
print(s.validWordAbbreviation("focus", "f6k")) # false

print(s.validWordAbbreviation("Facebook", "F2eb2k")) # true
print(s.validWordAbbreviation("Facebook", "8")) # true
print(s.validWordAbbreviation("Faceboook", "8")) # false
print(s.validWordAbbreviation("Faceboook", "8k")) # true
print(s.validWordAbbreviation("Facebook", "8k")) # false
print(s.validWordAbbreviation("Facebok", "8k")) # false





def validWordAbbreviation(word: str, abbr: str) -> bool:
    i,j=0,0
    n,m = len(word), len(abbr)

    while i<n and j<m:
      #if digit is found j pointer will increase till 
      #there are consecutive digits
      if abbr[j].isdigit():
        if abbr[j]=='0': return False
        increment_by = ''
        while j<m and abbr[j].isdigit():
          increment_by+=abbr[j]
          j+=1
        #increment i to the number that is found in abbr
        i+=int(increment_by)
      else:
        if word[i]!=abbr[j]: return False
        i+=1
        j+=1
    return i==n and j==m

word = "internationalization"
abbr = "i12iz4n"
print(validWordAbbreviation(word, abbr))