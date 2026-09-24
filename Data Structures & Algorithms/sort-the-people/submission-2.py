class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        return [i[1] for i in reversed(sorted(list(zip(heights, names))))]