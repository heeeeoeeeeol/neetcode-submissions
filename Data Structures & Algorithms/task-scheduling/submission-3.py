class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        d = {}
        for task in tasks: d[task] = d.get(task, 0) + 1
        heap = list(d.values())
        heapq.heapify_max(heap)

        idle = (heap[0]-1)*n
        for i in range(1, len(heap)):
            idle -= min(heap[0]-1, heap[i])

        return max(0, idle) + len(tasks)