class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)

        m = 0 
        for num in nums: 
            if num-1 in numset:
                continue
            i = num
            while i in numset:
                i+=1
            if i - num >= m: m = i-num

        return m


                

        