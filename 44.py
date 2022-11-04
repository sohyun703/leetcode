class Solution:
    result: int = 0

    def longestPath(self, root: TreeNode) -> int:
        def dfs(node: TreeNode):
            if node is None:
                return 0

						#존재하지 않는 노드까지 탐색 , 재귀구조
            left = dfs(node.left)
            right = dfs(node.right)

						#현재노드와 자식노드가 동일할 경우 거리 1 증가
            if node.left and node.left.val == node.val:
                left+=1
            else:
                left = 0
            if node.right and node.right.val == node.val:
                right+=1
            else:
                right = 0

            self.result = max(self.result, left+right)
            return max(left,right)

        dfs(root)
        return self.result