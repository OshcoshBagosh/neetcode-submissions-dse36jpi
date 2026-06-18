class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        from collections import deque
        if endWord not in wordList:
            return 0

        n = len(beginWord)
        
        def is_one(w1, w2):
            count = 0
            for i in range(n):
                if w1[i] != w2[i]:
                    count += 1
                if count > 1:
                    return False

            return count == 1
        words = 0
        queue = deque([beginWord])
        visit = [False] * len(wordList)
        while queue:
            words += 1
            for _ in range(len(queue)):
                node = queue.popleft()
                if node == endWord:
                    return words
                for i in range(len(wordList)):
                    if visit[i]:
                        continue
                    if is_one(node, wordList[i]):
                        queue.append(wordList[i])
                        visit[i] = True
        
        return 0