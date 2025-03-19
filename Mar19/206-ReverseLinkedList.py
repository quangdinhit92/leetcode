# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # if not head:
        #     return None

        # if None == head.next:
        #     return head

        # new_head = self.reverseList(head.next)

        # head.next.next=head
        # head.next=None

        # return new_head

        pre = None
        cur = head
        while cur:
            nextNode = cur.next
            cur.next = pre
            pre = cur
            cur = nextNode
        return pre
