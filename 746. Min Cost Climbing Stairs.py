class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        if n == 1:
            return cost[0]
        if n == 2:
            return min(cost[0], cost[1])

        minArr = [0] * n
        minArr[0], minArr[1] = cost[0], cost[1]

        for i in range(2, n):
            minArr[i] = min(minArr[i - 1], minArr[i - 2]) + cost[i]
        
        # Return the minimum cost to reach the top from last element or the one before
        return min(minArr[-1], minArr[-2])
