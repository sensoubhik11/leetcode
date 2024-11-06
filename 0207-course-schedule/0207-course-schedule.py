class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        n = numCourses
        mat = [[0]*n for _ in range(n)]

        for row in prerequisites:
            mat[row[1]][row[0]] = 1
        flag = True
        def dfs_visit(i, tags):
            nonlocal flag
            tags[i] = 1
            for j in range(n):
                if mat[i][j]:
                    if tags[j] == 0:
                        dfs_visit(j, tags)
                    elif tags[j] == 1:
                        flag = False
                        break
            tags[i] = 2

        def dfs(n):
            tags = [0]*n
            for i in range(n):
                if tags[i] == 0:
                    dfs_visit(i,tags)
        dfs(n)
        return flag