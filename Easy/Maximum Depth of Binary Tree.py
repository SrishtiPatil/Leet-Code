class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root == None:
            return 0
        if root.left == None and root.right == None:
            return 1
        else:
            left = self.maxDepth(root.left)
            right = self.maxDepth(root.right)
            if left > right:
                return left+1
            else:
                return right+1
        
