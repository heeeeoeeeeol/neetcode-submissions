class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1

        while r > l:
            mid = (l+r)//2

            if nums[mid] < nums[r]:
                r = mid
            else:
                l = mid+1

        
        start, end = 0, len(nums)-1

        while start <= end:
            mid = (end+start)//2
            if nums[(mid+l)%len(nums)] > target: end = mid-1
            elif nums[(mid+l)%len(nums)] < target: start = mid+1
            else: return (mid+l)%len(nums)

        return -1