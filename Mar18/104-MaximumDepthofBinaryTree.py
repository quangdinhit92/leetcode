# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        l = self.maxDepth(root.left)
        r = self.maxDepth(root.right)
        # not null -> +1 vao dem , tim left right
        return 1 + max(l, r)

        # def count(node: Optional[TreeNode],counting):
        #     if not node:
        #         return counting
        #     c0 = count(node.left,counting+1)
        #     c1 = count(node.right,counting+1)

        #     counting=max(c0,c1)

        #     return counting

        # return count(root,0)
