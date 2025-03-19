# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        if not root:
            return []

        ret = []

        queue = deque([root])

        while queue:
            queue_len = len(queue)

            for i in range(queue_len):

                node = queue.popleft()

                if i == queue_len - 1:
                    ret.append(node.val)

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

        return ret
