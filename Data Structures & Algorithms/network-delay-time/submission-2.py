class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for i in times: adj[i[0]].append(i)
        heap = []       
        heapq.heappush(heap, (0, k)) 

        res, vis = 0, set()
        while heap:
            time, node = heapq.heappop(heap)
            if node in vis: continue
            res = time
            vis.add(node)
            for e in adj[node]: 
                heapq.heappush(heap, (time+e[2], e[1]))

        return res if len(vis) == n else -1



