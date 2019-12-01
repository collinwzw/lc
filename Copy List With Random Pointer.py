"""
# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        self.visited = {}
        
        def getnode(node):
            if node:
                if node in self.visited:
                    return self.visited[node]
                
                else:
                    self.visited[node] = Node(node.val,None,None)
                    return self.visited[node]
            return None
        
        if not head:
            return head
        
        old_node = head
        new_node = Node(old_node.val,None,None)
        self.visited[old_node] = new_node
        
        while old_node != None:
            new_node.next = getnode(old_node.next)
            new_node.random = getnode(old_node.random)
            
            old_node = old_node.next
            new_node = new_node.next
        
        return self.visited[head]