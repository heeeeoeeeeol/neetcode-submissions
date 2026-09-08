class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        least = [sys.maxsize]*(amount+1)
        least[0] = 0

        for i in range(1, amount+1):
            for c in coins:
                if i == c: least[i] = 1
                if i > c: least[i] = min(least[i], least[i-c]+1)

        return -1 if least[amount] == sys.maxsize else least[amount]

