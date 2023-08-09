class Solution(object):
    def dfs(self,x,y,grid):
        row = len(grid)
        col = len(grid[0])
        if x <=-1 or y <=-1 or x>= row or y >= col:
            return False
        if grid[x][y]=="1":
            grid[x][y]="0"
            self.dfs(x-1,y,grid)
            self.dfs(x+1,y,grid)
            self.dfs(x,y-1,grid)
            self.dfs(x,y+1,grid)
            return True
        return False
        
    def numIslands(self, grid):
        row = len(grid)
        col = len(grid[0])
        count =0
        for i in range(row):
            for j in range(col):
                if self.dfs(i,j,grid)==True:
                    count+=1
        return count
        
       
                