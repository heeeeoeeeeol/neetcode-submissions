class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start = 0
        end = len(numbers)-1

        while start < end:
            if target < numbers[start] + numbers[end]:
                end -= 1
            elif target > numbers[start] + numbers[end]:
                start += 1
            else:
                return [start+1, end+1]

        