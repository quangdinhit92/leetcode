# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

        n = len(nums)
        root = TreeNode()

        def buildTree(left, right):

            if left > right:
                return None

            mid = (left + right) // 2

            root = TreeNode(val=nums[mid])

            root.left = buildTree(left, mid - 1)
            root.right = buildTree(mid + 1, right)

            return root

        return buildTree(0, n - 1)
