class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False #flag for end of a valid word

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.endOfWord = True

    def search(self, word: str) -> bool:
        def dfs(ix, node):
            if ix == len(word):
                return node.endOfWord
            char = word[ix]

            #wildcard char case
            if char == ".":
                for child in node.children.values():
                    #keep searching for matching children
                    if dfs(ix + 1, child):
                        return True
                #children not found
                return False
            #standard char case
            else:
                if char not in node.children:
                    return False
                return dfs(ix + 1, node.children[char])
        return dfs(0,self.root)
        
