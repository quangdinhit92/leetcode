# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def traversal(root: TreeNode, max_sofar):

            good = 0
            if max_sofar <= root.val:
                max_sofar = root.val
                good = 1

            l = 0
            if root.left:
                l = traversal(root.left, max_sofar)

            r = 0
            if root.right:
                r = traversal(root.right, max_sofar)
            return good + r + l

        return traversal(root, root.val)
