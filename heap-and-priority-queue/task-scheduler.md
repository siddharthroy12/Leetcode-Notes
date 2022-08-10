# Task Scheduler

Given a characters array `tasks`, representing the tasks a CPU needs to do, 
where each letter represents a different task. Tasks could be done in any 
order. Each task is done in one unit of time. For each unit of time, the CPU 
could complete either one task or just be idle.

However, there is a non-negative integer `n` that represents the cooldown 
period between two **same tasks** (the same letter in the array), that is 
that there must be at least `n` units of time between any two same tasks.

Return *the least number of units of times that the CPU will take to finish 
all the given tasks*.

**Example 1**:

```
Input: tasks = ["A","A","A","B","B","B"], n = 2
Output: 8
Explanation: 
A -> B -> idle -> A -> B -> idle -> A -> B
There is at least 2 units of time between any two same tasks.
```

**Example 2**:

```
Input: tasks = ["A","A","A","B","B","B"], n = 0
Output: 6
Explanation: On this case any permutation of size 6 would work since n = 0.
["A","A","A","B","B","B"]
["A","B","A","B","A","B"]
["B","B","B","A","A","A"]
...
And so on.
```

**Example 3**:

```
Input: tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"], n = 2
Output: 16
Explanation: 
One possible solution is
A -> B -> C -> A -> D -> E -> A -> F -> G -> A -> idle -> idle -> A -> idle -> idle -> A
```

**Solution**

```python
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # length of maximum occuring character
        maxTaskCount = max(Counter(tasks).values())
        # total number of characters occuring at max times
        maxCountRepeats = Counter(Counter(tasks).values())[maxTaskCount]

        return max(len(tasks), ((maxTaskCount-1) * (n+1)) + maxCountRepeats)
        
```

**maxTaskCount** = length of maximum occuring character
**maxCountRepeats** = total number of character that are occuring for max times.

Let's take a example **AAABBBC** , **n=2**
maxTaskCount: 3 => `AAA` and `BBB`
maxCountRepeats: 2 => `AAA` and `BBB`
result: 7 => `ABCAB#AB`

First we try to fill most frequent character and a empty gap of length `n` is created between these two characters.

`A _ _ A _ _ A`

Here places of most frequent character is fixed, and in empty spaces we have to fill remaining character, we can also notice that length of all part (excluding last character `'A'`) is equals to `(maxTaskCount - 1) * (n+1)` , i.e. `A _ _ A _ _`.

Reason: As we are excluding last `'A'` total slots created is `(maxTaskCount-1)` and after including `'A'` and empty spaces `(A _ _ )`, length of one slot is `(n+1)`
so, length after excluding last `'A'` = `(maxTaskCount-1)*(n+1)`.

But, there can be a case where more than one character can appear for max times, so in this case we have to fill second character just after first,

`A B _ A B _ A B`

in this case, length of last part which was excluded earlier is equals to `maxCountRepeats`, `A B _ A B _ A B`
so, `totalLength = ((maxTaskCount-1) * (n+1)) + maxCountRepeats`

But, wait!, what if we have given n=0, we don't have to bother about the order of occurences, so it result will be equals to tasks.length.
So,

`result = max(len(tasks), ((maxTaskCount-1) * (n+1)) + maxCountRepeats)`