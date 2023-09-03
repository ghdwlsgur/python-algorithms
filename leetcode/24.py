# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#
# class Solution(object):
#     def sortList(self, head):
#         """
#         :type head: ListNode
#         :rtype: ListNode
#         """
#         l = []
#         while head:
#             l.append(head.val)
#             head = head.next
#
#         dummy = ListNode(0)
#         cur = dummy
#         pointer, change_pointer = 0, 0
#         minimum = float('inf')
#
#         while pointer < len(l):
#             for idx, num in enumerate(l[pointer:]):
#                 if minimum > num:
#                     minimum = num
#                     change_pointer = idx + pointer
#             l[pointer], l[change_pointer] = l[change_pointer], l[pointer]
#
#             cur.next = ListNode(l[pointer])
#             cur = cur.next
#
#             pointer += 1
#             minimum = float('inf')
#
#         return dummy.next

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head

        slow = head
        fast = head.next

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next


        mid = slow.next
        slow.next = None

        left = self.sortList(head)
        right = self.sortList(mid)

        tmp = ref = ListNode(0)

        while(left and right):
            if left.val < right.val:
                tmp.next = left
                left = left.next
            else:
                tmp.next = right
                right = right.next
            tmp = tmp.next

        tmp.next = left if left else right

        return ref.next


s = Solution()

#
# head = ListNode(4, ListNode(2, ListNode(1, ListNode(3))))
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
s = Solution()
print(s.sortList(head))

