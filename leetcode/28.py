
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        def inorder(node):
            if not node:
                return []
            return inorder(node.left) + [node.val] + inorder(node.right)

        values = inorder(root)

        return values[k-1]

# node2 = TreeNode(2)
# node1 = TreeNode(1, None, node2)
# node4 = TreeNode(4)
# root = TreeNode(3, node1, node4)

node1 = TreeNode(1)
node2 = TreeNode(2, node1, None)
node4 = TreeNode(4)
node3 = TreeNode(3, node2, node4)
node6 = TreeNode(6)
root = TreeNode(5, node3, node6)


s = Solution()
s.kthSmallest(root, 3)
