class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[-1] == max(nums): return nums[0]

        l, r = 0, len(nums)-1

        while (r-l)>1:
            mid = (l+r)//2

            if nums[mid] > nums[r]:
                l = mid
            elif nums[mid] < nums[r]:
                r = mid

        if l == len(nums)-1:
            return nums[0]
        else: return nums[l+1]