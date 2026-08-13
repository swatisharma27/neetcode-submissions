class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        m = len(matrix) ## no of rows
        n = len(matrix[0]) ## no of columns

        low = 0
        high = m*n - 1

        while low <= high:
            mid = low + (high-low)//2

            # Convert 1-D index to 2-D index
            row = mid // n
            column = mid % n

            if matrix[row][column] == target:
                return True
            elif matrix[row][column] > target:
                high = mid - 1
            else:
                low = mid + 1

        return False
