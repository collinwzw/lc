
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