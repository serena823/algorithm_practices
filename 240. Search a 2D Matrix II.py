class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if len(matrix) == 0:
            return False
        
        row = len(matrix)
        column = len(matrix[0])
     
        i, j = row - 1, 0
        
        while i >= 0 and j < column:
            if matrix[i][j] == target:  
                return True
            elif matrix[i][j] < target:
                j += 1
            elif matrix[i][j] > target:
                i -= 1
        return False
        
        
        