class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children: curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.end = True

    def search(self, word: str) -> bool:
        def dfs(i, node):
            for j in range(i, len(word)):
                if word[j] not in node.children: 
                    if word[j] == ".":
                        for val in node.children.values(): 
                            if dfs(j+1, val): return True
                        return False
                    else:
                        return False
                node = node.children[word[j]]
            return node.end

        curr = self.root
        return dfs(0, curr)
        
