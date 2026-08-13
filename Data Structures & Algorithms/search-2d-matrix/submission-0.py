class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        TC: O(log m*n)
        SC: O(1)
        """
        m = len(matrix)
        n = len(matrix[0])
        
        low = 0
        high = m*n - 1

        while low <= high:
            mid = low + (high-low)//2

            row = mid // n 
            column = mid % n

            if matrix[row][column] == target:
                return True

            elif matrix[row][column] < target:
                low = mid + 1

            else:
                high = mid - 1
                

        return False