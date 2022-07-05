class Solution(object):
    def checkXMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: bool
        """
        rows=len(grid)
        col=len(grid[0])
        for i in range (rows):
                for j in range(col):
                        if i==j or i+j==col-1:
                                if grid[i][j] == 0:
                                        return False
                        else:
                                if grid[i][j] != 0:
                                        return False
        return True
   
                                
                         
