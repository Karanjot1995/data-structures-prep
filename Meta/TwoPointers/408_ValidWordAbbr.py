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