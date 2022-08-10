# Merge Two Sorted Lists (Blind)

You are given the heads of two sorted linked lists `list1` and `list2`.

Merge the two lists in a one **sorted** list. The list should be made by 
splicing together the nodes of the first two lists.

Return the head of the merged linked list.

**Example 1**:

![](https://assets.leetcode.com/uploads/2020/10/03/merge_ex1.jpg)

```
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
```

**Example 2**:

```
Input: list1 = [], list2 = []
Output: []
```

**Example 3**:

```
Input: list1 = [], list2 = [0]
Output: [0]
```

**Solution**:

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
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