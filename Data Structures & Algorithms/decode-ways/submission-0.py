class Solution:
    def numDecodings(self, s: str) -> int:
        if len(s) == 0 or  s[0] == "0":
            return 0
        if len(s) == 1 and s[0] != "0":
            return 1

        dp = [0]*(len(s) + 1)
        dp[0] = 1
        dp[1] = 1

        for i in range(2,len(s)+1):
            #check current char
            if s[i-1] != '0':
                dp[i] += dp[i-1]
            #check 2-digit number
            if int(s[i-2:i]) <= 26 and s[i-2] > '0':
                dp[i] += dp[i-2]
        return dp[len(s)]

                
        