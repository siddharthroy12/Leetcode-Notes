```python
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        pre_map = { c: [] for c in range(numCourses)}
        
        for course, pre in prerequisites:
            pre_map[course].append(pre)
        
        visited, cycle = set(), set()
        output = []
        
        def dfs(course):
            if course in cycle:
                return False
            if course in visited:
                return True
            
            cycle.add(course)
            for pre in pre_map[course]:
                if dfs(pre) == False:
                    return False
            cycle.remove(course)
            visited.add(course)
            output.append(course)
            return True
        
        for course in range(numCourses):
            if dfs(course) == False:
                return []
            
        return output
```
