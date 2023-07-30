'''
There is a strange printer with the following two special properties:

The printer can only print a sequence of the same character each time.
At each turn, the printer can print new characters starting from and ending at any place and will cover the original existing characters.
Given a string s, return the minimum number of turns the printer needed to print it.

 

Example 1:

Input: s = "aaabbb"
Output: 2
Explanation: Print "aaa" first and then print "bbb".
Example 2:

Input: s = "aba"
Output: 2
Explanation: Print "aaa" first and then print "b" from the second place of the string, which will cover the existing character 'a'.
 

Constraints:

1 <= s.length <= 100
s consists of lowercase English letters.
'''
class Solution:
    def strangePrinter(self, s: str) -> int:
        n=len(s)
        if not s:
            return 0

        dp=[[sys.maxsize]*n for _ in range(n)]

        for i in range(n):
            dp[i][i]=1

        for l in range(2,n+1):
            for i in range(n-l+1):
                j=i+l-1
                dp[i][j]=dp[i+1][j]+1

                for k in range(i+1,j+1):
                    if s[i]==s[k]:
                        dp[i][j]=min(dp[i][j],dp[i][k-1]+(dp[k+1][j] if j>k else 0))

        return dp[0][n-1]                        
