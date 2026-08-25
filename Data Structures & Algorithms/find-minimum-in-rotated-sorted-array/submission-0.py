class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1

        prev = nums[-1]
        while l < r:
            mid = (l+r)//2

            if nums[mid] > prev:
                l = mid+1
                prev = nums[mid]
            elif nums[mid] < prev:
                r = mid-1
                prev = nums[mid]

        if l == len(nums)-1:
            return nums[0]
        else: return nums[l+1]