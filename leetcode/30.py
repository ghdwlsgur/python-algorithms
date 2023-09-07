class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """

        def searchLevel(node, level, result):
            if node is None:
                return

            if len(list) == level:
                result.append(node.val)

            if node.left:
                result.append(node.left)
            if node.right:
                result.append(node.right)

        result = []
        searchLevel(root, 1, result)
        print(result)
            # searchLevel(node.left, level+1)
            # print(node.val)

            # right = searchLevel(node.right, level+1)
            # print(node.val)
            # print(left.val)
            # return [searchLevel(node.left, level+1, list)] + [searchLevel(node.right, level+1, list)]

        # result = []
        result = searchLevel(root, 1)
        # print(result)






node9 = TreeNode(9)
node15 = TreeNode(15)
node7 = TreeNode(7)
node20 = TreeNode(20, node15, node7)
root = TreeNode(3, node9, node20)

s = Solution()
print(s.averageOfLevels(root))