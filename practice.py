
class Solution:

#3Sum
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         hashset = []
        
#         nums.sort()
        
#         for i in range(0,len(nums)-1):
#             left = i+1
#             right = len(nums) -1
#             while (left !=right):
#                 if nums[i] + nums[left] + nums[right] == 0:
#                     if [nums[i],nums[left],nums[right]] not in hashset:
#                         hashset.append([nums[i],nums[left],nums[right]])
#                     if left + 1 != right:
#                         left +=1
#                         right -=1
#                     else:
#                         break
#                 elif nums[i] + nums[left] + nums[right] > 0:
#                     right -= 1
#                 elif nums[i] + nums[left] + nums[right] < 0:
#                     left +=1
        
#         return hashset   
        

    def threeSum(self, nums):
        res = []
        nums.sort()
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l, r = i+1, len(nums)-1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s < 0:
                    l +=1 
                elif s > 0:
                    r -= 1
                else:
                    res.append((nums[i], nums[l], nums[r]))
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    l += 1; r -= 1
        return res

    #Maximum subarray
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [-sys.maxsize for x in range(0,len(nums))]
        
        dp[0] = nums[0]
        for i in range(1,len(nums) ):
            if nums[i-1] > 0:
                nums[i] += nums[i-1]
            dp[i] = max(nums[i],dp[i-1])
        print(dp)
        return dp[len(dp) - 1]

    #Merge Inteval

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 0:
            return []
        s_stack = []
        e_stack = []

        intervals.sort(key = lambda x:x[0])
        
        ans = []
        
        s_stack.append(intervals[0][0])
        e_stack.append(intervals[0][1])       
        for i in range(1,len(intervals)):
            if intervals[i][0] <= e_stack[len(e_stack) -1]:
                if intervals[i][1] > e_stack[len(e_stack) -1]:
                    e_stack.pop()
                    e_stack.append(intervals[i][1])
                else:
                    continue
            else:
                s_stack.append(intervals[i][0])
                e_stack.append(intervals[i][1])
        
        for i in range(0,len(e_stack)):
            ans.append([s_stack[i],e_stack[i]])

        
        
        return ans

#973. K Closest Points to Origin

    def calculate_dis_square(point):
        return point[0]**2 + point[1]**2
    
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        hashtable = {}
        for point in points:
            distance = Solution.calculate_dis_square(point)
            if distance in hashtable.keys():
                temp = hashtable.get(distance)
                temp.append(point)
                hashtable.update({distance: temp})
            else:    
                hashtable.update({distance: [point]})
            
        dis_list = hashtable.keys()
        #print(dis_list)
        sorted_dis_list = sorted(dis_list)
        #print(sorted_dis_list)
        ans = []
        for i in range(0,K):
         #   print(hashtable.keys())
            if len(hashtable.get(sorted_dis_list[i])) == 1:
                ans.append(hashtable.get(sorted_dis_list[i])[0])
            else:
                for element in hashtable.get(sorted_dis_list[i]):
                    ans.append(element)
                    #print(ans)
                if len(ans) == K:
                    return ans
        return ans
                    
#289. Game of Life
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        # Neighbors array to find 8 neighboring cells for a given cell
        neighbors = [(1,0), (1,-1), (0,-1), (-1,-1), (-1,0), (-1,1), (0,1), (1,1)]

        rows = len(board)
        cols = len(board[0])

        # Create a copy of the original board
        copy_board = [[board[row][col] for col in range(cols)] for row in range(rows)]

        # Iterate through board cell by cell.
        for row in range(rows):
            for col in range(cols):

                # For each cell count the number of live neighbors.
                live_neighbors = 0
                for neighbor in neighbors:

                    r = (row + neighbor[0])
                    c = (col + neighbor[1])

                    # Check the validity of the neighboring cell and if it was originally a live cell.
                    # The evaluation is done against the copy, since that is never updated.
                    if (r < rows and r >= 0) and (c < cols and c >= 0) and (copy_board[r][c] == 1):
                        live_neighbors += 1

                # Rule 1 or Rule 3        
                if copy_board[row][col] == 1 and (live_neighbors < 2 or live_neighbors > 3):
                    board[row][col] = 0
                # Rule 4
                if copy_board[row][col] == 0 and live_neighbors == 3:
                    board[row][col] = 1
#121. Best Time to Buy and Sell Stock I
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        minimum = sys.maxsize
        for price in prices:
            if price < minimum:
                minimum = price
                continue
            
            if price - minimum > profit:
                profit = price - minimum
        
        return profit
        
#122. Best Time to Buy and Sell Stock II
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
         
        for i in range(1,len(prices)):
            if prices[i] > prices[i-1]:
                profit += (prices[i] - prices[i -1])
                
        return profit