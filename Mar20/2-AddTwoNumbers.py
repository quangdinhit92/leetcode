# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        # ve ban chat ta se duyet 2 list va theo cai dai hon
        head = ListNode()
        tmp = head

        while l1 or l2:
            v = 0
            r = 0
            if l1:
                v += l1.val
                l1 = l1.next
            if l2:
                v += l2.val
                l2 = l2.next

            # tmp luu lai gia tri cua node hien tai

            v += tmp.val
            # tinh dc r cho node tiep theo
            r = v // 10
            # cap nhat
            tmp.val = v % 10

            tmp.next = ListNode(r)

            # truong hop dac biet la 2 day ket thuc va r=0
            if not l1 and not l2 and 0 == r:
                tmp.next = None
                break
            # neu day con hoac r# 0 thi tiep tuc chay
            tmp = tmp.next
        return head
