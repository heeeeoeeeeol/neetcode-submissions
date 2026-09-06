class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = defaultdict(list)
        cost = [[sys.maxsize]*(k+2) for _ in range(n)]
        for s, d, c in flights: adj[s].append((d,c))
        heap = [(0,src,k)]

        while heap:
            tot, v, kc = heapq.heappop(heap)
            if kc < -1 or cost[v][kc] <= tot: continue
            cost[v][kc] = tot
            if v == dst: return tot
            for d,c in adj[v]:
                heapq.heappush(heap,(tot+c,d,kc-1))
        return -1

            
