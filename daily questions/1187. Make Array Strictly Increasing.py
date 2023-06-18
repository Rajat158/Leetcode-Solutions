'''
Given two integer arrays arr1 and arr2, return the minimum number of operations (possibly zero) needed to make arr1 strictly increasing.

In one operation, you can choose two indices 0 <= i < arr1.length and 0 <= j < arr2.length and do the assignment arr1[i] = arr2[j].

If there is no way to make arr1 strictly increasing, return -1.

 

Example 1:

Input: arr1 = [1,5,3,6,7], arr2 = [1,3,2,4]
Output: 1
Explanation: Replace 5 with 2, then arr1 = [1, 2, 3, 6, 7].
Example 2:

Input: arr1 = [1,5,3,6,7], arr2 = [4,3,1]
Output: 2
Explanation: Replace 5 with 3 and then replace 3 with 4. arr1 = [1, 3, 4, 6, 7].
Example 3:

Input: arr1 = [1,5,3,6,7], arr2 = [1,6,3,3]
Output: -1
Explanation: You can't make arr1 strictly increasing.
 

Constraints:

1 <= arr1.length, arr2.length <= 2000
0 <= arr1[i], arr2[i] <= 10^9
'''

class Solution:
    def makeArrayIncreasing(self, first: List[int], second: List[int]) -> int:
        @cache
        def dp(i: int, prev_max: int) -> int:
            if i == len(first):
                return 0

            j = bisect_right(second, prev_max)

            return min(
                dp(i + 1, first[i]) if first[i] > prev_max else maxsize,
                dp(i + 1, second[j]) + 1 if j < len(second) else maxsize,
            )

        second.sort()
        operations = dp(0, -maxsize)
        return operations if operations != maxsize else -1
