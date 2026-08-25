class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[-1] > nums[0]: return nums[0]

        l, r = 0, len(nums)-1

        while r > l:
            mid = (l+r)//2

            if nums[mid] > nums[l]:
                l = mid
            else:
                r = mid

            print(nums[l], nums[r])
            

        return nums[r+1]