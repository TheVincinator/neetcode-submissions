class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.endOfWord = True

    def search(self, word: str) -> bool:
        def searchRec(word, curr):
            for i, c in enumerate(word):
                if c == ".":
                    for child in curr.children.values():
                        if not searchRec(word[i + 1:], child):
                            continue
                        return True
                    return False
                elif c not in curr.children:
                    return False
                curr = curr.children[c]
            return curr.endOfWord
        return searchRec(word, self.root)
