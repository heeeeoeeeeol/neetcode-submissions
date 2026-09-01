class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        offset = [(-1,0),(1,0),(0,-1),(0,1)]
        def bfs(q,s):
            while q:
                r,c = q.popleft()
                s.add((r,c))
                for x,y in offset:
                    if 0<=r+y<len(heights) and 0<=c+x<len(heights[0]) and (r+y,c+x) not in s and heights[r+y][c+x] >= heights[r][c]:
                        q.append((r+y,c+x))
        
        res, q, pa, at = [], deque(), set(), set()

        for r in range(len(heights)): q.append((r,0))
        for c in range(len(heights[0])): q.append((0,c))
        bfs(q, pa)
        for r in range(len(heights)): q.append((r,len(heights[0])-1))
        for c in range(len(heights[0])): q.append((len(heights)-1,c))
        bfs(q, at)

        for p in pa: 
            if p in at: res.append([p[0],p[1]])
        return res






                


