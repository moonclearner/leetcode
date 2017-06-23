'''
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


class Solution(object):
    def maxDepth(self, root):
        if root == None: return 0
        node_list = [root]
        depth = 0
        while not node_list == []:
            depth += 1
            next_level = []
            for node in node_list:
                if not node.left == None:
                    next_level.append(node.left)
                if not node.right == None:
                    next_level.append(node.right)
            node_list = next_level
        return depth
