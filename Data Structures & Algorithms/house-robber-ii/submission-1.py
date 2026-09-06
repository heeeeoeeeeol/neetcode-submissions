class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        one, two = 0, 0
        for n in nums[:-1]:
            tmp = max(one+n,two)
            one = two
            two = tmp
        three, four = 0, 0
        for n in nums[1:]:
            tmp = max(three+n,four)
            three = four
            four = tmp

        return max(two, four)