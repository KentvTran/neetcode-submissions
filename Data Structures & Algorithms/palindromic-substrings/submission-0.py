class Solution:
    def countSubstrings(self, s: str) -> int:
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
        
        n = len(s)
        palCounter = 0

        #2d array nxn
        dp = [[False] * n for _ in range(n)]

        #base case 1: len 1 palindrome
        for i in range(n):
            dp[i][i] = True
            palCounter += 1

        #base case 2: len 2 palindrome
        for i in range(n-1):
            if s[i] == s[i+1]:
                dp[i][i+1] = True
                palCounter += 1

        #base case 3: len 3+ palindrome 
        for length in range(3, n+1):
            for i in range(n-length+1):
                j = i + length - 1
                #check outer letters and inner letters
                if s[i] == s[j] and dp[i+1][j-1]:
                    dp[i][j] = True
                    palCounter +=1
        return palCounter
        
        