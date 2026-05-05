# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """
        Rotating linked list is similar to array but lesser operational cost as just, 
        the new last element needs to point to Null and old last element needs to point to first.

        Can find length of linkedlist by slow and fast pointer. (slow pointer not used only cur 
        count)

        if k % n == 0
            return head
        else
            point last to first

        Point new last to Null
        and return new first
        """
        fast = head
        cur, n = 1, 0

        if not head:
            return head

        while fast and fast.next:
            prev = fast
            fast = fast.next.next
            cur += 1

        n = cur * 2 - 1 if fast else (cur - 1) * 2

        # print(F"{n=}, {fast=}, {cur=} ")

        shifts = k % n
        if shifts == 0:
            return head
        elif n&1:
            fast.next = head
            # print(f"Last ele: {fast.val}")
        else:
            prev.next.next = head
            # print(f"Last ele: {prev.next.val}")

        
        node, prev = head, head
        cur = 1
        while cur <= n - shifts:
            prev = node
            node = node.next
            cur += 1
        
        prev.next = None
        return node
