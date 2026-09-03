class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList: return 0
        q = deque()
        q.append(beginWord)

        lvl = 1
        while q:
            for _ in range(len(q)):
                w = q.popleft()
                for i in range(len(w)):
                    j=0
                    lenw = len(wordList)
                    while j < lenw:
                        if w[:i] + w[i+1:] == wordList[j][:i] + wordList[j][i+1:]:
                            if wordList[j] == endWord: return lvl + 1
                            q.append(wordList[j])
                            wordList.pop(j)
                            lenw -= 1
                        else:
                            j += 1
            lvl += 1

        return 0