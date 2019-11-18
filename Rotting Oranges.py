import collections
class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        #BFS
        
        # better solution?
        
        rott_point_list = []
        n_fresh = 0
        for row in range(0,len(grid)):
            for col in range(0,len(grid[0])):
                if grid[row][col] == 2:
                    rott_point_list.append([row,col]) 
                elif grid[row][col] == 1:
                    n_fresh += 1
                
        if n_fresh == 0:
            return 0
        if len(rott_point_list) == 0:
            return -1
        queue = collections.deque()
        
        for rott_point in rott_point_list:
            queue.append([rott_point,0])
            
        while len(queue)> 0:
            cur_point, cur_minutes = queue.popleft()
            for moved in [[cur_point[0]+1,cur_point[1]],[cur_point[0]-1,cur_point[1]],[cur_point[0],cur_point[1]+1],[cur_point[0],cur_point[1]-1]]:
                if moved[0]>= 0 and moved[0] < len(grid) and moved[1]>= 0 and moved[1]< len(grid[0]) and grid[moved[0]][moved[1]] == 1:
                    grid[moved[0]][moved[1]] = 0
                    n_fresh -= 1
                    queue.append([moved,cur_minutes+1])
                    
        
        if n_fresh != 0:
            return -1
        else:
            return cur_minutes
                    