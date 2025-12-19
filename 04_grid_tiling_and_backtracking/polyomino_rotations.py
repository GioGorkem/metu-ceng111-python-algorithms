base_shapes = {"I": [(0,0), (1,0), (2,0), (3,0)], "J": [(0,0), (-1,0), (-2,0), (-2,-1)], "L": [(0,0), (1,0), (2,0), (2,-1)], 
                   "T": [(0,0), (0,1), (-1,1), (1,1)], "O": [(0,0), (1,0), (0,1), (1,1)], "S": [(0,0), (1,0), (1,-1), (2,-1)],
                    "Z": [(0,0), (1,0), (0,-1), (-1,-1)], "K": [(0,0)]}
shapes = {} 
    
for name in base_shapes: 
        current_shape = base_shapes[name]
        rotations = [] 
        for _ in range(4):
            current_shape.sort()
            if current_shape not in rotations:
                rotations.append(current_shape)
            new_shape = []
            for point in current_shape:
                x = point[0]
                y = point[1]
                new_shape.append((-y, x))
            current_shape = new_shape
        shapes[name] = rotations
print(shapes)
