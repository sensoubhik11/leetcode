class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indeg = [0]*numCourses
        adj_list = defaultdict(list)
        for a, b in prerequisites:
            adj_list[b].append(a)
            indeg[a] += 1
        queue = deque([i for i,v in enumerate(indeg) if v == 0])
        cnt = 0
        while queue:
            u = queue.popleft()
            cnt += 1
            for v in adj_list[u]:
                indeg[v] -= 1
                if indeg[v] == 0:
                    queue.append(v)
        return cnt == numCourses
