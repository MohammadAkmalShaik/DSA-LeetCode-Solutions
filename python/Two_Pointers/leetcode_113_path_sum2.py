class Solution(object):
    def pathSum(self, root, targetSum):
        res = []
        path = []

        def dfs(node, curr):
            if not node:
                return
            path.append(node.val)
            curr += node.val
            if not node.left and not node.right:
                if curr == targetSum:
                    res.append(list(path))
            else:
                dfs(node.left, curr)
                dfs(node.right, curr)
            path.pop()

        dfs(root, 0)
        return res
