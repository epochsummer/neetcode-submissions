class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) == 0:
            return False
        
        row_number = len(matrix)
        column_number = len(matrix[0])

        left = 0
        right = row_number * column_number - 1

        while left <= right:
            middle = (left + right) // 2

            middle_row = middle // column_number
            middle_column = middle % column_number

            value = matrix[middle_row][middle_column]

            if value > target:
                right = middle - 1
            elif value < target:
                left = middle + 1
            else:
                return True
            
        return False



        
        