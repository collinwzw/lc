# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        cur = head
        self.l = []
        while cur != None:
            self.l.append(cur.val)
            cur = cur.next
        
        def helper(start,end,parent):
            if start > end:
                return
            mid = (start + end)/2
            new = TreeNode(self.l[mid])
            if self.l[mid] < parent.val:
                parent.left = new
            else:
                parent.right = new

            helper(start,mid-1,new)
            helper(mid+1,end,new)
            
        head = TreeNode(sys.maxsize)
        helper(0, len(self.l) - 1,head)
        return head.left
            
            
            
            
            
        