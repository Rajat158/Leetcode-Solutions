'''
Given the root of a Binary Search Tree (BST), return the minimum absolute difference between the values of any two different nodes in the tree.

 

Example 1:


Input: root = [4,2,6,1,3]
Output: 1
Example 2:


Input: root = [1,0,48,null,null,12,49]
Output: 1
 

Constraints:

The number of nodes in the tree is in the range [2, 104].
0 <= Node.val <= 105
 

Note: This question is the same as 783: https://leetcode.com/problems/minimum-distance-between-bst-nodes/
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        # Initialize variables for previous value and minimum difference
        prev = float('-inf')  # Initialize prev to negative infinity
        min_diff = float('inf')  # Initialize min_diff to positive infinity
        
        def inorderTraversal(root):
            nonlocal prev, min_diff
            if not root:
                return
            
            # In-order traversal: visit the left subtree
            if root.left:
                inorderTraversal(root.left)
            
            # Compare the current node's value with the previous value
            if (root.val - prev) < min_diff:
                min_diff = root.val - prev
            
            # Update the previous value to the current node's value
            prev = root.val
            
            # In-order traversal: visit the right subtree
            if root.right:
                inorderTraversal(root.right)
                
        # Start the in-order traversal from the root of the binary tree
        inorderTraversal(root)
        
        # Return the minimum difference between any two nodes in the tree
        return min_diff
