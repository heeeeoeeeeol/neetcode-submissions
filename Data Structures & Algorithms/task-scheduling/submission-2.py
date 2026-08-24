class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        d = {}
        for task in tasks: d[task] = d.get(task, 0) + 1
        heap = list(d.values())
        heapq.heapify_max(heap)

        q = deque()
        time = 0
        while heap or q:
            if q and time >= q[0][0]: 
                heapq.heappush_max(heap, q.popleft()[1])
            elif not heap:
                time = q[0][0]
                continue
            t = heapq.heappop_max(heap) - 1
            time += 1
            if t: q.append((time+n, t))

        return time
            


