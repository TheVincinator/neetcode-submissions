class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode() 

    def insert(self, word: str) -> None:
        curr = self.root
        for i, char in enumerate(word):
            if char not in curr.children:
                curr.children[char] = TrieNode()
            if i == len(word) - 1:
                curr.endOfWord = True
            curr = curr.children[char]

    def search(self, word: str) -> bool:
        curr = self.root
        for i, char in enumerate(word):
            if char not in curr.children:
                return False
            if i == len(word) - 1:
                if not curr.endOfWord:
                    return False
            curr = curr.children[char]
        return True

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for char in prefix:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        return True
        
        
        