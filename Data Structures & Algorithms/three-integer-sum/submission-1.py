class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ret = []
        nums = sorted(nums)

        for i, n in enumerate(nums):
            start = 0
            end = len(nums)-1

            while start < end:
                if start == i: start += 1 
                elif end == i: end -= 1 
                elif nums[start] + nums[end] > -n: end-=1 
                elif nums[start] + nums[end] < -n: start+=1 
                else: 
                    temp = sorted([n, nums[start], nums[end]])
                    if temp not in ret: ret.append(temp)
                    break

        return ret