## 206. Reverse Linked List
# Given the head of a singly linked list, reverse the list, and return the reversed list.

# ## Implementation

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_linked_list(head: ListNode) -> ListNode:
    prev = None
    temp = head
    while temp:
        front = temp.next
        temp.next = prev
        prev = temp
        temp = front

    return prev
