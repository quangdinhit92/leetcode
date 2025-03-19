class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:

        def traverse(root: Optional[TreeNode]):

            if not root.left and not root.right:
                return [root.val]

            ret = []
            if None != root.left:
                ret += traverse(root.left)

            if None != root.right:
                ret += traverse(root.right)

            return ret

        return traverse(root1) == traverse(root2)
