class TrieNode:
    def __init__(self):
        self.children = [None]*26
        self.end = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for c in word:
            if not curr.children[ord(c)-ord('a')]: curr.children[ord(c)-ord('a')] = TrieNode()
            curr = curr.children[ord(c)-ord('a')]
        curr.end = True

    def search(self, word: str) -> bool:
        curr = self.root
        for c in word:
            if not curr.children[ord(c)-ord('a')]: return False
            curr = curr.children[ord(c)-ord('a')]
        return curr.end

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for c in prefix:
            if not curr.children[ord(c)-ord('a')]: return False
            curr = curr.children[ord(c)-ord('a')]
        return True
     
        