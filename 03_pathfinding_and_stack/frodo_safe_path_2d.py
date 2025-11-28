# Stack Implementation as required by the assignment
def CreateStack(): return []
def Push(item, Stack): Stack.append(item)
def Pop(Stack): return Stack.pop()
def Top(Stack): return Stack[-1]
def IsEmpty(Stack): return len(Stack) == 0

def safe_path(grid):
    rows = len(grid)
    cols = len(grid[0])
    start_point = None

    # Find Frodo's starting position
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == "F":
                start_point = (i, j)
                break
        if start_point:
            break
            
    if not start_point:
        return []

    stack = CreateStack()
    # Stack stores: (row, col, list of moves to get here, set of visited nodes)
    Push((start_point[0], start_point[1], [], {start_point}), stack)
    
    # Directions: row_change, col_change, "direction_name"
    directions = [
        (-1, 0, "north"), 
        (0, 1, "east"),   
        (1, 0, "south"),  
        (0, -1, "west")   
    ]

    while not IsEmpty(stack):
        curr_r, curr_c, current_path, visited = Pop(stack)

        # If we reached Mount Doom, return the path
        if grid[curr_r][curr_c] == "M":
            return current_path

        # Try all 4 directions
        for dr, dc, dir_name in directions:
            next_r = curr_r + dr
            next_c = curr_c + dc

            # Check boundaries
            if 0 <= next_r < rows and 0 <= next_c < cols:
                # Check if it's safe (not an Orc "O") and not visited in this path
                if grid[next_r][next_c] != "O" and (next_r, next_c) not in visited:
                    
                    # Create new path and visited set for the next step
                    new_path = current_path + [dir_name]
                    new_visited = visited.copy()
                    new_visited.add((next_r, next_c))
                    
                    # Push the valid next step to the stack
                    Push((next_r, next_c, new_path, new_visited), stack)

    # If the stack is empty and "M" wasn't found
    return []

# --- Test Cases ---
if __name__ == "__main__":
    print(safe_path([["O", "", "", "M"], ["", "O", "", ""], ["F", "", "", "O"]]))
    print(safe_path([["O", "", "", "M"], ["", "O", "", ""], ["F", "", "O", "O"]]))