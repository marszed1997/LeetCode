# https://leetcode-cn.com/problems/kth-ancestor-of-a-tree-node/

class TreeAncestor:

    def __init__(self, n, parent):
        """
        :param n: int
        :param parent: List[int]
        """
        self.son = [[] for _ in range(n + 1)]
        self.lca = [[-1 for i in range(20)] for _ in range(n + 1)]
        for id, par in enumerate(parent):
            self.son[par].append(id)
        self.dfs(0, -1)

    def get_lca(self, node, fa):
        tmp_fa = fa
        self.lca[node][0] = fa
        for i in range(1, 20):
            if tmp_fa == -1:
                break
            self.lca[node][i] = self.lca[tmp_fa][i - 1]
            tmp_fa = self.lca[node][i]

    def dfs(self, node, fa):
        self.get_lca(node, fa)
        for son in self.son[node]:
            self.dfs(son, node)

    def getKthAncestor(self, node, k):
        """
        :param node: int
        :param k: int
        :return: int
        """
        cnt = 0
        fa = node
        while k:
            if fa == -1:
                return -1
            if k % 2 != 0:
                fa = self.lca[fa][cnt]
            cnt += 1
            k = k // 2
        return fa

# Your TreeAncestor object will be instantiated and called as such:
# obj = TreeAncestor(n, parent)
# param_1 = obj.getKthAncestor(node,k)
