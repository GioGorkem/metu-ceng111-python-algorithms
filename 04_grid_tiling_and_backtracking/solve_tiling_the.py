def solve_tiling(grid_height, grid_width, pieces_list):
    shapes = {
        'K': [[(0, 0)]],
        'I': [[(0, 0), (1, 0), (2, 0), (3, 0)], [(0, 0), (0, 1), (0, 2), (0, 3)]],
        'O': [[(0, 0), (1, 0), (0, 1), (1, 1)]],
        'T': [[(0, 0), (1, 0), (2, 0), (1, 1)], [(0, 0), (0, 1), (0, 2), (1, 1)],
              [(0, 0), (1, 0), (2, 0), (1, -1)], [(0, 0), (0, 1), (0, 2), (-1, 1)]],
        'L': [[(0, 0), (0, 1), (0, 2), (1, 2)], [(0, 0), (1, 0), (2, 0), (2, -1)],
              [(0, 0), (1, 0), (0, 1), (0, 2)], [(0, 0), (1, 0), (2, 0), (0, 1)]],
        'J': [[(1, 0), (1, 1), (1, 2), (0, 2)], [(0, 0), (0, 1), (1, 1), (2, 1)],
              [(0, 0), (1, 0), (0, 1), (0, 2)], [(0, 0), (1, 0), (2, 0), (2, 1)]],
        'S': [[(0, 0), (1, 0), (1, -1), (2, -1)], [(0, 0), (0, 1), (1, 1), (1, 2)]],
        'Z': [[(0, 0), (1, 0), (1, 1), (2, 1)], [(1, 0), (0, 1), (1, 1), (0, 2)]]
    }

    grid = []
    for _ in range(grid_height):
        row = [0] * grid_width
        grid.append(row)

    used = [False] * len(pieces_list)
    result = [None] * len(pieces_list)

    def solve():
        empty_x = -1
        empty_y = -1
        found = False
        
        for y in range(grid_height):
            for x in range(grid_width):
                if grid[y][x] == 0:
                    empty_x = x
                    empty_y = y
                    found = True
                    break
            if found: break
        
        if not found:
            for u in used:
                if u == False: return False
            return True

        for i in range(len(pieces_list)):
            if used[i] == False:
                name = pieces_list[i]
                if name not in shapes: continue
                
                rotations = shapes[name]
                for shape in rotations:
                    can_place = True
                    for point in shape:
                        nx = empty_x + point[0]
                        ny = empty_y + point[1]
                        
                        if nx < 0 or nx >= grid_width or ny < 0 or ny >= grid_height:
                            can_place = False
                            break
                        if grid[ny][nx] != 0:
                            can_place = False
                            break
                    
                    if can_place:
                        for point in shape:
                            nx = empty_x + point[0]
                            ny = empty_y + point[1]
                            grid[ny][nx] = 1
                        
                        used[i] = True
                        result[i] = (name, empty_x, empty_y)
                        
                        if solve():
                            return True
                        
                        for point in shape:
                            nx = empty_x + point[0]
                            ny = empty_y + point[1]
                            grid[ny][nx] = 0
                        used[i] = False
                        result[i] = None
        return False

    if solve():
        return result
    else:
        return None
print(solve_tiling(4, 10, [ 'J', 'J', 'L', 'L', 'I', 'I', 'I', 'I', 'O', 'O']))



        
