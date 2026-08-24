class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        ind_0 = -1
        flag_one_0 = False
        flag_mult_0 = False

        for i in range(len(nums)):
            if nums[i] == 0: 
                if flag_one_0:
                    flag_mult_0 = True
                else:
                    flag_one_0 = True
                    ind_0 = i
                continue
            product*= nums[i]

        if flag_mult_0:
            return [0] * len(nums)
        elif flag_one_0:
            ret = [0] * len(nums)
            ret[ind_0] = product
            return ret
        else:
            for i in range(len(nums)):
                nums[i] = int(product / nums[i])
            return nums