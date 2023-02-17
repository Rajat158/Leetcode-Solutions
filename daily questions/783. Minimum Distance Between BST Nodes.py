'''
Given the root of a Binary Search Tree (BST), return the minimum difference between the values of any two different nodes in the tree.

 

Example 1:


Input: root = [4,2,6,1,3]
Output: 1
Example 2:


Input: root = [1,0,48,null,null,12,49]
Output: 1
 

Constraints:

The number of nodes in the tree is in the range [2, 100].
0 <= Node.val <= 105
'''
class Solution:
    def __init__(self):
        self.Inorder = []
    
    def inorder(self, root):
        if not root:
            return
        self.inorder(root.left)
        self.Inorder.append(root.val)
        self.inorder(root.right)
    
    def minDiffInBST(self, root):
        if not root:
            return 0
        self.inorder(root)
        res = float('inf')
        for i in range(1, len(self.Inorder)):
            res = min(res, self.Inorder[i] - self.Inorder[i-1])
        return res
