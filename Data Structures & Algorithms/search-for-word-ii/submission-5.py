class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

class PrefixTree:
    def __init__(self, words):
        self.root = TrieNode()
        for word in words: self.insert(word)

    def insert(self, word):
        curr = self.root
        for c in word:
            if c not in curr.children: curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.end = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        pre = PrefixTree(words).root
        res = set()
        path = []

        def backtrack(r, c, curr):
            if r < 0 or r >= len(board) or c < 0 or c >= len(board[r]) or board[r][c] not in curr.children: return
            
            path.append(board[r][c])
            if curr.children[board[r][c]].end: res.add("".join(path))
                
            board[r][c] = "$"
            backtrack(r-1,c,curr.children[path[-1]])
            backtrack(r+1,c,curr.children[path[-1]])
            backtrack(r,c-1,curr.children[path[-1]])
            backtrack(r,c+1,curr.children[path[-1]])
            board[r][c] = path[-1]
            path.pop()

        for r in range(len(board)):
            for c in range(len(board[r])):
                backtrack(r, c, pre)
        return list(res)
        