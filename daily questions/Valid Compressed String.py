'''
A special compression mechanism can arbitrarily delete 0 or more characters and replace them with the deleted character count.
Given two strings, S and T where S is a normal string and T is a compressed string, determine if the compressed string  T is valid for the plaintext string S. 


Example 1:

Input:
S = "GEEKSFORGEEKS"
T = "G7G3S"
Output:
1
Explanation:
We can clearly see that T is a valid 
compressed string for S.

Example 2:

Input:
S = "DFS"
T = "D1D"
Output :
0
Explanation:
T is not a valid compressed string.

Your Task:  
You don't need to read input or print anything. Your task is to complete the function checkCompressed() which takes 2 strings S and T as input parameters and returns integer 1 if T is a valid compression of S and 0 otherwise.


Expected Time Complexity: O(|T|)
Expected Auxiliary Space: O(1)


Constraints:
1 ≤ |S| ≤ 106
1 ≤ |T| ≤ 106
All characters are either capital or numeric.

'''
# import math
class Solution:
    def checkCompressed(self, S, T):
        # code here
        i=0
        j=0
        m=len(S)
        n=len(T)

        while i<m and j<n:
            if not T[j].isdigit():
                if T[j]!=S[i]:
                    return 0
                i+=1
                j+=1
            else:
                k=j+1
                while k<n and T[k].isdigit():k+=1
                i+=int(T[j:k])
                j=k
        return 1 if i==m and j==n else 0
