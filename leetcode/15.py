class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        bucket = []
        while list1:
            bucket.append(list1.val)
            list1 = list1.next

        while list2:
            bucket.append(list2.val)
            list2 = list2.next

        dummy = ListNode(0)
        cur = dummy

        for i in sorted(bucket):
            cur.next = ListNode(i)
            cur = cur.next

        return dummy.next

        # while dummy.next:
        #     print(dummy.val)
        #     dummy = dummy.next



l1 = ListNode(1, ListNode(2, ListNode(4)))
l2 = ListNode(1, ListNode(3, ListNode(4)))

s = Solution()
s.mergeTwoLists(l1, l2)