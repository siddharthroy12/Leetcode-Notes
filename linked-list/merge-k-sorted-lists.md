# Merge k Sorted Lists

You are given an array of `k` linked-lists `lists`, each linked-list is sorted in ascending order.

*Merge all the linked-lists into one sorted linked-list and return it*.

**Example 1**:

```
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6
```

**Example 2**:

```
Input: lists = []
Output: []
```

**Example 3**:

```
Input: lists = [[]]
Output: []
```

**Solution**:

Use divide and conquer method

![](https://leetcode.com/problems/merge-k-sorted-lists/Figures/23/23_divide_and_conquer_new.png)

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        
        while len(lists) > 1:
            mergedLists = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i+1] if (i+1) < len(lists) else None
                mergedLists.append(self.mergeTwoLists(l1, l2))
            lists = mergedLists
        
        return lists[0]
    
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        new_node = None
        head = None
        p1 = list1
        p2 = list2
        
        while p1 or p2:
            new_value = None
            
            if not p1 and p2:
                new_value = p2.val
                p2 = p2.next
            if not p2 and p1:
                new_value = p1.val
                p1 = p1.next
                
            if p1 and p2:
                if p1.val > p2.val:
                    new_value = p2.val
                    p2 = p2.next
                else:
                    new_value = p1.val
                    p1 = p1.next
            
            if not new_node:
                new_node = ListNode(new_value)
                head = new_node
            else:
                new_node.next = ListNode(new_value)
                new_node = new_node.next
        
        return head
```

Time Complexity: O(n log k) where k is number of linked list and n
is total number of nodes in two lists.

Space Complexity: O(1)