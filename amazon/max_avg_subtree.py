class TreeNode:
    def __init__(self, value):
        self.val = value
        self.children = []

class Solution:

    def max_average_subtree(self, root):

        if not root or root.children:
            return None

        self.result = [float('-inf'), 0]
        self.dfs(root)
        return self.result[1]

    def dfs(self, root):

        if not root.children:
            return [root.val, 1]

        temp_sum, temp_num = root.val, 1

        for child in root.children:
            child_sum, child_num = self.dfs(child)
            temp_sum += child_sum
            temp_num += child_num

        if temp_sum/temp_num > self.result[0]:
            self.result = [temp_sum/temp_num, root.val]

        return [temp_sum, temp_numlin]
