class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        bucket1 = []
        bucket2 = []
        while l1:
            bucket1.append(l1.val)
            l1 = l1.next

        while l2:
            bucket2.append(l2.val)
            l2 = l2.next

        num1 = int(''.join(map(str, bucket1[::-1])))
        num2 = int(''.join(map(str, bucket2[::-1])))
        res = num1 + num2

        res = [int(i) for i in str(res)]
        res = res[::-1]

        node = ListNode(res[0])
        cur = node

        for i in range(1, len(res)):
            cur.next = ListNode(res[i])
            cur = cur.next

        return node
        # while node:
        #     print(node.val)
        #     node = node.next



l1 = ListNode(2, ListNode(4, ListNode(3)))
l2 = ListNode(5, ListNode(6, ListNode(4)))

s = Solution()
s.addTwoNumbers(l1, l2)


