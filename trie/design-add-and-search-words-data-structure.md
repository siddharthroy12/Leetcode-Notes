# Design Add and Search Words Data Structure

Design a data structure that supports adding new words and finding if a string matches any previously added string.

Implement the `WordDictionary` class:

- `WordDictionary()` Initializes the object.
- `void addWord(word)` Adds `word` to the data structure, it can be matched later.
- `bool search(word)` Returns `true` if there is any string in the data structure 
that matches `word` or `false` otherwise. `word` may contain   
dots `'.'` where dots can be matched with any letter.

**Example***:

```
Input
["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
Output
[null,null,null,null,false,true,true,true]

Explanation
WordDictionary wordDictionary = new WordDictionary();
wordDictionary.addWord("bad");
wordDictionary.addWord("dad");
wordDictionary.addWord("mad");
wordDictionary.search("pad"); // return False
wordDictionary.search("bad"); // return True
wordDictionary.search(".ad"); // return True
wordDictionary.search("b.."); // return True
```

**Solution**:

```python
class Node:
    def __init__(self, value, end):
        self.value = value
        self.nexts = {}
        self.end = end

class WordDictionary:

    def __init__(self):
        self.root = Node(None, False)

    def addWord(self, word: str) -> None:
        current = self.root
        
        for i, letter in enumerate(word):
            if letter not in current.nexts:
                current.nexts[letter] = Node(letter, False)
                
            if i == len(word)-1:
                current.nexts[letter].end = True
            else:
                current = current.nexts[letter]
            

    def search(self, word: str) -> bool:
        
        def dfs(node, pointer) -> bool:
            if pointer >= len(word):
                return False
            
            letter = word[pointer]
            
            if letter != ".":
                if letter in node.nexts:
                    if pointer == len(word) - 1 and node.nexts[letter].end:
                        return True
                    return dfs(node.nexts[word[pointer]], pointer+1)
                else:
                    return False
            else:
                if not len(node.nexts):
                    return False
                
                for k in node.nexts:
                    if pointer == len(word) - 1 and node.nexts[k].end:
                        return True
                    
                    if dfs(node.nexts[k], pointer+1):
                        return True
                
                return False
        
        return dfs(self.root, 0)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
```