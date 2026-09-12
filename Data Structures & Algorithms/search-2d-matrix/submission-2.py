class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        N = m*n

        low = 0
        high = N-1

        while low <= high:

            mid = low + (high-low)//2

            row = mid // n # as after four columns we have the next row as per example
            column = mid % n

            if matrix[row][column] == target:
                return True
            elif matrix[row][column] > target:
                high = mid - 1
            else:
                low = mid + 1
        
        return False

                
