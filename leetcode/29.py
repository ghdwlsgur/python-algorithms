from collections import deque

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        def rightFirst(node, level, list):
            if node is None:
                return

            if len(list) < level:
                list.append(node.val)

            rightFirst(node.right, level+1, list)
            rightFirst(node.left, level+1, list)


        result = []
        rightFirst(root, 1, result)
        return result



node5 = TreeNode(5)
node2 = TreeNode(2, None, node5)
node4 = TreeNode(4)
node3 = TreeNode(3, None, node4)
root = TreeNode(1, node2, node3)

# node2 = TreeNode(2)
# root = TreeNode(1, None, node2)

s = Solution()
print(s.rightSideView(root))

