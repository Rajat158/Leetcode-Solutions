'''
The array-form of an integer num is an array representing its digits in left to right order.

For example, for num = 1321, the array form is [1,3,2,1].
Given num, the array-form of an integer, and an integer k, return the array-form of the integer num + k.

 

Example 1:

Input: num = [1,2,0,0], k = 34
Output: [1,2,3,4]
Explanation: 1200 + 34 = 1234
Example 2:

Input: num = [2,7,4], k = 181
Output: [4,5,5]
Explanation: 274 + 181 = 455
Example 3:

Input: num = [2,1,5], k = 806
Output: [1,0,2,1]
Explanation: 215 + 806 = 1021
 

Constraints:

1 <= num.length <= 104
0 <= num[i] <= 9
num does not contain any leading zeros except for the zero itself.
1 <= k <= 104
'''
class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        if not num:
            return [int(d) for d in str(k)]
        carry = 0
        res = []
        for i in range(len(num)-1, -1, -1):
            total = num[i] + carry + (k % 10)
            carry = total // 10
            res.append(total % 10)
            k //= 10
        while k > 0:
            total = carry + (k % 10)
            carry = total // 10
            res.append(total % 10)
            k //= 10
        if carry > 0:
            res.append(carry)
        return res[::-1]
