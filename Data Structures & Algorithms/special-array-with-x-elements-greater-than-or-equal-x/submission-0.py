class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()
        l, r = 1, len(nums)

        while l <= r:
            mid = (l+r)//2
            c = sum(1 for n in nums if n >= mid)
            if c < mid: r = mid-1
            elif c > mid: l = mid+1
            else: return mid
        return -1