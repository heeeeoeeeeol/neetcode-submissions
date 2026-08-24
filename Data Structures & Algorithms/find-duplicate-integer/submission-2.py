class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = fast = 0

        while 1:
            fast=nums[nums[fast]]
            slow=nums[slow]
            if fast==slow: break

        fast=0
        while 1:
            fast=nums[fast]
            slow=nums[slow]
            if fast==slow: break

        return fast