def deploy_drones(grid, k):

    def solve():
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 0:
                    if is_safe(grid, row, col):
                        grid[row][col] += 2
                        return True

    def is_safe(grid, row, col):
        # köşe durumlar
        # sol üst köşe
        if row == 0 and col == 0:
            if grid[row][col+1] == 2 or grid[row+1][col] == 2:
                return False
        # sağ üst köşe
        if row == 0 and col == len(grid[0]):
            if grid[row][col-1] == 2 or grid[row+1][col] == 2:
                return False
        # sol alt köşe
        if row == len(grid) and col == 0:
            if grid[row][col+1] == 2 or grid[row-1][col] == 2:
                return False
        #sağ alt köşe
        if row == len(grid) and col == len(grid[0]):
            if grid[row][col-1] == 2 or grid[row-1][col] == 2:
                return False
        #üst kenarda olabilir
        elif row == 0:
            if grid[row][col-1] == 2 and grid[row][col+1] == 2 and grid[row+1][col] == 2:
                return False
        #alt kenarda olabilir
        elif row == len(grid):
            if grid[row][col-1] == 2 and grid[row][col+1] == 2 and grid[row-1][col] == 2:
                return False
        # sol kenarda olabilir
        elif col == 0:
            if grid[row][col+1] == 2 and grid[row+1][col] == 2 and grid[row-1][col] == 2:
                return False   
        #sağ kenarda olabilir
        elif col == 0:
            if grid[row][col-1] == 2 and grid[row+1][col] == 2 and grid[row-1][col] == 2:
                return False  
        # ortalarda bir yerde olabilir
        elif row != 0 and row != len(grid) and col != 0 and col != len(grid[0]):
            if grid[row][col-1] == 2 and grid[row][col+1] == 2 and grid[row-1][col] == 2 and grid[row+1][col] == 2:
                return False  
        else:
            return True





    if solve():
        return grid
    else:
        return None
    
grid = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]
k = 4
print(deploy_drones(grid,k))