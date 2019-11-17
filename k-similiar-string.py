import collections
import sys
class Solution(object):
    def kSimilarity(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        
        #sort?
        # not BFS, but similair concept
        # find the letter that euqals B[i] and do swap, backtracking it and find the next one, swap it. 
        # let m = len(B)
        # O(m^2)  swap is constant time
        #better solution?
        #we can store the A into a hash map, so we can get index of particular char in constant time and swap them. then we have to update the d everytime.
        
#         d = collections.defaultdict(list)
#         for index, element in enumerate(A):
#             d[element].append(index)
            
#         print(d)
        self.ans = sys.maxsize
        A = list(A)

        def helper(index,swaps):
            if index == len(B) - 1:
                return min(self.ans,swaps)
            else:
                if A[index] == B[index]:
                    return helper(index +1,swaps)
                else:
                    for i in range(index+1, len(A)):
                        if A[i] == B[index]:
                            temp = A[i]
                            A[i] = A[index]
                            print(A)
                            return helper(index+1, swaps+1)
                            A[i] = temp
        return helper(0,0)


a =Solution()
A="bccaba"
B="abacbc"

print(a.kSimilarity(A,B))
