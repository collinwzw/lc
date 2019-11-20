import collections

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        d = collections.defaultdict(list)
        for i in range(0,numCourses):
            d[i] = []
        
        for course,pre in prerequisites:
            d[pre].append(course)
        print(d)
        #DFS
        self.visited = [False for x in range(0,numCourses)]
        self.ans =[]
        self.check_cycle = [False for x in range(0,numCourses)]
        self.cycle = False
        
        def DFS(course):
        
            self.ans.append(course)
            self.visited[course] = True
            self.check_cycle[course] = True
            for c in d[course]:
                if self.check_cycle[c] == True:
                    self.cycle = True
                    return
                if self.visited[c] != True:
                    DFS(c)
                self.check_cycle[course] = False
            
        for course in range(0,numCourses):
            if self.visited[course] == True:
                continue
            else:
                DFS(course)
                
        print(self.ans)
        if self.cycle == True:
            return False
        
        return len(self.ans) == numCourses

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        dic = collections.defaultdict(set)
        neigh = collections.defaultdict(set)
        for i, j in prerequisites:
            dic[i].add(j)
            neigh[j].add(i)
        stack = [i for i in range(numCourses) if not dic[i]]
        res = []
        while stack:
            node = stack.pop()
            res.append(node)
            for i in neigh[node]:
                dic[i].remove(node)
                if not dic[i]:
                    stack.append(i)
            dic.pop(node)
        return res if not dic else []