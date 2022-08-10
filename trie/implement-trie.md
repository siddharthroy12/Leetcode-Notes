# Implement Trie

A trie (pronounced as "try") or prefix tree is a tree data structure used to
efficiently store and retrieve keys in a dataset of strings.
There are various applications of this data structure, such as autocomplete and spellchecker.

Implement the Trie class:

- `Trie()` Initializes the trie object.
- `void insert(String word)` Inserts the string `word` into the trie.
- `boolean search(String word)` Returns `true` if the string `word` is in
the trie (i.e., was inserted before), and `false` otherwise.
- `boolean startsWith(String prefix)` Returns `true` if there is a previously
inserted string `word` that has the prefix `prefix`, and `false` otherwise.

**Example 1**:

```
Input

["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
[[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]

Output

[null, null, true, false, true, null, true]

Explanation

Trie trie = new Trie();
trie.insert("apple");
trie.search("apple");   // return True
trie.search("app");     // return False
trie.startsWith("app"); // return True
trie.insert("app");
trie.search("app");     // return True
```

**Solution**:

```js
class TrieNode {
  constructor(value) {
    this.value = value;
    this.nexts = {};
    this.end = false;
  }
}

var Trie = function() {
    this.root = new TrieNode(null);
};

/**
 * @param {string} word
 * @return {void}
 */
Trie.prototype.insert = function(word) {
    let currentNode = this.root;

  for (let i = 0; i < word.length; i++) {
    const letter = word[i];

    if (currentNode.nexts[letter]) {
      currentNode = currentNode.nexts[letter];

      if (i === word.length-1) {
        currentNode.end = true;
      }

      continue;
    } else {
      let newNode = new TrieNode(letter);

      currentNode.nexts[letter] = newNode;

      currentNode = newNode;

      if (i === word.length-1) {
        currentNode.end = true;
      }

      continue;
    }
  }
};

/** 
 * @param {string} word
 * @return {boolean}
 */
Trie.prototype.search = function(word) {
    let currentNode = this.root;

  for (let i = 0; i < word.length; i++) {
    const letter = word[i];

    if (!currentNode.nexts[letter]) {
      return false;
    }

    currentNode = currentNode.nexts[letter];
  }

  return currentNode.end;
};

/**
 * @param {string} prefix
 * @return {boolean}
 */
Trie.prototype.startsWith = function(prefix) {
    let currentNode = this.root;

  for (let i = 0; i < prefix.length; i++) {
    const letter = prefix[i];

    if (!currentNode.nexts[letter]) {
      return false;
    }

    currentNode = currentNode.nexts[letter];
  }

  return Object.keys(currentNode).length > 0;
};

/**
 * Your Trie object will be instantiated and called as such:
 * var obj = new Trie()
 * obj.insert(word)
 * var param_2 = obj.search(word)
 * var param_3 = obj.startsWith(prefix)
 */
```

Every method in this class has Time Complexity of O(n) where n is the

length of the input word.