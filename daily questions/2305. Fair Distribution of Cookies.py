'''
You are given an integer array cookies, where cookies[i] denotes the number of cookies in the ith bag. You are also given an integer k that denotes the number of children to distribute all the bags of cookies to. All the cookies in the same bag must go to the same child and cannot be split up.

The unfairness of a distribution is defined as the maximum total cookies obtained by a single child in the distribution.

Return the minimum unfairness of all distributions.

 

Example 1:

Input: cookies = [8,15,10,20,8], k = 2
Output: 31
Explanation: One optimal distribution is [8,15,8] and [10,20]
- The 1st child receives [8,15,8] which has a total of 8 + 15 + 8 = 31 cookies.
- The 2nd child receives [10,20] which has a total of 10 + 20 = 30 cookies.
The unfairness of the distribution is max(31,30) = 31.
It can be shown that there is no distribution with an unfairness less than 31.
Example 2:

Input: cookies = [6,1,3,2,2,4,1,2], k = 3
Output: 7
Explanation: One optimal distribution is [6,1], [3,2,2], and [4,1,2]
- The 1st child receives [6,1] which has a total of 6 + 1 = 7 cookies.
- The 2nd child receives [3,2,2] which has a total of 3 + 2 + 2 = 7 cookies.
- The 3rd child receives [4,1,2] which has a total of 4 + 1 + 2 = 7 cookies.
The unfairness of the distribution is max(7,7,7) = 7.
It can be shown that there is no distribution with an unfairness less than 7.
 

Constraints:

2 <= cookies.length <= 8
1 <= cookies[i] <= 105
2 <= k <= cookies.length
'''
class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        n = len(cookies)
        dp = [[-1] * (1 << n) for _ in range(k + 1)]
        
        def unfairness(k, bagMask):
            if dp[k][bagMask] != -1: 
                return dp[k][bagMask]
            
            def sum_cookies(Mask):
                sum=0
                for i in range(n):
                    if Mask&(1<<i):
                        sum+=cookies[i]
                return sum
            # end of  sum_cookies 
            if k==1:
                dp[k][bagMask] = sum_cookies(bagMask)
                return dp[k][bagMask]
            ans=2**31
            Mask=bagMask
            while(Mask>0):
                sum1=sum_cookies(Mask)
                sum2=unfairness(k - 1, bagMask ^ Mask)
                ans=min(ans, max(sum1, sum2))
                Mask=(Mask - 1) & bagMask
            dp[k][bagMask] = ans
            return ans
        # end of unfairness
        return unfairness(k, (1 << n) - 1)
