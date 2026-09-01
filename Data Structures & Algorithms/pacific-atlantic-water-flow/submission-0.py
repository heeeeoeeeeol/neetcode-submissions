class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        def dfs(r,c,s,prev):
            if r<0 or r>=len(heights) or c<0 or c>=len(heights[0]) or (r,c) in s or heights[r][c] < prev: return
            s.add((r,c))
            dfs(r-1,c,s,heights[r][c])
            dfs(r+1,c,s,heights[r][c])
            dfs(r,c-1,s,heights[r][c])
            dfs(r,c+1,s,heights[r][c])

        res, pa, at = [], set(), set()

        for r in range(len(heights)): dfs(r,0,pa,-1)
        for c in range(len(heights[0])): dfs(0,c,pa,-1)

        for r in range(len(heights)): dfs(r,len(heights[0])-1,at,-1)
        for c in range(len(heights[0])): dfs(len(heights)-1,c,at,-1)

        for p in pa: 
            if p in at: res.append([p[0],p[1]])
        return res


        