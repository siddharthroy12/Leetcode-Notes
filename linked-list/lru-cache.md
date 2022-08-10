# LRU Cache

Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the `LRUCache` class:

- `LRUCache(int capacity)` Initialize the LRU cache with 
**positive** size `capacity`.

- `int get(int key)` Return the value of the `key` if the key 
exists, otherwise return `-1`.

- `void put(int key, int value)` Update the value of the `key` if 
the key exists. Otherwise, add the `key-value` pair to the cache. If 
the number of keys exceeds the `capacity` from this operation, 
**evict** the least recently used key.

- The functions `get` and `put` must each run in `O(1)` average time complexity.


**Example 1**:

```
Input
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, null, -1, 3, 4]

Explanation
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache is {1=1}
lRUCache.put(2, 2); // cache is {1=1, 2=2}
lRUCache.get(1);    // return 1
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    // returns -1 (not found)
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    // return -1 (not found)
lRUCache.get(3);    // return 3
lRUCache.get(4);    // return 4
```

**Solution**:

Use a doubly linked list where the left side is the least used
and the right side is most used and store the pointer to the node
in linked list in a hashmap.

```python
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next, self.prev = None, None

class LRUCache:
    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.least, self.most = Node(0, 0), Node(0, 0)
        self.least.next, self.most.prev = self.most, self.least

    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev
    
    # Insert from most
    def insert(self, node):
        prev = self.most.prev
        prev.next = node
        node.prev = prev
        node.next = self.most
        self.most.prev = node
    
    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].value
        return -1

    def put(self, key: int, value: int) -> None:
        # Update if exists
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            self.cache[key].value = value
        else: # If key doesn't exist
            if len(self.cache) >= self.capacity: # If we are out of capacity
                least_used = self.least.next
                del self.cache[least_used.key]
                self.remove(least_used)
            # Insert new node
            new_node = Node(key, value)
            self.cache[key] = new_node
            self.insert(new_node)
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
```