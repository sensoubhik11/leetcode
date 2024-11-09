class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        cnt = 0
        # 0 for not visited, 1 = visited but still exploring, 2 = fully explored
        visited = [0]*len(isConnected)
        def dfs(u):
            visited[u] = 1
            for v in range(len(isConnected[u])):
                if isConnected[u][v] == 1 and visited[v] == 0:
                    dfs(v)
            visited[u] = 2
        for u in range(len(isConnected)):
            if visited[u] == 0:
                cnt += 1
                dfs(u)
        return cnt
