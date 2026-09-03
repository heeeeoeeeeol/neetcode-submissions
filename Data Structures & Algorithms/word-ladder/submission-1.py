class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        q = deque()
        try: wordList.remove(endWord)
        except ValueError: return 0
        q.append(endWord)
        wordList.append(beginWord)

        lvl = 1
        while q:
            for _ in range(len(q)):
                w = q.popleft()
                for i in range(len(w)):
                    for j in range(len(wordList)):
                        if w[:i] + w[i+1:] == wordList[j][:i] + wordList[j][i+1:]:
                            if wordList[j] == beginWord: return lvl + 1
                            q.append(wordList[j])
                            wordList[j] = ""
            lvl += 1

        return 0