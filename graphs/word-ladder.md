```python
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        nei = {}
        wordList.append(beginWord)

        # Build adjacency list
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + '*' + word[i+1:]
                if pattern not in nei:
                    nei[pattern] = []
                nei[pattern].append(word)

        # bfs
        visited = set([beginWord])
        currentLevel = [beginWord]
        res = 1
        while currentLevel:
            nextLevel = []
            for word in currentLevel:
                if word == endWord:
                    return res
                for i in range(len(word)):
                    pattern = word[:i] + '*' + word[i+1:]
                    for n in nei[pattern]:
                        if n not in visited:
                            visited.add(n)
                            nextLevel.append(n)
            currentLevel = nextLevel
            res += 1

        return 0
```
