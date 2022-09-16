```python
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prerqMap = {}
        
        for pair in prerequisites:
            if pair[0] not in prerqMap:
                prerqMap[pair[0]] = [pair[1]]
            else:
                prerqMap[pair[0]].append(pair[1])
        
        def dfs(current, seen):
            if current in prerqMap:
                for prerq in prerqMap[current]:
                    if prerq in seen:
                        return False
                    else:
                        s.add(prerq)
                        if dfs(prerq, seen) == False:
                            return False
                        else:
                            s.remove(prerq)
                            
                del prerqMap[current]
            return True
        
        for num in range(numCourses):
            s = set()
            s.add(num)
            if dfs(num, s) == False:
                return False
            
        return True
```
