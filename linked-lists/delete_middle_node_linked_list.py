from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Edge case: only one node
        if not head.next:
            return None

        slow = head
        fast = head.next.next

        # Move pointers until fast reaches the end
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Delete the middle node
        slow.next = slow.next.next

        return head