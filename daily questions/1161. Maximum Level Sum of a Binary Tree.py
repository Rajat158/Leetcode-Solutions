'''
LeetCode Logo
Problem List
160

avatar
1161. Maximum Level Sum of a Binary Tree
Medium
2.7K
83
Companies
Given the root of a binary tree, the level of its root is 1, the level of its children is 2, and so on.

Return the smallest level x such that the sum of all the values of nodes at level x is maximal.

 

Example 1:


Input: root = [1,7,0,7,-8,null,null]
Output: 2
Explanation: 
Level 1 sum = 1.
Level 2 sum = 7 + 0 = 7.
Level 3 sum = 7 + -8 = -1.
So we return the level with the maximum sum which is level 2.
Example 2:

Input: root = [989,null,10250,98693,-89388,null,null,null,-32127]
Output: 2
 

Constraints:

The number of nodes in the tree is in the range [1, 104].
-105 <= Node.val <= 105
'''

class Solution:
    def maxLevelSum(self, root):
        if not root:
            return 0

        queue = [root]
        max_level = 1
        max_sum = float('-inf')
        level = 1

        while queue:
            level_sum = 0
            next_level = []

            for node in queue:
                level_sum += node.val

                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)

            if level_sum > max_sum:
                max_sum = level_sum
                max_level = level

            queue = next_level
            level += 1

        return max_level
