class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList: return 0
        d = defaultdict(list)
        for w in wordList:
            for i in range(len(w)): d[w[:i] + "*" + w[i+1:]].append(w)

        q = deque()
        q.append(beginWord)

        lvl, vis = 1, set()
        while q:
            for _ in range(len(q)):
                word = q.popleft()
                vis.add(word)
                for i in range(len(word)): 
                    for w in d[word[:i] + "*" + word[i+1:]]:
                        if w == endWord: return lvl+1
                        if w not in vis: q.append(w)
            lvl += 1

        return 0

        