class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for n in nums:
            if n in d:
                d[n] += 1
            else:
                d.setdefault(n, 1)

        return list(dict(sorted(d.items(), key=lambda x: x[1], reverse=True)).keys())[:k]