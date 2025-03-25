# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: int
        """
        # duyet theo chieu sau, moi lan di qua 1 node ta se co duoc remain cua no , toi khi remain =0 nghia la ta tinh dc target
        prefixSum = defaultdict(int)
        prefixSum[0] = 1

        def sumPath(node, total):

            if not node:
                return 0

            total += node.val
            count = prefixSum[total - targetSum]
            prefixSum[total] += 1

            count += sumPath(node.left, total)
            count += sumPath(node.right, total)

            prefixSum[total] -= 1

            return count

        return sumPath(root, 0)
