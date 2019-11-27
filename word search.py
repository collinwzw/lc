import collections
class Solution:
    def exist(self, board,word):
        #DFS with backtracking
        s_p = collections.deque()
        
        for row in range(0,len(board)):
            for col in range(0, len(board[0])):
                if board[row][col] == word[0]:
                    s_p.append([row,col,1])
                
        
        
        while len(s_p) >0:
            queue = collections.deque()
            queue.append(s_p.popleft())
            
            while len(queue) > 0:
                c_r, c_c,c_i = queue.popleft()
                temp = board[c_r][c_c]
                board[c_r][c_c] = ''

                    
                if c_i == len(word):
                    return True
                
                for m_r, m_c in [[c_r+1,c_c],[c_r-1,c_c],[c_r,c_c+1],[c_r,c_c-1]]:
                    if m_r >= 0 and m_c >= 0 and m_r < len(board) and m_c < len(board[0]) and board[m_r][m_c] == word[c_i]:
                        
                        queue.append([m_r,m_c,c_i+1])
                    
                board[c_r][c_c] = temp
            
                            
                
        return False


a = Solution()
board = [["a","a"]]
string = "aaa"
a.exist(board,string)