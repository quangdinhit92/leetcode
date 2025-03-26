# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not list1 and not list2:
            return None
        head = ListNode()
        cur = head
        while list1 and list2:
            if list1.val < list2.val:
                cur.val = list1.val
                list1 = list1.next
            else:
                cur.val = list2.val
                list2 = list2.next
            if list1 or list2:
                cur.next = ListNode()
                cur = cur.next

        while list1:
            cur.val = list1.val
            list1 = list1.next
            if list1:
                cur.next = ListNode()
                cur = cur.next
        while list2:
            cur.val = list2.val
            list2 = list2.next
            if list2:
                cur.next = ListNode()
                cur = cur.next
        return head
