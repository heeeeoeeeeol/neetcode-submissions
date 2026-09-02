class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        d = defaultdict(list)
        for p in prerequisites: d[p[0]].append(p[1])

        def dfs(i, vis):            
            if i not in d: return True
            if i in vis: 
                print(i)
                return False
            vis.add(i)
            for p in d[i]:
                if not dfs(p, vis): 
                    return False
                vis.discard(p)
                d.pop(p, None)
            return True

        for i in range(numCourses):
            if not dfs(i, set()): 
                return False
        return True
                
        

        

        