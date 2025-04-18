# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0
        q = deque()
        q.append((root, 1))

        while q:
            for _ in range(len(q)):
                node, depth = q.popleft()
                if node:
                    q.append((node.left, 1 + depth))

                    q.append((node.right, 1 + depth))

                    if not node.left and not node.right:
                        return depth
