class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        dp = [sys.maxsize for x in range(0,amount+1)]
        dp[0] = 0
        
        #recursion is better
        
        for a in range(1,amount+1):
            for coin in coins:
                if coin <= a:
                    dp[a] = min(dp[a],dp[a-coin] + 1)
        
        
#         def helper(target):
#             if dp[target] != sys.maxsize:
#                 return dp[target]
#             else:
                
#                 if target in coins:
#                     dp[target] = 1
#                     return 1
#                 else:
#                     for coin in coins:
#                         dp[target] = min(dp[target], helper(target - coin) + 1)
#                         return dp[target]
                    
        
        
        if dp[-1] == sys.maxsize:
            return -1
        return dp[-1]
                    
        
        