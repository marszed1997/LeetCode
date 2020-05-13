# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def __init__(self):
        self.ans = []

    def dfs(self, deep, root):
        if root is None:
            return
        try:
            self.ans[deep].append(root.val)
        except:
            self.ans.append([root.val])
        self.dfs(deep + 1, root.left)
        self.dfs(deep + 1, root.right)

    def levelOrder(self, root):
        """
        :param root: TreeNode
        :return: List[List[int]]
        """
        self.dfs(0, root)
        return self.ans

