class Solution:
    def commonChars(self, words: List[str]) -> List[str]:        
        cnt = Counter(words[0])

        for w in words[1:]:
            wc = Counter(w)
            for c in cnt:
                cnt[c] = min(cnt[c], wc[c])

        res = []
        for c in cnt:
            for _ in range(cnt[c]): res.append(c)

        return res