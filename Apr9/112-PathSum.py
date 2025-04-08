# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        else:
            if not root.left and not root.right:
                if targetSum - root.val == 0:
                    return True
                else:
                    return False
            return self.hasPathSum(root.left, targetSum - root.val) | self.hasPathSum(
                root.right, targetSum - root.val
            )

        # if not root:
        #     return False

        # def dfs(node:TreeNode,target):
        #     if node:
        #         if not node.left and not node.right:

        #             if 0 ==target - node.val :
        #                 return True
        #             return False

        #         target -=node.val
        #         if True == dfs(node.left,target):
        #             return True
        #         if True ==dfs(node.right,target):
        #             return True
        #         return False
        #     return False
        # return dfs(root,targetSum)
