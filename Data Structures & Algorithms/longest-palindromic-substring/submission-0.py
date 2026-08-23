class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s

        n = len(s)
        #make 2d array nxn
        dp = [[False]*n for _ in range(n)]

        startIx = 0
        maxLen = 1

        #base case 1 len 1 palindrome
        for i in range(n):
            dp[i][i] = True 
        #base case 2 len 2 palindrome
        for i in range(n-1):
            if s[i] == s[i+1]:
                dp[i][i+1] = True 
                startIx = i
                maxLen = 2
        #base case 3 len 3+ palindrome
        for length in range(3,n+1):
            for i in range(n-length+1):
                j = i + length - 1
                #check outer layers and inner palindrome
                if s[i] == s[j] and dp[i+1][j-1]:
                    dp[i][j] = True
                    #update maxLen
                    if length > maxLen:
                        startIx = i
                        maxLen = length
        return s[startIx: startIx + maxLen]