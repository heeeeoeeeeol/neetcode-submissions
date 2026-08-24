class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        changes = [0] * len(prices)

        prev = prices[0]
        for i, n in enumerate(prices):
            changes[i] = n-prev
            prev = n

        print(changes)

        m = 0
        s = 0
        for i, n in enumerate(changes):
            if s < 0:
                s = n
            else:
                s += n
            if s > m:
                m = s

        return m
            