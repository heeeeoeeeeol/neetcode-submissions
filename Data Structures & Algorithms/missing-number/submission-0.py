class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        for i in range(len(nums)+1):
            if i not in cnt: return i