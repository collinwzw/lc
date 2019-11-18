class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        
        # starting from back of the input string.
        # uses recursion
        # backtracking the added words
        # If it reaches index 0 then return the str which is converted from string.
        
        self.check = [False for x in range(0, len(s)+1)]
        self.check[0] = True   
        self.ans = []
        def helper(start, temp_list):
            print(temp_list)
            if start == len(s):
                if self.check[-1] == True:
                    self.ans.append(temp_list.copy())
            else:
                for i in range(start, len(s)+1):
                    if self.check[start] == True and s[start:i] in wordDict:
                        self.check[i] = True
                        temp_list.append(s[start:i])
                        helper(i,temp_list)
                        temp_list.pop()
                        self.check[i] = False
                        

        
        helper(0,[])
        
        return self.ans


s = "catsanddog"
words = ["cat","cats","and","sand","dog"]

a =Solution()
print(a.wordBreak(s,words))