# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        queue = deque([root])
        minLevel = 1
        level = 0

        levelSum = []

        while queue:
            queue_len = len(queue)
            tmp = 0
            level += 1

            for i in range(queue_len):
                node = queue.popleft()
                tmp += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            print(f"level:{level} sum:{tmp}")
            levelSum.append((level, tmp))

        maxLevel = levelSum[0][0]
        maxSum = levelSum[0][1]

        for item in levelSum:
            if item[1] > maxSum:
                maxSum = item[1]
                maxLevel = item[0]
        return maxLevel
