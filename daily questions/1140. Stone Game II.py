'''
Alice and Bob continue their games with piles of stones.  There are a number of piles arranged in a row, and each pile has a positive integer number of stones piles[i].  The objective of the game is to end with the most stones. 

Alice and Bob take turns, with Alice starting first.  Initially, M = 1.

On each player's turn, that player can take all the stones in the first X remaining piles, where 1 <= X <= 2M.  Then, we set M = max(M, X).

The game continues until all the stones have been taken.

Assuming Alice and Bob play optimally, return the maximum number of stones Alice can get.

 

Example 1:

Input: piles = [2,7,9,4,4]
Output: 10
Explanation:  If Alice takes one pile at the beginning, Bob takes two piles, then Alice takes 2 piles again. Alice can get 2 + 4 + 4 = 10 piles in total. If Alice takes two piles at the beginning, then Bob can take all three piles left. In this case, Alice get 2 + 7 = 9 piles in total. So we return 10 since it's larger. 
Example 2:

Input: piles = [1,2,3,4,5,100]
Output: 104
 

Constraints:

1 <= piles.length <= 100
1 <= piles[i] <= 104
'''
class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        dp = {} 
        def recursion(index,M):
            # if we reached to the end we cannot score any value
            if index == n:
                return 0
            # we search if we have solved the same case earlier
            if (index,M) in dp:
                return dp[(index,M)] 
            # total remaining score is the sum of array from index to the end
            total = sum(piles[index:])           
            # if we can take the complete array it is the best choice
            if index + 2*M >= n :return total
            # my_score is the score we are getting as the player who is playing
            my_score = 0
            for x in range(index,index+2*M):
                # opponent score will be calculated by next recursion
                opponent_score = recursion(x+1,max(M,x-index+1))
                # my_score is the remaining value of total - opponent_score
                my_score = max(my_score,total - opponent_score)          
            # this is memoization part
            dp[(index,M)] = my_score
            # return the score
            return my_score
        
        return recursion(0,1)
