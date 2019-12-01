# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import collections
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
#         s = ""
#         if not root:
#             return s
#         self.ans = []
#         q = collections.deque()
#         q.append([root,1])
        
#         while len(q)>0:
            
#             cur_node,index = q.popleft()

#             while len(self.ans) < index:
#                 self.ans.append('null')
#             self.ans.append(cur_node.val)
#             if cur_node.left:
#                 q.append([cur_node.left, index*2])
#             if cur_node.right:
#                 q.append([cur_node.right,index*2+1])
        
#         for element in self.ans:
#             s += str(element)
#             s +=','
#         print(s[:-1])
#         return s[:-1]
        stack = []
        stack.append(root)
        string = ''
        while len(stack) >0:
            cur = stack.pop()
            if cur == None:
                string += 'None,'
            else:
                string += str(cur.val) + ','
                stack.append(cur.right)
                stack.append(cur.left)
        
        print(string)
        return string
                
            
    
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        li = list(data.split(','))
        print(li)
        def rec(l):
            if l[0] == 'None':
                l.pop(0)
                return None
            
                
            root = TreeNode(l[0])
            l.pop(0)
            root.left = rec(l)
            root.right = rec (l)
            return root
        root = rec(li)
        return root

            
                
        # if not data:
        #     return None
        # d =collections.defaultdict()
        # print(data)
        # li = list(data.split(','))
        # print(li)
        # root = TreeNode(int(li[1]))
        # d[1] = root
        # for index in range(2, len(li) ):
        #     if li[index] != 'null':
        #         if index/2 *2 == index:
        #             d[index/2].left = TreeNode(int(li[index]))
        #             d[index] = d[index/2].left
        #         else:
        #             d[index/2].right = TreeNode(int(li[index]))
        #             d[index] = d[index/2].right
        # return root
# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))