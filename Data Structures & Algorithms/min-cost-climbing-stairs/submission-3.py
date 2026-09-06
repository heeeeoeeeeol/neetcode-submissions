class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        first, second = 0, 0
        for c in cost:
            tmp = c + min(first, second)
            first = second
            second = tmp

        return min(first,second)