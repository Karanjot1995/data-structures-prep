class Solution:
    # TC - O(N) | SC - O(1)
    # Video - https://www.youtube.com/watch?v=rhotywtQ1KE&ab_channel=codeExplainer
    def countBinarySubstrings(self, s: str) -> int:
        # cur and prev reprents the groups of consecutive 1s and 0s
        # as soon as the 0s and 1s are flipped we make prev = cur and cur = 1
        cur = 1 # 1 as sting will be min len 1
        prev = 0
        ans = 0

        for i in range(1, len(s)):
            if s[i - 1] == s[i]:
                cur += 1
            else:
                # numbers are flipped here
                
                # 00111 for this we have 2 0s and 3 1s so how many substr we can make? -> min(prev, cur) where prev = 2 and cur = 3
                # so the substr are 0[01]11 and [0011]1
                ans += min(cur, prev)
                prev = cur
                cur = 1
        
        # take care of the case 0011[000111] the last flip for last group
        return ans + min(cur, prev)
    
    # groups = [1]
    # for i in range(1, len(s)):
    #   if s[i-1] != s[i]:
    #     groups.append(1)
    #   else:
    #     groups[-1] += 1

    # ans = 0
    # for i in range(1,len(groups)):
    #   ans+=min(groups[i-1],groups[i])
    # return ans
