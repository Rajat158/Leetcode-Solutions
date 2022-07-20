'''
Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.

 

Example 1:

Input: nums = [4,3,2,7,8,2,3,1]
Output: [5,6]
Example 2:

Input: nums = [1,1]
Output: [2]
 

Constraints:

n == nums.length
1 <= n <= 105
1 <= nums[i] <= n
'''
#Solution-->
class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # return set(range(1, len(nums) + 1)) - set(nums)
        output = []
        n = len(nums) + 1
        nums = set(nums)
        
        for i in range(1, n):
            if i not in nums:
                output.append(i)
        
        return output
