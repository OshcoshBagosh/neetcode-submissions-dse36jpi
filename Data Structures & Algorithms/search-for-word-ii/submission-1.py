class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        """
        The plan is to create a trie data structure, then we will add all words to the trie
        then we will use backtracking for the matrix to see if a word exists
        """
        class TrieNode:
            def __init__(self):
                self.children = {}
                self.end = False
            
            def add_word(self, word:str) -> None:
                cur = self
                for c in word:
                    if c not in cur.children:
                        cur.children[c] = TrieNode()
                    cur = cur.children[c]
                cur.end = True

        root = TrieNode()
        for w in words:
            root.add_word(w)

        ROWS, COLS = len(board), len(board[0])
        res, visit = set(), set()
        def backtrack(r, c, node, word):
            if (r < 0 or c < 0 or 
                r == ROWS or c == COLS or (r,c) in visit
                or board[r][c] not in node.children):

                return

            visit.add((r,c))
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.end:
                res.add(word)

            backtrack(r + 1, c, node, word)
            backtrack(r - 1, c, node, word)
            backtrack(r, c + 1, node, word)
            backtrack(r, c - 1, node, word)

            visit.remove((r,c))

        for r in range(ROWS):
            for c in range(COLS):
                backtrack(r, c, root, "")

        return list(res)

        
            

        