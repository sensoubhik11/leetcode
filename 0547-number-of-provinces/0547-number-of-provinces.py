class Solution:
    def dfs(self, isConnected: List[List[int]], u: int, color: List) -> None:
        color[u] = 1
        for v in range(0,len(isConnected[u])):
            if isConnected[u][v] == 1:
                if color[v] == 0:
                    self.dfs(isConnected, v, color)
        color[u] = 2
        
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        k: int = 0
        n: int = len(isConnected)
        color: list = [0]*n
        for u in range(0, n):
            if color[u] == 0:
                k = k+1
                self.dfs(isConnected, u, color)
        return k
