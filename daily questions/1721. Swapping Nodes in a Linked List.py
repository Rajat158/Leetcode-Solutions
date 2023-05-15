'''
You are given the head of a linked list, and an integer k.

Return the head of the linked list after swapping the values of the kth node from the beginning and the kth node from the end (the list is 1-indexed).

 

Example 1:


Input: head = [1,2,3,4,5], k = 2
Output: [1,4,3,2,5]
Example 2:

Input: head = [7,9,6,6,7,8,3,0,9,5], k = 5
Output: [7,9,6,6,8,7,3,0,9,5]
 

Constraints:

The number of nodes in the list is n.
1 <= k <= n <= 105
0 <= Node.val <= 100
'''

class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        curr = head
        for _ in range(k-1):
            curr = curr.next
        # curr is reached to first desired node 

        # save it as first to exchange val later 
        first = curr

        # initialize sec node to head
        second = head 

        # when curr reaches the end , second will be at desired node
        while curr.next:
            curr = curr.next
            second = second.next
        
        # so then just swap the values if first and second node 
        first.val, second.val = second.val, first.val 

        # return head 
        return head


        
