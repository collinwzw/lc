# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, inorder, postorder):
        
        
        # post order, last element must be the root
        # in inorder, find where the root value is and we know everything to the left in order list is left part of root, everything in right is right of the root
        
        #recursively do that?
        
        
        def helper(inor):
            if len(inor) == 0:
                return None
            if len(inor) == 1:
                return TreeNode(inor)
            
            else:
                root = TreeNode(postorder.pop())
                
                for index in range(0,len(inor)):
                    if inor[index] == root.val:
                        
                        root.right = helper(inor[index+1:])
                        root.left = helper(inor[:index])
                        break
                return root
            
        return helper(inorder)
                        
inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]

a = Solution()
a.buildTree(inorder,postorder)
        