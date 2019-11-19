class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums) == 0:
            return []
        stack = []
        ans = [-sys.maxsize for x in range(0,len(nums))]
        cur = 0
        move = 1
        
        while cur%len(nums) != move%len(nums):
            if nums[cur%len(nums)] < nums[move% len(nums)]:  #we find the next biggest element!
                ans[cur%len(nums)] = nums[move% len(nums)]
                

                while len(stack) >0:
                    cur = stack.pop()
                    ans[cur%len(nums)] = nums[move%len(nums)]
                cur = move
                move += 1
            else:
                
                while len(stack) >0 and nums[stack[-1]%len(nums)] < nums[move%len(nums)]:
                    popitem = stack.pop()
                    ans[popitem%len(nums)] = nums[move%len(nums)]
                if ans[move%len(nums)] == -sys.maxsize:
                    stack.append(move)
                #print(stack)
                move +=1
                
        while len(stack) >0:
            if nums[stack[-1]%len(nums)] < nums[move%len(nums)]:
                ans[stack.pop()%len(nums)] = nums[cur]
            else:
                ans[stack.pop()%len(nums)] = -1
        ans[cur] = -1
        return ans