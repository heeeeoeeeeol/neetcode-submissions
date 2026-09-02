class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:  
        numPre = [0]*numCourses
        adj = [[] for _ in range(numCourses)]

        for a, b in prerequisites:
            numPre[a] += 1
            adj[b].append(a)

        q = deque()
        for i in range(len(numPre)):
            if numPre[i] == 0: q.append(i)

        finished = 0
        res = []
        while q:
            p = q.popleft()
            res.append(p)
            finished += 1
            for cls in adj[p]: 
                numPre[cls] -= 1
                if not numPre[cls]: 
                    q.append(cls)

        return res if finished == numCourses else []