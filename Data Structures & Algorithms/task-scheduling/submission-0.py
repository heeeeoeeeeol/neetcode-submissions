class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        d = {}

        for task in tasks:
            d[task] = d.get(task, 0) + 1

        heap = []
        for key in d.keys():
            heapq.heappush_max(heap, d[key])

        q = deque()
        time = 0
        while heap or q:
            if not heap:
                if time >= q[0][0]: heapq.heappush_max(heap, q.popleft()[1])
                else: 
                    time += 1
                    continue
            t = heapq.heappop_max(heap) - 1
            if t: q.append((time+n+1, t))
            time += 1

        return time
            


