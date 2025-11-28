def CreateStack():
    return []
def Push(item, Stack):
    Stack.append(item)
def Pop(Stack):
    return Stack.pop()
def Top(Stack):
    return Stack[-1]
def IsEmpty(Stack):
    return Stack == []


def solve_titan_protocol(grid):
    layers = len(grid)
    rows = len(grid[0])
    cols = len(grid[0][0])
    for l in range(layers):
        for r in range(rows):
            for c in range(cols):
                if grid[l][r][c] == "S":
                    start_point = (l, r, c)
                    break
    
    stack = CreateStack()
    # push (current layer, current row, current col, move index, has mask, path)
    Push((start_point[0], start_point[1], start_point[2], 0, 0, [(start_point[0], start_point[1], start_point[2], 0)]), stack)
    directions = [(0,0,1), (0,1,0), (0,0,-1), (0,-1,0), (1,0,0), (-1,0,0)]
    while not IsEmpty(stack):
        curr_l, curr_r, curr_c, mv_idx, has_mask, path = Top(stack)
        if grid[curr_l][curr_r][curr_c] == "E":
            return get_directions(path)
        found = False
        for i in range(mv_idx, 6):
            dl, dr, dc = directions[i]
            next_l, next_r, next_c = curr_l + dl, curr_r + dr, curr_c + dc
            if 0 <= next_l < layers and 0 <= next_r < rows and 0 <= next_c < cols:
                next_has_max = has_mask
                if grid[next_l][next_r][next_c] == "M":
                    next_has_max = 1 
                can_pass = True
                if dl == 1 and grid[curr_l][curr_r][curr_c] != "U":
                    can_pass = False
                if dl == -1 and grid[curr_l][curr_r][curr_c] != "D":
                    can_pass = False
                if not next_has_max and grid[next_l][next_r][next_c] == "G":
                    can_pass = False
                if grid[next_l][next_r][next_c] == "1":
                    can_pass = False
                if (next_l, next_r, next_c, next_has_max) in path:
                    can_pass = False
                if can_pass:
                    Pop(stack)
                    Push((curr_l, curr_r, curr_c, i + 1, has_mask, path), stack)
                    Push((next_l, next_r, next_c, 0, next_has_max, path + [(next_l, next_r, next_c, next_has_max)]), stack)
                    found = True
                    break
        if not found:
            Pop(stack)
    return []

def get_directions(path):
    result = []
    for i in range(len(path)-1):
        f_l, f_r, f_c, f_m = path[i]
        s_l, s_r, s_c, s_m = path[i+1]

        dl, dr, dc = s_l - f_l, s_r - f_r, s_c - f_c
        
        if dl == 1:
            result.append("up")
        elif dl == -1:
            result.append("down")
        elif dr == 1:
            result.append("south")
        elif dr == -1:
            result.append("north")
        elif dc == 1:
            result.append("east")
        elif dc == -1:
            result.append("west")
    return result

def run_test(case_name, grid, description):
    print(f"\n--- {case_name} ---")
    print(f"Senaryo: {description}")
    
    path_dirs = solve_titan_protocol(grid)
    
    if path_dirs:
        print(f"SONUÇ: Rota Bulundu! ({len(path_dirs)} adım)")
        print(f"Hareketler: {path_dirs}")
    else:
        print("SONUÇ: Rota Bulunamadı.")

# ---------------------------------------------------------

# CASE 1: ASANSÖR KULLANIMI (Temel 3D)
# Kat 0'da S var, Kat 1'de E var.
# S -> 'U' karesine git -> Yukarı Çık -> E'ye git.
grid1 = [
    # Kat 0
    [['S', '0', 'U'], 
     ['1', '1', '1']], 
    # Kat 1
    [['1', '1', '0'], 
     ['1', '1', 'E']]
]
# Yol: East -> East (U'ya geldi) -> Up (Kat 1'e çıktı) -> South -> East (E'ye geldi).
run_test("Test 1: Kata Çıkış", grid1, "Sadece 'U' karesinden yukarı çıkılabilir.")


# CASE 2: MASKE GEREKSİNİMİ (State + 3D)
# E'ye giden yol Gaz ('G') ile dolu.
# Önce alt kata inip ('D'), maskeyi ('M') alıp, tekrar yukarı çıkıp ('U'), gazın içinden geçmelisin.
grid2 = [
    # Kat 0 (Zemin)
    [['M', '0', 'U'],  # Maske burada. U ile yukarı çıkılır.
     ['1', '1', '1']],
    
    # Kat 1 (Başlangıç ve Hedef burada)
    [['S', 'D', '1'],  # S burada. Yanında D var (aşağı inmek için).
     ['G', 'G', 'E']]  # Hedefe giden yol Gazlı.
]
# Yol: 
# 1. East (D'ye git)
# 2. Down (Kat 0'a in, (0,1) noktasına)
# 3. West (M'ye git, Maskeyi al!)
# 4. East -> East (U'ya git)
# 5. Up (Kat 1'e geri çık, (1,2) noktasına)
# 6. South (E'ye git - Gaz olmasına rağmen girebilirsin çünkü masken var)
run_test("Test 2: Maske Operasyonu", grid2, "Maske için alt kata inip geri gelmek gerekiyor.")


# CASE 3: YANLIŞ RAMPA
# Yukarı çıkmak istiyorsun ama yanında sadece 'D' (Aşağı inen rampa) var.
# Yukarı çıkamazsın, yol yok dönmeli.
grid3 = [
    [['S', 'D']], # Kat 0: Yanında D var ama alt kat yok (z-1 yok).
    [['E', '0']]  # Kat 1: Hedef burada.
]
# 'D' sadece aşağı indirir. Kat -1 olmadığı için hareket edemez. Yukarı da çıkamaz çünkü 'U' yok.
run_test("Test 3: Bozuk Asansör", grid3, "D karesi yukarı çıkarmaz, U karesi aşağı indirmez.")