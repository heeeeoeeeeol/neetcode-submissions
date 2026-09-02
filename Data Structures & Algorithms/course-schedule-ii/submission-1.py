class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preq = [0]*numCourses
        adj = [[] for _ in range(numCourses)]

        for a, b in prerequisites:
            preq[a] += 1
            adj[b].append(a)

        q = deque()
        for i in range(numCourses):
            if not preq[i]: q.append(i)

        fin, res = 0, []
        while q:
            p = q.popleft()
            res.append(p)
            fin += 1

            for a in adj[p]:
                preq[a] -= 1
                if not preq[a]: q.append(a)

        return res if fin==numCourses else []