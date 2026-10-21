# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        before,after=ListNode(0),ListNode(0)
        l,r,curr=before,after,head
        while curr:
            follow=curr.next
            curr.next=None
            if curr.val<x:
                l.next=curr
                l=curr
            else:
                r.next=curr
                r=curr
            curr=follow
        l.next=after.next
        return before.next