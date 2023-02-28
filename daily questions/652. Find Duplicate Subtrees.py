'''
Given the root of a binary tree, return all duplicate subtrees.

For each kind of duplicate subtrees, you only need to return the root node of any one of them.

Two trees are duplicate if they have the same structure with the same node values.

 

Example 1:


Input: root = [1,2,3,4,null,2,4,null,null,4]
Output: [[2,4],[4]]
Example 2:


Input: root = [2,1,1]
Output: [[1]]
Example 3:


Input: root = [2,2,2,3,null,3,null]
Output: [[2,3],[3]]
 

Constraints:

The number of the nodes in the tree will be in the range [1, 5000]
-200 <= Node.val <= 200
'''
class Solution:
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        def traverse(node):
            if not node:
                return None
            left = traverse(node.left)
            right = traverse(node.right)
            subtree = (node.val, left, right)
            subtree_id = subtree_ids.get(subtree)
            if subtree_id is None:
                subtree_id = len(subtrees)
                subtrees.append(subtree)
                subtree_ids[subtree] = subtree_id
            subtree_counts[subtree_id] += 1
            if subtree_counts[subtree_id] == 2:
                duplicates.append(node)
            return subtree_id

        subtrees = []
        subtree_ids = {}
        subtree_counts = defaultdict(int)
        duplicates = []
        traverse(root)
        return duplicates
