class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        d = defaultdict(list)
        for i in times: d[i[0]].append(i)
        time = [sys.maxsize]*n

        def dfs(node, t):
            if t >= time[node-1]: return
            time[node-1] = min(time[node-1], t)              
            for e in d[node]: dfs(e[1], t+e[2])

        dfs(k, 0)
        return max(time) if max(time) != sys.maxsize else -1