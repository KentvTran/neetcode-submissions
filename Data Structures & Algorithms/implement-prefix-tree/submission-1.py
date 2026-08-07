class TrieNode:
    def __init__(self):
        self.children = {} #map a single char to its next Node
        self.endOfWord = False

class PrefixTree:

    def __init__(self):
        self.root =TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root

        for char in word:
            if char not in curr.children:
                #append char to to Trie
                curr.children[char] = TrieNode()
            #traverse child if it is there
            curr = curr.children[char]
        curr.endOfWord = True

    def search(self, word: str) -> bool:
        curr = self.root

        for char in word:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        return curr.endOfWord

    def startsWith(self, prefix: str) -> bool:
        curr = self.root

        for char in prefix:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        return True
        