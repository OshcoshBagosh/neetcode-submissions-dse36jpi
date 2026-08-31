"""
Since we are dealing with searching prefixes we can use a prefix tree/trie
"""
class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()  

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.end = True
    
    """
    "."s can be any letter in alphabet so we can apply dfs to search to find word
    if our curr char is a letter we continue through the path
    """

    def search(self, word: str) -> bool:
        def dfs(root, j):
            cur = root

            for i in range(j, len(word)):
                c = word[i]
                if c == ".":
                    for child in cur.children.values():
                        if dfs(child, i + 1):
                            return True
                    return False
                else:
                    if c not in cur.children:
                        return False
                    cur = cur.children[c]

            return cur.end
        
        return dfs(self.root, 0)


        
