class Solution:
    def binary_search(self, matrix, target, low, high):
        if low <= high:
            mid = low + (high-low)//2
            mid_i = mid//len(matrix[0])
            mid_j = mid%len(matrix[0])
            if matrix[mid_i][mid_j] == target:
                return True
            elif target < matrix[mid_i][mid_j]:
                return self.binary_search(matrix, target, low, mid-1)
            return self.binary_search(matrix, target, mid+1, high)
        return False
        
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        return self.binary_search(matrix, target, 0, m*n-1)