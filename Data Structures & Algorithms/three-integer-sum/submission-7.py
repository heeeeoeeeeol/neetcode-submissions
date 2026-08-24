class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ret = []
        nums = sorted(nums)
        
        for i, n in enumerate(nums):
            start = 0
            end = len(nums)-1

            while start < end:
                if start == i: 
                    start += 1 
                    continue
                elif end == i: 
                    end -= 1 
                    continue

                if nums[start] + nums[end] > -n: 
                    end-=1 
                    continue
                elif nums[start] + nums[end] < -n: 
                    start+=1 
                    continue
                else: 
                    if i < start:
                        temp = [n, nums[start], nums[end]]
                    elif i > end:
                        temp = [nums[start], nums[end], n]
                    else:
                        temp = [nums[start], n, nums[end]]
                    if temp not in ret: ret.append(temp)
                    start += 1
                    end -= 1

        return ret