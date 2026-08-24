class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        start, end = 0, len(matrix)*len(matrix[0])-1

        while start <= end: 
            mid = (start+end)//2
            midr = mid // len(matrix[0])
            midc = mid % len(matrix[0])
            if matrix[midr][midc] > target: end = mid-1
            elif matrix[midr][midc] < target: start = mid+1  
            else: return True

        return False
