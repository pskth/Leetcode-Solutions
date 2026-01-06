# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        max_level = -1
        max_sum = -float('inf')
        levels = []
        levels.append([root])

        for i, level in enumerate(levels):
            # print(i, level)
            cur_sum = 0
            next_level = []

            for root in level:
                cur_sum += root.val
                if root.left:
                    next_level.append(root.left)
                if root.right:
                     next_level.append(root.right)

            if max_sum < cur_sum:
                max_sum = cur_sum
                max_level = i + 1
            if next_level:
                levels.append(next_level)

        return max_level