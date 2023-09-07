class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        # cur_node = root
        # if cur_node.left and cur_node.right:
        #     return cur_node.val
        #
        # min_num = float('inf')
        # memory = root.val
        #
        # while cur_node:
        #     if cur_node.val is not None and cur_node.val != memory:
        #         diff = memory - cur_node.val
        #         memory = cur_node.val
        #         if min_num > diff:
        #             min_num = diff
        #     cur_node = cur_node.left
        #
        # while cur_node:
        #     if cur_node.val is not None and cur_node.val != memory:
        #         diff = memory - cur_node.val
        #         memory = cur_node.val
        #         if min_num > diff:
        #             min_num = diff
        #     cur_node = cur_node.right
        #
        # return min_num

        # def inorder(node):
        #     if not node:
        #         return []
        #     return inorder(node.left) + [node.val] + inorder(node.right)
        #
        # values = inorder(root)
        # min_diff = float('inf')
        #
        # for i in range(1, len(values)):
        #     diff = values[i] - values[i - 1]
        #     min_diff = min(min_diff, diff)
        #
        # return min_diff

        def inorder(node):
            if not node:
                return []
            return inorder(node.left) + [node.val] + inorder(node.right)

        values = inorder(root)
        min_diff = float('inf')

        for i in range(1, len(values)):
            diff = values[i] - values[i - 1]
            min_diff = min(min_diff, diff)

        return min_diff


node1 = TreeNode(1)
node3 = TreeNode(3)
node2 = TreeNode(2, node1, node3)
node6 = TreeNode(6)
root = TreeNode(4, node2, node6)

s = Solution()

print(s.getMinimumDifference(root))
