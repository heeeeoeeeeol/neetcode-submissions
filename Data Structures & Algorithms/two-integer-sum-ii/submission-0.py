class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(1, len(numbers)):
            if numbers[i] + numbers[i-1] == target:
                return [i, i+1]
        