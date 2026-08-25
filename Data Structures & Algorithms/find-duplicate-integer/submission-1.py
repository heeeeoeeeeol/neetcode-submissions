class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = fast = nums[0]

        while fast!=slow:
            fast=nums[nums[fast]]
            slow=nums[slow]

        fast=nums[0]
        while fast!=slow:
            fast=nums[fast]
            slow=nums[slow]

        return fast