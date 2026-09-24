class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        ind = [i for i in range(len(names))]
        ind.sort(key=lambda i: -heights[i])
        return [names[i] for i in ind]