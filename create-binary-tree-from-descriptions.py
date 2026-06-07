# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        nodes = defaultdict(TreeNode)
        child = set()
        root = set()

        for par, ch, il in descriptions:
            nodes[par].val = par
            nodes[ch].val = ch

            if il:
                nodes[par].left = nodes[ch]
            else:
                nodes[par].right = nodes[ch]

            if nodes[par] not in child:
                root.add(nodes[par])

            child.add(nodes[ch])
            root.discard(nodes[ch])

        return list(root)[0]
